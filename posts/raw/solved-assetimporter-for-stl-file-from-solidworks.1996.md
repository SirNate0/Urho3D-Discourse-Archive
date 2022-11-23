Jacob_Christ | 2017-01-02 01:12:09 UTC | #1

I'm trying to convert an STL file that was exported from Solidworks into a Urho3D mdl file. I can open the STL file with the assimp_viewer.exe and I've converted the file to a mdl file using something like this:

AssetImporter model file.stl file.mdl

I get the output file.mdl and when I open it with my Urho3D project I don't get any errors in the Urho3D.log file, but nothing is rendered in the view port.

If I try to open the file.mdl in the Urho3D editor I get an error (at the moment I can't open the editor so I can't get the exact error, but when I figure this out I will post it as well).

If its helpful I can post the STL and/or the mdl file.  They are about 1M each.

Any help would be appreciated.

Jacob

-------------------------

Bananaft | 2017-01-02 01:12:09 UTC | #2

Hello, welcome to the forum!

Editor log file is saved to C:\Users\JacobChrist\AppData\Roaming\urho3d\logs\Editor.as.log

-------------------------

Jacob_Christ | 2017-01-02 01:12:09 UTC | #3

Okay, if I try to use "Import model..." to import the converted mdl file in Urho3D editor I get this error:

ERROR: Failed to execute AssetImporter to import model.

When I saw this I said, hey, Urho3D is trying to use AssetImporter so maybe I should just try to import the STL file directly.  When I tried this I get this error:

ERROR: Could not find resource Models/name of the file.mdl

Which I then thought to myself, that is a strange error since I just told it to load a STL file.

Jacob

-------------------------

Jacob_Christ | 2017-01-02 01:12:09 UTC | #4

[quote="Bananaft"]Hello, welcome to the forum!

Editor log file is saved to C:\Users\JacobChrist\AppData\Roaming\urho3d\logs\Editor.as.log[/quote]

Here is the log file... I think maybe Urho3D Editor can't find AssetImporter (not pathed)?

Also, my STL file may not be close to origin. assimp_viewer.exe I think is centering the object.

[Mon May  2 14:49:36 2016] INFO: Opened log file C:/Users/Jacob Christ/AppData/Roaming/urho3d/logs/Editor.as.log
[Mon May  2 14:49:36 2016] INFO: Created 3 worker threads
[Mon May  2 14:49:36 2016] INFO: Added resource path C:/subversion/game-dev/Urho3D/Urho3D-1.5-Windows-64bit-STATIC-3D11/bin/../share/Urho3D/Resources/Data/
[Mon May  2 14:49:36 2016] INFO: Added resource path C:/subversion/game-dev/Urho3D/Urho3D-1.5-Windows-64bit-STATIC-3D11/bin/../share/Urho3D/Resources/CoreData/
[Mon May  2 14:49:36 2016] INFO: Set screen mode 1920x1017 windowed resizable
[Mon May  2 14:49:36 2016] INFO: Initialized input
[Mon May  2 14:49:36 2016] INFO: Initialized user interface
[Mon May  2 14:49:36 2016] INFO: Initialized renderer
[Mon May  2 14:49:36 2016] INFO: Set audio mode 44100 Hz stereo interpolated
[Mon May  2 14:49:36 2016] INFO: Initialized engine
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorActions.as:806,5 Compiling void ApplyUIElementStyleAction::ApplyStyle(const String&in)
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorActions.as:824,28 Variable 'element' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorHierarchyWindow.as:1055,1 Compiling Node@[] GetMultipleSourceNodes(UIElement@)
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorHierarchyWindow.as:1091,27 Variable 'node' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorView.as:1205,1 Compiling void UpdateView(float)
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorView.as:1438,35 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/AttributeEditor.as:301,1 Compiling UIElement@ CreateIntAttributeEditor(ListView@, Serializable@[]@, const AttributeInfo&in, uint, uint)
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:317,48 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:317,48 Implicit conversion changed sign of value
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/AttributeEditor.as:624,1 Compiling void LoadAttributeEditor(UIElement@, const Variant&in, const AttributeInfo&in, bool, bool, const Variant[]&in)
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:680,37 Variable 'refList' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:702,18 Variable 'sameValue' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:708,33 Variable 'vector' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:711,29 Variable 'value' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:721,27 Variable 'info' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:742,18 Variable 'sameValue' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:748,28 Variable 'map' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:751,29 Variable 'value' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:761,27 Variable 'info' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:771,21 Variable 'value' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:781,20 Variable 'value' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/AttributeEditor.as:800,1 Compiling void StoreAttributeEditor(UIElement@, Serializable@[]@, uint, uint, uint)
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:834,24 Variable 'map' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/AttributeEditor.as:869,1 Compiling void GetEditorValue(UIElement@, VariantType, String[]@, uint, Variant[]&inout)
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:880,19 Variable 'attrEdit' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:903,27 Variable 'attrEdit' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/AttributeEditor.as:909,19 Variable 'attrEdit' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorCubeCapture.as:12,1 Compiling void PrepareZonesForCubeRendering()
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorCubeCapture.as:19,23 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorCubeCapture.as:55,1 Compiling void UnprepareZonesForCubeRendering()
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorCubeCapture.as:58,23 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorCubeCapture.as:63,23 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorScene.as:1234,1 Compiling bool SceneRenderZoneCubemaps()
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorScene.as:1240,23 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorScene.as:1243,27 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorScene.as:1254,23 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorUI.as:321,1 Compiling void CreateMenuBar()
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorUI.as:478,19 Variable 'menu' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorUI.as:479,21 Variable 'popup' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorUI.as:1963,1 Compiling void HandleWheelChangeColor(StringHash, VariantMap&inout)
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorUI.as:1965,39 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorResourceBrowser.as:229,1 Compiling void CreateResourceFilterUI()
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorResourceBrowser.as:251,23 Float value truncated in implicit conversion to integer
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorResourceBrowser.as:257,15 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorLayers.as:149,1 Compiling void ChangeNodeViewMask(Node@, EditActionGroup@, int)
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorLayers.as:154,53 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorLayers.as:185,1 Compiling void EstablishBitMaskToSelectedNodes()
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorLayers.as:194,39 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorLayers.as:212,34 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorColorWheel.as:147,1 Compiling void HandleWheelButtons(StringHash, VariantMap&inout)
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorColorWheel.as:155,20 Variable 'eventData' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorColorWheel.as:163,20 Variable 'eventData' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorColorWheel.as:171,20 Variable 'eventData' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorColorWheel.as:212,1 Compiling void HandleColorWheelMouseWheel(StringHash, VariantMap&inout)
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorColorWheel.as:234,55 Float value truncated in implicit conversion to integer
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorColorWheel.as:243,1 Compiling void HandleColorWheelMouseMove(StringHash, VariantMap&inout)
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorColorWheel.as:276,14 Float value truncated in implicit conversion to integer
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorColorWheel.as:277,14 Float value truncated in implicit conversion to integer
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorColorWheel.as:288,33 Float value truncated in implicit conversion to integer
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorColorWheel.as:288,28 Float value truncated in implicit conversion to integer
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorColorWheel.as:329,59 Float value truncated in implicit conversion to integer
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorColorWheel.as:349,39 Float value truncated in implicit conversion to integer
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorColorWheel.as:403,1 Compiling void EstablishColorWheelUIFromColor(Color)
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorColorWheel.as:413,51 Float value truncated in implicit conversion to integer
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorColorWheel.as:417,31 Float value truncated in implicit conversion to integer
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorColorWheel.as:427,53 Float value truncated in implicit conversion to integer
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorColorWheel.as:427,44 Float value truncated in implicit conversion to integer
[Mon May  2 14:49:38 2016] INFO: Scripts/Editor/EditorViewDebugIcons.as:102,1 Compiling void UpdateViewDebugIcons()
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorViewDebugIcons.as:104,59 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorViewDebugIcons.as:134,86 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorViewDebugIcons.as:152,30 Signed/Unsigned mismatch
[Mon May  2 14:49:38 2016] WARNING: Scripts/Editor/EditorViewDebugIcons.as:174,48 Variable 'bb' hides another variable of same name in outer scope
[Mon May  2 14:49:38 2016] INFO: Compiled script module Scripts/Editor.as
[Mon May  2 14:49:38 2016] WARNING: Localization::Get("Export scene to OBJ...") not found translation, language="en"
[Mon May  2 14:49:38 2016] WARNING: Localization::Get("Export selected to OBJ...") not found translation, language="en"
[Mon May  2 14:49:38 2016] WARNING: Localization::Get("Reset transform") not found translation, language="en"
[Mon May  2 14:49:38 2016] WARNING: Localization::Get("Show components icons") not found translation, language="en"
[Mon May  2 14:49:38 2016] WARNING: Localization::Get("Render Zone Cubemap") not found translation, language="en"
[Mon May  2 14:51:24 2016] ERROR: Failed to execute AssetImporter to import model
[Mon May  2 14:51:54 2016] ERROR: Could not find resource Models/Assy, Main, ProdA, Precise 400 ShellEXT, PF400 BINARY VER - Assy, Base, ShellEXT, PF400-1.mdl
[Mon May  2 14:55:45 2016] ERROR: Failed to execute AssetImporter to import model
[Mon May  2 14:57:08 2016] ERROR: Failed to execute AssetImporter to import model
[Mon May  2 15:01:55 2016] ERROR: Failed to execute AssetImporter to import model
[Mon May  2 15:02:04 2016] ERROR: Could not find resource Models/Assy, Main, ProdA, Precise 400 ShellEXT, PF400 BINARY VER - Assy, Base, ShellEXT, PF400-1.mdl
[Mon May  2 15:02:12 2016] ERROR: Could not find resource Models/Assy, Main, ProdA, Precise 400 ShellEXT, PF400 ASCII VER - Assy, Base, ShellEXT, PF400-1.mdl
[Mon May  2 15:02:33 2016] ERROR: Could not open file C:\Users\Jacob Christ\AppData\Roaming\urho3d\temp\command-stderr
[Mon May  2 15:02:36 2016] ERROR: Could not open file C:\Users\Jacob Christ\AppData\Roaming\urho3d\temp\command-stderr
[Mon May  2 15:43:05 2016] ERROR: Failed to execute AssetImporter to import model

-------------------------

Jacob_Christ | 2017-01-02 01:12:10 UTC | #5

So, yeah, my STL has an offset from the origin and the parts is really big relitive to my view port.  So it was working all this time, it was just off the screen!

I guess the good news is that if someone else tries to do the same thing and have problems I hope this helps.

I'm using Urhosharp, this is the code that is working:

            var planeObject2 = planeNode.CreateComponent<StaticModel>();
            planeObject2.Model = ResourceCache.GetModel("_IPT/mdl/simple.mdl");
            planeObject2.SetMaterial(ResourceCache.GetMaterial("_IPT/mdl/Materials/DefaultMaterial.xml"));
'
I don't know why the editor can't load the part.

Jacob

-------------------------

