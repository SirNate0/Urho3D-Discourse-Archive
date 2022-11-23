GSpub64 | 2017-01-02 01:12:04 UTC | #1

Hello everyone,

My name is Joseph and I'm new to the forums and Urho3D.  I'd like to start off on the good foot here and i'll try to learn on my own before making too many rtfm posts  :slight_smile: 

First the boring about me stuff to get it out of the way....
* i'm a long-term software engineer and have used another engine for years develop various indie style games and feature scripts for others to use. Sadly the engine's company went out of business before they could complete a conversion system to get games to Android/iOS. ( i won't mention the engine here as to not date myself )

* I never published anything [b][color=#007F00]_but_[/color][/b] with Urho3D I plan to change that by building a game concept i have and finally publish my first game to GooglePlay.  I've chosen Urho3D because of the on-going support and all of the features I need in a game engine are already built-in to Urho3D v1.5 so I can get started out of the box.


OK now for my main question; I see that Urho3D supports: AngelScript, Lua, and C++

1: I've used Lua before with a couple other engines and had pretty decent results although the absence of switch-case and arrays bogged my mind.  
I was leaning toward using Lua to do my entire game concept but I read somewhere that there were issues with Urho3D and that you were considering removing it? or was that the LuaJIT, or?

2: C++ I'm fairly new at but understand some of the basics pretty ok ( ish )

3: AngelScript I've never used before -but- i'm not sure about it's syntax styles.....

I am FAR more accustomed to JavaScript than anything else and am extremely proficient with JS.

What recommendation would you suggest for getting started from scratch with Urho3D and scripting a complete game with it ?

-------------------------

rku | 2017-01-02 01:12:04 UTC | #2

Always go with native language. Anything else gives great pains. If engine is written in c++ then using c++ is most painless thing. This is somewhat less of an issue with Urho3D as API is automatically wrapped and wrappers are really good. However should you start integrating any third party libraries they will most likely also be c++ or c and then you will have a bad time. So just go with c++.

-------------------------

GSpub64 | 2017-01-02 01:12:04 UTC | #3

thanks, rku and yes i plan to integrate google's admob...  [i]i can't believe i am considering actually putting ads in my game[/i]  :blush: I've never liked ads in games but money is money i guess and I figure i'll just let the user remove the ads for $0.99 or something like i've seen other games offer.  ( h_ll of a way to get my $0.99 -_- )

I realllllllllllly want to go for it using C++ all the way but the issue I have is that time is kind of a factor...  I figure that it will take me at least twice as long to do it in C++ so i figured using a scripting language would be quicker and easier.

( i'm still very tempted to go the C++ route but then i'll have a lot of rtfm questions regarding C++ usage lol )

-------------------------

boberfly | 2017-01-02 01:12:05 UTC | #4

Hi Joseph,

If you're proficient in JS, I would use AngelScript. It's quite similar and it is the best wrapper bind for Urho3D. I shipped a simple app written in AS, and low-level stuff with C++ like OpenAL support on iOS.

And the class names and syntax match C++ quite well, so converting AngelScript back to C++ shouldn't be too difficult, if performance or portability (think HTML5/Emscripten) is a concern. If you're making a subsystem (like integrating a third-party library/middleware written in C/C++), then just use C++, but if it's purely gameplay code which relies on built-in Urho stuff, AngelScript.

There is also Atomic Game Engine which is a fork of Urho3D with JS bindings too. And there's also a branch which integrates Runtime-Compiled C++ support, which makes testing/deving in C++ at scripting speed turnarounds.

My 2c.

-------------------------

GSpub64 | 2017-01-02 01:12:05 UTC | #5

I would much rather just go all the way with C++ and have fun with it but for time constraints I'm leaning towards AngelScript - but two considerations for me are:

1:  how easy is it to integrate third-party things like google admob using AngelScript? ( is there a walk through for this or a wiki article? )

2:  are there any tutorials on getting started with AngelScript to help me get up to speed with it's differences from other languages?

-------------------------

1vanK | 2017-01-02 01:12:05 UTC | #6

You can use C# :)

-------------------------

boberfly | 2017-01-02 01:12:05 UTC | #7

Hi Joseph,

From the docs [url]https://developers.google.com/admob/android/games[/url] I would follow the cocos2d-x tutorial which suggests AnySDK is a C++ API to get to adMob.

This would be a 'low-level' middleware/lib so definitely this needs to be in C++ as some kind of subsystem. For access in AngelScript you would need to bind this yourself. Following how Urho implements third-party middleware like bullet/recast/detour/databases, it should be relatively straight-forward...

Hope this helps!

-------------------------

