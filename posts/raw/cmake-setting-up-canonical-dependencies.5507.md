Sinoid | 2019-08-25 23:15:19 UTC | #1

I use Premake so I generally don't have to deal with it, but what's the call-site for sticking in additional dependencies that can't go through the copy-pasta and list-soup-pumps that the CMake scripts are using (ie. need to do the correct `include_directories`, `target_link_libraries` etc - not the soup)?

Library in question is V-EZ and all of the gobbly gook slop that goes with it (glslang, spirv, spirv-cross, oglcompiler, etc). I am not going to write new CMake scripts for those just to tie them in.

Just can't seem to find the right spot to hook it all together that it goes into the right spot without later being overwritten by the Urho CMake scripts list pumping.

-------------------------

Sinoid | 2019-08-25 23:15:25 UTC | #2

Ahh, found it. After the header install business, that's the last thing that blows out any CMake state.

-------------------------

