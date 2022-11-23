inqubator | 2017-01-02 01:03:26 UTC | #1

Hello!

We created iPhone examples of Urho3D, and the camera can be moved with touch, but not the character. Is this a normal behaviour?

CharacterDemo seems to have "patchInstructions" variable etc. for on-screen joystick; how can this be enabled?

And, is it normal that the output does not fit on the Iphone screen? it looks squared and doesn't rotate when screen is rotated.

Thank you!

-------------------------

hdunderscore | 2017-01-02 01:03:37 UTC | #2

Hi,

I do believe it's normal to be able to move the view and not the character with touch input in the samples (you can change that if you want of course).

By default, the touch controls should appear in the samples when touch input is received. I haven't tested on iphone myself, so I am not sure if those are expected errors although I suspect that's not the case.

-------------------------

weitjong | 2017-01-02 01:03:42 UTC | #3

[quote="inqubator"]CharacterDemo seems to have "patchInstructions" variable etc. for on-screen joystick; how can this be enabled?[/quote]
You don't have to use "patching" approach as the sample. You can define a [b]complete[/b] on-screen joystick UI layout using the Editor app or hand-coded the XML manually. Since we have a lot of sample apps and most of them can share a basic same layout, our approach is to use this basic UI layout and then specialized it as needed using the XML patching mechanism for each sample. But to answer your question directly, there is no special option required to enable this XML patching mechanism. The patching mechanism is available for [b]any[/b] XML resources and not just limited to UI layout XML file. See [github.com/urho3d/Urho3D/pull/119](https://github.com/urho3d/Urho3D/pull/119) for more detail. You may have to look into the XMLFile::Patch() method to see how it works.

-------------------------

