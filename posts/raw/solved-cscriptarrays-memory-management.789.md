setzer22 | 2017-01-02 01:02:54 UTC | #1

As a young magician apprentice I'm not even starting to grasp all the magic and mysteries behind this class. It keeps me awake at night and is the source for 50% of the bugs in my project. I seek for advice in the obscure art of registering methods to the Script API...

Now seriously! I'm using a mixture of C++ and AngelScript in my project and to do so I'm registering each of my C++ components to the Script API. 

Sometimes you have to return an array handle because it's the most sensible thing to do for an API, even if that involves the overhead of converting a Vector<T> into a CScriptArray*. Looking through Urho's source I've come up with many of the answers on how to do so. I've got two questions:

First of all, and that's just a confirmation: When registering a function that returns a CSriptArray as something like Array<IntVector2>@ I should get the return value with a @ right? Because CScriptArray doesn't inherit from RefCounted. This has worked for me but I want to know if I've got it right.

And second, when I do something like: 

CScriptArray* GetSomething() {
     Vector<Something> v = GetSomething(); //Returns a Vector, overloaded method.
     return VectorToArrau<Something>(v, "Array<Something");
}

Does the CScriptArray get auto-deleted when nothing points to it anymore? Should I use auto-handles for the registered return value for that matter? (Array<Something>@+ instead of Array<Something>@).

Thanks!

-------------------------

cadaver | 2017-01-02 01:02:54 UTC | #2

When the array is a function return value and you use the VectorToArray helper functions, you should not use auto handles (@+) but a normal handle (@) as the helpers already set the right refcount value for the array (basically just by constructing it.)

On the other hand, if the array is passed from script to C++ as a function parameter, auto handles will be preferable so that the C++ side doesn't need to do any refcount management.

I think Urho's built in API adheres to these conventions throughout, so by following / copying it you should be safe.

CScriptArray is an AngelScript refcounted class in contrast to Urho refcounted class. But nevertheless, it will be auto-deleted when nothing holds a strong ref (handle) to it anymore.

-------------------------

setzer22 | 2017-01-02 01:02:54 UTC | #3

Thank you!

-------------------------

