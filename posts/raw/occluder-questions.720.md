rogerdv | 2017-01-02 01:02:23 UTC | #1

Can somebody explain me what impact does it have occluder options in meshes, in terms of render quality and perfomance?

-------------------------

codingmonkey | 2017-01-02 01:02:23 UTC | #2

it's increase perfomance on new PC, i guess. then your front big model hides(close view) to other models on background.
but i'm test occlusion example on old PC and it's more slow with ON option then OFF )
because on the old PC CPU is so slow. 

but, I do not know how this option works on mobile platforms. there are strong enough CPU to calculate occluders without losing FPS ?)

-------------------------

rogerdv | 2017-01-02 01:02:23 UTC | #3

I thought it was related to lights.

-------------------------

codingmonkey | 2017-01-02 01:02:24 UTC | #4

Well this is generally associated with rendering including with light )
light is not something in itself a separate and independent.

Light is only option for shader programm, shader can compute some light and some light not. 
Then less meshshe/objects brings to the rendering (in the camera frustrum, or behind front  solid geometry) theme less shaders will be fulfilled. (it's preserve GPU-power to other things)
occuders is optimization tech to exclude from rendering non visible geometry from next frame based on some kind simplified pre-frame calculation.

-------------------------

thebluefish | 2017-01-02 01:02:24 UTC | #5

Every Drawable can be an Occluder or Occludee. Essentially if an occludee is completely covered by an occluder in screen-space, then it won't be rendered.  Say you have a box which is an occluder and a 1,000,000 poly model that is an occludee. If you cannot see the model because it is hidden behind an occluder, then the system doesn't have to draw those 1,000,000 polys.

This is good because performance impacts can be localized. A game which takes place in close quarters could have a scene with many rooms, many objects, and many enemies. If the walls were occluders and all the objects/enemies occludees, then you would only be rendering what you can immediately see. So instead of rendering dozens of rooms and hundreds of items, you are rendering at most one room's worth of content at a time and maybe a hallway or two.

-------------------------

