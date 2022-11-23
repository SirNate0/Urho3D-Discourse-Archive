Pencheff | 2018-02-22 10:50:35 UTC | #1

After descent amount of work on this the last month I would like to share some results. 

TurboBadger options menu:
![tb_options|690x387](upload://2NX0jH5aF2boxf1htxhKDHBt5Gi.png)

CEF3 ui webview and browser:

It handles 60fps CEF3 rendering:
![tb_cef3_60fps_webview|690x387](upload://aJe3gw2yHZlbLihIfnxi2Qn9sCQ.jpg)

CEF3 main loop runs in a separate thread, CefRenderHandler does not interfere with the main application loop, texture updates are done with dirty rectangle updates to reduce texture upload times:
![tb_cef3_profiler|690x387](upload://fgO8FDvhSuMafSuDhIK6DSnd1XK.jpg)

It doesn't slow down the rendering loop:
![tb_cef3_nofpslimit|690x387](upload://w03xO31NymSxQY8XMfxiuiJT9eb.jpg)

CEF3 integration is a bit tricky to get right, this is my third integration in an engine so far, AtomicGameEngine was also a good reference, especially for the keyboard handling part. WebBrowser components 
are available both in the UI and in the scene.

I'd like to thank @Lumak for his TurboBadger integration, it was a good starting point, here is my work on top of it: https://gist.github.com/PredatorMF/18c8f50d72296f427eb6b2bdfa729dad . I've added clipboard support and made it work alongside the internal Urho3D UI (consuming input events) and also draw only when TB content is changed.

-------------------------

johnnycable | 2018-03-14 17:17:47 UTC | #2

I'm trying to set this up but I get errors on GLFW/glfw3.h missing. Is that needed?
Can you share the link to @Lumak setup, just to see if I'm on the right track?

-------------------------

Pencheff | 2018-03-14 17:33:18 UTC | #3

https://github.com/Lumak/Urho3D-1.4-TurboBadger

-------------------------

Pencheff | 2018-03-14 17:38:39 UTC | #4

I've only finished my Windows version and didn't check the Linux version, maybe some include is missing. Also noticed that my Android build has issues with multiple definitions of TurboBadger's functions...I'll update the gist when I check it out.

-------------------------

johnnycable | 2018-03-20 11:01:53 UTC | #5

Ok, looks I've managed to go forward.
I've integrated the UI into Urho build system on my branch. Now it's a build option like others.
Now when I'm compiling the downstream app I get this:

in tb_ui_renderer.cpp, line 832

> // static
> TBFile* TBFile::Open(const char *filename, tb::TBFile::TBFileMode) {
>   Urho3D::UTBFile* file = new Urho3D::UTBFile(Urho3D::FrameworkApp::Get()->GetContext());
> 
>   if (!file->OpenFile(filename)) {
>     delete file;
>     file = NULL;
>   }
> 
>   return file;
> }

_No member named 'FrameworkApp' in namespace 'Urho3D'_

I guess it's looking for CEF or some app of yours here. How did you integrate this?
I'm actually stuck without this piece.

More on integration. in line 862:

> TBImageLoader *TBImageLoader::CreateFromFile(const char *filename) {
>   TBTempBuffer buf;
>   if (buf.AppendFile(filename)) {
>     int w, h, comp;

doesn't find CreateFromFile. In TBTempBuffer class there's a AppendPath function that suits, and it's like:

> bool TBTempBuffer::AppendPath(const char *full_path_and_filename)
> {
> 	const char *str_start = full_path_and_filename;
> 	while (const char *next = strpbrk(full_path_and_filename, "\\/"))
> 		full_path_and_filename = next + 1;

is this multiplatform? Did you removed because it doesn't work on win?
Bye

-------------------------

Pencheff | 2018-03-20 14:58:57 UTC | #6

FrameworkApp::Get() is singleton access for my application class which inherits Urho3D::Object and acts like top level object. My bad I left it out in the gist. Just store the instance of the Urho3D::Context somewhere in a global variable and use it when you need to obtain the ResourceCache subsystem.

-------------------------

TheGreatMonkey | 2018-05-23 08:22:48 UTC | #7

I've just started trying to integrate CEF3 into an Urho based project. There's almost no documentation on how to integrate it into an application. Any chance you could share you're integration method?

-------------------------

Pencheff | 2018-05-23 09:04:13 UTC | #8

I cannot directly share my code since its proprietary but I can give you ideas and guides on how-to. You can start here: https://bitbucket.org/chromiumembedded/cef/wiki/GeneralUsage .

To give you the basic idea:
1. Create CefApp
2. Run CefInitialize()
3. Integrate CefRunMessageLoop() or CefDoMessageLoopWork() in your game/app loop.
4. Create a browser - CefBrowserHost::CreateBrowserSync()

If you want to render on a texture, use the Off-Screen Rendering method described in the link above. 
On every Paint() call of a browser frame you'll get the pixel data as BGRA32, you can copy that to a texture and render anywhere on the screen. You can also inject input from Urho3D directly. You could look at AtomicGameEngine sources, they have good CEF3 integration.

-------------------------

Pencheff | 2018-10-22 13:22:49 UTC | #9

Just updated my gist with the TurboBadger integration, for anyone interested:
https://gist.github.com/PredatorMF/18c8f50d72296f427eb6b2bdfa729dad

-------------------------

