umen | 2017-01-02 00:58:51 UTC | #1

Hello all ( this scenario i tested 3 times with same results each time ) 
1. i compiled static ./ios-Build/build/Debug-iphoneos/libUrho3D.a
2. created new project as it written in : [urho3d.github.io/documentation/a00004.html](http://urho3d.github.io/documentation/a00004.html)  named : myProjectTest2
3. in the source directory i copied the sources from hello world 
in this directory i created the CMakeList.txt that looks like this:
[code]# Set project name
project (myProjectTest2)
# Set minimum version
cmake_minimum_required (VERSION 2.8.6)
if (COMMAND cmake_policy)
    cmake_policy (SET CMP0003 NEW)
endif ()
# Set CMake modules search path
set (CMAKE_MODULE_PATH $ENV{URHO3D_HOME}/Source/CMake/Modules CACHE PATH "Path to Urho3D-specific CMake modules")
# Include Urho3D Cmake common module
include (Urho3D-CMake-common)
# Find Urho3D library
find_package (Urho3D REQUIRED)
include_directories (${URHO3D_INCLUDE_DIRS})
# Define target name
set (TARGET_NAME Main)
# Define source files
define_source_files ()
# Setup target with resource copying
setup_main_executable ()[/code]
4. run the cmake_ios.sh 
the output :
[code]meirs-Mac-mini:myProjectTest2 meiryanovich$ ./cmake_ios.sh 
-- The C compiler identification is Clang 5.1.0
-- The CXX compiler identification is Clang 5.1.0
-- Check for working C compiler using: Xcode
-- Check for working C compiler using: Xcode -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler using: Xcode
-- Check for working CXX compiler using: Xcode -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Found Urho3D: /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/Urho3D/ios-Lib/libUrho3D.a
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/myProjectTest2/ios-Build
[/code]

as i understand the cmake run passed succesfully 

5. load the Xcode project myProjectTest2.xcodeproj from myProjectTest2/ios-Build
every thing in the configuration looks fine and i try to build it but i got 69 linking errors that looks like this :
[code]
d /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/myProjectTest2/ios-Bin/Main.app/Main normal i386
    cd /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/myProjectTest2/Source
    export IPHONEOS_DEPLOYMENT_TARGET=7.1
    export PATH="/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/usr/bin:/Applications/Xcode.app/Contents/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ -arch i386 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator7.1.sdk -L/Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/myProjectTest2/ios-Bin -F/Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/myProjectTest2/ios-Bin -filelist /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/myProjectTest2/ios-Build/myProjectTest2.build/Debug-iphonesimulator/Main.build/Objects-normal/i386/Main.LinkFileList -Xlinker -objc_abi_version -Xlinker 2 -framework AudioToolbox -framework CoreAudio -framework CoreGraphics -framework Foundation -framework OpenGLES -framework QuartzCore -framework UIKit -Wl,-search_paths_first -Wl,-headerpad_max_install_names /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/Urho3D/ios-Lib/libUrho3D.a -ldl -lpthread -lpthread -lpthread -Xlinker -no_implicit_dylibs -mios-simulator-version-min=7.1 -Xlinker -dependency_info -Xlinker /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/myProjectTest2/ios-Build/myProjectTest2.build/Debug-iphonesimulator/Main.build/Objects-normal/i386/Main_dependency_info.dat -o /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/myProjectTest2/ios-Bin/Main.app/Main

ld: warning: ignoring file /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/Urho3D/ios-Lib/libUrho3D.a, missing required architecture i386 in file /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/Urho3D/ios-Lib/libUrho3D.a (2 slices)
Undefined symbols for architecture i386:
  "Urho3D::RefCounted::ReleaseRef()", referenced from:
      Urho3D::SharedPtr<Urho3D::Text>::ReleaseRef() in HelloWorld.o
      Urho3D::SharedPtr<HelloWorld>::ReleaseRef() in HelloWorld.o
      Urho3D::SharedPtr<Urho3D::Context>::ReleaseRef() in HelloWorld.o
      Urho3D::SharedPtr<Urho3D::Sprite>::ReleaseRef() in HelloWorld.o
      Urho3D::SharedPtr<Urho3D::Engine>::ReleaseRef() in HelloWorld.o
  "Urho3D::RefCounted::AddRef()", referenced from:
      Urho3D::SharedPtr<Urho3D::Text>::AddRef() in HelloWorld.o
      Urho3D::SharedPtr<HelloWorld>::AddRef() in HelloWorld.o
      Urho3D::SharedPtr<Urho3D::Context>::AddRef() in HelloWorld.o
      Urho3D::SharedPtr<Urho3D::Sprite>::AddRef() in HelloWorld.o
  "Urho3D::StringHash::StringHash(char const*)", referenced from:
      ___cxx_global_var_init in HelloWorld.o
      ___cxx_global_var_init5 in HelloWorld.o
      ___cxx_global_var_init8 in HelloWorld.o
      ___cxx_global_var_init11 in HelloWorld.o
      ___cxx_global_var_init14 in HelloWorld.o
      ___cxx_global_var_init17 in HelloWorld.o
      ___cxx_global_var_init19 in HelloWorld.o
      ...
  "Urho3D::Application::Run()", referenced from:
      RunApplication() in HelloWorld.o
  "Urho3D::Application::Application(Urho3D::Context*)", referenced from:
      Sample::Sample(Urho3D::Context*) in HelloWorld.o
  "Urho3D::AllocatorFree(Urho3D::AllocatorBlock*, void*)", referenced from:
      Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>::FreeNode(Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>::Node*) in HelloWorld.o
  "Urho3D::ResourceCache::GetResource(Urho3D::ShortStringHash, char const*, bool)", referenced from:
      Urho3D::Texture2D* Urho3D::ResourceCache::GetResource<Urho3D::Texture2D>(char const*, bool) in HelloWorld.o
      Urho3D::Image* Urho3D::ResourceCache::GetResource<Urho3D::Image>(char const*, bool) in HelloWorld.o
      Urho3D::XMLFile* Urho3D::ResourceCache::GetResource<Urho3D::XMLFile>(char const*, bool) in HelloWorld.o
      Urho3D::Font* Urho3D::ResourceCache::GetResource<Urho3D::Font>(char const*, bool) in HelloWorld.o
  "Urho3D::ParseArguments(int, char**)", referenced from:
      _SDL_main in HelloWorld.o
  "Urho3D::ShortStringHash::ShortStringHash(char const*)", referenced from:
      Sample::Setup() in HelloWorld.o
      ___cxx_global_var_init1 in HelloWorld.o
      ___cxx_global_var_init3 in HelloWorld.o
      ___cxx_global_var_init7 in HelloWorld.o
      ___cxx_global_var_init10 in HelloWorld.o
      ___cxx_global_var_init13 in HelloWorld.o
      ___cxx_global_var_init16 in HelloWorld.o
      ...
  "Urho3D::AllocatorReserve(Urho3D::AllocatorBlock*)", referenced from:
      Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>::ReserveNode(Urho3D::ShortStringHash const&, Urho3D::Variant const&) in HelloWorld.o
  "Urho3D::AllocatorUninitialize(Urho3D::AllocatorBlock*)", referenced from:
      Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>::~HashMap() in HelloWorld.o
  "Urho3D::Text::SetFont(Urho3D::Font*, int)", referenced from:
      HelloWorld::CreateText() in HelloWorld.o
  "Urho3D::Text::SetText(Urho3D::String const&)", referenced from:
      HelloWorld::CreateText() in HelloWorld.o
  "Urho3D::Text::Text(Urho3D::Context*)", referenced from:
      HelloWorld::CreateText() in HelloWorld.o
  "Urho3D::Time::GetTimeStamp()", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Color::BLUE", referenced from:
      ___cxx_global_var_init144 in HelloWorld.o
  "Urho3D::Image::Image(Urho3D::Context*)", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Image::~Image()", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Engine::CreateConsole()", referenced from:
      Sample::CreateConsoleAndDebugHud() in HelloWorld.o
  "Urho3D::Engine::CreateDebugHud()", referenced from:
      Sample::CreateConsoleAndDebugHud() in HelloWorld.o
  "Urho3D::Engine::Exit()", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Object::SubscribeToEvent(Urho3D::StringHash, Urho3D::EventHandler*)", referenced from:
      Sample::Start() in HelloWorld.o
      HelloWorld::SubscribeToEvents() in HelloWorld.o
  "Urho3D::Object::OnEvent(Urho3D::Object*, Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&)", referenced from:
      vtable for Sample in HelloWorld.o
      vtable for HelloWorld in HelloWorld.o
      vtable for Urho3D::Application in HelloWorld.o
  "Urho3D::Object::~Object()", referenced from:
      Urho3D::Application::~Application() in HelloWorld.o
  "Urho3D::Sprite::SetHotSpot(int, int)", referenced from:
      Sample::CreateLogo() in HelloWorld.o
  "Urho3D::Sprite::SetTexture(Urho3D::Texture*)", referenced from:
      Sample::CreateLogo() in HelloWorld.o
  "Urho3D::Sprite::SetScale(float)", referenced from:
      Sample::CreateLogo() in HelloWorld.o
  "Urho3D::String::EMPTY", referenced from:
      Sample::CreateLogo() in HelloWorld.o
  "Urho3D::String::Resize(unsigned int)", referenced from:
      Urho3D::String::operator+(char const*) const in HelloWorld.o
      Urho3D::String::operator+(Urho3D::String const&) const in HelloWorld.o
      Urho3D::String::operator=(char const*) in HelloWorld.o
      Urho3D::String::operator=(Urho3D::String const&) in HelloWorld.o
  "Urho3D::String::endZero", referenced from:
      Urho3D::String::String() in HelloWorld.o
      Urho3D::String::String(char const*) in HelloWorld.o
  "Urho3D::Console::SetVisible(bool)", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Console::SetDefaultStyle(Urho3D::XMLFile*)", referenced from:
      Sample::CreateConsoleAndDebugHud() in HelloWorld.o
  "Urho3D::Console::Toggle()", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Context::Context()", referenced from:
      RunApplication() in HelloWorld.o
  "Urho3D::Variant::SetType(Urho3D::VariantType)", referenced from:
      Urho3D::Variant::operator=(Urho3D::String const&) in HelloWorld.o
      Urho3D::Variant::operator=(bool) in HelloWorld.o
      Urho3D::Variant::~Variant() in HelloWorld.o
  "Urho3D::Variant::operator=(Urho3D::Variant const&)", referenced from:
      Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>::InsertNode(Urho3D::ShortStringHash const&, Urho3D::Variant const&, bool) in HelloWorld.o
      Urho3D::Variant::Variant(Urho3D::Variant const&) in HelloWorld.o
  "Urho3D::DebugHud::SetDefaultStyle(Urho3D::XMLFile*)", referenced from:
      Sample::CreateConsoleAndDebugHud() in HelloWorld.o
  "Urho3D::DebugHud::ToggleAll()", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Graphics::SetWindowIcon(Urho3D::Image*)", referenced from:
      Sample::SetWindowTitleAndIcon() in HelloWorld.o
  "Urho3D::Graphics::SetWindowTitle(Urho3D::String const&)", referenced from:
      Sample::SetWindowTitleAndIcon() in HelloWorld.o
  "Urho3D::Graphics::TakeScreenShot(Urho3D::Image&)", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::HashBase::AllocateBuckets(unsigned int, unsigned int)", referenced from:
      Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>::InsertNode(Urho3D::ShortStringHash const&, Urho3D::Variant const&, bool) in HelloWorld.o
  "Urho3D::HashBase::ResetPtrs()", referenced from:
      Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>::Clear() in HelloWorld.o
  "Urho3D::Renderer::SetDrawShadows(bool)", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Renderer::SetShadowMapSize(int)", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Renderer::SetShadowQuality(int)", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Renderer::SetTextureQuality(int)", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Renderer::SetMaterialQuality(int)", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Renderer::SetSpecularLighting(bool)", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Renderer::SetDynamicInstancing(bool)", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Renderer::SetMaxOccluderTriangles(int)", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::UIElement::SetOpacity(float)", referenced from:
      Sample::CreateLogo() in HelloWorld.o
  "Urho3D::UIElement::SetVisible(bool)", referenced from:
      Sample::SetLogoVisible(bool) in HelloWorld.o
  "Urho3D::UIElement::CreateChild(Urho3D::ShortStringHash, Urho3D::String const&, unsigned int)", referenced from:
      Urho3D::Sprite* Urho3D::UIElement::CreateChild<Urho3D::Sprite>(Urho3D::String const&, unsigned int) in HelloWorld.o
  "Urho3D::UIElement::SetPriority(int)", referenced from:
      Sample::CreateLogo() in HelloWorld.o
  "Urho3D::UIElement::SetAlignment(Urho3D::HorizontalAlignment, Urho3D::VerticalAlignment)", referenced from:
      Sample::CreateLogo() in HelloWorld.o
  "Urho3D::UIElement::SetVerticalAlignment(Urho3D::VerticalAlignment)", referenced from:
      HelloWorld::CreateText() in HelloWorld.o
  "Urho3D::UIElement::SetHorizontalAlignment(Urho3D::HorizontalAlignment)", referenced from:
      HelloWorld::CreateText() in HelloWorld.o
  "Urho3D::UIElement::SetSize(int, int)", referenced from:
      Sample::CreateLogo() in HelloWorld.o
  "Urho3D::UIElement::AddChild(Urho3D::UIElement*)", referenced from:
      HelloWorld::CreateText() in HelloWorld.o
  "Urho3D::UIElement::SetColor(Urho3D::Color const&)", referenced from:
      HelloWorld::CreateText() in HelloWorld.o
  "Urho3D::FileSystem::GetProgramDir() const", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Image::SavePNG(Urho3D::String const&) const", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Object::GetSubsystem(Urho3D::ShortStringHash) const", referenced from:
      Urho3D::ResourceCache* Urho3D::Object::GetSubsystem<Urho3D::ResourceCache>() const in HelloWorld.o
      Urho3D::UI* Urho3D::Object::GetSubsystem<Urho3D::UI>() const in HelloWorld.o
      Urho3D::Graphics* Urho3D::Object::GetSubsystem<Urho3D::Graphics>() const in HelloWorld.o
      Urho3D::Console* Urho3D::Object::GetSubsystem<Urho3D::Console>() const in HelloWorld.o
      Urho3D::DebugHud* Urho3D::Object::GetSubsystem<Urho3D::DebugHud>() const in HelloWorld.o
      Urho3D::Renderer* Urho3D::Object::GetSubsystem<Urho3D::Renderer>() const in HelloWorld.o
      Urho3D::FileSystem* Urho3D::Object::GetSubsystem<Urho3D::FileSystem>() const in HelloWorld.o
      ...
  "Urho3D::String::Replaced(char, char, bool) const", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "Urho3D::Console::IsVisible() const", referenced from:
      Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) in HelloWorld.o
  "typeinfo for Urho3D::Object", referenced from:
      typeinfo for Urho3D::Application in HelloWorld.o
  "_main", referenced from:
      start in crt1.o
     (maybe you meant: _SDL_main)
ld: symbol(s) not found for architecture i386
clang: error: linker command failed with exit code 1 (use -v to see invocation)

[/code]

what did i do wrong here ?
Thanks

-------------------------

weitjong | 2017-01-02 00:58:51 UTC | #2

Did you build a 64-bit only static library? If you did then you also need to enable 64-bit build option for your own project.

-------------------------

umen | 2017-01-02 00:58:52 UTC | #3

no they both using : $(ARCHS_STANDARD_32_BIT)  
and arm64 armv7 armv7s
and all other configurations are the same

-------------------------

weitjong | 2017-01-02 00:58:52 UTC | #4

[quote]ld: symbol(s) not found for architecture i386[/quote]

Ok. In that case, I think you have not built the lib for iphonesimulator but your app is trying to build for iphonesimulator. On iOS platform, there is a custom target (Urho3D_universal) to build the Urho3D library as Mach-O universal binary consists of iphoneos and iphomesimulator archs.

-------------------------

umen | 2017-01-02 00:58:52 UTC | #5

Thanks for the fast replay .
i builded the main Urho3D build with Urho3D_universal target every thing compiled fine 
when i tried to build my test app i got another link error :
again same config on both 

[code]



Ld /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/myProjectTest2/ios-Build/myProjectTest2.build/Debug-iphoneos/Main.build/Objects-normal/armv7/Main normal armv7
    cd /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/myProjectTest2/Source
    export IPHONEOS_DEPLOYMENT_TARGET=7.1
    export PATH="/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin:/Applications/Xcode.app/Contents/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ -arch armv7 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS7.1.sdk -L/Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/myProjectTest2/ios-Bin -F/Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/myProjectTest2/ios-Bin -filelist /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/myProjectTest2/ios-Build/myProjectTest2.build/Debug-iphoneos/Main.build/Objects-normal/armv7/Main.LinkFileList -dead_strip -framework AudioToolbox -framework CoreAudio -framework CoreGraphics -framework Foundation -framework OpenGLES -framework QuartzCore -framework UIKit -Wl,-search_paths_first -Wl,-headerpad_max_install_names /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/Urho3D/ios-Lib/libUrho3D.a -ldl -lpthread -lpthread -lpthread -miphoneos-version-min=7.1 -Xlinker -dependency_info -Xlinker /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/myProjectTest2/ios-Build/myProjectTest2.build/Debug-iphoneos/Main.build/Objects-normal/armv7/Main_dependency_info.dat -o /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/myProjectTest2/ios-Build/myProjectTest2.build/Debug-iphoneos/Main.build/Objects-normal/armv7/Main

ld: warning: ignoring file /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/Urho3D/ios-Lib/libUrho3D.a, file was built for archive which is not the architecture being linked (armv7): /Users/meiryanovich/Documents/3d/urho3d/git/Urho3d_2/Urho3D/ios-Lib/libUrho3D.a
ld: entry point (_main) undefined. for architecture armv7
clang: error: linker command failed with exit code 1 (use -v to see invocation)
[/code]

what does it mean now ?

-------------------------

weitjong | 2017-01-02 00:58:52 UTC | #6

It seems to me that you have changed the deployment target (from simulator to iOS device) in between your posts. Though that should not be the root cause of your problem, it will help us to help you if you stated what have you changed in between explicitly. Anyhow, from the output it shows that your lib does not have armv7 arch. To verify that, you can use Apple "lipo" command line tool with option "-info" or "-detailed_info". Have you manually tinkered the ARCHS or VALID_ARCHS in the CMake-generated Xcode project file?

Sorry for not able to be more helpful than this.

-------------------------

umen | 2017-01-02 00:58:52 UTC | #7

Hey 
well first thing i did in the morning before all family woke up 
i did clean build and then clean the test  project and you are right the project was just mest up .
every thing is working and compiled now . 
Thanks for pointing me about the lipo tool ( I'm new to mac) .
have a nice day !

-------------------------

