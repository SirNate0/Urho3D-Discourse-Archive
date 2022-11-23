SeeSoftware | 2017-11-16 01:42:41 UTC | #1

Do all RefCounted objects have to be allocated on the heap like this:

    SomeObject *foo = new SomeObject(context_);
    foo->ReleaseRef(); // <- safe

or can you have them on the stack too:

    SomeObject bar(context_)
    bar.ReleaseRef(); // <- unsafe ?

-------------------------

magic.lixin | 2017-11-16 02:49:13 UTC | #2

 it`s OK I guess, only refCount_ is allocated in heap

-------------------------

Eugene | 2017-11-16 09:24:42 UTC | #3

It's okay to create `Object`s on the stack if you could gurantee that neither you nor Urho internal routines create `SharedPtr`-s for this object.

-------------------------

SirNate0 | 2017-11-17 21:18:29 UTC | #4

I think that you could even get away with creating SharedPtrs as long as you manually incremented the reference count first and the SharedPtrs are released before the object goes out of scope, though I'm not certain of this...

-------------------------

