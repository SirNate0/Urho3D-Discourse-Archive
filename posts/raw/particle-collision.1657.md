Enhex | 2017-01-02 01:09:17 UTC | #1

If particle emitter would have an option or a derived class that enables detecting when particles collide with drawables, that would be useful.
Particle can be regarded as points so only a raycast towards the new position is needed.

I think that it would be a more efficient solution than using dedicated rigid body and billboard/particle emitter for every particle.

When it collides the user should have the flexibility to choose what to do, so it should have a callback and report the individual particle and raycast result.
Use cases are for example:
- Stop the particle's movement
- Make the particle slide along the collision plane.
- Make the particle bounce
- Remove the particle and create a decal on the drawable it collided it using the collision point & normal.

Using events might be too expensive and an overkill because I don't think other objects should be listening to the collisions.
From design prespective, just like how a particle emitter have a [i]"particle effect"[/i], it should also have a [i]"particle response"[/i].

-------------------------

Dave82 | 2017-01-02 01:09:17 UTC | #2

I already mentioned this in one of my posts (in my fire and direction aliged particles demo)


Basically i have everything in my head i just need time to code it :
Placing decals on collision point is not a good idea instead another particle form another emiter should be emitted at collision point (raindrops , explosions etc)

The ParicleEmitter class is enough for collision detection no additional derrivation is needed as you can implement this in the ParitlceEmitter's Update function.

What i want to do is :
- Graph based interpolation (linear , quadratic , and cosine) scale , color , size , velocity
- Direction aligned particles.
- Collision Detection : POP , BOUNCE , POP_SPAWN and SLIDENORMAL.
- Modifiers with masks (only has effect on Partilces with specific bit set):
     - Wind . vacuum , Force fields etc.
- Event based collision. However this can be expensive , but can be useful in some situation if smaller amount of particles are used.
- global sorting particles.Need to be sorted globally because flickering may occur (e.g smoke and fire emitters)

what i did so far :

- SetAutoremove(bool autoremove); If the emitter become inactive (all particles emitted) it is automatically removed.Useful in certain situations (gunsmoke , bullet hit sparks etc)
- GetActiveParticles(). Returns the number of active particles in the Particle Emitter

-------------------------

Enhex | 2017-01-02 01:09:17 UTC | #3

[quote="Dave82"]- Collision Detection : POP , BOUNCE , POP_SPAWN and SLIDENORMAL.[/quote]
Those are specific use cases. Limiting the API to hardcoded specific use cases isn't a good idea.

[quote="Dave82"]- Event based collision. However this can be expensive , but can be useful in some situation if smaller amount of particles are used.[/quote]
How will it be useful?
If you're using few particles you could just use a rigid body, or have a separate class that sends events.
The purpose of my suggestions is let the particle do something on collision, not some other object. It will be unneeded overhead.

The rest of the stuff you mentioned are off-topic, aren't related to particle collision.

-------------------------

sabotage3d | 2017-01-02 01:09:17 UTC | #4

I think it would be good idea to be attribute based rather than event based. For example Houdini's particle system writes an attribute when collision is detected. These are some of the attributes: [url]http://www.sidefx.com/docs/houdini15.0/nodes/dop/popcollisiondetect[/url]

-------------------------

TikariSakari | 2017-01-02 01:09:18 UTC | #5

I was thinking about this, and thought that maybe there could be 2 kinds of particle emitters. One that is stationary, and other one that can move. With the one that remains still, you could possibly generate collision geometry around the emitter to check the collisions against. I am not actually sure if it would speed things even up compared to actually doing actual ray cast against the environment. Another hacky approach that I thought could be adding some radius where particles that are within the radius gets skipped for collision detection, but I suppose then the particles needs to be ordered by their distance to the emitter.

Now if the emitter is actually moving one, then there needs to be more generic solution like what you mentioned the ray casting. It does sound quite a lot of calculation though, if you are using like 10 000 particles, then during every simulation update doing 10 000 ray casts generates dunno how many collision checks. I am also not sure how much more time consuming checks against complex shapes are. So this might be quite expensive in terms of performance, but then maybe it is really fast to iterate through all the particles for ray casting.

-------------------------

Enhex | 2017-01-02 01:09:19 UTC | #6

The particle emitter's position isn't the positions of the particles. Checking collision with the emitter is useless.

If you're going to use spheres for the collision you might as well use a rigid body and let Bullet do it more efficiently.

What use case do you have that needs 10,000 colliding particles?
The main use for such feature is stuff like debris effect, it's few dozens at most.
And still raycast would be the cheapest way I know of for a particle to detect collision.

-------------------------

TikariSakari | 2017-01-02 01:09:20 UTC | #7

[quote="Enhex"]
If you're using few particles you could just use a rigid body, or have a separate class that sends events.
The purpose of my suggestions is let the particle do something on collision, not some other object. It will be unneeded overhead.
[/quote]
[quote="Enhex"]The particle emitter's position isn't the positions of the particles. Checking collision with the emitter is useless.

If you're going to use spheres for the collision you might as well use a rigid body and let Bullet do it more efficiently.

What use case do you have that needs 10,000 colliding particles?
The main use for such feature is stuff like debris effect, it's few dozens at most.
And still raycast would be the cheapest way I know of for a particle to detect collision.[/quote]

Few dozens of particles, do you mean like few dozens of particles generated per frame or maximum number of particles the system can have during any given time. I meant maximum of 10000 particles on any given time. I haven't really used bullet, but if the maximum amount of particles at any given time is less than 100, is the Bullet really that slow, that it really would plummet all the performance?  

What I was thinking is, if you create collision geometry for your particle emitter, and with the assumption that it remains still, you should be able to predict the path the particles take during the creation of a particle. Since position would be calculated from s = v0t + (1/2)at^2, you could solve the t from the equation to see when the particle will hit something. On the other hand I am not really sure how easy it is to actually solve the t from trying to calculate the surroundings when the particle hits something = collision. Basically this would be same as doing ray cast at the creation time, just that when you add gravity to the particles, the movement of the particle becomes parabel, without gravity you could just do single ray cast on creation of a particle to determine the time it will collide to a surrounding object.

Now the problem is, that calculating the collision time during creation only works if the system doesn't have outside interference, which is probably the more common case. The particle system is moving, so the collision geometry around the particle emitter changes, or someone enters inside the emitter emitting range.

With the sphere, I meant something like geometrical sphere. Like as long as particles are inside the sphere, they aren't colliding with anything. Since the mathematical equation to sphere is x^2 + y^2 + z^2 = r^2, you could simply check if particle is within the radius of the sphere. Also you could possibly generate something like octree for the particle emitter and do collision checks for that. Then determine which of the particles remain in which octree and you would skip checking collision of the particles that aren't inside the octree that actually has a collision. You would just have to think a way to have a good sorting of particles to easily find which octree has the particle inside of them.

Sorry, I am not sure if any of this makes any kind of sense, I am generally terrible of explaining my thinking and these are only ideas, not something that I have actually tried.

-------------------------

Enhex | 2017-01-02 01:09:20 UTC | #8

The things you describe don't detect collision.

-------------------------

