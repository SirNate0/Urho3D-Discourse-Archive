sovereign313 | 2017-01-02 01:09:39 UTC | #1

Hi,

So, I created a map with tiled, and generated a tmx file.  I can load that wonderfully (although any objects on it don't load well ie: houses).  I can load an animated sprite, wonderfully.... just as long as I don't load the tmx.

I've tried loading the TMX first, and then the animated sprite, and vice versa.  I've also tried attaching the animated sprite to the same node as the tilemap.  I've looked for a way to attach the sprite to the tilemap, but there is no createChild or createComponent of TileMap2D.  Does anyone know how to go about getting the sprite to show up ON TOP of the tmx map?


[ EDIT ]
spriterAnimatedSprite->SetLayer(10); // Layer above tmx

-------------------------

