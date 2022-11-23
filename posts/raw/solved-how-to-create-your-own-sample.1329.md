cap | 2017-01-02 01:06:52 UTC | #1

Suppose you wanted to clone all the Urho3D source code and add a new Sample to the samples, say 100_MySample. Suppose you didn't want that particular sample to inherit from Sample.h, but rather you just wanted a main.cpp in there which have code depending on Urho3D project. One more thing, suppose 100_MySample uses a header library with that code in directory a MyLibInclude.

I tried this with the extra sample directory having this structure:

100_MySample/
|-- MyLibInclude/
|-- CMakeLists.txt
|-- main.cpp

and the following CMakeLists.txt:

  include_directories (
  	  "${CMAKE_CURRENT_SOURCE_DIR}/MyLibInclude"
  )

  # Define target name
  set (TARGET_NAME 100_MySample)

  # Setup target with resource copying
  setup_main_executable ()

  # Setup test cases
  setup_test ()

So basically the CMakeLists.txt is identical to that for all the other samples, except without the line

  define_source_files (EXTRA_H_FILES ${COMMON_SAMPLE_H_FILES})

And up in the CMakeLists.txt for the Sample folder I added the line

  add_sample_subdirectory (100_MySample)

After running cmake a corresponding Visual Studio project is constructed for the Sample, but none of the code (i.e. main.cpp) is discovered. Am I doing this right? Or, alternatively, what's the easiest way to add your own new Sample, if you don't want it to inherit from Sample.h? Thanks.

-------------------------

weitjong | 2017-01-02 01:06:52 UTC | #2

You still need to call the define_source_files() macro without any arguments to define the source files for your new sample target. If you really want to go back to basics, why not just use basic CMake commands instead of calling our CMake macros in your CMakeLists.txt? I guess that depends on the purpose of your new sample.

-------------------------

cap | 2017-01-02 01:06:54 UTC | #3

Thanks!

Including define_source_files with no arguments fixed this problem. (And it turns out there are other problems but not related to this specific question....)

(Yes, I would like and am attempting to go back to basics with cmake, it's just that my understanding is limited to fairly toy-ish examples, and when I've tried to have a project interact with Urho or just change Urho a bit I've just been breaking things; whereas Urho builds beautifully and so I'm trying to just mimic as close as possible what I can see is already actually working.)

Thanks again.

-------------------------

