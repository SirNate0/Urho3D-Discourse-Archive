Unick | 2017-01-02 01:15:40 UTC | #1

Hello.

During render i can change camera settings: fov, rotation. But i have group of elements, which should be rendered with fixed camera parameters. As the result, i need to have different camera settings for different objects during render.

What is the best way to do this?

I want to render all in one view, For now i see only one way to change camera settings in material.

-------------------------

jmiller | 2017-01-02 19:27:39 UTC | #2

Something like this?

http://discourse.urho3d.io/t/solved-mix-orthographic-and-perspective-cameras/1747

-------------------------

Unick | 2018-05-21 16:28:16 UTC | #3

I was able to make using several viewports. For each viewport i setup camera and copy result of first viewport to second viewport.

-------------------------

