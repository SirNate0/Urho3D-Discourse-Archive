Eugene | 2017-03-06 22:42:24 UTC | #1

May anybody check or reproduce the following problems?

1) Resource Browser preview has wrong scale or like this, its content is not centered:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/244233824307ef4a26b25af4fd6b01afeb031a02.png" width="690" height="184">

2) Hierarchy is spammed with this strange node (temporaries are hidden):
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/c90c03be02e72cc7a1193274fb1fad49fe37bb6c.png" width="282" height="106">
This item disappear on save.

Command line: `Data/Scripts/Editor.as -w`, screen resolution is 1366x768

-------------------------

1vanK | 2017-03-07 07:19:17 UTC | #2

Confirmed, it seems it's added in one of the latest patches

-------------------------

cadaver | 2017-03-07 08:40:40 UTC | #3

Confirmed. Looks like the editor is confusing the main scene and the browser preview scene.

-------------------------

cadaver | 2017-03-07 11:35:50 UTC | #4

Started happening after the PaintSelection PR.

-------------------------

cadaver | 2017-03-07 12:31:33 UTC | #5

Appears the editor preview camera position is a separate issue; it didn't start directly from the PaintSelection.

-------------------------

1vanK | 2017-03-07 14:18:43 UTC | #6

Also if create node with AnimatedModel component and drag model (Mutant fot example) it cause error
**Not set** - drag from resource browser

-------------------------

cadaver | 2017-03-07 14:37:43 UTC | #7

The extra node is easily fixable with proper scene detection in the event handlers, the rest of the issues are related to AngelScript update. Will make an issue, this certainly needs resolving before release.

-------------------------

cadaver | 2017-03-07 15:39:30 UTC | #8

Issues listed in this thread should be fixed. Additionally, I silenced the warning of calling StaticModel::SetModel() on AnimatedModel from the AngelScript API, the resource browser could cause this. Redirection is now done in AngelScript API to allow this, instead of in StaticModel code.

-------------------------

KonstantTom | 2017-03-07 16:46:43 UTC | #9

I found another bug in editor: if you press "Create terrain" when editor launched from binary package, it will cause error:
```
[Tue Mar 07 19:39:28 2017] ERROR: Could not open file D:/CXXProjects/Urho3D-Windows-Static-Build/SDK/bin/Data/Textures/heightmap-1488908367.png
[Tue Mar 07 19:39:28 2017] ERROR: Could not find resource D:/CXXProjects/Urho3D-Windows-Static-Build/SDK/bin/Data/Textures/heightmap-1488908367.png
[Tue Mar 07 19:39:28 2017] ERROR: Scripts/Editor/EditorTerrain.as:324,9 - Exception 'Null pointer access' in 'void TerrainEditor::CreateTerrain()'
AngelScript callstack:
	Scripts/Editor/EditorTerrain.as:void TerrainEditor::CreateTerrain():324,9
```
The origin of this error is in:
```angelscript
    private void CreateTerrain()
    {
        String fileName = "Textures/heightmap-" + time.timeSinceEpoch  + ".png";
        String fileLocation = fileSystem.programDir + "Data/" + fileName;
        ...
```
In Urho3D binary package resources placed separately and there isn't Data folder in program dir. Also if we create this dir, heightmap will be outside resource paths.

-------------------------

Eugene | 2017-03-07 17:06:27 UTC | #10

Actually, I faced this error even when run Editor as always.

-------------------------

KonstantTom | 2017-03-07 18:23:26 UTC | #11

When I run editor from BUILD_DIR/bin directory, all works normally.
And I found another defect: **there isn't any button for saving changed heightmap!**
UPD: Heighmap can be saved by executing script from console, but it's very unconvinient.

-------------------------

xDarkShadowKnightx | 2017-03-12 07:34:58 UTC | #12

@KonstantTom the heightmap can be saved by simply saving the scene :slight_smile:

-------------------------

KonstantTom | 2017-03-12 09:21:15 UTC | #13

@xDarkShadowKnightx Thanks for your reply! But, in my opinion, there should be button for saving heightmap without saving scene.

-------------------------

