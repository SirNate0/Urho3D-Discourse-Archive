sabotage3d | 2017-01-02 01:15:20 UTC | #1

Hi,
Is there an example on how play Spritesheet animation in Urho3D? In the 2D examples I could find only scml files using sequence of png's.

-------------------------

1vanK | 2017-01-02 01:15:20 UTC | #2

Animated sprite in UI:

[discourse.urho3d.io/t/animated-sprite-2d-and-loading-screen/2019/2](http://discourse.urho3d.io/t/animated-sprite-2d-and-loading-screen/2019/2)

-------------------------

sabotage3d | 2017-01-02 01:15:21 UTC | #3

Do I need to generate xml in addition to the spritesheet?

-------------------------

1vanK | 2017-01-02 01:15:21 UTC | #4

no

-------------------------

sabotage3d | 2017-01-02 01:15:21 UTC | #5

I am trying to get it work with SpriteSheet2D. I am trying the code below where I generated the sp.xml using the SpritePacker tool. But I can't get it to play the animation.

[code]Sprite2D* sprite = cache->GetResource<Sprite2D>("Particles/sp.png");
SpriteSheet2D* spritesheet = cache->GetResource<SpriteSheet2D>("Particles/sp.xml");

sprite->SetSpriteSheet(spritesheet);

particleEmitter_->SetSprite(sprite);
particleEmitter_->SetAnimationEnabled(true);[/code]

-------------------------

sabotage3d | 2017-01-02 01:15:22 UTC | #6

I got it partially working with your example using Sprite. Compared to using xml and SpriteSheet2D it is quite tedious.

-------------------------

ghidra | 2017-01-02 01:15:23 UTC | #7

Just spent some times cleaning up an example I had laying around for animating sprites on a plane.
I imagine that it could be used to animated particles spites too... haven't tried taking it that far yet.
As well, this example is far from perfect. And is missing a few features, like alpha. And there is some incorrect math for the uv shifting, that is causing a jitter, that I hadn't noticed till now.

--------------------------------------

All code  and images can also be found here:
[url]https://github.com/ghidra/urho_research/commit/b3b424fdd775a02c30ae54aa7d9f9aa1238c410f[/url]
example sheet here:
[url]https://developer.valvesoftware.com/w/thumb.php?f=Vista_smoke_alpha.jpg&w=800[/url]

--------------------------------------

[b]The Material[/b] AnimatedSprite.xml has these paramaters:

[code]
 <parameter name="Sheet" value="6.0 6.0" />
 <parameter name="Rate" value="16.0" />
[/code]

The "Sheet" paramater is the number of slices horizontally, and vertically.
In the shader, we are using uv space, to scale and translate the verticies uvs into place on the sprite sheet.
Currently, the shaders also assumes that the spritesheet is one animation only. The posted images, has 2 animations on it. Which is another imperfection.

The "Rate" paramater, allows some control over the playback speed.

--------------------------------------

[b]The Technique[/b] AnimatedSprite.xml is very vanilla.
I changed the blend mode, to test alpha, but it didnt do what I expected. So its mute for now.

--------------------------------------

[b]The Shader[/b] AnimatedSprite.glsl is where the work is done.

specifically this part in the VS part:

[code]
float frames = cSheet.x*cSheet.y;
float frame = mod(floor(cElapsedTime*cRate),frames);
float xoff = mod(frame,cSheet.x)*(1/cSheet.x);
float yoff = floor(frame/cSheet.y)*(1/cSheet.y);

vTexCoord = GetTexCoord(iTexCoord)*(1.0/cSheet)+vec2(xoff,yoff);
[/code]

This is the part that moves the uvs around. It's also missing another offset to fix the jitter.

--------------------------------------

Just as a proof of concept, its very basic. A few features could be added in. Some clean up. etc.
[url=https://developer.valvesoftware.com/w/thumb.php?f=Vista_smoke_alpha.jpg&w=800][img]https://developer.valvesoftware.com/w/thumb.php?f=Vista_smoke_alpha.jpg&w=800[/img][/url]
[url=http://imgur.com/cGZ5GMB][img]http://i.imgur.com/cGZ5GMB.gif[/img][/url]

-------------------------

sabotage3d | 2017-01-02 01:15:23 UTC | #8

Thanks ghidra. This is quite cool. It is big pain to align spritesheets perfectly most of the time they are packed with specific coords for each bucket which are written into seperate file.
The main problem I am hitting with this technique is non squared sprite-sheets. If you repack them into square you will get gaps where you will need again the seperate file with the mappings.

-------------------------

sabotage3d | 2017-01-02 01:15:26 UTC | #9

If anyone has the same problem I made a small helper class: [url]http://discourse.urho3d.io/t/spritesheet-reader/2445/1[/url]

-------------------------

