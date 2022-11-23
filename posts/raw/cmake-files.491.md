rogerdv | 2017-01-02 01:00:50 UTC | #1

Im trying to create my first project, following doc directions. I copied&pasted the cmakelists.txt file, but it doesnt works:

 [code]CMake Error at CMakeLists.txt:18 (include):
  include could not find load file:

    Urho3D-CMake-common


CMake Error at CMakeLists.txt:20 (find_package):
  By not providing "FindUrho3D.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "Urho3D", but
  CMake did not find one.

  Could not find a package configuration file provided by "Urho3D" with any
  of the following names:

    Urho3DConfig.cmake
    urho3d-config.cmake

  Add the installation prefix of "Urho3D" to CMAKE_PREFIX_PATH or set
  "Urho3D_DIR" to a directory containing one of the above files.  If "Urho3D"
  provides a separate development package or SDK, be sure it has been
  installed.
[/code]

I already declared the URHO3D_HOME variable and checked that it is available, but I think this is not the cause of the problem. I havent installed Urho3d, I just want to use it from the source directory.

-------------------------

weitjong | 2017-01-02 01:00:51 UTC | #2

Your CMake error is quite clear. It could not find the Urho3D-CMake-common module. Make sure your CMakeLists.txt has this line.

[quote]# Set CMake modules search path
set (CMAKE_MODULE_PATH $ENV{URHO3D_HOME}/Source/CMake/Modules CACHE PATH "Path to Urho3D-specific CMake modules")[/quote]

If it already has this line then double check that by listing the content of this directory.

On Unix-like system:
ls $URHO3D_HOME/Source/CMake/Modules

On Windows system:
dir %URHO3D_HOME%\Source\CMake\Modules

The directory should contain the "Urho3D-CMake-common.cmake" file among others. If not then most likely you have set the URHO3D_HOME environment variable wrongly.

-------------------------

rogerdv | 2017-01-02 01:00:51 UTC | #3

My mistake, I had some errors in the path. Also, the cache file has to be removed.

-------------------------

weitjong | 2017-01-02 01:00:51 UTC | #4

The CMake cache is a double edged sword. On one side it helps us from repeating ourselves to key in the environment variable values and it speeds up the CMake configuration/generation time as well. But on other side, if thing is going south then it may confuse the CMake beginner users even more.

-------------------------

rogerdv | 2017-01-02 01:00:51 UTC | #5

Does that same cmake file works for Windows?

-------------------------

weitjong | 2017-01-02 01:00:51 UTC | #6

If you are asking whether the same CMakeLists.txt files that we have work on Windows platform then the answer is yes. In fact the same set of CMakeLists.txt files work on all the platforms that Urho supports. But of course, on Windows you can only invoke the *.bat batch files which in turn call CMake to process our CMakeLists.txt files.

-------------------------

