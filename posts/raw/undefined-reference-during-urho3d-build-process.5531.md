pirogronian | 2019-08-29 16:04:51 UTC | #1

I'm trying to build package for my Linux distro from git master, becaue of this: [No keyboard input](https://discourse.urho3d.io/t/no-keyboard-input/5523/9)

Here is a build script used in package of my Linux distro:
    mkdir -p "$srcdir/Urho3D/build"
    cd "$srcdir/Urho3D/build"
    cmake "$srcdir/Urho3D/" -DCMAKE_INSTALL_PREFIX="/usr" -DURHO3D_USE_LIB_DEB=1 -DURHO3D_SAMPLES=1
    make

Build process fails at:
> [ 76%] Linking CXX executable ../../../bin/Urho3DPlayer
> /usr/bin/ld: ../../../lib/libUrho3D.a(loslib.c.o): in function `os_tmpname':
> loslib.c:(.text+0x242): warning: the use of `tmpnam' is dangerous, better use `mkstemp'
> /usr/bin/ld: ../../../lib/libUrho3D.a(PhysicsWorld.cpp.o): in function `Urho3D::PhysicsWorld::PhysicsWorld(Urho3D::Context*)':
> PhysicsWorld.cpp:(.text+0x4fed): undefined reference to `btSequentialImpulseConstraintSolver::btSequentialImpulseConstraintSolver()'
> /usr/bin/ld: ../../../lib/libUrho3D.a(Constraint.cpp.o): in function `Urho3D::Constraint::ApplyFrames()':
> Constraint.cpp:(.text+0x2600): undefined reference to `btHingeConstraint::setFrames(btTransform const&, btTransform const&)'
> /usr/bin/ld: ../../../lib/libUrho3D.a(Constraint.cpp.o): in function `Urho3D::Constraint::CreateConstraint()':
> Constraint.cpp:(.text+0x3e03): undefined reference to `btHingeConstraint::btHingeConstraint(btRigidBody&, btRigidBody&, btTransform const&, btTransform const&, bool)'
> /usr/bin/ld: Constraint.cpp:(.text+0x47ee): undefined reference to `btPoint2PointConstraint::btPoint2PointConstraint(btRigidBody&, btRigidBody&, btVector3 const&, btVector3 const&)'
> /usr/bin/ld: ../../../lib/libUrho3D.a(btDiscreteDynamicsWorld.cpp.o): in function `btDiscreteDynamicsWorld::btDiscreteDynamicsWorld(btDispatcher*, btBroadphaseInterface*, btConstraintSolver*, btCollisionConfiguration*)':
> btDiscreteDynamicsWorld.cpp:(.text+0x6998): undefined reference to `btSequentialImpulseConstraintSolver::btSequentialImpulseConstraintSolver()'
> collect2: error: ld returned 1 exit status

Earlier my laptop shut itself down due to overheating, so, in case of bad building of Bullet, I rebuilt it, but without result.

I couldnt find any serious differences between packages used for 1.7 and master version. Here are they:
[urho3d](https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=urho3d)
[urho3d-git](https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=urho3d-git)

Edit:
Here is a exact command, extracted from verbose pass:

> /usr/bin/c++  -mtune=generic -march=x86-64 -mtune=generic -O2 -pipe -fno-plt -std=gnu++11 -Wno-invalid-offsetof -march=native -msse3 -pthread -fdiagnostics-color=auto -O3 -DNDEBUG  -Wl,-O1,--sort-common,--as-needed,-z,relro,-z,now -rdynamic CMakeFiles/Urho3DPlayer.dir/Urho3DPlayer.cpp.o  -o ../../../bin/Urho3DPlayer ../../../lib/libUrho3D.a -ldl -lm -lrt -lGL -ldl -lm -lrt -lGL

-------------------------

S.L.C | 2019-08-29 16:48:56 UTC | #2

I don't see any mention of what OS or compiler was used. Those usually allow people to replicate your current situation (if possible). So you should usually mention them.

Edit: OS seems to be Arch linux. But as it's common with linux. There is more than one way to do things. Such as desktop environment, window manager and other such configurations that can make every target different in it's own way. At least something that could hinder keyboard input.

Also, do you have another version of bullet installed on your system?

You have the most insight into your system. So you should give more details about your current environment. What was described so far doesn't help enough to reproduce the situation.

-------------------------

SirNate0 | 2019-08-29 20:10:52 UTC | #3

If you just rebuilt the bullet library but not libUrho3D.a as well that could be your problem. If you want to be certain it isn't just some incomplete file from when your computer shut down try rebuilding from the start (probably best to remove the build directory and recreate it, rerunning CMake as well).

-------------------------

pirogronian | 2019-08-29 20:10:34 UTC | #4

Thank you for your answers. Indeed, a whole library was corrupted, so it was enought to remove it from build/lib (I really didn't want to restart the whole build process, because it kills both me and my machine). But previously I thought rebuilding libBullet.a will force reconsolidation of libUrho3D.a.

-------------------------

S.L.C | 2019-08-30 03:52:50 UTC | #5

Try to limit the amount of build threads that CMake uses. The `-j#` parameter.

-------------------------

