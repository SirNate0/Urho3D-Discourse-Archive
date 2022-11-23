darkhog | 2017-01-02 01:04:31 UTC | #1

Urho3D is very good engine and I love language was choosen to be Lua instead of some stupid Python variant like certain other open source alternative to Unity. 

However, I don't think it can compete with Unity without huge financial support (that is, unless some genius like Carmack, Romero or Jens Blomquist sees this project and decide to get involved out of his own free will). That's why I think Urho should find some niche which either is unfilled or filled with sub-par offerings.

In my opinion, it should be support for old, no longer officially supported consoles such as Dreamcast, PS2 or GameCube (preferably would include Saturn, PSX and N64 on the list as well, but I don't think porting here would be feasible as Urho in its current state probably wouldn't run on those systems even after some heavy optimizations).

There's enough docs on the web to make at least Dreamcast port, so I think we should start there and if people like it expand it further.

IMO, because of Urho's greatness as a toolset, it could be go to "devkit" for older (but not too old) systems, which could bring it to the spotlight on retro console dev scene (especially if LuaJIT/AngelScript could be ported as well).

-------------------------

HeadClot | 2017-01-02 01:04:31 UTC | #2

I personally would love dreamcast support :slight_smile:

Dreamcast was and still is an awesome console.

I posted the following on the unity forums. Regular members of the forum were honestly wanting it. But unity Official said no.

[quote]
Ok so unity did a little April's fools joke today/yesterday regarding a new build platform the ZX Spectrum.

That said - I would personally like to see Sega dreamcast support for Unity3D.

I have gone ahead and put this up on unitys feedback tracker. feedback.unity3d dot com/suggestions/sega-dreamcast-as-a-build-platform

Also worth the read - 
venturebeat dot com/2013/05/17/consoles-that-wont-die-the-sega-dreamcast/
[/quote]

-------------------------

GoogleBot42 | 2017-01-02 01:04:31 UTC | #3

Unfortunately, I think it would really difficult to create a renderer for each of these consoles... I know that GameCube and PS2 both have VERY different graphics systems from opengl and DirectX, plus, system memory is shared with gpu...  IDK about dreamcast.

If you know how the graphics systems of these work in more detail and are up for the challenge maybe you could fork Urho3D and add the renderers. :slight_smile:

-------------------------

darkhog | 2017-01-02 01:04:33 UTC | #4

GoogleBot, are you Urho dev? If so, it would be worth asking around in GC/PS2/DC homebrew communities, you may find willing programmers there. As I said, there are lots of docs available for Dreamcast, dunno for other consoles though.

-------------------------

GoogleBot42 | 2017-01-02 01:04:33 UTC | #5

[quote="darkhog"]GoogleBot, are you Urho dev?[/quote]

Nope I am not.  I am not familiar enough with the engine source code... Have paid close attention to the Directx11 and OpenGL3.1 additions that have been in progress lately and I am do know how Urho3D supports graphics systems (it unsurprisingly is similar in some ways to a lot of other solutions out there)... A LOT of work had to be done to add Directx11 support because of how different it is compared to Directx9 and OpenGL 2.1.  OpenGL 3.1 wasn't too bad if I understand correctly because of how similar it is to OpenGL 2.1.  But GameCube graphics, etc. would be a big challenge.  Not really because 3D is hard to use on those but because the 3D graphics API's are REALLY different from Directx9 (the graphics model that Urho3D is centered around).

In other words, the more different the graphics API is from Directx9 and OpenGL 2.1 the harder it will be to add support.  I do not see the devs making support for any non-standard graphics API's any time soon because of the work involved (and the lack of popular demand).  If you want support I suggest you fork the project and add try adding it. :wink:  If you get it working nicely maybe you can merge it with the central branch. :smiley:

I do agree that adding support would be beneficial because Urho3D could get new members from home brew communities but... I really don't know how much work would be involved other than it would probably be a lot for an open source project with a relatively small community.  

Again if you knowledgable in how these platforms work I think you should give it a shot!   :wink:  Personally, I don't think Urho3D should focus on this but should instead focus on bug fixing and supporting OpenGL 4.1 and adding new features.  Maybe Urho3D can finish their Lua bindings...

Also just looked a bit at dreamcast and it looks kind of scary... I read this on wikipedia "The Saturn was a CD-ROM-based console that displayed both 2D and 3D computer graphics, but its complex dual-CPU architecture made it more difficult to program for than its chief competitor, the Sony PlayStation."  So far seems this console in particular might be a challenge based on their decisions to not be very supportive of devs.

-------------------------

darkhog | 2017-01-02 01:04:33 UTC | #6

Nope, Saturn and Dreamcast are two different consoles. Also if I could add support myself, this thread would go something like this: "Hello, I'm adding Dreamcast support to Urho. What do you think?". As I've said it would be good to ask around homebrew community to get some Dreamcast coders on board with this idea.

Additionally, again, it's about finding a niche. Let's face it and I'll be blunt: Urho never will be AAA engine without extreme financing. I think they understand that, so they're targetting indies. BUT that niche is filled by Unity and recently UE4 and CryEngine, probably soon Source2 as well. But wait, people still make homebrew for the old consoles with 3D support, but SDKs available are terrible. If we could make their lives easier, then we'd get popularity in those circles and they'd probably also write about us on sites like Kotaku. Hmm...

-------------------------

cadaver | 2017-01-02 01:04:34 UTC | #7

Urho already has its niche, which I would call "bullshit-free good performance game and rendering library that is unrestrictive open source and has relatively clean architecture." It's quite a given that it cannot compete with eg. Unity in features and tool support, but neither does Unity give you the full source for free.

The graphics pipeline in Urho is so far always based on vertex & pixel shaders, and the low-level rendering abstraction (Graphics class) has the same functions independent of the underlying API being used (D3D9, D3D11, OpenGL..) Adding support for a platform with no shaders but fixed function instead, would disrupt the abstraction and force fixed function concepts into it, which would to me seem like going backwards.

There might be some merit to a fork which would drop shader support and implement a graphics abstraction based on the features of old consoles (+ "emulation" of them on modern desktop platforms.) But I don't think the official Urho development should have anything to do with it.

-------------------------

TikariSakari | 2017-01-02 01:04:34 UTC | #8

Just out of curiosity why dreamcast support out of all of them? As far as I remember the time I was a teenager, only one person had dreamcast. I do admit that shenmue was one of the most stunning game graphic wise back then and I did enojy playing countless hours of Soul Calibur, but still the console didn't really do too well back in the days. It still annoys me even today that Shenmue 3 never came out and I will never know how the story ends.

-------------------------

GoogleBot42 | 2017-01-02 01:04:34 UTC | #9

[quote="darkhog"]Nope, Saturn and Dreamcast are two different consoles. Also if I could add support myself, this thread would go something like this: "Hello, I'm adding Dreamcast support to Urho. What do you think?". As I've said it would be good to ask around homebrew community to get some Dreamcast coders on board with this idea.[/quote]

I am trying to say that it seems that there really isn't anyone who wants to... So if you can that might be the only way that it will happen.  Urho3D is focused on modern things like windows phone and HTML5 + WebGL.  If the devs lose focus this may cause the project to stall which is the last thing that should happen.

[quote="darkhog"]Additionally, again, it's about finding a niche. Let's face it and I'll be blunt: Urho never will be AAA engine without extreme financing. I think they understand that, so they're targetting indies. BUT that niche is filled by Unity and recently UE4 and CryEngine, probably soon Source2 as well. But wait, people still make homebrew for the old consoles with 3D support, but SDKs available are terrible. If we could make their lives easier, then we'd get popularity in those circles and they'd probably also write about us on sites like Kotaku. Hmm...[/quote]

You should ask those homebrew communities if they would port Urho3D.  After all, who would know better on how to do it than them right? :wink:  I do agree it would be a nice way to get even more Urho3D users but Urho3D just doesn't have the manpower to make the port.

[quote="cadaver"]Urho already has its niche, which I would call "bullshit-free good performance game and rendering library that is unrestrictive open source and has relatively clean architecture." It's quite a given that it cannot compete with eg. Unity in features and tool support, but neither does Unity give you the full source for free.[/quote]

Couldn't have said it better.   :slight_smile:   That is exactly why I use Urho3D.  Just when I was begining to think that there wasn't a game engine that is fully unrestrictive, under constant development, and includes support for useful gaming libraries builtin... I found Urho3D!  :stuck_out_tongue:  :wink: 

[quote="cadaver"]Adding support for a platform with no shaders but fixed function instead, would disrupt the abstraction and force fixed function concepts into it, which would to me seem like going backwards.[/quote]

Very good point!  How did I not recall that about these consoles...

[quote="cadaver"]There might be some merit to a fork which would drop shader support and implement a graphics abstraction based on the features of old consoles (+ "emulation" of them on modern desktop platforms.) But I don't think the official Urho development should have anything to do with it.[/quote]

Hmmm... I agree Urho3D should not regress...  if you want to make the port darkhog maybe the two Urho3D branches could be combined by disabling some features that are not compatible with old consoles.  But IDK, this might not even be possible without considerable effort at best. :\


EDIT: on the note about that Urho3D doesn't have developers... While the pool is relatively small right now I think it will only grow.  Take irrlicht for example.  Their last release was a year and a half ago.  They only support DirectX9, OpenGL2.1, and some software renderers...  Plus, they don't even have an official mobile port.  There is coppercube but that isn't under an open licence and isn't geared towards c++ devs.  Irrlicht doesn't support any gaming libraries.  I think devs that are sick of irrlicht will come here just as I did. :slight_smile:

-------------------------

Siana | 2017-01-02 01:06:13 UTC | #10

Hello there,

Myself a random person myself who is fairly well familiar with Dreamcast and am looking for something curious to port onto it. Currently porting a 2D game (but a pretty elaborate one, originally Direct3D-rendered) that i will announce later and elsewhere - one of the biggest tasks is crunching down 80MB worth of memory allocation per level down to perhaps 1/10th of it, just goes to say, if you have the technical foundation ported, doesn't mean it will be useful for existing software on such a limited platform. Came here through google.

I'm not familiar with Urho3D, but i disagree with Cadaver in principle. I believe a shader-friendly abstraction is advantageous even for fixed function hardware. The abstraction should merely not enforce shader language nor shader semantics. Then a description language can be defined, akin to Quake3 shader language :slight_smile: that will merely trigger and combine backend's rendering features.

As far as higher level parts depend on specifics of shader language, and given Urho's feature set, that looks like a shit ton of work, perhaps not within my capabilities as far as time goes. I'd like to ask the OP, Darkhog, though, what the purpose of this exercise of porting an engine is? Are YOU specifically an application developer, a user of the engine? Can a limited subset of the engine features be encircled that you need so volunteer X doesn't need to work his or her ass of for something nobody will ever use? If you are not, then who is this for? If this doesn't result in a released software that people can run and will enjoy, then it's a wasted effort. It will just be another useless repo on github.

-------------------------

cadaver | 2017-01-02 01:06:14 UTC | #11

Hi and welcome,
the abstraction you describe certainly makes sense for an engine that could hypothetically render both in shaders and in fixed function, and would have been designed for that from the start. The trouble with adapting this to Urho3D is that Urho has deliberately chosen the graphics abstraction to be at the low level, assuming support for actual GPU shader programs in some shader language that can be compiled with different compilation defines. The low (API specific) level knows nothing of things like lights or even camera view / projection matrices, it just binds shaders and feeds them with uniform data from the higher level. 

With the current abstraction, you could make a fixed-function backend only by seriously ugly hacks, basically by watching for shader names, compilation defines and uniform names commonly used by Urho's higher-level constructs (Material / Technique) and the higher-level scene rendering code.

-------------------------

