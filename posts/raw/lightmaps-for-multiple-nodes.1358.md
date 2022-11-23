sabotage3d | 2017-01-02 01:07:10 UTC | #1

Hi guys, 
What is the recommended workflow when doing lightmaps for multiple nodes. Should I merge all the nodes generate the lightmaps and create alternative UV set 2 in my program of choice ? And then in Urho3d to use the main texture in UV set 1 and add the lightmaps texture in UV set 2 ?

-------------------------

Enhex | 2017-01-02 01:07:10 UTC | #2

A nice article about how Quake 2's lightmaps:
[fabiensanglard.net/quake2/quake2 ... nderer.php](http://fabiensanglard.net/quake2/quake2_opengl_renderer.php)

Yes, you want to use 2 different textures, 1 for the diff texture and 1 for the lightmap.
This way you can reuse the diff texture, and use a lower resolution lightmap texture.
Lightmap resolution is usually measured in pixels per world unit or vice versa.

You'd also want to batch the lightmaps into atlases.

-------------------------

rasteron | 2017-01-02 01:07:10 UTC | #3

Someone already posted a full example for diffuse and lightmaps being used. I forgot the post title and I remember that it was just months ago.

-------------------------

codingmonkey | 2017-01-02 01:07:10 UTC | #4

also you may bake the AO into model's vertex color.
there is an example and it's no use any textures, there is only baked AO into vertexes color. 
but back side of this method is that you perhaps will needed to use more highpoly models for working this properly.
[url=http://savepic.su/6110916.htm][img]http://savepic.su/6110916m.jpg[/img][/url]

>Should I merge all the nodes generate the lightmaps and create alternative 
I do not know where are you will do this in what editor. 
But reason for join all static geometry is for make one huge-common-layout at once and after that you may separate big geometry again into small pices. 
New common UV2 layout is preserved for each of them. Otherwise you will needed to adjust uv2 set of each object that will be use common lightmap.

-------------------------

sabotage3d | 2017-01-02 01:07:14 UTC | #5

Thanks a lot guys. I assume if I have dynamically changing level I will need to generate the light-maps at runtime. 
Sinoid I think your approach was the best so far. Can you give me some of the key points I need to address in order to generate a simple light-map at runtime ?

-------------------------

sabotage3d | 2017-01-02 01:07:14 UTC | #6

I tried to compile the LightmapGenerator but I am getting this error:

[code]In file included from /DEV/Urho3D-Lightmapping/Source/Tools/LightmapGenerator/DataCache.cpp:25:
/DEV/Urho3D-Lightmapping/Source/Tools/LightmapGenerator/GeometryInfo.h:57: error: declaration of 'Urho3D::Plane TriangleInfo::Plane'
/DEV/Urho3D-Lightmapping/build/include/Urho3D/Math/Plane.h:32: error: changes meaning of 'Plane' from 'class Urho3D::Plane'
make[2]: *** [Source/Tools/LightmapGenerator/CMakeFiles/LightmapGenerator.dir/DataCache.cpp.o] Error 1
make[1]: *** [Source/Tools/LightmapGenerator/CMakeFiles/LightmapGenerator.dir/all] Error 2
make: *** [all] Error 2[/code]

I fixed it by changing Plane to Urho3D::Plane in the TriangleInfo struct,  but I am getting another error:

[code]/DEV/Urho3D-Lightmapping/Source/Tools/LightmapGenerator/LightmapGenerator.cpp:55:27: error: URho3D/IO/Log.h: No such file or directory
/DEV/Urho3D-Lightmapping/Source/Tools/LightmapGenerator/LightmapGenerator.cpp: In member function 'virtual void LightmapGenerator::Start()':
/DEV/Urho3D-Lightmapping/Source/Tools/LightmapGenerator/LightmapGenerator.cpp:213: error: no matching function for call to 'LightmapGenerator::HandleGenerate(Urho3D::StringHash, Urho3D::VariantMap)'
/DEV/Urho3D-Lightmapping/Source/Tools/LightmapGenerator/LightmapGenerator.h:76: note: candidates are: void LightmapGenerator::HandleGenerate(Urho3D::StringHash, Urho3D::VariantMap&)
/DEV/Urho3D-Lightmapping/Source/Tools/LightmapGenerator/LightmapGenerator.cpp: In member function 'bool LightmapGenerator::StartGeneration()':
/DEV/Urho3D-Lightmapping/Source/Tools/LightmapGenerator/LightmapGenerator.cpp:450: error: 'LOGERROR' was not declared in this scope
/DEV/Urho3D-Lightmapping/Source/Tools/LightmapGenerator/LightmapGenerator.cpp:457: error: 'LOGERROR' was not declared in this scope
make[2]: *** [Source/Tools/LightmapGenerator/CMakeFiles/LightmapGenerator.dir/LightmapGenerator.cpp.o] Error 1
make[1]: *** [Source/Tools/LightmapGenerator/CMakeFiles/LightmapGenerator.dir/all] Error 2
make: *** [all] Error 2[/code]

-------------------------

