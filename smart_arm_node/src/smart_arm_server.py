#!/usr/bin/env python
#from __future__ import division

# Basics
import ipdb
import roslib
roslib.load_manifest('smart_arm_node')
import rospy

# ROS messages
from std_msgs.msg import Float64, Bool, Float64MultiArray
from dynamixel_msgs.msg import JointState, MotorStateList
from smart_arm_node.msg import Float64List
from smart_arm_node.srv import SmartArmService, SmartArmServiceResponse
import tf

# Maths
from numpy import pi, arctan2, cos, sin, array, sqrt, arccos, eye, array, dot, zeros

# Time
from time import sleep



################################################################################
def ask_server(req):
    """
    Accepts external requests about status and movements, depending on the
    'req.what' value.
        1 : joint status
        2 : move the four first joints to desired joint angles
        3 : move the four first joints to desired (x,y,z) using IK solver
        4 : grab/ungrab with the hand
    Data should be provided for some of the requests.
    A response according to what is accomplished is retured.
    """
    if req.what == 1:
        # joint status
        ans = list(joints_curr)
    elif req.what == 2:
        # move radians
        qs = list(req.data)
        ans = [arm.move_all(qs),]
    elif req.what == 3:
        # move xyz
        xyz = list(req.data)
        ans = [arm.move_xyz(xyz),]
    elif req.what == 4:
        # grab/ungrab
        ans = [arm.grab(),]
    else:
        # no valid request
        print 'no valid request\n'
        ans = [0,]

    return SmartArmServiceResponse(ans)
        


################################################################################
def angle_wrap(a):
    '''
    Retruns the angle a normalized between -pi and pi
    '''
    if a > pi :
        a -= 2*pi
    elif a < -pi :    
        a += 2*pi
    return a
    
    
    
################################################################################
def check_j1(msg):
    check_joint(1,msg)
def check_j2(msg):
    check_joint(2,msg)
def check_j3(msg):
    check_joint(3,msg)
def check_j4(msg):
    check_joint(4,msg)
def check_j5(msg):
    check_joint(5,msg)
    
    
    
################################################################################
def check_joint(i,msg):
    '''
    Checks if a joint is still moving and also if the torque is too big and the
    movement should be stopped.
    '''

    joints_move[i-1] = msg.is_moving
    joints_load[i-1] = abs(msg.load) > 0.8
    joints_curr[i-1] = msg.current_pos
    
    # Publish transformations for the joints (1-4), not the hand (5)
    if i < 5:
        # Get transformation between the joint and previous joint
        parent = "joint%s" % str(i-1)
        child  = "joint%s" % str(i)
        trans  = arm.links[i-1].tr(joints_curr[i-1])
        # Broadcast tf [translation (x,y,z), rotation (x,y,z,w), time, child, parent]
        tfbr.sendTransform(tf.transformations.translation_from_matrix(trans),
                           tf.transformations.quaternion_from_matrix(trans),
                           rospy.Time.now(),
                           child,
                           parent)
    
    if joints_load[i-1] and i==5:
        print 'Too much load on joint %s\nStopping joint...' % i
        print 'Load = ', msg.load
        pub_move[i-1].publish(msg.current_pos)
    
    
    
################################################################################
def get_arm_limits():
    '''
    Obtains the limits for each joint from the parameter server
    of the "smart_arm_controller"
    '''
    # Names of the parameters to get
    tic2rad = rospy.get_param('/dynamixel/smart_arm/6/radians_per_encoder_tick')
    joints = ['/shoulder_pan_controller','/shoulder_pitch_controller',
              '/elbow_flex_controller', '/wrist_roll_controller', '/right_finger_controller']
    motors = ['/motor',] + ['/motor_master',]*2 + ['/motor',]*2
    
    # Initialization
    qlims = zeros((5,2))
    
    # Get parameters
    for i in range(len(joints)):
        vini = rospy.get_param(joints[i] + motors[i] + '/init')
        vmax = rospy.get_param(joints[i] + motors[i] + '/max')
        vmin = rospy.get_param(joints[i] + motors[i] + '/min')
        qlims[i,0] = -abs(vmin-vini)*tic2rad # minimum
        qlims[i,1] = +abs(vmax-vini)*tic2rad # maximum
    
    return qlims
    
    
    
################################################################################
class Link(object):
    '''
    Class to handle revoution links defined with DH method.
    '''
    
    def __init__(self,theta,d,a,alpha,offset):
        '''
        Constructor of the class link.
        theta,d,a,alpha : defined by DH method.
        offset          : difference between the real zero of the joint motors
                          and the theoric zero.
        '''
        self.theta = theta
        self.d = d
        self.a = a
        self.alpha = alpha
        self.offset = offset
        
        
        
    def tr(self,q=0):
        '''
        Returns the forward kinematics matrix of the link at the especified
        theta (q) value.
        '''
        q = q + self.offset    # correct offset
        sa = sin(self.alpha)
        ca = cos(self.alpha)
        st = sin(q)
        ct = cos(q)
        d = self.d
        a = self.a
        val = array([[ct, -ca*st,  sa*st, a*ct],
                     [st,  ca*ct, -sa*ct, a*st],
                     [ 0,     sa,     ca,    d],
                     [ 0,      0,      0,    1]])
        return val



################################################################################ 
class Arm(object):
    '''
    Class to handle the whole arm of the robot with forward kinematics and
    inverse kinematics.
    '''
    
    def __init__(self,links):
        '''
        Constructor of the arm with the specified list of links.
        '''
        assert isinstance(links,list)
        self.links = links
        
    
    
    def fkine(self,qs):
        '''
        Returns the forward kinematics matrix for all joints
        '''
        assert len(qs)>=4
        val = eye(4)
        for i in range(4):
            val = dot(val, self.links[i].tr(qs[i]))
        return val


        
    def ikine(self,xyz):
        '''
        Returns the inverse kinematics (list of joint positions) to achieve a
        (x,y,z) position on the end effector.
        '''
        # Input/output variables
        x,y,z = xyz          # goal position
        sols = zeros((4,5))  # 4 solutions obtained with IK
        
        # Inverse kinematics
        ## Joint 1
        q1 = arctan2(y,x)
        sols[0,0] = q1
        sols[1,0] = q1
        sols[2,0] = q1 + pi
        sols[3,0] = q1 + pi
        
        ## Joints 2&3 when q1
        e = sqrt(x**2 + y**2)
        f = sqrt((e-a1)**2 + (d1-z)**2)
        g = sqrt(d4**2 + a3**2)
        h = arctan2(d1-z,f)
        q3 = arccos((f**2 - a2**2 - g**2)/(2*a2*g))
        sols[0,2] = q3
        sols[0,1] = arctan2(g*sin(q3), a2+g*cos(q3)) + h
        q3 = 2*pi - q3
        sols[1,2] = q3
        sols[1,1] = arctan2(g*sin(q3), a2+g*cos(q3)) + h
        
        ## Joints 2&3 when q1+pi
        f = sqrt((e+a1)**2 + (d1-z)**2)
        h = arctan2(d1-z,f)
        q3 = arccos((f**2 - a2**2 - g**2)/(2*a2*g))
        sols[2,2] = q3
        sols[2,1] = pi - (arctan2(g*sin(q3), a2+g*cos(q3)) + h)
        q3 = 2*pi - q3
        sols[3,2] = q3
        sols[3,1] = pi - (arctan2(g*sin(q3), a2+g*cos(q3)) + h)
        
        # Check solutions
        print 'Target: %s, %s, %s' % (x,y,z)
        for i in range(4):        # for all solutions
        
            ## Check solution with joint limits
            for j in range(4):    # for all joints
                sols[i,j] = angle_wrap(sols[i,j])
                if not( min(qlims[j,:]) <= sols[i,j] <= max(qlims[j,:]) ):
                    sols[i,4] = 1 # no valid solution
                    break
                    
            ## Check solution with FK
            trans = self.fkine(sols[i,:4])[:3,3]
            if sqrt( sum( ( trans-array([x,y,z]) )**2 ) ) > 0.01: 
                sols[i,4] = 1     # no valid solution
            
            ## Some output   
            print 'Solution %s: ' % i, trans
            print 'Rejected: ', sols[i,4]
            print 'Error: ', sqrt( sum( ( trans-array([x,y,z]) )**2 ) )
            print 'Joints: ', sols[i,0:4], '\n'
        
        print 'found %s solutions' % sum(sols[:,4]==0)
        
        # If more than one solution, take the nearest to curent one
        ipdb.set_trace()
        #TODO: check offset interaction here!!!!
        return 1
    
    
    
    def grab(self,auto=True):
        """
        Grabs or ungrabs depending on the joint state.
        """
        # TODO: check better the movement
        # Check condition
        if abs(joints_curr[4]-qlims[4,0]) < 0.1 and auto:
            val = +1 # close
        else:
            val = -1 # open
            
        # Publish to controller
        pub_move[4].publish(Float64(val))
            
        # Wait until movement end
        while sum(joints_move) > 0:
            sleep(0.1)
            
        return 1
        
    
    
    def move_all(self,qs):
        '''
        Moves the arm to the specified joint positions.
        '''
        assert len(qs) >= 4
        
        # Send movement commands to the smart_arm_controller (not the hand)
        for i in range(4):
            pub_move[i].publish(Float64(qs[i]))
            
        # Wait until finish movement
        while sum(joints_move) > 0:
            sleep(0.1)
        
        # Check if the goal is reached
        cond = abs( array(joints_curr[:4]) - array(qs) ) < 0.05
        if sum(cond) == 4:
            return 1
        else:
            return 0
            
            
            
    def move_joint(i,q):
        '''
        Moves the specified joint "i" to the specified position "q".
        '''
        assert i<5
        pub_move[i-1].publish(Float64(qs))
        
        # Wait until finish movement
        while sum(joints_move) > 0:
            sleep(0.1)
        
        # Check if the goal is reached
        cond = abs( array(joints_curr[:4]) - array(qs) ) < 0.05
        if sum(cond) == 4:
            return 1
        else:
            return 0
        
        
        
    def move_xyz(self,xyz):
        '''
        Moves the arm to specified (x,y,z) position of the end effector, using
        the inverse kinematics solution.
        '''
        qs = self.ikine(xyz)
        return self.move_all(qs)
        
        
        
    def tf(self,i,q=0,pub=False):
        '''
        Gets the transformation from one joint. Also publishes the
        transformation if it is specified.
        '''
        trans = self.links[i-1].tr(q)
        
        if pub:
            parent = "joint%s" % str(i-1)
            child  = "joint%s" % str(i)
            # Broadcast tf [translation (x,y,z), rotation (x,y,z,w), time, child, parent]
            tfbr.sendTransform(tf.transformations.translation_from_matrix(trans),
                               tf.transformations.quaternion_from_matrix(trans),
                               rospy.Time.now(),
                               child,
                               parent)
        return trans



    def tf_all(self,qs):
        '''
        Publishes the transformations for all joints.
        '''
        for i in range(4):
            self.tr(i+1,qs[i],True)
        return 1



################################################################################
# Default values
qlims = array([[-1.22207136,1.22207136],[-1.04822021,1.97372195],[-1.88679637,1.97372195],
               [-2.61288061,2.61799388],[-0.24032366,0.84368943]])

# Control of the joint status initialization
joints_move = [False,]*5
joints_load = [False,]*5
joints_curr = [0,]*5


                    
################################################################################
####################            MAIN            ################################
################################################################################
if __name__ == '__main__':
    # Initialize ROS node
    rospy.init_node('smart_arm_server')#, anonymous=True)
    rospy.loginfo('smart_arm_server initialized')
    
    # Publishers
    ## To controller
    pub_j1 = rospy.Publisher("/shoulder_pan_controller/command",   Float64)
    pub_j2 = rospy.Publisher("/shoulder_pitch_controller/command", Float64)
    pub_j3 = rospy.Publisher("/elbow_flex_controller/command",     Float64)
    pub_j4 = rospy.Publisher("/wrist_roll_controller/command",     Float64)
    pub_j5 = rospy.Publisher("/right_finger_controller/command",   Float64)
    pub_move = [pub_j1, pub_j2, pub_j3, pub_j4, pub_j5]
        
    # Subscribers
    ## From controller
    stat_j1 = rospy.Subscriber('/shoulder_pan_controller/state',   JointState, check_j1)
    stat_j2 = rospy.Subscriber('/shoulder_pitch_controller/state', JointState, check_j2)
    stat_j3 = rospy.Subscriber('/elbow_flex_controller/state',     JointState, check_j3)
    stat_j4 = rospy.Subscriber('/wrist_roll_controller/state',     JointState, check_j4)
    stat_j5 = rospy.Subscriber('/right_finger_controller/state',   JointState, check_j5)
    
    # Transform broadcaster
    tfbr = tf.TransformBroadcaster()
    
    # Services
    srv_values = rospy.Service('get_arm_srv', SmartArmService, ask_server)

    # Get controller limits
    try:
        qlims = get_arm_limits()
        print '# Readed limits from controller:\n', qlims, '\n'
    except: # arm controller not initialized
        print '# Error: No controller found.\nLoading standard joint limits' # TODO:change to rosdebug info
        qlims = array([[-1.22207136,1.22207136],[-1.04822021,1.97372195],[-1.88679637,1.97372195],
                       [-2.61288061,2.61799388],[-0.24032366,0.84368943]])
                       
    # Sizes obtained with DH method
    a1 = 0.051
    a2 = 0.174
    a3 = 0.023
    d1 = 0.14
    d4 = 0.16

    # Link creation
    ## Design parameters
    links = list()
    links.append( Link(    0,  d1, a1, -pi/2,     0) )
    links.append( Link(    0,   0, a2,    pi,     0) ) # offset=-45
    links.append( Link(-pi/2,   0, a3,  pi/2, -pi/2) )
    links.append( Link(   pi, -d4,  0,    pi,    pi) )
    ## Real parameters (offset of the real motors)
    
    # Robot creation
    arm = Arm(links)

    # Forward kinematics
    print '# Forward kinematics test:\n', arm.fkine([0,0,0,0]), '\n'
    print '# Inverse kinematics test:\n', arm.ikine([a1+a2+d4,0,d1-a3])
    ipdb.set_trace()
        
    # Continue execution forever
    rospy.spin()