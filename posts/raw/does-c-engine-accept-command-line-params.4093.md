johnnycable | 2018-03-16 08:52:13 UTC | #1

[Urho3D player](https://urho3d.github.io/documentation/1.7/_running.html) has the option of using command line parameters. Can Urho C++ do the same?
What I'd like to know is if it exists some urho api part I've missed that can do command line scan in the way the player does, without recurring to scripting, I mean
Thanks guys

-------------------------

kostik1337 | 2018-03-16 09:11:12 UTC | #2

Yes, it supports them the same way as Urho3D player, unless you override them in Application::Setup, command-line options have lower priority than options specified in code

-------------------------

Eugene | 2018-03-16 09:26:03 UTC | #3

https://github.com/urho3d/Urho3D/blob/70049ba58210ad26d8402363cf4d864f6c294155/Source/Urho3D/Engine/Application.cpp#L54

-------------------------

johnnycable | 2018-03-16 13:34:58 UTC | #4

Thank you guys (20 character filler)

-------------------------

