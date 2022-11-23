Lumak | 2018-03-30 20:11:47 UTC | #1

Just another one of those videos to inspire others on this forum. 

Does it actually inspire others? I wonder.

Side friction stiffness settings:
front: 0.8f
rear: 0.04f

https://youtu.be/L05nckGYOEU

-------------------------

elix22 | 2018-03-30 23:01:57 UTC | #2

Nice .
I guess it's a Chibii racers retro car.

-------------------------

Lumak | 2018-03-31 00:54:15 UTC | #3

Yes, that's correct. I bought several art packs from 3drt and noticed you were using the retro set as well. I gotta say, it's nice to work with something of a quality, unlike my pickup truck that I made in my offroad repo.

oh, wait. The name of the person that made the android racer started with 'E' and I thought it was you, but it's extobias.

-------------------------

extobias | 2018-03-31 00:41:13 UTC | #4

That's really nice. I'm trying to get the same effects, unsuccessfully, for a couple of weeks. The thing is I would to have several height's on the track but the car is flying in the curves with heights.

-------------------------

Lumak | 2018-03-31 00:56:22 UTC | #5

What do you mean by added heights, something like a ramp, speed bump, or gradual height elevation on the road?

-------------------------

extobias | 2018-03-31 18:10:19 UTC | #6

Like in gradual height elevation. The front wheels start to bumping, even applying a down force.
I've playing with sideFrictionStiffness, but the problem occurs when the car takes the curve with height.


https://youtu.be/EnV_52BAL60

-------------------------

Lumak | 2018-03-31 18:44:09 UTC | #7

OK, I understand what you mean.  One thing that can help force the vehicle to stay on the ground is to apply a downward force.  In the original 19_VehicleDemo, there's this block:
[code]
    // Apply downforce proportional to velocity
    Vector3 localVelocity = hullRot.Inverse() * hullBody_->GetLinearVelocity();
    hullBody_->ApplyForce(hullRot * Vector3::DOWN * Abs(localVelocity.z_) * DOWN_FORCE);
[/code]

I do something similar but apply force only when one of the wheel is not touching:
[code]
void Vehicle::ApplyDownwardForce()
{
    // apply downward force when some wheels are grounded
    if (numWheelContacts_ != numWheels_ )
    {
        // small arbitrary multiplier
        const float velocityMultiplyer = 1.00f;
        Vector3 downNormal = node_->GetUp() * -1.0f;
        float velocityMag = hullBody_->GetLinearVelocity().LengthSquared() * velocityMultiplyer;
        velocityMag = Clamp(velocityMag, MIN_DOWN_FORCE, MAX_DOWN_FORCE);
        hullBody_->ApplyForce(velocityMag * downNormal);
    }
}
[/code]

The **velocityMultiplyer** is a tweakable value, which I haven't touched yet. And the MIN_DOWN_FORCE and MAX_DOWN_FORCE are set to 10.0f and 1e4f, respectively. The MAX value is pretty high, but I tend to have my vehicles travel at much faster speed than normal.

edit: You should also consider raising your sidewalls, though.

-------------------------

noskopo | 2018-04-01 14:40:07 UTC | #8

How did you make the tire tracks? :grinning:

-------------------------

Lumak | 2018-04-01 17:19:10 UTC | #9

Welcome to the forum noskopo. You can find the skid track code here, https://github.com/Lumak/Urho3D-Offroad-Vehicle

-------------------------

slapin | 2018-04-02 01:55:46 UTC | #10

I think you could try to play with:
1. vehicle center of mass and your collision shape. In some cases one can make car which
can't flip at all.
2. If you're using raycast vehicle, try to increase spring stiffness.
3. If you're using raycast vehicle, try also decreasing roll influence.
Also I find it amusing to use 2 downforces - one when all wheels touch ground and another which
whorks when at least one wheel touches ground. This makes vehicle hard to go flying for no reason.
Also try to learn yourself a bit about real vehicle physics parameters to make sure the behavior is not too
unrealistic and makes sense at least a tiny bit. Articles like https://www.howacarworks.com/basics/how-the-transmission-works and http://blender3d.org.ua/forum/game/iwe/upload/Vehicle_Simulation_With_Bullet.pdf
and http://www.asawicki.info/Mirror/Car%20Physics%20for%20Games/Car%20Physics%20for%20Games.html
help a lot with understanding mechanics. Also, try some common games like Tux Racer, GTA3/VC/SA and try to feel the difference and what you really like and dislike.
Hope that helps.

-------------------------

slapin | 2018-04-02 01:59:49 UTC | #11

Also Bullet term for "I use convex hull and my vehicle behaves strange, I did everything abouc center of mass and still can't make it behave, Havok fixes it easily with inertia shape" is Inertia Tensor. Just for records.

-------------------------

slapin | 2018-04-02 02:05:07 UTC | #12

Well, your track is too flat, a little curve for it and slight elevation of some parts would make it much more interesting...
About side friction - how do you implement it? The problem about  original btRaycastVehicle in addition to wheel rotation is absence of control of side to side slide. Probably this also should depend on track surface somehow, but I did not go that far yet. (Urho3D component fixes wheel rotation, but not side-side sliding).

-------------------------

Lumak | 2018-04-02 16:53:23 UTC | #13

[quote="slapin, post:12, topic:4142"]
Well, your track is too flat, a little curve for it and slight elevation of some parts would make it much more interesting…
[/quote]

That won't happen until the level design/creation phase. I still have a couple of dynamics to work out first before I get to that point.

[quote="slapin, post:12, topic:4142"]
About side friction - how do you implement it?
[/quote]

You reviewed the "offroad repo" a long time ago -- it's the changes to the btRaycastVehicle side.

-------------------------

Lumak | 2018-04-04 21:14:00 UTC | #14

I just tested this bit for auto correct pitch roll: //ref from https://discourse.urho3d.io/t/constraint-class-working-on-derived-class/4081/6
[code]
void Vehicle::AutoCorrectPitchRoll()
{
    // auto correct pitch and roll while air borne
    if (numWheelContacts_ == 0)
    {
        // ref from https://discourse.urho3d.io/t/constraint-class-working-on-derived-class/4081/6
        const float stability = 0.3f;
        const float speed = 1.5f;
        Vector3 predictedUp = Quaternion(hullBody_->GetAngularVelocity().Length() * M_DEGTORAD * stability / speed,
                                         hullBody_->GetAngularVelocity()) * node_->GetUp();
        Vector3 torqueVector = predictedUp.CrossProduct(Vector3::UP);
        torqueVector *= speed * speed * m_fVehicleMass;
        hullBody_->ApplyTorque(torqueVector);
    }
}
[/code]
The predictedUp calculation is clever and it works a lot better.

edit: I added this to the repo minutes ago.

-------------------------

Lumak | 2018-04-05 19:00:38 UTC | #15

21 AI vehicles pathing on a spline. Tested on my Android phone and it ran very smooth.

https://youtu.be/fjFJ9B2C49k

-------------------------

slapin | 2018-04-06 09:16:13 UTC | #16

Your phone is tough.
Mine can handle up to 5 btRaycastVehicles, so I have to LOD and run distant ones without physics.

-------------------------

slapin | 2018-04-06 09:21:08 UTC | #17

I mean without Bullet as I do very simple fake physics manually. I think it depends on terrain
and various other aspects like my phone is Meizu M5 note.

-------------------------

Lumak | 2018-04-06 10:07:01 UTC | #18

I'm not usually up this early, but went to bed early and just got up for no good reason.  Anyway, my phone is Android 4.1.2, API 16, a duo-core arm, and yours is Android 6.0 with an octa-core cpu, a more powerful phone. It's hard to believe that you can only have 5 raycast vehicles in your scene.  It must be the terrain. I don't have it in my scene nor did I have it testing on my phone.

-------------------------

slapin | 2018-04-06 10:27:24 UTC | #19

Well, I did play with raycast schedule pipeline, and it does have potential. so maybe I will be able to run more than 5 vehicles as I come to this, I just need to write another subsystem for this.

-------------------------

slapin | 2018-04-06 10:31:44 UTC | #20

btw, my terrain is 240x240 grid (procedural, but nothing fancy), distance between vertices is 1 unit. So one have to be careful about raycasts to survive.

-------------------------

Lumak | 2018-04-07 19:44:47 UTC | #21

Could the culprit for your performance caused by your custom terrain? The default terrain uses Bullet's btHeightfieldTerrainShape, and I don't remember the performance being bad.

-------------------------

slapin | 2018-04-08 03:22:54 UTC | #22

Yes, the terrain is custom and uses btHeightfieldTerrainShape but also I use AI to prevent collisions, which uses raycasts too, and it seems somehow it chokes on large amount of raycasts per frame. After I implemented priority queue of raycasts and removed physics from distant vehicles (I run simple car physics on them which is fully custom - just simple integration of 3 values) I can run about 20 vehicles at 20 fps.

-------------------------

weitjong | 2018-04-08 07:16:50 UTC | #23

@slapin Please stay on the topic. If you have an issue, please create another thread of your own.

-------------------------

Lumak | 2018-04-08 15:29:23 UTC | #24

@weitjong, he is on topic.

@slapin - right, the raycast performance issue. Have you tried using the **RaycastSingleSegmented()** fn for ray lengths > 10 meters? You'll get a better performance than the **RaycastSingle()** fn.

-------------------------

weitjong | 2018-04-08 15:45:55 UTC | #25

@Lumak, If you say so. Have fun.

-------------------------

slapin | 2018-04-09 06:15:17 UTC | #26

Ah, thanks for RaycastSingleSegmented() - this is really makes difference. I can run ~30 vehicles this way. I think using threaded raycast would make it even better, but I don't have guts to look that direction. Thanks a lot! This looks like I can increase. performance for NPCs too.

-------------------------

Enhex | 2018-04-09 07:52:59 UTC | #27

RaycastSingleSegmented() is based on Bullet's raycasting.
Might be relevant:
https://pybullet.org/Bullet/phpBB3/viewtopic.php?t=10143

Bullet's author confirms here raycasts are thread safe when not stepping the world.

-------------------------

Lumak | 2018-04-16 22:21:33 UTC | #28

Network testing - what you see in the video is on the client side. The host is sitting at the starting line.  All other drivers are AI. 

https://youtu.be/Yismp9qJI_o

-------------------------

elix22 | 2018-04-17 05:35:13 UTC | #29

Nice !
I am also playing with it lately , creating scenes with race cars.
I uploaded some video , all of them are AI driven , runs also flawlessly on  low range Android and iOS mobiles

https://www.youtube.com/watch?v=306y2R00IQk&feature=youtu.be

-------------------------

Lumak | 2018-04-17 06:13:04 UTC | #30

Oh, sweet! Wow, you got a full level designed and created already, awesome. That's probably my most difficult part in my game development. I get to that point in my prototypes and ... just draw blank.

What type of AI pathing do you use?

-------------------------

elix22 | 2018-04-17 11:55:44 UTC | #31

For AI , 
I am using "Chase The Rabbit" algorithm .
Basically each car is following its own  virtual invisible "rabbit" .
Each rabbit (node) is following predefined markers that form different paths , with some random salt modified each frame causing it to jump from path to path
Every frame :
The acceleration of the car is modified based upon its distance to its "rabbit" 
The steering of the car is modified based of direction of the car in relation to its "rabbit" in world space
In addition I am raycasting several rays from each car to the sides and front to detect collision with other cars , and modify steering & acceleration accordingly .

Regarding the level itself , I am using my "wild imagination" :slight_smile:
Basically adding & removing some stuff and see how it looks , a lot of trial and error , still not happy with it.

-------------------------

Lumak | 2018-04-17 21:00:16 UTC | #32

Tid bit of info about my vehicle setup for network:
* rigibody - REPLICATED
* collisonshape - REPLICATED
* prefab xml car node layout: hubs, steering wheel node, driver node, static models - all LOCAL
* raycast vehicle (btRaycastVehicle) - LOCAL
* wheels - LOCAL
* sounds - LOCAL
* skid track - LOCAL

-------------------------

Lumak | 2018-05-16 17:15:49 UTC | #33

My 1st semi-completed level testing.

https://youtu.be/SSl8PPOqh6g

-------------------------

Lumak | 2018-05-17 03:12:08 UTC | #34

I've just looked at my profiler view of the level and the race from the vid above and got my total memory usage is shown as 7.2MB. I added extra dump in the largest memory user for each type of resource and got:
[code]
rscgrp: Texture2D, largest: name=Textures/vp_sky_v3_007_1024LGT.png, size=2.7 M 
rscgrp: Technique, largest: name=Techniques/NoTexture.xml, size=1.4 k           
rscgrp: XMLFile, largest: name=track6/track6.xml, size=47.3 k                   
rscgrp: Image, largest: name=Textures/UI.png, size=128.0 k                      
rscgrp: Font, largest: name=Fonts/Anonymous Pro.ttf, size=12.2 M                
rscgrp: Model, largest: name=Models/Sphere.mdl, size=41.9 k                     
rscgrp: Material, largest: name=Materials/pineMat.xml, size=588 b               
rscgrp: TextureCube, largest: name=Textures/Level0Cube.xml, size=128.3 k        
rscgrp: Sound, largest: name=Sounds/engine-prototype.ogg, size=119.9 k          
rscgrp: Shader, largest: name=Shaders/GLSL/LitSolid.glsl, size=122.9 k          
rscgrp: Animation, largest: name=Racers/Racer_Idle.ani, size=79.2 k             

[/code]

My question is, how is the total memory 7.2MB while the font usage is 12.2MB?

-------------------------

