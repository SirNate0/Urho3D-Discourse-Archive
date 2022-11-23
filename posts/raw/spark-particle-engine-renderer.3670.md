dakilla | 2017-11-19 07:46:18 UTC | #1

Hi

I'm building an urho3D renderer for the SPARK particle engine, I love its modularity.
Maybe I will build an editor too.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/d2104161112ea73e8ab2cbc5849ef7225856b817.jpg'>

https://github.com/fredakilla/uspark

Editor (Prototype in dev) (Windows x64 version) 
http://ge.tt/6zXXuNn2

-------------------------

johnnycable | 2017-10-19 08:47:24 UTC | #2

You mean this [SPARK](https://github.com/Synxis/SPARK) here?
Woah, didn't know about that! I searched for st similar a lot! 
Thank u man!

-------------------------

smellymumbler | 2017-10-20 17:40:23 UTC | #3

That's nice. What are the advantages compared to Urho's built-in particles?

-------------------------

dakilla | 2017-10-21 07:56:28 UTC | #4

It is fast and modular and easy to build complex effects. Its code is also quite flexible and scalable with its design to create your own extensions. 

Personally I use it because it also works independently of the 3D engine (I'm using Urho and another engine for my stuffs and I need and independent library to get same effects works in both engine) but without this constraint, it is also a nice alternative to urho built-in particles to consider if you like to render cool effects, and by default it offers some additional nice features :

- Independent Renderers per group (Quad and Point for now - what I added for urho - But I'd also like add a Marching Cube renderer to render fluid like, and also a mesh renderer to draw meshes instead of sprites) 
- Cool Modifiers :(Basic,Collider,Destroyer,EmitterAttacher,LinearForce,Obstacle,PointMass,RandomForce,Rotator,Vortex)
- Particles collisions (particles vs environment and particles vs particles)
- Differents built-in spatial Zones used by emitter and modifiers : Box, Cylinder, Plane, Point, Ring, Sphere.
- Emitters : from Normals zone, Random, Spheric, static, Sraight
- Different interpolators (basic, random, graph)
- Particles can triggers actions. 
...

The actual QuadRenderer (like urho billboard) for urho support differents options to orientate particles sprites :
CAMERA_PLANE_ALIGNED, CAMERA_POINT_ALIGNED, DIRECTION_ALIGNED, AROUND_AXIS, TOWARDS_POINT, FIXED_ORIENTATION

-------------------------

johnnycable | 2017-10-21 09:50:36 UTC | #5

Cannot compile on OsX. I get

> SPARK-spark2/external/pugixml/src/pugixml.cpp:3165:82: No type named 'basic_istream' in namespace 'std'

default project generated with cmake for xcode. It looks like a library problem.
If I change that to gnu libstdc++ I get:

> /SPARK-spark2/include/Core/SPK_Group.h:373:4: Non-type template argument of type 'size_t (SPK::Group::*)() const' cannot be converted to a value of type 'type' (aka 'returnType (SPK::Group::*)() const')

so now way. What to do?

-------------------------

dakilla | 2017-10-21 10:21:13 UTC | #6

disable xml at compile with this define : SPK_NO_XML
I know there is some errors with xml io, I will fix that later

-------------------------

johnnycable | 2017-10-26 11:23:51 UTC | #7

Gave a try with Xcode9 and I get various errors, last one:

> Rendering/Urho3D/SPK_Urho3D_QuadRenderer.cpp:140:32: Call to pointer to member function of type 'void (const SPK::Particle &, SPK::URHO::IUrho3DBuffer &)' drops 'const' qualifier

given up on Os X, seems XCode is not very forgiving.
Gonna try on Ubuntu...

-------------------------

dakilla | 2017-10-26 12:37:38 UTC | #8

Sorry I don't have any OS X. Actually, I only tested it on linux, but thanks for report I'll check this error.

Did you get the last commit ? I think this problem should be resolved in last updates I made many changes.

-------------------------

dakilla | 2017-10-27 05:41:24 UTC | #9

Some progress...

The Urho3D renderer for sprites works as expected (same render as internal opengl renderer).

I used my old procedural editor for urho (inacheved) to quickly integrate the spark engine. The modular design of spark works fine with this kind of editor. All the spark modules are not yet integrated, but basics are here.

https://youtu.be/fU-2uTLqZwo

-------------------------

Eugene | 2017-10-27 09:01:14 UTC | #10

BTW, what UI do you use?

-------------------------

dakilla | 2017-10-27 09:26:05 UTC | #11

It's a personnal fork of this tool (written in Qt) : https://github.com/enigmastudio/Enigma-Studio-4

-------------------------

johnnycable | 2017-10-28 15:36:53 UTC | #12

Today I tried building on my Ubuntu, but no luck. Seems QT Creator doesn't want to find Urho includes. Must be some trick to it. I googled for, but found no solution...

-------------------------

stark7 | 2017-11-14 17:28:37 UTC | #13

It will be a good day if SPARK will be part of the Urho3D 1.8 :slight_smile:

-------------------------

dakilla | 2017-11-19 07:42:12 UTC | #14

Hi,

I released a prototype of the procedural editor I'm working on, for urho and spark. (windows version)
I would like your opinion on it, any suggestions are welcomes.

I made a little tuto on how to use the editor: open "tuto.e4prj"

**EDIT**: I updated package with missing dll and I updated tuto :
 http://ge.tt/6zXXuNn2

-------------------------

dakilla | 2017-11-25 10:00:35 UTC | #15

Hi,

I now integrated SPARK inside Urho3D as thirdparty with cmake scripts.
repo: https://github.com/fredakilla/uspark

It can now be used like others Urho3D resources or manually to create effects from scratch.
See sample : 60_SparkParticles in repo.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/f/f3289ee5388c015e62eef2fa28c8791b36608283.png'>

-------------------------

yushli1 | 2017-11-25 10:15:41 UTC | #16

That looks really nice. Thanks for sharing it.
How is the performance when running it on mobile device?

-------------------------

rku | 2017-11-25 10:19:50 UTC | #17

This is awesome! Do particles react to scene geometry?

-------------------------

Eugene | 2017-11-25 13:29:34 UTC | #18

[quote="rku, post:17, topic:3670, full:true"]
This is awesome! Do particles react to scene geometry?
[/quote]

I'm 99% sure that no. It sounds like incredibly hard task.

-------------------------

dakilla | 2017-11-25 14:05:15 UTC | #19

[quote="rku, post:17, topic:3670, full:true"]
This is awesome! Do particles react to scene geometry?
[/quote]

Do you mean for collisions ?
If it is, actually not. SPARK handle collisions but in internal with its own colliders shapes (box, sphere, plane, cylinder...) so it is possible to fake some scene collision using spark shapes over urho scene geometry (for basics shapes).

But I think it should not be too difficult to extended it using bullet physics shapes and get real world collisions.

[quote="yushli1, post:16, topic:3670, full:true"]
That looks really nice. Thanks for sharing it.

How is the performance when running it on mobile device?
[/quote]

I can't test on mobile for now, I need to config a dev platform for that, but soon...
However, on desktop performances are really good.

-------------------------

johnnycable | 2017-11-25 14:20:19 UTC | #20

It works!
I had to comment out SPK_WITH_XML on Os X otherwise I get errors, but It's working!

![spark|662x500](upload://hX6sjuBjdv76DDBS8mP13Oli712.jpg)

-------------------------

dakilla | 2017-11-26 08:48:51 UTC | #21

[quote="johnnycable, post:20, topic:3670"]
I had to comment out SPK_WITH_XML on Os X otherwise I get errors, but It’s working!
[/quote]

Thanks for OsX report... But if this flag is not present you can't load spark effect files.
I just fixed the cmake build and a xml error, it's ok now for Linux and Windows, maybe this also fix OsX errors...
Can you give me the compiler errors if there are still some ?
Thanks.

-------------------------

johnnycable | 2017-11-26 12:21:16 UTC | #22

![spark|690x315](upload://y6Re6M6wq3xl1QvoA4UtjCV7OH1.jpg)

No more errors on Os X.
Whoa looks good!

-------------------------

SirNate0 | 2017-11-28 03:57:54 UTC | #23

Looks nice! What's the performance like compared to Urho's own particles?

-------------------------

dakilla | 2017-11-28 10:49:50 UTC | #24

[quote="SirNate0, post:23, topic:3670, full:true"]
Looks nice! What’s the performance like compared to Urho’s own particles?
[/quote]

Good question.
It need some advanced test to really compare both. But I made some quick test and spark is really more faster...

I build a similar effect for both system and tunes both side to render nearly same particles count. 

Some images with stats:
 
![spark1|643x500](upload://p04wCcMjwxFd4r23PvG4pPKqgEY.png)![urho1|643x500](upload://7q6V7B9e78doT1z6UG0BLu9kyKT.png)![spark2|643x500](upload://wsu5w9mS0Xw9LwvsWFgb5eiaosz.png)![urho2|643x500](upload://nBMG1q0um9g3iHQaeyAObIfvcja.png)


conclusions : 

- currently spark is faster and can render many more particles before dropping the fps.

- The rendering method is faster for spark  :  we can see in statistics that the urho particle emitter does not dynamically update the vertex buffer count (always at max count), only the index buffer count is updated - spark update both.

- A test without rendering (only particles update will be usefull too, but not tested yet)...

- I see in stats that UpdateDrawables and ReinsertToOctree methods are less expensive on spark side.

- spark is modular, when a feature is not needed (rotation, texture index, gravity, color interpolation,...) it is not computed in final effect, so a simple effect is really more efficient than a complex one. I think it's not the case in urho particles, that always compute all features...


**EDIT:**
I made a little mistake when printing the "visible particle count" values on screenshots.
good values are :

(SPARK) 93787 => 62525
(URHO) 60000 => 40000

(SPARK) 357077 => 239056
(URHO) 145350 => 96900

This value is the geometry indexCount / 6. I divided by 4...
However it doesn't affect other stats.

-------------------------

dakilla | 2017-12-02 14:40:50 UTC | #25

Hello.

I'd like to know if the core team would like to integrate this library into Urho3D as an official internal ThirdParty or if I continue to my dev on it as a standalone addon ? I'm facing some code design that will change considering this answer.
Thanks.

-------------------------

weitjong | 2017-12-02 16:08:17 UTC | #26

I have no issue to have it added as 3rd-party libs, as long as it is optional. I do have a concern though that the last commit in that library was made like 3 years ago.

-------------------------

dakilla | 2017-12-02 17:29:11 UTC | #27

I use the URHO_SPARK flag so compile can be optional.
Yes the last commit was made 3 years ago. I talk with the spark dev and officially the lib is suspended now.

However its state is full and stable and to my knowledge there is no other such particles library so evolved and with an open source license. 

Morehover I use my own fork of SPARK. As official one is suspended, I think it's more flexible to integrate new changes. This fork remove the latest commits of the official lib that broke the gcc compilation, I also fixed some bugs, removed the unused renderers (irrlicht, dx9, ogl) and created the urho one. I also plan to add new features to the core lib and continue the dev on this fork.

-------------------------

weitjong | 2017-12-03 01:49:55 UTC | #28

Ok..that sounds good to me.

-------------------------

elix22 | 2017-12-03 10:24:58 UTC | #29

Nice library porting .
Quick check on Android , it doesn't work well on Android (at least the demo )
To my understanding the only working/displayed  effect is "Spark/Effects/Spark1.xml" .

I didn't have time to debug it yet .

-------------------------

Dave82 | 2017-12-03 22:20:38 UTC | #30

It's interesting that SPARK is a CPU engine and runs so much faster than Urho3d's GPU transformed particles.

-------------------------

dakilla | 2017-12-04 06:01:54 UTC | #31

[quote="elix22, post:29, topic:3670"]
Quick check on Android , it doesn’t work well on Android (at least the demo )
[/quote]

I see this bug on emscripten too, manually build effects works, but loaded effects (from files) are not rendered. I'm investigating...

[quote="Dave82, post:30, topic:3670, full:true"]
It’s interesting that SPARK is a CPU engine and runs so much faster than Urho3d’s GPU transformed particles.
[/quote]

During my tests I found that BillboardSet (used by urho's particles) push on the vertex buffer the max particle count (set at particle creation) but doesn't update it according the real alive particles count during effect lifetime. so it's often bigger than necessary and need too much memory, I think it makes it actually not optimized for rendering dynamic particles. imho Fixing this first issue should render urho's particles a bit faster, after it will need others benchmark.

-------------------------

johnnycable | 2017-12-06 10:13:01 UTC | #32

Tested on Ipad with Ios 10.3, looks ok.

-------------------------

dakilla | 2017-12-16 00:01:44 UTC | #33

- Fixed bad loading effect files on some platforms (emscripten and android).
- Clean code and fix warnings compilations.

Use this branch for now : https://github.com/fredakilla/Urho3D/tree/sparkdev

-------------------------

elix22 | 2017-12-16 14:19:16 UTC | #34

I verified it on Android devices with versions 4.4.4 and 7.0
Works well.
Thanks for your work.

-------------------------

smellymumbler | 2018-11-26 04:16:00 UTC | #35

Hi @dakilla! Are you still using this in Urho?

-------------------------

dakilla | 2018-11-26 16:07:26 UTC | #36

I'm still using spark, but not with urho.

-------------------------

smellymumbler | 2018-11-26 16:53:08 UTC | #37

Have you abandoned the integration? Could you share with the us the most up-to-date repo/branch? I would like to keep it up.

-------------------------

dakilla | 2018-12-05 20:38:42 UTC | #38

Yes this integration is frozen since I use spark with others engines.

The most up to date urho3d integration is on my urho fork : https://github.com/fredakilla/Urho3D/tree/sparkdev

It use this SPARK modified version : https://github.com/fredakilla/SPARK (I made some  few modifications to get it compile on linux and emscripten, fix some warnings, clean, add qt project and cmake ...)

I'm also working on a node editor for spark : https://github.com/fredakilla/spkgen

-------------------------

dakilla | 2018-11-30 05:57:39 UTC | #39

I'm come back to Urho :stuck_out_tongue:
I just created a new repo for the urho spark integration using an external library to maintain it independently and outside of the urho engine: https://github.com/fredakilla/Urhox

@ [rku](https://discourse.urho3d.io/u/rku) I also added your imgui implementation (thanks)

-------------------------

GoldenThumbs | 2019-08-10 01:10:36 UTC | #40

This still active? If yes, is this going to be in a future update of Urho?

-------------------------

dev4fun | 2019-08-10 02:52:58 UTC | #41

I really liked this particle engine: http://effekseer.github.io/

Is japanese, unfortunately they don't use c++ 11 and I dont know about the code quality.. the best thing on this is the editor and samples. I guess its the best that we can find with particle editor (open source obviously). :slight_smile:

-------------------------

suppagam | 2019-09-03 04:25:53 UTC | #42

@dakilla do you still plan to make a PR for this?

-------------------------

