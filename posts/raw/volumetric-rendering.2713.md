NiteLordz | 2017-01-16 15:45:43 UTC | #1

I have been looking thru the forums, and was wondering if anyone has attempted to create a volumetric renderer.  I am interested in implementing the Horizon Dawn Volumetric Clouds system, and if anyone has a head start on it, would jump in on it, otherwise, would will start from scratch.

Thanks much

-------------------------

dragonCASTjosh | 2017-01-16 21:05:39 UTC | #2

I think there has been a few experiments in the community on volumetric rendering but i dont think there is anything game ready. Once i start making progress on my long list of features i will eventually hit Volumetrics but likely not anytime soon. Once i get to it i will likely based my implementation upon [http://www.frostbite.com/2015/08/physically-based-unified-volumetric-rendering-in-frostbite/](http://www.frostbite.com/2015/08/physically-based-unified-volumetric-rendering-in-frostbite/)

-------------------------

SirNate0 | 2017-07-12 16:00:28 UTC | #3

Any progress with this?

-------------------------

godan | 2017-07-12 17:32:35 UTC | #4

For IOGRAM, I hacked together a material/shader combo that requires a box and a 3d texture. The shader renders the volume texture using some nice tricks. The advantage of this is that it fits in well with the existing render pipeline (i.e. you can easily control visibility/occlusion). <img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a8a342094c68cbc11b940baf6121251ec96396fa.jpg" width="690" height="370">

Also, I wrote some code to combine sequences of images in to a single 3d texture, and even modify the 3d texture directly.

Here are the sources: [[1]](https://gist.github.com/danhambleton/f318a91405c36aef15dc4cda4e93c451), [[2]](https://github.com/MeshGeometry/IogramSource/blob/master/Components/Graphics_Texture3D.cpp)

original post: https://discourse.urho3d.io/t/volume-shader-for-3d-textures/2966

-------------------------

Bananaft | 2017-07-27 10:05:42 UTC | #5

I've made a raymarching demo with some cool optimizations.
https://discourse.urho3d.io/t/3d-fractals-demo/2403

Horizon's cloud system would be super cool to play with. Hovever, it is super expencive, as my favorite part from their paper suggests:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/c63662311cea5c3a26cdf36ca722fe954d339d61.png'>
And both Horizon and [Unigine](https://developer.unigine.com/ru/devlog/20170206-unigine-2.4) are using either Temporal AA or some other form of reprojection to spread samples over time.

-------------------------

