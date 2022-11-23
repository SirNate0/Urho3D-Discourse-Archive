slapin | 2017-04-07 19:11:27 UTC | #1

Hi, all!

How can I create c++ component so that it is seen by both Lua and AngelScript?
I want to access some attributes and run some methods.

-------------------------

Eugene | 2017-04-07 19:48:59 UTC | #2

You have to make script bindings. It's pretty easy for AS and pretty hard for Lua if you don't work in fork.

-------------------------

slapin | 2017-04-07 20:26:03 UTC | #3

I do not work in fork, but I want these to be eventually integrated, so that should be no problem.
I currently work in separate project using Urho as library. I need to start with AngelScript.
How can I do this?

-------------------------

Eugene | 2017-04-08 06:16:59 UTC | #4

Check files `Urho3D/AngelScript/*API.cpp` for examples

-------------------------

KonstantTom | 2017-04-08 11:08:35 UTC | #5

It's very easy to bind components from your downstream project to AngelScript, but it may not work when you link to Urho3D dynamically. Example from my project where I bind my `Map` component:
https://github.com/KonstantinTomashevich/colonization/blob/master/sources/Colonization/AngelScriptBinders/Core/BindMap.hpp
https://github.com/KonstantinTomashevich/colonization/blob/master/sources/Colonization/AngelScriptBinders/Core/BindMap.cpp#L30
You should run `Bind{ComponentName} (script)` functions on application startup.
https://github.com/KonstantinTomashevich/colonization/blob/master/sources/Colonization/Utils/Activities/ActivitiesApplication.cpp#L48
https://github.com/KonstantinTomashevich/colonization/blob/master/sources/Colonization/Utils/Hubs/BindAll.cpp#L27

-------------------------

slapin | 2017-04-08 20:54:04 UTC | #6

Thanks a lot for the example!

-------------------------

