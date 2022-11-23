setzer22 | 2017-01-02 01:05:50 UTC | #1

I just found out Urho now supports stl-compatible iterators for Vector and PODVector, so functions std::begin/end are implemented for those types.

As far as I know the only thing I need to use it is including ForEach.h from <Urho3D/Container/ForEach.h>, but doing so results in clang++ telling me there's no proper implementation of begin and end for that kind of type (type is actually Vector<WeakPtr<MyComponent>> (where MyComponent is a LogicComponent subclass). What am I doing wrong? Should I be doing anything else?

Also, I would like to avoid using the foreach macro, which I guess is still there to be compatible with older versions of the microsoft Visual C++ compiler, which is kind of its own beast. So as an offtopic question, is there a Windows compiler that properly implements the C++11 standard and isn't tied to an IDE?

-------------------------

gawag | 2017-01-02 01:05:56 UTC | #2

[quote]I just found out Urho now supports stl-compatible iterators for Vector and PODVector, so functions std::begin/end are implemented for those types.[/quote]
Oh really? Finally!  :mrgreen: *I need to update*
Is there any reason Urho is designed so STL-unfriendly with all its non-compatible function names like Size() instead of size()? That's so annoying...

[quote]As far as I know the only thing I need to use it is including ForEach.h from <Urho3D/Container/ForEach.h>, but doing so results in clang++ telling me there's no proper implementation of begin and end for that kind of type (type is actually Vector<WeakPtr<MyComponent>> (where MyComponent is a LogicComponent subclass). What am I doing wrong? Should I be doing anything else?[/quote]
I just looked around in GitHub and found that in [stackoverflow.com/questions/8164 ... -for-loops](http://stackoverflow.com/questions/8164567/how-to-make-my-custom-type-to-work-with-range-based-for-loops). Maybe you need a using namespace std;. Are C++11 ranged based for loops working for other types like std::vector? Is your compiler complaining about something more specific and suggesting candidates?
You can also try if auto iter=begin(myvector); and the same with end() is working and returning the right type of iterator (with for example exchanging auto with the full type written out).

[quote]Also, I would like to avoid using the foreach macro, which I guess is still there to be compatible with older versions of the microsoft Visual C++ compiler, which is kind of its own beast. So as an offtopic question, is there a Windows compiler that properly implements the C++11 standard and isn't tied to an IDE?[/quote]
I'm happily using GCC 4.9.2 via MinGW on Windows 7 with the CodeBlocks IDE (there may be newer GCC versions now). Setting that up is explained in [urho3d.wikia.com/wiki/Creating_a ... 3D_Project](http://urho3d.wikia.com/wiki/Creating_a_new_Urho3D_Project) . Write me if something there is unclear/outdated/bad.

-------------------------

setzer22 | 2017-01-02 01:05:56 UTC | #3

[quote="gawag"]Is there any reason Urho is designed so STL-unfriendly with all its non-compatible function names like Size() instead of size()? That's so annoying...[/quote]

The Urho3D containers are customly made because the stl containers are implementation-dependant, and thus the implementation in a platform may differ from the others. More specifically the concern seems to be with the size of the static part of the containers. In Urho3D sizeof(Vector<int>) is coherent between platforms while sizeof(std::vector<int>) is not guaranteed to be. That would be a source of trouble when working with Variants and the likes. 

The uppercase thing is just to maintain the same naming conversion across all the engine.

[quote="gawag"]I just looked around in GitHub and found that in [stackoverflow.com/questions/8164](http://stackoverflow.com/questions/8164) ... -for-loops. Maybe you need a using namespace std;. Are C++11 ranged based for loops working for other types like std::vector? Is your compiler complaining about something more specific and suggesting candidates?
You can also try if auto iter=begin(myvector); and the same with end() is working and returning the right type of iterator (with for example exchanging auto with the full type written out).[/quote]

As far as I know I've been doing it the right way. But I'm going to try manually calling the begin() and end() functions so I can better understand what's going on, thanks!

[quote="gawag"]I'm happily using GCC 4.9.2 via MinGW on Windows 7 with the CodeBlocks IDE (there may be newer GCC versions now). Setting that up is explained in [urho3d.wikia.com/wiki/Creating_a](http://urho3d.wikia.com/wiki/Creating_a) ... 3D_Project . Write me if something there is unclear/outdated/bad.[/quote]

Oh, good, so you can get GCC under windows. After having fought the MSVC for a while (not in Urho but other personal projects) this makes me happy.  :smiley:

-------------------------

Sir_Nate | 2017-01-02 01:06:02 UTC | #4

I know that I, at least, couldn't figure out how to get the enhanced for loops to work (lots of error: ?end? was not declared in this scope     for (String str : strings_)), but creating another header with the begin and end methods in namespace Urho3D instead of namespace std stopped them. I don't know if it is proper or not, and I've only tried it with g++ and variants (mingw and android and raspberry pi cross compilers) with c++11, but it's worked for me so far.
[code]#pragma once

#include <Container/Vector.h>

namespace Urho3D
{


template <typename T>
RandomAccessIterator<T> begin(Vector<T>& v)
{
    return v.Begin();
}

template <typename T>
RandomAccessIterator<T> end(Vector<T>& v)
{
    return v.End();
}

template <typename T>
const RandomAccessConstIterator<T> begin(const Vector<T>& v)
{
    return v.Begin();
}

template <typename T>
const RandomAccessConstIterator<T> end(const Vector<T>& v)
{
    return v.End();
}

}[/code]

-------------------------

