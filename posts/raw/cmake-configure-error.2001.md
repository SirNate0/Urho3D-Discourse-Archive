marcules | 2017-01-02 01:12:12 UTC | #1

Hi I've been trying to get a project up and running all night but I cant get it to work.
I've been following the "Building Urho3D" to build the Urho3D engine and samples. Then I've continued with the "Using Urho3D as external library".
Everything has been fine untill I come to the CMake configure step.
My source is [b]/home/marcus/Dev/Urho3d/build[/b]
and my target build is [b]/home/marcus/Dev/Urho3dSandbox[/b]
my source is built from the Urho3Ds repository which i've stored at [b]/home/marcus/Dev/Urho3d/rep[/b]
The error I'm getting when trying to configure with CMake is [b]"CMake Error: The source directory "/home/marcus/Dev/Urho3d/build" does not appear to contain CMakeLists.txt."[/b]

Should I add this CMakeLists.txt manually or should this file have been generated from the previous step when I was building the Urho3D engine? Isn't the CMake configure supposed to use the CMakeLists.txt file in target which are shown in the "Using Urho3D as external library" documentation? When I tried to put the CMakeLists.txt in the source folder (instead of the target) the configure works, but then when trying to generate it throws another error: [b]"CMake Error: Cannot determine link language for target "SandboxExec"."[/b]. I managed to get this fixed by adding the main.cpp into the source folder but then the project setup is becomes completely wrong.

I'm new here and I've tried to find answers for this issue but haven't found any and I hope I can get some help from you guys.
I'm using Ubuntu 16 if that helps.

Best regards.

-------------------------

weitjong | 2017-01-02 01:12:12 UTC | #2

Welcome to our forum.

To me the error message from CMake is already very clear on what exactly went wrong. To quickly get started with your own project, you can use the "scaffolding" rake task which will help you to create a skeleton project structure complete with a minimum CMakeLists.txt. The usage of the scaffolding rake task is explained in the last section of the "Using Urho3D as external library" page. We should probably reorganize the page to have this section on top since now this rake task works universally. In the past it was only working on Unix-alike host systems but not on Windows.

-------------------------

marcules | 2017-01-02 01:12:17 UTC | #3

Thanks!
And thanks, that did the trick. But I was going back over to Windows form Ubuntu and did it with CMake again and now it worked. Not sure what I was doing wrong the last time.

Sorry for a late reply. Was reading the message the day after you wroite it but forgot to answer.

-------------------------

