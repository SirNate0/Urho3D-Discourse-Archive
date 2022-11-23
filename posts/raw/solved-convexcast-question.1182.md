Dave82 | 2017-01-02 01:05:55 UTC | #1

Hi i'm trying to re-work my existing character controller because i don't like force driven character controllers. They have countless issues and they just don't react as they should. So i decided to use convex cast 
first thing i've noticed is the PhysicsWorld::ConvexCast function require a btCollisionShape instead of Urho3D::CollisionShape , so ive tried to create a btCapsuleShape but it fails with the following unresolved externals 

[code]1>INFCharacterController.obj : error LNK2001: unresolved external symbol "void * __cdecl btAlignedAllocInternal(unsigned int,int)" (?btAlignedAllocInternal@@YAPAXIH@Z)
1>INFCharacterController.obj : error LNK2001: unresolved external symbol "public: __thiscall btCapsuleShape::btCapsuleShape(float,float)" (??0btCapsuleShape@@QAE@MM@Z)
1>INFCharacterController.obj : error LNK2001: unresolved external symbol "void __cdecl btAlignedFreeInternal(void *)" (?btAlignedFreeInternal@@YAXPAX@Z)[/code]

is there any idea how to get ConvexCast working ?


EDIT :
Never mind... i just saw there is a Urho3D::CollisionShape version of the function... Intellisense was broken again (:x i hate when that happens) and it didn't listed the another function

-------------------------

globus | 2017-01-02 01:05:55 UTC | #2

Linker errors

-------------------------

