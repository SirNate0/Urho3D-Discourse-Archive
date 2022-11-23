rku | 2018-04-20 17:46:35 UTC | #1

For few months i was working on a C# bindings generator for Urho3D. I am at the point where while still experimental it already looks like it could be usable. Be aware that project is made with my fork in mind, which is a little bit different from upstream Urho3D. However things generator depends upon are few and minor and i would love to get them upstreamed.

A recap on the features: https://github.com/rokups/Urho3D/wiki/C%23-support
Repository with bindings generator: https://github.com/rokups/Urho3D, build with `-DURHO3D_CSHARP=ON`.
Repository contains sample `102_CSharpProject` written in C#.

Differences from urhosharp:
* Also works with .net framework
* Supports inheriting c++ classes and overriding their virtual methods
* Supports multiple inheritance
* Supports serializing and deserializing managed objects without magical patches to the source
* Supports access of protected class members
* Getters and setters are converted to C# properties
* 

Demo:
```cs
using System;
using System.Diagnostics;
using System.IO;
using Urho3D;

namespace DemoApplication
{
    [ObjectFactory]
    class RotateObject : LogicComponent
    {
        public RotateObject(Context context) : base(context)
        {
            UpdateEventMask = UseUpdate;
        }

        public override void Update(float timeStep)
        {
            var d = new Quaternion(10 * timeStep, 20 * timeStep, 30 * timeStep);
            Node.Rotate(d);
        }
    }

    class DemoApplication : Application
    {
        private Scene _scene;
        private Viewport _viewport;
        private Node _camera;
        private Node _cube;
        private Node _light;

        public DemoApplication(Context context) : base(context)
        {
        }

        public override void Setup()
        {
            var currentDir = Directory.GetCurrentDirectory();
            EngineParameters[EngineDefs.EpFullScreen] = false;
            EngineParameters[EngineDefs.EpWindowWidth] = 1920;
            EngineParameters[EngineDefs.EpWindowHeight] = 1080;
            EngineParameters[EngineDefs.EpWindowTitle] = "Hello C#";
            EngineParameters[EngineDefs.EpResourcePrefixPaths] = $"{currentDir};{currentDir}/..";
        }

        public override void Start()
        {
            Input.SetMouseVisible(true);

            // Viewport
            _scene = new Scene(Context);
            _scene.CreateComponent<Octree>();

            _camera = _scene.CreateChild("Camera");
            _viewport = new Viewport(Context, _scene, _camera.CreateComponent<Camera>());
            Renderer.SetViewport(0, _viewport);

            // Background
            Renderer.DefaultZone.FogColor = new Color(0.5f, 0.5f, 0.7f);

            // Scene
            _camera.Position = new Vector3(0, 2, -2);
            _camera.LookAt(Vector3.Zero);

            // Cube
            _cube = _scene.CreateChild("Cube");
            var model = _cube.CreateComponent<StaticModel>();
            model.Model = Cache.GetResource<Model>("Models/Box.mdl");
            model.SetMaterial(0, Cache.GetResource<Material>("Materials/Stone.xml"));
            _cube.CreateComponent<RotateObject>();

            // Light
            _light = _scene.CreateChild("Light");
            _light.CreateComponent<Light>();
            _light.Position = new Vector3(0, 2, -1);
            _light.LookAt(Vector3.Zero);

            SubscribeToEvent(CoreEvents.E_UPDATE, args =>
            {
                var timestep = args[Update.P_TIMESTEP].Float;
                Debug.Assert(this != null);
            });
        }
    }

    internal class Program
    {
        public static void Main(string[] args)
        {
            using (var context = new Context())
            {
                using (var application = new DemoApplication(context))
                {
                    application.Run();
                }
            }
        }
    }
}
```

-------------------------

Sinoid | 2018-03-26 02:55:02 UTC | #2

Are the generated bindings ephemeral (ie. Fody magic) or could you toss them into a dump repo? Curious what they look like, but not enough set it up (point @ canonical llvm install dir, vs2015, etc).

-------------------------

Omid | 2018-03-26 06:45:57 UTC | #3

Looks nice. Good job . Why you are not helping UrhoSharp team to do them all there? 
UrhoSharp already is famous and it's used in lot of projects. If you apply your changes there then it's will be use in existing projects too.
And you make me happy too :grin:

-------------------------

rku | 2018-03-26 07:25:00 UTC | #4

[quote="Sinoid, post:2, topic:4119"]
Are the generated bindings ephemeral (ie. Fody magic) or could you toss them into a dump repo?
[/quote]

They could totally be in their own repo. Actually with a tiny bit effort (sorting of input headers) these bindings would become reproducible as well, so tiny changes would result in tiny diffs in the binding output.

[quote="Sinoid, post:2, topic:4119"]
Curious what they look like
[/quote]
This is current full output: https://gist.github.com/rokups/e1239dd2500a4460d92c055e879e8ef9

[quote="Sinoid, post:2, topic:4119"]
point @ canonical llvm install dir, vs2015
[/quote]
Yeah llvm thingy needs fixing, build system does not like spaces. Recommendation is just a workaround as i was pushing fast for windows build.
Actually yesterday we got it working with vs2015. Had to remove single `constexpr` as it was optional anyway. Also fixed several other bugs that cropped up. @Eugene had luck testing it with vs2015.

[quote="Omid, post:3, topic:4119"]
Why you are not helping UrhoSharp team to do them all there?
[/quote]
I believe their methods are broken and their bindings are broken. It will never be possible to use urhosharp with upstream Urho3D while making my bindings work with upstream project would not be that hard, just need a few tiny changes, where urhosharp sprinkles magic calls around the engine in order to compensate for lack of virtual method overriding support. Also urhosharp bindings generator works only on MacOS. This is simply not acceptable.

---

Also i would like too point out that these bindings are **unsafe**. Unsafe in a sense that you have to mind what you are doing. For example anything that does not inherit RefCounted may be freed by engine while you holding a reference to it.

For example you may not keep reference to `Application.EngineParameters` yourself, because lifetime of `EngineParameters` is managed by it's parent class. Wrapper must return a reference, otherwise we will not be able to modify it. So if you kept reference to `EngineParameters` and freed your `Application` subclass things would go boom.

-------------------------

Eugene | 2018-03-26 09:07:42 UTC | #5

@Egorbo that's what I talked about.
Is there any chance to reuse this work in UrhoSharp?
IMO good binding should be able to bind arbitrary user C++ components, resources and things, and that's why I pin my hopes on this project.
UrhoSharp has its own feature set and community, but really lacks flexibility.

-------------------------

Omid | 2018-03-26 09:39:21 UTC | #6

I have no idea about it. I didn't deep looks to the UrhoSharp source code and you know what I know Xamarin is part of the Microsoft and I'm sure there is a big support behind that. That why I said it's good to apply your changes in that projects
There are 2 reasons. First we have centralized C# binding version. Second is all the users same as me be sure if you don't like to continue your project there is someone else exists to continue.
UrhoSharp have some binding problem I found (https://forums.xamarin.com/discussion/123514/urho-spline-class-is-not-exists-in-c) and exists more. It's good if you merge your job with that project then everybody have full version and about that I think it's a good idea to talk with @Egorbo and @migueldeicaza

By the way already UrhoSharp is bind to Android, iOS, Windows, Linux, Mac, Xamarin.Forms, and other platforms. Also you can have it in Workbooks that perfect tools who help to test and play with codes before develop something new.

-------------------------

Sinoid | 2018-03-27 07:08:45 UTC | #7

Nice touch with the commented parse-source above the binding. I'll have to mess with it and see about getting it to spit out [Odin](https://github.com/odin-lang/Odin) bindings.

-------------------------

rku | 2018-03-27 07:51:22 UTC | #8

Ah yeah i had to add these comments in CApi.cpp in order to aid making rules file (basically adding stuff to ignore).

[quote="Sinoid, post:7, topic:4119"]
I’ll have to mess with it and see about getting it to spit out Odin bindings.
[/quote]
Not sure how much of use this generator will be to you.. Most of passes are very C#-specific, whats left is rather minimal infrastructure. However if you do find it usable then that would be terrific. Me and @boberfly were already having some thoughts to also add support for python by generating code for pybind11. But that is another rather big undertaking, although probably not as big as C#. 

---

Another thingy i would like to pull off is get rid of Urho3D dependency for generator. This would allow us to build generator and generate bindings before Urho3D is built. Then we can build a monolithic Urho3D library that exports both C++ and PInvoke interfaces. Then Urho3DNet.dll would import Urho3D.dll directly instead of Urho3DCSharp.dll.

---

Edit: this method could totally be used to auto-generate bindings for AngelScript and Lua as well. Just need someone who cares about these langs to do it.. :)

-------------------------

elix22 | 2018-03-28 07:20:10 UTC | #9

Well , simply amazing work .
I have never been a C# guy , always using C++ or C (performance freak) , but this is amazing.

I am curious about the overhead imposed by InstanceCache.cs 
"GetOrAdd()"  for new instances creation or "Remove()" for removal  (using ConcurrentDictionary).
What will be the performance hit while creating and removing many objects , specifically on mobile devices.

-------------------------

rku | 2018-03-28 07:36:34 UTC | #10

Performance will suck and not even because of InstanceCache. At the moment i am working on mobile game port to android and game stutters when adding/removing too many objects even if code is written in c++.

InstanceCache sucks though. But we have a nasty problem here. What should we do when native function returns a pointer to native object? Every time create a new C# object that wraps same class? That has a potential to leak a lot of memory. If we cache things then cache may be potentially modified outside of  main thread so have to account for that. I would love us to have a better solution so if you have ideas please shoot ^_^ Also i am unsure if even with concurrent cache things are safe, because shared pointers in urho3d arent thread-safe and it is likely we will be calling `RemoveRef()` from non-main thread. But hey it worked for Atomic so maybe this will be alright :)

-------------------------

Egorbo | 2018-03-29 15:16:16 UTC | #11

[quote="rku, post:4, topic:4119"]
I believe their methods are broken and their bindings are broken. It will never be possible to use urhosharp with upstream Urho3D while making my bindings work with upstream project would not be that hard, just need a few tiny changes, where urhosharp sprinkles magic calls around the engine in order to compensate for lack of virtual method overriding support. Also urhosharp bindings generator works only on MacOS. This is simply not acceptable.
[/quote]

I use a fork for Urho3D instead of directly mainstream for two reasons:
1) Experiments - e.g. UWP support, HoloLens, etc
2) Urho3D and SDL don't support scenarios to work with Urho3D as a subview in existing apps (iOS, Android, macOS) - we just wanted to create a simple and small visualizer for (primary) non-gaming apps.
When there are no SDL changes in the upstream - it takes 15-30 minutes to update bindings and test. SDL-guys love to refactor it every update so it always break my patches.

Do you really need "virtual" methods when there are tons of events for everything which are automatically bound to C#? I agree - there is a mess in the Binder code, I am trying to rewrite it now to be more clean and easy to extend. And yes, the generator works only on macOS, but it's possible to add Linux support (and Windows via WSL) - it's just a clang with a few patches to provide bindable clang AST API to C# in order to be able to write simple generators in C# (unlike CppSharp which is quite complicated).

> InstanceCache sucks though. But we have a nasty problem here. What should we do when native function returns a pointer to native object? Every time create a new C# object that wraps same class? That has a potential to leak a lot of memory. If we cache things then cache may be potentially modified outside of main thread so have to account for that. I would love us to have a better solution so if you have ideas please shoot :slight_smile: Also i am unsure if even with concurrent cache things are safe, because shared pointers in urho3d arent thread-safe and it is likely we will be calling RemoveRef() from non-main thread. But hey it worked for Atomic so maybe this will be alright :slight_smile:

InstanceCache based on timers is really bad idea - what if your native object is deleted in Urho3D and a new one of a different type is created with the same address? And yes, RemoveRef from non-UI thread won't work.
the Atomic guys afair took my approach with a cache + callbacks from RefCounted + C# Finalizer which (if needed) dispatches RemoveRef to the game thread.
Took a quick glance to the code, especially Node - what if I serialize a component written in C# to an XML scene. Then restart app and deserialize the scene - what GetComponent<MyManagedComponent>() will return? According to your code it will be just Component, I am just trying to say there are lot of hidden details you are going to hit soon :slight_smile:

-------------------------

rku | 2018-03-29 16:21:38 UTC | #12

[quote="Egorbo, post:11, topic:4119"]
Do you really need “virtual” methods when there are tons of events for everything which are automatically bound to C#?
[/quote]

That depends. Inheriting `LogicComponent` requires overriding virtual methods. Or even creating `Application`. These can be worked around one way or the other, but my aim is to be as close to native API as possible. I do need virtuals ;)

[quote="Egorbo, post:11, topic:4119"]
And yes, the generator works only on macOS, but it’s possible to add Linux support (and Windows via WSL) - it’s just a clang with a few patches to provide bindable clang AST API to C# in order to be able to write simple generators in C# (unlike CppSharp which is quite complicated).
[/quote]

Introducing WSL to build sounds like over-complicating things. I still would not touch that :p Just like something that would require wine in order to build things on linux. That is crazy :)
To be honest i would have loved writing this bindings generator in C#, except that core of generator is cppast which is c++ lib and i just wasnt aware of anything comparable which worked in C#. Also bonus points for cppast - does not require clang patches so prebuilt binaries from llvm website can be used on windows and mac. Packages from repos can be used on linux. I spent quite some time trying to get CppSharp to work and compiling clang was a real burden.

[quote="Egorbo, post:11, topic:4119"]
InstanceCache based on timers is really bad idea - what if your native object is deleted in Urho3D and a new one of a different type is created with the same address? And yes, RemoveRef from non-UI thread won’t work.

the Atomic guys afair took my approach with a cache + callbacks from RefCounted + C# Finalizer which (if needed) dispatches RemoveRef to the game thread.
[/quote]

Ah interesting! I knew this will be source of problems. Thanks for pointing it out, ill take a look at how Atomic does things :+1:

[quote="Egorbo, post:11, topic:4119"]
Took a quick glance to the code, especially Node - what if I serialize a component written in C# to an XML scene. Then restart app and deserialize the scene - what GetComponent() will return? According to your code it will be just Component, I am just trying to say there are lot of hidden details you are going to hit soon :slight_smile:
[/quote]

Actually `GetComponent<T>()` will return whatever type you pass to it since it is generic. Or `null` if node does not have component of that type. `Node.GetComponents()` would also return array of `Component` subclasses because when deserializing XML a factory calls back into managed world to create managed instance of serialized class. Then this class ends up in the cache and next time managed wrapper sees particular pointer it will reuse instance from the cache.

This is a good point though. This problem could arise when native API returns for example `Component*` while instance is actually a native subclass of `Component`. Then wrong wrapper class instance would be created. At least for `Urho3D::Object` subclasses wrapper could inspect type `StringHash` and create instance of correct type.

---

If anything else comes to your mind please speak up. I definitely do not know all the hidden edgecases and you do have a headstart in this. Both projects definitely have things to learn from each other :+1:

-------------------------

Egorbo | 2018-03-29 16:46:56 UTC | #13

[quote="rku, post:12, topic:4119"]
Introducing WSL to build sounds like over-complicating things. I still would not touch that :stuck_out_tongue: Just like something that would require wine in order to build things on linux. That is crazy :slight_smile:
[/quote]
Well, WSL is a workaround, the patches can be applied to the windows version of Clang too I guess. WSL is not difficult to install - it's basically just an app in the app store, just click the install :smile:

> Then this class ends up in the cache and next time managed wrapper sees particular pointer it will reuse instance from the cache.

Ah, ok then, I didn't notice the factory.

> If anything else comes to your mind please speak up. I definitely do not know all the hidden edgecases and you do have a headstart in this. Both projects definitely have things to learn from each other :+1:

Ok :slight_smile:

-------------------------

rku | 2018-03-29 16:49:15 UTC | #14

[quote="Egorbo, post:13, topic:4119"]
Well, WSL is a workaround, the patches can be applied to the windows version of Clang too I guess. WSL is not difficult to install - it’s basically just an app in the app store, just click the install :smile:
[/quote]

Why is it patched though? cppast provides pretty much complete ast without patches. I am sure everyone would be happier if you could avoid depending on patched version of clang.

-------------------------

Egorbo | 2018-03-29 17:36:44 UTC | #15

it's patched to provide an API for C# in order to work with AST from C#

-------------------------

rku | 2018-04-20 17:58:36 UTC | #16

Heads-up everyone!

Important milestone was reached just now. Bindings generator was finally merged to master branch on [my repo](https://github.com/rokups/Urho3D), which means code is more useable than ever. Build it with `URHO3D_CSHARP=ON` and check out 102_CSharpProject sample.

A word of warning: hard dependency on mono was introduced therefore your mileage will wary on windows. It is pretty easy to use entire thing on linux though. I will look into windows deployment during weekend.

Also updated first post somewhat. Take a peek ;)

-------------------------

Omid | 2018-04-21 19:52:42 UTC | #17

@rku 
What should i set for LLVM_CONFIG_BINARY and Qt5Widget_DIR?

-------------------------

rku | 2018-04-22 05:09:51 UTC | #18

Build instructions on https://github.com/rokups/Urho3D/wiki/C%23-support

Not sure about Qt thing now. You can ignore it or disable profiling to get rid of the warning

-------------------------

elix22 | 2018-04-22 07:20:38 UTC | #19

On Mac only Urho3DNet.dll and libUrho3DCSharp.dylib are generated .
No Urho3D.dll and/or Urho3DCSharp.dll 

Let me know if I missed something.

mkdir build 
cd build

cmake ..  -DHAVE_CLOCK_GETTIME=0 -DURHO3D_DATABASE_SQLITE=1  -DURHO3D_CSHARP=ON -DLLVM_CONFIG_BINARY=/usr/local/opt/llvm/bin/llvm-config -DURHO3D_SAMPLES=0 -DURHO3D_PHYSICS=1 -DURHO3D_IK=1 -DURHO3D_NETWORK=1 -DURHO3D_NAVIGATION=1

cmake --build .

-------------------------

rku | 2018-04-22 07:24:38 UTC | #20

It is all good. You probably built engine as static library, this is why `libUrho3D.dylib` is not there. Engine code is in `libUrho3DCSharp.dylib` in this case. If you added `-DBUILD_SHARED_LIBS=ON` to cmake parameters then engine would be built as shared library. `libUrho3D.dylib` would be created and it would contain required C# glue code inside, there would be no `libUrho3DCSharp.dylib`.

-------------------------

elix22 | 2018-04-23 10:40:03 UTC | #21

Silly me , I read your Wiki ,
For some reason I thought  Urho3D.dll and Urho3DCSharp.dll are Dot Net Dlls 
But they are the Windows counterparts of  libUrho3D.dylib and libUrho3DCSharp.dylib.
Anyway I am getting exceptions on my Mac either using libUrho3D.dylib or libUrho3DCSharp.dylib  .
I barely used Dot Net in the past (always CPP,C,Assembly) , this is a new territory for me.
I Will have more spare time during the weekend to continue playing with it.

-------------------------

rku | 2018-04-23 12:07:23 UTC | #22

What kind of exceptions? It is true that i have not tested this code on Mac OS because no hardware. Just made sure everything compiles.

-------------------------

elix22 | 2018-04-24 03:49:19 UTC | #23

Elis-MBP:bin elialoni$ csc Program.cs  -r:Urho3DNet.dll 
Microsoft (R) Visual C# Compiler version 2.3.2.61928 (ec1cde8b)
Copyright (C) Microsoft Corporation. All rights reserved.

Elis-MBP:bin elialoni$ mono Program.exe 
mono_os_mutex_lock: pthread_mutex_lock failed with "Invalid argument" (22)
Stacktrace:

  at <unknown> <0xffffffff>
  at (wrapper managed-to-native) Urho3D.Context.Urho3DRegisterMonoInternalCalls () [0x00002] in <ac355153da7f4553b2dc9ab27641135e>:0
  at Urho3D.Context..cctor () [0x00001] in <ac355153da7f4553b2dc9ab27641135e>:0
  at (wrapper runtime-invoke) object.runtime_invoke_void (object,intptr,intptr,intptr) [0x0001e] in <e22c1963d07746cd9708456620d50e1a>:0
  at <unknown> <0xffffffff>
  at (wrapper managed-to-native) object.__icall_wrapper_mono_generic_class_init (intptr) [0x00000] in <e22c1963d07746cd9708456620d50e1a>:0
  at DemoApplication.Program.Main (string[]) [0x00001] in <b6d58905eb614a70a5ed205feb3cd371>:0
  at (wrapper runtime-invoke) <Module>.runtime_invoke_void_object (object,intptr,intptr,intptr) [0x0004e] in <b6d58905eb614a70a5ed205feb3cd371>:0

Native stacktrace:

	0   mono                                0x00000001019feb01 mono_handle_native_crash + 257
	1   libsystem_platform.dylib            0x00007fff6751ff5a _sigtramp + 26
	2   libmonosgen-2.0.1.dylib             0x000000010586a008 simple_lower_case_mapping_higharea_table0 + 20520
	3   libsystem_c.dylib                   0x00007fff672bd1ae abort + 127
	4   libmonosgen-2.0.1.dylib             0x00000001057aca52 monoeg_g_log + 0
	5   libmonosgen-2.0.1.dylib             0x00000001057ac9d7 monoeg_g_logv + 83
	6   libmonosgen-2.0.1.dylib             0x00000001057acaca monoeg_g_log + 120
	7   libmonosgen-2.0.1.dylib             0x00000001056a444e mono_icall_lock + 72
	8   libmonosgen-2.0.1.dylib             0x00000001056a43c4 mono_add_internal_call + 21
	9   libUrho3DCSharp.dylib               0x000000010439a1ba Urho3DRegisterMonoInternalCalls + 26
	10  ???                                 0x0000000101ecf527 0x0 + 4327273767
	11  mono                                0x0000000101953a07 mono_jit_runtime_invoke + 1383
	12  mono                                0x0000000101b15db4 do_runtime_invoke + 84
	13  mono                                0x0000000101b11f04 mono_runtime_class_init_full + 996
	14  mono                                0x00000001019af3d5 mono_generic_class_init + 21
	15  ???                                 0x0000000101ecf2f7 0x0 + 4327273207
	16  ???                                 0x0000000101ecf239 0x0 + 4327273017
	17  mono                                0x0000000101953a07 mono_jit_runtime_invoke + 1383
	18  mono                                0x0000000101b15db4 do_runtime_invoke + 84
	19  mono                                0x0000000101b193d9 do_exec_main_checked + 137
	20  mono                                0x00000001019c23bf mono_jit_exec + 287
	21  mono                                0x00000001019c4bb4 mono_main + 9140
	22  mono                                0x00000001019433cd main + 253
	23  mono                                0x00000001019432c4 start + 52
	24  ???                                 0x0000000000000002 0x0 + 2

Debug info from gdb:

(lldb) command source -s 0 '/tmp/mono-gdb-commands.2ms21c'
Executing commands in '/tmp/mono-gdb-commands.2ms21c'.
(lldb) process attach --pid 37629
warning: (x86_64) /Library/Frameworks/Mono.framework/Versions/5.8.1/lib/mono/4.5/mscorlib.dll.dylib empty dSYM file detected, dSYM was created with an executable with no debug info.
Process 37629 stopped
* thread #1, name = 'tid_307', queue = 'com.apple.main-thread', stop reason = signal SIGSTOP
    frame #0: 0x00007fff67362232 libsystem_kernel.dylib`__wait4 + 10
libsystem_kernel.dylib`__wait4:
->  0x7fff67362232 <+10>: jae    0x7fff6736223c            ; <+20>
    0x7fff67362234 <+12>: movq   %rax, %rdi
    0x7fff67362237 <+15>: jmp    0x7fff67358b25            ; cerror
    0x7fff6736223c <+20>: retq   
Target 0: (mono) stopped.

Executable module set to "/Library/Frameworks/Mono.framework/Versions/Current/Commands/mono".
Architecture set to: x86_64h-apple-macosx.
(lldb) thread list
Process 37629 stopped
* thread #1: tid = 0x64999, 0x00007fff67362232 libsystem_kernel.dylib`__wait4 + 10, name = 'tid_307', queue = 'com.apple.main-thread', stop reason = signal SIGSTOP
  thread #2: tid = 0x6499e, 0x00007fff67361a1e libsystem_kernel.dylib`__psynch_cvwait + 10, name = 'SGen worker'
  thread #3: tid = 0x6499f, 0x00007fff67358246 libsystem_kernel.dylib`semaphore_wait_trap + 10, name = 'Finalizer'
(lldb) thread backtrace all
* thread #1, name = 'tid_307', queue = 'com.apple.main-thread', stop reason = signal SIGSTOP
  * frame #0: 0x00007fff67362232 libsystem_kernel.dylib`__wait4 + 10
    frame #1: 0x00000001019feb8e mono`mono_handle_native_crash(signal=<unavailable>, ctx=<unavailable>, info=<unavailable>) at mini-exceptions.c:2726 [opt]
    frame #2: 0x00007fff6751ff5a libsystem_platform.dylib`_sigtramp + 26
    frame #3: 0x00007fff67361b6f libsystem_kernel.dylib`__pthread_kill + 11
    frame #4: 0x00007fff6752c080 libsystem_pthread.dylib`pthread_kill + 333
    frame #5: 0x00007fff672bd1ae libsystem_c.dylib`abort + 127
    frame #6: 0x00000001057aca52 libmonosgen-2.0.1.dylib`monoeg_log_default_handler + 105
    frame #7: 0x00000001057ac9d7 libmonosgen-2.0.1.dylib`monoeg_g_logv + 83
    frame #8: 0x00000001057acaca libmonosgen-2.0.1.dylib`monoeg_g_log + 120
    frame #9: 0x00000001056a444e libmonosgen-2.0.1.dylib`mono_icall_lock + 72
    frame #10: 0x00000001056a43c4 libmonosgen-2.0.1.dylib`mono_add_internal_call + 21
    frame #11: 0x000000010439a1ba libUrho3DCSharp.dylib`Urho3DRegisterMonoInternalCalls + 26
    frame #12: 0x0000000101ecf527
    frame #13: 0x0000000101953a07 mono`mono_jit_runtime_invoke(method=<unavailable>, obj=<unavailable>, params=0x0000000000000000, exc=0x00007fdcee844610, error=<unavailable>) at mini-runtime.c:2800 [opt]
    frame #14: 0x0000000101b15db4 mono`do_runtime_invoke(method=0x00007fdcef0141e0, obj=0x0000000000000000, params=0x0000000000000000, exc=0x00007ffeee2be1d8, error=0x00007ffeee2be220) at object.c:2849 [opt]
    frame #15: 0x0000000101b11f04 mono`mono_runtime_class_init_full [inlined] mono_runtime_try_invoke(method=<unavailable>, obj=<unavailable>, params=<unavailable>, error=0x00007ffeee2be220) at object.c:2956 [opt]
    frame #16: 0x0000000101b11ebf mono`mono_runtime_class_init_full(vtable=0x00007fdcee001c70, error=0x00007ffeee2be220) at object.c:473 [opt]
    frame #17: 0x00000001019af3d5 mono`mono_generic_class_init(vtable=<unavailable>) at jit-icalls.c:1462 [opt]
    frame #18: 0x0000000101ecf2f7
    frame #19: 0x0000000101ecf239
    frame #20: 0x0000000101953a07 mono`mono_jit_runtime_invoke(method=<unavailable>, obj=<unavailable>, params=0x00007ffeee2be5b8, exc=0x00007fdcee001c70, error=<unavailable>) at mini-runtime.c:2800 [opt]
    frame #21: 0x0000000101b15db4 mono`do_runtime_invoke(method=0x00007fdced407f98, obj=0x0000000000000000, params=0x00007ffeee2be5b8, exc=0x0000000000000000, error=0x00007ffeee2be5f8) at object.c:2849 [opt]
    frame #22: 0x0000000101b193d9 mono`do_exec_main_checked [inlined] mono_runtime_invoke_checked(method=<unavailable>, obj=<unavailable>, error=<unavailable>) at object.c:3002 [opt]
    frame #23: 0x0000000101b19398 mono`do_exec_main_checked(method=0x00007fdced407f98, args=<unavailable>, error=0x00007ffeee2be5f8) at object.c:4726 [opt]
    frame #24: 0x00000001019c23bf mono`mono_jit_exec(domain=<unavailable>, assembly=<unavailable>, argc=1, argv=0x00007ffeee2be918) at driver.g.c:1040 [opt]
    frame #25: 0x00000001019c4bb4 mono`mono_main [inlined] main_thread_handler at driver.g.c:1109 [opt]
    frame #26: 0x00000001019c4b81 mono`mono_main(argc=2, argv=<unavailable>) at driver.g.c:2222 [opt]
    frame #27: 0x00000001019433cd mono`main [inlined] mono_main_with_options(argc=<unavailable>, argv=<unavailable>) at main.c:46 [opt]
    frame #28: 0x00000001019433b9 mono`main(argc=2, argv=<unavailable>) at main.c:339 [opt]
    frame #29: 0x00000001019432c4 mono`start + 52
  thread #2, name = 'SGen worker'
    frame #0: 0x00007fff67361a1e libsystem_kernel.dylib`__psynch_cvwait + 10
    frame #1: 0x00007fff6752a589 libsystem_pthread.dylib`_pthread_cond_wait + 732
    frame #2: 0x0000000101bcec9e mono`thread_func [inlined] mono_os_cond_wait(mutex=<unavailable>) at mono-os-mutex.h:173 [opt]
    frame #3: 0x0000000101bcec8b mono`thread_func at sgen-thread-pool.c:165 [opt]
    frame #4: 0x0000000101bcec7d mono`thread_func(data=0x0000000000000000) at sgen-thread-pool.c:196 [opt]
    frame #5: 0x00007fff67529661 libsystem_pthread.dylib`_pthread_body + 340
    frame #6: 0x00007fff6752950d libsystem_pthread.dylib`_pthread_start + 377
    frame #7: 0x00007fff67528bf9 libsystem_pthread.dylib`thread_start + 13
  thread #3, name = 'Finalizer'
    frame #0: 0x00007fff67358246 libsystem_kernel.dylib`semaphore_wait_trap + 10
    frame #1: 0x0000000101b7b2fc mono`finalizer_thread [inlined] mono_os_sem_wait(flags=MONO_SEM_FLAGS_ALERTABLE) at mono-os-semaphore.h:90 [opt]
    frame #2: 0x0000000101b7b2f1 mono`finalizer_thread at mono-coop-semaphore.h:43 [opt]
    frame #3: 0x0000000101b7b2e5 mono`finalizer_thread(unused=<unavailable>) at gc.c:866 [opt]
    frame #4: 0x0000000101b375b0 mono`start_wrapper [inlined] start_wrapper_internal at threads.c:1003 [opt]
    frame #5: 0x0000000101b37513 mono`start_wrapper(data=<unavailable>) at threads.c:1063 [opt]
    frame #6: 0x00007fff67529661 libsystem_pthread.dylib`_pthread_body + 340
    frame #7: 0x00007fff6752950d libsystem_pthread.dylib`_pthread_start + 377
    frame #8: 0x00007fff67528bf9 libsystem_pthread.dylib`thread_start + 13
(lldb) detach

=================================================================
Got a SIGABRT while executing native code. This usually indicates
a fatal error in the mono runtime or one of the native libraries 
used by your application.
=================================================================

Abort trap: 6
(lldb) quit

-------------------------

rku | 2018-04-25 09:17:06 UTC | #24

Does 102 sample run?

-------------------------

elix22 | 2018-04-25 11:04:13 UTC | #25

The output of the crash is from  Program.cs from sample 102

I copied Program.cs to the build/bin folder 
csc Program.cs -r:Urho3DNet.dll
mono Program.exe

-------------------------

rku | 2018-04-25 11:15:22 UTC | #26

Maybe try sample that gets built by cmake

-------------------------

Omid | 2018-05-14 13:07:09 UTC | #27

@rku  Do you have any plan to make Nuget package?

-------------------------

rku | 2018-05-14 13:20:06 UTC | #28

No immediate plans. Unsure how useful it would be without rest of the tools though.

-------------------------

rku | 2019-03-07 14:30:49 UTC | #29

Hey @Omid and anyone else interested - nuget is here!

Here is how to get it working:
1. Create C# project
2. Install [rbfx.Urho3DNet](https://www.nuget.org/packages/rbfx.Urho3DNet/) package
3. Set your project framework to .net 4.7.1
4. Set your project cpu architecture to x64

A sample `Program.cs` to get things running faster:
```cs
//
// Copyright (c) 2017-2019 Rokas Kupstys.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//
using System;
using System.Diagnostics;
using System.IO;
using Urho3DNet;

namespace DemoApplication
{
    [ObjectFactory]
    class RotateObject : LogicComponent
    {
        public RotateObject(Context context) : base(context)
        {
            SetUpdateEventMask(UpdateEvent.UseUpdate);
        }

        public override void Update(float timeStep)
        {
            var d = new Quaternion(10 * timeStep, 20 * timeStep, 30 * timeStep);
            GetNode().Rotate(d);
        }
    }

    class DemoApplication : Application
    {
        private Scene _scene;
        private Viewport _viewport;
        private Node _camera;
        private Node _cube;
        private Node _light;

        public DemoApplication(Context context) : base(context)
        {
        }

        public override void Setup()
        {
            var currentDir = Directory.GetCurrentDirectory();
            EngineParameters[Urho3D.EpFullScreen] = false;
            EngineParameters[Urho3D.EpWindowWidth] = 1920;
            EngineParameters[Urho3D.EpWindowHeight] = 1080;
            EngineParameters[Urho3D.EpWindowTitle] = "Hello C#";
            EngineParameters[Urho3D.EpResourcePaths] = "CoreData";
            EngineParameters[Urho3D.EpResourcePrefixPaths] = $"{currentDir};{currentDir}/..";
        }

        public override void Start()
        {
            GetInput().SetMouseVisible(true);

            // Viewport
            _scene = new Scene(GetContext());
            _scene.CreateComponent<Octree>();

            _camera = _scene.CreateChild("Camera");
            _viewport = new Viewport(GetContext());
            _viewport.SetScene(_scene);
            _viewport.SetCamera(_camera.CreateComponent<Camera>());
            GetRenderer().SetViewport(0, _viewport);

            // Background
            GetRenderer().GetDefaultZone().SetFogColor(new Color(0.5f, 0.5f, 0.7f));

            // Scene
            _camera.SetPosition(new Vector3(0, 2, -2));
            _camera.LookAt(Vector3.Zero);

            // Cube
            _cube = _scene.CreateChild("Cube");
            var model = _cube.CreateComponent<StaticModel>();
            model.SetModel(GetCache().GetResource<Model>("Models/Box.mdl"));
            model.SetMaterial(0, GetCache().GetResource<Material>("Materials/DefaultGrey.xml"));
            var rotator = _cube.CreateComponent<RotateObject>();

            // Light
            _light = _scene.CreateChild("Light");
            _light.CreateComponent<Light>();
            _light.SetPosition(new Vector3(0, 2, -1));
            _light.LookAt(Vector3.Zero);
        }
    }

    internal class Program
    {
        public static void Main(string[] args)
        {
            using (var context = new Context())
            {
                using (var application = new DemoApplication(context))
                {
                    application.Run();
                }
            }
        }
    }
}
```

Edit:
On gitter we discovered that package does not work correctly with old style .csproj projects. If you run into problems - use [sample csproj](https://gist.github.com/rokups/c676212bd8d35d07b0067858fa94a950) for testing.

-------------------------

Omid | 2019-03-07 15:25:16 UTC | #30

Thanks. Good job :+1:

-------------------------

glebedev | 2021-02-23 16:33:37 UTC | #31

Just in case anyone going to google for it and find this thread: there is a Visual Studio Multi-Project Template you can use to create rbfx/Urho3DNet application

https://marketplace.visualstudio.com/items?itemName=GlebLebedev.Urho3DNet

It has projects for .net framework, .net core, uwp, xamarin android and ios. The application logic code is in a shared .net standard 2.0 class library and there is another one for content (temporal workaround while I'm figuring out how to work with IWizard).

-------------------------

George1 | 2021-02-24 10:16:42 UTC | #32

There is also Urho.Net from elix22, which was based off UrhoSharp branch.
I think elix22 updated it to work with latest Urho3D source.  It also contains example from Lumak and Action stuff from UrhoSharp.

https://discourse.urho3d.io/t/urho-net-c-cross-platform-game-development-framework/6674

-------------------------

glebedev | 2021-02-24 10:32:34 UTC | #33

I've also ported Actions to the Urho3DNet, added some fluent goodness on top of it:

                        var action1 = ActionBuilder<Node>.Build()
                            .RotateBy(2, 0, -2.0f * (float)Math.PI, 0)
                            .RepeatForever()
                            .Complete();
                        action1.Run(_actionManager, _currentIcon.Frame1Node);
                        var action2 = ActionBuilder<Node>.Build()
                            .Show()
                            .Then(_=>_
                                .RotateBy(1, 0, 2.0f * (float)Math.PI, 0)
                                .RepeatForever())
                            .Complete();
                        action2.Run(_actionManager, _currentIcon.Frame3Node);

-------------------------

