SteveU3D | 2017-10-20 10:04:06 UTC | #1

Hi,
I wrote an application using Urho3D in QML (see  https://github.com/SteveTJS/urho3DInQML) and I have a crash when deleting the Urho3D class named "Urho3DApplication" in the code.
In fact, I need to delete and create again this class at runtime.

The error I get is : 
    
    in Urho3D/Container/RefCounted.cpp line 42 : Assertion refCount_->refs_ == 0.

So I assume it is due to non deleted objects. In the Urho3DApplication destructor, I tested with : 
    
    Urho3DApplication::~Urho3DApplication()
    {
        mScene->RemoveAllChildren();
        mScene->RemoveAllComponents();
        mScene->Clear();
    }
    
and others things, but I still get the crash and the same error.
Any ideas?

-------------------------

Eugene | 2017-10-20 10:31:05 UTC | #2

You are not allowed to `delete` SharedPtr. Use any other technique to reset the content (Reset or assign empty).
Moreover, I suggest you to forget about C++ statement `delete` at all. It gives nothing but pain.

-------------------------

SteveU3D | 2017-10-20 14:48:54 UTC | #3

:expressionless: Indeed, my bad, still used to new / delete pointers.
Thanks!

-------------------------

