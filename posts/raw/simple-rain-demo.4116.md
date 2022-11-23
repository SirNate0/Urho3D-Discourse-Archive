Dave82 | 2018-03-22 18:51:17 UTC | #1

Playing with particles.The demo uses two emitters 1. Rain is a simple emitter with long particles + big velocity,
2 . Splash. The splash is achived by expanding the ParticleEmitter and ParticleEffect with a new emittertype called "EMITTER_MESH".It takes a mesh as a shape and generates random points inside it's triangles.The direction of the particle is calculated from the triangle's normal.Since it uses a very cheap solution it can generate extremely big amount of particles (almost no frame drop).The only drawbacks are : On bigger triangles there will be less particles than on a smaller set of triangles.(ground plane VS sphere cap in the video) however it can be easily solved.

https://youtu.be/zqZzB8YXfq8

-------------------------

coldev | 2018-03-31 03:58:00 UTC | #2

source download please   :grin:  thanks

-------------------------

Dave82 | 2018-03-31 22:56:43 UTC | #3

Well the rain itself is pretty easy : 
[code]
<particleeffect>
	<material name="Materials/rain.xml" />
	<numparticles value="4000" />
	<updateinvisible enable="true" />
	<relative enable="true" />
	<scaled enable="true" />
	<animlodbias value="0" />
	<emittertype value="Sphere" />
	<emittersize value="200 1 200" />
	<direction min="-0.04 -1 -0.04" max="0.04 -1 0.04" />
	<dampingforce value="0" />
	<activetime value="0" />
	<inactivetime value="0" />
	<emissionrate min="2000" max="2500" />
	<particlesize min="0.15 25" max="0.25 35" />
	<timetolive min="0.5" max="0.6" />
	<velocity min="700" max="800" />
	<constantforce value="0 -46 0" />
	<color value="0.08 0.085 0.09 0.1" />
</particleeffect>
[/code]
Set your emitter face camera mode to rotate only bi y (emitter->SetFaceCameraMode(FC_ROTATE_Y)

Material  : 

[code]
<material>
    <technique name="Techniques/DiffVColAdd.xml" />
    <texture unit="diffuse" name="Textures/rain.bmp" />
</material> 
[/code]

Rain rexture (rain.bmp): 

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/5/52402b24557f434cdcd43b6ff2742a9f390c85cf.png'>

Unfortunately the raindrop effect requires massive rework of the existing ParticleEmitter and ParticleEffect classes that in this particular state (which i use) wouldn't be accepted PR.(scale frames , random texture frames, etc ) Instead i'm thinking of adding a general purpose template based interpolator (like in SPARK) which can be used to manipulate the parameters of the particles.Would be more convenient to use and easy to expand in the future . 
Also you have to modify the EmitNewParticle() function to
[code]
bool EmitNewParticle(const unsigned char* &vertexData, unsigned vertexSize, unsigned vertexCount , const unsigned char* &indexData, unsigned indexSize);
[/code]

to avoid mesh vertex buffer lock each time a new particle is emitted.I don't know is there any better workaround for this but this is how i use it right now.

-------------------------

