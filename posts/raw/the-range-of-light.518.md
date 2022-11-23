shu | 2017-01-02 01:01:02 UTC | #1

Hi, 

I have a short question: I have a very simple 'space' scene where I load some low-poly asteroids. I have one directional light, but everything that's farther away than 1000 units is not lit and stays dark.
I've looked in the documentation, but I can't find the reason. I did set higher values for draw distance and range in the light, but that didn't help. I haven't set LightMasks and do not use zones yet.

The code for the light:
[code]
  Node* lightNode = scene->CreateChild( "DirectionalLight" );
  lightNode->SetDirection( Vector3( 0.0f, -1.0f, 0.2f ) );
  Light* light = lightNode->CreateComponent<Light>();
  light->SetLightType( LIGHT_DIRECTIONAL );
  light->SetFadeDistance( 50000.f );
  light->SetDrawDistance( 50000.f );
  light->SetRange( 50000.f );
[/code]

What could be the reason? 
Thanks!

-------------------------

JTippetts | 2017-01-02 01:01:02 UTC | #2

Are you sure those faraway asteroids are being drawn at all? Have you altered Camera's far clip distance? The default value for far clip is 1000.0f, so anything further than that will not be drawn at all unless you call Camera::SetFarClip() with a larger value.

-------------------------

shu | 2017-01-02 01:01:03 UTC | #3

Hi, yes, I did set the the farClip of the cam to 10.000 and I see the silhouettes (the outline) of the asteroids, so they are drawn. They're just black.

e: Like this.
[img]http://i.imgur.com/TWdATrh.png[/img]

The asteroid/potato in the middle is 580 units away, the black outlines in the background are asteroids with a distance greater than 1000 units. 
I also did set the size of the octtree to a BoundingBox( -50000.f, 50000.f ).

-------------------------

reattiva | 2017-01-02 01:01:03 UTC | #4

[quote="shu"]do not use zones yet[/quote]

Try adding a zone, set its boundingBox, fogStart and fogEnd.

-------------------------

shu | 2017-01-02 01:01:03 UTC | #5

Thanks reattiva! That fixed it. :slight_smile:

-------------------------

