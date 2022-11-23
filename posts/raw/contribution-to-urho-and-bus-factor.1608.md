Enhex | 2017-01-02 01:08:53 UTC | #1

The problem:
[quote="cadaver"]bvanevery is quite spot on regarding the core developer manpower. It would be no problem to integrate Newton as an option (I will not make comments on its quality since I've not tested it personally in depth) if we got a contributor who does the integration and is then willing to maintain it. In general Urho3D's problem is accumulating features while former steady contributors become inactive, leaving for the most part me and Yao Wei Tjong to maintain the whole.[/quote]

I think Urho could encourage more contributions by reducing the barriers of entry.
Here are some suggestions:

[b][u]Contribution friction:[/u][/b]
Reducing contribution friction will encourage more contributions.

- Less strict contribution requirements. For example requiring AngelScript and Lua versions means the contributor has to learn how to use them and/or bind them. Instead the script versions can be added as tasks to complete before merging the contributed changes.

- Document how things work under the hood, so if someone wants to change existing things he can actually have an idea what he's doing, instead of having to try to guess.

- When facing the choice between making an external cod to Urho, or modifying Urho, if someone doesn't know if a PR will be accepted, it's safer and faster to just make external code than waiting to see if it got accepted, and if not having to convert it to external code anyway.
A clear and fast way to validate if some work will be accepted into Urho before it's done can to favor contributing to Urho instead of playing safe.
Maybe something like a sub-forum or a chat, in which users can get a quick answer.


[b][u]Bus Factor:[/u][/b]
[en.wikipedia.org/wiki/Bus_factor](https://en.wikipedia.org/wiki/Bus_factor)

- Like before, document how things work internally.

-------------------------

cadaver | 2017-01-02 01:08:54 UTC | #2

We have also allowed contributions that are lacking in some respect, and have fixed them on merging or instructed the author on how to fix.

I don't think lack of contributions as such is a problem. If you look at Urho's github we have over 300 closed pull requests, of which I believe most were accepted.

The real problem (which I didn't articulate well enough in that reply) is the lack of people who are core developer or owner material. For that demands are even higher than providing script bindings, as you should be able to understand most of the engine (or be motivated to learn), be interested in fixing engine issues that necessarily don't have to do with your own projects, managing PR's yourself, and perhaps most importantly stay onboard and not quit.

In short, I don't want more contributed code that I have to fix, but rather I'd want people who could keep the wheels rolling even if e.g. I was away. I'm all for sharing power / responsibility in the engine, but it's quite rare to be asked "Hey, I want to be a core contributor!" Rather I've had to pester well-contributing people myself. "Hey, do you want push rights?"

The fortunate thing is that nothing exactly needs to change, but in that case the development of Urho will not at least speed up.

-------------------------

bvanevery | 2017-01-02 01:08:56 UTC | #3

I don't know how I feel about documentation, yet.  I have plenty of 3d background, but it comes from a different era.  Equations and principles are not a big deal to me, it's the APIs and toolchains that are a barrier.  I'm currently resolved to slowly plod along with DirectX Whatever until I see the light at the end of the tunnel.  Urho3D's main virtue in that regard is being a non-trivial base of working DX11 code.  I've kept up on the general principles of DX11 over the years but I haven't done anything specifically with it.  So the minutiae of ThingAMaJig->ShovingIntoTheFunctionThing(crap, o, la) is quite tiresome but I suppose I'll eventually be sufficiently familiar with it.  There's so much boilerplate to get anything done, I hate it.  But I tried to do Linux and OpenGL in rebellion for 3 years recently, and I became firmly convinced that it's decidedly the worse API and platform.  So back to DirectX crap it is!  Vulkan couldn't come too soon.

So, I wouldn't confuse learning graphics and 3D API stuff, for learning Urho3D stuff.  People either swallow the former or they do not.  I've written my own 3d API "pave over" stuff before, back in the DX8 era.  Urho3D's architecture in that regard seems pretty straightforward to me.  I have no difficulty understanding how multiple 3d APIs are "made to function alike".  For me the area of investigation is, whether optimal use of DX11 performance concepts are being made.  Time will tell.

It happens that because I've suffered for years trying to get other people's open source projects to actually work on Windows, that I have erstwhile CMake skills.  So although I don't like CMake, and indeed got kicked out of their developer community back in the day, I do know my way around the block there.  I realize it's a maintenance barrier for people who don't know it, and I sympathize with anyone trying to know it.  I have very high minded ideas about what a better build system would look like, but in 7 years I haven't produced it, so ha!  Glad there's 1 guy around, Weitjong, who really knows his CMake stuff.  If he got hit by a truck I personally would survive though.  I may finally give Premake4 a whirl, because if nothing else it's Lua scripted.  CMake has the virtue of being mostly feature complete, a heavyweight of industry, and that's probably a good fit to a 3d game engine's ongoing development.  Premake4 might turn out to be better for small end user applications though.  I suppose I will see.

Mainly the way I personally see Urho3D, is "this is easier than writing my own 3D engine from scratch."  A lot of gruntwork has already been done.  I expect that I'll eventually get to the point where I understand whatever there is to know about Urho3D's internals.  Then I will either decide, 1) holy cow, this code is a pile of needless confusion!  I surely don't want to cast my lot with [i]this[/i], or 2) this code is fine.  Time to build a game, maybe also add DX12 if not too much work.  (1) happened to me with Ogre3D, back in the day.  Especially stupid was their homebrewed shader language stuff.  From a long term sustainability standpoint, you gotta be kidding me!  Might have sounded good in the long, stable DX9 era, but really dumb once DX10 and DX11 are coming around the corner.

So I guess I inevitably defer the question of documenting internals.  Is there really something that needs to be known?  I'm sure I'll file an issue when I make such a determination.  But frankly, building 3d engines is not for amateurs, one must already have skills.  My view is adding any documentation needed for a professional level developer to continue with a support effort.

-------------------------

bvanevery | 2017-01-02 01:08:56 UTC | #4

[quote="Enhex"]
- Less strict contribution requirements. For example requiring AngelScript and Lua versions means the contributor has to learn how to use them and/or bind them. Instead the script versions can be added as tasks to complete before merging the contributed changes.[/quote]

Another example of that is GLSL vs. HLSL shaders.  Please, please, don't even consider trying to implement some kind of "common language" shader.  It's a completely stupid idea.  Industry will always march on and people will always have to do different shaders.  Just wait 'till Metal and Vulkan get here, you're going to be dancing with even more shaders.

I actually [url=https://github.com/urho3d/Urho3D/issues/1066]filed an issue[/url] that was proxmite / driven by this.  For some odd reason it rapidly resulted in a meltdown of discourse, which I think was more about 1 person than anything I said.  I think that person took the position that everyone should be an expert at everything, and simply write all of the GLSL's / HLSL's / Lua's / AngelScripts / CMake's needed.  I was taking the position that I don't want to do that.  I may not even be in a position to do that, because it may not even be my code, I may just be bug hunting someone else's code.  So what I wanted, was to stub things out in the build system or at runtime, and get lots of nice obnoxious warnings about what stuff hasn't been implemented.  BZZT!  BZZT!  You don't have a HLSL shader and you're running a DX11 engine, BZZT!!  That's all pretty doable.  Boring gruntwork to implement but quite doable.

It is possible that in the heat of the moment, with that particular issue filed, that I didn't do the greatest possible job communicating the intent.  But I was shocked that I would need to communicate such intent, as it's standard drill on every cross-platform "build system generator" project I've ever worked on, whether CMake, Autoconf, IMake, or hand built Makefiles.  Yeah, IMake.  Anyone remember IMake?   :laughing:  How about Linux kernel 0.99something?

Macro defines in shaders need some kind of "lint" or runtime check too.  It's very easy for a developer to miss one of the needed macros to suit Urho3D's proclivities.  I've had [url=https://github.com/gawag/Urho-Sample-Platformer/issues/57]an issue[/url] "in the wild" about this, still have been too lazy to definitively diagnose and iron that one out.  Has something to do with that code running at 1.5 FPS on my machines.  I currently prefer to work on [url=https://github.com/gawag/UrhoSampleProject]a simpler piece[/url] of "much faster" 10..15 FPS code.

-------------------------

