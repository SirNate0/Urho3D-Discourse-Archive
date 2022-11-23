ToolmakerSteve | 2021-12-03 03:37:01 UTC | #1

Following instructions at https://urho3d.io/docs/getting-started/installation.

Section "Install Urho3D Library", I do:

* cd \gh\urho3d   <-- root of urho3d repo
* rake build install

result:

> MSBUILD : error MSB1009: Project file does not exist.

Above these instructions, I see

> CAUTION:  
> On Windows host the environment variables have to be set on separate command before invoking Rake task.

But it doesn't say **what** environment variables need to be set, and to what values.

I figure I'm either in the wrong folder (though I see a "rakefile" there), or I'm supposed to edit some file first, or set some environment variable.

What should I try next?

OR: I now have successfully completed "cmake" instructions, and have "Urho3d.sln". Does this mean I no longer need to do "rake build"?

-------------------------

xlat | 2021-12-03 10:57:13 UTC | #2

[quote="ToolmakerSteve, post:1, topic:7081"]
OR: I now have successfully completed “cmake” instructions, and have “Urho3d.sln”. Does this mean I no longer need to do “rake build”?
[/quote]

Run “Urho3d.sln” by Visual Studio and press button Build Solution.

And ...

-------------------------

xlat | 2021-12-03 11:00:07 UTC | #3

You should get (for VS2019):

![2021-12-03_2|690x424](upload://tSiIDlfmG4k9txEpqPlErfng2AN.jpeg)


==

![2021-12-03_134653|690x371](upload://blxrW9It0IRWkPSd0Qv5WVBrW0T.jpeg)

-------------------------

ToolmakerSteve | 2021-12-03 17:53:10 UTC | #4

Thanks. Indeed, the .sln works. Running the samples now.

-------------------------

