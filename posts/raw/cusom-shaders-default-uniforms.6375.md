Avagrande | 2020-09-07 15:47:50 UTC | #1

 I am in the position where I have a particular shader being used multiple times across many materials and its a real chore to specify a parameter for each one individually so I would like to give them default values and then tweak them slightly when needed in each material. 

I tried to just initialise the uniform but this only works on recent glsl versions, is there a way to tell urho3d to upload a default value for a uniform?

-------------------------

Eugene | 2020-09-07 17:18:18 UTC | #2

If you want generic and stable solution, you will find it outside of shader core or Graphics subsystem in general.
E.g. just make a script or something that automatically sets shader parameter in Material if it's not present, or something like that.

Capacity of setting default parameter value in shader will require multi-system refactoring of Graphics and Renderer subsystems (as far as my understanding goes). It may be simpler if you need only OpenGL and only free uniforms (i.e. no uniform buffers), but generic solution is complicated.

-------------------------

