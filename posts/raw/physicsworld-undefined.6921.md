nickwebha | 2021-07-14 16:37:51 UTC | #1

I feel really dumb asking this but I just can not figure this out.

I have:
`this->scene_->CreateComponent< Urho3D::PhysicsWorld >();`
and it gives me:
`error: ‘PhysicsWorld’ is not a member of ‘Urho3D’`

It is the same for `Urho3D::RigidBody` and `Urho3D::CollisionShape`.

What am I doing wrong?

**Edit**
The samples (where I learned about `PhysicsWorld` from) all compile fine.

-------------------------

S.L.C | 2021-07-14 19:41:27 UTC | #2

Did you include the associated headers?

Is your code already in the Urho3D namespace? Imagine this scenario:

```cpp
namespace Urho3D {
/*already in Urho3D namespace*/
this->scene_->CreateComponent< Urho3D::PhysicsWorld >();
/*must prefix with :: for outer scope*/
//this->scene_->CreateComponent< ::Urho3D::PhysicsWorld >();
}
```

-------------------------

nickwebha | 2021-07-14 20:18:30 UTC | #3

Sorry, I really should have mentioned that.

*Urho3DAll.h* is included. I have a compiling, working prototype game just without collision detection. For example, the lines right before that one are:

```
this->scene_ = new Urho3D::Scene( this->context_ );
this->scene_->CreateComponent< Urho3D::Octree >();
```
and they compile fine.

I am not currently using any namespaces or `using`. I also commented out `using namespace Urho3D;` in *Urho3DAll.h*.

-------------------------

Eugene | 2021-07-14 22:08:08 UTC | #4

Okay, second dumb question. Do you have physics enabled in you build?
Does monolithic header include physics headers?

-------------------------

nickwebha | 2021-07-14 22:27:01 UTC | #5

[quote="Eugene, post:4, topic:6921"]
Do you have physics enabled in you build?
Does monolithic header include physics headers?
[/quote]
Another thing I should have mentioned.

I did not specify `-D URHO3D_PHYSICS` when using cmake, leaving it at its default of 1 (according to [the documentation](https://urho3d.io/documentation/HEAD/_building.html)).

Yes, I do see the headers in there including *include/Urho3D/Physics/PhysicsWorld.h*. Opening said file I see `class URHO3D_API PhysicsWorld` under the `Urho3D` namespace. Same for the other classes (`Urho3D::RigidBody` and `Urho3D::CollisionShape`).

Strange, right? This is a fresh install of Linux and Urho3D (via a `git clone` of `master`).

-------------------------

SirNate0 | 2021-07-15 11:02:40 UTC | #6

You can try explicitly including the PhysicsWorld header. You could also try having the compiler dump the preprocessor output ( `-E` flag in gcc) and check for the existence of the PhysicsWorld class there. 
Or you can try adding an `#error This was included` line in the PhysicsWorld header. If you see that error messages when compiling, you know the file is being included. Also, you should probably double check that you have spelled everything correctly in your code. I'm assuming you did since it looks right here, but it can't hurt to check.

-------------------------

nickwebha | 2021-07-15 14:34:48 UTC | #7

Just for giggles I recompiled Urho3D with `cmake -D URHO3D_PHYSICS=1 ..` and saw no difference. The odd thing here is I do see *Linking CXX static library libBullet.a* and *Built target Bullet* in the `make` output.

Looking in *Urho3D/Urho3DAll.h* I see `#if URHO3D_PHYSICS` so I stuck `#error This was included` right after that line. It never spits out *This was included*.

If I include all the files manually (copy and pasted from *Urho3D/Urho3DAll.h*) I get:
`/home/nick/Urho3D/build.linux/include/Urho3D/Physics/PhysicsUtils.h:31:10: fatal error: Bullet/LinearMath/btVector3.h: No such file or directory`
a few times.

Again, the samples all compile fine.

I am going to spin up a new VM and do a compile. Will report back later.

-------------------------

SirNate0 | 2021-07-15 15:39:33 UTC | #8

How are you setting up your project to compile? Are you using the provided CMake modules? What does the compile command look like (you can use `make VERBOSE=1` to find out)?

-------------------------

nickwebha | 2021-07-15 16:38:01 UTC | #9

```
git clone https://github.com/urho3d/Urho3D.git
cd Urho3D/
mkdir build.linux && cd build.linux/
cmake ..
make -j 4
```

I also tried:
`../script/cmake_generic.sh .` in place of `cmake ..` but got the same results.

I also tried:
`make` (without the `-j 4`) but got the same results.

Here is an example from `make VERBOSE=1`:

```
[ 50%] Building CXX object Source/ThirdParty/Bullet/CMakeFiles/Bullet.dir/src/BulletDynamics/Dynamics/btRigidBody.cpp.o
cd /home/nick/Urho3D/build.linux/Source/ThirdParty/Bullet && /usr/bin/c++  -DURHO3D_ANGELSCRIPT -DURHO3D_FILEWATCHER -DURHO3D_IK -DURHO3D_LOGGING -DURHO3D_LUA -DURHO3D_NAVIGATION -DURHO3D_NETWORK -DURHO3D_PHYSICS -DURHO3D_PROFILING -DURHO3D_STATIC_DEFINE -DURHO3D_THREADING -DURHO3D_URHO2D -DURHO3D_WEBP -I/home/nick/Urho3D/Source/ThirdParty/Bullet/src  -mtune=generic  -Wno-invalid-offsetof -march=native -msse3 -pthread -fdiagnostics-color=auto -O3 -DNDEBUG -fvisibility=hidden -fvisibility-inlines-hidden   -std=c++11 -o CMakeFiles/Bullet.dir/src/BulletDynamics/Dynamics/btRigidBody.cpp.o -c /home/nick/Urho3D/Source/ThirdParty/Bullet/src/BulletDynamics/Dynamics/btRigidBody.cpp
```
and later:
`/usr/bin/ranlib libBullet.a`

I am seeing `-DURHO3D_PHYSICS` all over the place.

-------------------------

weitjong | 2021-07-15 16:41:41 UTC | #10

If you can see the `#if URHO3D_PHYSICS` in the `Urho3DAll.h` header file then it means the Urho3D library was built with Physic subsystem enabled, which is the default. But that does not mean the downstream project using the library *must* be using that. That build option is not baked in. So, I would suspect that some how you have disabled the Physics build option in your own project. Check the `URHO3D_PHYSICS` build option in the `CMakeCache.txt` file inside the build tree of your own project. That is also the only explanation why your "#error" did not show up.

-------------------------

nickwebha | 2021-07-15 16:42:48 UTC | #11

[quote="weitjong, post:10, topic:6921"]
Check the `URHO3D_PHYSICS` build option in the `CMakeCache.txt` file inside the build tree of your own project.
[/quote]
```
//Enable physics support
URHO3D_PHYSICS:BOOL=ON
```

[quote="nickwebha, post:7, topic:6921"]
I am going to spin up a new VM and do a compile. Will report back later.
[/quote]
Got the same problem.

-------------------------

weitjong | 2021-07-15 16:53:52 UTC | #12

I just created a newly scaffolding project using `rake new` and then inside the UrhoApp.cpp, I have added the line

```
scene_->CreateComponent<PhysicsWorld>();
```

After the `Octree` component in the original generated code. Everything compiled fine. The UrhoApp uses `Urho3DAll.h` as well. The last line in that header file already has `using namespace Urho3D;`. I have the library built and installed using the default. In CLion I can see the IDE auto-complete the line. Opening the `Urho3DAll.h` file in the editor, the IDE also correctly shows that all the Physics related headers are being included.

So, I can only conclude there was something wrong with your project setup. Perhaps you should just nuke your project build tree and regenerate it from scratch again. Keep rebuilding Urho3D library itself in a new VM serve no purpose as the issue may not be in the library building.

-------------------------

nickwebha | 2021-07-15 16:56:28 UTC | #13

[quote="weitjong, post:12, topic:6921"]
I can only conclude there was something wrong with your project setup.
[/quote]
I agree; I must be doing something wrong. But to have
`auto* cache = GetSubsystem< Urho3D::ResourceCache >();`
work but not
`auto* body = this->objectNode_->CreateComponent< Urho3D::RigidBody >();`
?

I saw `using namespace Urho3D;` in *Urho3DAll.h* and commented it out for a while. I have also tried compiling with it for giggles even though I am specifying `Urho3D::`.

My compile scripts looks like:

```
g++																					\
	client/source/*.cpp																\
	client/lib/linux/libUrho3D.a													\
	-Iclient/include/																\
	-Iinclude/ -I/home/nick/Urho3D/build.linux/include/ -I/home/nick/boost_1_76_0/	\
	-std=c++17																		\
	-Wall -Werror																	\
	-pthread -ldl -lGL -g3 -O0														\
	-D __DEBUG__																	\
	-o distribution/simpletanks.debug
```

-------------------------

weitjong | 2021-07-15 17:01:50 UTC | #14

if you are using your own script then you should have told us in the beginning. If you really must do so, you may want to use `pkg-config` command to get all the compiler flags and linker flags from there. For sure, you have missed out some key ingredient!

-------------------------

nickwebha | 2021-07-15 17:41:31 UTC | #15

I misspoke. It is not so much a complex script as me having just written down the command I am using to compile. It does not do anything else. That, plus `#!/bin/bash` at the top, composes the entire "script".

Is there a document/wiki page that documents how I should be compiling? Is pointing `g++` at the lib and headers directory not enough? I did a `sudo make install` in my VM but `pkg-config urho3d` gives me nothing (not sure what I am doing with `pkg-config`).

**Edit**
I did a `pkg-config --variable pc_path pkg-config` and there is nothing Urho3D in any of those directories after a `sudo make install`.

-------------------------

weitjong | 2021-07-16 16:00:20 UTC | #16

Sorry about that. I should have mentioned it in my earlier post, but it is kind of late here already. So, I will be brief. You missed out the long list of compiler defines. As for how to use `pkg-config`, you can refer to this legacy doc. https://urho3d.io/documentation/HEAD/_using_library.html#Using_pkg_config

-------------------------

nickwebha | 2021-07-16 16:16:34 UTC | #17

Thank you guys for you help! Now it is on to the physics documentation for me!

For anyone else trying to do this using their own build system:
You can look in *Urho3DAll.h* for which defines the system wants and add them to your command line (`-D URHO3D_PHYSICS`, for example). You might have to copy some includes into your own build tree from *Urho3D/Source/ThirdParty/*.

-------------------------

