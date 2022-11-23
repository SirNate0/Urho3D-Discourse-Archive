George1 | 2017-06-02 13:32:13 UTC | #1

Hi, It seems like the Asset Importer from the editor is broken in current build in Github.
I tried to import model from the editor and get this error.

ERROR: Failed to execute AssetImporter to import model.

AssetImporter.exe existed inside the tool folder.

-------------------------

weitjong | 2017-06-02 16:36:20 UTC | #2

What is your build options and build configuration?

-------------------------

George1 | 2017-06-03 04:06:41 UTC | #3

I used CMake 3.4.3 like I did before. I configure using the default option with static library for visual studio 2015.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/c4d3cf19f961648c1a91f97b5311b962332612dd.png" width="166" height="500">

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/d5870e9e6e790615915823ce199f93ac6871e91d.png" width="234" height="500">

The Urho library engine runs find. Just the editor having that AssetImporter error.

Regards

-------------------------

weitjong | 2017-06-03 04:31:02 UTC | #4

That is only the build options. How about the build configuration? Did you use Release build config or Debug build config? On Windows platform the Debug build config generates binaries with "_d" suffix. However, the Editor script currently always expects to find the Release-built "AssetImporter.exe". If that is indeed your issue then you could raise it as an issue in our GitHub issue tracker.

-------------------------

George1 | 2017-06-03 04:32:21 UTC | #5

[quote="weitjong, post:4, topic:3191"]
se Release build
[/quote]

Hi Weitjong, thanks I only build using debug in visual studio. I will build using release option, when I get access to my PC tonight.

Thanks mate

-------------------------

