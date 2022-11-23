Jace | 2017-01-02 00:57:46 UTC | #1

I'd just like to quickly convey some of my thoughts on something that I've witnessed negatively effect many game engines (both open source and commercial) over the years.  
Now I know "negatively" can be interpreted in many different ways, so here is a basic example of what I'm talking about:

The Torqe3D engine which you may or may not be aware of went full open source (MIT) over a year ago. It actually started out immensely popular, but because they choose to make so much of the engine's functionality, f.e. the editors and engine core, dependent on their proprietary and not widely known scripting language known as TorqueScript a lot of game developers, who could have been potential contributors as well mind you, were put off by it and opted to go with different engines. 

So why am I bringing this up? Well, I couldn't help but notice when I first found Urho3D that it is very heavily AngelScript oriented (both the editor and primary game example are fully coded in AngelScript after all). However, I was pleased to see from going through the source that the engine's core functionality is in fact written entirely in c++. It's also great that Urho3D supports the option to compile without any scripting languages included with compile flags, but the problem is you lose the use of the editor as well as the best and most useful example project (ninja snow war). I'd hate to see Urho3D go the same way Torque3D did and become too dependent on AngelScript (or lua even for that matter). 

Don't you think it would be better to use C++ for the editors and tools too and include the primary game example/s ("ninja snow war") in c++ as well as the most popular scripting languages?  If the tools and primary game example were initially written in c++ it would be easier to wrap their functions in just about any scripting language (lua can practically do this automatically) The tools and game example are the most important part of introducing new users to an engine in my opinion, so why lock them down to one particular scripting language?

Here are the reasons why I think this would be more pragmatic as well as more beneficial to the success of a game engine as a whole. 

1. It gives you a much larger community. (Developers don't often like to take the time to learn scripting languages they don't know already, especially ones they haven't heard of, so they will simply look for an engine that supports the one they want or allows them to easily embed their scripting language of choice. A larger community means more contributions to the engine as well as bugs reported.) 

2. It's easier to embed a new scripting language in c++ than it is to remove/replace an existing one. (you have to back-port  exclusive features of the scripting language you're removing to c++ first)

3. The C++(11) improvements have made coding in c++ nearly as quick and easy as using a scripting language. (Okay maybe that's a bit of a stretch but it is a lot better isn't it?)  :laughing: 

4. C++(11) is becoming more and more popular at a rapid rate. (It is much easier to port to other platforms and both Google, Mozilla, and Microsoft are encouraging developers to write in c++ now more than other languages for that reason).

5. C++ can easily be ported to the web now (Emscripten, Mandreel and now Duetto all allow this).

Just some musings of mine for the Urho3D team  :slight_smile:

-------------------------

JTippetts | 2017-01-02 00:57:46 UTC | #2

The chief difference, I think, is that there is a world of difference between TorqueScript and AngelScript, or TorqueScript and Lua. As you mention, TorqueScript was proprietary and not very widely used outside of Torque; the same can't really be said for AngelScript and Lua. Both are open source, and both are fairly widely used in many other fields.

Ultimately, code is code and as long as the language is accessible, the main driver should be ease of development. Despite the C++11 standard's changes, it is still demonstrably quicker to develop in a language such as Lua or AS than C++. Now, I don't want to turn this into a language flamewar, but from where I sit the tight integration between Urho3D and Lua is a very, very strong selling point. Being able to essentially drop-in Lua-based or AS-based components (without having to jump through the binding hoops that you have to with less tightly-integrated engines) is neat. Considering the open source nature of both scripting languages, I really can't foresee any need to remove either one, outside of the trivial configure-time changes necessary to exclude one or the other. While I won't comment on whether or not C++ is growing as fast as you say, I do know that a number of professional AAA devs of my acquaintance have indicated that the industry (at least, their parts of it) is moving more toward such a tightly-integrate paradigm, leaving C++ to the underlying framework and sticking to dynamically typed, interpreted languages such as Lua for the high-level game logic. In my opinion, the current architecture really facilitates this.

As far as porting the editor to C++, I'm neutral; however, I could see the logic in it, to make it accessible to those who build with AS disabled. Since I really don't use the editor I have no real strong opinion nor investment, and leave that discussion up to others.

-------------------------

friesencr | 2017-01-02 00:57:46 UTC | #3

I can't code in c++.  I am trying to learn but its slow going.  

I have 14 commits post google code: 
[github.com/urho3d/Urho3D/commit ... =friesencr](https://github.com/urho3d/Urho3D/commits?author=friesencr)

I have also reported at least 9 bug reports post google code: 
[github.com/urho3d/Urho3D/issues ... ate=closed](https://github.com/urho3d/Urho3D/issues/created_by/friesencr?direction=desc&labels=bug&page=1&sort=updated&state=closed)

I work on the editor because I can.  This is my primary open source effort.  I have 10 years in web programming on lots of different platforms, but I suck at game codez and low level stuff.  My wife is barely a coder, albeit pretty smart, read all of the docs then mutilated the angel script character demo and got a character walking around, which I think is pretty awesome.  I am a fortunate benefactor of the accessibility.

Something to consider is that the editor's primary function is facilitate Urho's data driven design.  It makes lots of xml.  Having an Urho3dPlayer running the editor with angelscript could have 0 impact on your game's actual design.  If you get to using the editor and have suggestions that would be helpful to me.

-------------------------

cin | 2017-01-02 00:57:46 UTC | #4

[quote]I can't code in c++. I am trying to learn but its slow going. [/quote]
O_o

-------------------------

cadaver | 2017-01-02 00:57:46 UTC | #5

The initial reasons for writing the editor and the game example in AngelScript were to get a way to test the viability of the script bindings. As time has passed, I would think the editor has certainly been much more productive to write in AngelScript than in C++, so going to C++ would be a downgrade for development of new editor features. Of course, the C++ API to the engine is the most powerful of all, as you can do eg. byte-level manipulation of textures and vertex buffers. So far the editor has not needed that.

Maintaining an example as large as NinjaSnowWar in multiple languages is not feasible with the current size of the active development team. The sample applications are already hard enough to keep in sync in 3 languages. In my opinion the C++ samples should be enough to get into the use of the C++ API and are in fact pedagogically much better than NSW, which does a bit too many things at once.

Another matter is that Urho3D doesn't have a clear application model, such as Unity does. This is probably good for an open source engine, as you're free to structure eg. your main program exactly like you want, but it makes writing an editor with functionality like Unity (test the whole game by pressing the play button in editor) impossible.

-------------------------

ruminant | 2017-01-02 00:57:47 UTC | #6

I think the way Urho3D is exposed to scripting languages makes it fairly easy for a C++ programmer to understand those scripts.  The demos written in lua/angelscript look pretty similar to how they would in c++ (minus some boilerplate stuff).

I've worked on projects where this hasn't been the case, where the script bindings are an abstraction layer above the engine (the advantage with these is that the underlying engine can change but the script interface would remain the same).

With Urho3D, the script access is almost one-to-one.  I think that makes a big difference.

I'm using Urho3D in pet projects that are only C++ and some that are only Lua and that's completely workable because learning the engine in one helps the other.

-------------------------

