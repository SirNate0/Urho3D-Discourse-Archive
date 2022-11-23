Pyromancer | 2017-01-02 01:07:30 UTC | #1

I did a thing!

So I have some initial work on improvements to the reflection system. Still very much a work in progress, but I has a fork of Urho3D on my github that has the initial work. It loaded up the NinjaSnowWar example just fine, though it needs a much more thorough battery of testing to make sure that everything works as it should.  :mrgreen: 

Compiled and ran just fine on Apple LLVM 7.0.0

[url]https://github.com/BrightBlueFlame/Urho3D[/url]

-------------------------

gwald | 2017-01-02 01:07:37 UTC | #2

[quote="Sinoid"]
I think you've crossed it, actually I think you ran right over it into the sunset never looking back at the explosions behind you.[/quote]
 :open_mouth: 

 :laughing:  :laughing:  :laughing: 
That's very funny, everyone has their own style

-------------------------

Pyromancer | 2017-01-02 01:07:37 UTC | #3

[quote="Sinoid"]There's a fine line between a macro DSL and macro hell.

I think you've crossed it, actually I think you ran right over it into the sunset never looking back at the explosions behind you.[/quote]

So kinda like this you mean?
[img]http://i.imgur.com/SqZlt1I.gif?noredirect[/img]

Funny thing is that aster's commits yesterday implemented everything I wanted, so the most I will need to do now is just update my registration helpers since base type querying is now in the core of the engine. Most of that crap will cease to be.

@gwald - True, but he's right in a way (though he didn't [i]really[/i] need to put me on blast). I shared my fork with you guys specifically so I could get feedback on it. To be honest, I myself was starting to get a little frustrated at the way I went about implementing the feature I wanted.

-------------------------

boberfly | 2017-01-02 01:07:38 UTC | #4

That gif though, always my favourite.

Whatever benefits the eventual ease of binding it for pipeline tools/editors or other languages (python!) the better!

-------------------------

Pyromancer | 2017-01-02 01:07:40 UTC | #5

I don't think this will do much for easing bindings to languages. The ClassConstructor class and URHO_REGISTER_OBJECT macro is more of a wrapper around the existing system, with the AttributeProperty class  acting as a bit of code-level metadata for... whateverthehell you want. I guess it could be used as a means of automating script binding, but there are better ways to do that. I'm of the camp that says script binding should be automated as little as possible because the script->C++ barrier is slow as hell no matter what language you use. I myself can't see myself using Angelscript all that much (despite my prior experience with the library when I was in college).

Tools implemented in C++ however, that is probably where my additions will help you tremendously.  :mrgreen:

-------------------------

