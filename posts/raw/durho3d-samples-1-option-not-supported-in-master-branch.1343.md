Lumak | 2017-01-02 01:07:00 UTC | #1

Just downloaded the master branch and did a cmake vs2013 with [b]-DURHO3D_SAMPLES=1[/b] option, but none of the sample project files are created in the solution.

Are we doing away with this build option in all platforms now?

What file do I need to change to enable this again?

-------------------------

TikariSakari | 2017-01-02 01:07:00 UTC | #2

At least it worked for me, I just tried upgrading to the current master version and created new build directory with 
[code]
cmake_vs2013.bat ..\vsurhosamples -DURHO3D_SAMPLES=1
[/code]

-------------------------

Lumak | 2017-01-02 01:07:00 UTC | #3

Verified that typing -DURHO3D_SAMPLES=1 on the command line does generate sample project files.

However, my vs2013_samples.bat file which used to work and has:
[code]
@%~dp0\cmake_generic.bat %* -VS=12 -DURHO3D_SAMPLES=1
[/code]

Now fails to build sample project files. Works on 1.4.

-------------------------

weitjong | 2017-01-02 01:07:00 UTC | #4

Try to switch around the last two arguments in your own script. There is a recent changes in cmake_generic.bat to make it supports spaces in source/build path. However,  in doing so I also notice there is some weirdness in the current argument parsing logic that it now susceptible to argument order in some cases. That's what you get from a Linux guy doing a Windows job. Still it is better that than being left out while Linux and Mac users already use space as the final frontier.  :smiley:

-------------------------

Lumak | 2017-01-02 01:07:01 UTC | #5

Switching the arguments worked and generated the sample project files.
Thank you.

-------------------------

