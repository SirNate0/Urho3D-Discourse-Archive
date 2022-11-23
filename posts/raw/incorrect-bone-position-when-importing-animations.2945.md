Florastamine | 2017-03-23 07:56:12 UTC | #1

I've been banging my head against the wall the last few days trying to figure out the problem. When using AssetImporter through the editor to import my FBX file, meshes, textures, materials, and animations all went through fine. However when playing the animation, part of the bones are not correctly positioned, like this: (the weapon model and the hand model are not in sync): 

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/62a640365d01dd577810afb657d135ec62d09ed3.jpg" width="690" height="387">

Whereas when I tried to import the file to both Autodesk FBX Converter and FBX Review, both shows correct bone positioning and animations: [here](http://i.imgur.com/IjAf9QU.jpg) and [here](http://i.imgur.com/DhIsSd2.jpg); and even fragMotion: i.imgur.com/V4zytig.jpg 

What exactly is causing the issue, and is there any tools that I can use to somehow alter the animation data stored in .ani files? I tried moving nodes around in the editor, trying different AssetImporter options (-np), even to the point of writing an alternative version of Animation::Save() to save the animations to a xml but still no luck trying to alter animation data.

-------------------------

KonstantTom | 2017-03-23 08:08:50 UTC | #2

I had the same issue when tryed to use FBX files in Unity. And there was the same issue when I tryed to import this FBX files to Urho3D. I don't know why this happends. Try [Blender to Urho3D exporter](https://github.com/reattiva/Urho3D-Blender), it solves this problem in my case.

-------------------------

Florastamine | 2017-03-23 13:06:27 UTC | #3

Thanks! I would definitely give it a look. It seems like a really nice plugin and all, the only problem now is I don't really know any Blender :<

By the way, I fixed it... sort of. Don't know why, but I converted the .fbx to Ogre's .mesh.xml and .skeleton.xml, then imported back to Urho using OgreImporter. Surprisingly, the bones are now shown and positioned correctly. Animations are now played without problems. 

FBXs are really a hassle to work with. 
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/ebbffc35108612f32d27e6fc6b364991f6d0506f.jpg" width="690" height="387">

-------------------------

