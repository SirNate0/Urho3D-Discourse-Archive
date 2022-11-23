winduptoy | 2017-01-02 00:59:38 UTC | #1

Can someone please explain the usage of the [b]SharedPtr[/b] and [b]WeakPtr[/b] classes and when to use them? For someone who is new to pointers and memory management, an explanation in the documentation would be great.

Sorry if this is already in the documentation, I couldn't find it.

-------------------------

jorbuedo | 2017-01-02 00:59:38 UTC | #2

Usually if you don't know how to use them, you probably don't need them. 
I haven't used them here, but I suppose they work with the usual meaning that you can find for example here:
[cplusplus.com/reference/memory/shared_ptr/](http://www.cplusplus.com/reference/memory/shared_ptr/)
[en.cppreference.com/w/cpp/memory/weak_ptr](http://en.cppreference.com/w/cpp/memory/weak_ptr)

Basically a pointer is a small variable that directs you to another place, usually a bigger portion of memory. In object oriented programming, that may be an object. 
Shared and weak pointers are smart pointers that can free memory when an object is no longer referenced by anyone. 
If you have a shared pointer, you own an object that may be also owned and modified by someone else. If the last shared pointer to an object is removed, the object is deleted and the memory is freed. 
The weak pointer points to an object from someone else, and it does not prevent the object to be deleted without you knowing it. If you try to modify the pointed object, and it still exists, your weak pointer is temporally transformed into shared pointer, so you can work with your object, and then release it.

-------------------------

thebluefish | 2017-01-02 00:59:39 UTC | #3

Take the concept of a regular pointer. It's a variable that points to an object in the memory. Let's look at the downsides:

[ul]
[li] If the variable is deleted before the object is deleted, then there is nothing to keep track of the object and it is forever lost in memory. This is called a [url=http://en.wikipedia.org/wiki/Memory_leak]Memory Leak[/url].[/li]
[li] Multiple objects can keep a pointer reference to a given object. This can cause an issue where one object modifies the object, and the other objects assume that it's still valid. Say I have an object type Car. I have a class CarTracker that keeps a pointer to an instance of Car. I also have a class Highway that keeps a pointer to the same instance of car. Say we assume that CarTracker "owns" the Car object and deletes it because we got into a space-bending accident, then Highway tries to access Car without knowing it has been deleted.[/li]
[li] Conversely let's say that nobody owns Car, and neither tracker decides to delete it. Then we run into the aforementioned Memory Leak.[/li][/ul]

SharedPtr and WeakPtr are two classes designed to handle the problem of ownership of a pointer. In fact, modern day programming practices highly recommend the use of SharedPtr and WeakPtr instead of holding raw pointers. Even outside of Urho3D, we now have std::SharedPtr and std::WeakPtr to accomplish this.

SharedPtr keeps track of the object that it is pointing to globally. If my instance of Car is tracked by both Highway and CarTracker, then the SharedPtr will contain 2 references of it.
[ul]
[li]If CarTracker or Highway removes it, then instead of the object getting deleted, only CarTracker's reference to the object is removed and the Reference Counter is decreased to 1.[/li]
[li]If both CarTracker AND Highway remove their reference to the object, then the Reference Counter is decreased to 0. [/li]
[li]Since nothing references the object anymore, the SharedPtr class will delete the object at that point.[/li][/ul]

WeakPtr helps to solve the problem of ownership. For example, if the previously mentioned instance of Car were supposed to be deleted as soon as CarTracker removes it, then SharedPtr cannot solve this on its own.
[ul]
[li] In this case, CarTracker should continue to hold a SharedPtr since it "owns" the Car.[/li]
[li] Highway should instead hold a WeakPtr. This way if CarTracker removes the Car, the Car should be gone.[/li]
[li] If the Car is gone and Highway still references the Car, then Highway will simply get a NULL value when attempting to access the pointer. This way we safely know when we no longer have a Car to track and can take appropriate action.[/li][/ul]

Let me know if you have any more questions and I will do my best to clear things up for you :slight_smile:

-------------------------

friesencr | 2017-01-02 00:59:39 UTC | #4

What is the purpose of a WeakPtr over a normal pointer.

-------------------------

gunnar.kriik | 2017-01-02 00:59:39 UTC | #5

[quote="friesencr"]What is the purpose of a WeakPtr over a normal pointer.[/quote]

For safety reasons. If a the data pointed to by a raw pointer is deleted somewhere else then you have no way of knowing if that data is no longer there if you don't own the data. A weak pointer will allow you to test for this when you convert the weak pointer to the shared pointer (when you wish to access the data pointed to by the weak ptr). If the data isn't there anymore, then you get an empty shared ptr or null reference, or something else which is consistent. This way you can avoid a lot of weird crashes and memory corruptions amongst other things. Hope that made sense.

-------------------------

lexx | 2017-01-02 00:59:40 UTC | #6

[I'm coming from java/c# world so this is the area that I still doesnt understand really]

I had very difficult to understand shared_ptr and weak_ptr but thanks to everyone, now I think I understand these (more or less). Still I wonder, should I use always SharedPtr myObj;  or ie void *myObj;  Do you C++ programmers use always shared/weak pointers and forgot these "raw" pointers?

-------------------------

gunnar.kriik | 2017-01-02 00:59:40 UTC | #7

[quote="lexx"] Still I wonder, should I use always SharedPtr myObj;  or ie void *myObj;  Do you C++ programmers use always shared/weak pointers and forgot these "raw" pointers?[/quote]

There is a place for code which uses raw pointers, but generally when you find yourself writing delete statements, you should look at your code and reconsider what you are doing (e.g. not use raw pointers). It seems simple and easy at first, but using raw pointers WILL at some point get you into the realm of memory leaks, memory corruption and random segfaults. I recommend reading Scott Meyers "Effective C++" if you feel that you need advice on what to do and what not to do in C++. In fact, if there is one C++ book you should read then this is it. It's rather short, and offers excellent advice, although you might not appreciate / understand all of it at first if you are rather new to C++, but worth the read nonetheless. Mind you that Effective C++ third edition isn't updated with the latest C++11 spec, but I heard that will arrive soon.

-------------------------

cadaver | 2017-01-02 00:59:41 UTC | #8

Urho3D uses intrusive reference counting (refcount is in the object itself, the RefCounted class) so it's always valid to create a shared pointer from a raw pointer, or vice versa. 

What you should watch out that creating a SharedPtr manipulates the refcount, and for performance reasons this is not made thread-safe. So at least when you work with threads, you should rather use raw pointers. 

Adding on what Gunnar said, generally you should be very careful if you find yourself writing delete statements for objects that derive from RefCounted. Because if there's a SharedPtr somewhere referencing that object, it will also delete the object when the refcount goes to zero. A double delete will result in a crash.

Also when you don't need to hold on to the object (for example, when you need it only for a duration of a function), using a SharedPtr is unnecessary overhead.

-------------------------

thebluefish | 2017-01-02 00:59:43 UTC | #9

[quote="cadaver"]What you should watch out that creating a SharedPtr manipulates the refcount, and for performance reasons this is not made thread-safe. So at least when you work with threads, you should rather use raw pointers.[/quote]

Why not make it thread-safe? So long as raw pointers and shared pointers are intermixed for a given object, it's at that point guaranteed that the ref count doesn't drop to 0 when there is still actually a reference to the object.

Enforcing best code practices for the benefit of thread safety far outweighs compatibility for outdated and unnecessary code practices.

-------------------------

jorbuedo | 2017-01-02 00:59:43 UTC | #10

[quote="thebluefish"][quote="cadaver"]What you should watch out that creating a SharedPtr manipulates the refcount, and for performance reasons this is not made thread-safe. So at least when you work with threads, you should rather use raw pointers.[/quote]

Why not make it thread-safe? So long as raw pointers and shared pointers are intermixed for a given object, it's at that point guaranteed that the ref count doesn't drop to 0 when there is still actually a reference to the object.

Enforcing best code practices for the benefit of thread safety far outweighs compatibility for outdated and unnecessary code practices.[/quote]

As he said, it's not about compatibility for outdated and unnecessary code practices, it's about performance. 
Thread safety is avoiding race conditions, and ensuring that for everything is costly. In a game engine, even if you try to make it easy, sometimes you have to go for performance and leave the safety to the programmer.

-------------------------

