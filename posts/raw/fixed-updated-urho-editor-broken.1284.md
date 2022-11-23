christianclavet | 2017-01-02 01:06:36 UTC | #1

Hi, I updated today (20 aug 2015). And for some unknown reason I can't get the EDITOR to run. All the examples work fine, but the editor and the ninja game example fail to launch and display some errors.

I'm Using the CMAKE GUI to create the build. Here is my current setup:
[img]http://www.clavet.org/files/URHO/URHO_config.jpg[/img]
I have the URHO3D lib done and the tools and examples builds. 
Here is the error that is reported when I try to start the editor:
[img]http://www.clavet.org/files/URHO/ErrorScripts.jpg[/img]
Is there something done wrong? I've build and compiled URHO on Windows 7 HP using MSVC 2013.
If I try to start the URHO Player directly, it give a window asking to specify a script. (Normal behavior I think)

[b]EDIT:[/b] When I enable LUA, The URHO Lib can't be compiled. Only work when I uncheck LUA.
My project requirement are:
- Linux and Windows
- Using LUA and OPENGL
So I'm trying to set the build to use this.

Here is the report from MSCV (French)
[quote]23>C:\Users\Public\Projets\URHO\Build\Source\Urho3D\LuaScript\generated\ResourceLuaAPI.cpp(3756): error C2039: 'emptyArray'?: n'est pas membre de 'Urho3D::JSONValue'
23>          C:\Users\Public\Projets\URHO\Urho3D\Source\Urho3D\Resource/JSONValue.h(54)?: voir la d?claration de 'Urho3D::JSONValue'
23>C:\Users\Public\Projets\URHO\Build\Source\Urho3D\LuaScript\generated\ResourceLuaAPI.cpp(3756): error C2065: 'emptyArray'?: identificateur non d?clar?
23>C:\Users\Public\Projets\URHO\Build\Source\Urho3D\LuaScript\generated\ResourceLuaAPI.cpp(3765): error C2039: 'emptyObject'?: n'est pas membre de 'Urho3D::JSONValue'
23>          C:\Users\Public\Projets\URHO\Urho3D\Source\Urho3D\Resource/JSONValue.h(54)?: voir la d?claration de 'Urho3D::JSONValue'
23>C:\Users\Public\Projets\URHO\Build\Source\Urho3D\LuaScript\generated\ResourceLuaAPI.cpp(3765): error C2065: 'emptyObject'?: identificateur non d?clar?[/quote]

[quote]Erreur	145	error C2039: 'emptyArray'?: n'est pas membre de 'Urho3D::JSONValue'	C:\Users\Public\Projets\URHO\Build\Source\Urho3D\LuaScript\generated\ResourceLuaAPI.cpp	3756	1	Urho3D
Erreur	146	error C2065: 'emptyArray'?: identificateur non d?clar?	C:\Users\Public\Projets\URHO\Build\Source\Urho3D\LuaScript\generated\ResourceLuaAPI.cpp	3756	1	Urho3D
Erreur	147	error C2039: 'emptyObject'?: n'est pas membre de 'Urho3D::JSONValue'	C:\Users\Public\Projets\URHO\Build\Source\Urho3D\LuaScript\generated\ResourceLuaAPI.cpp	3765	1	Urho3D
Erreur	148	error C2065: 'emptyObject'?: identificateur non d?clar?	C:\Users\Public\Projets\URHO\Build\Source\Urho3D\LuaScript\generated\ResourceLuaAPI.cpp	3765	1	Urho3D[/quote]

-------------------------

weitjong | 2017-01-02 01:06:36 UTC | #2

This should teach you a lesson. Check the CI build status badges before doing git pull on master branch. We try to be careful not to break the build when committing changes to master branch, but we are just human and mistake does happen.

You can either wait until the mistake has been fixed in the master. Or discarding the offending commits that break the build in your local branch. For the latter, I believe this should do it: git reset --hard HEAD~2, discarding the last two commits. NOTE: I am assuming you don't have any committed and uncommitted changes in your local branch. Once reset, you can kiss them goodbye unless you have backed them up somewhere else.

-------------------------

christianclavet | 2017-01-02 01:06:38 UTC | #3

Hi.
I will have to check it more, but it seem to me that it was green (from what I remember). Thank to making me remember to double check there before syncing my fork.

Lasse as fixed it. Was able to build it with LUA and have the editor working back again.
[b]EDIT:[/b] Wow. I did not know that we could list the history and see the "bad" commits. Can the report write "passed" just because the last commit was good but still fail because of a commit before that?

-------------------------

