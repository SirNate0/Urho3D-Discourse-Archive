vmost | 2022-01-10 16:23:15 UTC | #1

I am building a component that creates a long-lived object. The object's hot path contains two vectors with unknown size (in the worst case). These vectors require two allocations, and the vectors can't be naively cached in a member variable because the hot path could be called recursively (e.g. how Object.SendEvent() can be called recursively, so that function unavoidably contains a HashMap allocation).

This [CPPCON talk](https://www.youtube.com/watch?v=Tof5pRedskI) introduced me to 'polymorphic memory resources'. Basically, pmr lets you cache a memory buffer (which can be defined on the stack or heap), then allocate out of that memory buffer. If you are using the default allocator to set the memory buffer (e.g. the normal heap allocator), then when the buffer is fully used it will re-allocate a larger buffer. If you initialize with a static buffer (e.g. a `char static_buffer[256];`), then the buffer size is fixed.

Unfortunately, the STL only has pmr in C++17, and clang doesn't even support it yet. Instead, Boost's pmr has much more compiler support.

Here is how I used it.

```
# CMakeLists.txt

find_package(Boost 1.6 REQUIRED COMPONENTS container)
target_link_library(my_target PRIVATE Boost::container)
target_include_directories(my_target PUBLIC ${Boost_INCLUDE_DIRS})


# object.h

#include "boost/container/pmr/monotonic_buffer_resource.hpp"
#include "boost/container/pmr/polymorphic_allocator.hpp"
#include "boost/container/pmr/unsynchronized_pool_resource.hpp"
#include "boost/container/pmr/vector.hpp"

using MyType_Vec_t = boost::container::pmr::vector<MyType>;

namespace config
{
    const std::size_t default_buffer_size{256};
}

class MyObject
{
public:
    MyObject() :
        m_pmr_buffer{config::default_buffer_size},  //start with some memory so the first use of the buffer doesn't require an allocation
        m_pmr_resource{&m_pmr_buffer},
        m_pmr_allocator_MyType{&m_pmr_resource}
    {}
    ...
    void DoSomething();

private:
    boost::container::pmr::monotonic_buffer_resource m_pmr_buffer;
    boost::container::pmr::unsynchronized_pool_resource m_pmr_resource;
    boost::container::pmr::polymorphic_allocator<MyType> m_pmr_allocator_MyType;
}


# object.cpp

#include "object.h"

void MyObject::DoSomething()
{
    MyType_Vec_t new_vector{m_pmr_allocator_MyType};

    new_vector.reserve(10);  //ask m_pmr_resource for an allocation, which gets memory from m_pmr_buffer

    ...
} //~new_vector(): m_pmr_resource releases the memory back to m_pmr_buffer
```

I don't have rigorous performance numbers, but the impact is significant if you are reusing the pmr objects many times (and your worst-case doesn't cause memory exhaustion).

-------------------------

vmost | 2022-01-10 17:55:02 UTC | #2

I suspect this mechanism could be very useful in the engine (although it may fall apart on deeper inspection). Suppose `Context` owns the monotonic buffer and pool resource. Different places that require allocations (especially `Object.SendEvent()`) can dip into that resource pool at-will. Since allocations are one of the largest burdens outside rendering, this approach could have non-trivial and large scale benefits.

One concern is that every time the buffer needs to increase in size, it must reallocate the entire thing. This may be very expensive if the buffer gets large. I'm also not 100% sure if reallocating the buffer would invalidate iterators. EDIT: Nvm, it does not reallocate the entire thing - just adds more memory.

EDIT: It looks like `monotonic_buffer_resource` is only useful if you want the pool to obtain memory from a static buffer, or a dynamic buffer with an initial size. Otherwise the pool can exist on its own, obtaining more memory from the default allocator ad hoc when it runs out. One advantage of a standalone-pool is you can use `synchronized_pool_resource` for thread safety (`monotonic_buffer_resource` isn't thread-safe).

-------------------------

