vivienneanthony | 2017-01-02 01:06:50 UTC | #1

Hello,

I'm trying to sort something out. Maybe someone can explain why something looks okay in the preview box but in the actual  scene the specularity is wrong? The UV map was done correctly etc.

I can't match the light to show  the texture in the editor. I've been playing around with the code the last hour trying to figure out whats wrong. I can't. Everything seems to be set right right.

[imgur.com/a/mbFZp](http://imgur.com/a/mbFZp)

[code]
<?xml version="1.0"?>
<material>
	<technique name="Techniques/DiffSpec.xml" quality="1" loddistance="0" />
	<texture unit="diffuse" name="Textures/IvoryPlainTexture.png" />
	<texture unit="specular" name="Textures/SpecularNoise2.png" />
	<parameter name="UOffset" value="1 0 0 0" />
	<parameter name="VOffset" value="0 1 0 0" />
	<parameter name="MatDiffColor" value="0.8 0.8 0.8 1" />
	<parameter name="MatEmissiveColor" value="0 0 0" />
	<parameter name="MatEnvMapColor" value="1 1 1" />
	<parameter name="MatSpecColor" value="0.9 0.9 0.9 80" />
	<cull value="none" />
	<shadowcull value="none" />
	<depthbias constant="0.0002" slopescaled="0.5" />
</material>[/code]

Vivienne

-------------------------

vivienneanthony | 2017-01-02 01:06:50 UTC | #2

I think I got some better results. I am just not sure how to element the line area near the wall tops.  There is a external light source outside the hanger/room with light source cast shadow, wall set to cast shadows, but somehow it's still being calculated meaning the light source. Creating the top line on the walls.

-------------------------

codingmonkey | 2017-01-02 01:06:50 UTC | #3

I suppose that you got falling shadow from roof to walls. 
I guessing because you room composed with separated models try to join it into one solid model and place global light in room not outside.

Actually for indoor scenes like room or angars you better build level in blender or other 3d editor and bake lighmap. 
see dima's example: [youtube.com/watch?v=qAl2m483RF0](https://www.youtube.com/watch?v=qAl2m483RF0)
then place in it local light in room if needed or better use something like faked lights

-------------------------

vivienneanthony | 2017-01-02 01:06:52 UTC | #4

[quote="codingmonkey"]I suppose that you got falling shadow from roof to walls. 
I guessing because you room composed with separated models try to join it into one solid model and place global light in room not outside.

Actually for indoor scenes like room or angars you better build level in blender or other 3d editor and bake lighmap. 
see dima's example: [youtube.com/watch?v=qAl2m483RF0](https://www.youtube.com/watch?v=qAl2m483RF0)
then place in it local light in room if needed or better use something like faked lights[/quote]


Hmmm. I would love to do the latter but considering the rooms will be completely customizable including light sources. I might have to layout out the room then combine the messhes.

-------------------------

