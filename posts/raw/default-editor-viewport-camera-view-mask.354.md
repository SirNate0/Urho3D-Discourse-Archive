ucupumar | 2017-01-02 00:59:50 UTC | #1

Hello all.

Why editor viewport camera view mask is not using -1 value?
I've use a lot of view mask setting and because of that, some objects isn't displayed on viewport.

-------------------------

friesencr | 2017-01-02 00:59:50 UTC | #2

As far as I can tell it is only used to filter out raycasts for objects that are reserved for the editor, which at this point are the grid and the gizmo.  If you reserve the last bit for urho you should be good. so use less then 0x80000000.

-------------------------

ucupumar | 2017-01-02 00:59:50 UTC | #3

It looks like not every bit less than 0x80000000 can be used on editor viewport. Actually objects can only showed up if bit 1 (0x00000002) of view mask is valued 1. It can be 2 or 3, but not 4 or 1, etc. 
So, the viewport only display objects on bit 1 view mask, everything else will not displayed. It's strange.

After messing around with editor script, I found the code that responsible for this, on EditorView.as line 108:
[code]camera.viewMask = 0x80000000 + (uint(1) << index); // It's easier to only have 1 gizmo active this viewport is shared with the gizmo   [/code]Index variable means active viewport. I didn't know before that Urho Editor can use more than one viewport. So it means that on viewport 0, camera viewmask will use value of 0x80000002, and on viewport 1, it will use value of 0x80000004, etc. It explains the strange behaviour I wrote before. After I test using more than viewport, viewport 0 can only display bit 1, viewport 1 can only display bit 2, etc.

If I commented line 108 and use this code:
[code]//camera.viewMask = 0x80000000 + (uint(1) << index); // It's easier to only have 1 gizmo active this viewport is shared with the gizmo
 camera.viewMask = -1;[/code]Editor will display anything view mask I input (expect '0' of course). As far as I tested, the gizmo and grid still works as usual too.

Why camera editor isn't just use value of -1? I means why use different mask on different viewport camera?

-------------------------

friesencr | 2017-01-02 00:59:50 UTC | #4

The reason they use a different mask was to hide the gizmo.  Now that the pre render viewport callbacks exist that could be fixed to do without.  I did write that code and I am a bit of a peanut brain.  I will do the refactor.  It will still have to be >0x80000000 but i can atleast get rid of the viewport specific stuff.

-------------------------

friesencr | 2017-01-02 00:59:50 UTC | #5

Now every camera is using the same mask.  The update is on master.

-------------------------

ucupumar | 2017-01-02 00:59:50 UTC | #6

Yeah thanks friesencr! You're the best!  :mrgreen:

-------------------------

ucupumar | 2017-01-02 00:59:50 UTC | #7

Wait a minute, now I can't even change object view mask to anything expect -1 (0xFFFFFFFF)
After checked the diff, I see:
[code]camera.viewMask = 0x80000000; // It's easier to only have 1 gizmo active this viewport is shared with the gizmo[/code]Now every camera use 0x80000000, it means active the only active bit is bit 31. 
Why don't you just use -1 to camera view mask? What kind of gizmo hiding you're talking about?

-------------------------

friesencr | 2017-01-02 00:59:50 UTC | #8

The gizmo is sized relative to distance you are away from it.  That way when you are really far away you can still see it.  However it is only sized based on the active viewport.  If you are zoomed out on the active viewport and have another view seeing the gizmo can take up the whole screen, which is kind of funny to watch but not very useful.  The sizing code could probably be put in the begin viewport render callback.  The gizmo only being in the active view is there slightly because of usability too.  I don't have strong feelings about that.  I personally found it to be a slightly nice indicator.  I did changed the camera viewmask to -1, its on master.  

 This is definitely better thank you for the feedback.

-------------------------

ucupumar | 2017-01-02 00:59:50 UTC | #9

Thanks for the fast response friesencr.
I think I understand about the gizmo now, I've seen that funny behavior just now. Now it's gone! And the view mask works too! Yay!
Now you're really the best!  :mrgreen:

-------------------------

