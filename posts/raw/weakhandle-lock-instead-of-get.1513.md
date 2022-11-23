Enhex | 2017-01-02 01:08:12 UTC | #1

Wouldn't it be more semantically correct to use Lock() instead of Get() for WeakHandle?
Lock() means getting a shared pointer and Get() means getting a raw pointer.
Since the current Get() function returns RefCounted@ it should be named Lock() instead.

-------------------------

Enhex | 2017-01-02 01:08:13 UTC | #2

Wouldn't that count as Lock() functionality, even tho the C++ side uses Get()?

-------------------------

cadaver | 2017-01-02 01:08:14 UTC | #3

Practically, the codebase is full of cases where C++ does just appropriately checked raw pointer access directly from WeakPtr's, or has GetXXX() APIs that return a raw pointer, while in AngelScript you must remember that every time you get an object through any of these API's, and put it to a handle, you're holding a strong ref. So having Lock() in this one case wouldn't make much difference to the mental burden.

(Because we have intrusively refcounted objects, we have the option of skipping Lock() safely when we are just interested in the object itself and not holding it in a SharedPtr. So in that regard Urho deviates from the std library.)

-------------------------

