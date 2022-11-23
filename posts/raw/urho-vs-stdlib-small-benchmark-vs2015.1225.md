Enhex | 2017-08-30 15:27:27 UTC | #1

I wanted to do a quick test to see which containers perform faster.
Tried the two most common containers, vector and hash map.

The test was done with Windows 7 64bit, i5-2400 processor, Visual Studio 2015.
Urho3D version 1.4.

[img]http://puu.sh/jlEuU/ad5a15772f.png[/img]

[b]Code:[/b] [i](warning: quick and dirty)[/i]
https://gist.github.com/Enhex/9c8cf1f614267565189b

[b]Conclusions:[/b] [i](relative to what was tested)[/i]
- std::vector is faster than Urho3D::Vector.
- Urho3D::HashMap is faster than std::unordered_map.
- std::string is faster than Urho3D::String.

-------------------------

friesencr | 2017-01-02 01:06:12 UTC | #2

For ints you should us PODVector instead of Vector

-------------------------

Enhex | 2017-01-02 01:06:12 UTC | #3

[quote="friesencr"]For ints you should us PODVector instead of Vector[/quote]
Wouldn't that be comparing apples to oranges?

btw would it be possible for Vector to do what PODVector does with template specialization and traits?
Maybe something like this (C++11): [url]http://stackoverflow.com/questions/19154080/restricting-c-template-usage-to-pod-types[/url]

-------------------------

cadaver | 2017-01-02 01:06:14 UTC | #4

We'll still have to be a bit careful of C++11 only features. But for now, friesencr is right, PODVector should be used for ints for best performance. This can also be abused for non-POD types if the constructor/destructor don't do anything vital.

-------------------------

Enhex | 2017-01-02 01:06:14 UTC | #5

[quote="cadaver"]We'll still have to be a bit careful of C++11 only features. But for now, friesencr is right, PODVector should be used for ints for best performance. This can also be abused for non-POD types if the constructor/destructor don't do anything vital.[/quote]

Why the need to be careful with C++11 ?

-------------------------

cadaver | 2017-01-02 01:06:15 UTC | #6

On VS side that means upgrading to post-VS2010 versions, which can be argued to be more bloated than the previous, and don't support compiling for old OS versions (there may be some niche use of Urho like using an old VS version such as 2008 to compile for Win2000 / XP) 

Though I've been using VS2013 quite exclusively for some time and personally am happy with it.

-------------------------

Enhex | 2017-01-02 01:06:15 UTC | #7

[quote="cadaver"]On VS side that means upgrading to post-VS2010 versions, which can be argued to be more bloated than the previous, and don't support compiling for old OS versions (there may be some niche use of Urho like using an old VS version such as 2008 to compile for Win2000 / XP) 

Though I've been using VS2013 quite exclusively for some time and personally am happy with it.[/quote]

To me it seems like a huge sacrifice to hold back to be compatible with outdated software.
AFAIK VS2015 support at least down to win XP.

-------------------------

cadaver | 2017-01-02 01:06:16 UTC | #8

You can also go the other way around and ask what are the absolute vital reasons/features (not just convenience) for the engine/library itself to go for c++11? Bear in mind, you can always choose to use c++11 in your application code.

If interested, here's the c++11 discussion for Ogre: [ogre3d.org/forums/viewtopic.php?f=4&t=80319](http://www.ogre3d.org/forums/viewtopic.php?f=4&t=80319)

-------------------------

jenge | 2017-01-02 01:06:16 UTC | #9

I very much like that Urho3D is clean of C++11 constructs.  Nothing is keeping me from using VS2015.  We do have C++11 enabled for some ThirdParty libraries that use it very minimally.  There are also compilers on various platforms that do not support C++11.

-------------------------

Enhex | 2017-01-02 01:06:16 UTC | #10

[quote="cadaver"]You can also go the other way around and ask what are the absolute vital reasons/features (not just convenience) for the engine/library itself to go for c++11? Bear in mind, you can always choose to use c++11 in your application code.

If interested, here's the c++11 discussion for Ogre: [ogre3d.org/forums/viewtopic.php?f=4&t=80319](http://www.ogre3d.org/forums/viewtopic.php?f=4&t=80319)[/quote]

Looks like their reasoning is mainly based on ignorance and social proof. I also posted a reply there about the "auto is evil" nonsense.
Also the argument that C++'s stdlib somehow de-matured also doesn't make sense.

While looking for reasons is important, "absolute vital" sounds like an attempt to invalidate any reason.
What are the "absolute vital" reasons for C++ over C? What are the ones of C over ASM?
The "absolutely vital" condition doesn't make sense! Nothing is "absolutely vital" if you can get the job done. With that line of reasoning we'll be still using punch cards.

C++11 have features that can make code shorter, easier to read and understand, easier to maintain, and faster. What else is there to ask for?
The discussion about C++ was started by how it can boost the performance of the most commonly used container by nearly 50%. (saying "use PODVector" is like saying "Use array" or something else with non-matching functionality)
Also VS2015 have great debugging tools: [url]https://www.youtube.com/watch?v=NVCSuzFPzEM[/url]

The only reason so far is backward compatibility with outdated compilers. Even then, how do you draw the line for how backward compatible it is? C++98? C++85?
Of course that full backward compatibility doesn't make any sense. A good heuristic is to be as advanced as possible while supporting the majority of the users.
Both [url=https://www.visualstudio.com/en-us/products/visual-studio-2013-compatibility-vs.aspx]vs2013[/url] and [url=https://www.visualstudio.com/en-us/products/visual-studio-2015-compatibility-vs.aspx]vs2015[/url] are backward compatible down to win XP. And I don't think there are that many people who still use some 15+ years old version of windows.

Sorry about the rant, it's just irrational to me and I had to let it out.

-------------------------

cadaver | 2017-01-02 01:06:16 UTC | #11

I realize it's a rant, but if we're being serious, the difference between C & C++ is quite a large feature cutoff for large software such as Urho3D that could be considered "absolutely vital" for sanity, if not anything else.

Projects have to prioritize themselves differently, I can well understand if for some being modern in their language usage takes high priority. I believe the worst part of Urho not using C++11 is that project contributors don't get to exercise their skills in the new language features.

-------------------------

friesencr | 2017-01-02 01:06:17 UTC | #12

I hear the Magnum game engine author trip over new c++ feature bugs all the time.  Often on exotic platforms.  They are hard to detect sometimes.

I am a light contributor.  I do not know c/c++ well.  I believe also that the style that Urho is written in semantically  represents the problem it is trying to solve well.  As someone who does not know c++ well the more modest use of c++ features actually allows me to learn how to code better, faster.  Through implementing my current project I have learned a great deal about pointer arithmetic and data.

-------------------------

sabotage3d | 2017-01-02 01:06:17 UTC | #13

I think a game engine should be generic as possible and let the user handle anything more specific. SDL2 is one of Urho's third-party libraries and it is written in C, it is used everywhere and it is extremely portable. But I am thumbs up for faster containers :slight_smile:

-------------------------

cadaver | 2017-01-02 01:06:17 UTC | #14

The perf difference between a Vector<String> and std vector is something worth investigating. Probably is related to the reallocation of strings when the vector's storage expands.

-------------------------

globus | 2017-01-02 01:06:17 UTC | #15

[quote="Enhex"] ... are backward compatible down to win XP. And I don't think there are that many people who still use some 15+ years old version of windows.[/quote]
winXP - the best that has been created in Microsoft.
It is the working environment created by the developers.
win7-8-9-10 -... created by traders to make money.  :wink:

-------------------------

Enhex | 2017-01-02 01:06:18 UTC | #16

[quote="globus"][quote="Enhex"] ... are backward compatible down to win XP. And I don't think there are that many people who still use some 15+ years old version of windows.[/quote]
winXP - the best that has been created in Microsoft.
It is the working environment created by the developers.
win7-8-9-10 -... created by traders to make money.  :wink:[/quote]
MS always was for profit business.
Win 7 is the best IMO.
Win 9 never existed, you missed the news :wink:

-------------------------

globus | 2017-01-02 01:06:18 UTC | #17

[quote="Enhex"]Win 7 is the best IMO.[/quote]
[img]http://i.piccy.info/i9/f90896d6d4f906e5265302e658b94080/1438791546/46177/912050/xpshare.jpg[/img]
But Microsoft has completed the official support Win7.
The next time Microsoft will say: DirextX 14 only for Windows 11.
Nothing personal. Only business.  :wink:

-------------------------

1vanK | 2017-01-02 01:06:18 UTC | #18

I like XP too, but new hardware is not working on it. :) So I had to go to Win7.

-------------------------

globus | 2017-01-02 01:06:19 UTC | #19

For this reason, I collected a computer
with the latest hardware resources that support WinXP.
[spoiler]Motherboard: ASRock z77 extreme4-M
CPU: Intel Core i7 - 3770T
DDR3 memory
Video: GeForce GTX 750Ti 2Gb[/spoiler]
It good but hard to find motherboard with winXP support.

I use WinXP as a working environment.
For other platforms, have plans to use the remote method compilation 
(using FTP connection) or duble bootable HDD.

-------------------------

boberfly | 2017-01-02 01:06:20 UTC | #20

Hi,

I've learned a lot of C++ through Urho3D and prior to that Horde3D, as well as libraries often found in the VFX industry (OpenEXR/IlmBase). There's so much to learn, but it's fun to read up on this stuff.

I have on/off plans to make a plugin for Maya, and usually you need to match the compiler to the Maya version. So I'm a bit concerned that is C++11 really needed?
[url]http://help.autodesk.com/view/MAYAUL/2016/ENU/?guid=__files_Setting_up_your_build_environment_htm[/url]
Visual Studio 2012 update 4, and this is the latest Maya! Older ones like Maya 2015 uses GCC 4.1.x for instance, it doesn't say what it uses for Linux in this documentation. Recently the library OpenSubdiv reverted some C++11-isms to keep compatibility, for instance.

Not that it's a problem for Urho3D to limit itself to a 3D DCC and I don't want to force this requirement, but it's kind of nice to not go with the latest and greatest. Sure there are ways around this like make a C99 wrapper and only interface to that to keep ABI compatibility. Actually does anyone know of a convenient library to assist in making one, and not by hand? Something akin to the GL/Horde3D API would be cool and would let you wrap it to any language too.

About containers, lots of hardcore game engine developers usually are huge fans of C99 for good reasons and just use constrained/minimal C++ features (templates/operator overloads/classes and minimal use of virtual functions in hot paths which is important to not cause pointer indirection which slows up in-order CPUs) and stay clear of the STD. For performance and fine-grained control reasons usually, like making explicit allocators for what you want to do without fragmentation, and for efficient cache use.
[url]https://www.youtube.com/watch?v=rX0ItVEVjHc[/url]

I did find this the other day:
[url]https://bitbucket.org/bitsquid/foundation[/url]
If you saw Autodesk's announcement of Stingray, it's actually the bitsquid engine...

Some good info too:
[url]http://bitsquid.blogspot.com.au/[/url]

-------------------------

1vanK | 2018-04-06 13:23:58 UTC | #21

Urho3D::SharedPtr vs std:shared_ptr (VS 2017)

```
#include <Urho3D/Urho3DAll.h>

#include <iostream>
using namespace std;

int main()
{
    Context context;
    SharedPtr<Component> a, b;
    shared_ptr<Component> c, d;

    const long long count = 1000000LL;

    for (int k = 0; k < 10; k++)
    {
        HiresTimer timer;
        timer.Reset();
        for (long long i = 0; i < count; i++)
        {
            a = new Component(&context);;
            b = a;
        }
        long long elapsed = timer.GetUSec(false);
        cout << "Urho3D::SharedPtr " << elapsed << "\n";

        timer.Reset();
        for (long long i = 0; i < count; i++)
        {
            c = make_shared<Component>(&context);
            d = c;
        }
        elapsed = timer.GetUSec(false);
        cout << "std:shared_ptr " << elapsed << "\n";
    }

    // Prevent throw out pieces of code by compiler optimizer.
    clog << "Ignore it: " <<  b.Null() << d.use_count();

    // Prevent crash on exit when context deleted before objects.
    a.Detach();
    b.Detach();
}
```

Urho3D::SharedPtr 314000
std:shared_ptr 335000
Urho3D::SharedPtr 314000
std:shared_ptr 344000
Urho3D::SharedPtr 315000
std:shared_ptr 339000
Urho3D::SharedPtr 315000
std:shared_ptr 335000
Urho3D::SharedPtr 311000
std:shared_ptr 335000
Urho3D::SharedPtr 313000
std:shared_ptr 333000
Urho3D::SharedPtr 316000
std:shared_ptr 334000
Urho3D::SharedPtr 313000
std:shared_ptr 337000
Urho3D::SharedPtr 312000
std:shared_ptr 334000
Urho3D::SharedPtr 312000
std:shared_ptr 339000

-------------------------

Enhex | 2018-04-06 14:30:28 UTC | #22

maybe it's because Urho uses intrusive reference counting, with everything inheriting from `RefCounted`?
So we're getting 2 ref counts with `std::shared_ptr` instead of one.

To fix the comparison you'll need to create a class that inherits from `RefCounted` for Urho, and the same class without inheriting from `RefCounted` for `std::shared_ptr`.

This is how I corrected the code:
```C++
#include <Urho3D/Urho3DAll.h>

#include <iostream>
using namespace std;


struct TestUrho : RefCounted
{
	int x = 0;
};

struct Test
{
	int x = 0;
};


int main()
{
    SharedPtr<TestUrho> a, b;
    shared_ptr<Test> c, d;

    const long long count = 1000000LL;

    for (int k = 0; k < 10; k++)
    {
        HiresTimer timer;
        timer.Reset();
        for (long long i = 0; i < count; i++)
        {
            a = MakeShared<TestUrho>();
            b = a;
        }
        long long elapsed = timer.GetUSec(false);
        cout << "Urho3D::SharedPtr " << elapsed << "\n";

        timer.Reset();
        for (long long i = 0; i < count; i++)
        {
            c = make_shared<Test>();
            d = c;
        }
        elapsed = timer.GetUSec(false);
        cout << "std:shared_ptr " << elapsed << "\n";
    }

    // Prevent throw out pieces of code by compiler optimizer.
    clog << "Ignore it: " <<  b.Null() << d.use_count();
}
```

These are the results I got:
```
Urho3D::SharedPtr 140000
std:shared_ptr 79000
Urho3D::SharedPtr 127000
std:shared_ptr 77000
Urho3D::SharedPtr 142000
std:shared_ptr 78000
Urho3D::SharedPtr 141000
std:shared_ptr 78000
Urho3D::SharedPtr 126000
std:shared_ptr 79000
Urho3D::SharedPtr 126000
std:shared_ptr 78000
Urho3D::SharedPtr 137000
std:shared_ptr 78000
Urho3D::SharedPtr 141000
std:shared_ptr 81000
Urho3D::SharedPtr 130000
std:shared_ptr 78000
Urho3D::SharedPtr 143000
std:shared_ptr 80000
```

it seems that in this test `std::shared_ptr` is about 50% to 80% faster than Urho's `SharedPtr`.

Note: with the old code `SharedPtr` was indeed faster.

-------------------------

1vanK | 2018-04-06 15:01:42 UTC | #23

[quote="Enhex, post:22, topic:1225"]
maybe it’s because Urho uses intrusive reference counting, with everything inheriting from RefCounted?

So we’re getting 2 ref counts with std::shared_ptr instead of one.

To fix the comparison you’ll need to create a class that inherits from RefCounted for Urho, and the same class without inheriting from RefCounted for std::shared_ptr.

This is how I corrected the code:
[/quote]

Refcounting preccessd only by SharedPtr class. In your example sizes of structs is different, so you have faster memory allocation for shared_ptr

-------------------------

Enhex | 2018-04-06 15:06:46 UTC | #24

`std::shared_ptr` adds ref count externally, and `Urho3D::SharedPtr` can only be used with classes that inherit from `Urho3D::RefCounted`, so my benchmark is correct.

-------------------------

1vanK | 2018-04-06 15:30:29 UTC | #25

Ah yes, u are right!

EDIT:
```
Urho3D::SharedPtr 133000
std:shared_ptr 78000
Urho3D::SharedPtr 141000
std:shared_ptr 94000
Urho3D::SharedPtr 131000
std:shared_ptr 77000
Urho3D::SharedPtr 141000
std:shared_ptr 94000
Urho3D::SharedPtr 125000
std:shared_ptr 93000
Urho3D::SharedPtr 125000
std:shared_ptr 94000
Urho3D::SharedPtr 125000
std:shared_ptr 95000
Urho3D::SharedPtr 141000
std:shared_ptr 78000
Urho3D::SharedPtr 141000
std:shared_ptr 78000
Urho3D::SharedPtr 141000
std:shared_ptr 78000
```
with your code

-------------------------

1vanK | 2018-04-06 21:11:34 UTC | #26

With std pointers imposimple this thing:

```
void CrowdAgent::OnCrowdUpdate(dtCrowdAgent* ag, float dt)
{
        ...
        // Use pointer to self to check for destruction after sending events
        WeakPtr<CrowdAgent> self(this);
        ...
        crowdManager_->SendEvent(E_CROWD_AGENT_REPOSITION, map);
        if (self.Expired())
            return;
        ...
}

-------------------------

Sinoid | 2018-04-06 21:15:06 UTC | #27

No it isn't. The STL way is more verbose but can do the same thing using enable_shared_from_this and dynamic_pointer_cast.

-------------------------

Eugene | 2018-04-06 21:31:43 UTC | #28

TBH, `enable_shared_from_this` isn't the silver bullet. No way to do things in ctor, while intrusive ptrs have no problem there.

-------------------------

1vanK | 2018-04-06 21:36:34 UTC | #29

If I understand correctly, enable_shared_from_this stores shared_ptr inside function and to allow deleting shared_ptr outside we need crazy constructions inside function to get weak_ptr from shared_ptr and delete shared_ptr

-------------------------

Sinoid | 2018-04-06 23:01:27 UTC | #30

[quote="1vanK, post:29, topic:1225, full:true"]
If I understand correctly, enable_shared_from_this stores shared_ptr inside function and to allow deleting shared_ptr outside we need crazy constructions inside function to get weak_ptr from shared_ptr and delete shared_ptr
[/quote]

Backwards. It only stores a weak_ptr internally, which means there's no craziness involved.

[quote="Eugene, post:28, topic:1225"]
No way to do things in ctor
[/quote]

Clarify? You can't do a host of things in a constructor either way, virtual calls being the big one.

-------------------------

1vanK | 2018-04-07 00:39:55 UTC | #31

[quote="Sinoid, post:30, topic:1225"]
Backwards. It only stores a weak_ptr internally, which means there’s no craziness involved.
[/quote]

1) enable_shared_from_this requires to store weak_ptr in object, so... we get same overhead for object size, as when inheriting from Urho3D: RefCounted
2) You can not recieve this weak_ptr directly. You can recieve only share_ptr, convert to weak_ptr and then delete shared_ptr to allow self-destruct object outside function and get correct num refs in weak_ptr inside function

actually Urho's intrusive counter is different from boost https://github.com/boostorg/smart_ptr/blob/develop/include/boost/smart_ptr/intrusive_ref_counter.hpp
1) Urho stores count of weak refs (what for?)
2) Urho stores ref to RefCount instead storing of count in the object itself

EDIT: weak_from_this is part of c++17 http://en.cppreference.com/w/cpp/memory/enable_shared_from_this/weak_from_this

-------------------------

Sinoid | 2018-04-07 01:00:21 UTC | #32

I've been using STL-only in my local fork for quite a while, I haven't had a single issue or encountered anything that could not be done that the Urho containers were doing.

The switch also made it a lot easier to work with 3rd-party libraries that are almost always going to be using STL as well as concurrency primitives that I had to have for multithreaded rendering.

-------------------------

Eugene | 2018-04-07 07:45:31 UTC | #33

[quote="Sinoid, post:30, topic:1225"]
Clarify? You can’t do a host of things in a constructor either way, virtual calls being the big one.
[/quote]
Cannot spawn weak/shared ptr from ctor. 
And yes, it was a problem in my day job projects.
E.g. I was working with async server, and there’s no way to spawn tasks from ctor.

-------------------------

Enhex | 2018-04-07 12:13:02 UTC | #34

it sounds a bit dangerous to use an object that wasn't fully constructed yet, it's kinda like as if it's uninitialized.
You can always use some helper function that construct the object, then passes it to some other function.

BTW not all Urho objects need to use ref counting (ex: a subsystem with a known lifetime, usually until the program shuts down), and using std::shared_ptr gives the flexibility to choose not to.

-------------------------

Eugene | 2018-04-07 13:33:13 UTC | #35

[quote="Enhex, post:34, topic:1225"]
it sounds a bit dangerous to use an object that wasn’t fully constructed yet, it’s kinda like as if it’s uninitialized.
[/quote]

Meh, it's _sometimes_ dangerous. It wasn't my case tho. Async task manager needs weak ptr just to automatically cancel tasks if owner is destroyed. And there's no way to use it from ctor, despite it's completely safe.

-------------------------

1vanK | 2019-06-21 12:53:34 UTC | #36

As an experiment and optimization for cache locality, I moved refCounter from external structure into Object. WeakRefCounter still stay as external structure, so external counter created only when WeakPointers is used. In my tests, I did not see any difference of FPS. So I believe that pointers do not affect overall performance compared to other things — physics, rendering, and so on.

https://dropmefiles.com/3eAjq (build without AS and LUA)

-------------------------

weitjong | 2019-06-21 14:27:57 UTC | #37

The link is not working for me.

-------------------------

1vanK | 2019-06-21 15:13:34 UTC | #38

try it https://drive.google.com/open?id=1hiMki-KQUsCI1m5M9vegj_gKjquS5GZf

-------------------------

weitjong | 2019-06-21 15:53:00 UTC | #39

It's a link to the modified source code? I had hoped to see some benchmark result or some kind of comparison result instead. :slight_smile:

-------------------------

1vanK | 2019-06-21 15:56:41 UTC | #40

I just launch original and modified samples and recieve same FPS.

-------------------------

S.L.C | 2019-06-21 16:55:27 UTC | #41

Although you can't really expect to see a noticeable difference in a hello-world type of application. And a synthetic benchmark doesn't show much either. And since Urho doesn't have a complex game/application built with it. You can't do much but assume things.

As for the claim in the first post that:

[quote="Enhex, post:1, topic:1225"]
* std::string is faster than Urho3D::String.
[/quote]

Well, `std::string` is likely implemented with a small buffer optimization. And  this here `auto s = to_string(i);` falls into that kind of optimization.

If you would've created a test that goes away from that optimization. And the only way i can think of doing it in order to preserve the same amount and order of operations would be to use an array of random strings, like:

```cpp

const char * STRS[] = {
    "qZ[N.wv+tPMu7(RMmc{5Kh]u4s7@=TP2",
    "p==H'h5ez6W~rBtd[cM*)B(<+>wm=r7m",
    "XWmEmgW@-TN5E47J*-Pf^uFFkM5R#t8Z",
    "VFCY{K8;/x*(a3:3-8}^>Xu=5/#u%_Lb",
    "Sh5K?3~F^;~HuYGE`E!KN_sw[&6jz5&M",
    "+VR8eFE,^@\{C@@43~?=bsFpPM-+=6c`",
    "a:JH-7rG{}m7HJ9rx'dw;*e3jLy:v$Ny",
    "sC%}p&HFyNewS]JU&(%J+9ZH4Rr#6(4?",
    "Z[X2Gu%q}Q!6^FH6(aTGHwC2n=::#HGJ",
    "~X4f28TJq4*$t@KyFdr'wSm23^F9nd`B"
};
```

And then insert from those strings:
```cpp
	auto s = std::string(STRS[i%10]);
	std[s] = s;
```

You probably would've had a different outcome now. Because `std::string` is now a fatter structure because of that local buffer and also contains twice the validation, also because of that local buffer.

Which brings me back to my original point. The fact that you cannot look at a simple test like that and hope that result to reflect on a complex real world project.

And which brings me to my issue with using the standard library instead of built in structures. With which I have no problem. Just so I'm clear about that. But this is a project that targets many platforms and many compilers. Which brings the main issue with using STL. The fact that it's unpredictable. Results from one implementation might not align with the results of another. Each change must take into consideration each implementation that could be used to compile this engine with. Whoever maintains the engine must have a clear view of multiple implementations instead of just one.

Some implementations could have a smaller buffer used for the small buffer optimization. Some could use a bigger one. Different alignment on one implementation can introduce padding into your structures. Some could use reference counting and copy on write instead. Imagine finding the cause of a bottleneck through all these different implementations (*don't just assume there cannot be one, just because it's a string. you don't know what you need until you need it*). Not to mention that you've now introduced exceptions into the engine. Like i said, very unpredictable and time consuming.

Sure, you have tests and what not. But you broaden the scope of what developers must be familiar with.

And not to mention that you can kiss goodbye to dynamic libraries. If anyone relies on that.

I'm not saying STL is bad. I'm just saying that for a game engine with such a broad scope. It might prove to be a bit more headache than necessary.

That's just my opinion. Moving into this direction wouldn't affect me that much. And I'd love to see this happen and what outcome would there be. Pretty sure it'll be a valuable lesson for everyone involved (*including me*).

-------------------------

rku | 2019-07-05 10:36:33 UTC | #42

[quote="S.L.C, post:41, topic:1225"]
And not to mention that you can kiss goodbye to dynamic libraries. If anyone relies on that.
[/quote]

What do you mean? STL works just fine when used in dynamic libraries.

-------------------------

S.L.C | 2019-07-05 14:07:13 UTC | #43

Maybe. I won't argue that. But if built with the same compiler/options/STL implementation etc. Which kinda takes away from their usefulness.

That being said. I (personally) wouldn't consider doing it. The conditions for it to work the way it should are quite narrow. At least that's my opinion.

-------------------------

