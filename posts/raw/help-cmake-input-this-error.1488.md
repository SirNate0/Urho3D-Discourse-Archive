GoldNotch | 2017-01-02 01:08:06 UTC | #1

When I try to configure Urho3d, CMake input this error
[code]CMake Warning at CMake/Modules/Urho3D-CMake-common.cmake:193 (message):
  Could not use MKLINK to setup symbolic links as this Windows user account
  does not have the privilege to do so.  When MKLINK is not available then
  the build system will fallback to use file/directory copy of the library
  headers from source tree to build tree.  In order to prevent stale headers
  being used in the build, this file/directory copy will be redone also as a
  post-build step for each library targets.  This may slow down the build
  unnecessarily or even cause other unforseen issues due to incomplete or
  stale headers in the build tree.  Request your Windows Administrator to
  grant your user account to have privilege to create symlink via MKLINK
  command.  You are NOT advised to use the Administrator account directly to
  generate build tree in all cases.
Call Stack (most recent call first):
  CMakeLists.txt:47 (include)[/code]

How i can repear it?

-------------------------

thebluefish | 2017-01-02 01:08:06 UTC | #2

That's a warning, not an error. It's perfectly acceptable to see that if your user account is not a local admin.

-------------------------

friesencr | 2017-01-02 01:08:06 UTC | #3

Try running the command in a cmd.exe with "Run as Administrator".

-------------------------

weitjong | 2017-01-02 01:08:06 UTC | #4

The warning actually explicitly says, do not use Administrator for the purpose of generating a build tree. You have to put a lot of trust in the project that it would not do any harm to your host system whether it is intentional or unintentional when you run our scripts as admin user. If you have the password to "Run as Administrator" then you might as well setup your host system as it should be from a security stand point. I am not Windows savvy but with the help of Google, it just took me a while to setup my newly upgraded Windows 10 partition to mimic my Linux system to have one root/admin account and one normal user account, and only grant privileges as minimal as possible to the normal user account that it needs to function properly.

-------------------------

