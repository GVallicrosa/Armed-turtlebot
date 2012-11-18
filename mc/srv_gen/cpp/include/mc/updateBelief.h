/* Auto-generated by genmsg_cpp for file /export/home/james.rowell/ros_workspace/Armed-turtlebot/mc/srv/updateBelief.srv */
#ifndef MC_SERVICE_UPDATEBELIEF_H
#define MC_SERVICE_UPDATEBELIEF_H
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




namespace mc
{
template <class ContainerAllocator>
struct updateBeliefRequest_ {
  typedef updateBeliefRequest_<ContainerAllocator> Type;

  updateBeliefRequest_()
  : belief()
  , value(0)
  {
  }

  updateBeliefRequest_(const ContainerAllocator& _alloc)
  : belief(_alloc)
  , value(0)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _belief_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  belief;

  typedef int64_t _value_type;
  int64_t value;


  typedef boost::shared_ptr< ::mc::updateBeliefRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mc::updateBeliefRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct updateBeliefRequest
typedef  ::mc::updateBeliefRequest_<std::allocator<void> > updateBeliefRequest;

typedef boost::shared_ptr< ::mc::updateBeliefRequest> updateBeliefRequestPtr;
typedef boost::shared_ptr< ::mc::updateBeliefRequest const> updateBeliefRequestConstPtr;


template <class ContainerAllocator>
struct updateBeliefResponse_ {
  typedef updateBeliefResponse_<ContainerAllocator> Type;

  updateBeliefResponse_()
  {
  }

  updateBeliefResponse_(const ContainerAllocator& _alloc)
  {
  }


  typedef boost::shared_ptr< ::mc::updateBeliefResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mc::updateBeliefResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct updateBeliefResponse
typedef  ::mc::updateBeliefResponse_<std::allocator<void> > updateBeliefResponse;

typedef boost::shared_ptr< ::mc::updateBeliefResponse> updateBeliefResponsePtr;
typedef boost::shared_ptr< ::mc::updateBeliefResponse const> updateBeliefResponseConstPtr;

struct updateBelief
{

typedef updateBeliefRequest Request;
typedef updateBeliefResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct updateBelief
} // namespace mc

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::mc::updateBeliefRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::mc::updateBeliefRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::mc::updateBeliefRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "e50891a9fcb180110e784cd3637d31ff";
  }

  static const char* value(const  ::mc::updateBeliefRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xe50891a9fcb18011ULL;
  static const uint64_t static_value2 = 0x0e784cd3637d31ffULL;
};

template<class ContainerAllocator>
struct DataType< ::mc::updateBeliefRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "mc/updateBeliefRequest";
  }

  static const char* value(const  ::mc::updateBeliefRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::mc::updateBeliefRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "string belief\n\
int64 value\n\
\n\
";
  }

  static const char* value(const  ::mc::updateBeliefRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::mc::updateBeliefResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::mc::updateBeliefResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::mc::updateBeliefResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const  ::mc::updateBeliefResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::mc::updateBeliefResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "mc/updateBeliefResponse";
  }

  static const char* value(const  ::mc::updateBeliefResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::mc::updateBeliefResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
\n\
";
  }

  static const char* value(const  ::mc::updateBeliefResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::mc::updateBeliefResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::mc::updateBeliefRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.belief);
    stream.next(m.value);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct updateBeliefRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::mc::updateBeliefResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct updateBeliefResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<mc::updateBelief> {
  static const char* value() 
  {
    return "e50891a9fcb180110e784cd3637d31ff";
  }

  static const char* value(const mc::updateBelief&) { return value(); } 
};

template<>
struct DataType<mc::updateBelief> {
  static const char* value() 
  {
    return "mc/updateBelief";
  }

  static const char* value(const mc::updateBelief&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<mc::updateBeliefRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "e50891a9fcb180110e784cd3637d31ff";
  }

  static const char* value(const mc::updateBeliefRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<mc::updateBeliefRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "mc/updateBelief";
  }

  static const char* value(const mc::updateBeliefRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<mc::updateBeliefResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "e50891a9fcb180110e784cd3637d31ff";
  }

  static const char* value(const mc::updateBeliefResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<mc::updateBeliefResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "mc/updateBelief";
  }

  static const char* value(const mc::updateBeliefResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // MC_SERVICE_UPDATEBELIEF_H
