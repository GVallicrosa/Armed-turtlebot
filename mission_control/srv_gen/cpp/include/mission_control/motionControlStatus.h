/* Auto-generated by genmsg_cpp for file /home/user/ros_workspace/Armed-turtlebot/mission_control/srv/motionControlStatus.srv */
#ifndef MISSION_CONTROL_SERVICE_MOTIONCONTROLSTATUS_H
#define MISSION_CONTROL_SERVICE_MOTIONCONTROLSTATUS_H
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




namespace mission_control
{
template <class ContainerAllocator>
struct motionControlStatusRequest_ {
  typedef motionControlStatusRequest_<ContainerAllocator> Type;

  motionControlStatusRequest_()
  {
  }

  motionControlStatusRequest_(const ContainerAllocator& _alloc)
  {
  }


private:
  static const char* __s_getDataType_() { return "mission_control/motionControlStatusRequest"; }
public:
  ROS_DEPRECATED static const std::string __s_getDataType() { return __s_getDataType_(); }

  ROS_DEPRECATED const std::string __getDataType() const { return __s_getDataType_(); }

private:
  static const char* __s_getMD5Sum_() { return "d41d8cd98f00b204e9800998ecf8427e"; }
public:
  ROS_DEPRECATED static const std::string __s_getMD5Sum() { return __s_getMD5Sum_(); }

  ROS_DEPRECATED const std::string __getMD5Sum() const { return __s_getMD5Sum_(); }

private:
  static const char* __s_getServerMD5Sum_() { return "581cc55c12abfc219e446416014f6d0e"; }
public:
  ROS_DEPRECATED static const std::string __s_getServerMD5Sum() { return __s_getServerMD5Sum_(); }

  ROS_DEPRECATED const std::string __getServerMD5Sum() const { return __s_getServerMD5Sum_(); }

private:
  static const char* __s_getMessageDefinition_() { return "\n\
"; }
public:
  ROS_DEPRECATED static const std::string __s_getMessageDefinition() { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED const std::string __getMessageDefinition() const { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED virtual uint8_t *serialize(uint8_t *write_ptr, uint32_t seq) const
  {
    ros::serialization::OStream stream(write_ptr, 1000000000);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    ros::serialization::IStream stream(read_ptr, 1000000000);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint32_t serializationLength() const
  {
    uint32_t size = 0;
    return size;
  }

  typedef boost::shared_ptr< ::mission_control::motionControlStatusRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mission_control::motionControlStatusRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct motionControlStatusRequest
typedef  ::mission_control::motionControlStatusRequest_<std::allocator<void> > motionControlStatusRequest;

typedef boost::shared_ptr< ::mission_control::motionControlStatusRequest> motionControlStatusRequestPtr;
typedef boost::shared_ptr< ::mission_control::motionControlStatusRequest const> motionControlStatusRequestConstPtr;


template <class ContainerAllocator>
struct motionControlStatusResponse_ {
  typedef motionControlStatusResponse_<ContainerAllocator> Type;

  motionControlStatusResponse_()
  : status(0)
  {
  }

  motionControlStatusResponse_(const ContainerAllocator& _alloc)
  : status(0)
  {
  }

  typedef int8_t _status_type;
  int8_t status;


private:
  static const char* __s_getDataType_() { return "mission_control/motionControlStatusResponse"; }
public:
  ROS_DEPRECATED static const std::string __s_getDataType() { return __s_getDataType_(); }

  ROS_DEPRECATED const std::string __getDataType() const { return __s_getDataType_(); }

private:
  static const char* __s_getMD5Sum_() { return "581cc55c12abfc219e446416014f6d0e"; }
public:
  ROS_DEPRECATED static const std::string __s_getMD5Sum() { return __s_getMD5Sum_(); }

  ROS_DEPRECATED const std::string __getMD5Sum() const { return __s_getMD5Sum_(); }

private:
  static const char* __s_getServerMD5Sum_() { return "581cc55c12abfc219e446416014f6d0e"; }
public:
  ROS_DEPRECATED static const std::string __s_getServerMD5Sum() { return __s_getServerMD5Sum_(); }

  ROS_DEPRECATED const std::string __getServerMD5Sum() const { return __s_getServerMD5Sum_(); }

private:
  static const char* __s_getMessageDefinition_() { return "int8 status\n\
\n\
\n\
"; }
public:
  ROS_DEPRECATED static const std::string __s_getMessageDefinition() { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED const std::string __getMessageDefinition() const { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED virtual uint8_t *serialize(uint8_t *write_ptr, uint32_t seq) const
  {
    ros::serialization::OStream stream(write_ptr, 1000000000);
    ros::serialization::serialize(stream, status);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    ros::serialization::IStream stream(read_ptr, 1000000000);
    ros::serialization::deserialize(stream, status);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint32_t serializationLength() const
  {
    uint32_t size = 0;
    size += ros::serialization::serializationLength(status);
    return size;
  }

  typedef boost::shared_ptr< ::mission_control::motionControlStatusResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mission_control::motionControlStatusResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct motionControlStatusResponse
typedef  ::mission_control::motionControlStatusResponse_<std::allocator<void> > motionControlStatusResponse;

typedef boost::shared_ptr< ::mission_control::motionControlStatusResponse> motionControlStatusResponsePtr;
typedef boost::shared_ptr< ::mission_control::motionControlStatusResponse const> motionControlStatusResponseConstPtr;

struct motionControlStatus
{

typedef motionControlStatusRequest Request;
typedef motionControlStatusResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct motionControlStatus
} // namespace mission_control

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::mission_control::motionControlStatusRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::mission_control::motionControlStatusRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::mission_control::motionControlStatusRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const  ::mission_control::motionControlStatusRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::mission_control::motionControlStatusRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "mission_control/motionControlStatusRequest";
  }

  static const char* value(const  ::mission_control::motionControlStatusRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::mission_control::motionControlStatusRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
";
  }

  static const char* value(const  ::mission_control::motionControlStatusRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::mission_control::motionControlStatusRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::mission_control::motionControlStatusResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::mission_control::motionControlStatusResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::mission_control::motionControlStatusResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "581cc55c12abfc219e446416014f6d0e";
  }

  static const char* value(const  ::mission_control::motionControlStatusResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x581cc55c12abfc21ULL;
  static const uint64_t static_value2 = 0x9e446416014f6d0eULL;
};

template<class ContainerAllocator>
struct DataType< ::mission_control::motionControlStatusResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "mission_control/motionControlStatusResponse";
  }

  static const char* value(const  ::mission_control::motionControlStatusResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::mission_control::motionControlStatusResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "int8 status\n\
\n\
\n\
";
  }

  static const char* value(const  ::mission_control::motionControlStatusResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::mission_control::motionControlStatusResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::mission_control::motionControlStatusRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct motionControlStatusRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::mission_control::motionControlStatusResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.status);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct motionControlStatusResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<mission_control::motionControlStatus> {
  static const char* value() 
  {
    return "581cc55c12abfc219e446416014f6d0e";
  }

  static const char* value(const mission_control::motionControlStatus&) { return value(); } 
};

template<>
struct DataType<mission_control::motionControlStatus> {
  static const char* value() 
  {
    return "mission_control/motionControlStatus";
  }

  static const char* value(const mission_control::motionControlStatus&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<mission_control::motionControlStatusRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "581cc55c12abfc219e446416014f6d0e";
  }

  static const char* value(const mission_control::motionControlStatusRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<mission_control::motionControlStatusRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "mission_control/motionControlStatus";
  }

  static const char* value(const mission_control::motionControlStatusRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<mission_control::motionControlStatusResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "581cc55c12abfc219e446416014f6d0e";
  }

  static const char* value(const mission_control::motionControlStatusResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<mission_control::motionControlStatusResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "mission_control/motionControlStatus";
  }

  static const char* value(const mission_control::motionControlStatusResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // MISSION_CONTROL_SERVICE_MOTIONCONTROLSTATUS_H

