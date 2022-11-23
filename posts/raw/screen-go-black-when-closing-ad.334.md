att | 2017-01-02 00:59:41 UTC | #1

On my android game, when I closed the full screen ad, the screen goes black, here is the error log

[code]I/Ads     ( 6525): Ad closing.
E/libEGL  ( 6525): eglSwapBuffers:1051 error 300d (EGL_BAD_SURFACE)
V/SDL     ( 6525): onResume()
E/libEGL  ( 6525): eglSwapBuffers:1051 error 300d (EGL_BAD_SURFACE)
V/SDL     ( 6525): surfaceCreated()
V/SDL     ( 6525): surfaceChanged()
V/SDL     ( 6525): pixel format RGB_565
V/SDL     ( 6525): Window size:768x1184
V/PhoneStatusBar( 3416): setLightsOn(true)
W/Adreno-EGL( 6525): <qeglDrvAPI_eglSwapBuffers:3526>: EGL_BAD_SURFACE
V/SDL     ( 6525): onWindowFocusChanged(): true
V/SDL     ( 6525): nativeResume()
W/art     ( 6525): Thread[29,tid=6709,Native,Thread*=0x536170d8,peer=0x64ff3098,"Thread-12615"] attached without supplying a name
W/Adreno-EGL( 6525): <qeglDrvAPI_eglSwapBuffers:3526>: EGL_BAD_SURFACE
W/Adreno-EGL( 6525): <qeglDrvAPI_eglSwapBuffers:3526>: EGL_BAD_SURFACE
W/Adreno-EGL( 6525): <qeglDrvAPI_eglSwapBuffers:3526>: EGL_BAD_SURFACE
W/Adreno-EGL( 6525): <qeglDrvAPI_eglSwapBuffers:3526>: EGL_BAD_SURFACE
W/Adreno-EGL( 6525): <qeglDrvAPI_eglSwapBuffers:3526>: EGL_BAD_SURFACE
W/Adreno-EGL( 6525): <qeglDrvAPI_eglSwapBuffers:3526>: EGL_BAD_SURFACE
W/Adreno-EGL( 6525): <qeglDrvAPI_eglSwapBuffers:3526>: EGL_BAD_SURFACE[/code]

-------------------------

cadaver | 2017-01-02 00:59:42 UTC | #2

It looks like the screen surface creation fails after focus returns to the Urho program.

Does this also happen if you go away from your program with the home button, run some other apps, and then return to your program? If yes, then it's a general bug in Urho/SDL resume & lost surface handling.

If no, then it's a bug that's specific to showing the ad. In that case you should be prepared to examine the SDL code to resolve it yourself (and hopefully submit a patch/pull request if you find the cause), as the Urho project itself doesn't have test cases for external interactions like this. Also I recommend looking at the SDL forums to see if someone has encountered similar issues.

-------------------------

