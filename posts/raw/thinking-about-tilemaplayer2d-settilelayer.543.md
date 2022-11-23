LouisCyphre | 2017-01-02 01:01:16 UTC | #1

Hi everybody,

First of all [b]thanks a lot [/b] for this very nice library and it's very nice and readable sourcecode..

I am basically trying to use the TileMap functionality and I am loading a .tmx file.

I was just wondering, if the tilemap data is static, shouldnt we simply "render" the tilemap to texture, then create one quad with this texture... Creating an Array of StaticSprite2D seems like a bit of overkill to me, if the data does not change, and the whole texture fits in (Texture) Memory? .. lets say 256 x 256 tiles, tilesize 32x32 Pixels --> 8192x8192 Texture? 

does this make sense?

I am no expert, but that 8192x8192 texture shouldn't be too large according to [url]http://udn.epicgames.com/Three/TextureSupportAndSettings.html#Compressed%20Texture%20Memory%20Requirements[/url]  ?

Sorry If I am missing out on something...

-------------------------

friesencr | 2017-01-02 01:01:16 UTC | #2

The tilemap does use the proxy cache to batch draws.  The sample only produces 4 draw calls.

-------------------------

cadaver | 2017-01-02 01:01:17 UTC | #3

You will run into hardware limits with big textures, particularly on mobile (I wouldn't risk anything greater than 2048x2048). Also you'd be wasting GPU memory whenever a tile is repeated. So for large worlds, drawing tiles as sprites and batching them makes more sense.

-------------------------

LouisCyphre | 2017-01-02 01:01:17 UTC | #4

Thanks for your Infos, will check that out !

-------------------------

