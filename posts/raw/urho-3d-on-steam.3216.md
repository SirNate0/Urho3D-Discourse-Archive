glebedev | 2017-06-06 12:22:46 UTC | #1

Hey,

Someone already suggested it AFAIK. What if we put urho editor as an application to Steam Direct and let people add samples as workshop items?

-------------------------

Eugene | 2017-06-06 13:05:19 UTC | #2

Urho Editor isn't something that can be deployed and used by end user, IMO.

-------------------------

cadaver | 2017-06-06 13:12:45 UTC | #3

Furthermore, in a serious project you are likely to customize the application by adding your own C++ classes and such. If put on Steam, it would be the "vanilla" version. And not only that, there isn't even a canonical build config. It's really a coder / code-oriented engine and thus I fully agree with @Eugene.

-------------------------

glebedev | 2017-06-06 13:25:54 UTC | #4

So the vanilla version of engine and editor isn't user friendly but a game + editor would make more sense?

-------------------------

hdunderscore | 2017-06-07 20:20:50 UTC | #5

I think there is some potential in it, if either the Lua side of things were made more friendly (ie, errors are reported instead of crashing the engine) or you promote the Angelscript side, then users could create script libraries instead of C++ extensions.

The awkward part is that there is no integrated script editor, but you could bundle something like atom. Atomic engine would probably work better out-of-the-box on steam.

-------------------------

