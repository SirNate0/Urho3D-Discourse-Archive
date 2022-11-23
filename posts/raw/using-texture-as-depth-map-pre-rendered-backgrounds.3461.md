napoleon | 2017-08-19 14:58:51 UTC | #1

Hi all,

So I'd like to use pre-rendered backgrounds like in the first Resident Evil games.
For this I render my backgrounds in Blender and then render the depth values to a grayscale image (with the values {0, 1} stretching from the near to far clip).

Is there a way to "render" the values from the grayscale texture directly into the depth buffer?

Thanks in advance!

-------------------------

Bananaft | 2017-08-22 19:57:58 UTC | #2

As far as I know, you can not write into depth buffer that is used by GPU for pixel sorting. You can however read your own depth in pixel shader, and discard pixels that are further away.

Another solution would be to use mesh occludes - invisible meshes, that are only rendered into depth buffer. Like some old games did it:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/c43be8dce3f7b7384e25c5f396e838ae51adeb59.png'>
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/540918c3bdf146dbf91c88b035997d9caedc6877.png'>

-------------------------

napoleon | 2017-08-23 13:59:10 UTC | #3

Thank you very much! I was experimenting with a much more complicated solution, but I guess using occludes will be more suitable (and actually work).
For testing this method I rendered my occlude mesh with a modified version of the "Unlit" shader, where I simply deleted the "oColor" definitions, so only "oDepth" will be written into, but nothing happens, the stuff behind the occlude is still visible. Is that the correct way to do it? (I don't know much about hlsl shaders.)
Here is a part of the "PS" section of my hlsl shader: (The rest is identical to the standard "Unlit" shader)

    #if defined(PREPASS)
        // Fill light pre-pass G-Buffer
        oColor = float4(0.5, 0.5, 0.5, 1.0);
        oDepth = iWorldPos.w;
    #elif defined(DEFERRED)
        // Fill deferred G-buffer
        //oColor = float4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
        //oAlbedo = float4(0.0, 0.0, 0.0, 0.0);
       //oNormal = float4(0.5, 0.5, 0.5, 1.0);
        oDepth = iWorldPos.w;
    #else
        //oColor = float4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
    #endif

EDIT: To elaborate: I now have two scenes and two viewports to first render the background and then the rest on top of it ([like this](https://discourse.urho3d.io/t/how-to-layer-scenes/740/4)). So I guess I need to have a shader where nothing except for the depth values is drawn, correct? If no color output occured, shouldn't you be able to see the background viewport instead?

-------------------------

Bananaft | 2017-08-29 14:35:08 UTC | #4

Stuff like this must be determined by technique, not shader: https://urho3d.github.io/documentation/1.4/_materials.html
here are some solutions you can try:
1) Enabling depthwrite and depthtest, setting blend mode to add and outputting black color in shader.

2) Assuming you are using ForwardDepth render path, you can make a technique that renders your occluder during depth scenepass, and does nothing during base scenepass.

3) Another way is to write a shader for your occluder, that reads your background image in screen coordinates(rather than UVs) and outputs as oColor. That way painting background image on top of any geometry that further away.

-------------------------

napoleon | 2017-08-29 14:32:57 UTC | #5

Oh man, thank you so much! I used the first solution and it finally works!
I gained much insight into the network of shaders, scenepasses and techniques, thank you!

-------------------------

Bananaft | 2017-08-29 18:16:20 UTC | #6

Ugh, actually, on second thought i realized, there could be a pitfall with this method.  You have to somehow be sure, that occluder is drawn before stuff that needs to be occluded. Otherwise it wont work. Engine is choosing order to draw stuff in opaque pass with fancy algorithm, to draw stuff faster, there is no guarantee it will keep this particular order forever.

I guess, you should draw only occluders in base pass, and occludable objects in postopaque pass.

-------------------------

