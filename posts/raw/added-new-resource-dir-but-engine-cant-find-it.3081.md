smellymumbler | 2017-04-30 23:13:16 UTC | #1

I've used the following example to create a new project, instead of my old stuff:
http://urho3d.wikia.com/wiki/First_Project

I'm trying to get things more standardized and using CMake and everything. Unfortunately, this new system can't detect my custom data folder. 

```
engineParameters_["ResourcePaths"] = "GameData;Data;CoreData";
```

I keep getting `Failed to add resource path 'GameData', check the documentation on how to set the 'resource prefix path'`. Am i missing something? The data folders are inside the `bin` folder of my project, at the same level as the executable.

-------------------------

Victor | 2017-04-30 23:25:35 UTC | #2

You may need to ensure your prefix path is also setup properly.

    engineParameters_[EP_RESOURCE_PREFIX_PATHS] = "../../Contents;../../Base/path/to/gamedata;"
    engineParameters_[EP_RESOURCE_PATHS] = "CoreData;Data;GameData;";

So you might store CoreData and Data in /Contents, while GameData is stored in the second path for prefix paths.

-------------------------

smellymumbler | 2017-04-30 23:46:18 UTC | #3

That didn't solve the issue. However, i've downloaded the newest Urho3D version and i've noticed that the CMake thing has changed. I was using the old `Urho3D-CMake-common` and now i'm using `UrhoCommon` and `define_resource_dirs`. Worked like a charm.

-------------------------

Victor | 2017-05-01 00:16:16 UTC | #4

Ah, sorry that didn't help, but I'm glad you figured out the solution :)

Edit: When you say you downloaded the latest version, do you mean from the site, or that you pulled the latest changes from the master branch? Just curious, as I'm probably a few commits behind from the latest changes on the master branch and I'm now wondering if there has been some major changes with how resources directories are setup.

-------------------------

smellymumbler | 2017-05-01 00:34:32 UTC | #5

I'm using the latest master.

-------------------------

weitjong | 2017-05-01 01:31:48 UTC | #6

The setup is largely the same. The new define_resource_dirs() macro merely just capitalizes the existing flexibility of the Urho3D engine in setting up the resources.

-------------------------

Victor | 2017-05-01 01:54:58 UTC | #7

I see, thanks for explaining that! I'll update my branch later tonight to ensure I have everything properly setup on my end.

-------------------------

