aster2013 | 2017-01-02 00:58:43 UTC | #1

[img]https://dl.dropboxusercontent.com/u/56770481/Urho3DShadow.jpg[/img]

-------------------------

cadaver | 2017-01-02 00:58:43 UTC | #2

That's because the scene has only a strong directional light with shadows, and ambient light (uniform in each direction)

You could avoid the flatness by eg. creating another directional light in the scene, which doesn't cast shadows and is weaker in brightness, but affects objects everywhere in the scene. That'll be another render pass so it's going to slow down rendering a bit.

-------------------------

aster2013 | 2017-01-02 00:58:43 UTC | #3

If object in shadow, we can reduce the diffuse color intensity, but don't make it to zero, will look more reality.

-------------------------

cadaver | 2017-01-02 00:58:43 UTC | #4

That's possible too. It's the shadowIntensity property in Light which tells how dark shadows are. By default it's 0 (fully dark) but you could try increasing it to something like 0.1 or 0.2.

-------------------------

boberfly | 2017-01-02 00:58:43 UTC | #5

Probably because the character is a solid colour doesn't help either... :wink:

For ambient/indirect lighting you probably will need to do things like use arrays of cube maps for different zones or whatever that has indirect lights baked into it, or use spherical harmonics to get indirect diffuse which you can inject into the vertex shader (perhaps store the values in a zone and inject into a shader, it will probably break instancing though). Then multiply it with a cavity map or baked ambient occlusion or some post-process AO effect. It's one of those things where many kinds of games have their own way of doing ambient lighting with advantages and trade-offs for each kind of technique. UnrealEngine4 is using light propagation volumes as far as I know to keep things dynamic with indirect lights for instance and would work with instancing, and same for Crysis and other modern engines. Then it's getting reflections to work that are not just flat surfaces like water which is the new one to solve (screen-space local reflections + cubemap fallbacks seem to be the trend now, and voxel cone tracing is still not ready for mainstream yet). Or there might be hybrid raytracing approaches which might be the trend.

Cheers

-------------------------

friesencr | 2017-01-02 00:58:44 UTC | #6

I just bake my ao in the color map :O and enjoy me some mid 2000s quality graphics with a ton more vertices \m/  It seems like my gtx 780 can handle 100 million verts of static models without a drop.  My macbook air can't run a scene with lights and stay above 60fps.  Which is another reason i bake my ao into col.  Running a game on those stupid intel cards is workout.  I would love to try spherical harmonics.  I looked at the math and said, and you can quote me, 'nope'.  Which is why I am stuck in math hell forever.  Math is a tool of the man to keep mediocre people down!  Like everything though you just play it out like Rocky.  You have to wear down your opponent with your face then after they get tired in the 15th round you give em the ole uppercut.

-------------------------

