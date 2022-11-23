HaeferlKaffee | 2018-08-14 16:42:31 UTC | #1

Changing the size of the depth rendertarget in any technique XML breaks the viewport result. Is this supposed to happen? Is there a better way to resize the depth image, ideally using nearest-neighbour interp?

Example: sizedivisor = "2 2"
![broken|690x387](upload://kBiQ2O8YIhWvcrjQ46ggOAFXBnZ.png)

-------------------------

Bananaft | 2018-08-16 19:11:06 UTC | #2

Are you sizedividing all render targets or just depth? If your pass is outputting multiple render targets they all have to be same size.

-------------------------

HaeferlKaffee | 2018-08-16 20:09:48 UTC | #3

Well the default renderpaths only have one rendertarget, depth

-------------------------

Bananaft | 2018-08-17 20:25:56 UTC | #4

Oh, yeah, there is also default rendertarget. So you should add an "rgba" rendertarget (assuming, you are not going to use HDR, in that case "rgba16f") set it as output for all scenepasses, then add quad command with CopyFramebuffer shader, that will read your lowres rendertarget, and output it to default rendertarget.

-------------------------

HaeferlKaffee | 2018-08-17 10:14:38 UTC | #5

This seems to have worked, thanks

-------------------------

Bananaft | 2018-08-17 20:25:56 UTC | #6

Wooo! gimme that tasty "solved" badge.

-------------------------

