vivienneanthony | 2017-01-02 01:05:09 UTC | #1

Hi

So I got 1.4 to compile along with the code I made. The old version I have a folder /Resources under /Bin where I add all the things I made. It's there any way to force the compile and build to use "/CoreData" and secondly "/Resources" instead of "/Data"

Vivienne

-------------------------

thebluefish | 2017-01-02 01:05:09 UTC | #2

[code]engineParameters["ResourcePaths"] = "CoreData;Resources";[/code]
or
[code]engineParameters["ResourcePaths"] = "CoreData;Data;Resources";[/code]

-------------------------

vivienneanthony | 2017-01-02 01:05:10 UTC | #3

Find it. Cool. THanks.

-------------------------

