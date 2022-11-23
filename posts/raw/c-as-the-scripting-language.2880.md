rico.decho | 2017-03-10 07:47:15 UTC | #1

If you want pure execution performance, the best scripting language I know is Cling.

It's an interactive C++ interpreter, based on LLVM.

Basically it compiles C++ code interactively within the host application.

That's much more efficient than the DLL compilation hacks (RCCpp, etc)...

And the best part of that is that once your scripts run fine in the C++ interpreter, you can add them to you C++ application build files :grinning:

Awesome !

(reposted)

-------------------------

TheSHEEEP | 2017-03-10 08:57:21 UTC | #2

Interesting. Not suited for all use cases (I don't think you want to expose scripters to C++ syntax and pitfalls, for example), but for where it can be used, that's pretty neat.

-------------------------

sabotage3d | 2017-03-10 11:45:18 UTC | #3

Looks really cool. Thanks for sharing. Do you know if you can link it to external libraries?

-------------------------

rico.decho | 2017-03-10 12:09:18 UTC | #4

Basically, it's just made to be embedded in a host application and directly use its declared types and functions.

So I've absolutely no idea what should be done to make it work with loaded DLLs for instance.

-------------------------

godan | 2017-03-10 12:55:50 UTC | #5

This looks excellent!

-------------------------

hicup_82017 | 2017-08-27 14:18:17 UTC | #6

Hello,
Any of you tried this?
I am just into Urho3d and interested to learn c++ a bit better. I only work with embedded C all the time. So this would allow me to bypass LUA learning and enhance my c++ skill set as well.

Thanks in advance :slight_smile:

-------------------------

JTippetts | 2017-08-27 14:49:00 UTC | #7

There's no requirement of using Lua. Just use C++. What this thread is describing is a "different way" of using C++, that's all. You've always been able to use C++ in the traditional fashion with Urho3D, as that is the language the engine itself is written in.

-------------------------

hicup_82017 | 2017-08-31 15:21:11 UTC | #9

Hi JTippetts,
In a sense your suggestion actually makes more sense for a newbie like me. 
All I want to do is, learn and design a simple game. Since you guys already made whole Urho3D as a library. My game code compile time should be very less and worrying for it doesn't make sense now.
Update: Able to complete reading some of the sample programs in C++ only :slight_smile:

-------------------------

1vanK | 2019-05-12 09:07:20 UTC | #10

http://chaiscript.com/

-------------------------

Leith | 2019-05-12 09:47:47 UTC | #11

Well, if we're going to do scripting, we might as well go the whole hog, and deal with runtime compilation of c++ sourcecode - inside our runtime application. Let's have our cake, and eat it too.

-------------------------

elix22 | 2019-05-12 14:15:16 UTC | #12

The only problem ChaiScript  is that performance is very bad
See entry 48 in the Results table .
https://github.com/r-lyeh-archived/scriptorium

I agree with Leith ,   Runtime Compiled C++   is the only way to go .
Someone actually implemented such a thing 
I might surprise  with my own implementation in the future :slight_smile: 
https://discourse.urho3d.io/t/runtime-compiled-c-in-urho3d-aka-scripting-in-c/318

-------------------------

S.L.C | 2019-05-12 20:58:19 UTC | #13

There is one thing that i don't understand from this request. Which is that you don't get anything in return.

The reason scripting is implemented in something is to simplify the entire application and allow for quick prototyping. You try something in the script. And as it grows, you look at the parts that can be moved to native code and you do that.

With this approach, you don't simplify anything. You are already programming in C++. In fact, you are complicating the whole process by such a degree. That any new person that wants to try out the application itself will eventually get lost in the details and rules of the implementation.

This isn't the purpose of a scripting language. And if performance is your argument (JIT). Again, this isn't the purpose of a scripting language. You move performance critical code to native code and expose it.

-------------------------

1vanK | 2019-05-13 04:00:52 UTC | #14

> The reason scripting is implemented in something is to simplify the entire application and allow for quick prototyping.

Reason of scripting also is user's mods and execute code from text form (triggers in levels or console commads).

> With this approach, you don’t simplify anything. You are already programming in C++.

This is subjective. For me personally, C ++ is much easier than lua or angel script because I use it more often. For example idTech use c-like language for scripting.

>  And as it grows, you look at the parts that can be moved to native code and you do that.

This is simpler when the script is already C++ code.

> And if performance is your argument (JIT). Again, this isn’t the purpose of a scripting language.

It is true.

http://fabiensanglard.net/doom3/interviews.php#qvm

EDIT:
I like quake 3 approach. http://fabiensanglard.net/quake3/qvm.php
```
Overall the VM system is very versatile since a Virtual Machine is capable of running:
* Interpreted bytecode
* Bytecode compiled to x86 instructions
* Code compiled as a Windows DLL
```

So if you need perfomance, you can just compile same code to native dll

-------------------------

1vanK | 2019-10-22 18:45:04 UTC | #15

I played a little with the cling. "cling-demo" demonstrates embedding and running c++ scripts and works great. But... compilation of cling took more than an hour (I don’t know exactly how much, I just didn’t wait and went about my business) and demanded 40GB HDD space with Debug configuration. If there is a way to extract only the necessary parts of LLVM, that would be great (I don't know if this is possible).

p.s. Build instruction https://root.cern.ch/cling-build-instructions

-------------------------

