throwawayerino | 2021-08-12 14:54:49 UTC | #1

I want to collect the normals of a model, write them to a surface, and read from it later down. Is it possible to do so all within the renderpath and techniques?

Snippet of my renderpath:
```
<rendertarget name="earlyzmap" sizedivisor="1 1" format="rgba" /> <!-- Create texture -->
<command type="clear" color="1 0.65 0 1" output="earlyzmap" />
...
<command type="scenepass" pass="earlyz"  >
	<output unit="0" name="earlyzmap" />
</command>
<command type="scenepass" pass="outline" >
	<texture unit="specular" name="earlyzmap" />
</command>
...
```
And the technique that I'm working on has this
```
<pass name="earlyz" vs="EarlyZ" ps="EarlyZ" />
```
Renderdoc (which is awesome) shows that the rendertarget does get created and cleared to orange but I can't seem to be able to modify it with the `earlyz` pass. The problem could be with my shaders, but I want to check if my renderpath setup is correct.

-------------------------

throwawayerino | 2021-08-14 14:38:48 UTC | #2

Guys I'm stupid. Everything above is correct but I had to fix depth testing. I added `depthtest="always"` to the technique
Now I can't seem to read the map from the 'outline' pass
EDIT 2: I also figured that out. I had a typo in the technique pass name.

-------------------------

