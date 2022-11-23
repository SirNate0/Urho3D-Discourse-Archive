haolly | 2017-11-25 15:45:52 UTC | #1

``` c++
// Make a copy of the context pointer in case the object is destroyed during event handler invocation
    Context* context = context_;
    EventHandler* specific = nullptr;
    EventHandler* nonSpecific = nullptr;

```

The comment "Make a copy ..." really confuse me,  the code ` Context* context = context_` really is a pointer assignment,
the content of *context_* is not  copied to *context* , so if `context_` is destroyed , say `context_ = nullptr`, so `context` is also 
be invalid to use, because they are point to the same address.

It will be appreciate if someone explain the code a bit more.
I recently wanted to learn an open source game engine, so I try to read the source and fing out what it was doing.

-------------------------

Eugene | 2017-11-25 12:38:48 UTC | #2

[quote="haolly, post:1, topic:3784"]
It will be appreciate if someone explain the code a bit more.
[/quote]
Context is considered as immortal object among any other `Object`s, so it's never destructed in any function.
However, event processing could destroy _the object_, so `context_` become invalid.

If you have small quetions like this, it's probably makes sence to ask them [here](https://gitter.im/urho3d/Urho3D)

-------------------------

haolly | 2017-11-27 12:02:09 UTC | #3

Eugene , thanks for you reply.
You mean the event receiver itself may be destroyed during event processing?
 Is there Only one `Context` object living in the whole lifetime of the engine run time ?

Gitter is a good place,  I will  post my left small question there to see if it would be overwhelmed by others discussions

-------------------------

Eugene | 2017-11-29 06:34:07 UTC | #4

[quote="haolly, post:3, topic:3784"]
You mean the event receiver itself may be destroyed during event processing?
[/quote]

Exactly.

[quote="haolly, post:3, topic:3784"]
Is there Only one Context object living in the whole lifetime of the engine run time ?
[/quote]
In most cases you don't need more that one context.
There is nothing wrong in creating and using multiple ones tho.

However, I don't recommend to run multiple instances of the engine in separate contextes, because it's only theoretically working and almost untested.

In summary, you could use as much contextes as you need, but don't create more than one `Engine`.

-------------------------

