Conqueror | 2017-03-19 19:24:09 UTC | #1

Hi
 
I’m new with Urho3d and I’m making test on a 2D game.
 
For the test I use the 36_Urho2DTileMap example.
I changed the tileset but I can see the neighboring border tile.
 
Screenshoot :
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/138e9233791ea5a4452c098d5e35236d12e95b64.png'>
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/f030a7cd1a940da8e49b6bf136602f273d1a28c8.png'>
 
TMX file : [http://pastebin.com/7BBhfMKK](http://pastebin.com/7BBhfMKK)
 
Test tiletest : http://opengameart.org/sites/default/files/snow-expansion.png
 
 
How I can solve it ?

-------------------------

Modanung | 2017-03-19 20:04:04 UTC | #2

From the [documentation on Urho2D](https://urho3d.github.io/documentation/HEAD/_urho2_d.html):
[quote]
if 'seams' between tiles are obvious then you should make your tilesets images nearest filtered (see [Static sprites](https://urho3d.github.io/documentation/HEAD/_urho2_d.html#Urho2D_Static_Sprites) section above.)
[/quote]

You need to create an XML file in the same folder as the texture, with the same name (but ending in xml) containing:
```
<texture>
    <filter mode="nearest" />
</texture>
```

-------------------------

Modanung | 2017-03-19 20:00:07 UTC | #3

..and welcome to the forums! :)

-------------------------

