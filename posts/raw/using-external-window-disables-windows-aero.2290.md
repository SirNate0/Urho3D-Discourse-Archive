Enhex | 2017-01-02 01:14:32 UTC | #1

After some recent(several months old) Nvidia driver updates, using external window causes Windows Aero to be turned off until the application is closed.
The Aero turn off happens after the line:
[code]impl_->context_ = SDL_GL_CreateContext(window_);[/code]
In:
OGLGraphics.cpp Graphics::Restore()

I encountered it in my level editor, using wxWidgets for the external window.

Anyone knows how to deal with this problem?

-------------------------

Enhex | 2017-01-02 01:14:44 UTC | #2

I've contacted Nvidia and got some hints:
"We have received reports of this issue and the problem appears to be due to a recent change in the 370.xx drivers to expose 16bit float format by default in OpenGL as visible format. This change is likely causing some app to behavior incorrectly by requesting a pixel format that is not compatible with DWM. In fact the blender app version 2.77 also had the same problem and they updated to version 2.78 which is now working with 370.xx drivers. Development suggest updating the pixel format selection to resolved the problem on the app side."

Referred Blender problem is: [developer.blender.org/T49215](https://developer.blender.org/T49215)

I tried to look into Urho's source and it seems to use RGB888 PACKED32 with SDL.
Could the problem be with the external window?

-------------------------

cadaver | 2017-01-02 01:14:45 UTC | #3

Self-created windows and external windows should handle the pixel format setup similarly, in the SDL function WIN_GL_SetupWindow(). Though I haven't looked into that function in detail, it probably does some format selection magic.

-------------------------

