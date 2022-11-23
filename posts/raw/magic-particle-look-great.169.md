aster2013 | 2017-01-02 00:58:34 UTC | #1

I find that Magic particle look great, it's editor is easy to use. [url]http://www.astralax.com/[/url] But it's licence may not fit us.

-------------------------

cadaver | 2017-01-02 00:58:35 UTC | #2

Yes, it certainly looks visually nice. The core engine should not have integrations of binary-only proprietary libraries. So it would be up to a developer to choose to use this and modify Urho3D for integration. Looking at the API briefly it looks somewhat unprofessional, and contains slightly odd convenience functions, like searching a directory for particle effect files.

-------------------------

aster2013 | 2017-01-02 00:58:35 UTC | #3

It is hard to write a new particle system from ground up, the better solution is integrating an existed third-party particle system. But, which?

-------------------------

Hevedy | 2017-01-02 00:58:35 UTC | #4

In the Id tech 4 Doom3 have a particle editor/system (not very good)
[github.com/id-Software/DOOM-3/t ... s/particle](https://github.com/id-Software/DOOM-3/tree/master/neo/tools/particle)

-------------------------

aster2013 | 2017-01-02 00:58:35 UTC | #5

It is MFC, I hate it.

-------------------------

cadaver | 2017-01-02 00:58:35 UTC | #6

I think we discussed Spark before? That is probably the best free / permissively licensed C++ particle library. It's also huge so integrating / wrapping all of its features would result in a large amount of glue code, too.

-------------------------

aster2013 | 2017-01-02 00:58:35 UTC | #7

Yes, spark look good, but it never update since last year.  Last Update: 2013-05-27.

-------------------------

cadaver | 2017-01-02 00:58:35 UTC | #8

They have a SVN branch "spark2" which has been updated more recently. On their forum they said it's basically already in a good condition, but of course there's no telling when the 2.0 version is actually released.

-------------------------

Odin_KG | 2017-01-02 00:58:35 UTC | #9

[quote="cadaver"]and contains slightly odd convenience functions, like searching a directory for particle effect files.[/quote]
The editor of Magic Particles creates ptc-files for API, which contain emitters and folders. These functions allow to work with ptc-file like with file system.

-------------------------

cadaver | 2017-01-02 00:58:35 UTC | #10

Thanks for the clarification, in that case it makes a lot of sense.

-------------------------

aster2013 | 2017-01-02 00:58:35 UTC | #11

Odin is the author of magic particle.

-------------------------

indie.dev | 2017-01-02 00:58:37 UTC | #12

[quote="Hgdavidy"]In the Id tech 4 Doom3 have a particle editor/system (not very good)
[github.com/id-Software/DOOM-3/t ... s/particle](https://github.com/id-Software/DOOM-3/tree/master/neo/tools/particle)[/quote]
Doom3 is GPL.

-------------------------

Hevedy | 2017-01-02 00:58:38 UTC | #13

[quote="indie.dev"][quote="Hgdavidy"]In the Id tech 4 Doom3 have a particle editor/system (not very good)
[github.com/id-Software/DOOM-3/t ... s/particle](https://github.com/id-Software/DOOM-3/tree/master/neo/tools/particle)[/quote]
Doom3 is GPL.[/quote]

And use MFC but where is the problem ?
You can view the code and make some like that.
also you can see the code of UE4 for learn...

-------------------------

Odin_KG | 2017-01-02 00:59:48 UTC | #14

[b]Magic Particles 2.25[/b] was released. You can learn the details about new version here: [astralax.com/projects/particles/history](http://astralax.com/projects/particles/history)

-------------------------

rasteron | 2017-01-02 00:59:48 UTC | #15

Hey Odin_KG, Looks interesting, I'll keep an eye on this.

[quote="Odin_KG"][b]Magic Particles 2.25[/b] was released. You can learn the details about new version here: [astralax.com/projects/particles/history](http://astralax.com/projects/particles/history)[/quote]

-------------------------

Odin_KG | 2017-01-02 00:59:48 UTC | #16

[quote="aster2013"]Odin is the author of magic particle.[/quote]
Yes  :smiley:

[quote="rasteron"]Hey Odin_KG, Looks interesting, I'll keep an eye on this.[/quote]
Hey [b]rasteron[/b]. You can see some commercial games that use Magic Particles here: [astralax.com/titles](http://astralax.com/titles)

-------------------------

aster2013 | 2017-01-02 00:59:48 UTC | #17

@Odin_KG, Magic Particles 3D (Dev) 2.25 editor can not run on Windows 8.1.

-------------------------

Odin_KG | 2017-01-02 00:59:48 UTC | #18

[quote="aster2013"] Magic Particles 3D (Dev) 2.25 editor can not run on Windows 8.1.[/quote]
I am developing [b]Magic Particles[/b] using Windows 8.1
Could you give me more info?

-------------------------

aster2013 | 2017-01-02 00:59:48 UTC | #19

I will try it again tomorrow. Thanks.

-------------------------

aster2013 | 2017-01-02 00:59:52 UTC | #20

@Odin_KG
I run it again, it shows the register dialog, when I press the continue button, it shows the splash screen and then disappear silent. 

PS: What's your email?

-------------------------

Odin_KG | 2017-01-02 00:59:52 UTC | #21

[b]aster2013[/b]
[quote]I run it again, it shows the register dialog, when I press the continue button, it shows the splash screen and then disappear silent. [/quote]
Could you send to me the log-file ?
Magic Particles saves the log-file here: c:\Users\All Users\Particles\
Thanks a lot.

[quote]PS: What's your email?[/quote]
[support@astralax.com](mailto:support@astralax.com)

-------------------------

aster2013 | 2017-01-02 00:59:52 UTC | #22

@Odin_KG
I have sent email to you, please check it.

-------------------------

Odin_KG | 2017-01-02 00:59:53 UTC | #23

[quote="aster2013"]I have sent email to you, please check it.[/quote]
Yes. I received your message.

-------------------------

aster2013 | 2017-01-02 00:59:53 UTC | #24

Magic Particles in Urho3D.
[url]https://www.dropbox.com/s/s355x0a0clp6py4/MagicParticles.jpg[/url]

-------------------------

aster2013 | 2017-01-02 00:59:54 UTC | #25

I have submit the first version of Urho3D Magic Particle integration on my Urho3D repo, please get it from [url]https://github.com/aster2013/Urho3D[/url]. To enable it please add -DURHO3D_MAGICPARTICLE=1 to cmake command line. Current it work well on my Windows platform, I have not test it on other platforms now. These is a MagicParticleDemo under samples folder, AngelScript and Lua binding also added.

-------------------------

WangKai | 2019-03-18 07:08:21 UTC | #26

I saw https://github.com/effekseer/Effekseer today. Looks nice.

-------------------------

