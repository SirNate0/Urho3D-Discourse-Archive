Dave82 | 2017-01-02 01:05:34 UTC | #1

Hi i started expanding the particle effect class. What i did so far :

- Random texture atlas frames
- Gravity
- Graph based interpolation (linear/ cosine) of scale and velocity (this is still experimetal i'm tring to use it for explosions and mushroom cloud)

But can't figure out how to implement direction aligned particles. As i remember in SPARK2 it was done by directly recalculating the quad's vertex positions (apply rotation,scale , and translate) 
but in urho it is done by storing the quad in 2d (MASK_TEXCOORD2). Does this mean that the particle calculations are performed on GPU ? if so , what/where would be the best way to modify the code to add direction in 3d to them ?

Also there's some small problem with colorfade values as the time values are scaled instead of normalized. If you have particles with random lifetime beween 5 and 9. You can't set the correct color values for both of them (if your last time-key is 9 then particles with liftime of 5 will pop earlier or vice versa)

Wouldn't it be better to store time values normalized ? (0 - born of the particle 1- death of the particle inependently of their lifetimes) ?

-------------------------

cadaver | 2017-01-02 01:05:34 UTC | #2

Yes, final quad vertices are calculated by the shader from the particle size stored in TEXCOORD2. You could modify the shader and add the direction to another vertex element, if you wish.

For the timelines I would guess both usecases (scaled and absolute times) would be appropriate at times, and especially something like "using scaled time for fade and absolute time for texture animation". So maybe add "use scaled time" booleans for both.

-------------------------

Dave82 | 2017-01-02 01:05:34 UTC | #3

[quote]Yes, final quad vertices are calculated by the shader from the particle[/quote]

Thats good news ! most of the particle engines (at least the open source ones) are all CPU based. including SPARK2.  For now i implemented somekind of a "poor man's direction aligned particles" by transforming the direction to camera world.

[code]Vector3 tDir = camWorldRot.Inverse() * particle.velocity_.Normalized();
billboard.rotation_ = Quaternion(tDir , Vector3::UP).EulerAngles().z_;[/code]

It works quite nice except when the particle moves towards or away from the camera and there's no rotation on the z axis :slight_smile: , but definitely usable...

-------------------------

Dave82 | 2017-01-02 01:05:35 UTC | #4

Well here are some particle effects with the modified effects class


Simple Fire

[video]https://www.youtube.com/watch?v=rKGEkiXxce4&feature=youtu.be[/video]

Direction Aligned particles : (Sorry for the bad quality...)

[video]https://www.youtube.com/watch?v=EJBgzXKlCt8[/video]



Some ideas (What do you think ?):

- Collision detection (using raycast or spherecast)
- COLLISIONMODE_POP                if the particle hits the body , it pops
- COLLISIONMODE_SPAWNPOP      if the particle hits a body a particle is spawned at hit pos from another emitter
- COLLISIONMODE_BOUNCE          The particle is bouncing in the direction's reflection vector

EmitterAttach :
Attaching an emitter to another emitter (each particle will create a trail using particles from the attached emitter. May be used for explosions) although this may need more modification of the particle source

-------------------------

weitjong | 2017-01-02 01:05:35 UTC | #5

Cool. Hope to see the changes to be merged into main branch.

-------------------------

v0van1981 | 2017-01-02 01:05:36 UTC | #6

Look nice! Do you plan to open the source code?

-------------------------

Dave82 | 2017-01-02 01:05:36 UTC | #7

[quote="weitjong"]Cool. Hope to see the changes to be merged into main branch.[/quote]
[quote="v0van1981"]Look nice! Do you plan to open the source code?[/quote]

Thanks! i will pull request ASAP  The only problem is i'm recently started learning git  :slight_smile: , so it will take some time...

-------------------------

weitjong | 2017-01-02 01:05:36 UTC | #8

I was new to git as well but luckily I have a friend called Google  :smiley:. Looking forward for your PR!

-------------------------

sabotage3d | 2017-01-02 01:13:49 UTC | #9

Hi guys, is there any update on this?

-------------------------

