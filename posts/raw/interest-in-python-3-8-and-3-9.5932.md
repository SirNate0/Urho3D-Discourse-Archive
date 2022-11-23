bvanevery | 2020-02-17 21:54:42 UTC | #1

Python is currently at version 3.8.1.  Version 3.9.0 will be released [late this year](https://www.python.org/downloads/release/python-390a3/).  The Python community is split between versions 2.x and 3.x of the language, with various vested interests refusing to move forwards.  This schism happened quite awhile ago, as Python 3.0 was released in December 2008.  Python 2.7.x was officially given [end-of-life on January 1, 2020](https://www.python.org/dev/peps/pep-0373/), with version 2.7.18 code frozen at that time.  It will actually be released in mid-April, 2020.  There will never be a Python 2.8.

Why talk about Python, when Urho3D already has its hands full with Lua and AngelScript?  Because improving things with either of those languages is not easy or some kind of "free move".  Lua versions have substantial incompatibilities.  tolua++ would need to be depreciated, so doing a new C++ binding regime while phasing out the old one, is *work*.  Bumping the AS version is easy, but I hear that despite its C++ friendliness, no *automated* C++ wrapper exists for it.  I haven't investigated that yet so YMMV, but *manual* labor to produce C++ wrappers, clearly isn't the equal of an automated regime.  When someone contributes an Urho3D pull request, they often haven't done AS or Lua bindings, which greatly delays or stops their work from getting into core.  That's unsustainable.  Whereas with Python, I expect that an automated C++ binding regime is out there, since Python's ecosystem is large.

Python will never be the performance equal of some of the other scripting language choices.  However it offers something that other languages do not: a *strategic ecosystem.*  Python is favored in the 3d modeling and animation world now.  Autodesk has a stranglehold on the market with its 3DSMAX and Maya products, both of which do Python nowadays.  It's Python *2.x*, which is regrettable, but it's still Python.  When I last checked on it, there was not a peep out of them about ever moving forwards, but that was some time ago.  Maybe official end-of-life will get them moving someday?  Maybe it'll depend on what their paying customers actually clamor for, so they'll sloooowly get around to it.  I don't expect the 2.x holdouts to manage their stubbornness forever.

Meanwhile, Blender 2.80 is using Python 3.x.  I believe it's 3.5.  Python numbering culture is that minor releases don't break anything.  3.x is 3.x is 3.x.  If a Blender person wanted to start banging on Urho3D, I can't reasonably expect any problems for them to do so.

The popular Godot 3D engine, which I'm sure many of you realize is sucking the air out of the room for projects like Urho3D, uses a bastardized Python called GDScript.  It's not real Python.  For me personally that's a dealbreaker.  I'm not trusting my game scripting content to some rinky dink one shot engine developer!  I've got complex coding stuff in mind, and the only things I'm going to use are either a standard language, or *my own* language, which I don't actually have implemented at this time.  There's no reasonable future for GDScript outside of Godot, it is simply not a career skill or valuable in the marketplace.  Python 3.x, in contrast, is something that people can reuse for all sorts of things and *make money at*, while they're trying to survive as indie game developers.

My other reasons for rejecting Godot are it's 2D oriented, mobile oriented, and not strong at 3D.  Pity, as their development effort has other strengths going for it.

Banging up the UI of a game in Python 3.x is a sane idea.  As a lone wolf indie, I need to have this sort of thing.  Banging it up in Lua isn't a horrible idea, for instance Blizzard did it for World of Warcraft, but it does beg questions about which version of Lua.  Picking a Lua isn't a free move, because of the C++ binding issue.  I have no doubt in my mind, that Python is better suited to larger scale applications development, than Lua is.  Witness Blender.

Meanwhile, from an ecosystem standpoint, I don't really see AS as even a contender.  I don't want to undermine an extant ecosystem, as it's important to preserve existing user base.  But really, if you're sitting down to write something important, why AS rather than Python 3.x?  I don't see any money or life blood coming from that.  The world of 3d modeling and animation has pretty much voted on what works, and it's Python.

I haven't even checked on whether anyone forked Urho3D to do any kind of Python.  For the record I'm also not interested in "collect all languages" binding efforts.  I talk about Python because it has specific strategic value, that other languages don't have.

In particular, I have no interest in C#.  If you want that, I have no idea why you're not using Unity.  And if *that* isn't good enough, I have no idea why you're not doing [NeoAxis](https://www.neoaxis.com/).  It came from Ogre3D, some dev who said "I wanna do C#!" and also said, he wanted to get *paid* to sustain it.

C# is not a scripting language, you can't just interpret it in plain text and have your results immediately available for your prototyping.  It's the tedious compile cycle drill, and it doesn't offer anything interesting as a language, for someone whose tastes might run more towards Lisp or Forth.  In any event there are plenty of "new devs coming up", who really only know C# as their world, who want to go do stuff in C#.  There are plenty of open source 3d projects already doing that sort of thing.  Between those and Unity absorbing the vast majority of game devs, I see no motive whatsoever, to try to compete with anyone on a C# basis.  It's *suicide*.

If Jonathan Blow finally ships [Jai](https://en.wikipedia.org/wiki/Jonathan_Blow#JAI_language), we'll talk about that.  I hear some early betas are going around now.  But we're also 5.5 years out, and it isn't here yet.  And I didn't get my own language done either.  So here we are, talking about what to do with Urho3D scripting.  Looking over the archives, I'm surprised that my first minimal involvement with Urho3D was over 4 years ago.  Some CMake build bug stuff.  I probably had just finished my cleanup of the moribund Ogre3D ecology and ditched it.

-------------------------

SirNate0 | 2020-02-17 22:02:53 UTC | #2

I'm interested in Python 3.x support. In fact, at the moment I'm (slowly) working on a mostly automated binding generator based on libclang and pybind11. We'll see how it goes - I started over a year ago and then the project got put on the back burner, but I've recently started back on it.

-------------------------

George1 | 2020-02-17 23:33:26 UTC | #3

Python is good, but it is slow compared to other variant.

I would question about your comment on C# and scripting.
e.g.  CS-Script
etc. 

You can script and have what ever return you desired.
You could do live scripting if needed.  It is an implementation issues rather than the language is not capable of.   

My text serves no purposes but only to defend to C# a little. Because I'm familiar with using it.

-------------------------

bvanevery | 2020-02-18 00:05:57 UTC | #4

I've been studiously ignoring the C# ecosystem since it first came out.  Microsoft *never* integrated the C# side of its business strategy, with the C++ DirectX game development side of things.  First there was Managed DirectX, and then they pulled the plug on that.  Then there was XNA, and they pulled the plug on that.  I never had any real interest in what Mono was doing, so when they started having trouble, and then subsequently got help (? buyout?) from Microsoft, I really didn't care.  I was interested in F# for a time, which is an OCaml derivative.  It was always historically too awkward to deal with the DirectX COM interface binding problem.  After years and years of occasionally poking at this, I gave up trying.  I just accepted that if I got back into DirectX's orbit again, I would have to deal with C++.

With this kind of blase background, I've been totally unaware of C# interpreters such as CS-Script.  That solves one problem, which is seeing results immediately.  Let me guess though: performance isn't anything to write home about?  Like doesn't buy you anything over Python.  Is your debugging life any easier, crossing a compiled C# to interpreted C# boundary?  Not gonna be shocked if it isn't, but you tell me.

I don't like C#, Java, or C++.  I'm not stuck with the first 2, so I don't deal with them.  C++, DirectX on Windows pretty much forces me to deal with it.  Otherwise I wouldn't.  I've chased *many* languages over the years, seeking a C++ replacement.  The problem is, those languages always turn out to be run by academics, or single developers who abandon their projects.  They get to some OpenGL at best, which isn't even important anymore.  Never do these efforts really intersect the Windows DirectX game industry.  Those people just keep chugging along with C++, with some C# inroads.  And Microsoft never pushes C# as a good fit for DirectX development, the support simply isn't there.

Maybe someday Jonathan Blow will save us all with Jai.  Can't wait right now though.

Blow also convinced me that Rust isn't worth bothering with.  Too much bondage and discipline and not solving the real problems of a game developer.  I've checked on the Rust 3d engine ecosystem occasionally, and last I looked sometime last year, I didn't see anything compelling.  I always leave myself room to be surprised, but it's been *awhile* now and I haven't seen anything compelling coming from that direction.  Especially if DirectX is a hard requirement.  Not saying they don't ever deal with it, but there's way too much OpenGL DNA in most open source projects.  It's stale, hard to use, and all needs to be retired.

-------------------------

George1 | 2020-02-18 00:12:04 UTC | #5

I don't mean to bash python.  As I'm using it in in my current work for AI stuff.   
The good thing about it is in its short syntax and many open libraries.

-------------------------

bvanevery | 2020-02-18 01:18:19 UTC | #6

Yeah, as I said above in long form, and will try to say now in short form, Python isn't a *performance* argument.  It's an *ecosystem* argument.  Here's a current article on [Lua's ecosystem troubles, compared to Python](https://lwn.net/SubscriberLink/812122/bd245e8bd1018885/).  Additionally, in the domain of "things 3d", there's a clear winner nowadays.  In 3d modeling and animation, it's Python.  It's not C#, it's not Javascript, it's not Lua, and it's not C++.

The best performance thing for a scripting language, probably has not yet been written.  LuaJIT is pretty good.  It's also a development dead end.  If only Jai would ship.

-------------------------

bvanevery | 2020-02-20 19:43:24 UTC | #7

I'm learning that nobody on r/gamedev takes Python seriously for 3d game engines.  In open source, a MIT/permissive licensed 3d engine that does DirectX 11 or newer with Python, and is under active development, may not even exist.  I have not previously run into any such thing.  Panda3D for instance is back on DX9.  Generally speaking when I go searching for the keyword "DirectX" in Python communities, I get nothing.

The architecture for a Python 3d engine is not straightforward equivalent to Lua or AngelScript.  You simply don't embed Python, the core Python developers are pretty hostile to it being used that way.  Rather, your app is Python, and you call C.  With 3rd party stuff, you presumably call C++.

Python performance issues are dominated by the [Global Interpreter Lock](https://realpython.com/python-gil/) problem.  This can turn a multi-threaded CPU-bound app into essentially single-threaded.  Architecting to avoid this problem is non-trivial.  I wonder what Panda3D does?  Anyways, it's not simply a "free move" to go grab a Python 3.x C++ binding thing and call it a day.  There's real architectural work to think about.  So, back to the drawing board, as compared to Lua or AS.

At least [one Maya employee](https://forums.autodesk.com/t5/maya-ideas/upgrade-to-python-3-x/idi-p/7963375) is aware of the need to move on to Python 3.x in industry:

>tj.galda, Employee, 05-09-2018 08:56 PM
>
>We are indeed working with the VFX Reference Platform and have been for some time.  Python 3 is on our radar for sure and we're working out the timing of that as well as the technical approach.  The trick for us is we don't want to build a version of Maya that people don't want to buy, so need to figure out the best way to bridge across the versions.
>
>We're listening, your input on how you'd like to see that work out is valuable.  Every time I visit a studio, we check to see how ready people are for Python 3 & what timing would work well for teams.

The [VFX Reference Platform](https://vfxplatform.com/) is indeed something that Autodesk is on record as participating in, so perhaps tj.galda's statement can be taken as sincere.  Python 2.7 being end-of-lifed may finally force movement, and Autodesk may have planned all along to wait for that, before bothering to move forwards.  Calendar Year 2020 is supposed to have Python 3.7.x as the reference platform:

>The move to Python 3 was delayed from CY2019 to CY2020 due to:
>
>* No supported combination of Qt 5.6, Python 3 and PySide 2 so Qt first needed to be upgraded.
>* Upgrade of both Qt and Python in the same year was too large a commitment for software vendors and large studios.
>
>Python 3 in CY2020 is a firm commitment, it will be a required upgrade as Python 2 will no longer be supported beyond 2020. Software vendors are strongly encouraged to provide a tech preview release in 2019 to help studios with testing during their Python migration efforts.

Even if Autodesk doesn't want to move forwards, industry competition will presumably force their hand over time.  And be advised, the existence of VFX Reference Platform demonstrates that Python *is the thing* in the visual effects industry.  It's not any of the other languages under discussion.

Sure you don't want to run the performance parts of your game with Python.  But building the *non-performance* parts of your game with Python is not crazy, it's actually a pretty good idea.  And there's all this *art asset* stuff that is going to be coming through the Python world.  That's a basis for Urho3D to compete, with both the likes of Godot that only has GDScript, and Unity that has C#.

Especially since, it looks like nobody's thought to do it.  Seems that Unity started with a Python-like (? someone's claim) language called Boo, and Javascript, and C#.  XNA devs decamped when Microsoft abandoned it, and went to Unity.  C# demand grew, and eventually Unity nixed the other 2 offerings.  The Python universe didn't get its act together and didn't get any love.  They were probably living out the 2.x vs. 3.x schism over this same period.

Over the past year, r/gamedev is filled with noobs who come and say, "I know Python, how do I develop games in that?"  They get directed to stupid stuff like Pygame (well I'm sure it's fine for what it means to do, but it's amateur hour) or other 2d offerings, or Godot with its GDScript because it's hand wavy like Python.  All of those noobs could be Urho3D users.

Issues of scale to consider on Reddit.  Number of Members in sub:
* r/programming - 2.5m
* r/Python - 504k
* r/gamedev - 403k
* r/learnpython - 305k
* r/blender - 196k
* r/Unity3D - 169k
* r/csharp - 133k
* r/cpp - 121k
* r/3Dmodeling - 53.3k
* r/vfx - 39.8k
* r/godot - 33.6k
* r/Maya - 26.1k
* r/3dsmax - 16.2k
* r/lua - 8.9k
* an AngelScript sub does not exist

Poor lost souls show up in r/Python fairly regularly looking for 3d stuff, and they've got nothing.

Well ok, some people remember Panda3D, but it has limitations.  DX9.  They do have a Vulkan branch, but they only talked about it in [their blog in 2017](https://www.panda3d.org/blog/a-look-behind-the-curtains/).  They've had several releases since then, and they don't even talk about OpenGL much, let alone Vulkan.  Looks like Apple depreciating OpenGL [rattled them](https://www.panda3d.org/blog/june-2018-development-update/).  Didn't put a hot match under them about rendering backends though.  Their blog posts read a bit slow in that regard.  Faster is library integration stuff, like Python 3.8 for instance.  They're still transitioning to CMake from their makepanda build tool.  They've got some crowdfunding.

Pity that the GIL is standing in the way of glory.  I don't know that allowing it to invade the top level UI of a game is actually a good idea.

-------------------------

bvanevery | 2020-02-20 03:16:38 UTC | #8

Tool around in the archives long enough, this is what you find out.

FOSDEM '20, occurred 1 & 2 Feb.

>[# Python for Godot](https://fosdem.org/2020/schedule/event/gamedev_python_for_godot/)
>
>Godot is an incredible open source game engine. Among it key features, it comes packed with a script language called GDscript and loosely based on Python. But could it be even better ? Could we use the real Python to code our game on Godot ?
>
> And maybe even more important, is it really a good idea ?
>
> [...]
>
> Finally we will discuss the pros and cons about using Python as a script language for Godot vs the traditional GDscript.

Video available, about 20 minutes.  Summary: Godot has a C API.  Author uses Cython to make Python available.  Author's [Godot Python](https://github.com/touilleMan/godot-python) repo.  Generates a bunch of bindings.  His optimization culture is to get users to start with Python, then have them rewrite code in Cython if they need it to be faster.

Sales pitch on [Cython website](https://cython.org/) :

> All of this makes Cython the ideal language for **wrapping** external C libraries, **embedding** CPython into existing applications, and for **fast C modules** that speed up the execution of Python code.

[Cython and the GIL](https://wiki.python.org/moin/GlobalInterpreterLock):
> * in Cython the GIL exists, but can be released temporarily using a "with" statement

[Releasing the GIL](https://cython.readthedocs.io/en/latest/src/userguide/external_C_code.html#releasing-the-gil)
[Acquiring the GIL](https://cython.readthedocs.io/en/latest/src/userguide/external_C_code.html#acquiring-the-gil)
[Conditional Acquiring / Releasing the GIL](https://cython.readthedocs.io/en/latest/src/userguide/external_C_code.html#conditional-acquiring-releasing-the-gil)
[Declaring a function as callable without the GIL](https://cython.readthedocs.io/en/latest/src/userguide/external_C_code.html#declaring-a-function-as-callable-without-the-gil)

Although having a succinct mechanism is nice, I'm seeing a problem.  To the extent that one would want to use Python to *directly control Urho3D*, I think its locking mechanics intrude into Urho3D's execution.  That is, if you think you're going to write Python code to control Urho3D *at a rather low level*.  Writing Python wrappers above Urho3D wouldn't be any problem.  But providing an Urho3D user with the completely exposed Urho3D API in Python, may be *committing performance suicide*.

It all hinges on what a "Python Object" is, and whether a wrapper around an Urho3D C++ object, becomes such.  Whether someone is wanting to pass things from C++ to Python to different C++.  The C++ cannot manipulate any "Python Object", it becomes in essence "Python code, subject to GIL" the moment it does so.

-------------------------

SirNate0 | 2020-02-20 03:22:50 UTC | #9

Unrelated to the most recent posts, I've successfully created Python bindings for Urho, (as in it can create and run an application without crashing). These are (for the most part) automatically generated using the python wrapper for libclang. Presently they are just python 2.7, but that's just what I had configured before (I believe pybind11 supports both, so it's just a matter of switching the libraries and includes when building). It is by no means feature complete (probably not really even ready to be shared given all the hard-coded paths in the Makefile), but if you guys want to track my progress you can at:
https://github.com/SirNate0/PYrho3D
PS: Suggestions (including about the name) are welcome.

-------------------------

bvanevery | 2020-02-20 03:27:08 UTC | #10

I don't think the name matters, if your goal is to get it into Urho3D.  Your repo is then only a holding tank.

I'd be wondering about pybind11's theory of operation, with respect to GIL.

-------------------------

SirNate0 | 2020-02-20 03:31:10 UTC | #11

Maybe later, but for now it certainly doesn't belong there. Potentially it never will, given it takes a few minutes to build the one file to produce the python module. On the other hand, we can always hope for it to get included...

In regards to pybind11 and the GIL, this may provide some insight https://pybind11.readthedocs.io/en/stable/advanced/misc.html#global-interpreter-lock-gil

-------------------------

bvanevery | 2020-02-20 06:23:09 UTC | #12

[pybind11 - Global Interpreter Lock (GIL)](https://pybind11.readthedocs.io/en/stable/advanced/misc.html#global-interpreter-lock-gil):
> When calling a C++ function from Python, the GIL is always held. The classes `gil_scoped_release` and `gil_scoped_acquire` can be used to acquire and release the global interpreter lock in the body of a C++ function call. In this way, long-running C++ code can be parallelized using multiple Python threads. Taking [Overriding virtual functions in Python](https://pybind11.readthedocs.io/en/stable/advanced/classes.html#overriding-virtuals) as an example, this could be realized as follows (important changes highlighted):

I think this means somewhat unpleasantly peppering Urho3D code with Pythonisms.  It's like the physical realization of the "invasive tendrils" I imagined in my post above.  It reminds me very much of "Managed C++" issues back in the day, nowadays "C++/CLI" application design.  You don't get to escape Python's execution model.

Actually I'm getting mixed up.  "Python calling C++", the GIL is always held.  "C++ calling Python", the GIL can be released, if you write a little bit of Python-specific C++ code.  But how does the latter even work?  Guess I have to RTFM more about theory of operation.

The Cython approach looks like it would be cleaner, as a matter of layering and avoiding source code pollution.  "Python calling C++", you have the choice of releasing the GIL, as long as you don't do anything to a Python Object.  This choice is written in the Cython code, which is a superset of C, C++, and Python code.

I don't think a C++ contributor to Urho3D should have to know a darned thing about Python GIL concerns.  Or any of the scripting language concerns, for that matter.

Cython claims to cover "most of" C++.  I hope *that* isn't a minefield.

[Cython, pybind11, cffi – which tool should you choose?](http://blog.behnel.de/posts/cython-pybind11-cffi-which-tool-to-choose.html#)
**Cython** is Python with native C/C++ data types.
**pybind11** is modern C++ with Python integration.
**CFFI** is Python with a dynamic runtime interface to native code.

CFFI is not appropriate for Urho3D.  It's a dynamic runtime pig.  *That said*, PyPy is a JIT compiler replacement for CPython, and it [strongly recommends CFFI](https://www.pypy.org/compat.html).  It implements Python 3.6.9 and 2.7.13.  It [still has the GIL](https://pypy.readthedocs.io/en/latest/faq.html#does-pypy-have-a-gil-why).

A [repo giving examples](https://github.com/tleonhardt/Python_Interface_Cpp) of Cython, SWIG, PyPy, CFFI, and pybind11 with a simple Fibonacci benchmark.
> the performance [of CFFI] is decidedly worse than the other options presented here unless it is used in combination with PyPy, in which case the performance is truly excellent.

Someone wrote a raytracer in Python, then wrote about [optimizing it](https://www.reddit.com/r/Python/comments/e4mv0n/my_notes_on_optimizing_a_python_raytracer/).  They did single and multi threaded versions.  PyPy was much better than CPython.  C was much better than PyPy.  Interesting because it approximates some kinds of heavy game load problems, if not others.  Also because someone would bother *in Python*.  Says something about the VFX industry influence I think.

-------------------------

Modanung | 2020-02-20 11:08:06 UTC | #13

Cool you're picking this up. About the name, I think Pyrho3D looks better than PYrho3D. People will understand it's a portmanteau.

-------------------------

Eugene | 2020-02-20 15:43:29 UTC | #14

Are there any examples of whole binding API? Example shows only a few functions.

-------------------------

bvanevery | 2020-02-20 16:27:27 UTC | #15

[quote="Eugene, post:14, topic:5932"]
examples of whole binding API?
[/quote]

"Surely", somewhere, but my mind is stuffed with many concerns and I haven't really been looking for production examples of Cython, pybind11, or PyPy+CFFI. 

In [that 5-way comparison](https://github.com/tleonhardt/Python_Interface_Cpp#pybind11):
>pybind11 is essentially what arose from the ashes of Boost.Python. **It is the newest of the tools presented here**, but it is already better than Boost.Python ever was.

So, maturity?  It warrants more research.

I don't really understand CFFI yet.  The only way Urho3D would realistically use it, is marrying itself to PyPy.  The limitation of the PyPy approach is not all Python libraries are going to work with it.  Users would have to go through special pain to integrate those.  I have trouble visualizing how much that matters for a game developer.  Or a VFX developer, since a lot of my argument is about attracting that crowd, to get more bodies into Urho3D's door.  There's not really a 3d game development ecosphere to understand with Python, it's not something game developers do.  Production pipelines, yes, but 3d engine work, no never.  2d, maybe there's something to learn, maybe not though.  I haven't researched 2d Python mobile or web games.

Godot Python uses Cython.  That's 100% proof of concept that it can work for Urho3D, *if* you accept the multiple layers of hair to do things that way.  Cython's other proof of concept seems to be in scientific batch processing work.  For instance, Cython's website has a sidebar where a SciPy developer talks about the value to them:
> »SciPy is approximately 50% Python, 25% Fortran, 20% C, 3% Cython and 2% C++ … The distribution of secondary programming languages in SciPy is a compromise between a powerful, performance-enhancing language that interacts well with Python (that is, Cython) and the usage of languages (and their libraries) that have proven reliable and performant over many decades.
>
>For implementing new functionality, Python is still the language of choice. If Python performance is an issue, then we prefer the use of Cython followed by C, C++ or Fortran (in that order). The main motivation for this is maintainability: Cython has the highest abstraction level, and most Python developers will understand it. C is also widely known, and easier for the current core development team to manage than C++ and especially Fortran.« → [Pauli Virtanen et al., SciPy](https://www.nature.com/articles/s41592-019-0686-2)

So you can surely get a scientist to follow the Cython drill :-) but that doesn't imply a VFX person would do it.  I suppose I should learn about VFX and Cython.

And whether we'd want to push a game developer to do it, is a matter of *taste*.  No basic model to follow, because Python isn't a 3d gaming thing.  *Yet*.

Actually Cython has all kinds of testimonials from various people that it "works for them".  For instance, PayPal.  Their sidebar is really funky when you expand it.  It's like *blah blah blah blah blah blah blah* thin narrow strip running down the right side of my widescreen.

-------------------------

SirNate0 | 2020-02-21 06:55:55 UTC | #16

If you mean the generated script API, it's probably about 50% right now. If you look at the commented out functions, there are some (esoteric) indicators about which part is unsupported in the given unbound function. 

A large portion of the not-yet-covered functions are due to not yet having fixed the operator support (I believe I had it working at one point last year, but disabled it, though I forgot why at this point). Other key remaining features are supporting more than just VariantMap, VariantVector, and StringMap containers, and telling the binding-generating code that Shared/Weak/ExternalPtr return types and parameters are allowed. In addition, presently no enums are supported, both in parsing the Urho source and (given that) of course not in generating the bindings. And also global functions and variables -- I think none of those are exposed at this point.

After that, it will probably cover about 90-99% of the Urho3D API.

If you mean how the source is parsed and the binding code generated, the three python files parseobjects.py, cppobjects.py, and bindpython.py  in the repository are all of it (excepting libclang, of course).

---
@bvanevery, you may have already seen this, but pybind11 supports at least some versions of PyPy - CFFI is not the only way to interface with it. Though I think other languages may support CFFI(-type?) bindings, so that route could be interesting to explore in any case.

-------------------------

SirNate0 | 2020-02-26 02:47:26 UTC | #17

Update on progress:
 * Global (Urho3D::*) functions are now supported. 
 * Operators are mostly supported, with a few more operators remaining, like enabling some implicit conversions for Variant and such. 
 * Enums are now supported.

Yet to be done:
 * Template type stuff, especially fixing up some more return types and call types for (POD)Vector and perhaps a few more.
 * Proper handling of Deserializable and Serializable: presently they cannot be exposed as being base classes since they cannot have a SharedPtr as the holder type, and pybind11 doesn't seem to support mixing holder types of base classes (I'm looking into that, and have asked them on gitter).
 * Keeping the Context alive until after everything else
 * Function pointer parameters to functions
 * Splitting the binding code into multiple files (see notes below)

Some fun notes:
 * The generated binding file is now over 14,000 lines, over 10,000 of which are code.
 * This is generated with less than 1,400 lines of code in python
 * Compiling this one file takes about 4 minutes and over 11 GB of RAM (with gcc version 5.4.0)
  * Comparing to the results of cloc *.h *.cpp from the AngelsScript directory in Urho3D, we actually have fewer lines of code to generate the python bindings (though compilation probably takes quite a bit longer)
 * Generated .so is about 113 MB, though this is without explicitly calling for any optimization or following the suggestion of pybind11 and forcing hidden visibility by default.

-------------------------

rku | 2020-03-01 10:16:36 UTC | #18

[quote="SirNate0, post:17, topic:5932"]
over 11 GB of RAM
[/quote]

Ouch. It might be a good idea to split that file.

-------------------------

SirNate0 | 2020-03-01 15:39:19 UTC | #19

That's actually exactly what I'm doing right now. The generating script now produces a configurable number of files each with their own couple of binding functions so the class and enums (the enums take a surprising amount of RAM to compile - I'm guessing it has something to do with the compiler trying to optimize them). As a bonus, this allows for a multithreaded build provided the RAM is not an issue.

-------------------------

