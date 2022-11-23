mrchrissross | 2018-11-09 19:53:00 UTC | #1

Hi Everyone,

All of a sudden I'm getting this LNK error on my home computer: 

    Severity	Code	Description	Project	File	Line	Suppression State
    Error	LNK1104	cannot open file 'C:\Users\Chris Ross\Documents\GitHub\Urho3DProject\Project\Build\bin\UrhoProject_d.exe'	UrhoProject	C:\Users\Chris Ross\Documents\GitHub\Urho3DProject\Project\Build\LINK	1

I've built the same game on another few PC but they work perfectly it only doesnt work on my PC :frowning:

Any help with this issue would be fantastic

-------------------------

S.L.C | 2018-11-09 21:14:37 UTC | #2

Is the file locked from being overwritten? Like being opened, locked/scanned by an AV or simply not having the permissions to write to it in that particular location. Try to delete it manually and see what happens.

And last but not least. Check if the executable is actually there. Maybe the path was configured incorrectly or something related to this kind of issue. Like the executable being created somewhere else and expected to be in that place. Where it obviously can't be found.

-------------------------

