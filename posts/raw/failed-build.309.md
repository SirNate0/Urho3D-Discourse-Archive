NemesisFS | 2017-01-02 00:59:31 UTC | #1

Hi,

I have some trouble building Urho3D on linux. I use gcc and ccache, which I have tried to clear without success.
This is the error I get:
[code]In file included from Urho3D/Source/ThirdParty/kNet/include/kNet/SharedPtr.h:19:0,
                 from Urho3D/Source/ThirdParty/kNet/include/kNet/SerializedDataIterator.h:19,
                 from Urho3D/Source/ThirdParty/kNet/include/kNet/DataDeserializer.h:23,
                 from Urho3D/Source/ThirdParty/kNet/src/DataDeserializer.cpp:24:
/usr/include/c++/4.9.0/cstdlib:178:10: error: expected unqualified-id before ?__int128?
   inline __int128
          ^
ThirdParty/kNet/CMakeFiles/kNet.dir/build.make:54: recipe for target 'ThirdParty/kNet/CMakeFiles/kNet.dir/src/DataDeserializer.cpp.o' failed[/code]

The whole buildprocess is logged here, in case it is necessary.:
[ideone.com/pvtXZ3](http://ideone.com/pvtXZ3)

I hope you can help me

-------------------------

friesencr | 2017-01-02 00:59:32 UTC | #2

It looks like gcc broke compatibility with that around 4.8.2.  It also looks like a 32bit only problem.  Have you tried the 64bit build?

./cmake_gcc.sh -DURHO3D_64BIT=1

It also sounds like gcc suggests adding your own typedef to compensate.

-------------------------

NemesisFS | 2017-01-02 00:59:32 UTC | #3

It looks like you are correct, the 64 bit build runs perfect.
What confuses me is, that I have this problem on my laptop but not on my desktop though both run the same gcc version (4.9.0)

-------------------------

