sabotage3d | 2017-01-02 01:05:54 UTC | #1

Hello,
I remember before when I create a Static Model in the Editor pointing to an mdl file it was refreshing if I change the mdl. Now it is no longer the case, I have to restart the Editor to see the changed model.
Is there a specific preference or setting I have to change for the old behaviour? I also just compiled the latest from github and the behavior is the same. The resource browser works as expected it shows the model change instantly.

-------------------------

cadaver | 2017-01-02 01:05:54 UTC | #2

This should not be related to the editor itself (though only the editor uses resource reloading presently), but points to a regression in either the StaticModel or FileWatcher code. Thanks for notifying.

EDIT: On Windows this works fine, for example creating a built-in box object and pasting the Sphere.mdl over Box.mdl, and back again. Will check other OS'es later.

-------------------------

sabotage3d | 2017-01-02 01:05:54 UTC | #3

Thank you for your reply cadaver. I am under OSX but it should be same on Linux. In order to see the issue write a Sphere geomtry to test.mdl create the Static Model in the editor point it to the test.mdl and write different geometry let say a Cube replacing the test.mdl. It will still show the Sphere geometry.

-------------------------

cadaver | 2017-01-02 01:05:54 UTC | #4

Tested also on Linux and OSX. I didn't get the bug to appear. The sequence I used:

- In Editor, create builtin object -> Box 
- In bin/Data/Models directory:
cp Box.mdl _Box.mdl (make backup)
cp Sphere.mdl Box.mdl (observe box turning to sphere)
cp _Box.mdl Box.mdl (observe sphere turning back into box)

Maybe you're doing something different that makes the bug appear?

-------------------------

sabotage3d | 2017-01-02 01:05:54 UTC | #5

I am under OSX 10.10.2
I jus tried this:
- In Editor, created StaticModel from the shelf. 
- In a custom directory $HOME/Data/models I copied Sphere.mdl and Box.mdl from the original Urho3d Data directory
- On the model field of the StaticModel, clicked on pick model and I choosed Box.mdl from $HOME/Data/models
- The viewport was showing a Box
- I copied Sphere.mdl to Box.mdl in $HOME/Data/models
- The viewport was still showing Box
- Restarted the Editor and the scene, the viewport was showing a Sphere

-------------------------

amit | 2017-01-02 01:05:54 UTC | #6

It did also happened to me (I am on osx) but am not able to replicate it.
I tried again,
Coppied box.mdl -> x.mdl
Loaded static node for above x in editor, and it showed.
Coppied another model over x.mdl and the model changed.

@sabotage3d, Did you copy box from coredata to data folder?

Anyway I'll try again and let me try replicate the same.

-------------------------

cadaver | 2017-01-02 01:05:54 UTC | #7

This looks like the directory watching not being correctly setup for resource directories that are added during runtime. I'll look into it. Inside the Urho base folders (CoreData & Data) it should work.

-------------------------

cadaver | 2017-01-02 01:05:54 UTC | #8

The probable cause is this: when you try to pick files from whatever part of the harddisk, the editor doesn't automatically add a resource path to the engine (which is required to actually load the file as a Urho resource.) This is actually for your protection in scene authoring: a scene file only stores relative resource names, and it has no concept of storing these "extra" paths, so if you proceeded to save a scene with files picked from anywhere on the HD, it wouldn't load back correctly.

Rather, start with File -> Set Resource Path, or load a scene, which sets the path automatically. After that, picking files and hot-reloading them from within the path you've chosen, should work properly.

-------------------------

sabotage3d | 2017-01-02 01:05:55 UTC | #9

Thanks cadaver it works perfectly :slight_smile:

-------------------------

