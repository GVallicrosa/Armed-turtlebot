/* Auto-generated by genmsg_cpp for file /home/user/workspaces/ros/Armed-turtlebot/motionControl/srv/motionControl_backward.srv */
#ifndef MOTIONCONTROL_SERVICE_MOTIONCONTROL_BACKWARD_H
#define MOTIONCONTROL_SERVICE_MOTIONCONTROL_BACKWARD_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "ros/service_traits.h"




namespace motionControl
{
template <class ContainerAllocator>
struct motionControl_backwardRequest_ {
  typedef motionControl_backwardRequest_<ContainerAllocator> Type;

  motionControl_backwardRequest_()
  : linear(0.0)
  , angular(0.0)
  {
  }

  motionControl_backwardRequest_(const ContainerAllocator& _alloc)
  : linear(0.0)
  , angular(0.0)
  {
  }

  typedef double _linear_type;
  double linear;

  typedef double _angular_type;
  double angular;


  typedef boost::shared_ptr< ::motionControl::motionControl_backwardRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::motionControl::motionControl_backwardRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct motionControl_backwardRequest
typedef  ::motionControl::motionControl_backwardRequest_<std::allocator<void> > motionControl_backwardRequest;

typedef boost::shared_ptr< ::motionControl::motionControl_backwardRequest> motionControl_backwardRequestPtr;
typedef boost::shared_ptr< ::motionControl::motionControl_backwardRequest const> motionControl_backwardRequestConstPtr;


template <class ContainerAllocator>
struct motionControl_backwardResponse_ {
  typedef motionControl_backwardResponse_<ContainerAllocator> Type;

  motionControl_backwardResponse_()
  {
  }

  motionControl_backwardResponse_(const ContainerAllocator& _alloc)
  {
  }


  typedef boost::shared_ptr< ::motionControl::motionControl_backwardResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::motionControl::motionControl_backwardResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct motionControl_backwardResponse
typedef  ::motionControl::motionControl_backwardResponse_<std::allocator<void> > motionControl_backwardResponse;

typedef boost::shared_ptr< ::motionControl::motionControl_backwardResponse> motionControl_backwardResponsePtr;
typedef boost::shared_ptr< ::motionControl::motionControl_backwardResponse const> motionControl_backwardResponseConstPtr;

struct motionControl_backward
{

typedef motionControl_backwardRequest Request;
typedef motionControl_backwardResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct motionControl_backward
} // namespace motionControl

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::motionControl::motionControl_backwardRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::motionControl::motionControl_backwardRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::motionControl::motionControl_backwardRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "144a16e4d6b53a0dbadc2e617460a173";
  }

  static const char* value(const  ::motionControl::motionControl_backwardRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x144a16e4d6b53a0dULL;
  static const uint64_t static_value2 = 0xbadc2e617460a173ULL;
};

template<class ContainerAllocator>
struct DataType< ::motionControl::motionControl_backwardRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "motionControl/motionControl_backwardRequest";
  }

  static const char* value(const  ::motionControl::motionControl_backwardRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::motionControl::motionControl_backwardRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "float64 linear\n\
float64 angular\n\
\n\
";
  }

  static const char* value(const  ::motionControl::motionControl_backwardRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::motionControl::motionControl_backwardRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::motionControl::motionControl_backwardResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::motionControl::motionControl_backwardResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::motionControl::motionControl_backwardResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const  ::motionControl::motionControl_backwardResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::motionControl::motionControl_backwardResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "motionControl/motionControl_backwardResponse";
  }

  static const char* value(const  ::motionControl::motionControl_backwardResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::motionControl::motionControl_backwardResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
\n\
";
  }

  static const char* value(const  ::motionControl::motionControl_backwardResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::motionControl::motionControl_backwardResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::motionControl::motionControl_backwardRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.linear);
    stream.next(m.angular);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct motionControl_backwardRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::motionControl::motionControl_backwardResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct motionControl_backwardResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<motionControl::motionControl_backward> {
  static const char* value() 
  {
    return "144a16e4d6b53a0dbadc2e617460a173";
  }

  static const char* value(const motionControl::motionControl_backward&) { return value(); } 
};

template<>
struct DataType<motionControl::motionControl_backward> {
  static const char* value() 
  {
    return "motionControl/motionControl_backward";
  }

  static const char* value(const motionControl::motionControl_backward&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<motionControl::motionControl_backwardRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "144a16e4d6b53a0dbadc2e617460a173";
  }

  static const char* value(const motionControl::motionControl_backwardRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<motionControl::motionControl_backwardRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "motionControl/motionControl_backward";
  }

  static const char* value(const motionControl::motionControl_backwardRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<motionControl::motionControl_backwardResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "144a16e4d6b53a0dbadc2e617460a173";
  }

  static const char* value(const motionControl::motionControl_backwardResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<motionControl::motionControl_backwardResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "motionControl/motionControl_backward";
  }

  static const char* value(const motionControl::motionControl_backwardResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // MOTIONCONTROL_SERVICE_MOTIONCONTROL_BACKWARD_H
