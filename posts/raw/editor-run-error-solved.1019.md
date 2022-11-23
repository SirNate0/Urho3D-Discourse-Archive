practicing01 | 2017-01-02 01:04:52 UTC | #1

Edit: Credits to Thebluefish for the fix, overwrite the old CoreData & Data folders with the new ones.

Hello, I've merged the latest master and compiled.  When trying to run the editor it does not load and gives the following error:
[quote]
./Editor.sh 
[Mon Apr 27 13:37:59 2015] INFO: Opened log file /home/practicing01/.local/share/urho3d/logs/Editor.as.log
[Mon Apr 27 13:37:59 2015] INFO: Created 1 worker thread
[Mon Apr 27 13:37:59 2015] INFO: Added resource path /home/practicing01/Desktop/Programming/Urho3D/Build/bin/Data/
[Mon Apr 27 13:37:59 2015] INFO: Added resource path /home/practicing01/Desktop/Programming/Urho3D/Build/bin/CoreData/
[Mon Apr 27 13:38:00 2015] INFO: Set screen mode 1024x768 windowed resizable
[Mon Apr 27 13:38:00 2015] INFO: Initialized input
[Mon Apr 27 13:38:00 2015] INFO: Initialized user interface
[Mon Apr 27 13:38:00 2015] INFO: Initialized renderer
[Mon Apr 27 13:38:00 2015] INFO: Set audio mode 44100 Hz stereo interpolated
[Mon Apr 27 13:38:00 2015] INFO: Initialized engine
[Mon Apr 27 13:38:02 2015] INFO: Scripts/Editor/AttributeEditor.as:301,1 Compiling UIElement@ CreateIntAttributeEditor(ListView@, Serializable@[]@, const AttributeInfo&in, uint, uint)
[Mon Apr 27 13:38:02 2015] WARNING: Scripts/Editor/AttributeEditor.as:317,48 Signed/Unsigned mismatch
[Mon Apr 27 13:38:02 2015] WARNING: Scripts/Editor/AttributeEditor.as:317,48 Implicit conversion changed sign of value
[Mon Apr 27 13:38:03 2015] INFO: Scripts/Editor/EditorResourceBrowser.as:226,1 Compiling void CreateResourceFilterUI()
[Mon Apr 27 13:38:03 2015] WARNING: Scripts/Editor/EditorResourceBrowser.as:248,23 Float value truncated in implicit conversion to integer
[Mon Apr 27 13:38:03 2015] WARNING: Scripts/Editor/EditorResourceBrowser.as:254,15 Signed/Unsigned mismatch
[Mon Apr 27 13:38:03 2015] INFO: Scripts/Editor.as:283,1 Compiling void SaveConfig()
[Mon Apr 27 13:38:03 2015] ERROR: Scripts/Editor.as:335,55 'sm3Support' is not a member of 'Graphics'
[Mon Apr 27 13:38:03 2015] ERROR: Scripts/Editor.as:336,60 'sm3Support' is not a member of 'Graphics'
[Mon Apr 27 13:38:03 2015] ERROR: Failed to compile script module Scripts/Editor.as
[/quote]

Thanks for any help.

-------------------------

