ucmRich | 2018-01-15 08:05:02 UTC | #1

Hey guys!

I'm using Linux and a text editor for my C++ developments...

I'm somewhat new to C++ in general but I have been studying C++14 and am considering just skipping straight to C++17.


Here's what I want to do:

I want to keep Urho3D 1.7 just the way it is and not change a thing.

I want to create my own "from scratch" .cpp files in my own folder.

Then when I compile; I want to compile Urho3D 1.7 but have the compiler also compile "my" c++ code.

My C++ code would basically be accessing and using Urho3D 1.7 but 100% from my own .cpp files and I want to use Urho3D in this way but the end result would basically be a c++ scripting instead of using lua or angelscript.


My biggest thing is that I want to use c++14 or c++17 in my own files if at all possible.

** If I can't then my fall back would be to use Lua but I prefer to go c++

I hope this makes sense what I'm asking...

-------------------------

Eugene | 2018-01-15 08:27:20 UTC | #2

If you are talking about using C++ with Urho, there is a page in docs:
https://urho3d.github.io/documentation/HEAD/_using_library.html

If you are talking about _dynamic scripting_ in C++...
One tried it, but it's not very viable.

-------------------------

godan | 2018-01-15 16:20:23 UTC | #3

@TrevorCash and I have been working on a live C/C++ platform built with (and for) Urho. It is still pretty rough from a workflow perspective but the live code side of things is working super well. I definitely think that dynamic scripting with C/C++ is the way to go!

Here is quick screencast. Still a WIP!

https://youtu.be/sAzu3zPFCL8

-------------------------

S.L.C | 2018-01-15 19:00:43 UTC | #4

@ucmRich First of all, your use of the word `scripting` in the context of C++ might be interpreted wrong by some people. Since C++ is a compiled language, people tend to use the therm `programming`. And `scripting` is mostly used for interpreted languages like python, php, javascript or lua and angelscript for that matter.

And if I follow these rules, then I'll interpret your question as: You want to compile Urho with either regular C++ or C++11 but you'd like to use C++14/17 in your source files. And you can totally do that if you want to. Urho shouldn't have any issues with it.

This becomes a bit harder to do when you want to do it from the build system. Since I haven't seen an option with which standard you want to choose. Just pick whether you want C++11. Which means you'll have to modify a few files to get that working.

And based on the other information you gave. I assume you want to have your files be compiled by Urho's build system. For that, you might want to give this a read: https://urho3d.github.io/documentation/1.7/_using_library.html

I found Urho to be really easy to switch to another way of building. For example. I made a Code::Blocks project that I use to build it. Since it makes it easier for me to debug. I know it sounds dumb but I got used to this workflow (https://s13.postimg.org/r6e0qi1br/Untitled.png).

-------------------------

ricab | 2018-01-17 19:10:18 UTC | #5

I was also confused by the term "script" here but, IIUC, I have been asking myself the same thing for a while. Actually I posted a question in stackoverflow for this: https://stackoverflow.com/questions/46746878/is-it-safe-to-link-c17-c14-and-c11-objects

There is no answer yet and it is still unclear to me, but discussion in comments suggests that
- there is no guarantee in the standard about this, it is up to compilers
- it is probably ok, but still a risk

So @S.L.C.

> Urho shouldn’t have any issues with it.

Not Urho, but the linker might, unless your compiler's documentation states otherwise.

Personally I am still sticking to C++11 for the moment. To move to C++17, I would customize Urho's cmake modules to compile it with the same option to avoid risks.

-------------------------

