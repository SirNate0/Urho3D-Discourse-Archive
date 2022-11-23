archwind | 2020-04-27 20:31:27 UTC | #1

I kept getting this error. Maybe you're aware of it:

[code]

ERROR [2020-04-27 14:40:29,969] Exception            System.Exception: Could not find resource Textures/Ramp.png. You can omit this exception by subscribing to Urho.Application.UnhandledException event and set Handled property to True.
ApplicationOptions: args -w -p "CoreData" -pp "E:\NewMV\Tools\Editor\bin\Debug;E:\NewMV\Tools\Editor\bin\Debug\../../native;E:\NewMV\Tools\Editor\bin\Debug" -hd -landscape -portrait 
   at Urho.Application.ThrowUnhandledException(Exception exc) in E:\NewMV\Bindings\Portable\Application.cs:line 582
   at Urho.Runtime.OnNativeCallback(CallbackType type, IntPtr target, IntPtr param1, Int32 param2, String param3) in E:\NewMV\Bindings\Portable\Runtime\Runtime.cs:line 154
   at Urho.Renderer.Renderer_Renderer(IntPtr context)
   at Urho.Renderer..ctor(Context context) in E:\NewMV\Bindings\Portable\Generated\Renderer.cs:line 88
   at Urho.Renderer..ctor() in E:\NewMV\Bindings\Portable\Generated\Renderer.cs:line 77
   at Multiverse.Tools.WorldEditor.WorldEditor.SetupUrho(Context ct) in E:\NewMV\Tools\WorldEditor\WorldEditor.cs:line 1369
   at Multiverse.Tools.WorldEditor.Program.Start() in E:\NewMV\Tools\WorldEditor\Program.cs:line 100
[/code]

I traced it into renderer.cpp at line 1595. Checking other samples, I removed the unhandled exception to test the samples code and have the same issue so therefore the internal engine can't find the path to the working directory. I added a handler to my code but the real fix needs done internally.

-------------------------

Eugene | 2020-04-27 22:21:12 UTC | #2

Do you actually have this resource in the resource folder/package/whatever?
I don’t understand what kind of fix you expect.

-------------------------

archwind | 2020-04-27 22:43:25 UTC | #3

Yeah it is in the root execution directory. CoreData.pak 

If I remove the unhandled exception from any of the samples it crashes with the same problem. Like it can't find the path to it's resources.

-------------------------

archwind | 2020-04-27 23:16:35 UTC | #4

This may be an issue with UrhoSharp. All their samples have handlers for unhandled exceptions and if that is removed it throws the same error.

The documentation says If the data folder is null then the default is Data. I tried renaming the pak to Data but that didn't work. I passed it a directory "Data" and set up a folder with the unzipped pak files and it still doesn't see it. The image is there. I checked that it exist in Textures\Ramp.png. I tried also making a directory CoreData and copied CoreData.pak to both these also.

-------------------------

SirNate0 | 2020-04-28 16:05:58 UTC | #5

Try specifying the full path to the file and/or adding a .pak to the end of it. No idea if that will solve the problem, but it should at least narrow things down.

Are you getting any messages in the log about it?

-------------------------

archwind | 2020-04-28 19:33:41 UTC | #6

I tried adding the pak file directly and it failed with message 'can't find CoreData.pak' so I removed the pak file from the path. I also tried leaving the "/' at the end and removing it.

"E:/NewMV/Tools/Editor/bin/Debug/CoreData.pak"
"E:/NewMV/Tools/Editor/bin/Debug/"
"E:/NewMV/Tools/Editor/bin/Debug"

Adding the full path did not help. I'll just use the handler for unhandled exceptions for now. Maybe recompile the engine later. I have source for everything so not a big deal.

-------------------------

SirNate0 | 2020-04-29 14:55:10 UTC | #7

I think you're using the wrong argument for package files. From the docs `-pf <files>  Resource package file to use, separated by semicolons, default to none`.

-------------------------

archwind | 2020-04-30 19:23:18 UTC | #8

I had to configure it. The samples are pretty simple and don't configure the directory structure so it just runs with defaults.

fixed.

-------------------------

