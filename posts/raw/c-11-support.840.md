thebluefish | 2017-01-02 01:03:21 UTC | #1

Hey all, I wanted to get some feedback before adhering to C++11.  During integration of libRocket, I want to use std::shared_ptr for any classes that I cannot override to work with Urho3D::Object.

Is it safe to assume C++11 support for most people at this point?

-------------------------

setzer22 | 2017-01-02 01:03:22 UTC | #2

I use C++11 already in all my projects and Urho is no exception. Can't speak for anyone else but I've never found a reason for which I shouldn't be using the latest standard of the language. There's total retrocompatibility AFAIK.

-------------------------

weitjong | 2017-01-02 01:03:22 UTC | #3

I believe you can enable the C++11 support and use the C++11 feature in your own project safely. If I recall correctly the past discussion about this subject then we only have problem to include the code with C++11 feature in the Urho3D project, simply because we still try to support the ancient VS2008. But I believe, the VS2008 support will be dropped in time. The sooner the better.

-------------------------

cadaver | 2017-01-02 01:03:23 UTC | #4

Yes, supporting VS2008 or other ancient compilers is already pretty much becoming a non-priority, as time goes on and VS2013 seems to work relatively well, and the Community version offers features above the previous Express editions.

Using C++11 in Turso3D has been a pleasant experience and it would be nice to move use of constructs like auto to Urho3D as well.

However, on the subject of std::shared_ptr, as it's not intrusive you have to be more careful in its use: make sure that multiple shared_ptr's with different reference counts do not get constructed that point to the same object. Particularly if users will be dealing directly with them. Script binding them may also be problematic. I've typically handled 3rd party lib objects by wrapping them inside Urho RefCounted objects (constructed either with new/delete or by the lib's own creation/deletion functions) but of course, if you'd have to wrap a whole library, I can understand you wouldn't want to do that.

-------------------------

thebluefish | 2017-01-02 01:03:24 UTC | #5

@cadaver How do you deal with third party factories?

In my example, I'm dealing with libRocket's Context. It's easy enough to inherit from the Context class and Urho3D::Object, and I can get it working fine that way. However the libRocket documentation states that we should not be creating the Context class directly, and instead use the built-in GetContext method to create it.

I was thinking of manually creating the Context and re-implementing whatever additional logic that GetContext does, but that's not nearly as future-proof as I'd hope.

Otherwise I'd prefer to use std::shared_ptr instead of a raw pointer. VS2008 is of no concern to me since VS2013 Community Edition was released.

-------------------------

cadaver | 2017-01-02 01:03:24 UTC | #6

A similar case is Urho's ScriptFile class, it contains an AngelScript module as a member variable and manages it through the library's creation/deletion functions.

I would personally stay away from multiple-inheriting Object/Refcounted and the 3rd party library classes, as that creates mess and potentially the library itself isn't able to handle that (by wrapping I didn't mean inheritance, but containing.)

Let's assume the libRocket implementation would be component-based. This means a component ("GuiCanvas" or such) would refer to a libRocket context and manage its lifetime using the library functions. The component would have a getter to retrieve the libRocket context, and user would interact with it directly, again using libRocket native functions. Lifetime of the context would be managed by the GuiCanvas component destructor destroying it, so only the component would actually need to obey Urho refcounting. (In this case, no attempt would be made to make the individual libRocket widgets etc. to behave like Urho refcounted objects)

-------------------------

TikariSakari | 2017-01-02 01:03:36 UTC | #7

Umm another noobish question, but how should one set for windows the c++11 support, when compiling to android with make? I tried compiling to android my "tween"-thingy, but when I tried to use -std=c++11, my building halted on CoreAPI.cpp-file. I am not even sure if I did this right way, since I just added it in one of those android_cxx_flags, like here:
[code]
inside android.tuulchain.cmake:

set( ANDROID_CXX_FLAGS "${ANDROID_CXX_FLAGS} -fsigned-char -std=c++11" ) # good/necessary when porting desktop libraries
[/code]

The make also complained that it was using the -std=c++11 parameter on compiling c-files.

Edit:: After I disabled angel script and, I managed to compile it. It could be that my path to cmake/make is/was using some old version, or the fact that I updated ndk-version since I first used the cmake_android, but now that I made new project without angelscript all went well.

-------------------------

TikariSakari | 2017-01-02 01:03:47 UTC | #8

I figured answering my own question on enabling C++11, if someone else is as clueless as I am with all this C++ and happens to google out the question later on. Visual studio at least for me had this enabled by default, without me having to do anything to make it work, but when compiling with make for android, instead of adding it to the toolchain what I did before, adding it to the project level seems to do the work.

For example I have my projects sources under Urho3D/Source/myprojs/whateverproject. Under the myproj-folder modifying the CMakeLists.txt by adding following line:
[code]set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")[/code] 

I am not sure if this enables C++11 for all the projects after the myproj-folder, but at least for the subfolders under myprojs can now use auto, nullptr and shared_ptr even when I use the make to build android application + the AngelScript compiles this way as well, unlike if I try to compile everything as C++11 enabled by changing the toolchain.

Well I am still not sure if this is the right way, but at least it is one way to enable it.

-------------------------

