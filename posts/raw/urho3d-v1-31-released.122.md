cadaver | 2017-01-02 00:58:12 UTC | #1

Now Urho3D V1.31 is finally tagged and released, and this is perhaps the biggest amount of commits and new features added in between releases! Thanks and congratulations (again) to everyone who was involved, whether in form of direct code contributions, or bug reports / discussion.

As Google Code no longer hosts new downloads, we have moved to SourceForge for file releases.

Release post at the homepage /w changelog: [url]http://urho3d.github.io/releases/2014/03/06/urho3d-131-release[/url]
GitHub source package: [url]https://github.com/urho3d/Urho3D/archive/1.31.zip[/url]
SourceForge downloads folder: [url]http://sourceforge.net/projects/urho3d/files/Urho3D/1.31/[/url]

-------------------------

aster2013 | 2017-01-02 00:58:12 UTC | #2

Congratulations!  :smiley:

-------------------------

alexrass | 2017-01-02 00:58:12 UTC | #3

Great job!!! Urho best open source engine!!!

-------------------------

weitjong | 2017-01-02 00:58:12 UTC | #4

Ditthree. Congrats again!

Just want to add that the manually-packaged Windows MSVC binary and documentation are built against D3D9. While the Windows snapshot binary and documentation are built against OpenGL with MinGW cross-compiler.

-------------------------

alexrass | 2017-01-02 00:58:12 UTC | #5

May be drop D3D support? OpenGL way?

-------------------------

weitjong | 2017-01-02 00:58:12 UTC | #6

I am waiting for that day to come  :wink: . But seriously, Urho3D user community is already quite small as it is, so I think we should embrace more users rather than trying to alienate a huge chunk of them. And I suppose we should not discuss it in this topic thread.

-------------------------

alexrass | 2017-01-02 00:58:12 UTC | #7

Ok

-------------------------

weitjong | 2017-01-02 00:58:12 UTC | #8

For those who do not tracking the development HEAD and plan to migrate your existing project using v1.3 to v1.31, here are some migration notes that I originally keep for myself. They may not be comprehensive.

[ol]
[li]In RenderPaths, rename 'prealpha' pass to 'postopaque'.[/li]
[li]Billboard texture up side down flip.[/li]
[li]Rename Urho3D-CMake-magic.cmake to Urho3D-CMake-common.cmake.[/li]
[li]All FindXXX modules, rename include and library variables to plural forms.[/li][/ol]
Hope you find it useful.

-------------------------

rasteron | 2017-01-02 00:58:12 UTC | #9

Congratulations on the new release guys!! and good to be back here with the new forum

Keep it up  :smiley:

-------------------------

cadaver | 2017-01-02 00:58:13 UTC | #10

I'll answer the D3D / OpenGL thing in this thread nevertheless: from a maintainability viewpoint of a small team, dropping D3D in favor of a single renderer would be tempting, and in fact Urho3D started as OpenGL-only (so long time ago that no public repo of that phase exists)  However, in typical Urho3D use, OpenGL on Windows achieves only 75% - 85% of the performance of D3D, and OpenGL driver quality of older GPUs may still be questionable, so from a technical viewpoint it wouldn't be a good move. Also the ability to load previously compiled binary shaders results in faster startup time on D3D.

-------------------------

carlomaker | 2017-01-02 00:58:13 UTC | #11

[b]Congrats to cadaver and all contributors!!!![/b]!!

-------------------------

Hevedy | 2017-01-02 00:58:13 UTC | #12

[quote="cadaver"]I'll answer the D3D / OpenGL thing in this thread nevertheless: from a maintainability viewpoint of a small team, dropping D3D in favor of a single renderer would be tempting, and in fact Urho3D started as OpenGL-only (so long time ago that no public repo of that phase exists)  However, in typical Urho3D use, OpenGL on Windows achieves only 75% - 85% of the performance of D3D, and OpenGL driver quality of older GPUs may still be questionable, so from a technical viewpoint it wouldn't be a good move. Also the ability to load previously compiled binary shaders results in faster startup time on D3D.[/quote]

Nice work to all.
Yes the OpenGl in windows run from 0% to 30% (depending on the case) slower than D3D...
Cadaver this need  GI [crytek.com/cryengine/cryengi ... lumination](http://www.crytek.com/cryengine/cryengine3/presentations/cascaded-light-propagation-volumes-for-real-time-indirect-illumination) seriously and the HDR Skybox.

-------------------------

jmiller | 2017-01-02 00:58:14 UTC | #13

Congratulations!
Thank you all for your hard work on this great project. :slight_smile: To a great future!

This AngelScript revision broke pre-Vista compatibility (threads), but it was quickly fixed and here are the current revisions if needed:
[svn.code.sf.net/p/angelscript/co ... thread.cpp](http://svn.code.sf.net/p/angelscript/code/trunk/sdk/angelscript/source/as_thread.cpp)
[svn.code.sf.net/p/angelscript/co ... s_thread.h](http://svn.code.sf.net/p/angelscript/code/trunk/sdk/angelscript/source/as_thread.h)

-------------------------

cadaver | 2017-01-02 00:58:14 UTC | #14

Thanks, that will be included.

-------------------------

