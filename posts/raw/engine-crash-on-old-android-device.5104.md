att | 2019-04-15 03:08:59 UTC | #1

I build my game for nexus 4(android version 5.1.1), debug version or release with debug info can run success, but release without debug info crash every time, the crash log is following,

--------- beginning of crash
F/google-breakpad(30269): Microdump skipped (uninteresting)
W/google-breakpad(30094): ### ### ### ### ### ### ### ### ### ### ### ### ###
W/google-breakpad(30094): Chrome build fingerprint:
W/google-breakpad(30094): 68.0.3440.91
W/google-breakpad(30094): 344009100
W/google-breakpad(30094): ### ### ### ### ### ### ### ### ### ### ### ### ###
F/libc    (30094): Fatal signal 7 (SIGBUS), code 1, fault addr 0xb90f5de5 in tid 30239 (SDLThread)
I/DEBUG   (  194): *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
I/DEBUG   (  194): Build fingerprint: 'google/occam/mako:5.1.1/LMY48T/2237560:user/release-keys'
I/DEBUG   (  194): Revision: '11'
I/DEBUG   (  194): ABI: 'arm'
I/DEBUG   (  194): pid: 30094, tid: 30239, name: SDLThread  >>> ********************** <<<
I/DEBUG   (  194): signal 7 (SIGBUS), code 1 (BUS_ADRALN), fault addr 0xb90f5de5
I/DEBUG   (  194):     r0 b90f5df5  r1 b90f5de5  r2 00000010  r3 b90f7a08
I/DEBUG   (  194):     r4 0000000c  r5 00000010  r6 3f800000  r7 93ef46b8
I/DEBUG   (  194):     r8 b90f7a04  r9 00000000  sl b90f07d0  fp b90f0788
I/DEBUG   (  194):     ip b6dea64c  sp 93ef46a8  lr b6da6259  pc a349b3c2  cpsr 200f0030
I/DEBUG   (  194): 
I/DEBUG   (  194): backtrace:
I/DEBUG   (  194):     #00 pc 002f63c2  /data/app/**********************-1/lib/arm/libgame.so (Urho3D::VectorBuffer::Write(void const*, unsigned int)+79)
I/DEBUG   (  194):     #01 pc 002f6ca1  /data/app/**********************-1/lib/arm/libgame.so (Urho3D::Serializer::WriteVariantData(Urho3D::Variant const&)+72)
I/DEBUG   (  194):     #02 pc 002f6c4b  /data/app/**********************-1/lib/arm/libgame.so (Urho3D::Serializer::WriteVariant(Urho3D::Variant const&)+24)
I/DEBUG   (  194):     #03 pc 00329a2f  /data/app/**********************-1/lib/arm/libgame.so (Urho3D::Material::RefreshShaderParameterHash()+58)
I/DEBUG   (  194):     #04 pc 00327335  /data/app/**********************-1/lib/arm/libgame.so (Urho3D::Material::ResetToDefaults()+584)
I/DEBUG   (  194):     #05 pc 0032700b  /data/app/**********************-1/lib/arm/libgame.so (Urho3D::Material::Material(Urho3D::Context*)+138)
I/DEBUG   (  194):     #06 pc 0030b9b5  /data/app/**********************-1/lib/arm/libgame.so (Urho3D::Renderer::Initialize()+200)
I/DEBUG   (  194):     #07 pc 003540a7  /data/app/**********************-1/lib/arm/libgame.so (Urho3D::Object::OnEvent(Urho3D::Object*, Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)+88)
I/DEBUG   (  194):     #08 pc 003547ff  /data/app/**********************-1/lib/arm/libgame.so (Urho3D::Object::SendEvent(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)+382)
I/DEBUG   (  194):     #09 pc 00318f87  /data/app/**********************-1/lib/arm/libgame.so (Urho3D::Graphics::SetMode(int, int, bool, bool, bool, bool, bool, bool, int, int, int)+1106)
I/DEBUG   (  194):     #10 pc 0034a4eb  /data/app/**********************-1/lib/arm/libgame.so (Urho3D::Engine::Initialize(Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant> const&)+1794)
I/DEBUG   (  194):     #11 pc 0034f3e5  /data/app/**********************-1/lib/arm/libgame.so (Urho3D::Application::Run()+40)
I/DEBUG   (  194):     #12 pc 00227115  /data/app/**********************-1/lib/arm/libgame.so
I/DEBUG   (  194):     #13 pc 002763e5  /data/app/**********************-1/lib/arm/libgame.so (Java_org_libsdl_app_SDLActivity_nativeRunMain+456)
I/DEBUG   (  194):     #14 pc 002484dd  /data/dalvik-cache/arm/data@app@**********************-1@base.apk@classes.dex

I think the engine failed to initialized, but can not fixed why,
has somebody encountered this problem?

-------------------------

weitjong | 2019-04-15 16:13:30 UTC | #2

Does it happen on your app only or also on the samples provided by Urho3D project?

It's a long shot but if I were you then I would try to modify the compiler flags for the Release build config to override the effective optimization level from O3 to O2, then O2 to O1, to see if makes any difference.

-------------------------

orefkov | 2019-04-15 20:44:42 UTC | #3

I report early about it - https://github.com/urho3d/Urho3D/issues/2386
I don't know, is it was fixed in main sources.

-------------------------

att | 2019-04-16 02:08:47 UTC | #4

I haven't test on samples, for now just found on myself game, later I will make test as you said.

-------------------------

