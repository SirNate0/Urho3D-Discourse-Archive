vivienneanthony | 2017-01-02 01:03:46 UTC | #1

(Note: I posted this on some other sites but no reply but posting it here and I'll give credit to everyone that help. I posted the latest version on GitHub.)

Hello,

Is there anyone concept artist or graphics artist who can do texturizing and models? I am trying to put a team together. I am working on a game project. Open source and I need help building. It's at the point of conceptual design and mechanics implementation. I have some of the model assets made already. My current pipeline of applications are Blender, Urho3D, Makehuman, SnappyTree.com and a few other applications.

The initial goal is a exploration game for standalone immediately and online in the future. I am working on the client aspect. There is some Star Trek character models but majority of it is up to creative direction. I'm thinking on the scale of Eve Online/Mass Effect in a procedural environment. The overall concept is like [youtube.com/watch?v=ZVl1Hmth3HE](https://www.youtube.com/watch?v=ZVl1Hmth3HE) specifically ground map as first.

Youtube Playlist
[youtube.com/watch?v=m48OTA5 ... 7&index=30](https://www.youtube.com/watch?v=m48OTA5qtRM&list=PLg3Q9upEQvPRAYaIqhImkUu1RBgSZA_N7&index=30)

Note: It's been updated even more.

Github
[github.com/vivienneanthony/Exis ... evelopment](https://github.com/vivienneanthony/Existence/tree/development)

Video Log
[topic241.html](http://discourse.urho3d.io/t/existence-video-log/255/1)

Assets and other information
[cgprojectsfx.wordpress.com](http://cgprojectsfx.wordpress.com)

Talk soon. My email is [cgprojectsfx@gmail.com](mailto:cgprojectsfx@gmail.com). Any other contribution or help is appreciated.

-------------------------

practicing01 | 2017-01-02 01:03:46 UTC | #2

A list of models you need would be helpful.  Along with a link to an image of what you'd like each of those models to look like.  This way people with spare time can pick them off little by little.

-------------------------

vivienneanthony | 2017-01-02 01:03:47 UTC | #3

[quote="practicing01"]A list of models you need would be helpful.  Along with a link to an image of what you'd like each of those models to look like.  This way people with spare time can pick them off little by little.[/quote]


Okay. I posted a picture of terrain assets at [imgur.com/a/6iNGh](http://imgur.com/a/6iNGh) 

The assets are named by planet type like desert, terrain, and ice then subtype like alien and terrain. So, I can have a alien blend file with assets per subtype planet type.  The file naming convention is the same or smiliar.

What i dont have is more variety in desert planet type for both terrain or alien, and variety of terrain plants and rock assets.

So, I one or two cactus and grass for terrain earth like and cactus like alien, then a few plants. That I can find some quick pictures.

I found some [imgur.com/a/2gjLM](http://imgur.com/a/2gjLM)

A few of the cactus plant can be alien or changed to be more alien like.

-------------------------

practicing01 | 2017-01-02 01:03:48 UTC | #4

I started out trying to make a cactus but I'm too noob to figure out how to do spikes. [dropbox.com/s/ta9nayi0tgbfq ... us.7z?dl=0](https://www.dropbox.com/s/ta9nayi0tgbfq4j/alienCactus.7z?dl=0)

[spoiler][img]http://img.ctrlv.in/img/15/02/28/54f1e3489de82.png[/img][/spoiler]

-------------------------

vivienneanthony | 2017-01-02 01:03:49 UTC | #5

[quote="practicing01"]I started out trying to make a cactus but I'm too noob to figure out how to do spikes. [dropbox.com/s/ta9nayi0tgbfq ... us.7z?dl=0](https://www.dropbox.com/s/ta9nayi0tgbfq4j/alienCactus.7z?dl=0)

[spoiler][img]http://img.ctrlv.in/img/15/02/28/54f1e3489de82.png[/img][/spoiler][/quote]

Which program do you use? If its Blender I can do a quick how to when I'm home.

-------------------------

vivienneanthony | 2017-01-02 01:03:50 UTC | #6

Heres another quick dirty method I would do a cactus. I was rushing out the door.

If I had time I would make the circle 16 or 8 vertiices modeling at a low count and all quads.

 [m.youtube.com/?#/watch?v=9ZPwrSsuVwA](https://m.youtube.com/?#/watch?v=9ZPwrSsuVwA)

Hope the link worked. The one you did practicing I we would use for a desert based plant cactus.

-------------------------

vivienneanthony | 2017-01-02 01:03:52 UTC | #7

[quote="practicing01"]A list of models you need would be helpful.  Along with a link to an image of what you'd like each of those models to look like.  This way people with spare time 
can pick them off little by little.[/quote]

The one you made. I did a quick remesh with the uvmapped ane a plain default texture. If you want to see it and play with that.

In addition a plain texture terrain texture file.

[dropbox.com/s/1aedfkxaawwzu ... 1.zip?dl=0](https://www.dropbox.com/s/1aedfkxaawwzu28/TerrainDesertPlant-CactusSapien1.zip?dl=0)

If you want to play around with those, the terrain I used the pipes plugin that for the top part. A cube I subdivided to have the same number veritices along the middle as the pople. Then I bridge connected them and smoothed it.   Marked those linking areas then a simple uv unwarpped if finish.

You can probably play around with those you like then I can use those for the client. I just didn't do grass which is straight forward. If you want to experiment use the hair emitter particle modifier system then convert it to a mesh with the Convert button.

-------------------------

