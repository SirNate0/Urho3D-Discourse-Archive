vivienneanthony | 2017-01-02 01:04:39 UTC | #1

Hi,

Does any know how to turn off resize compression? I am using the code to resize a 2049 by 2049 texture 4097 by 4097. The  original image has no compression but I think compression is added on conversion. When i try to combine it with a higher image it fails segfault.

Any have any suggestion? Or links i can go to showing merhod or source.

Viv

-------------------------

TikariSakari | 2017-01-02 01:04:39 UTC | #2

Do you mean something like texture filter? At least texture has a function called SetFilterMode, which you can try setting to FILTER_NEAREST. I am not sure if that is what you are asking though.

Edit: I think I have misread the question tho.

Does gpus really accept textures that are that big? I think people do not recommend using over 2048x2048 textures in general. Also if you're generating mipmaps for the texture for LODs (I am not sure if urho does this by default, or how to even do them), then the size of the texture will be increased.

-------------------------

vivienneanthony | 2017-01-02 01:04:39 UTC | #3

I think most modern GPU's should be able handle 4096x4096 . The textures are being used to create terrain geometry unlesd that processed is pushed to the GPU.

I'm not sure how to set mip maps with the current Image class. If it was possible I would do geometry shape one layer then noisy perlin on the other.

-------------------------

vivienneanthony | 2017-01-02 01:04:39 UTC | #4

Can I generate the terrain height map then use [urho3d.github.io/documentation/1 ... 9d965ae566](http://urho3d.github.io/documentation/1.32/class_urho3_d_1_1_image.html#a6dd41c6d09d08071499e039d965ae566)?

Image  ->	PreCalculateMipLevel

-------------------------

