cin | 2017-01-02 00:57:49 UTC | #1

Which unit used in Urho3D?
I think what 1 unit = 1 inch.
Bullet use metric system: [bulletphysics.org/mediawiki- ... _The_World](http://www.bulletphysics.org/mediawiki-1.5.8/index.php?title=Scaling_The_World)
I must scale all models to meters?

-------------------------

friesencr | 2017-01-02 00:57:49 UTC | #2

Different 3d modeling tools have a weird conversion thing.  I seem to recall that 3ds max/maya may scale everything down 100x.  There might be a fudge in asset import to try to correct this.

-------------------------

cadaver | 2017-01-02 00:57:49 UTC | #3

The recommended unit is meter, so that Bullet gravity works out of the box. Also the default Camera far clip view = 1000 units, which is thought to mean 1 km. However if you adjust things like gravity and far clip, you can use whatever unit convention you want. NinjaSnowWar used to use 1 cm until the models were downscaled.

The AssetImporter tool code itself shouldn't have any fudges, however some loaders in Assimp might have (haven't checked in detail.)

-------------------------

NemesisFS | 2017-01-02 00:57:50 UTC | #4

so the engine automatically scales everything, I just need to adjust the gravity?
The bullet wiki claims that one needs to scale a lot more. Can I ignore that?

-------------------------

cadaver | 2017-01-02 00:57:52 UTC | #5

The engine doesn't scale anything automatically, it uses the assets exactly like they're given to it. All camera parameters and vertex positions are just numbers to it, it doesn't know what real-world units they represent.

Most important criteria in use of Bullet is that there are no huge mass ratio differences between objects (ie. not very light and not very heavy objects). The NInjaSnowWar objects use kilograms for mass, so ninja has mass 80, which is quite credible, but the mass of the snowballs has been set to a ridiculously high value (10 kg) so that they seem to have a noticeable effect on the objects they collide with. I'd just tweak the values so that they seem to make sense for the gameplay you're trying to achieve.

-------------------------

