Avagrande | 2020-06-10 05:36:30 UTC | #1

Hello.

I am looking into packaging but I find that documentation for it is rather scarce.

If I create a package out of say the Data folder and then bind it, will that create a a true read only filesystem such that I can iterate the contents of the directory using ScanDir? 

I use file structure to automatically bind scripts and other assets for the purposes of modding and ease of use, so you can do things like introduce a new entity by simply creating a appropriately named file and folder.  This makes modding really easy but I am not sure if this would be compatible with package structures.

I haven't tried yet to implement it so I am asking just in case someone else has experience with it. 

tl;dr : How do packages work and what are their limitations?

-------------------------

Eugene | 2020-06-10 10:33:33 UTC | #2

[quote="Avagrande, post:1, topic:6198"]
tl;dr : How do packages work and what are their limitations?
[/quote]

Packages don't interact with Filesystem in any way.
Package support and abstraction is implemented at the level of ResourceCache.
I'm not aware of any mechanism that allows to iterate resources without knowing their names thru ResourceCache.
Although, there's no physical limitation for implementing it... at the level of ResourceCache, of course.

-------------------------

Avagrande | 2020-06-10 10:34:22 UTC | #3

Thanks.  
I guess I will have to implement my own package format.

-------------------------

dertom | 2020-06-10 13:43:08 UTC | #4

Without ever using it, but you might want a look to this:
https://icculus.org/physfs/

-------------------------

Miegamicis | 2020-06-10 14:01:11 UTC | #5

You can iterate trough the package entries with the following code:

```
auto packageFiles = GetSubsystem<ResourceCache>()->GetPackageFiles();
for (auto it = packageFiles.Begin(); it != packageFiles.End(); ++it) {
    auto files = (*it)->GetEntryNames();
    for (auto it2 = files.Begin(); it2 != files.End(); ++it2) {
        if ((*it2).EndsWith(".as")) {
           //This is an AngelScript file in a package
           // (*it2) is a string with the full file path like Scripts/Sample.as
        }
    }
}
```

But you can't add new files to an existing package as far as I know.

-------------------------

Avagrande | 2020-06-10 20:52:07 UTC | #6

Oh thats nice! from the looks of it, its possible to create a index from packages which means I could then integrate it with the filesystem not just the cache.  

My goal is to make a package that mimics filesystem without Write or rather when you write it writes on disk in the same location.
so if I ScanDir in "Scripts/" and I have "Scripts/OnDisk.lua" in the hdd and then "Scripts/InPkg.lua" in the PKG, the ScanDir function should return both files. 

However if I write to "Scripts/InPkg.lua" that will create a file on the actual filesystem ( hdd ) and not the pkg, but when I then run ScanDir I will still have two files and the one in PKG will be ignored.

The filesystem will prefer the InPkg.lua from the filesystem instead of the pkg.
Although I will probably want to give some control to the priority list such that I can prefer one package over the other or in some instances prefer pkg over filesystem. 

The benefit of this would be that players can exchange mods in .pkg format and easily remove or add them without the need to unzip anything and that my filesystem controls remain the same. Even if I try to write to a file thats in the pkg it will just write it to the hdd and therefore "overwrite" it as far as priority is concerned.  Therefore making somewhat of a virtual extension to the filesystem. 


I previously worked on Love2D  ( which uses PhysicsFS ) before moving to Urho3D, One key issue with PhysicsFS is that it applies strict limitations making something like a file browser next to impossible to do. If you are making a editor for example or something that needs to access files on disk it will be a pain since you might need to write all the operations yourself for each OS.

I think the way the package system is now its possible to create the behaviour I need, so I will have a ago.

-------------------------

