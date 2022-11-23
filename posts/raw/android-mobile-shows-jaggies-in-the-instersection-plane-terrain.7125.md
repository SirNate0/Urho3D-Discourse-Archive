feresmu | 2022-01-11 11:59:19 UTC | #1

Hi
For performance issues, I tried to change the water material (Materials/Water.xml) with Materials/Red.xml
```
<material>
    <technique name="Techniques/NoTexture.xml" />
    <parameter name="MatDiffColor" value="1 0 0 0.25" />
    <parameter name="MatSpecColor" value="1 1 1 16" />
</material>
```
in the water example (without reflexion camera).
It works fine in desktop and android table.
![Captura|374x500](upload://uahQ3shDShUmeeHmINRYih0RlI5.png)
But in android mobile it shows jaggies in the instersection with the terrain.
![IMG-4766|375x500](upload://4AIKKpt7muhRBkZazoenPNMrGB1.jpeg)
I tried a lot of things like change material with SetDepthBias or SetRenderOrder but nothing works.
The terrain is the same of the water example.
Any ideas?

-------------------------

Eugene | 2022-01-11 12:01:10 UTC | #2

What's your camera range, znear/zfar? I assume you don't use orthographic cameras.

-------------------------

feresmu | 2022-01-11 18:10:48 UTC | #3

Hi.
I don’t use orthographic cameras.
Because the camera can be far away of the terrain I create it with:
Camera* camera = cameraNode_->CreateComponent<Camera>();
camera->SetFarClip( 11750.0f );

Then
nearClip_ = 0.100000001
farClip_ = 11750.0000

if I do
Camera* camera = cameraNode_->CreateComponent<Camera>();
only (without camera->SetFarClip( 11750.0f );)
nothing happens ( it shows jaggies )

-------------------------

Eugene | 2022-01-11 18:15:02 UTC | #4

[quote="feresmu, post:3, topic:7125"]
nearClip_ = 0.100000001
farClip_ = 11750.0000
[/quote]
Yep, what I thought.
You probably have only 16 bits of depth on mobiles.

Just to give you an idea of how little it is... You literally have no intermediate depths between 
z=2562, z=4207, and z=11750, these are 65533th, 65534th and 65535th depth layers. There will be no deterministic depth order between an object on z=4k and another object on z=5k.

[quote="feresmu, post:3, topic:7125"]
nothing happens ( it shows jaggies )
[/quote]
Default values are still too much. Try near=1 and far=100?

-------------------------

feresmu | 2022-01-12 07:36:41 UTC | #5

Hi.
It seems that camera->SetNearClip( 1 ); do the trick
even with camera->SetFarClip( 3000.0f );

Well, with camera->SetFarClip( 3000.0f ); I show jaggies but are smaller.
But with camera->SetNearClip( 100 ); and camera->SetFarClip( 700 ); I show perfect, like desktop.
So playing with that and the camera distance and limit camera zoom out, I got it.

Thanks a lot!!

-------------------------

