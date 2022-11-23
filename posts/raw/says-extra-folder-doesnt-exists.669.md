ghidra | 2017-01-02 01:02:00 UTC | #1

Per suggestion, I've linked some of my folders into the /Bin/Extra folder. But the urho player when run gives me an errors, that it doesnt exist:

[code]
INFO: Added resource path /home/projects/urho/Urho3D/Bin/Data/
INFO: Added resource path /home/projects/urho/Urho3D/Bin/CoreData/
WARNING: Skipped autoload folder Extra as it does not exist
[/code]

It's there along with the CoreData and the Data folder.

-------------------------

cadaver | 2017-01-02 01:02:02 UTC | #2

There was a bug where the Engine would not append the executable's base path correctly, which would result in that error if you were eg. running from debugger and the working directory was not set the same as the executable's directory. Should be fixed now in the master branch.

Note that the Extra directory itself is not directly added as a resource path, but if it contains packages or subdirectories, they will be added.

-------------------------

weitjong | 2017-01-02 01:02:02 UTC | #3

That bug has been fixed in the "buildsystem" topic branch. I just want to add that in the branch I have taken the liberty of changing the AutoloadPaths parameter default value from "Extra" to "Autoload" because I think the latter is clearer. If you plan to use this feature, please be reminded to double check the default parameter value again when the "buildsystem" topic branch get merged into master branch later.

-------------------------

