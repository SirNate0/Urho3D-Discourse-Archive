Deveiss | 2017-01-02 01:07:09 UTC | #1

I'm using a relatively simple program with only a few resources, so I've compiled everything into a single Data folder, ignoring CoreData. In my Setup function, I call:

[code]engineParameters_["ResourcePaths"] = "Data";[/code]

I copied the entire project and set it up for Android in the new directory. I'm using, for the most part, the same Java files that come as samples, only changing the package name. Soon I'd like to ditch the useless intent entierly, as there is only the one library. The APK compiles fine, and I'm able to use "ant installd" to move it to my phone for testing. However, upon running it, the app "opens" for a split second and then crashes back to the home screen. It's not an actual exception crash, but the engine stops itself. Examining the logcat shows this line:

[code]E/Urho3D  (29718):  Failed to add resource path 'Data', check the documentation on how to set the 'resource prefix path'[/code]

I can plainly see the Data folder within the APK if I open it as an archive, it's in the assets/ directory, as it is within the projects plain file system. So why can Android not find it if it's provided within the APK? Is there some other step I'm missing out on?

-------------------------

rasteron | 2017-01-02 01:07:09 UTC | #2

Assuming that you have a correct path there then I'm not entirely sure with this finding or if it is related but I think if you ditched the CoreData folder, you might ran into some issues with Android as it is hardwired to the build process. I reported this issue here:

[github.com/urho3d/Urho3D/issues/809](https://github.com/urho3d/Urho3D/issues/809)

For starters, just pack what you only need but try to have or maintain both Data and CoreData folder just to be sure.

-------------------------

Deveiss | 2017-01-02 01:07:09 UTC | #3

I have added both CoreData and Data, however the application continues to crash. It only says that Data isn't found, so I tried using just CoreData and then it said that CoreData wasn't found. I checked the code for acquiring the resource paths, it checks them one at a time and crashes at the first to fail, so Data is just being checked first.

As of right now, it still stands that the application crashes when I attempt to open it, with this error message in the system logs:
[code]E/Urho3D  (15264):  Failed to add resource path 'Data', check the documentation on how to set the 'resource prefix path'[/code]

-------------------------

weitjong | 2017-01-02 01:07:09 UTC | #4

Are you using the latest revision from master branch or release 1.4? There is recent changes in the Android's asset directory handling in our master branch. If you use the latest revision then you have to ensure your Android build tree has a custom Ant task properly setup. When in doubt, just run the cmake_android.sh or cmake_android.bat one more time to reconfigure your existing build tree.

-------------------------

Deveiss | 2017-01-02 01:07:09 UTC | #5

[quote="weitjong"]Are you using the latest revision from master branch or release 1.4?[/quote]
I was about to say 1.4, because that's what I developed on, specifically to avoid these bleeding edge issues. However I just remembered, when I cloned Urho into a secondary directory for the Android build, I forgot to checkout the 1.4 tag. Will do so now and rebuild, then report back.

-------------------------

TikariSakari | 2017-01-02 01:07:09 UTC | #6

Sorry for inviding in your thread, but after I updated my project to main branch I ran into an issue:

[quote="weitjong"]Are you using the latest revision from master branch or release 1.4? There is recent changes in the Android's asset directory handling in our master branch. If you use the latest revision then you have to ensure your Android build tree has a custom Ant task properly setup. When in doubt, just run the cmake_android.sh or cmake_android.bat one more time to reconfigure your existing build tree.[/quote]

Is it possible to have the android build work somehow like it did before the change, so that it would use the stuff that are under asset-folder? I was using linked directories in the asset folder for data and coredata. The data-folder was minimized one, where I had deleted most of the stuff that I do not need so that the apk-size would be as small as possible (6MB atm). Now with this new build the ant doesn't seem to accept having files or possibly having folders CoreData and Data inside the asset folder. I assume that it copies these assets from the main bin-folder?

-------------------------

Deveiss | 2017-01-02 01:07:10 UTC | #7

Rebuilding from 1.4 fixed the issue! The game was almost done, the Android build was the last road block in the port from AngelScript prototype done in a weekend with friends to a C++ game for mobile platforms. Now, my focus will be on expanding the original prototype into more of a game. Anyone interested in seeing what I have done can join the public beta at: [play.google.com/apps/testing/me.benrstraw.hd](https://play.google.com/apps/testing/me.benrstraw.hd). When the app goes public, I'll be sure to make a post in the Showcase forums. Thanks to the forums and especially the IRC for all the help!

-------------------------

TikariSakari | 2017-01-02 01:07:10 UTC | #8

I think this is a bug with windows platform when trying to compile to android with the current master branch. Also once I finally managed to get something transferred to android. I created a program that copied every single file and added '_' after every single folder, but not on a file. For some reason the UI didn't anymore scale like it used to, but other data seemed to come out normally, such as music and others.

So basically my file structure looks like this:
[code]
assets_
   Data_
      Models_
         file1.mdl
   CoreData_
[/code]

Edit: nvm it was working as it used to work, I just forgot that I changed something. The minsize of text works bit differently on windows than android as if I set same font-size as what it used to be, it doesn't recalculate min-size to texts on android. Also I noticed that there was a version where one could use the old way of just throwing everything to assets-folder.

-------------------------

