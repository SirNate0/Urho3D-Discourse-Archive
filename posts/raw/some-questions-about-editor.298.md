att | 2017-01-02 00:59:28 UTC | #1

Hi, 
The editor seems included the path of engine Bin/Data, although I had set other path.
 So some models can not added to the scene successfully if they have the same name.

-------------------------

cadaver | 2017-01-02 00:59:28 UTC | #2

Yes, it's true that the editor never removes the builtin data dirs from the resource system (Bin/CoreData, Bin/Data) so if you have similar named resources in your own resource path it will conflict. 

For now you can workaround this by cleaning up unnecessary or conflicting files from Bin/Data.

-------------------------

alexrass | 2017-01-02 00:59:28 UTC | #3

Then add you directory, set priority:
[quote]void 	AddPackageFile (PackageFile *package, unsigned int priority=PRIORITY_LAST)
 	Add a package file for loading resources from. Optional priority parameter which will control search order. 
bool 	AddResourceDir (const String &pathName, unsigned int priority=PRIORITY_LAST)
 	Add a resource load directory. Optional priority parameter which will control search order. [/quote]


Sorry, did I misread the question.

-------------------------

cadaver | 2017-01-02 00:59:28 UTC | #4

Yes, the editor could be changed to do that, at the risk of "inverting" the problem; the user's resources could override whatever the editor needs to load from its own data directory. However I don't think that's much of a problem, as it already loads at startup most of what it needs.

-------------------------

friesencr | 2017-01-02 00:59:28 UTC | #5

I am kind of thinking configuration is my next area of attack for the editor.

-------------------------

