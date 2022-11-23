OMID-313 | 2017-03-18 05:46:36 UTC | #1

Hi all,

I'm using Urho3D on Raspberry PI. And here is how I use it:

1. First I import some desired models with command line `AssetImporter`.
2. Then I write a script code mycode.as like the examples (https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scripts/04_StaticScene.as)
3. Finally, I run the code with the following command:
`./Urho3DPlayer /Scripts/mycode.as`

But recently I faced some hangs and freezes on Raspberry Pi while running some games, which popped up some fundamental questions for me:

Is this approach the correct way of running the game?
Shall I build or compile or render something before running the code?
Is it optimized to run the mycode.as file!? Or shall I generate another file?
What should I do in order to reduce the load of online real-time rendering of the game? Does building/compiling/rendering the game (before running it) makes it easier and lighter to be run afterwards?
When making animations with 3dsmax, we use high-end computers to design the animation and render it. After that, any low-end and simple computer can play the animation. Now can we use a similar approach? Can I build/compile/render the game in a high-end machine and run the game in a low-end machine?

Sorry for asking so many questions. 
Thanks for your time and support.

-------------------------

hdunderscore | 2017-03-18 06:22:37 UTC | #2

It depends on what you are doing in the script. Is it possible to share some examples?

Are you creating/destroying a lot of objects? You can get an easy performance boost by reusing objects instead of creating/destroying them.

You can look at the profiler results to narrow down the issue, debugHud->ToggleAll().

You can write Urho programs in C++, which can give a performance boost, although it's probably not as big of a boost as you might imagine because angelscript performs pretty well already. But for running on Raspberry Pi, maybe it will give a more noticeable improvement.

If you like working with Angelscript, you can move the slow parts to C++ and call it from Angelscript.

-------------------------

OMID-313 | 2017-03-18 06:36:59 UTC | #3

Thanks @hdunderscore for your answer.

I use fairly simple codes. Creating a scene and an object, and rotating them. That's it.

But I didn't get my answers!
Shall I build my code before running it?
Do we render the game in the build process? Or all the rendering is real-time while playing the game !?

-------------------------

weitjong | 2017-03-18 13:47:10 UTC | #4



-------------------------

