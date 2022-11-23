yushli | 2017-01-02 01:07:38 UTC | #1

I am trying to build heXon([github.com/LucKeyProductions/heXon](https://github.com/LucKeyProductions/heXon)) by using cmake. I used the following CMakeLists.txt file:

# Define target name
set (TARGET_NAME heXon)

# Define source files
define_source_files (EXTRA_H_FILES ${COMMON_SAMPLE_H_FILES})
set (CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -std=c++11")
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
# Setup target with resource copying
setup_main_executable ()
# Setup test cases
setup_test ()


It works fine if statically linked. but if I change URHO3D_LIB_TYPE to SHARED, there are link errors:

Linking CXX executable ../../../bin/heXon
CMakeFiles/heXon.dir/TailGenerator.cpp.o: In function TailGenerator::TailGenerator(Urho3D::Context*)': TailGenerator.cpp:(.text+0x25b1): undefined reference toUrho3D::SourceBatch::~SourceBatch()'
TailGenerator.cpp:(.text+0x29f7): undefined reference to Urho3D::SourceBatch::~SourceBatch()' TailGenerator.cpp:(.text+0x2a50): undefined reference toUrho3D::SourceBatch::SourceBatch()'
collect2: error: ld returned 1 exit status
make[2]: *** [bin/heXon] Error 1
make[1]: *** [Source/Samples/heXon/CMakeFiles/heXon.dir/all] Error 2
make: *** [all] Error 2

If I copy over the definition of these functions from drawable.cpp to TailGenerator.cpp, then it builds. 
Any idea why this happen? And how to fix it? Thank you

-------------------------

cadaver | 2017-01-02 01:07:38 UTC | #2

This looks like a missing URHO3D_API export specifier in SourceBatch. I'll push to master shortly.

EDIT: Pushed. Also needed to define copy-constructor & assignment manually to prevent compiler generating them inline and complaining of the Material shared pointer.

-------------------------

yushli | 2017-01-02 01:07:38 UTC | #3

Thanks for the quick response. It is fixed now.

-------------------------

