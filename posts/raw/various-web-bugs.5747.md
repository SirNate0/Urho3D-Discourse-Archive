JTippetts | 2019-12-04 01:40:16 UTC | #1

I'm working on a web project, a small[incremental game](https://jtippetts.github.io/GoldRush.html) inspired by a game called Reactor Idle, and in the development of it I've encountered a few bugs in the process: [#2479](https://github.com/urho3d/Urho3D/issues/2479) which has to do with buttons and check-boxes receiving doubled events on clicks, resulting in the check box being selected then immediately de-selected, and [#2552](https://github.com/urho3d/Urho3D/issues/2552) which sometimes causes the UI to go into an unresponsive state, with mouse clicks not being received, if you click in areas outside of the game window. You can switch browser tabs to restore it, but that's not really a solution to the problem.

I've invested a couple weeks into this project, and I'd hate to have to abandon it, but the thing is I don't understand the whole web-build process anywhere near well enough to begin debugging these issues. Are there any resources I can use to learn more about this, and about how I could start trying to debug it? It's gotten to the point where I'm considering just giving up altogether and moving on.

-------------------------

weitjong | 2019-12-04 14:46:18 UTC | #2

It has been awhile since I last tested it but just like other platforms you can use a Debug build config for the Web build. This in turns instructs Emscripten to produce a sourcemap among others.

https://github.com/urho3d/Urho3D/blob/2bcb0f1b2fd2a74bd36a80d876513f476f790935/CMake/Modules/UrhoCommon.cmake#L696-L698

The build artifacts will grow significantly larger because of that. After loading the page in the browser, you can then open the developer tool to inspect the "Sources". Yes, I am talking about C/C++ sources here where you can set breakpoint and step into. Not sure where you can get the online resources, I am learning how to debug in a browser the hard way at my day work.

Hope this helps.

-------------------------

