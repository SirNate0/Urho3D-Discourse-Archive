simonsch | 2018-04-19 10:31:32 UTC | #1

Hello Community it is me again.

I have the following problem, i want in certain conditions to save my scene in memory and hold it outside the urho3d lifecycle. I don't want to write it as a persistent file i only want to hold the byte stream in memory. Is this possible? 

I found that there is a 'save()' function which takes a urho3d Serializer, but there is no example or code how to exactly using this function.

-------------------------

Adam77 | 2018-04-19 10:59:36 UTC | #2

Taken form LuaFile.cpp

bool LuaFile::Save(Serializer& dest) const
{
    if (size_ == 0)
        return false;

    dest.Write(data_, size_);

    return true;
}

-------------------------

simonsch | 2018-04-19 13:50:18 UTC | #3

Thy for the fast answer, yeah i already saw that. But how to determine what Serializer to use, should i use MemoryBuffer in my case? What are 'data_'? Is that the scene? How to determine the size of it?

-------------------------

Adam77 | 2018-04-19 14:54:26 UTC | #4

    /// File size.
    unsigned size_;
    /// File data.
    SharedArrayPtr<char> data_;

-------------------------

Eugene | 2018-04-19 14:14:37 UTC | #5

`VectorBuffer` is fine. Was designed exactly for this use case.

-------------------------

simonsch | 2018-04-19 14:22:21 UTC | #6

Sry to ask but, can you provide an example from the beginning of the initialization of this VectorBuffer, through saving the whole scene into it and reading it back, with all of its components?

Would be awesome^^, cause i can't figure out how to use this stuff.

-------------------------

Eugene | 2018-04-19 14:38:42 UTC | #7

Lol, it seems that binary serialization wasn't exposed into Lua bindings.
It seems that Lua has some problems with hierarchies and multiple inheritance.
I'll check things this evening.

[details="Disregard this"]
I suppose, this code would work
```
buffer = VectorBuffer()
scene:Save(buffer)
buffer:Seek(0)
scene:Load(buffer)
```
if you add few lines into `Urho3D/LuaScript/pkgs/Scene/Serializable.pkg`:
```
bool Load(Deserializer& source);
bool Save(Serializer& dest) const;
```

I wonder why this wasn't done before...
[/details]

-------------------------

simonsch | 2018-04-19 14:41:40 UTC | #8

If it would work with normal cpp code it would be enough, i still would wonder if it would work cause i have several data in my vertexbuffer. Will try the provided save, seek and load sampe and update here asap.

-------------------------

Eugene | 2018-04-19 14:41:48 UTC | #9

Damn, I thought for some reason that you need it in Lua /_-
Yes, it will work at C++ side.

-------------------------

simonsch | 2018-04-19 14:49:49 UTC | #10

But this also doesn't work as expected, my bound data which is in some vertexbuffer on the gpu are not available after saving and loading. The pure serialization and deserialization seems to work now without any issue, but the scene appears empty.

Ok ... i get a "Material index out of bounds".....

-------------------------

Adam77 | 2018-04-19 15:02:31 UTC | #11

Removed since I haven't read previous post.

-------------------------

Eugene | 2018-04-19 14:57:42 UTC | #12

[quote="simonsch, post:10, topic:4189, full:true"]
But this also doesn’t work as expected, my bound data which is in some vertexbuffer on the gpu are not available after saving and loading. The pure serialization and deserialization seems to work now without any issue, but the scene appears empty.

Ok … i get a “Material index out of bounds”…
[/quote]

Ahh... So, you have some manual resources.
This makes things more complicated.
How do you manage them? I have to look at your code.

-------------------------

simonsch | 2018-04-20 07:13:59 UTC | #13

Okay, i already thought that this will get complicated, before code i want to share more details why i need this. Maybe someone knows a proper solution for my problem. So as some people maybe already know from other threads, i am developing on Android. 

This means i need to use SDL to provide the necessary glue between my java stuff and my c++ code base. One drawback of using SDL is the 'Only one window allowed'-philosophy.

Assume i have a process generating data which i stream into my scene, urho holds this data persistent as long as its session persist.

Assume now i have second use case in my app where i need a second SDLActivity with a different scene.

The only way to make this possible is to destroy the first Activity before starting the second one. But when i exit activity two i want to be able to switch back to activity one with its previous state. I already thought about resharing the GLSurfaceView aka SDLSurfaceView, but had no idea how to do that. 

The problem is that everything is where i need it, the data are on the gpu before destroying the activity and this is fine. Start trying to copy it back to cpu just to hold the actual state of the scene seems like an overkill for me. We are talking about millions of vertices....

I hope this sketches out the whole problem, saving the complete scene like i wanted yesterday is not a proper solution i think.

IDEA:
Maybe i thought to complicated, i will try to use only one activity and hold 2 scenes in urho lifecycle. Then i switch between those scene in certain conditions, hope this will work.

-------------------------

johnnycable | 2018-04-20 08:19:19 UTC | #14

Only reason for having 2+ activities is you have to manage s.t. in android java (i.e, using android java gui / android system). If not, hold 2+ scene into urho/cpp.
Use urho save scene mechanism. Save scene make a scene freeze, if you then reload you have everything back. Just need to have asset on filesystem.
Only need to persist with a model of yours if you need s.t _faster_ than the urho save scene utility.

https://discourse.urho3d.io/t/problem-to-load-scene-from-xml-scene-replication/4173/5

-------------------------

simonsch | 2018-04-20 09:24:49 UTC | #15

I don't think this will work in my case, i want to avoid copying to much data only for holding a certain state of the render scene.

-------------------------

johnnycable | 2018-04-20 10:01:08 UTC | #16

That's not a render scene. It's the XML data binding to your game assets. When you reload the scene, every asset is reloaded, like the scene starts over again. This way, you can build your scene on demand from your starting data, plus the game delta (movement, animations and so on). 
Try example 18 for a test.

-------------------------

Eugene | 2018-04-20 11:34:37 UTC | #17

[quote="simonsch, post:13, topic:4189"]
Maybe i thought to complicated, i will try to use only one activity and hold 2 scenes in urho lifecycle. Then i switch between those scene in certain conditions, hope this will work.
[/quote]

I wonder why you didn't started from this point

-------------------------

