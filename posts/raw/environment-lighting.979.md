vivienneanthony | 2017-01-02 01:04:35 UTC | #1

Has anyone setup environment lighting from a skybox? 

The reason I asked  because I want to delete the added lights to a generated scene and use the skybox. It will allow me to add more lights without conflicting lighting. I'm not sure how I want to override generated lights.

-------------------------

gabdab | 2017-01-02 01:06:40 UTC | #2

Did you solve it ?

-------------------------

codingmonkey | 2017-01-02 01:06:40 UTC | #3

>Has anyone setup environment lighting from a skybox? 
I'm do not trying this but I guess that you can put skybox texture into envMap TU-slot and do some fixes in LitSolid shader
look where in shader doing lookup cubemap and make similar fetch from your envmap and add/multiple this value to LightColor.
but I suppose this method of lighting is little strange )

-------------------------

