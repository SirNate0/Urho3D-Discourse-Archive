mazataza | 2017-11-20 21:12:50 UTC | #1

I am try to create character control using suche code

   btTransform startTransform;
    startTransform.setIdentity ();
    //startTransform.setOrigin (btVector3(0.0, 4.0, 0.0));
    const Vector3 &postion = _cameraNode->GetWorldPosition();
    startTransform.setOrigin (btVector3(postion.x_, postion.y_, postion.z_));


    ghostObject = new btPairCachingGhostObject();
    ghostObject->setWorldTransform(startTransform);

    btScalar characterHeight=1.75;
    btScalar characterWidth =1.75;
    ghostShape = new btCapsuleShape(characterWidth,characterHeight);
    ghostObject->setCollisionShape (ghostShape);
    ghostObject->setCollisionFlags (btCollisionObject::CF_CHARACTER_OBJECT);

    btScalar stepHeight = btScalar(0.35);
    characterController = new btKinematicCharacterController (ghostObject,ghostShape,stepHeight);

when compiling it with Clion i got following linking error

CMakeFiles\LoadScene.dir/objects.a(CharacterComponent.cpp.obj): In function `btAlignedAllocator<int, 16u>::deallocate(int*)':
C:/3d/Urho3D.git/Urho3D-SDK-Shared/include/Urho3D/ThirdParty/Bullet/LinearMath/btAlignedAllocator.h:96: undefined reference to `btAlignedFreeInternal(void*)'
CMakeFiles\LoadScene.dir/objects.a(CharacterComponent.cpp.obj): In function `btAlignedAllocator<btHashInt, 16u>::deallocate(btHashInt*)':
C:/3d/Urho3D.git/Urho3D-SDK-Shared/include/Urho3D/ThirdParty/Bullet/LinearMath/btAlignedAllocator.h:96: undefined reference to `btAlignedFreeInternal(void*)'
CMakeFiles\LoadScene.dir/objects.a(CharacterComponent.cpp.obj): In function `btAlignedAllocator<btTriangleInfo, 16u>::deallocate(btTriangleInfo*)':
C:/3d/Urho3D.git/Urho3D-SDK-Shared/include/Urho3D/ThirdParty/Bullet/LinearMath/btAlignedAllocator.h:96: undefined reference to `btAlignedFreeInternal(void*)'
CMakeFiles\LoadScene.dir/objects.a(CharacterComponent.cpp.obj):CharacterComponent.cpp:(.rdata$_ZTV17btTypedConstraint[_ZTV17btTypedConstraint]+0x60): undefined reference to `btTypedConstraint::serialize(void*, btSerializer*) const'
CMakeFiles\LoadScene.dir/objects.a(CharacterControl.cpp.obj): In function `btCollisionObject::operator new(unsigned long long)':
C:/3d/Urho3D.git/Urho3D-SDK-Shared/include/Urho3D/ThirdParty/Bullet/BulletCollision/CollisionDispatch/btCollisionObject.h:129: undefined reference to `btAlignedAllocInternal(unsigned long long, int)'
CMakeFiles\LoadScene.dir/objects.a(CharacterControl.cpp.obj): In function `CharacterControl::CharacterControl(Urho3D::Context*, Urho3D::Scene*)':
C:/3d/Urho3D.git/Urho3D-SDK-Shared/include/Urho3D/ThirdParty/Bullet/BulletCollision/CollisionDispatch/btCollisionObject.h:129: undefined reference to `btPairCachingGhostObject::btPairCachingGhostObject()'
CMakeFiles\LoadScene.dir/objects.a(CharacterControl.cpp.obj): In function `btCapsuleShape::operator new(unsigned long long)':
C:/3d/Urho3D.git/Urho3D-SDK-Shared/include/Urho3D/ThirdParty/Bullet/BulletCollision/CollisionShapes/btCapsuleShape.h:37: undefined reference to `btAlignedAllocInternal(unsigned long long, int)'
CMakeFiles\LoadScene.dir/objects.a(CharacterControl.cpp.obj): In function `CharacterControl::CharacterControl(Urho3D::Context*, Urho3D::Scene*)':
C:/3d/Urho3D.git/samples/LoadScene/CharacterControl.cpp:21: undefined reference to `btCapsuleShape::btCapsuleShape(float, float)'
CMakeFiles\LoadScene.dir/objects.a(CharacterControl.cpp.obj): In function `btKinematicCharacterController::operator new(unsigned long long)':
C:/3d/Urho3D.git/Urho3D-SDK-Shared/include/Urho3D/ThirdParty/Bullet/BulletDynamics/Character/btKinematicCharacterController.h:118: undefined reference to `btAlignedAllocInternal(unsigned long long, int)'
CMakeFiles\LoadScene.dir/objects.a(CharacterControl.cpp.obj): In function `CharacterControl::CharacterControl(Urho3D::Context*, Urho3D::Scene*)':
C:/3d/Urho3D.git/samples/LoadScene/CharacterControl.cpp:26: undefined reference to `btKinematicCharacterController::btKinematicCharacterController(btPairCachingGhostObject*, btConvexShape*, float, btVector3 const&)'
CMakeFiles\LoadScene.dir/objects.a(CharacterControl.cpp.obj): In function `btCollisionObject::operator delete(void*)':
C:/3d/Urho3D.git/Urho3D-SDK-Shared/include/Urho3D/ThirdParty/Bullet/BulletCollision/CollisionDispatch/btCollisionObject.h:129: undefined reference to `btAlignedFreeInternal(void*)'
CMakeFiles\LoadScene.dir/objects.a(CharacterControl.cpp.obj): In function `btCapsuleShape::operator delete(void*)':
C:/3d/Urho3D.git/Urho3D-SDK-Shared/include/Urho3D/ThirdParty/Bullet/BulletCollision/CollisionShapes/btCapsuleShape.h:37: undefined reference to `btAlignedFreeInternal(void*)'
CMakeFiles\LoadScene.dir/objects.a(CharacterControl.cpp.obj): In function `btKinematicCharacterController::operator delete(void*)':
C:/3d/Urho3D.git/Urho3D-SDK-Shared/include/Urho3D/ThirdParty/Bullet/BulletDynamics/Character/btKinematicCharacterController.h:118: undefined reference to `btAlignedFreeInternal(void*)'
collect2.exe: error: ld returned 1 exit status
CMakeFiles\LoadScene.dir\build.make:151: recipe for target 'bin/LoadScene_d.exe' failed
mingw32-make.exe[3]: *** [bin/LoadScene_d.exe] Error 1
mingw32-make.exe[2]: *** [CMakeFiles/LoadScene.dir/all] Error 2
mingw32-make.exe[1]: *** [CMakeFiles/LoadScene.dir/rule] Error 2
CMakeFiles\Makefile2:66: recipe for target 'CMakeFiles/LoadScene.dir/all' failed
CMakeFiles\Makefile2:78: recipe for target 'CMakeFiles/LoadScene.dir/rule' failed
Makefile:163: recipe for target 'LoadScene' failed
mingw32-make.exe: *** [LoadScene] Error 2

any idea what can case this ?

-------------------------

ppsychrite | 2017-11-20 21:16:13 UTC | #2

I've had something similar to this when I tried doing what you are.

What fixed it for me was including bullet headers before urho3d's headers and adding 

    #undef new

Hope that helps! :slight_smile:

-------------------------

mazataza | 2017-11-20 21:24:20 UTC | #3

thanks for your replay but i add what you said but i still got the error :-(

#include <Urho3D/ThirdParty/Bullet/btBulletCollisionCommon.h>
#include <Urho3D/ThirdParty/Bullet/btBulletDynamicsCommon.h>
#include <Urho3D/ThirdParty/Bullet/BulletCollision/CollisionDispatch/btGhostObject.h>
#include <Urho3D/ThirdParty/Bullet/BulletDynamics/Character/btKinematicCharacterController.h>

#undef new

#include <Urho3D/Core/CoreEvents.h>
#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/Input/InputEvents.h>

#include <Urho3D/Graphics/Camera.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/Graphics/Renderer.h>
#include <Urho3D/Graphics/Viewport.h>
#include <Urho3D/UI/UI.h>
#include <Urho3D/UI/UIEvents.h>

-------------------------

weitjong | 2017-11-21 01:48:23 UTC | #4

Try using STATIC version of the Urho3D library to see if it helps. The SHARED lib may have unused 3rd-party symbols optimized away at the time the lib is built. The STATIC lib on the other hand is an archive of all the symbols there are.

-------------------------

mazataza | 2017-11-21 07:43:23 UTC | #5

yes with static version i compiled it works .. 

i think that what you said about optimization is the issue, only the parts which are used by Urho3D to build Physic world is linked against.

but is there any way to let shared library of Urho3D to have all code without optimization on discarding any unused code? because a library should have all code compiled and included. when i for example compile libc as shared library i can't expect that some methods are discards from the shared lib at the end.

-------------------------

Eugene | 2017-11-21 08:59:03 UTC | #6

[quote="mazataza, post:5, topic:3764"]
but is there any way to let shared library of Urho3D to have all code without optimization on discarding any unused code?
[/quote]

To be fair, I'd like to avoid SHARED build of Urho at all. Memory management is awful. If you want to take DLL pain, make your own DLL and link it with Urho statically.

-------------------------

mazataza | 2017-11-21 13:03:53 UTC | #7

my target is later is android .. thus it is better to link it with static and in android it will be at the end a shared lib.

-------------------------

weitjong | 2017-11-21 14:24:06 UTC | #8

Perhaps there is something wrong with how we setup for library building for the SHARED lib type and even to certain extent the STATIC lib type as well. The setup is non-trivial considering we have to make it work for MSVC/GCC/Xcode with the same build script. We have attempted to use the `--whole-archive` linker flag on GCC to get as much symbols included, nevertheless from the past user feedback we aware some symbols are still optimized away. Alternative to use "export map" is beyond our mean (no one would spend time to maintain the map in the long run).

p.s. Aside from this, there is inherently nothing wrong in using a SHARED lib. DLL is another story though, user need to worry certain thing when the DLL boundary is crossed.

-------------------------

slapin | 2017-11-21 15:03:52 UTC | #9

No exported symbols can be optimized-away from static library.
For shared it is possible to hide symbols, but that depends on the way it is built.
More likely is that some parts are excluded from being in .a which might be checked.
as for .so I think only URHO3D_API symbols are exported, hence the error is produced
for linking.

-------------------------

mazataza | 2017-11-21 21:16:27 UTC | #10

i agree that shared or static should work .. i think it may be related how DLL export symboles.

-------------------------

