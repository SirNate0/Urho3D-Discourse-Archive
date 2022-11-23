TrevorCash | 2017-09-21 21:25:03 UTC | #1

I'm currently in the middle of refactoring my project, I have a lot of c++ classes that reference each other and want to strictly use forward declarations in my header files.

In short - is this a valid structure:


MyClass.h:
> 
> class ReferenceClass;
> class MyClass {
>       public:
>        void DoThingsWithRef();
>        SharedPtr\<ReferenceClass> pRef;
> }

MyClass.cpp:
> 
> void MyClass::DoThingsWithRef()
> {
> pRef->DoThings();
> }

I Keep Getting Compile Errors:

    2>c:\urho3d-1.7\build\include\urho3d\core\../Container/Ptr.h(223): error C2027: use of undefined type 'GridGeographicData'
    2>c:\users\casht\repos\greatgame\GridWorld.h(15): note: see declaration of 'GridGeographicData'
    2>c:\urho3d-1.7\build\include\urho3d\core\../Container/Ptr.h(220): note: while compiling class template member function 'void Urho3D::SharedPtr<GridGeographicData>::ReleaseRef(void)'
    2>c:\urho3d-1.7\build\include\urho3d\core\../Container/Ptr.h(79): note: see reference to function template instantiation 'void Urho3D::SharedPtr<GridGeographicData>::ReleaseRef(void)' being compiled
    2>c:\users\casht\repos\greatgame\Grid.h(93): note: see reference to class template instantiation 'Urho3D::SharedPtr<GridGeographicData>' being compiled
    2>c:\urho3d-1.7\build\include\urho3d\core\../Container/Ptr.h(223): error C2227: left of '->ReleaseRef' must point to class/struct/union/generic type

-------------------------

Eugene | 2017-09-21 20:02:56 UTC | #2

Ensure that your class' destructor is defined in the cpp.

-------------------------

TrevorCash | 2017-09-21 21:28:21 UTC | #3

[quote="Eugene, post:2, topic:3592, full:true"]
Ensure that your class' destructor is defined in the cpp.
[/quote]

Thanks, 

Solved - This was part of the problem, also the SharedPtr do indeed work with forward declarations.

-------------------------

Eugene | 2017-09-22 09:10:28 UTC | #4

[quote="TrevorCash, post:3, topic:3592"]
SharedPtr do indeed work with forward declarations.
[/quote]
SharedPtr could work with incomplete type unless reference counter is used.
So, construction, destruction (including member destruction), assignment and copying of shared ptrs require complete type.

-------------------------

