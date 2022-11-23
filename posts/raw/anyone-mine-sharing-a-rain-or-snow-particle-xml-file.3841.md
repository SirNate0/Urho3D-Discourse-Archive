GodMan | 2017-12-13 00:00:59 UTC | #1

I need one for outdoor weather effect and I'm sure someones made one already so I thought it would be counter intuitive to try and make another myself.


Thanks

-------------------------

SirNate0 | 2017-12-13 02:40:38 UTC | #2

You can try these (I wouldn't call them great, but if you just want passable they probably meet that standard):

Snow.xml
```xml
<particleeffect>
	<material name="Materials/Particle.xml" />
	<numparticles value="1000" />
	<updateinvisible enable="false" />
	<relative enable="true" />
	<scaled enable="true" />
	<sorted enable="false" />
	<fixedscreensize enable="false" />
	<animlodbias value="0" />
	<emittertype value="Sphere" />
	<emittersize value="30 0 30" />
	<direction min="0.1 -1 0.1" max="0.1 0 0.1" />
	<constantforce value="0 -1 0" />
	<dampingforce value="1" />
	<activetime value="0" />
	<inactivetime value="0" />
	<emissionrate min="20" max="50" />
	<!--light snow: min 10 max 25; decent snow: emissionrate min="20" max="35" /-->
	<particlesize min="0.1 0.1" max="0.1 0.1" />
	<timetolive min="10" max="10" />
	<velocity min="1" max="1" />
	<rotation min="0" max="0" />
	<rotationspeed min="0" max="0" />
	<sizedelta add="0" mul="1" />
	<faceCameraMode value="Rotate XYZ" />
	<color value="1 1 1 1" />
</particleeffect>
```
Rain.xml
```xml
<particleeffect>
	<material name="Materials/Particle.xml" />
	<numparticles value="1000" />
	<updateinvisible enable="false" />
	<relative enable="true" />
	<scaled enable="true" />
	<sorted enable="false" />
	<fixedscreensize enable="false" />
	<animlodbias value="0" />
	<emittertype value="Box" />
	<emittersize value="30 0 30" />
	<direction min="0.02 -1 0.02" max="0.02 0 0.02" />
	<constantforce value="0 -10 0" />
	<dampingforce value="1" />
	<activetime value="0" />
	<inactivetime value="0" />
<!--	<emissionrate min="25" max="10" /> -->
	<emissionrate min="50" max="200" />
	<particlesize min="0.02 0.05" max="0.04 0.1" />
	<timetolive min="5" max="5" />
	<velocity min="1" max="1" />
	<rotation min="0" max="0" />
	<rotationspeed min="0" max="0" />
	<sizedelta add="0" mul="1" />
	<faceCameraMode value="Rotate XYZ" />
	<color value="0.5 0.7 1 1" />
</particleeffect>
```
HeavyRain.xml
```xml
<particleeffect>
	<material name="Materials/Particle.xml" />
	<numparticles value="1000" />
	<updateinvisible enable="false" />
	<relative enable="true" />
	<scaled enable="true" />
	<sorted enable="false" />
	<fixedscreensize enable="false" />
	<animlodbias value="0" />
	<emittertype value="Box" />
	<emittersize value="30 0 30" />
	<direction min="0.02 -1 0.02" max="0.02 -0.4 0.2" />
	<constantforce value="0 -15 0" />
	<dampingforce value="1" />
	<activetime value="0" />
	<inactivetime value="0" />
	<emissionrate min="100" max="200" />
	<particlesize min="0.02 0.15" max="0.04 0.5" />
	<timetolive min="5" max="5" />
	<velocity min="1" max="1" />
	<rotation min="0" max="0" />
	<rotationspeed min="0" max="0" />
	<sizedelta add="0" mul="1" />
	<faceCameraMode value="Rotate Y" />
	<color value="0.4 0.6 0.8 1" />
</particleeffect>
```

-------------------------

GodMan | 2017-12-13 15:58:30 UTC | #3

Thanks at least this provides me basic ground work.

-------------------------

jmiller | 2018-08-21 02:53:50 UTC | #4

A rain particle effect (with 'wind') using a DDS texture, maybe best used as camera attachment.

texture sample - **tiled**

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/1/1a7ec79adf25e752b39257ea44ab73e453d754ed.png[/img][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/1/1a7ec79adf25e752b39257ea44ab73e453d754ed.png[/img]

particleeffect, with slight random 'wind' **direction**
```
<particleeffect>
  <material name="Materials/rain.xml" />
  <numparticles value="4000" />
  <updateinvisible enable="false" />
  <relative enable="false" />
  <scaled enable="false" />
  <sorted enable="false" />
  <animlodbias value="0" />
  <emittertype value="Box" />
  <emittersize value="50 0 50" />
  <direction min="-0.01 -1 -0.01" max="0.01 -1 0.01" />
  <constantforce value="0 0 0" />
  <dampingforce value="0" />
  <activetime value="0" />
  <inactivetime value="0" />
  <emissionrate min="4000" max="4000" />
  <particlesize min="0.25 1" max="0.25 1" />
  <timetolive min="1" max="1" />
  <velocity min="32" max="32" />
  <rotation min="0" max="0" />
  <rotationspeed min="0" max="0" />
  <faceCameraMode value="Direction" />
</particleeffect>
```
material
```
<material>
  <technique name="Techniques/DiffAddAlpha.xml" />
  <texture unit="diffuse" name="Textures/rain.dds" />
</material>
```
DDS texture:
  https://www.dropbox.com/s/x1vwhup4994dnvl/rain.dds?dl=0
Texture source file (GIMP XCF with layer mask)
  https://www.dropbox.com/s/g1ydotz42tascfd/rain.xcf?dl=0

-------------------------

Dave82 | 2018-04-08 08:15:46 UTC | #5

Try this : 
https://discourse.urho3d.io/t/simple-rain-demo/4116

-------------------------

GodMan | 2018-08-21 01:21:12 UTC | #6

Thanks guys looks great.

-------------------------

