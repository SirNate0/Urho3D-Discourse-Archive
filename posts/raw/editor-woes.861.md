vivienneanthony | 2017-01-02 01:03:36 UTC | #1

Hi

Does anyone know what might be causing problems with the Editor? Additionally, whenever it's started. I cannot reveal the hierarchy or properties window. In the master they show, but not in the client folder directory version.

I think maybe something isn't copied over or updated to the current in the Existence folder.

VIvienne

[code]Thu Feb 19 14:31:25 2015] INFO: Opened log file /home/vivienne/.local/share/urho3d/logs/Editor.as.log
[Thu Feb 19 14:31:25 2015] INFO: Created 3 worker threads
[Thu Feb 19 14:31:25 2015] INFO: Added resource path /media/home2/vivienne/Existence/Bin/Data/
[Thu Feb 19 14:31:25 2015] INFO: Added resource path /media/home2/vivienne/Existence/Bin/CoreData/
[Thu Feb 19 14:31:25 2015] INFO: Set screen mode 1024x768 windowed resizable
[Thu Feb 19 14:31:25 2015] INFO: Initialized input
[Thu Feb 19 14:31:25 2015] INFO: Initialized user interface
[Thu Feb 19 14:31:25 2015] INFO: Initialized renderer
[Thu Feb 19 14:31:25 2015] INFO: Set audio mode 44100 Hz stereo interpolated
[Thu Feb 19 14:31:25 2015] INFO: Initialized engine
[Thu Feb 19 14:31:25 2015] INFO: Scripts/Editor/AttributeEditor.as:301,1 Compiling UIElement@ CreateIntAttributeEditor(ListView@, Serializable@[]@, const AttributeInfo&in, uint, uint)
[Thu Feb 19 14:31:25 2015] WARNING: Scripts/Editor/AttributeEditor.as:317,48 Signed/Unsigned mismatch
[Thu Feb 19 14:31:25 2015] WARNING: Scripts/Editor/AttributeEditor.as:317,48 Implicit conversion changed sign of value
[Thu Feb 19 14:31:25 2015] INFO: Scripts/Editor/EditorResourceBrowser.as:226,1 Compiling void CreateResourceFilterUI()
[Thu Feb 19 14:31:25 2015] WARNING: Scripts/Editor/EditorResourceBrowser.as:248,23 Float value truncated in implicit conversion to integer
[Thu Feb 19 14:31:25 2015] WARNING: Scripts/Editor/EditorResourceBrowser.as:254,15 Signed/Unsigned mismatch
[Thu Feb 19 14:31:25 2015] INFO: Compiled script module Scripts/Editor.as
[Thu Feb 19 14:31:25 2015] ERROR: Scripts/Editor/EditorSettings.as:44,5 - Exception 'Null pointer access' in 'void UpdateEditorSettingsDialog()'
AngelScript callstack:
        Scripts/Editor/EditorSettings.as:void UpdateEditorSettingsDialog():44,5
        Scripts/Editor/EditorSettings.as:void CreateEditorSettingsDialog():16,5
        Scripts/Editor/EditorUI.as:void CreateUI():78,5
        Scripts/Editor.as:void FirstFrame():64,5

[Thu Feb 19 14:31:26 2015] ERROR: Could not parse XML data from /media/home2/vivienne/Existence/Bin/CoreData/Materials/TerrainTriPlanar-Ice.xml~
[Thu Feb 19 14:31:26 2015] ERROR: Could not parse XML data from /media/home2/vivienne/Existence/Bin/CoreData/Shaders/HLSL/TerrainBlendTriPlanar.shader
^Cvivienne@vivienne-System-Product-Name:/media/home2/vivienne/Existence/Bin$ ^C
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Existence/Bin$ 
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:03:36 UTC | #2

It's working now but I'm noticing the following errors.

[code]
[Thu Feb 19 14:39:56 2015] WARNING: Scripts/Editor/AttributeEditor.as:317,48 Signed/Unsigned mismatch
[Thu Feb 19 14:39:56 2015] WARNING: Scripts/Editor/AttributeEditor.as:317,48 Implicit conversion changed sign of value
[Thu Feb 19 14:39:56 2015] INFO: Scripts/Editor/EditorResourceBrowser.as:226,1 Compiling void CreateResourceFilterUI()
[Thu Feb 19 14:39:56 2015] WARNING: Scripts/Editor/EditorResourceBrowser.as:248,23 Float value truncated in implicit conversion to integer
[Thu Feb 19 14:39:56 2015] WARNING: Scripts/Editor/EditorResourceBrowser.as:254,15 Signed/Unsigned mismatc[/code]

-------------------------

cadaver | 2017-01-02 01:03:36 UTC | #3

I believe this happens when the editor is reading outdated editor UI assets from your project's resource folder. You could delete the editor config file to reset the resource path, and/or delete the offending UI assets. On Windows the editor config is at C:\Users\<username>\AppData\Roaming\urho3d\Editor

The problem was worse in old Urho versions so if you're not using the master branch I'd recommend you to.

-------------------------

friesencr | 2017-01-02 01:03:36 UTC | #4

I would run the editor from a different build than your existence source.  Go get a copy of master and run those binaries.  opening a scene file from a different folder should set your resource paths in the editor for you as long as they are in a Scene folder 1 level deep.

-------------------------

Modanung | 2017-01-02 01:04:43 UTC | #5

Where does this config file reside on Xubuntu GNU/Linux?

Edit: Found it with "find ~ -name urho3d"
On my apparatus it's location is: ~/.local/share/urho3d/Editor/Config.xml

-------------------------

