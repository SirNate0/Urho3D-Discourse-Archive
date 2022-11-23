fancypantsorama | 2017-06-03 00:33:10 UTC | #1

So
1. git clone /URHO3d-master

2. git clone/URHO3d

3. Put all adjustments to source in Urho3d-master
4. Build Urho3d

Question what dependency, pathing, library or source file when editor.bat is run in /urho3d uses my source from urho3d-master/bin/data/scripts/editor/editorscripts.as

Hope this helps

-------------------------

hdunderscore | 2017-06-04 00:23:27 UTC | #2

Are you suggesting there is an issue where the URHO3d directory is building from URHO3d-master source, or are you asking how to make that happen?

-------------------------

cadaver | 2017-06-04 11:20:56 UTC | #3

One thing that didn't come to mind during the prior email conversation, which may be related. The editor remembers the resource directory that you used last for scene editing, and attached it to the resource system after it has started. Though I don't think that should affect the script loading on startup, since all scripts are loaded first before the editor runs.

In any case, on Windows the editor config is inside C:\Users\username\AppData\Roaming\urho3d\Editor . Delete the Config.xml file and the editor shouldn't remember any old directory now.

-------------------------

