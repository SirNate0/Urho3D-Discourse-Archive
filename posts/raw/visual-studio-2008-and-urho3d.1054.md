Dave82 | 2017-01-02 01:05:06 UTC | #1

Hi ! First of all i want to say i love Urho3d ! It's the most powerful c++ game engine i ever tested so far , you guys really did a great job !
I have sucessfully built the latest version (SHARED lib with visual studio 2008), but i can't figure out how to create a new empty project in visual studio and use the built urho3d library?

What i did so far :
1. created an empty win32 project.
2. added a URHO3D_API proprocessor define (#define URHO3D_API)
3. added all folders inside Urho3d's Engine folder  (e.g : Core , Audio , etc) as additional include paths

now the projects compiles , but it got one linker error :

[quote]error LNK2001: unresolved external symbol "private: static char Urho3D::String::endZero" (?endZero@String@Urho3D@@0DA)[/quote]
which is probably defined in the Urho3d.dll. 

if i define URHO3D_API as __declspec(dllimport) then it builds the exe but i get a bunch of warnings like this :
[quote]engine\core\Variant.h(159) : warning C4251: 'Urho3D::ResourceRefList::names_' : class 'Urho3D::Vector<T>' needs to have dll-interface to be used by clients of struct 'Urho3D::ResourceRefList'[/quote]

So can you tell me what i'm doing wrong ? Or what is the proper way to create a new project ?
Thanks and keep up the good work !

-------------------------

friesencr | 2017-01-02 01:05:06 UTC | #2

if you are using master and having to define the URHO3D_API you need to include the <Urho3d/Urho3d.h> header which is generated from cmake.

-------------------------

Dave82 | 2017-01-02 01:05:06 UTC | #3

Hi ! Well i didn't used cmake for the new project  i did everything manually in visual studio (adding paths and defines)
i used Cmake only for build Urho3d and the samples for visual studio so i have no Urho3D.h file...

it works (i can run the exe) i just have to get rid of those warnings somehow

-------------------------

friesencr | 2017-01-02 01:05:06 UTC | #4

For reference the general build instructions are here: [urho3d.github.io/documentation/H ... lding.html](http://urho3d.github.io/documentation/HEAD/_building.html)

As far as my usual method goes for making a project I do 1 of 2 methods.

Part of solution:
If i want to build in the same 'solution' as urho I copy/paste the Urho3D Player and use that as a template.  If you know ruby there is a rake task to do this very thing.

Seperate solution:
If you want urho's build magic then follow these directions: [urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html)

If you do not want build magic then build urho normally and grab the include/lib folders from the build.

-------------------------

Dave82 | 2017-01-02 01:05:06 UTC | #5

Hey thanks , i've found out that there was a Urho3D.h file built after all... i just missed it. And as i see the above mentioned warning (4251) is disabled , thats exacly what i did so
it finally works without any warnings and errors !

So i did it without using CMake.To be honest i don't like fiddling with Makelists CMake and commandline... i think it's an unnecessary time-wasting step (at least on windows)

-------------------------

weitjong | 2017-01-02 01:05:06 UTC | #6

If you enjoy configuring your own project the hard way then you may want to look at the [b]baked[/b] compiler defines and flags which is auto-generated when you build Urho3D (shared) library using CMake. The baked setting can be found in your Urho3D [b]build-tree[/b] under "Source/Urho3D/Urho3D.pc". Note the stress that it is generated in the build-tree and that it is baked, i.e. its content differs from one to another depends on the enabled build options when you build your Urho3D library.

-------------------------

