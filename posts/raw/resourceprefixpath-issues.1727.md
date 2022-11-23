thebluefish | 2017-01-02 01:09:44 UTC | #1

I've been having issues since I've upgraded to Urho3D 1.5 last month. I'm still seeing these issues with the latest unstable.

My directory structure is as follows:

[code]
C:/Projects/bin/Debug
| Test.exe
| Data/
|| CoreData
|| Data
|| GameData
[/code]

My setup:
[code]
engineParameters_["ResourcePaths"] = configManager->GetString("engine", "ResourcePaths", "Data;CoreData;GameData");
engineParameters_["ResourcePrefixPath"] = configManager->GetString("engine", "ResourcePrefixPath", "Data");
[/code]

My log output:
[code]
[Fri Jan 29 10:00:38 2016] INFO: Added resource path C:/Projects/bin/Debug/Data/
[Fri Jan 29 10:00:38 2016] ERROR: Failed to add resource path 'CoreData', check the documentation on how to set the 'resource prefix path'
[/code]

AFAIK this should be correct. I went to C:/Projects/bin/Debug/Data/ and verified the folders are there. However my game can only find the ResourcePaths when they're in the same folder as the executable. How can I get this working?

-------------------------

weitjong | 2017-01-02 01:09:45 UTC | #2

It is not clear what your "configManager->GetString()" does in your post. Could you just for testing, isolate the problem by temporarily hard-coding a path to your resources and see whether it works? You can also test it by overriding the resource prefix path using "-pp" command line option.

-------------------------

thebluefish | 2017-01-02 01:09:45 UTC | #3

[quote="weitjong"]It is not clear what your "configManager->GetString()" does in your post.[/quote]

It get's the value from my config file, or returns the default (last parameter). In this case, it is functionally equivalent to:

[code]
engineParameters_["ResourcePaths"] = "Data;CoreData;GameData";
[/code]

The log file is showing that it is pointing to the correct location.

[quote="weitjong"]Could you just for testing, isolate the problem by temporarily hard-coding a path to your resources and see whether it works?[/quote]

[code]engineParameters_["ResourcePaths"] = "Data;CoreData;GameData";
engineParameters_["ResourcePrefixPath"] = "D:\_Projects\blu\_bin\Debug\Data";[/code]

[code]
[Fri Jan 29 21:32:00 2016] INFO: Added resource path D:/_Projects/blu/_bin/Debug/Data/
[Fri Jan 29 21:32:00 2016] ERROR: Failed to add resource path 'CoreData', check the documentation on how to set the 'resource prefix path'
[/code]

I ensured the files were in that path. Still nada. This is on latest build from master.

[quote="weitjong"]You can also test it by overriding the resource prefix path using "-pp" command line option.[/quote]

Nada.

-------------------------

thebluefish | 2017-01-02 01:09:45 UTC | #4

So as it turns out, [u]ResourcePrefixPath[/u] turned into [u]ResourcePrefixPaths[/u] between 1.4 and 1.5.

-------------------------

weitjong | 2017-01-02 01:09:46 UTC | #5

Ah yes. It was refactored to now accept a list of paths instead of just a single path, so the parameter got renamed also to reflect this change. The list should be a semicolon separated search paths, i.e. the default or the most preferred path where the resources could be found should be listed first. In other words, you could have "Data", "CoreData", and "GameData" in separate paths if you want to.

-------------------------

