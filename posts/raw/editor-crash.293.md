att | 2017-01-02 00:59:26 UTC | #1

Hi, 
I updated the latested code, and the editor crash

this is the error,
[Fri Jun  6 10:32:51 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

-------------------------

friesencr | 2017-01-02 00:59:26 UTC | #2

Is there anything else in the log?   I recently added a good chunk of code so its probable that I broke it.  What platform are you using?

-------------------------

rasteron | 2017-01-02 00:59:26 UTC | #3

Yep, confirmed. For me, I'm getting a blank screen when I run the editor..

-------------------------

att | 2017-01-02 00:59:26 UTC | #4

This is the Urho3D.log
[code][Sat May 17 14:31:34 2014] INFO: Opened log file Urho3D.log
[Sat May 17 14:31:34 2014] INFO: Created 1 worker thread
[Sat May 17 14:31:34 2014] INFO: Added resource path /Users/mini/Work/self/Urho3D/Bin/CoreData/
[Sat May 17 14:31:34 2014] INFO: Added resource path /Users/mini/Work/self/Urho3D/Bin/Data/
[Sat May 17 14:31:34 2014] WARNING: Skipped autoload folder Extra as it does not exist
[Sat May 17 14:31:34 2014] INFO: Set screen mode 1920x987 windowed resizable
[Sat May 17 14:31:34 2014] INFO: Initialized input
[Sat May 17 14:31:34 2014] INFO: Initialized user interface
[Sat May 17 14:31:34 2014] DEBUG: Loading resource Textures/Ramp.png
[Sat May 17 14:31:34 2014] DEBUG: Loading resource Textures/Ramp.xml
[Sat May 17 14:31:34 2014] DEBUG: Loading resource Textures/Spot.png
[Sat May 17 14:31:34 2014] DEBUG: Loading resource Textures/Spot.xml
[Sat May 17 14:31:34 2014] DEBUG: Loading resource Techniques/NoTexture.xml
[Sat May 17 14:31:34 2014] DEBUG: Loading resource RenderPaths/Forward.xml
[Sat May 17 14:31:34 2014] INFO: Initialized renderer
[Sat May 17 14:31:34 2014] INFO: Set audio mode 44100 Hz stereo interpolated
[Sat May 17 14:31:34 2014] DEBUG: Loading resource UI/MessageBox.xml
[Sat May 17 14:31:34 2014] DEBUG: Loading UI layout UI/MessageBox.xml
[Sat May 17 14:31:35 2014] DEBUG: Loading resource Scripts/Editor.as
[Sat May 17 14:31:35 2014] INFO: Compiled script module Scripts/Editor.as
[Sat May 17 14:31:35 2014] DEBUG: Started watching path /Users/mini/Work/self/Urho3D/Bin/CoreData/
[Sat May 17 14:31:35 2014] DEBUG: Started watching path /Users/mini/Work/self/Urho3D/Bin/Data/
[Sat May 17 14:31:35 2014] DEBUG: Started watching path /Users/mini/Work/self/stickto60s/android-Build/assets/Data/
[Sat May 17 14:31:35 2014] INFO: Added resource path /Users/mini/Work/self/stickto60s/android-Build/assets/Data/
[Sat May 17 14:31:35 2014] DEBUG: Loading resource UI/DefaultStyle.xml
[Sat May 17 14:31:35 2014] DEBUG: Loading resource UI/EditorIcons.xml
[Sat May 17 14:31:35 2014] DEBUG: Loading resource Textures/UI.png
[Sat May 17 14:31:35 2014] DEBUG: Loading resource Textures/UI.png
[Sat May 17 14:31:35 2014] DEBUG: Loading resource Textures/UI.xml
[Sat May 17 14:31:35 2014] DEBUG: Loading resource Fonts/Anonymous Pro.ttf
[Sat May 17 14:31:35 2014] DEBUG: Font face Anonymous Pro (11pt) has 624 glyphs
[Sat May 17 14:31:35 2014] DEBUG: Loading resource Textures/Editor/EditorIcons.png
[Sat May 17 14:31:35 2014] DEBUG: Loading resource Textures/Editor/EditorIcons.xml
[Sat May 17 14:31:35 2014] DEBUG: Loading resource Textures/Logo.png
[Sat May 17 14:31:35 2014] DEBUG: Loading resource Textures/Logo.xml
[Sat May 17 14:31:35 2014] DEBUG: Loading resource Fonts/BlueHighway.ttf
[Sat May 17 14:31:35 2014] DEBUG: Font face BlueHighway (9pt) has 393 glyphs
[Sat May 17 14:31:36 2014] DEBUG: Loading resource UI/EditorQuickMenu.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading UI layout UI/EditorQuickMenu.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource UI/EditorHierarchyWindow.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading UI layout UI/EditorHierarchyWindow.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource UI/EditorInspector_Attribute.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource UI/EditorInspector_Variable.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource UI/EditorInspector_Style.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource UI/EditorInspectorWindow.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading UI layout UI/EditorInspectorWindow.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource UI/EditorSettingsDialog.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading UI layout UI/EditorSettingsDialog.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource UI/EditorPreferencesDialog.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading UI layout UI/EditorPreferencesDialog.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource UI/EditorMaterialWindow.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading UI layout UI/EditorMaterialWindow.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource Models/Sphere.mdl
[Sat May 17 14:31:36 2014] DEBUG: Loading resource UI/EditorSpawnWindow.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading UI layout UI/EditorSpawnWindow.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource UI/EditorViewport.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading UI layout UI/EditorViewport.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource Models/Editor/Axes.mdl
[Sat May 17 14:31:36 2014] DEBUG: Loading resource Materials/Editor/RedUnlit.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource Techniques/NoTextureOverlay.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource Materials/Editor/GreenUnlit.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource Materials/Editor/BlueUnlit.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource Materials/VColUnlit.xml
[Sat May 17 14:31:36 2014] DEBUG: Loading resource Techniques/NoTextureUnlitVCol.xml
[Sat May 17 14:31:36 2014] DEBUG: Reloading shaders
[Sat May 17 14:31:36 2014] DEBUG: Loading resource Shaders/GLSL/LitSolid.glsl
[Sat May 17 14:31:36 2014] DEBUG: Loading resource Shaders/GLSL/Unlit.glsl
[Sat May 17 14:31:36 2014] DEBUG: Compiled vertex shader Unlit(VERTEXCOLOR)
[Sat May 17 14:31:36 2014] DEBUG: Compiled pixel shader Unlit(VERTEXCOLOR)
[Sat May 17 14:31:36 2014] DEBUG: Linked vertex shader Unlit(VERTEXCOLOR) and pixel shader Unlit(VERTEXCOLOR)
[Sat May 17 14:31:36 2014] DEBUG: Compiled vertex shader LitSolid(DIRLIGHT PERPIXEL)
[Sat May 17 14:31:36 2014] DEBUG: Compiled pixel shader LitSolid(AMBIENT DIRLIGHT PERPIXEL)
[Sat May 17 14:31:36 2014] DEBUG: Linked vertex shader LitSolid(DIRLIGHT PERPIXEL) and pixel shader LitSolid(AMBIENT DIRLIGHT PERPIXEL)
[Sat May 17 14:31:36 2014] DEBUG: Loading resource Shaders/GLSL/Basic.glsl
[Sat May 17 14:31:36 2014] DEBUG: Compiled vertex shader Basic(DIFFMAP VERTEXCOLOR)
[Sat May 17 14:31:36 2014] DEBUG: Compiled pixel shader Basic(DIFFMAP VERTEXCOLOR)
[Sat May 17 14:31:36 2014] DEBUG: Linked vertex shader Basic(DIFFMAP VERTEXCOLOR) and pixel shader Basic(DIFFMAP VERTEXCOLOR)
[Sat May 17 14:31:36 2014] DEBUG: Compiled pixel shader Basic(ALPHAMAP VERTEXCOLOR)
[Sat May 17 14:31:36 2014] DEBUG: Linked vertex shader Basic(DIFFMAP VERTEXCOLOR) and pixel shader Basic(ALPHAMAP VERTEXCOLOR)
[Sat May 17 14:31:38 2014] DEBUG: Compiled pixel shader Basic(ALPHAMASK DIFFMAP VERTEXCOLOR)
[Sat May 17 14:31:38 2014] DEBUG: Linked vertex shader Basic(DIFFMAP VERTEXCOLOR) and pixel shader Basic(ALPHAMASK DIFFMAP VERTEXCOLOR)
[Sat May 17 14:31:42 2014] DEBUG: Compiled vertex shader Basic()
[Sat May 17 14:31:42 2014] DEBUG: Compiled pixel shader Basic()
[Sat May 17 14:31:42 2014] DEBUG: Linked vertex shader Basic() and pixel shader Basic()
[Sat May 17 14:31:42 2014] DEBUG: Compiled vertex shader Basic(VERTEXCOLOR)
[Sat May 17 14:31:42 2014] DEBUG: Compiled pixel shader Basic(VERTEXCOLOR)
[Sat May 17 14:31:42 2014] DEBUG: Linked vertex shader Basic(VERTEXCOLOR) and pixel shader Basic(VERTEXCOLOR)
[Sat May 17 14:31:59 2014] DEBUG: Loading resource Textures/HeightMap.png
[Sat May 17 14:32:01 2014] DEBUG: Compiled vertex shader LitSolid()
[Sat May 17 14:32:01 2014] DEBUG: Compiled pixel shader LitSolid()
[Sat May 17 14:32:01 2014] DEBUG: Linked vertex shader LitSolid() and pixel shader LitSolid()
[Sat May 17 14:32:10 2014] DEBUG: Loading resource Materials/Terrain.xml
[Sat May 17 14:32:10 2014] DEBUG: Loading resource Techniques/TerrainBlend.xml
[Sat May 17 14:32:10 2014] DEBUG: Loading resource Textures/TerrainWeights.dds
[Sat May 17 14:32:10 2014] DEBUG: Loading resource Textures/TerrainDetail1.dds
[Sat May 17 14:32:10 2014] DEBUG: Loading resource Textures/TerrainDetail2.dds
[Sat May 17 14:32:10 2014] DEBUG: Loading resource Textures/TerrainDetail3.dds
[Sat May 17 14:32:10 2014] DEBUG: Loading resource Shaders/GLSL/TerrainBlend.glsl
[Sat May 17 14:32:10 2014] DEBUG: Compiled vertex shader TerrainBlend()
[Sat May 17 14:32:10 2014] DEBUG: Compiled pixel shader TerrainBlend()
[Sat May 17 14:32:10 2014] DEBUG: Linked vertex shader TerrainBlend() and pixel shader TerrainBlend()
[Sat May 17 14:32:13 2014] DEBUG: Compiled vertex shader TerrainBlend(PERPIXEL POINTLIGHT)
[Sat May 17 14:32:13 2014] DEBUG: Compiled pixel shader TerrainBlend(AMBIENT PERPIXEL POINTLIGHT SPECULAR)
[Sat May 17 14:32:13 2014] DEBUG: Linked vertex shader TerrainBlend(PERPIXEL POINTLIGHT) and pixel shader TerrainBlend(AMBIENT PERPIXEL POINTLIGHT SPECULAR)
[Sat May 17 14:32:16 2014] DEBUG: Compiled vertex shader TerrainBlend(DIRLIGHT PERPIXEL)
[Sat May 17 14:32:16 2014] DEBUG: Compiled pixel shader TerrainBlend(AMBIENT DIRLIGHT PERPIXEL SPECULAR)
[Sat May 17 14:32:16 2014] DEBUG: Linked vertex shader TerrainBlend(DIRLIGHT PERPIXEL) and pixel shader TerrainBlend(AMBIENT DIRLIGHT PERPIXEL SPECULAR)
[Sat May 17 14:32:59 2014] DEBUG: Loading resource Materials/Editor/BrightGreenUnlit.xml
[Sat May 17 14:33:42 2014] DEBUG: Loading resource Materials/Editor/BrightRedUnlit.xml
[Sat May 17 14:33:48 2014] DEBUG: Loading resource Materials/Editor/BrightBlueUnlit.xml
[Sat May 17 14:36:57 2014] DEBUG: Set occlusion buffer size 256x132 with 5 mip levels
[Sat May 17 14:37:25 2014] DEBUG: Removed unused occlusion buffer
[Sat May 17 14:37:25 2014] DEBUG: Set occlusion buffer size 256x132 with 5 mip levels
[Sat May 17 14:38:19 2014] DEBUG: Removed unused occlusion buffer
[Sat May 17 14:38:19 2014] DEBUG: Set occlusion buffer size 256x132 with 5 mip levels
[Sat May 17 14:38:50 2014] DEBUG: Removed unused occlusion buffer
[Sat May 17 14:38:55 2014] DEBUG: Set occlusion buffer size 256x132 with 5 mip levels
[Sat May 17 14:39:02 2014] DEBUG: Removed unused occlusion buffer
[Sat May 17 14:39:03 2014] DEBUG: Set occlusion buffer size 256x132 with 5 mip levels
[Sat May 17 14:39:26 2014] DEBUG: Removed unused occlusion buffer
[Sat May 17 14:39:47 2014] DEBUG: Set occlusion buffer size 256x132 with 5 mip levels
[Sat May 17 14:42:24 2014] DEBUG: Removed unused occlusion buffer
[Sat May 17 14:48:08 2014] DEBUG: Loading resource UI/MessageBox.xml
[Sat May 17 14:48:08 2014] DEBUG: Loading UI layout UI/MessageBox.xml
[Sat May 17 14:48:10 2014] DEBUG: Created directory /Users/mini/.Urho3D/
[Sat May 17 14:48:10 2014] DEBUG: Created directory /Users/mini/.Urho3D/Editor/
 [/code]

this is the terminal output 
[code][Fri Jun  6 17:15:19 2014] INFO: Opened log file /Users/mini/Library/Application Support/urho3d/logs/Editor.as.log
[Fri Jun  6 17:15:19 2014] INFO: Created 1 worker thread
[Fri Jun  6 17:15:19 2014] INFO: Added resource path /Users/mini/Work/self/Urho3D/Bin/CoreData/
[Fri Jun  6 17:15:19 2014] INFO: Added resource path /Users/mini/Work/self/Urho3D/Bin/Data/
[Fri Jun  6 17:15:19 2014] WARNING: Skipped autoload folder Extra as it does not exist
[Fri Jun  6 17:15:20 2014] INFO: Set screen mode 1920x987 windowed resizable
[Fri Jun  6 17:15:20 2014] INFO: Initialized input
[Fri Jun  6 17:15:20 2014] INFO: Initialized user interface
[Fri Jun  6 17:15:20 2014] DEBUG: Loading resource Textures/Ramp.png
[Fri Jun  6 17:15:20 2014] DEBUG: Loading resource Textures/Ramp.xml
[Fri Jun  6 17:15:20 2014] DEBUG: Loading resource Textures/Spot.png
[Fri Jun  6 17:15:20 2014] DEBUG: Loading resource Textures/Spot.xml
[Fri Jun  6 17:15:20 2014] DEBUG: Loading resource Techniques/NoTexture.xml
[Fri Jun  6 17:15:20 2014] DEBUG: Loading resource RenderPaths/Forward.xml
[Fri Jun  6 17:15:20 2014] INFO: Initialized renderer
[Fri Jun  6 17:15:20 2014] INFO: Set audio mode 44100 Hz stereo interpolated
[Fri Jun  6 17:15:20 2014] DEBUG: Loading resource UI/MessageBox.xml
[Fri Jun  6 17:15:20 2014] DEBUG: Loading UI layout UI/MessageBox.xml
[Fri Jun  6 17:15:20 2014] DEBUG: Loading resource Scripts/Editor.as
[Fri Jun  6 17:15:21 2014] INFO: Compiled script module Scripts/Editor.as
[Fri Jun  6 17:15:21 2014] DEBUG: Started watching path /Users/mini/Work/self/Urho3D/Bin/CoreData/
[Fri Jun  6 17:15:21 2014] DEBUG: Started watching path /Users/mini/Work/self/Urho3D/Bin/Data/
[Fri Jun  6 17:15:21 2014] DEBUG: Started watching path /Users/mini/Work/self/minecraftwarflappybird3d/android-Build/assets/Data/
[Fri Jun  6 17:15:21 2014] INFO: Added resource path /Users/mini/Work/self/minecraftwarflappybird3d/android-Build/assets/Data/
[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:504,5 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void PopulateBrowserDirectories():504,5
	Scripts/Editor/EditorResourceBrowser.as:void RebuildResourceDatabase():121,5
	Scripts/Editor/EditorScene.as:void SetResourcePath(String, bool = true, bool = false):140,5
	Scripts/Editor.as:void LoadConfig():162,17
	Scripts/Editor.as:void Start():55,5

[Fri Jun  6 17:15:21 2014] DEBUG: Loading resource RenderPaths/Prepass.xml
[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] DEBUG: Reloading shaders
[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in '- Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in '- Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in '- Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in '- Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] DEBUG: Loading resource UI/ScreenJoystick.xml
[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] DEBUG: Loading resource UI/ScreenJoystickSettings.xml
[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in '- Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in '- Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in '
[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in '- Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in '- Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in '- Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in '' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:21 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:162,9 - Exception 'Null pointer access' in 'void DoResourceBrowserWork()'
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():162,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorResourceBrowser.as:164,9 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorResourceBrowser.as:void DoResourceBrowserWork():164,9
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):95,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in '- Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in '- Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in '- Exception 'Null pointer access' in ''
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5

[Fri Jun  6 17:15:22 2014] ERROR: Scripts/Editor/EditorView.as:1062,5 - Exception 'Null pointer access' in 'void UpdateStats(float)'
AngelScript callstack:
	Scripts/Editor/EditorView.as:void UpdateStats(float):1062,5
	Scripts/Editor.as:void HandleUpdate(StringHash, VariantMap&inout):98,5
[/code]

[quote="friesencr"]Is there anything else in the log?   I recently added a good chunk of code so its probable that I broke it.  What platform are you using?[/quote]

-------------------------

att | 2017-01-02 00:59:26 UTC | #5

[quote="friesencr"]Is there anything else in the log?   I recently added a good chunk of code so its probable that I broke it.  What platform are you using?[/quote]

I tested it on mac book pro.

-------------------------

friesencr | 2017-01-02 00:59:26 UTC | #6

There was a load order I wasn't accounting for.  Give it a try now.  Sorry for the bug.

-------------------------

rasteron | 2017-01-02 00:59:27 UTC | #7

works now Chris, thanks for the update!  :slight_smile:

-------------------------

