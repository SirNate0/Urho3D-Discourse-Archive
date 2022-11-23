timob256 | 2022-01-21 15:20:09 UTC | #1

 
**I 'm trying to create a landscape , but I don 't know which program can do it , I tried many programs , but I couldn 't . What programs do you use ??**

Preferably something simple and understandable that is available in many languages of the world


-_______________________________________________________________-

 want to install a landscape generator, I looked:

    Instant Terra
    VUE
    Terragen
    World Creator
    World Machine
    Gaea

and noticed that they all work in Windows.

I found a FlowScape (more a toy) and picogen (a fairly old generator), they seemed to me not quite suitable.

-_______-


-----
I training to make this :
 [![enter image description here][1]][1]

I didn't understand which buttons to press to launch  texturing,

This is my result

[![enter image description here][2]][2]
[![enter image description here][3]][3]


  [1]: https://i.stack.imgur.com/hyTQk.jpg
  [2]: https://i.stack.imgur.com/zrOXo.png
  [3]: https://i.stack.imgur.com/b6tAc.png

-------------------------

lebrewer | 2022-01-21 15:31:12 UTC | #2

What exactly do you need help with? The tool doesn't really matter, what is important is the time you put into it and focusing on small, achievable goals. You won't make terrain that looks like it came out of Call of Duty in your first attempt. Maybe in your 50th. 

Pick references, choose a biome and stick with it. Try to mimic that within the tool. Once you are finished, try to get it in your engine of choice. I do not recommend Urho, since most commercial tools will have a pipeline optimized for industry-standard, like Unreal and Unity. Once your comfortable enough with all of the technology involved in the pipeline, you can attempt to get it inside Urho. 

There is an overwhelming amount of free tutorials and step-by-step guides on any tool you choose. So, make sure you set your expectations right and do it.



*ps.: I like Gaea a lot. Easy to use and lot's of tutorials. artstation.com is good for inspiration and tutorials. You can easily put Gaea terrains in UE.*

-------------------------

timob256 | 2022-01-21 15:41:47 UTC | #3

 

**what instrument would you take in my place** (I don't understand American well, I prefer Russian)???

true terrain   no support  ; _ ;
FlowScape  no obj format , trees and texturing  ; _ ;

-------------------------

Nerrik | 2022-01-21 20:57:04 UTC | #4

I like World Creator, easy to use / learn and it comes with good export opportunities splitable (obj mesh, heightmap 8 / 16 bit, normalmap, splat map, color map(iam using this one for my splatmaps and retexture the terrain with red, green blue, black, white... textures), relief map, ambient occ. map, smoothness map, roughness map, topo map and distribution map)

In my projekt  (top down camera) iam using a converted 16 bit to 8 bit png heightmap with the 16 bit info splitted into the 8bit rgb channels.

I cut out a part of the height, normal and splatmap at my characters position in a thread at runtime and using a flat plane at the position of my char that verts will be reposited in the vertexshader with sampling the cutted HM (normals / tangets will be calculated also in the VS).

for faster lagfree cpu->gpu i split these partmaps again and building the texture gradually.

so i have all the time "only" a 512x512 heightmap/SM/normalmap and one planemodel on the GPU side and the world can be infinite.

these cutting / planepositioning only happens when my char is moving to near to the end-edge of the current plane

for occlusion iam using a very very strong down computed discarded "model" at that position.

-------------------------

Nerrik | 2022-01-21 22:05:09 UTC | #5

Here a Video of my Terrain made with World Creator with lower loadingrange (sometimes you can see the terrain building), iam planning to add a terrain specular map also, for some reflections and a better look ;)

[http://wyrdan.de/terrain.mp4](http://wyrdan.de/terrain.mp4)

no idea how to embed videos :P

-------------------------

