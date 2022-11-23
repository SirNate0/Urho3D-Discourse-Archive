zerokol | 2017-01-02 01:07:03 UTC | #1

Hello, I'm in a project that will mainly run under a Raspberry PI with Raspbean OS, almost every thing works well, but when i try:

[code]graphics->ToggleFullscreen();[/code]

it not works, the windowed mode not actives (I have tested on OSX, Ubuntu and Windows without problem)

another issue is that the mode:
[code]
engineParameters_["FullScreen"]   = false;
engineParameters_["WindowWidth"]  = 1024;
engineParameters_["WindowHeight"] = 768;
[/code]

not works too (only in raspbean), neither windowed mode or screen resolution
I searched in the forum and found this:

[topic319.html](http://discourse.urho3d.io/t/solved-correct-way-to-run-fullscreen-on-lower-resolution/328/1)

but I don't know if it is a os config issue or urho3d, some one may help me?

-------------------------

weitjong | 2017-01-02 01:07:04 UTC | #2

I don't think windows mode is supported for RPI. When the RPI port was being developed, we have made a decision not to depend on X11 stack. If I recall it correctly then there should be way to setup the BCM VideoCore driver to output to a smaller region than the entire screen viewport. However, since there is no X11, there will be nothing else to display on the screen even when you have successfully done so. In one of my earlier attempt when the X11 was still being used, I could render VC output on top of the X11. But it was so long ago already I do not remember exactly how to "regress" to get the X11 back.  :wink:

-------------------------

