codder | 2017-01-02 01:12:50 UTC | #1

Hello,

I have a problem which I could not figure out the solution.
I'm drawing some textured vertices using graphics->Draw(...) and before calling it I want to apply some effects similar to post processing.
Is there a way to sample the rendertarget just for the incoming vertex & index array?

To clarify:
I draw a texture using custom array and then I want to apply a blur effect on top but without affecting the rest of the scene / draw calls.

-------------------------

1vanK | 2017-01-02 01:12:50 UTC | #2

[quote="codder"]Hello,

I have a problem which I could not figure out the solution.
I'm drawing some textured vertices using graphics->Draw(...) and before calling it I want to apply some effects similar to post processing.
Is there a way to sample the rendertarget just for the incoming vertex & index array?

To clarify:
I draw a texture using custom array and then I want to apply a blur effect on top but without affecting the rest of the scene / draw calls.[/quote]

U can create custom pass in RenderPath, which outs result to some texture

[code]
<command type="scenepass" pass="myPass" output="myTexture" ... />
[/code]

Also, you need to create material with this pass. Then all objects used this material will be rendererd to separate texture. U can blur this texture and output over scene.

-------------------------

1vanK | 2017-01-02 01:12:50 UTC | #3

Or u can draw mask of affected objects  to some texture and use this mask in your modified blurred shader.

-------------------------

codder | 2017-01-02 01:12:51 UTC | #4

[quote="1vanK"]Or u can draw mask of affected objects  to some texture and use this mask in your modified blurred shader.[/quote]

Any tips on achieving this?

-------------------------

1vanK | 2017-01-02 01:12:51 UTC | #5

u can see [github.com/1vanK/Urho3DOutlineSelectionExample](https://github.com/1vanK/Urho3DOutlineSelectionExample)

-------------------------

codder | 2017-01-02 01:12:52 UTC | #6

Thanks

-------------------------

