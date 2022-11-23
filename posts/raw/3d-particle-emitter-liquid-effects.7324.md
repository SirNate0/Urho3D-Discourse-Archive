Jens | 2022-09-08 14:13:44 UTC | #1

Is this possible? None of the sample particle effect xml files (I can find) produce anything like a liquid, which could be useful for example blood splatter from a hit enemy. There neither seems to be much documentation regarding the various parameters in the xml files.

One thing I'm finding confusing is the colour of the resulting particles

```
<particleeffect>
	  <material name="Particles/Particle.xml" />
```
Particle.xml references flare.dds; altering the colour of the dds image makes no difference to the result that I can see.

-------------------------

SirNate0 | 2022-09-08 17:03:51 UTC | #2

I believe Particle.xml uses vertex colors for the coloration, I think multiplied by the texture. So if you tint a circle a little green but have very red vertex colors from the particles, you will likely end up with a (darker) red particle.

Not sure about the liquid effects, I'm probably working on a more abstract looking game than I suspect you want, so I imagine my approach wouldn't work for you.

-------------------------

Jens | 2022-09-08 19:45:45 UTC | #3

Ok, thanks. I can, though, not figure out where it gets the colour information. The only colour reference seems to be in burst.xml via the colorfade parameters, but taking these out makes no apparent difference to the particle colours. Perhaps the necessary parameter is missing from these samples.

I'm not sure any type of realistic liquid particles are possible - I've searched for a while and can only find explosive/fire/smoke effects.

```
burst.xml
<particleeffect>
	 <material name="Particles/Particle.xml" />
	<numparticles value="500" />
	<updateinvisible enable="false" />
	<relative enable="true" />
	<scaled enable="true" />
	<sorted enable="false" />
	<animlodbias value="0" />
	<emittertype value="Sphere" />
	<emittersize value="0 0 0" />
	<direction min="-1 -1 -1" max="1 1 1" />
	<constantforce value="0 -20 0" />
	<dampingforce value="0" />
	<activetime value="3" />
	<inactivetime value="0" />
	<emissionrate min="2000" max="2000" />
	<particlesize min="0.03 0.3" max="0.06 1" />
	<timetolive min="1" max="1" />
	<velocity min="8" max="10" />
	<rotation min="0" max="0" />
	<rotationspeed min="0" max="0" />
	<sizedelta add="0" mul="0.01" />
	<faceCameraMode value="Direction" />
	<colorfade color="1 1 1 1" time="0" />
	<colorfade color="0.5 0.75 1 1" time="0.5" />
	<colorfade color="0 0 0 0" time="1" />
</particleeffect>

Particle.xml
<material>
    <technique name="Techniques/DiffUnlitParticleAdd.xml" />
    <texture unit="diffuse" name="Textures/Flare.dds" />
</material>
```

-------------------------

Nerrik | 2022-09-09 06:48:23 UTC | #4

Urho3d particles are some simple / standard, you can use the particle editor in the Urho3d level editor and try to make some liquid - style particles.

But if you want "real liquid style particles" you need some kind of fake physics and have to extend the particleemitter for yourself.

The particlemitter ("source/urho3d/graphics/ParticleEmitter") is easy to understand and to extend.

In my project i've written a small "multithreaded node emitter" for myself. It can spawn nodes with nearly any in it and can use pointcloud Models (vtk / csv) for the startframe / positioning of the nodes.

atm it has 3 emitter types 

- a normal emitter like urho3d

- real physics emitter with rigidbodys and collisionshapes for smaller effects like falling stones

- and a fake physics emitter for larger effects that makes one multithreaded physical single Raycast for each node in the node direction before the creation to search the first contact point. If it reaches it becomes an predefined random change of the direction and the speed.

sounds a bit time consuming but the programming takes me one day.

Here a small video from some particleeffects of my game

[video](https://picmento.de/wyrdan/Wyrdanparticle.m4v)

(its a stronger than normal and invul char in the video)

for the meteor effect iam using ~80 nodes filled with normal urho3d particleemitters (small effects ;)), with the start-positioning from an vtk pointcloud spheremodel and the fake physics.

for the raining arrows just a staticmodel with normal emitting.

the flamethrower mage uses the standard urho3d particlesystem.

-------------------------

Jens | 2022-09-14 08:38:38 UTC | #5

Ok, that video has some pretty cool effects. I should've pointed out that mine is just for Android so I'm limited to the out of the box emitter. It works pretty well using burst and smoke, so I'II likely stick with that.

-------------------------

