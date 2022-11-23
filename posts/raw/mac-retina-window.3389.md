adekto | 2019-05-23 13:20:00 UTC | #1

i want the banner of the mac apps to be in the native resolution
but the examples seem to have this odd down scale
have tried ```engineParameters_[EP_HIGH_DPI]     = true;``` but not getting any different results
![Untitled-1|399x95](upload://ipx7SGqSNTXvjVvNoPEVQ279rRS.png)

got the same problem with popup errors (comparing with cmake popup)
![50|492x499](upload://ff5ihMCDLRl5qr27eSTnOC8eLjT.png)

-------------------------

weitjong | 2017-07-27 11:39:18 UTC | #2

Are you using latest master branch or release 1.6?

The first issue might be due to a missing property key/value in the macOS bundle info plist file to use the high DPI mode. The second issue is a common pitfall for new user. Read the docs (use the keyword to search) as suggested by the error message.

-------------------------

johnnycable | 2017-07-27 12:11:24 UTC | #3

In the Application::Setup or in the application parameters starting file:

engineParameters_["HighDPI"] = true;
engineParameters_["WindowWidth"]=HSIZE;
engineParameters_["WindowHeight"]=VSIZE;

HSIZExVSIZE = your mac high dpi chosen res, eg 2048x1280

Using 1.6 stable, on Os X 10.12.6

Also setting engineParameters_["VSync"] = true and engineParameters_["FullScreen"] = true can help...

-------------------------

adekto | 2017-07-27 14:28:02 UTC | #4

ok that was it. why is that missing in the plist by default? as far as i can see every modern mac last few years are retina these days

-------------------------

weitjong | 2017-07-27 15:30:11 UTC | #5

Because the core devs (well, except Lasse recently) do not have Mac with Retina display yet, so we could not tell the difference it makes on our monitor :slight_smile:. You are welcome to make a PR to fix it. Actually the existing template was shamelessly taken from CMake quite some time ago and have not received any update. I am aware that the newer version of CMake has updated the plist file and sooner or later plan to make the sync again.

-------------------------

adekto | 2017-07-28 10:18:17 UTC | #6

[quote="weitjong, post:2, topic:3389"]
The second issue is a common pitfall for new user. Read the docs (use the keyword to search) as suggested by the error message.
[/quote]

so i looked at it but im using the mac app bundling and it still gives that error wen running with xcode, but its fine wen just opening the app the documentation did not say how to solve this
wich is going to make it hard to debug

how do i make it ignore this resource path since it should use the bundled Data/CoreData

update:
never mind figured it out
had to add this -pp /to/Data&CoreData/folder 
in Product -> Sheme -> Edit Sheme... -> Run -> Arguments
https://urho3d.github.io/documentation/1.6/_running.html#Running_Commandline

-------------------------

weitjong | 2017-07-28 10:06:36 UTC | #7

Yes, that is one of the way. You may want to switch the doc version to the same version of Urho3D library you are using.

-------------------------

