throwawayerino | 2019-07-22 16:00:05 UTC | #1

I want to pass data within an event using a struct (or similar if needed). `VariantMap` sent with the event seems to only accept specific classes.

-------------------------

ab4daa | 2019-07-22 16:51:04 UTC | #2

Maybe use void* to save custom struct in Variant?

    struct s {} a_s;
	Variant v(static_cast<void*>(&a_s));
	s * recv = static_cast<s*>(v.GetVoidPtr());

-------------------------

throwawayerino | 2019-07-22 16:26:01 UTC | #3

That's plausible and is what I'm actually doing, but I was hoping to find another solution

-------------------------

Dave82 | 2019-07-22 16:41:10 UTC | #4

Is there any valid reason why you need a custom type ?

-------------------------

throwawayerino | 2019-07-22 16:44:32 UTC | #5

I want to pass more than one type of data (string, image, etc) all in one structure. A struct looks (to me) as the best way.

-------------------------

Dave82 | 2019-07-22 16:50:02 UTC | #6

You could use VariantMap

Also this : 
[quote="ab4daa, post:2, topic:5320"]
struct s {} a_s; Variant v(static_cast<void*>(&a_s)); s * recv = static_cast<s*>(v.GetVoidPtr());
[/quote]
Is not a good idea to use. Once your a_s goes out of scope your void* becomes invalid. you can dynamically allocate a_s but then you have to track all your structs to prevent memory leaking by deleting them manually when they become useless

-------------------------

TheComet | 2019-07-22 16:55:34 UTC | #7

I would recommend adding your data to the VariantMap directly instead of first packing it into a struct.

```cpp
VariantMap data;
data["string"] = String("bla");
data["image"] = myImagePtr;
// etc
SendEvent(E_WHATEVER, data);
```

-------------------------

Leith | 2019-07-23 06:03:20 UTC | #8

Urho has support for custom variant types, but I have not toyed with it.
Variants tend to do (almost) everything I expect, with the exception of providing compare operators for equivalent types, or even acknowledging that type equivalency is potentially possible.
<https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_custom_variant_value.html>

-------------------------

dertom | 2019-08-04 13:23:14 UTC | #9

As @Leith mentioned you can use CustomVariantValue. I just used it the first time and it works as follows (at least it works for JSONObject) Use MakeCustomValue (which is located in Variant.h) to envelope your object:

put:
```
        VariantMap map;
        map[P_DATA]=MakeCustomValue(yourvalue);
```

And use GetCustom() to get it out again...

get:

```

    // eventData is the incoming VariantMap
    JSONObject data  =  eventData[P_DATA].GetCustom<YOURTYPE>();
```

Hope that helps

-------------------------

