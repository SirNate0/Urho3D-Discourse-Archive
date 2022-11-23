bvanevery | 2017-01-02 01:08:05 UTC | #1

I've been trying to build the Urho Sample Platformer.  I've been filing bugs and the author of USP has been fixing them.  We are currently having a problem with WinMain being undefined.  Despite superficial appearances, I don't think it's getting any "WIN32" define to trigger correct behavior in Core\main.h.  When I run a preprocessor my main.i output is 
[code]int RunApplication()
{
    Urho3D::SharedPtr<Urho3D::Context> context(new Urho3D::Context());
    Urho3D::SharedPtr<USP> application(new USP(context));
    return application->Run();
}
int main(int argc, char** argv) { Urho3D::ParseArguments(argc, argv); return RunApplication(); };[/code]
Visual Studio believes that DEFINE_MAIN is defined in Core\main.h as:
[code]#else
#define DEFINE_MAIN(function) \
int main(int argc, char** argv) \
{ \
    Urho3D::ParseArguments(argc, argv); \
    return function; \
}
#endif[/code]

Now, the earlier #ifdefs are governed by "WIN32".  However the correct preprocessor define according to the VS 2015 documentation is _WIN32.  [msdn.microsoft.com/en-us/library/b0084kay.aspx](https://msdn.microsoft.com/en-us/library/b0084kay.aspx)  "Defined for applications for Win32 and Win64. Always defined."

Now, Core\main.h is an exported header file.  Why should it be assuming that a CMake define, WIN32, would be used?  Isn't a platform define _WIN32 the more correct way to do things?  [web.archive.org/web/20140625123 ... ing_system](https://web.archive.org/web/20140625123925/http://nadeausoftware.com/articles/2012/01/c_c_tip_how_use_compiler_predefined_macros_detect_operating_system) seems to indicate that _WIN32 is the correct macro for all Windows compilers, not just Visual Studio.

-------------------------

cadaver | 2017-01-02 01:08:05 UTC | #2

Historically both have been defined, so WIN32 is not just CMake-specific, but arguably _WIN32 is the correct form as you say.

-------------------------

bvanevery | 2017-01-02 01:08:06 UTC | #3

I'm not sure who used to define what, but that article says WIN32 is depreciated, which is corroborated by the VS 2015 documentation.  I'm filing a bug.

-------------------------

bvanevery | 2017-01-02 01:08:07 UTC | #4

Consumers of Urho3D, such as Urho Sample Platformer, are the ones affected.

-------------------------

