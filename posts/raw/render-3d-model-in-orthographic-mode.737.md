NiteLordz | 2017-01-02 01:02:34 UTC | #1

How can i go about rendering a 3D model so that it is always positioned in the same place on the screen ? 

i have been looking at the override view flag, but i am not sure as it is attached to the camera.  Do i need to create a second camera, if so, how do i assign this model to only render from that camera view.

Thanks for any help

-------------------------

cadaver | 2017-01-02 01:02:34 UTC | #2

One way you'll certainly achieve exactly what you want is to create a second scene with only that model, and a second camera. Then use a renderpath that doesn't clear color or depth.

Alternatively look at the Skybox class and how it sets a custom transform. By using exactly the camera's world transform you would effectively remove its view transform and always render in the same spot.

(interestingly it seems nothing uses overrideView_ in Urho's current classes any more so we could remove it, simplifying the render code EDIT: make that nothing except deferred volume batches, meaning it can't be easily removed after all  :smiling_imp:  )

-------------------------

NiteLordz | 2017-01-02 01:02:34 UTC | #3

Thanks for your quick reply. I am not sure the skybox route is the one i want to go with.  I think the second scene will work better, as i will have multiple objects rendered in this manner.

-------------------------

