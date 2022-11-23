Dave82 | 2017-01-02 01:06:25 UTC | #1

Hi , i'm trying to disable the depth write with no luck. What i want is the object is always rendered on the top of everything int the scene... but whenever i try to set depthwrite to false , all i get is a random flickering and the object is just randomly disappears and reappears and it still uses depthwrite.

Tried to disable it in all the passes (in Diff.xml technique) but none of them worked.

Also is it possible to disable the depth write so the object is rendered on top of UI elements too ? i'm tring to rotate and display items in a 2d inventory , i know i can use render targets but this would be the most convenient way (if possible ofcourse...)

-------------------------

cadaver | 2017-01-02 01:06:25 UTC | #2

Depth write off alone won't guarantee rendering on top of everything. Try setting depth test to "always" in the pass(es) instead.

If you want to render objects on top of UI, you can use the "renderui" renderpath command, and put scene pass commands afterward. This disables the hardcoded rendering of UI after viewports.

-------------------------

Dave82 | 2017-01-02 01:06:25 UTC | #3

hi ! This is the current technique i use:

[code]<technique vs="Unlit" ps="Unlit" psdefines="DIFFMAP" >
    <pass name="base" depthtest="always"/>
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" />
    <pass name="deferred" psdefines="DEFERRED" />
</technique>[/code]

it is just a modified version of DiffUnlit

The problem with this is sometimes it works sometimes it doesn't.(from certain cam angle and distance it works but when i go closer or rotate the camera it just discards the depthtest)
The other problem is that the object depthtests itself too , so the furthest polys are drawed on top of the closest. So it looks like the object is turned inside out

-------------------------

cadaver | 2017-01-02 01:06:25 UTC | #4

Instead of modifying the depth test, you could also define a custom pass for the object, and before rendering that pass, destroy the depth buffer information in the renderpath (execute clear command with depth parameter 1.0, like in the beginning of the path). This will allow the object to depth-test against itself properly.

EDIT: a slight modification of this is the standard "two scenes rendered on top of each other" -technique, which has been discussed on this forum several times before. To use, you would use another viewport on top of the first, and another camera (possibly also another scene, but you can also render objects selectively by tweaking the view masks of the object and camera.) The second viewport would utilize a renderpath which doesn't clear color, but only depth. This would have the advantage that you don't have to mess with techniques / passes.

-------------------------

Dave82 | 2017-01-02 01:06:25 UTC | #5

Wow works perfectly ! Thanks ! I used a custom technique and passed the "renderui" command before the custom pass and it works perfectly !

-------------------------

