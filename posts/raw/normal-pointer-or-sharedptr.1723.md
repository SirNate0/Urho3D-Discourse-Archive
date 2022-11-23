Kanfor | 2017-01-02 01:09:42 UTC | #1

Is strictly necessary to use SharedPtr?
Is It wrong to use normal pointers?

Thanks  :wink:

-------------------------

thebluefish | 2017-01-02 01:09:42 UTC | #2

Yes/No and no.

Shared pointers are great because you will know if an object is deleted before the pointer, and it prevents some relatively bad issues as a result. However it is fine to use normal pointers as long as you pay attention.

Do note that you will want to keep a SharedPtr to an object as long as you want that object to stay alive. Otherwise you run into the possibility of the object getting deleted when the last SharedPtr pointing to it gets deleted. However beyond that, you can freely use normal points as much as you want.

-------------------------

Kanfor | 2017-01-02 01:09:42 UTC | #3

Thank you very much!  :slight_smile:

-------------------------

atai | 2017-01-02 01:09:43 UTC | #4

[quote="thebluefish"]Yes/No and no.

Shared pointers are great because you will know if an object is deleted before the pointe

Do note that you will want to keep a SharedPtr to an object as long as you want that object to stay alive. Otherwise you run into the possibility of the object getting deleted when the last SharedPtr pointing to it gets deleted. However beyond that, you can freely use normal points as much as you want.[/quote]

A related question is that, is there a reason not to use the C++ std::shared_ptr<> but a custom implementation in Urho3D?

-------------------------

weitjong | 2017-01-02 01:09:43 UTC | #5

[quote="thebluefish"]A related question is that, is there a reason not to use the C++ std::shared_ptr<> but a custom implementation in Urho3D?[/quote]
The SharedPtr questions have been asked a few times already in the forum. The most recent one is this. [topic1723.html](http://discourse.urho3d.io/t/solved-sharedptr-in-samples/1658/1). Urho3D SharedPtr uses intrusive refcounting.

-------------------------

valera_rozuvan | 2017-01-02 01:09:44 UTC | #6

From Urho3D documentation [urho3d.github.io/documentation/H ... tions.html](http://urho3d.github.io/documentation/HEAD/_conventions.html) :

[quote]Raw pointers are used whenever possible in the classes' public API. This simplifies exposing functions & classes to script, and is relatively safe, because SharedPtr & WeakPtr use intrusive reference counting.[/quote]

-------------------------

