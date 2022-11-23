Elendil | 2018-11-29 23:53:05 UTC | #1

I want integrate Noesis GUI which contains some RenderDevices for quick use. That means I can use OpenGL RenderDevice, which draw everything neccesary to display GUI. For example in GLFW I simply do View->Render() and thats all (there are more function to call before that, but only for ilustration).

I check ImGui, Nuclear, TurboBadger integrations, but all of those create textures and use some renderer from library which is not connected to GL or DX. Noesis is different, because it have prepared renderer for OpenGL or DX. When I simply do that in UIElement or Object Urho3D crash when try display GUI. Then question is, where to put this render function in Urho3D?

For example I successful integrate Noesis in to Panda3D without write lot of code for renderer. Beacuse I use this technique:
create custom DisplayRegion (Panda3D object) where is draw function which use View->Render() from Noesis. I am trying similar steps for Urho3D but without success.

-------------------------

