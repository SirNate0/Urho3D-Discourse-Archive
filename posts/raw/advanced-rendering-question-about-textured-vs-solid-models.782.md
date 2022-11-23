devrich | 2017-01-02 01:02:51 UTC | #1

This is a pretty advanced topic and I have no idea how to find out the answer nor even google for it.  Here's the situation I have with my game idea:  Essentially; I have several models that don't "need" to be textured but do need to be either just a solid color or a shaded color.

My question is on the way that the renders ( for Linux, Android, Windows, and iOS ) will render my models.  [i][u]Textured[/u][/i] / [i][u]Shaded-Color[/u][/i] / [i][u]Solid-Color[/u][/i] ( i don't know yet if i can do just solid-color somehow )

Which way will render fastest / faster / fast ?

my "theory" is that if I don't use any materials or textures and just use a solid color for each mesh in the model ( every model will have 2 or more meshes ) then i "think" that the renderes will process them extremely fast compared to using textures.

Of course that "theory" is based on the work that the video cards do for OpenGL and OpenGL ES... However... my theory won't work out like i think if the various video card hardware is "designed" to render textures 'faster' than solid or shaded colors and that's something I have no clue about at all.

If you could let me know which order of speed that modern video card hardware will render my models at then I would be most extremely grateful for all the MASSIVE time and headaches you will be saving me  :smiley:

-------------------------

cadaver | 2017-01-02 01:02:51 UTC | #2

You could assume that the rendering which results in the least complex pixel shader will render fastest, given that other variables (like the vertex shader, amount of vertices, amount of screen space filled) stays constant.

The order from least to most complex would be:
untextured unlit
textured unlit
untextured lit
textured lit

Lighting stresses the arithmetic unit(s) while texture fetches stress memory bandwidth; either can become the bottleneck, or then the bottleneck may also be elsewhere such as vertex processing or framebuffer fillrate, in which case the pixel shader performance actually doesn't matter. To get from assumptions to results you will still have to measure on the target hardware(s). For example create a program which allows to easily switch between the materials while keeping everything else constant.

-------------------------

devrich | 2017-01-02 01:02:51 UTC | #3

Your explaination makes perfect sence to me!!  I'm going to next focus on getting a few more models for testing into my test Urho3D document and then i'll go to work getting  the test document to my android tablet for testing.  I hope to have that going in the next day.

Thanks cadaver!!

-------------------------

