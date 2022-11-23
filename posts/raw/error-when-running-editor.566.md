rogerdv | 2017-01-02 01:01:24 UTC | #1

I pulled yesterday and today, but havent had time to run the editor,. so I compiled in both Linux and Windows and found a weird problem when running the editor:

[code][Tue Nov 18 15:02:31 2014] ERROR: Scripts/Editor/EditorSettings.as:44,5 - Exception 'Null pointer access' in 'void UpdateEditorSettingsDialog()'
AngelScript callstack:
	Scripts/Editor/EditorSettings.as:void UpdateEditorSettingsDialog():44,5
	Scripts/Editor/EditorSettings.as:void CreateEditorSettingsDialog():16,5
	Scripts/Editor/EditorUI.as:void CreateUI():75,5
	Scripts/Editor.as:void FirstFrame():62,5
[/code]

The editor runs, but Hierarchy and Attribute windows are not visible. Should I open an issue for this?

-------------------------

alexrass | 2017-01-02 01:01:24 UTC | #2

also editor crash if build with URHO3D_URHO2D=0

[code]
[Wed Nov 19 00:16:16 2014] ERROR: Scripts/Editor/EditorHierarchyWindow.as:878,21 Identifier 'ParticleEffect2D' is not a data type
[Wed Nov 19 00:16:16 2014] ERROR: Scripts/Editor/EditorHierarchyWindow.as:882,21 Identifier 'ParticleEmitter2D' is not a data type
[Wed Nov 19 00:16:17 2014] ERROR: Failed to compile script module Scripts/Editor.as
[/code]

Upd:
If normal build works normal...

-------------------------

cadaver | 2017-01-02 01:01:24 UTC | #3

The editor will not be resilient to disabling significant Urho functionality, like Urho2D (or Physics too, I'd suspect)

I recommend to nuke your build directory and do a full rebuild. If the editor still doesn't run, then open an issue.

-------------------------

alexrass | 2017-01-02 01:01:24 UTC | #4

Full build for develop, customized build for release )

-------------------------

rogerdv | 2017-01-02 01:01:24 UTC | #5

I already deleted build directory and recompiled all with my usual features (lua and samples, which for some reason, are built here, but not at my home PC).

-------------------------

