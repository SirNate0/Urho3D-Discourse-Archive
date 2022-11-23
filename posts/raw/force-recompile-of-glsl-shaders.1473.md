sabotage3d | 2017-01-02 01:08:01 UTC | #1

Hi guys is there a way to force recompile GLSL shaders while in the Editor it seems I need to restart it whenever I make a change.

-------------------------

codingmonkey | 2017-01-02 01:08:01 UTC | #2

Hi, actually on win8 recompiling works fine for me. 
I mean If I open Editor and start change code of shader in Notepad2 and then press CTRL+S it's immediately recompiled and show new shading of material in Editor's view (or error log:) ).

-------------------------

sabotage3d | 2017-01-02 01:08:01 UTC | #3

You mean the actual glsl shader? For me on OSX it doesn't work.

-------------------------

codingmonkey | 2017-01-02 01:08:01 UTC | #4

>You mean the actual glsl shader?
Yes, any shader that uses by scene's objects in their materials.

-------------------------

friesencr | 2017-01-02 01:08:01 UTC | #5

I have had issues with shader recompilation if I break the shader with bad code.  I think the problem is worse if the initial load is broken.  I remember it giving up if the first load was bad.  I also can't remember if this was fixed or not.

The resource cache auto reload has to be enabled for this feature to work.  It uses file system changes as notifiers to reload.  This is enabled on the editor but is normally disabled by default.

-------------------------

sabotage3d | 2017-01-02 01:08:02 UTC | #6

It just started working after I made a change to the technique.

-------------------------

