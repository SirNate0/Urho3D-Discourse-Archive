szamq | 2018-11-01 08:56:20 UTC | #1

I'm trying to implement matcap shader from this reference [clicktorelease.com/blog/crea ... ing-shader](http://www.clicktorelease.com/blog/creating-spherical-environment-mapping-shader)
I copied and modified litSolid shader and changed the cubemap, so it map to the sphere on emissive texture( because env unit is cube). Here is modification of fragment shader:
[code]  
#ifdef ENVCUBEMAP
    vec3 r =reflect(vReflectionVec, normal);
    float m = 2. * sqrt( pow( r.x, 2. ) + pow( r.y, 2. ) + pow( r.z + 1., 2. ) );
    vec2 vN = r.xy / m + .5;
    finalColor += cMatEnvMapColor * texture2D( sEmissiveMap, vN ).rgb;
#endif
[/code]
I got some nice results but it isn't still what it should be - the matcap's reflections are distorted. I suppose this is this because 
[code]
vReflectionVec =  worldPos-cCameraPos;
[/code]
isn't equivalent to
[code]
e = normalize( vec3( modelViewMatrix * vec4( position, 1.0 ) ) );
[/code]
in Urho's shader defines I can see cViewProj and cModel matrixes, but how can I get modelViewMatrix?

-------------------------

szamq | 2017-01-02 00:59:18 UTC | #2

Ok, it's working, I forgot to normalize from eye vector  :blush: 
[spoiler][img]http://i.imgur.com/BrLVd0u.jpg[/img][/spoiler]

-------------------------

vivienneanthony | 2017-01-02 00:59:19 UTC | #3

[quote="szamq"]Ok, it's working, I forgot to normalize from eye vector  :blush: 
[spoiler][img]http://i.imgur.com/BrLVd0u.jpg[/img][/spoiler][/quote]

Very nice.

-------------------------

Mike | 2017-01-02 00:59:19 UTC | #4

Well done  :slight_smile: 
Do you plan to disclose full code or send a pull request?
I think we need more shaders.

-------------------------

szamq | 2017-01-02 00:59:19 UTC | #5

I'm not sure how to integrate this. Because the environment sphere can't be set to env texture unit because it is cubemap, so I used emissive texture for that.
Just modify  ENVCUBEMAP defines in LitSolid shader like below and set your matcap texture [google.pl/search?q=matcap](https://www.google.pl/search?q=matcap)  to emmisive texture unit. Then you can use DiffEnvCube.xml technique in editor to see the effect.

Here are modifications. 
vertex shader
[code]
#ifdef ENVCUBEMAP
vReflectionVec =  normalize(worldPos-cCameraPos);
#endif[/code]
fragment shader
[code]
      #ifdef ENVCUBEMAP
            vec3 r =reflect(vReflectionVec, normal);
            float m = 2. * sqrt( pow( r.x, 2. ) + pow( r.y, 2. ) + pow( r.z + 1., 2. ) );
            vec2 vN = r.xy / m + .5;
            finalColor += cMatEnvMapColor * texture2D( sEmissiveMap, vN ).rgb;
        #endif
[/code]

-------------------------

Mike | 2017-01-02 00:59:19 UTC | #6

Thanks a lot, will try this today.  :wink:

-------------------------

friesencr | 2017-01-02 00:59:20 UTC | #7

Yeah it works alright.  Thanks for sharing szamq.  I spent a few hours trying to figure out to get this into its own technique.  The exercise was just what I needed to starting to understanding how the render passes work.  I think I can package it up so its easier to use.    It will take me quite a while longer to get all of the useful permutations figured out.

[spoiler][img]http://i.imgur.com/rgkz9u2.png[/img][/spoiler]

That is a glossy green ninja alright...

-------------------------

