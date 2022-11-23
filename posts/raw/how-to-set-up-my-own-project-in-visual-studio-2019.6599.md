Imago_Mundi3D | 2020-12-06 16:01:15 UTC | #1

Hi, 
I'm a newcomer here. Sorry for my lack of experties.
Is it possible to configure a newly created Urho project in VS2019 without using CMake build system?
I build up Urho from source (using CMake), as explained in the Documentation... But I'd prefer to set up a project with RMB clicking on "Project Properties"-->Additional Include/Libs Dir, and so on.
Please, could you point me in the right direction for this specific pourpose?
Thanks in advance, kind regards,

*Cosmo*

-------------------------

SirNate0 | 2020-12-06 16:19:16 UTC | #2

Hi Cosmo,

I think you should just need to point it to the include directory within the build directory for Urho and likewise for the built library directory. You'll possibly also need to set the right compiler defines on your own (to do that I'd recommend just looking at the command used to compile one of the samples and replicating that for your project). I don't use visual studio, though, so I could have that wrong.

-------------------------

1vanK | 2020-12-06 18:15:02 UTC | #3

Your project must contain the correct set of defines. If you are a beginner, you cannot do it manually

-------------------------

