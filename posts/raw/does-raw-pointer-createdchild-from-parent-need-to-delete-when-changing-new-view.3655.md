Taymindis | 2017-10-14 06:30:03 UTC | #1

Hi developers, 

I've seen some example code there are created with raw pointer. 
Doesn't need to be deleted when change to new view?

Sample 1
```cpp 
Urho3D::Button* button = _uiRoot->CreateChild<Urho3D::Button>();
```
Sample 2
```cpp
Text* windowTitle = new Text(context_);
```

Sample 3
```cpp
URHO3D_HANDLER(SoundEffect, HandleSoundVolume);
```

-------------------------

KonstantTom | 2017-10-14 09:27:50 UTC | #2

No, they don't.
Sample 1: created button is child of `_uiRoot` (obviously) and stored in `SharedPtr` in `_uiRoot` (as any other child).

Sample 2: I think, there something like `_uiRoot->AddChild (windowTitle);` is exists below, so memory managment will be performed by parent element (as in Sample 1).

Sample 3: This macro is used for functions like this: 
```c++
void SubscribeToEvent(Object* sender, StringHash eventType, EventHandler* handler);
```
So, `Object` (class, see `Object.h`) will perform memory managment in this case.

-------------------------

Taymindis | 2017-10-14 07:00:29 UTC | #3

@KonstantTom

Nice! :slight_smile:  

Thanks,

-------------------------

Eugene | 2017-10-14 11:59:34 UTC | #4

If some function return raw pointer, you don't have to do any memory management: the object is already stored somewhere internally. However, you _may_ store the object in the `SharedPtr` if you don't want it to be internally destroyed.

I don't recommend to store `Scene` hierarchy objects (e.g. `Component`s, `Node`s and `UIElement`s) in `SharedPtr` because it tampers lifetime of the objects and may end up with crashes during destruction.

It is always safe to store raw pointer in `WeakPtr`.

-------------------------

