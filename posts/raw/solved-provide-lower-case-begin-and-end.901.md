Enhex | 2017-01-02 01:03:58 UTC | #1

...so range-based for loops can be used.
You can have both lowercase and uppercase version if it's so important.

I've been told about ForEach.h on the IRC but it completely defeats the purpose of range-based loops which is to make simple things simple, not more complex.

-------------------------

cadaver | 2017-01-02 01:03:58 UTC | #2

What is the problem with ForEach.h? It defines std::begin, std::end free functions that work with the Urho containers, after which you should be able to use range-based for.

Another possibility is of course to move the free functions into the header files of vector, hashmap etc. after which including ForEach.h would become unnecessary.

-------------------------

Enhex | 2017-01-02 01:03:58 UTC | #3

I can't find an example or instructions of how to use it.
For me the solution was to switch to std containers.

-------------------------

Stinkfist | 2017-01-02 01:03:58 UTC | #4

[code]
#include <Urho3D/Container/ForEach.h>
#include <Urho3D/Container/Vector.h>
// ...
Urho3D::Vector<int> values;
values.Push(1);
// Push more...
for(auto v : values)
    // ...
[/code]

-------------------------

cadaver | 2017-01-02 01:03:58 UTC | #5

I will move the std::begin() / std::end() to the respective headers, after which you should only need to include ForEach.h if you use the macro (and the legacy hack for VS2010 support)

-------------------------

darkhog | 2017-01-02 01:04:31 UTC | #6

Do you need performance that badly? If not maybe you should use Lua instead of C++?

-------------------------

Stinkfist | 2017-01-02 01:04:35 UTC | #7

Thread should be tagged as [SOLVED] BTW.

-------------------------

