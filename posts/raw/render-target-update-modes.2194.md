Andre_B | 2017-01-02 01:13:49 UTC | #1

Hi im working on a application that uses RenderTextures.

On a single frame i want to queue the update of a previous frame RenderTexture and use this result to render the current frame.
It all works well and good, except at the start the previous texture is black for 1 frame.

I have the previous RenderTexture on Manual Update Mode, and i just Queue an Update to it.

My question is, queuing an update doesn't mean it gets rendered instantly, i think it means i only receive the result on the next frame? is this correct?
Is there any way i could force an update to a render texture to be on this frame?

I can post some images later on when i get home if it helps.

-------------------------

cadaver | 2017-01-02 01:13:49 UTC | #2

The only thing that Urho guarantees is that texture viewports are rendered on the same frame before backbuffer viewports. This allows e.g. using an up-to-date reflection texture. However order between textures is not guaranteed. At least currently, all rendering always happens at the end of frame, and it's not possible to render "immediately".

-------------------------

Andre_B | 2017-01-02 01:13:49 UTC | #3

[quote="cadaver"]The only thing that Urho guarantees is that texture viewports are rendered on the same frame before backbuffer viewports. This allows e.g. using an up-to-date reflection texture. However order between textures is not guaranteed. At least currently, all rendering always happens at the end of frame, and it's not possible to render "immediately".[/quote]

Ok thank you for the confirmation.

-------------------------

