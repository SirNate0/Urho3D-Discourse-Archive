TheComet | 2017-01-02 01:10:02 UTC | #1

The majority of times when I close my Urho3D application, it ends up aborting here:
[code]void RefCounted::ReleaseRef()
{
    assert(refCount_->refs_ > 0); // this assertion fails
    (refCount_->refs_)--;
    if (!refCount_->refs_)
        delete this;
}[/code]

Very, very rarely, the application actually exits normally. Other times it will also [b]delete[/b] twice, corrupting memory. The callstack always leads to Context::~Context().

What's causing this? Due to the random nature of this bug I assume a RefCounted object is being shared between multiple threads, causing a race condition. The code for reproducing this issue is my project, which can be found here: [url]https://github.com/thecomet93/hound[/url]

Some notable things that (may) be related?

I use SharedPtr where possible:
[code]	Urho3D::SharedPtr<Urho3D::Scene> scene_;
	Urho3D::SharedPtr<Urho3D::Node> playerNode_;
	Urho3D::SharedPtr<Urho3D::Node> cameraNode_;
	Urho3D::SharedPtr<PlayerController> playerController_;
	Urho3D::SharedPtr<CameraController> cameraController_;[/code]

I Clear() my shared pointers in Stop():
[code]void Hound::Stop()
{
	cameraController_.Reset();
	cameraNode_.Reset();

	playerController_.Reset();
	playerNode_.Reset();

	scene_.Reset();
}[/code]

I don't think this is wrong though. If I change those 5 SharedPtr's above to be raw pointers, it still crashes.

[EDIT] Oh yeah, info.

[code]Urho3D version is commit hash 213be51f920723a83b89b732bbbf9e01237d392e (current master).

$ gcc --version
gcc (Gentoo 4.9.3 p1.2, pie-0.6.3) 4.9.3

$ cmake --version
cmake version 3.0.2

$ uname -a
Linux twilight 4.1.15-gentoo-r1 #1 SMP Tue Jan 26 22:45:39 CET 2016 x86_64 AMD Phenom(tm) II X6 1090T Processor AuthenticAMD GNU/Linux

$ cmake -L
CMAKE_BUILD_TYPE:STRING=Debug
CMAKE_INSTALL_PREFIX:PATH=/usr/urho3d
URHO3D_64BIT:BOOL=ON
URHO3D_ANGELSCRIPT:BOOL=ON
URHO3D_DATABASE_ODBC:BOOL=OFF
URHO3D_DATABASE_SQLITE:BOOL=OFF
URHO3D_DEPLOYMENT_TARGET:STRING=native
URHO3D_DOCS:BOOL=OFF
URHO3D_DOCS_QUIET:BOOL=OFF
URHO3D_EXTRAS:BOOL=OFF
URHO3D_FILEWATCHER:BOOL=ON
URHO3D_LIB_TYPE:STRING=STATIC
URHO3D_LOGGING:BOOL=ON
URHO3D_LUA:BOOL=ON
URHO3D_LUAJIT:BOOL=OFF
URHO3D_LUA_RAW_SCRIPT_LOADER:BOOL=ON
URHO3D_NAVIGATION:BOOL=ON
URHO3D_NETWORK:BOOL=ON
URHO3D_PACKAGING:BOOL=OFF
URHO3D_PCH:BOOL=ON
URHO3D_PHYSICS:BOOL=ON
URHO3D_PROFILING:BOOL=ON
URHO3D_SAFE_LUA:BOOL=ON
URHO3D_SAMPLES:BOOL=OFF
URHO3D_SSE:BOOL=ON
URHO3D_TESTING:BOOL=OFF
URHO3D_THREADING:BOOL=ON
URHO3D_TOOLS:BOOL=OFF
URHO3D_URHO2D:BOOL=ON[/code]

-------------------------

TheComet | 2017-01-02 01:10:03 UTC | #2

Turns out this issue is directly related with this: [url]http://discourse.urho3d.io/t/solved-loading-resource-after-releaseref-segfaults/1777/1[/url]

-------------------------

