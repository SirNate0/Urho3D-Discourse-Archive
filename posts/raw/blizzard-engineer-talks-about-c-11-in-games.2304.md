rku | 2017-01-02 01:14:35 UTC | #1

Very interesting talk, check it out. Talks about all new sweet features in standard library.

[youtube.com/watch?v=8AjRD6mU96s](https://www.youtube.com/watch?v=8AjRD6mU96s)

-------------------------

sabotage3d | 2017-01-02 01:14:36 UTC | #2

Cool thanks for sharing. I watched most of the CppCons but I missed this one.

-------------------------

Lumak | 2017-01-02 01:14:36 UTC | #3

That was a good talk, but I doubt this is a trend that most devs would follow, not right now at least.  The mass concurrency seems to be the high lite of this talk.  The constexpr topic was interesting for serialization/deserialization. But w/o there being a multi-threaded rendering capability and the "breath of consumers having a graphics card that can support it," bottleneck would be there.

-------------------------

cadaver | 2017-01-02 01:14:36 UTC | #4

How well can you can rely on e.g. std::thread or std::chrono being on par with the (best use practices of) platform-specific system functions?

Probably quite well if you restrict yourself to the newest compilers. The Ogre thread on C++11 [ogre3d.org/forums/viewtopic.php?f=4&t=80319](http://www.ogre3d.org/forums/viewtopic.php?f=4&t=80319) is a couple of years old, but they mention the highres clock on VS2012 not really being highres.

-------------------------

rku | 2017-01-02 01:14:39 UTC | #5

Well if something like blizzard find std:: stuff useful it cant be that terrible. Or maybe it is no longer that terrible. We probably could use some of that stuff as well.

I found someone's fnv hash implementation in constexpr. gcc/clang/icc have no problem hashing during compile time. That sounds like potentially nice thing to have for supporting compilers. After all by now there is little reason to stick to older standards and older compilers as even microsoft compiler did catch up pretty nicely with new c++ features.

Compile-time hashing demo: [godbolt.org/g/ikADrz](https://godbolt.org/g/ikADrz)

-------------------------

cadaver | 2017-01-02 01:14:39 UTC | #6

On Visual Studio, there can unfortunately be IDE usability reasons to stick with an older version, e.g. at some time ago VS2015 was being rather sluggish compared to VS2013. That may have improved with a recent update, not 100% sure.

-------------------------

sabotage3d | 2017-01-02 01:14:52 UTC | #7

I am quite happy wiht C++11 it is fully supported now on Android with Clang and libc++. Is clang an option for Windows users?

-------------------------

Enhex | 2017-01-02 01:14:52 UTC | #8

[quote="sabotage3d"]I am quite happy wiht C++11 it is fully supported now on Android with Clang and libc++. Is clang an option for Windows users?[/quote]
Actually yes, Microsoft ported Clang, not fully IIRC, to Windows and has an extention for VS to use Clang.
[blogs.msdn.microsoft.com/vcblog ... -released/](https://blogs.msdn.microsoft.com/vcblog/2016/03/31/clang-with-microsoft-codegen-march-2016-released/)
[llvm.org/builds/](http://llvm.org/builds/)

-------------------------

S.L.C | 2017-01-02 01:14:52 UTC | #9

Barely anything new in that talk. At least not in 2016. He basically ([i]almost[/i]) lost me at the std::distance thing. To me it seems like someone who's been using the basics of C++ ([i]more like C with classes[/i]) and then just heard of C++11 and thought he knows enough to tell people that yea, this is the bomb. Most of what he talked about can be found in documentation websites such as cppreference.com. He barely even touched the good stuff. Most of what he covered can probably be found in something like an overview page of the C++11 features. Or a 10 minute 101 course. Nothing really critical to game engines was presented ([i]IMO[/i]). Like some revolutionary thing that no one didn't knew until now. And in my opinion C++11 was more like an experiment which was pimped a little in C++14 and finally done right in C++17. Which is why I'm more interested in C++17 than what we had so far.

As @cadaver mentioned, MSVC is not to be trusted when it comes to these features. And if I remember, the [url=http://stackoverflow.com/a/16299576/1695767]chrono issue[/url] is even acknowledged. They've delivered compilers with half implementations of the C++y features and then incrementally added them through those CTP updates. And the fun part, is they did not change the value of _MSC_VER in those updates. So it's kinda awkward to know if you're running in a basic install or an updated one.

For example, constexpr was not supported in the release of VS 2013. It was added in in the November CTP update. Then user defined literals was not supported either. They've added them in CTP 14 which later became VS 2015. And a bunch of these incomplete implementations and differences. They've probably released their compilers because they didn't want to fall behind and be left out.

I even remember having to write tons of workarounds because their compiler and standard library was never following the standards. They kinda wen't their own way.

However, I do agree that legacy C++ is dragging a lot of projects behind and let's just say that compilers like MSVC where you never know for sure whether you'll have that feature available or not or whether it works as it's supposed to be, are not helping the situation either.

-------------------------

namic | 2017-01-02 01:15:10 UTC | #10

[quote="rku"]Well if something like blizzard find std:: stuff useful it cant be that terrible. Or maybe it is no longer that terrible. We probably could use some of that stuff as well.

I found someone's fnv hash implementation in constexpr. gcc/clang/icc have no problem hashing during compile time. That sounds like potentially nice thing to have for supporting compilers. After all by now there is little reason to stick to older standards and older compilers as even microsoft compiler did catch up pretty nicely with new c++ features.

Compile-time hashing demo: [godbolt.org/g/ikADrz](https://godbolt.org/g/ikADrz)[/quote]

What's the point in using those hashing functions? Isn't std::unordered_map<std::string, blah> good enough for storing filenames and stuff?

-------------------------

