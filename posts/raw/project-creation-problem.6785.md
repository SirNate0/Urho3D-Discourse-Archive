Dares | 2021-04-06 19:37:24 UTC | #1

Hi,
I am trying to get a project with Urho working. I followed the Documentation, builded Urho, set the Environment variable(URHO3D_HOME) and used the CMakeLists.txt that is given in the Documentation. But I get the Error:
> -- Found Urho3D: /home/dares/Downloads/Urho3D-1.7.1/lib/libUrho3D.a (found version "Unversioned")
> CMake Error at CMake/Modules/UrhoCommon.cmake:770 (message):
>   Could not call define_resource_dirs() macro before define_source_files()
>   macro.
> Call Stack (most recent call first):
>   CMake/Modules/UrhoCommon.cmake:1001 (check_source_files)
>   CMake/Modules/UrhoCommon.cmake:1583 (define_resource_dirs)
>   CMakeLists.txt:26 (setup_main_executable)

What am I doing wrong?

-------------------------

Modanung | 2021-04-06 19:52:43 UTC | #2

If you have no specific reason to use an earlier version, stick to the latest master.

The minimum required cmake version was increased in the meantime. It may be related.

-------------------------

Dares | 2021-04-06 20:01:53 UTC | #3

do you mean the 1.8 alpha release or directly cloning the github-repository?

-------------------------

Modanung | 2021-04-06 20:18:15 UTC | #4

The latter. :slight_smile:

-------------------------

Dares | 2021-04-06 21:16:03 UTC | #5

That Error is gone now, thank you :)

-------------------------

