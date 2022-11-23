TheComet | 2017-08-02 15:25:56 UTC | #1

I'm trying to set up my project so all of my game code gets compiled into a shared library ```lightship```, and then two executables (server and client) link it, so server and client specific code is separated.

Here's how I set up the game library:

    include (UrhoCommon)
    set (TARGET_NAME lightship)
    define_source_files (RECURSE)
    setup_library (SHARED)
    include_directories ("include")

And here's how I set up the server executable:

    include (UrhoCommon)
    set (TARGET_NAME lightship-server)
    define_source_files (RECURSE)
    setup_main_executable (LIBS lightship)
    include_directories ("${CMAKE_SOURCE_DIR}/lightship/include")

The error I'm getting is:

    CMakeFiles/lightship-server.dir/src/main.cpp.o: In function `main':
    /home/thecomet/documents/programming/cpp/lightship-cpp/server/src/main.cpp:25: undefined reference to `Lightship::Lightship(Urho3D::Context*)'

Here's my main():

    int main(int argc, char** argv)
    {
        SharedPtr<Context> context(new Context);
        SharedPtr<Application> app(new Lightship(context));
        return app->Run();
    }

And here's my Lightship class:

    class Lightship : public Urho3D::Application
    {
    public:
        enum DebugDrawMode
        {
            DRAW_NONE = 0,
            DRAW_PHYSICS
        };

        Lightship(Urho3D::Context* context);

        virtual void Setup() override;
        virtual void Start() override;
        virtual void Stop() override;

    private:
        void RegisterSubsystems();
        void RegisterComponents();
        void LoadScene();
        void CreateCamera();
        void CreatePlayer();
        void CreateDebugHud();

        void HandleKeyDown(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
        void HandlePostRenderUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
        void HandleFileChanged(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);

        DebugDrawMode debugDrawMode_;

        Urho3D::SharedPtr<TrackingCamera> trackingCamera_;
        Urho3D::SharedPtr<MapState> map_;
        Urho3D::SharedPtr<Urho3D::Scene> scene_;
        Urho3D::SharedPtr<Urho3D::XMLFile> xmlScene_;
        Urho3D::SharedPtr<Urho3D::DebugHud> debugHud_;
    };

-------------------------

weitjong | 2017-08-02 15:51:12 UTC | #2

Try to set all the variables before calling the macro. The LIBS is a variable, not a macro argument so you cannot pass the value in the manner you posted above.

-------------------------

TheComet | 2017-08-02 17:23:29 UTC | #3

I tried, it still fails. I also tried calling target_link_libraries (lightship-server lightship) and the same thing happens.

Interestingly it works if the game library is static instead of shared.

Here's the updated config

    set (TARGET_NAME lightship-server)
    set (LIBS lightship)
    define_source_files (RECURSE)
    setup_main_executable ()
    include_directories ("${CMAKE_SOURCE_DIR}/lightship/include")

-------------------------

weitjong | 2017-08-02 22:04:38 UTC | #4

Our `setup_main_executable()` macro internally calls the same CMake `target_link_libraries()` command. You have different observation between static and shared library type then it is the setup for your library target that has problem. The linker may have optimizes out most of your symbols when you build your own shared lib. But I am just speculating here.

-------------------------

TheComet | 2017-08-02 22:27:14 UTC | #5

I figured out what's going on, but I am not sure how to "properly" fix it.

UrhoCommon.cmake has the line:

`set (CMAKE_CXX_VISIBILITY_PRESET hidden)`

By calling ```include (UrhoCommon)``` (which, as we established earlier, is required for find_package() to work), all subsequent targets will be compiled with CMAKE_CXX_VISIBILITY_PRESET=hidden which in my case is not desirable.

I currently just set it back to default after the find_package() call. There's probably a better solution.

-------------------------

weitjong | 2017-08-03 00:42:02 UTC | #6

No. Although you are right to point out that is why the symbols are hidden when building a shared library using our common module, that is not the place that needs fixing. See https://gcc.gnu.org/wiki/Visibility.

-------------------------

TheComet | 2017-08-03 13:06:53 UTC | #7

That's cool, I didn't know GCC supported visibility. I fixed things up with proper import/export macros like on windows using the visibility attributes and now it works fine.

-------------------------

weitjong | 2017-08-03 13:40:37 UTC | #8

Glad to hear that. It works on Clang too, BTW.

-------------------------

