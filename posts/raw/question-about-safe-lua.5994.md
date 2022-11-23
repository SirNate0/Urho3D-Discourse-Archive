evolgames | 2020-03-15 17:20:01 UTC | #1

If I build with URHO3D_SAFE_LUA=1, the resulting Urho3DPlayer binary in /bin/ should be different, right?

I followed the getting started on linux guide to rebuild and when doing cmake I do:
```
cmake . -DURHO3D_SAFE_LUA=1
```
[Here](https://urho3d.github.io/documentation/1.6/_building.html) it says to put -DOPTION=value. I don't know why the D, though.

However, with the resulting Urho3dPlayer binary, I still get segmentation faults without any other information as to why. With certain errors, I'll be told via the console, or in a terminal, about the error. But other times I just get segmentation fault, core dumped and nothing else. It's too time consuming to track everything down and guess why it's crashing.

What is Safe_Lua supposed to do here? I don't see any real difference. Or, did I build incorrectly? What's the best way to troubleshoot this?

-------------------------

SirNate0 | 2020-03-15 19:33:43 UTC | #2

My understanding (as someone who doesn't use Lua) is that the Safe Lua flag builds Lua with certain safety checks about types and such, which gives you the error messages in the console you describe. However, if there was are not in the Lua side but the c++ side you'll still get errors. Of course, there seems to me to be areas that could be considered overlapping - null function arguments, for example - is that a Lua error, a c++ error, or not an error, which may break things even with the Safe Lua flag. Possible example: doing something with an empty vector's Front() element.

To assist in tracking down errors:
 * Check the log for any unexpected error/warning messages
 * Run your program in a debugger so you see where it's actually having the segmentation fault and can go up there stack a bit too find the source (hopefully - this may be very hard using Lua/Angel Script.

Others may have more/better suggestions. I focus on c++ for my projects, so my go-to solution to find the problem is just run it in a debugger, which has worked 99% of the time.

-------------------------

Avagrande | 2020-03-20 20:03:05 UTC | #3

As opposed to many other people here I work with Lua primarily. almost all of my code-base for urho3d is in lua.  I do use safe lua and I must warn that if you are going to use it, you may get errors which are almost impossible to resolve due to the unnecessary const values in some of the package bindings so its usage is experimental for the most part and as a result of that you may want to familiarise yourself with how tolua++ works and the .pkg format so you can easily fix it. its not that difficult. 


If you want a quick test that Safe Lua works, you can try giving incorrect parameter such as a int to a function which expects a vector and it should give you an error, under normal circumstances it will not.  This sadly also affects some functions who's parameters have annotations such as const and causes frivolous errors.  

Don't expect safe lua to cover you for memory issues, if you don't properly manage memory such as not using :new() when you are passing things created in Lua to C++ structures. Memory management between Urho3D C++ and Lua is tricky but doable if you keep the rules in mind. Safe Lua will mostly provide simple type checking but beyond that its not much use. 

Additionally you may want to build in debug mode so you can use gdb to see where things go wrong as opposed to relying on safe lua to do it. if you see pointer related issues its probably because the C++ structures decided to delete something you are still using in Lua, this is often the majority of errors that I get, and its sometimes guess work to determine if everything is deleted properly, but generally if you pass something to a C++ structure then it has control over it and Lua must not interfere otherwise its double deleted.

For GDB I advise creating a script so it should be as simple as running a debug.sh in your project directory. you can execute a script in gdb with ```gdb -x <script>.cgdb```
Personally mine looks like 
```
file "/Projects/Tools/Urho3d/build/bin/Urho3DPlayer"
r '/Projects/<project>/uroh3d.lua' -w -p 'Data;CoreData;urho_ext;' -pp '/Projects/Tools/Urho3d/build/bin/Urho3DPlayer;/Projects/<project>;'
``` 
I have an additional local path added urho_ext I use to manage project specific data such as shaders, render paths etc. 


Good luck! and if you want better support for lua and can't have it any other way you can try using sol2 which has a binding converter from tolua++ pkg to its own format. I haven't tried it but its on my todo list. 

For your cmake question: 
If I recall correctly the D value is for Debug.  so -DURHO3D_SAFE_LUA=1 unpacks to "when building in debug mode build with safe lua" 
Personally I would suggest using the cmake gui, which works on both linux and windows for the ease of use as you can simply tick the options you want.

-------------------------

SirNate0 | 2020-03-20 20:15:11 UTC | #4

[quote="Avagrande, post:3, topic:5994"]
If I recall correctly the D value is for Debug. so -DURHO3D_SAFE_LUA=1 unpacks to “when building in debug mode build with safe lua”
[/quote]

I'm not certain, but I thought it was just how you set it for any build type, and that it meant something along the lines of define (e.g. define URHO3D_SAFELUA = 1 when generating the build files).

Agreed about cmake-gui, though. Generally it makes things a lot easier, and keeps you from misspelling the flags.

-------------------------

Avagrande | 2020-03-20 20:21:57 UTC | #5

Yep thank you, you are right. Just checked in the manual.
```
-D <var>:<type>=<value>, -D <var>=<value>
Create a cmake cache entry.

When cmake is first run in an empty build tree, it creates a CMakeCache.txt file and populates it with customizable settings for the project. This option may be used to specify a setting that takes priority over the project’s default value. The option may be repeated for as many cache entries as desired.
```

-------------------------

