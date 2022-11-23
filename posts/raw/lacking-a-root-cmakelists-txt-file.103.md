OvermindDL1 | 2017-01-02 00:58:00 UTC | #1

I set up Urho3D as a CMake external project dependency, but the lack of a root CMakeLists.txt file makes our very...hairy to do and breaks auto-importing project variables.  Is there any chance soon that a root CMakeLists.txt file could be added to the Urho3D project?  Basically if I can just do:
[code]cd somewhere
cmake -DVars path/to/urho3d[code]
And have it work then it could trivially work with the CMake external project system, or if I could just add_subdirectory it then even better.  Problem is that the existing CMakeLists.txt files everywhere are making invalid assumptions about the root source directory (instead of project source or relative) among some other issues, particularly in tool building it seems.  I barely touched it last night but those are the issues that I ran into.  Any chance of those being corrected and a root CMakeLists.txt file being used so Urho3D would be usable as a CMake ExternalProject so it can fit into the project dependencies of the other libraries I use cleanly?  I might have time to do another pull request in a week or so, but if done sooner than I would be quite happy.  :slight_smile:

-------------------------

weitjong | 2017-01-02 00:58:02 UTC | #2

Please do not double post in future.

User that interested in this topic, please follow the discussion here: [topic83.html](http://discourse.urho3d.io/t/cmake-fixes/104/1)

-------------------------

