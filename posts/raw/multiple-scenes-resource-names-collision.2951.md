t.artikov | 2017-03-25 11:33:55 UTC | #1

Consider the situation:
There are two scenes located in arbitrary directories, some scene resources have the same names.
C:/some_path/scene1/
  scene1.xml
  material.xml

D:/some_other_path/scene2/
  scene2.xml
  material.xml

How can I load these scenes at the same time? 
I believe it is impossible. The material from the first scene will be mistakenly used in both scenes, because the ResourceCache can contain only one material named "material.xml".

-------------------------

KonstantTom | 2017-03-25 15:15:44 UTC | #2

ResourceGroup (which is the part of ResourceCache) contain resources in HashMap where key is **full file path or relative to resource dir path**, not file name. There will be collision only if you specify *C:/some_path/scene1/* and *D:/some_other_path/scene2/* as resource paths, but it will not be if you specify *C:/some_path/* and *D:/some_other_path/* as resource paths.

-------------------------

t.artikov | 2017-03-25 16:25:15 UTC | #3

@KonstantTom
Well, it will work. But the problem is that the scenes should know where they are located.
There can be
C:/some_path/scene/scene.xml
and
D:/some_other_path/scene/scene.xml
In that case the resource directories will be "C:/" and "D:/" and the scenes will reference to the materials by "some_path/scene/material.xml" and "some_other_path/scene/material.xml" paths. It makes imposible to move the scenes to another location.

There is a related discussion on github.com - https://github.com/urho3d/Urho3D/issues/1866
It is a pity that a simple approach with relative paths that works on the web is not implemented in Urho3D.

-------------------------

KonstantTom | 2017-03-25 17:28:28 UTC | #4

@t.artikov 
If I understood question correctly and if scene folders have different names (for example scene1 and scene2), you can specify *C:/some_path/* and *D:/some_other_path/* as resource folders, then scene1 can acess its material as *scene1/material.xml* and scene2 can acess its material as *scene2/material.xml*.

-------------------------

t.artikov | 2017-03-25 17:53:44 UTC | #5

@KonstantTom 
The task is to implement a Urho3D scenes viewer which can play multiple scenes at the same time.
The paths to the scenes are specified via an open file dialog and, of course, can be arbitrary.

-------------------------

