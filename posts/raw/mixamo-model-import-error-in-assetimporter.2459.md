Lumak | 2017-01-02 01:15:32 UTC | #1

Anyone ever come across an error shown below?
[code]Could not open or parse input file <somemixamomodel.fbx>: invalid vector<T> subscript[/code]

There is a fix that I can provide forcing fbxconverter to skip processing animation on model import. I'll submit a PR if it's in demand.

-------------------------

rasteron | 2017-01-02 01:15:32 UTC | #2

Hey Lumak,

have you tried converting your FBX to 2013 version before converting with Assimp? You can also try exporting it with Blender.

-------------------------

Lumak | 2017-01-02 01:15:32 UTC | #3

I don't use Blender but do convert them to fbx 2013 version.

I was able to reproduce this error even when retargeting animations and discovered how to solve this problem.  If you see this error just add animation key to the "Hips" joint on the 1st frame and it'll solve it.  No importer code changes required.

-------------------------

rasteron | 2017-01-02 01:15:32 UTC | #4

Ah ok got it thanks.

-------------------------

