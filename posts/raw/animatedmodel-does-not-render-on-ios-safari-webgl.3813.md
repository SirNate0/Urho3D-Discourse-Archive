eldog | 2017-12-06 15:53:56 UTC | #1

On iOS 11 Safari using a StaticModel will render just fine, but when I try to use a AnimatedModel (mine has bones), it does not appear to render anything. I can interact with the rest of the scene just fine, but the AnimatedModel is not visible.

Android WebGL and desktop WebGL render the AnimatedModel. I'm not sure where to look, I'm wondering if there is an ios specific define that may need to be enabled.

-------------------------

Eugene | 2017-12-02 17:56:33 UTC | #2

Confirmed. When I checked WebGL demos on iOS yesterday, I saw this bug on the Navigation demo.

Debugging graphics is in my top 5 of most hated things. Debugging mobiles too.

I doubt there is any magic define. It looks like shader issue. Maybe bones uniforms are not updated, maybe they are not fetched properly. Maybe this is shader compiler bug, maybe it's Urho fault.

-------------------------

cadaver | 2017-12-02 22:47:20 UTC | #3

The graphics on WebGL assumes desktop-like capabilities, so it's likely to need scaling back / removing those assumptions if running on a mobile device. The shadow issue is very likely similar.

-------------------------

weitjong | 2017-12-03 01:56:27 UTC | #4

But what is the best way to do that? Sounds like the server needs to have two versions of the build, one for desktop and one for mobile browsers, and then the JS loader on the client side decides which version to load at run time?

-------------------------

cadaver | 2017-12-03 19:30:07 UTC | #5

That sounds cumbersome, so the ifdef checks would need to preferably become runtime capability queries instead, where possible.

Of course, when / if you get bgfx, the problem is likely to be moved from the lowlevel renderer to elsewhere, but principle remains the same.

But yeah, in general multiple capability levels are a headache..

-------------------------

weitjong | 2017-12-04 01:57:01 UTC | #6

The problem with web platform is, the “binary” (WASM or asm.js) is not installed, at most it is only cached and downloaded on demand when the cache expires. Assuming we were able to do multi-implementation in a single binary and to allow dynamic switch during run time based on the client capabilities, the binary would surely become bigger and it contains the other bits that the client will not require.

What would be ideal is the build system able to generate multiple binary modules (one common + one for each target deployment) in one go during compile time; and the JS on client side is responsible to load the correct modules during run time.

-------------------------

eldog | 2017-12-06 15:53:50 UTC | #7

Found a solution.

Similar to the Raspberry Pi, the problem is the maximum number of bones. Probably to do with the number of uniforms that iOS safari supports, there's [this issue](https://github.com/mrdoob/three.js/issues/7807) on threejs that describes a similar problem they experienced.

The change required was in `Graphics::GetMaxBones()` [here](https://github.com/urho3d/Urho3D/blob/54ed4c917f242817029797a72eb7867ea7ab0247/Source/Urho3D/Graphics/OpenGL/OGLGraphics.cpp#L2154). I changes it to `return 16;` and it worked, I don't know what the correct number for iOS Safari is at the moment (according to that threejs issue they like to change it from time to time).

![bunion-ios|280x500](upload://cFicgA646NU0gtuTUpQybTJlKO2.gif)

Animations running at 60fps on iOS :)

-------------------------

