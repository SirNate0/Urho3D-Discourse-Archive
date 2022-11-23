spwork | 2017-12-20 15:32:22 UTC | #1

when i use `Graphise::SetMode(x,y)` change resolution in fullscreen mode ,and my window flashse and Minimized，i must click on the state bar to restore the window,how to solve this situation?

I am use Win7 ,visual studio ,the lib build with DIRECT3D11。

-------------------------

SirNate0 | 2017-12-20 17:41:25 UTC | #2

If you call `Graphics::Raise()` after `Graphics::SetMode(x,y)` does it solve the problem?

-------------------------

spwork | 2017-12-20 20:27:27 UTC | #3

it didn't work, the window still minimized.

-------------------------

spwork | 2017-12-20 22:24:04 UTC | #4

using OPENGL is ok,but using d3d9 or d3d11 the window will minimized.

-------------------------

mrchrissross | 2018-10-25 15:39:12 UTC | #5

having same problem here, was this problem solved?

-------------------------

Modanung | 2018-10-25 15:49:11 UTC | #6

[This](https://www.sevenforums.com/gaming/204444-full-screen-games-minimizing-without-any-reason.html) might be related.

As might this:
https://superuser.com/questions/1144959/how-do-i-stop-fullscreen-games-from-minimizing-when-i-click-on-another-window-on#1251294

-------------------------

mrchrissross | 2018-10-25 19:03:49 UTC | #7

The `GetSubsystem<Graphics>()->SetMode(screenRes.x_, screenRes.y_);`  seems to work when i used it directly before `GetSubsystem<Graphics>()->ToggleFullscreen();` however to to toggle full screen off i use `GetSubsystem<Graphics>()->SetMode(screenRes.x_ / 2, screenRes.y_ / 2);` but this seems to minimize the screen.

here is the code in total:
```
if (input->GetKeyPress(KEY_P))
{ 
    if (GetSubsystem<Graphics>()->GetFullscreen() == true)
        GetSubsystem<Graphics>()->SetMode(screenRes.x_ / 2, screenRes.y_ / 2);
    else
        GetSubsystem<Graphics>()->SetMode(screenRes.x_, screenRes.y_);

    GetSubsystem<Graphics>()->ToggleFullscreen();
}
```

-------------------------

Modanung | 2018-10-25 15:59:30 UTC | #8

The behavior seems to be related to the `SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS` environment variable.

-------------------------

