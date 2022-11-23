sabotage3d | 2017-01-02 01:14:26 UTC | #1

Hi I am trying to overlay a simple OpenGL GUI to Urho3D. I have a few questions as I have never done it before. 
Should I create a quad and render the GUI framebuffer and overlay it into my scene?
Do I need to create the quad at all or just to follow a simpler approach like in the RenderToTexture example?
Can I directly draw OpenGL on top of existing Urho3D window without doing render to texture approach?
Which approach would be recommeded and is there any guidlines I have to follow?

-------------------------

cadaver | 2017-01-02 01:14:27 UTC | #2

You can intercept the part of frame where scene rendering is done and follow up with your own draw commands. For example the E_ENDRENDERING event comes just before presenting. Alternate event to watch for is E_ENDVIEWRENDER which is sent for each viewport. There's no especial benefit to rendering into a texture compared to rendering to the backbuffer, unless you especially want to sample it to accomplish some effect.

Note that if you can, using the Graphics class is recommended over raw OpenGL, because Graphics does its own state tracking to prevent redundant changes, and if the state isn't what it expects the next time Graphics is being used to draw, it won't draw correctly.

-------------------------

sabotage3d | 2017-01-02 01:14:27 UTC | #3

Thanks cadaver. At the moment when I draw with OpenGL it just draws on top of everything and it looks like it is either blocking or hiding what Urho3D is drawing.

-------------------------

rku | 2017-01-02 01:14:27 UTC | #4

You can check out NuklearUI integration - it does exactly what you are trying to do: [github.com/rokups/Urho3D-nuklea ... I.cpp#L101](https://github.com/rokups/Urho3D-nuklear-ui/blob/master/NuklearUI.cpp#L101)

-------------------------

sabotage3d | 2017-01-02 01:14:27 UTC | #5

Thanks I already tried it but I wanted to try using more of Urho3D Graphics API. 
What GraphicsApiStateBackup and GraphicsApiStateRestore do exactly?

-------------------------

sabotage3d | 2017-01-02 01:14:31 UTC | #6

So I am using E_ENDRENDERING and I can see my GUI on top. If I create a zone with Urho3D and set a color to red I can see it under the menu. The problem is if I try to create some models or anything else in Urho3d it appears for 1 frame and then it disappears. What is the best workaround for this?

-------------------------

