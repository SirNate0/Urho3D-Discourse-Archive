vivienneanthony | 2017-01-02 01:08:41 UTC | #1

Hi,

Do anyone know what might be the cause of this? I start my engine then start the script inside the main menu part. Everything works but when the it shutdowns. I get this Angelscript related segfault. Like the script system or file is not completely released.

Vivienne

[i.imgur.com/pSA1a70.png](http://i.imgur.com/pSA1a70.png)

[code]
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3D-Hangars-Myfork-BuildEditor/bin$ gdb ./EngineEditor
GNU gdb (Ubuntu 7.7.1-0ubuntu5~14.04.2) 7.7.1
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./EngineEditor...done.
(gdb) run
Starting program: /media/home2/vivienne/Urho3D-Hangars-Myfork-BuildEditor/bin/EngineEditor 
Traceback (most recent call last):
  File "/usr/share/gdb/auto-load/usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.19-gdb.py", line 63, in <module>
    from libstdcxx.v6.printers import register_libstdcxx_printers
ImportError: No module named 'libstdcxx'
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[Wed Dec 16 09:15:42 2015] INFO: Opened log file logging.log
[Wed Dec 16 09:15:42 2015] INFO: Default renderer OpenGL
[Wed Dec 16 09:15:42 2015] ERROR: Failed to load game options!
[New Thread 0x7ffff251f700 (LWP 15142)]
[New Thread 0x7ffff1d1e700 (LWP 15143)]
[New Thread 0x7ffff151d700 (LWP 15144)]
[Wed Dec 16 09:15:42 2015] INFO: Created 3 worker threads
[Wed Dec 16 09:15:42 2015] INFO: Added resource package /media/home2/vivienne/Urho3D-Hangars-Myfork-BuildEditor/bin/CoreData.pak
[Wed Dec 16 09:15:42 2015] INFO: Added resource path /media/home2/vivienne/Urho3D-Hangars-Myfork-BuildEditor/bin/Data/
[Wed Dec 16 09:15:42 2015] INFO: Added resource package /media/home2/vivienne/Urho3D-Hangars-Myfork-BuildEditor/bin/GameData.pak
[Wed Dec 16 09:15:42 2015] INFO: Added resource package /media/home2/vivienne/Urho3D-Hangars-Myfork-BuildEditor/bin/CoreData.pak
[Wed Dec 16 09:15:42 2015] INFO: Added resource package /media/home2/vivienne/Urho3D-Hangars-Myfork-BuildEditor/bin/GameData.pak
[Wed Dec 16 09:15:42 2015] ERROR: Could not find resource System/EngineEditor.png
[Wed Dec 16 09:15:43 2015] INFO: Set screen mode 1024x768 windowed resizable
[Wed Dec 16 09:15:43 2015] INFO: Initialized input
[Wed Dec 16 09:15:43 2015] INFO: Initialized user interface
[Wed Dec 16 09:15:43 2015] INFO: Initialized renderer
[New Thread 0x7fffea402700 (LWP 15145)]
[New Thread 0x7fffe9c01700 (LWP 15146)]
[Wed Dec 16 09:15:43 2015] INFO: Set audio mode 44100 Hz stereo interpolated
[Wed Dec 16 09:15:43 2015] INFO: Initialized engine
[Wed Dec 16 09:15:43 2015] INFO: Game Asset Manager Initialized
[Wed Dec 16 09:15:43 2015] INFO: Game Asset Manager assigned to Factory
[Wed Dec 16 09:15:43 2015] INFO: Game Asset Manager Loaded 194 Game Assets
[Wed Dec 16 09:15:43 2015] INFO: Game logic successfully initialized
[Wed Dec 16 09:15:43 2015] INFO: Game can be started
[Wed Dec 16 09:15:43 2015] ERROR: Could not find resource UI/Fonts/scarabeo.ttf
[Wed Dec 16 09:15:43 2015] ERROR: Null font for Text
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorActions.as:806,5 Compiling void ApplyUIElementStyleAction::ApplyStyle(const String&in)
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorActions.as:824,28 Variable 'element' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorHierarchyWindow.as:1047,1 Compiling Node@[] GetMultipleSourceNodes(UIElement@)
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorHierarchyWindow.as:1083,27 Variable 'node' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorView.as:1205,1 Compiling void UpdateView(float)
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorView.as:1438,35 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/AttributeEditor.as:301,1 Compiling UIElement@ CreateIntAttributeEditor(ListView@, Serializable@[]@, const AttributeInfo&in, uint, uint)
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:317,48 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:317,48 Implicit conversion changed sign of value
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/AttributeEditor.as:624,1 Compiling void LoadAttributeEditor(UIElement@, const Variant&in, const AttributeInfo&in, bool, bool, const Variant[]&in)
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:680,37 Variable 'refList' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:702,18 Variable 'sameValue' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:708,33 Variable 'vector' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:711,29 Variable 'value' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:721,27 Variable 'info' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:742,18 Variable 'sameValue' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:748,28 Variable 'map' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:751,29 Variable 'value' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:761,27 Variable 'info' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:771,21 Variable 'value' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:781,20 Variable 'value' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/AttributeEditor.as:800,1 Compiling void StoreAttributeEditor(UIElement@, Serializable@[]@, uint, uint, uint)
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:834,24 Variable 'map' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/AttributeEditor.as:869,1 Compiling void GetEditorValue(UIElement@, VariantType, String[]@, uint, Variant[]&inout)
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:880,19 Variable 'attrEdit' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:903,27 Variable 'attrEdit' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/AttributeEditor.as:909,19 Variable 'attrEdit' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorCubeCapture.as:12,1 Compiling void PrepareZonesForCubeRendering()
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorCubeCapture.as:19,23 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorCubeCapture.as:55,1 Compiling void UnprepareZonesForCubeRendering()
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorCubeCapture.as:58,23 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorCubeCapture.as:63,23 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorScene.as:260,1 Compiling bool SaveEngineSTDScene(const String&in)
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorScene.as:333,21 Variable 'attributePosition' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorScene.as:334,24 Variable 'attributeRotation' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorScene.as:335,21 Variable 'attributeScale' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorScene.as:1450,1 Compiling bool SceneRenderZoneCubemaps()
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorScene.as:1456,23 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorScene.as:1459,27 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorScene.as:1470,23 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorUI.as:1942,1 Compiling void HandleWheelChangeColor(StringHash, VariantMap&inout)
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorUI.as:1944,39 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorResourceBrowser.as:229,1 Compiling void CreateResourceFilterUI()
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorResourceBrowser.as:251,23 Float value truncated in implicit conversion to integer
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorResourceBrowser.as:257,15 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorLayers.as:149,1 Compiling void ChangeNodeViewMask(Node@, EditActionGroup@, int)
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorLayers.as:154,53 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorLayers.as:185,1 Compiling void EstablishBitMaskToSelectedNodes()
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorLayers.as:194,39 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorLayers.as:212,34 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorColorWheel.as:147,1 Compiling void HandleWheelButtons(StringHash, VariantMap&inout)
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorColorWheel.as:155,20 Variable 'eventData' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorColorWheel.as:163,20 Variable 'eventData' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorColorWheel.as:171,20 Variable 'eventData' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorColorWheel.as:212,1 Compiling void HandleColorWheelMouseWheel(StringHash, VariantMap&inout)
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorColorWheel.as:234,55 Float value truncated in implicit conversion to integer
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorColorWheel.as:243,1 Compiling void HandleColorWheelMouseMove(StringHash, VariantMap&inout)
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorColorWheel.as:276,14 Float value truncated in implicit conversion to integer
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorColorWheel.as:277,14 Float value truncated in implicit conversion to integer
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorColorWheel.as:288,33 Float value truncated in implicit conversion to integer
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorColorWheel.as:288,28 Float value truncated in implicit conversion to integer
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorColorWheel.as:329,59 Float value truncated in implicit conversion to integer
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorColorWheel.as:349,39 Float value truncated in implicit conversion to integer
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorColorWheel.as:403,1 Compiling void EstablishColorWheelUIFromColor(Color)
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorColorWheel.as:413,51 Float value truncated in implicit conversion to integer
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorColorWheel.as:417,31 Float value truncated in implicit conversion to integer
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorColorWheel.as:427,53 Float value truncated in implicit conversion to integer
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorColorWheel.as:427,44 Float value truncated in implicit conversion to integer
[Wed Dec 16 09:15:48 2015] INFO: Scripts/Editor/EditorViewDebugIcons.as:102,1 Compiling void UpdateViewDebugIcons()
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorViewDebugIcons.as:104,59 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorViewDebugIcons.as:134,86 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorViewDebugIcons.as:152,30 Signed/Unsigned mismatch
[Wed Dec 16 09:15:48 2015] WARNING: Scripts/Editor/EditorViewDebugIcons.as:174,48 Variable 'bb' hides another variable of same name in outer scope
[Wed Dec 16 09:15:48 2015] INFO: Compiled script module Scripts/Editor.as
[New Thread 0x7fffe8ff0700 (LWP 15147)]
[Wed Dec 16 09:15:48 2015] INFO: System started here
[Wed Dec 16 09:15:48 2015] WARNING: Localization::Get("Export scene to OBJ...") not found translation, language="en"
[Wed Dec 16 09:15:48 2015] WARNING: Localization::Get("Export selected to OBJ...") not found translation, language="en"
[Wed Dec 16 09:15:48 2015] WARNING: Localization::Get("Export scene to EngineStd...") not found translation, language="en"
[Wed Dec 16 09:15:48 2015] WARNING: Localization::Get("Reset transform") not found translation, language="en"
[Wed Dec 16 09:15:48 2015] WARNING: Localization::Get("Show components icons") not found translation, language="en"
[Wed Dec 16 09:15:48 2015] WARNING: Localization::Get("Render Zone Cubemap") not found translation, language="en"
[Wed Dec 16 09:15:48 2015] WARNING: Localization::Get("Game Asset") not found translation, language="en"
[Wed Dec 16 09:15:52 2015] INFO: Game logic life time is - 0.00249347 hours 0.149608 minutes 8.97651 seconds
[Thread 0x7fffe9c01700 (LWP 15146) exited]
[Thread 0x7fffea402700 (LWP 15145) exited]
[Thread 0x7ffff1d1e700 (LWP 15143) exited]
[Thread 0x7ffff151d700 (LWP 15144) exited]
[Thread 0x7ffff251f700 (LWP 15142) exited]
[Thread 0x7fffe8ff0700 (LWP 15147) exited]

Program received signal SIGSEGV, Segmentation fault.
0x00000000007480c4 in Urho3D::RefCounted::ReleaseRef() ()
(gdb) d.github.io/
[/code]

Vivienne

-------------------------

Enhex | 2017-01-02 01:08:47 UTC | #2

I know that in my project I had problems with AS keeping external objects alive with it's ref counting.
By external objects I mean objects which were created outside the AS script.

To solve that problem you need to use weak handles in AS.

-------------------------

vivienneanthony | 2017-01-02 01:09:02 UTC | #3

[quote="Enhex"]I know that in my project I had problems with AS keeping external objects alive with it's ref counting.
By external objects I mean objects which were created outside the AS script.

To solve that problem you need to use weak handles in AS.[/quote]

Thanks. We decided to use Scorvi IDE and porting that into the engine/game we are doing instead of Player/Scripting.

We are having some issues with some code relating to attributes but I am not sure if it's because the original is based on pre-1.4 code. It looks like some access violation or memory leak.

[i.imgur.com/MRGuZpZ.png](http://i.imgur.com/MRGuZpZ.png)

Crashes a lot selecting menus or hierarchy items (relating to some attribute code) and some reason mouse doesn't work with the camera like typical

-------------------------

