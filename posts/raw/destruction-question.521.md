sabotage3d | 2017-01-02 01:01:04 UTC | #1

As Urho3d is using bullet physics are some of the features exposed like compound shapes and fracturing. By compound shapes I mean gluing multiple pieces together to act as one rigid body as constraints are a lot more expensive. Any hints on how to achieve that with Urho3d. It is fairly straightforward with bullet itself but I would like to use the Urho3d bullet wrapper and component system.

Thanks,

Alex

-------------------------

weitjong | 2017-01-02 01:01:04 UTC | #2

I think the compound shape has been supported for quite some time now. Have you read this section of the documentation ([urho3d.github.io/documentation/H ... s_Movement](http://urho3d.github.io/documentation/HEAD/_physics.html#Physics_Movement))?  It explains how to create a compound shape in one sentence.

-------------------------

sabotage3d | 2017-01-02 01:01:05 UTC | #3

I am talking about this bullet physics demo: [github.com/bulletphysics/bullet ... actureDemo](https://github.com/bulletphysics/bullet3/tree/master/Demos/FractureDemo) 
Also this a good a example of glue: [youtube.com/watch?v=cX6o7OCOuf8](https://www.youtube.com/watch?v=cX6o7OCOuf8)
Where you have compounds shapes glued together when they collide with another object they break into seperate objects. 
We could have arrays of primitives that will define the connectivity order between the pieces.

-------------------------

weitjong | 2017-01-02 01:01:05 UTC | #4

Sorry to misunderstood you. I have never tried gluing and fracturing of the compound shapes as in the demo in Urho3D. May be other could help.

-------------------------

cadaver | 2017-01-02 01:01:06 UTC | #5

The specific Compound Fracture mechanism is not part of Urho's Bullet integration. Features which require you to subclass Bullet classes are difficult to add, unless you would create new corresponding Urho components.

-------------------------

sabotage3d | 2017-01-02 01:01:06 UTC | #6

Is there a simple example on how to extend Urho3d bullet integration, without changing the core library ?

-------------------------

cadaver | 2017-01-02 01:01:06 UTC | #7

No. There are generic examples of how to add new C++ components in the Source/Samples directory, like 05_AnimatingScene, 18_CharacterDemo and 19_VehicleDemo. I'm not completely sure, as the used parts of Bullet are linked into the Urho3D library, whether you're able to use additional Bullet features without causing undefined reference errors (to the functionality that wasn't linked in when Urho3D was built). If that is the case, you should not be afraid to modify Urho core itself. If the added features are cleanly implemented, it's likely they would be accepted as a pull request.

-------------------------

sabotage3d | 2017-01-02 01:01:06 UTC | #8

Thanks a I will look into this

-------------------------

smellymumbler | 2017-03-01 17:35:25 UTC | #9

Did you had any luck with this? I was also curious about destruction capabilities.

-------------------------

