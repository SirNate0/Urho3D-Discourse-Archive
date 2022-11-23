rico.decho | 2017-03-08 11:06:57 UTC | #1

The 1.0 version of the Crack language has just been released !!!

https://crack-lang.blogspot.be
http://www.mindhog.net/~mmuller/projects/crack/Manual-1.0.html

Features :
- Influences : C, C++, Java, Python
- Syntax : C-style, curly-brace
- Typing : Static, strong (with some implicit conversion)
- Compiler : native compiled, either JIT (at runtime) or AOT (native binary)
- Paradigms :  Object oriented, procedural
- Garbage Collection : Reference counted objects, programmer controlled
- OO Features : Virtual functions, overloaded functions, multiple inheritance, generics.

Awesome !!!

IMHO, it could be the **PERFECT C#-LIKE SCRIPTING LANGUAGE FOR URHO3D**, much better than AngelScript or Lua...

At the moment, it only runs on **Linux**, and I need a FFI example to make some tests.

But LLVM is portable and can generate ARM machine language, and I've already asked to Michael to explain us how to use Crack from a host application.

-------------------------

TheSHEEEP | 2017-03-08 11:34:41 UTC | #2

Oh, look. Another scripting language... ;)

I don't want to be too negative, but if it does not have strong IDE support, I think the valid use cases will be fairly limited. And not being cross-platform makes it dead in the water, to be blunt.
The syntax itself looks nice. Except the `. Good luck with that symbol on non-US keyboards (it is left of backspace on Finnish and German keyboards, for example, and requires shift pressed. Ugh).

However, I agree that both AngelScript and Lua have that problem as well (no great IDE with autocompletion...) and so far, I think C#/Mono is the only scripting language that allows you to do proper coding when using a scripting language. 
What I'll do for my project is completely ignoring the scripting present in Urho and rolling my own with C# so I can get autocompletion in IDEs.

When I chose the scripting language to use, my checkpoints were:
1) Performance
2) JIT-support (when developing, scripting languages without this lose a lot of a appeal if you can't reload a script at runtime)
3) Ease of use (for scripters/modders)
4) Versatility (Lua for example, is extremely limited without many addons, there isn't even a proper socket API)
5) Ease of integration (for coders)

The only downside of C#/Mono is that it is horrible to integrate/embed and that part is hilariously bad documented. It is of course easy to run some C# script from C++, but any real use case requires interfaces between the two layers and that is just a nightmare with Mono. But on the upside, you only have to do that integration step once.
Also, JIT/script reload at runtime is hard to do with it (but not impossible).

In former projects, I usually went with Lua, but the lack of automatic autocompletion and the fact that its syntax is simply weird as hell and no modder really likes it made me drop it.

-------------------------

slapin | 2017-03-08 11:41:53 UTC | #3

Ah, another one of these llvm stuff :(

-------------------------

rico.decho | 2017-03-08 13:10:07 UTC | #4

That's right.

It's not ready as a viable alternative to Angelscript now.

But to me, it's actually "Angelscript done right".

Thus my post...

-------------------------

jmiller | 2017-03-08 18:55:34 UTC | #5

[quote="TheSHEEEP, post:2, topic:2868"]
However, I agree that both AngelScript and Lua have that problem as well (no great IDE with autocompletion...
[/quote]

Including **AngelScriptAPI.h** in search paths has been the usual solution. I'd assume it should work somewhat consistently across IDEs, if not ideal.
[url=http://discourse.urho3d.io/t/configuring-codelite-for-editing-as-scripts/68]Autocomplete and syntax highlighting in CodeLite[/url] -- which I find to be a great IDE; ofc that's subjective. ;)

-------------------------

slapin | 2017-03-08 19:23:10 UTC | #6

There's no great IDEs except for vim!

-------------------------

Eugene | 2017-03-08 19:46:05 UTC | #7

[quote="jmiller, post:5, topic:2868"]
Including AngelScriptAPI.h in search paths has been the usual solution
[/quote]

Actually, I haven't managed to find _any_ IDE for AngelScript -_-

-------------------------

slapin | 2017-03-08 20:00:28 UTC | #8

I use vim for AngelScript

    au BufRead,BufNewFile *.as set syntax=cpp "angelscript
    au BufRead,BufNewFile *.angelscript set syntax=cpp "angelscript

-------------------------

KonstantTom | 2017-03-08 20:03:41 UTC | #9

[CodeBlocks](http://www.codeblocks.org/) supports AngelScript by including AngelScriptAPI.h. 
Also CodeLite supports AngelScript, see [this forum thread](http://discourse.urho3d.io/t/configuring-codelite-for-editing-as-scripts/68).
I use [Atom](https://atom.io/) for editing my scripts. There is [angel script plugin by hdunderscore](https://atom.io/packages/language-angelscript).

-------------------------

TheSHEEEP | 2017-03-09 10:50:39 UTC | #10

Well, good to see that at least some support is there for AS in IDEs.
However, my main beef with AngelScript was always the performance. I could not find any reliable information on this. Without the JIT-compiler, it is too slow for any performance heavy scenario, for sure. And I couldn't find any numbers on performance that would compare AngelScript with JIT to C#/Mono or LuaJIT.
Just some people who couldn't get the JIT compiler to work (and it is not maintained by the main AS dev).

And the lack of any real numbers on this to me is pretty much a warning sign.

-------------------------

Eugene | 2017-03-09 12:18:35 UTC | #11

I dislike AS mostly because it has extremely dirty assembler hacks for function calls - big cost for nice binding syntax.

-------------------------

rico.decho | 2017-03-10 07:44:10 UTC | #12

If you want pure execution performance, the best scripting language I know is Cling.

It's an **interactive C++ interpreter**, based on LLVM.

Basically it compiles C++ code interactively within the host application. 

That's much more efficient than the DLL compilation hacks (RCCpp, etc)...

And the best part of that is that once your scripts run fine in the C++ interpreter, you can add them to you C++ application build files :grinning:

Awesome !

-------------------------

rico.decho | 2017-03-10 07:58:00 UTC | #13

Btw I've re-posted this as a topic ("C++ as the scripting language")...

-------------------------

