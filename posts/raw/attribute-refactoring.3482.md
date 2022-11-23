Eugene | 2017-08-23 21:59:28 UTC | #1

Here is semi-major attribute refactoring.
I would be happy if someone review code and/or test changes before I push it.
https://github.com/urho3d/Urho3D/pull/2091

1. Arbitrary attribute metadata was added.

Attribute metadata is per-attribute `VariantMap` with custom values.
The only way to set metadata is to call `SetMetadata` on `URHO3D_ATTRIBUTE`-like macros. `SetMetadata` calls may be chained.

Metadata may be acquired via `AttributeInfo::GetMetadata` or `AttributeInfo::GetMetadata<T>`. It is also exposed to Angel Script.

2. Offset-based attributes were removed due to unsafety.

`URHO3D_ATTRIBUTE` and `URHO3D_ENUM_ATTRIBUTE` are aliased to accesor attributes now. So, offset can't be used to identify attribute anymore. Use attribute name or metadata. See `Constraint` for example.

Attribute type hacking will get broken. If you lied with attribute type, code won't compile. E.g. `Light::CascadeParameters::splits_` were `float[4]` and serialized like `Vector4`. Don't lie to your compiler anymore.

3. Vector structure elements and corresponding defines were removed, @KonstantTom.

Use metadata variable `AttributeMetadata::P_VECTOR_STRUCT_ELEMENTS` instead. It shall be initialized with `StringVector` instead of `const char*[]`, no trailing zero is needed.

-------------------------

yushli1 | 2017-08-24 02:03:06 UTC | #2

Can you compare the performance difference between these changes, especially the retiring the offset part.

-------------------------

KonstantTom | 2017-08-24 07:40:54 UTC | #3

[quote="Eugene, post:1, topic:3482"]
3. Vector structure elements and corresponding defines were removed,
[/quote]
These changes are fine to me. Arbitrary metadata is much more flexible. It looks good for me.

-------------------------

Alex-Doc | 2017-08-24 06:28:29 UTC | #4

It looks good to me.

The only thing I don't like is the new line for [code].SetMetadata[/code] but it's just a matter of personal taste.

-------------------------

Eugene | 2017-08-24 11:11:18 UTC | #5

[quote="yushli1, post:2, topic:3482, full:true"]
Can you compare the performance difference between these changes, especially the retiring the offset part.
[/quote]

Performance is not affected. The test below take the same time with both old and new version (75++5 ms for Debug, 10-+0.5 ms for Release). I didn't test metadata-related changes because they have very limited area.

[details=Code]
    #include <Urho3D/Scene/Serializable.h>
    #include <Urho3D/IO/VectorBuffer.h>
    #include <Urho3D/Core/StringUtils.h>
    #include <chrono>

    using namespace Urho3D;

    #define URHO3D_NEW_ATTRIBUTE(name, typeName, variable, defaultValue, mode) URHO3D_ACCESSOR_ATTRIBUTE_FREE(name, [](const ClassName* classPtr) -> typename AttributeTrait<typeName >::ReturnType { return classPtr->variable; }, [](ClassName* classPtr, typename AttributeTrait<typeName >::ParameterType value) { classPtr->variable = value; }, typeName, defaultValue, mode)
    #undef URHO3D_ATTRIBUTE
    #define URHO3D_ATTRIBUTE(name, typeName, variable, defaultValue, mode) URHO3D_NEW_ATTRIBUTE(name, typeName, variable, defaultValue, mode)

    class TestSerializable : public Serializable
    {
       URHO3D_OBJECT(TestSerializable, Serializable);

    public:
       TestSerializable(Context* context) : Serializable(context)
       {
          bool_ = !!Random(0, 1);
          int_ = Random(1, 100);
          float_ = Random(1.0f, 100.0f);
          string_ = String(Random(1, 100));
          vector_ = { Random(1, 100), Random(1, 100), Random(1, 100) };
          map_ = { { "1", Random(1, 100) }, { "2", Random(1, 100) }, { "3", Random(1, 100) } };
       }
       static void RegisterObject(Context* context)
       {
          context->RegisterFactory<TestSerializable>();

          URHO3D_ATTRIBUTE("Bool", bool, bool_, false, AM_DEFAULT);
          URHO3D_ATTRIBUTE("Int", int, int_, 0, AM_DEFAULT);
          URHO3D_ATTRIBUTE("Float", float, float_, 0.0f, AM_DEFAULT);
          URHO3D_ATTRIBUTE("String", String, string_, String::EMPTY, AM_DEFAULT);
          URHO3D_ATTRIBUTE("VariantVector", VariantVector, vector_, Variant::emptyVariantVector, AM_DEFAULT);
          URHO3D_ATTRIBUTE("VariantMap", VariantMap, map_, Variant::emptyVariantMap, AM_DEFAULT);
       }
    private:
       bool bool_;
       int int_;
       float float_;
       String string_;
       VariantVector vector_;
       VariantMap map_;
    };

    size_t Test(Context* context)
    {
       TestSerializable::RegisterObject(context);
       Vector<SharedPtr<TestSerializable>> objects;
       for (int i = 0; i < 10000; ++i)
          objects.Push(MakeShared<TestSerializable>(context));
       VectorBuffer output;
       output.Resize(1024 * 1024);

       auto t1 = std::chrono::high_resolution_clock::now();
       for (TestSerializable* object : objects)
          object->Save(output);
       auto t2 = std::chrono::high_resolution_clock::now();
       size_t us = (size_t)std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count();

       File file(context);
       file.Open("C:/output.bin", FILE_WRITE);
       file.Write(output.GetData(), output.GetSize());
       file.Close();
       return us;
    }
[/details]

[quote="Alex-Doc, post:4, topic:3482"]
The only thing I don’t like is the new line for .SetMetadata but it’s just a matter of personal taste
[/quote]
The idea is pretty simple here. Have you heard about "single line -
 single declaration" rule in C++? Here is the same situation. Metadata  is the declaration of the new variable inside the map, so it shall be placed on its own line.
The same is about variadic `SendEvent`: I'd like to put every event parameter on its own line.

-------------------------

TheComet | 2017-08-24 10:57:15 UTC | #6

In this test code you're not really testing the performance of ```object->Save()```, you're testing the hundreds of memory allocations that are occurring in VectorBuffer, which are comparatively slow to serialization.

I can't test it for myself now but recommend reserving space on the vector buffer before doing the test and see if it makes any difference.

```cpp
output.Resize(sizeof(TestSerializable) * 10000);  // Not entirely sure how attributes contribute to the size of the serialized data, so maybe you need to increase this factor
```

-------------------------

Eugene | 2017-08-24 11:23:49 UTC | #7

[quote="TheComet, post:6, topic:3482"]
In this test code you’re not really testing the performance of object-&gt;Save(), you’re testing the hundreds of memory allocations that are occurring in VectorBuffer, which are comparatively slow to serialization.
[/quote]

Hundreds of memory allocations take only about 10% of overall time. New test results:

Debug Old: 65..75 ms;
Debug New: 70..76 ms;
Release Old: 8.8..10 ms;
Release New: 9.3..10 ms.

-------------------------

yushli1 | 2017-08-24 12:58:21 UTC | #8

How are the meanings of these results? Does that mean Release Old use 8.8 to 10 ms while Release New use 9.3 to 10 ms? 
Also VauleAnimation and ObjectAnimation relies on AttributeAnimation. We may need to test their performance differences before commiting such a fundamental code change as well.

-------------------------

yushli1 | 2017-08-24 13:38:44 UTC | #9

Please come back often and give the valuable opinions. It may take you ten minutes but will save a lot of arguments and point the right direction for this amazing engine. Like the retiring the attribute offset thing, do you think it will affect the overall performance since AttributeAnimation, ValueAnimation and ObjectAnimation are all depending on it?

-------------------------

Eugene | 2017-08-24 13:38:44 UTC | #10

I don't understand why do you care about performance at all.
1. offset attributes is an old hack that should be removed ASAP. 
2. Performance can't be worse than accessor attributes.
3. Only 25% of urho attributes are affected.

-------------------------

yushli1 | 2017-08-24 13:55:14 UTC | #11

Debug Old: 65…75 ms;
Debug New: 70…76 ms;
Release Old: 8.8…10 ms;
Release New: 9.3…10 ms.

Judging from this test result,  new performance is  actually a bit slower, consistently in both debug and release.

-------------------------

Eugene | 2017-08-24 14:18:29 UTC | #12

You should treat these results as 'accessor attributes are negligibly slower (~5% in release mode) than offset attributes due to two extra pointer-to-function calls'.
Then, my refactorig is obligatory migration to accessor attributes without breaking API for safety reasons.

-------------------------

Enhex | 2017-08-24 14:44:38 UTC | #13

I understand fixing Undefined Behavior with the offset usage (just use lambda accessor instead?).

I don't understand why:
1. you need attribute meta info
2. overhead is introduced

-------------------------

Eugene | 2017-08-24 14:54:36 UTC | #14

[quote="Enhex, post:13, topic:3482"]
you need attribute meta info
[/quote]

I just wanted to add attribute metadata at some point and get rid of kludge named 'vector structure elements'. When I tried to remove offset attributes, I understood that the point is now. See changes in Constraint.cpp in my PR.

[quote="Enhex, post:13, topic:3482"]
overhead is introduced
[/quote]
What overhead do you mean?

-------------------------

yushli1 | 2017-08-24 15:08:39 UTC | #15

5% slower in release mode consistently is not negligible for such a core feature because many other features are depending on it, like ValueAnimation, ObjectAnimation, Serialization, Deserialization and Networking. Using offset exists safely for many years and should not be changed just for so called safety at the price of performance. And this change cannot be opt out. I suggest only commit such a change with thorough test and ensure no negative performance introduced at all.

-------------------------

Enhex | 2017-08-24 16:54:56 UTC | #16

[quote="Eugene, post:14, topic:3482"]
vector structure elements
[/quote]

Looked at it a bit, undocumented and looks quite messy. I'm not sure I understand what is it used for (stores names of members encoded into a VariantVector?).
Also it only seems to be used in a single place in the editor, which is also undocumented.

Internally Urho uses URHO3D_ACCESSOR_VARIANT_VECTOR_STRUCTURE_ATTRIBUTE for two classes: StaticModelGroup and SplinePath.

They seem to use VariantVector to store known ID type + size count as the first element, which doesn't make sense (just use a `vector<T>` of the known type).
Is it because serialization doesn't support vector<T> or something?

To me it seems this kludge should be completely removed and replaced with a proper solution.
If meta info suppose to replace it, it still doesn't solve the underlying kludge that caused it in the first place.

-------------------------

Eugene | 2017-08-24 16:31:05 UTC | #17

> 5% slower in release mode consistently is not negligible for such a core feature

So, it's the problem of accessor attributes introduced six years ago. Accessor attributes were _designed_ to make code more _simple_ and _safe_ despite some performance loss. Do you think it was bad decision? Why nobody cared about it for six years?

> should not be changed just for so called safety at the price of performance

Undefined Behavior must not be used. Consider this as axiom.

Think the opposite: there is no reason to use unsafe code unless it is noticeably faster.
Now the difference is too small to care about. Note that random performance fluctuation is much bigger than performace loss. So, performace loss is negligibly small.
![image|480x288](upload://4tv1sKQO66ixWXv1ag70SwyUppE.png)

100 tries, test duration measured in microseconds.

-------------------------

Enhex | 2017-08-24 16:58:17 UTC | #18

You should label charts.

Also there are benchmarking frameworks for getting statistically sound results.
https://github.com/nickbruun/hayai
https://github.com/DigitalInBlue/Celero
https://github.com/google/benchmark

-------------------------

Eugene | 2017-08-24 17:01:42 UTC | #19

[quote="Enhex, post:16, topic:3482"]
To me it seems this kludge should be completely removed and replaced with a proper solution.

If meta info suppose to replace it, it still doesn’t solve the underlying kludge that caused it in the first place.
[/quote]

What do you call 'proper solution'? Metadata is designed to be something that _is not used_ by the engine core.

> stores names of members encoded into a VariantVector?

 It stores display names of VariantVector elements.

-------------------------

cadaver | 2017-08-24 17:17:40 UTC | #20

On the performance of attribute animations, regardless of whether set accessor or offset access is used, the path to getting the value into the intended destination is complex and ugly. If there are 100's or 1000's of scene objects which need to animate this way, so that the time taken to apply the animations is significant, then optimizing to an explicit update could be beneficial. Also note the call to ApplyAttributes() which is necessary according to how the attributes work and how they may have late-applied side-effects. In most cases when you know what you're animating, it should be unnecessary, but the animation system cannot decide that.

-------------------------

Enhex | 2017-08-24 17:48:39 UTC | #21

What I understood from:
> I just wanted to add attribute metadata at some point and get rid of kludge named ‘vector structure elements’. 

is that metadata suppose to replace `vector structure elements`.
What I'm saying is to begin with `vector structure elements` was added to handle a kludge of using `VariantVector` instead of `vector<T>`.
Solving original vector kludge -> `vector structure elements` isn't needed -> nothing to replace.

Extra name info is only used by the editor, for displaying things.
That means that the naming info can be implemented in a way which is completely external to the engine.

Or just display `vector<T>` without naming each element entry, just indenting and/or with some default name like "element", so no extra naming info is needed. Though that might degrade UX.

-------------------------

Eugene | 2017-08-24 18:30:36 UTC | #22

>Or just display vector<T> without naming each element entry, just indenting and/or with some default name like “element”, so no extra naming info is needed

It sux.
![image|365x318](upload://AgE71qE6Grv5yL6CKCAplZdjqV3.png)

> That means that the naming info can be implemented in a way which is completely external to the engine

It was implemented inside an Editor year ago. If you need to hack Editor code to make the component attributes work, the architecture sux.

> Solving original vector kludge
How to do it? What's T for BillboardSet?

-------------------------

Lumak | 2017-08-24 19:17:35 UTC | #23

I was reluctant about this, especially regarding if this will cause loss in performance. However, this statement:
[quote="Eugene, post:17, topic:3482"]
Think the opposite: there is no reason to use unsafe code unless it is noticeably faster.
[/quote]
want to give this a benefit of doubt.

-------------------------

Eugene | 2017-08-24 22:23:18 UTC | #24

@cadaver May you elaborate how Constraint attributes work?
There is `Position` attribute. When it is set via serializable interface, `otherPosition_` is updated. When it is set via `SetPosition`,`otherPosition_` is untouched.
What's the point?

-------------------------

KonstantTom | 2017-08-24 20:15:13 UTC | #25

[quote="Enhex, post:16, topic:3482"]
Internally Urho uses URHO3D_ACCESSOR_VARIANT_VECTOR_STRUCTURE_ATTRIBUTE for two classes: StaticModelGroup and SplinePath.
[/quote]

Also it's used by BillboardSet in which each billboard has position, size, uv, color and other parameters. So, vector structure elements are designed for cases such as BillboardSet billboards.
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/BillboardSet.cpp#L60

-------------------------

Enhex | 2017-08-24 23:50:05 UTC | #26

With BillboardSet, you got a vector of `Billboard`'s, T is `Billboard`.
I didnt mean just display "count".
For something like StaticModelGroup, you have NodeIDs, so it will say something like "NodeIDs count/size".
We're suppose to be serializing `vector<T>` as an attribute here, so it should already have a name. We also don't just serialize some random set of unnamed attributes for each element, we're serializing T. Information about T's attributes should be provided, including their names.
So it's more like a nested type attributes thingy. And there's no need for editor-side stuff.
A good example for nested type serialization thingy is [cereal library](http://uscilab.github.io/cereal/). Now that we can use C++11 we could do something similar.

Looking at Urho I see that the `AttributeInfo` type is limited to the hardcoded `VariantType`'s. That means that adding "nested type serialization" support will require a refactor to support any type. I'm assuming other things rely on attributes to use `Variant`, so it may also require further refactoring of other code to be more generic.
The rabbit hole goes deeper. Perhaps it will be better to find the most low level part that requires refactoring and start from there, and work our way up to attributes. To me it seems to be usage of `Variant` where generic templates could've been used.

I don't have a full overview about what attributes are used for, and what they require to be able to do. If I'm missing something let me know (documentation's welcome!).

@KonstantTom Thanks, forgot to search for the `MIXED` macro version. This post also addresses your point.

-------------------------

yushli1 | 2017-08-25 02:47:47 UTC | #27

void AttributeAnimationInfo::ApplyValue(const Variant& newValue)
{
    Animatable* animatable = static_cast<Animatable*>(target_.Get());
    if (animatable)
    {
        animatable->OnSetAttribute(attributeInfo_, newValue);
        animatable->ApplyAttributes();
    }
}
If attribute are to be redesigned and improved, I think it should take this use case into consideration. Each update will need to set the attribute by using a Variant, while the type information of the variant is already known when creating the animation. That actually waste a lot of execution time. Can this variant be taken away at compile time, say, by using template?

-------------------------

Eugene | 2017-08-25 06:36:32 UTC | #28

[quote="Enhex, post:26, topic:3482"]
Now that we can use C++11 we could do something similar.
[/quote]

[quote="yushli1, post:27, topic:3482"]
Each update will need to set the attribute by using a Variant, while the type information of the variant is already known when creating the animation.
[/quote]

We couldn't. We will never be able to mix templates and polymorphism. Unless we drop all virtual cascades and do serialization in the header, we cannot perserve real type in any way and get rid of Variant. And it's not the point of this topic because of it.

[quote="yushli1, post:27, topic:3482"]
That actually waste a lot of execution time
[/quote]

We often lose execution time to make code usage convinient. The more generic engine is, the more performance is lost.

-------------------------

hdunderscore | 2017-08-25 07:05:45 UTC | #29

I think the solution provided is relatively clean. The mixing of macro and method chaining is a bit on the ugly side but should do.

The performance test appears to have been done only for saving ? How relevant is that performance test on the average run-time of a game?

-------------------------

Enhex | 2017-08-25 08:09:31 UTC | #30

[quote="yushli1, post:27, topic:3482, full:true"]
Can this variant be taken away at compile time, say, by using template?
[/quote]
Yes. The type is known at compile time. `AttributeAnimationInfo` should be templated to animate `T` and use
`ApplyValue(const T& newValue)`. The question is what else needs to be refactored.

[quote="Eugene, post:28, topic:3482"]
We couldn’t. We will never be able to mix templates and polymorphism. Unless we drop all virtual cascades and do serialization in the header, we cannot perserve real type in any way and get rid of Variant. And it’s not the point of this topic because of it.
[/quote]
Can you better explain what's the problem with Cereal's approach?
The topic started with trying to fix code smell. I think it's better to dig deep, find the root cause, and fix it.

[quote="Eugene, post:28, topic:3482"]
We often lose execution time to make code usage convinient. The more generic engine is, the more performance is lost.
[/quote]
This is wrong.
Again, look at Cereal - ***much*** simpler and convenient code usage than Urho's serialization, without losing any execution time, in fact it's even faster because things are being done at compile time.
And it's more generic than Urho's serialization - it can handle any type.

You're not trading off execution time for usage connivance.
You're trading off proper problem solving and design for an easier problem (which is not inherently a bad thing, common practice when considering resource constraints).

If anyone which is familiar with Attribute and/or Attribute animation can give me complete requirements for what they need to technically do (instead of me guessing and missing stuff by looking at code), I could try to prototype a system that uses templates to see if it's feasible.
Meanwhile I can start prototyping based on what I already understand.

In general documentation for developers could be nice - overviews of how systems in the engine are designed, what problem they're trying to solve and how. It's much faster and safer than trying to guess and assume based on code.

-------------------------

yushli1 | 2017-08-25 08:19:38 UTC | #31

[quote="Enhex, post:30, topic:3482"]
, I could try to prototype a system that uses templates to see if it’s feasible.

Meanwhile I can start prototyping based on what I already understand.
[/quote]

I will vote for this try.

-------------------------

Enhex | 2017-08-25 09:06:50 UTC | #32

So for now I can prototype:
- serialize attribute of any type, using compile time information.
- animate attribute value, using compile time information.

-------------------------

Eugene | 2017-08-25 09:11:49 UTC | #33

> AttributeAnimationInfo should be templated to animate T and use
ApplyValue(const T& newValue). The question is what else needs to be refactored

It will give you exactly nothing. ValueAnimation is the Resource that stores Variant-s. You will have to cast this variant somehow before applying it to the attribute. Now this cast is performed inisde accessor. If you templatize anything, you will just make the architecture more compliacted and move this cast at the level of AttributeAnimationInfo or ValueAnimationInfo. You will not get _any_ benefit unless you templatize ValueAnimation Resource itself.

> Can you better explain what’s the problem with Cereal’s approach?

Just compare the syntax of Cereal and Urho. I can't imagine how to match it without breaking the API and resource compatibility.

> Again, look at Cereal - much simpler and convenient code usage than Urho’s serialization

And much less powerful.

> If anyone which is familiar with Attribute and/or Attribute animation can give me complete requirements for what they need to technically do (instead of me guessing and missing stuff by looking at code), I could try to prototype a system that uses templates to see if it’s feasible

My current experience tell me that it's _not_ feasible. Of course, you could try. Here are requrements, good luck:

1. Don't break Serializable API, including these macros. Urho and user components shall work without changes.
2. Don't break compatibility of serialized XMLs and Jsons;

I suppose it's ok to break OnSetAttribute hooks (8 Urho components used it). It is smelly hack and have to be removed at some point.

-------------------------

Enhex | 2017-08-25 09:17:51 UTC | #34

backward compatibility isn't a requirement for what the system suppose to do.
I mean things like "be able to add value animations dynamically".

Value animation will require complete rethinking. That's why I suggested earlier to start refactoring from the bottom - so you'll know what you're building on.

-------------------------

cadaver | 2017-08-25 09:28:51 UTC | #35

Did you read the comment?

        // Convenience for editing static constraints: if not connected to another body, adjust world position to match local
        // (when deserializing, the proper other body position will be read after own position, so this calculation is safely
        // overridden and does not accumulate constraint error

It's somewhat of a kludge. Feel free to remove or refactor.

-------------------------

Eugene | 2017-08-25 09:42:14 UTC | #36

[quote="Enhex, post:34, topic:3482"]
backward compatibility isn’t a requirement for what the system suppose to do.
[/quote]

It is a requirement for Urho API (with exceptions listed in poritng notes)

> That’s why I suggested earlier to start refactoring from the bottom - so you’ll know what you’re building on

Refactoring != breaking anything and building from scratch. What's the point of such changes? Especially when benefit is so impalpable. You won't win any FPS. You will win few milliseconds for binary serialization. And you will lose all users, beacuse (I suppose) such PR will never be merged.

Okay, here are functional requirements:

1. Of course, The System shall be able to serialize variant attributes of the object. Either all attributes simultaneously or one-by-one.

2. The System shall store and provide access to attribute information: attribute name, enum names, default values, attribute flags and metadata.

3. The System shall allow to iterate over attributes.

4. The System shall support attributes with custom setters and getters.

5. The System shall support XML, Json and binary formats.

6. The System shall support user-friendly enums for XML and Json.

-------------------------

KonstantTom | 2017-08-25 10:37:43 UTC | #37

Why did you save enum names? I think, enum names can be added as metadata too.

-------------------------

Eugene | 2017-08-25 11:05:04 UTC | #38

Enum names are important for Urho core mechanisms. I don't want to use metadata for obligatory attribute parameters. However, I may change my opinion later...

-------------------------

Enhex | 2017-08-25 12:25:24 UTC | #39

Did some initial prototyping for generic serialization.
Note that it's a simple prototype showing generic serialization(only) implementation, and not drop-in replacement for Urho's attributes.

[Simple introduction example for variadic templates usage](https://wandbox.org/permlink/ib1BFzZ32aGTTWP8).
[Example of generic serialization to file](https://gist.github.com/Enhex/4d42ef13dda1681eaac7ae6ead25669c).

-------------------------

Eugene | 2017-08-25 12:34:24 UTC | #40

Will you try to make your serialization meet at least these weak requirements?

[quote="Eugene, post:36, topic:3482"]
Of course, The System shall be able to serialize variant attributes of the object. Either all attributes simultaneously or one-by-one.

The System shall store and provide access to attribute information: attribute name, enum names, default values, attribute flags and metadata.

The System shall allow to iterate over attributes.

The System shall support attributes with custom setters and getters.
[/quote]

-------------------------

Enhex | 2017-08-25 12:46:45 UTC | #41

[quote="Eugene, post:40, topic:3482"]
serialize variant attributes
[/quote]

That's what we need to fix.

You're confusing serialization and other features related to attributes.
Serialization is just about reading and writing, it isn't responsible all the other things u listed.
Serialization can use setters and getters, you can specialize the type's serialization for input and output, and call set / get in each.

And the core problem is the use of variant, which create limitations that lead to kludges (already explained how).
Naming, default values, etc don't use variant therefore there's no problem to fix here.

There are only 2 things that I know of that use variant - attribute serialization and animation.

-------------------------

Eugene | 2017-08-25 13:11:51 UTC | #42

[quote="Enhex, post:41, topic:3482"]
That’s what we need to fix.
[/quote]

I meant, serialize types supported by variant.

> You’re confusing serialization and other features related to attributes
> Serialization is just about reading and writing, it isn’t responsible all the other things u listed

Urho don't need plain serialization like cereal per se.
Urho need attribute system that allows to treat object as group of named and parameterized attributes.
Serialization is just an usage of this attribute system.
Have you tried to prototype such attribute system without Variant? It's hard for me to even imagine it.

-------------------------

Enhex | 2017-08-25 13:34:12 UTC | #43

[quote="Eugene, post:42, topic:3482"]
I meant, serialize types supported by variant.
[/quote]
It's trivial.
First of all in the example I automatically generate serialization for arithmetic types, that includes all the kinds of integers and floats.
I updated the example with a Vector3 class. Serializing it is this simple:
```C++
template<typename Stream>
void serialize(Stream& f, Vector3& value) {
	read_or_write(f, value);
}
```

We don't need to completely replace all of Urho's attributes system. Just get rid of the use of variant where it causes limitations and can be replaced with a better solution.

-------------------------

Eugene | 2017-08-25 13:42:01 UTC | #44

[quote="Enhex, post:43, topic:3482"]
Just get rid of the use of variant where it causes limitations and can be replaced with a better solution
[/quote]

Variant is the basement of Urho attributes. How do you replace it with templates?

-------------------------

cadaver | 2017-08-25 14:08:14 UTC | #45

In the Tundra project we had attributes with templates / subclasses.

https://github.com/realXtend/tundra-urho3d/blob/master/src/TundraCore/Scene/IAttribute.h
https://github.com/realXtend/tundra-urho3d/blob/master/src/TundraCore/Scene/IAttribute.cpp

Not necessarily prettier. Another part of using Variant is that you gain freeform data for scripting.

-------------------------

Enhex | 2017-08-25 14:10:24 UTC | #46

[quote="Eugene, post:44, topic:3482"]
How do you replace it with templates?
[/quote]

- Identify what are the problems Variant is used for.
- Prototype a better solution in isolation so you don't have to deal with external complexity.
- Integrate the better solution to replace the previous solution.

Again, I only came across variant being used for serialization and animation, and in both cases I don't see any necessity to use variant instead of generic templates.
So the next step is to prototype a generic solution for attribute animation. That may be more complicated since animations are dynamically added.

Later on we need to see how they're integrated into Urho - that may lead to more refactoring as other code that interacts with the previous systems uses variant.

-------------------------

Eugene | 2017-08-25 15:09:26 UTC | #47

If we make hierarchy like in Tundra
AttributeInfo <- AttributeInfoImpl<T>

1. AttributeInfo shall have virtual Save/Load XML/JSon/Binary for serialization (PImpl-ed);
2. AttributeInfo shall have virtual SetVariant to work with ValueAnimation resource (just postpone the problem for now);
3. We shall expose all AttributeInfoImpl<T> to AS and update Editor code.

-------------------------

Eugene | 2017-08-26 12:59:07 UTC | #48

Here is one more important change.
I replaced attribute accessor with function pointers and used lambda _for each_ attribute macro.

Pros:

- Removed `AttributeTrait`, `MixedAttributeTrait` and the whole hierarchy of `AttributeAccessor`;
- Removed one virtual call on attribute set/get;
- Things are more generic now, **accessors don't have to match the exact type anymore**
- So, `URHO3D_MIXED_ACCESSOR_ATTRIBUTE` is deprecated (not removed, of course), use `URHO3D_ACCESSOR_ATTRIBUTE` instead.

Cons:

- ??? things have changed, maybe

[quote="Enhex, post:46, topic:3482"]
Later on we need to see how they’re integrated into Urho - that may lead to more refactoring as other code that interacts with the previous systems uses variant.
[/quote]

Getting rid of Variant in attributes will make script API more complicated and cause a lot of work, so I am not going to work on it. Despite the fact that serialization could became faster without Variant casting.
You could try to do it on your own if you have enough passion.

-------------------------

Enhex | 2017-08-26 14:23:07 UTC | #49

[quote="Eugene, post:48, topic:3482"]
I replaced attribute accessor with function pointers
[/quote]

Instead of function pointers you can use template functors. It will allow inlining lambdas and functions. [Example](https://github.com/Enhex/Benchmarks/tree/master/lambda%20std%20function%20vs%20template%20parameter)

[quote="Eugene, post:48, topic:3482"]
Getting rid of Variant in attributes will make script API more complicated
[/quote]
How will it make things more complicated?

-------------------------

Eugene | 2017-08-26 14:45:48 UTC | #50

[quote="Enhex, post:49, topic:3482"]
How will it make things more complicated?
[/quote]

This is just a guess.
Variant is simple. It's plain type, that is easy to pass to function, return from function or facade to script API. Once you replace straightforward value type with virtual hierarchy, it causes wide scale refactoring. Try to get attributes from the Tundra and fit them into Urho-s `ScriptInstance`.

[quote="Enhex, post:49, topic:3482"]
Instead of function pointers you can use template functors
[/quote]
I cannot because AttributeInfo is non-template.

-------------------------

Enhex | 2017-08-26 15:24:59 UTC | #51

It isn't a simple type, it's like a union. You have to manually handle each case for each type.

Why use virtual hierarchy as a replacement?

Of course it would cause wide scale refactoring.
If we can't find a way to fix things without causing performance regression, I suggest dropping this issue for now.
The current attributes system isn't broken. It's better to focus on something else.

-------------------------

Eugene | 2017-08-26 15:47:19 UTC | #53

[quote="Enhex, post:51, topic:3482"]
If we can’t find a way to fix things without causing performance regression, I suggest dropping this issue for now.
[/quote]

Probably I misunderstood something. Where do you see performance regression?

-------------------------

Enhex | 2017-08-26 16:51:39 UTC | #54

earlier you reported your fix reduced performance

-------------------------

Eugene | 2017-08-26 17:07:51 UTC | #55

[quote="Enhex, post:54, topic:3482, full:true"]
earlier you reported your fix reduced performance
[/quote]

My fix is unrelated here.
In release mode accessor attributes are negligibly slower than offset attributes probably due to two extra pointer-to-function calls. Negligibly means that measurement error is greater than the difference.

I can not get the idea of better attribute refactoring out of my head, btw...

-------------------------

weitjong | 2017-08-26 23:56:10 UTC | #56

I have to agree with Enhex on this. If ain't broken then don't fix it. Or perhaps don't do it now until you have more overview or more comfortable with the code base.

At a quick glance on the last commit in the master branch, I don't feel it has went through all the basic use cases yet. I could be wrong though, but it looks like the refactoring work is incomplete as it has only done on those cases where the `Serializable::OnSetAttribute()` are being overridden. Also, it does not feel that right (at least to me) to have so many almost identical accessor methods. It bloats the code base unnecessarily.

I think the last commit should be reverted back first and keep it in a new topic branch. The work can be continued in the branch if there is really such need. And when the whole refactoring is done then a pull request is made to ask the lib users to evaluate, before actually merging. I think Lasse would do it like this for fundamental change.

-------------------------

Eugene | 2017-08-27 00:24:29 UTC | #57

> At a quick glance on the last commit in the master branch, I don’t feel it has went through all the basic use cases yet. I could be wrong though, but it looks like the refactoring work is incomplete as it has only done on those cases where the Serializable::OnSetAttribute() are being overridden.

Commit in the master is not heavily tied to this attribute refactoring, I wanted to do it anyway.
If the Component need an action on attribute set, it shall explicitly state this action.
if-cascades in `OnSetAttribute` are a bit too ugly.
I could (ok, _you could_) revert this commit if you don't like the implementation, but I don't want to keep attribute hooks in `OnSetAttribute`. They looks like they came from the pre-accessor epoch when all logic had to be implemented inside `OnSetAttribute`.

-------------------------

weitjong | 2017-08-27 00:42:34 UTC | #58

I believe all the related commits for a fundamental change should go in together as a whole instead of piecemeal. The last commit appears to be a small part of the whole work to me.

-------------------------

Eugene | 2017-08-27 00:48:40 UTC | #59

Now I have an idea how to get rid of the hooks without such amouth of methods...
I reverted last commit. It was big and unpleasant, I agree.

-------------------------

cadaver | 2017-08-27 10:31:16 UTC | #60

The accessor hooks are / were a tool, because they were available, they got used, for better or worse. Whatever was most convenient. 

In this case the price of removing them is the introduction of (more) functions needed only for the manipulation of attributes. I don't see a way around this, at least immediately. Ideally the attribute accessors would be just the same as the component's public API, but in case of ID attributes and such, it needs those "fictional" functions just for the attributes. A "deeper" solution might transform pointers to / from IDs and resource refs directly.

-------------------------

Eugene | 2017-08-27 10:40:44 UTC | #61

[quote="cadaver, post:60, topic:3482"]
Ideally the attribute accessors would be just the same as the component’s public API
[/quote]

I see one more problem here. Public API do the work immediatelly, but attribute setters postpone heavy actions for ApplyAttributes. E.g. CollisionShape::SetShapeType updates shape and rigid body, but attribute accessor just set the `recreateShape_ = true` flag. This is also dirty: two separate mechanisms of doing the same work.

[quote="cadaver, post:60, topic:3482"]
I don’t see a way around this, at least immediately.
[/quote]

For example, the action could be explicitly specified in the attribute declaration. So it would be explicitly stated that attribute A setup cause MarkSomethingDirty, attribute B setup cause MarkSomethingElseDirty and attribute C setup cause ValidateThisThisAndThis.

However, it doesn't fix generic problem with GetSmthAttr+GetSmth pairs.

-------------------------

cadaver | 2017-08-27 12:31:15 UTC | #62

I'm talking idealistically now, so in practice any changes might be unfeasible or cause performance loss, but it seems a bit of an antipattern that there even is a difference between the public API and attribute access, in regard to this "late" setting of heavy state. After all, if you're instantiating something purely in code, you're going to make several public API calls to set the state anyway.

For example collision shape recreation or other heavy operations could be made to happen on demand before next Bullet update if needed, etc. regardless of which route the change was made.

But of course, this is just daydreaming, there's surely a lot of improvements to Urho that could be made that are more important than this.

-------------------------

elix22 | 2017-08-27 12:46:13 UTC | #63

Just my 2 cents
Since you already moved  to C++11.
Take a look at the following:
https://github.com/billyquith/ponder

-------------------------

weitjong | 2017-08-27 13:32:43 UTC | #64

It looks neat but I wonder about its performance. As we all know the reflection approach is usually slower.

-------------------------

Eugene | 2017-08-28 09:25:36 UTC | #65

[quote="cadaver, post:60, topic:3482"]
I don’t see a way around this, at least immediately.
[/quote]

However, there are semi-optimal solutions that both not very heavy and and help to avoid public API bloating.

Getter and setter could be written as lambda function inside RegisterObject even now, but it's not the shortest and the simplest solution.

It migth be better to specify epilogue (post-set) action in the non-accessor attribute declaration. Such changes will require some design effort, but the attributes will be more straightforward than with OnSetAttr hooks. I'll try to implement this.

-------------------------

rku | 2017-10-17 07:50:47 UTC | #66

Someone recently pointed me to awesome lib that may be relevant in this case. Maybe you people should check it out: http://www.rttr.org/

-------------------------

Eugene | 2017-11-11 17:06:04 UTC | #67

I have to go back to this task, so here is new revision.
https://github.com/urho3d/Urho3D/pull/2091
I temporarily added some code in HelloWorld to test things, you could check it for example.

**Important changed:**

- offset_ is removed, all attributes are working via accessors now.

- So, identifying attribute inside OnSetAttribute by offset doesn't work anymore.

- I added `URHO3D_ATTRIBUTE_EX` and `URHO3D_ENUM_ATTRIBUTE_EX` that call specified member function when attribute is set (similar to accessor attributes, but this function doesn't have input arguments). Metadata or attribute name could also be used to identify the attribute, but I decided to avoid this for now. Could be changed.

- I replaced all `URHO3D_*_FREE` functions with `URHO3D_CUSTOM_ATTRIBUTE` and `URHO3D_CUSTOM_ENUM_ATTRIBUTE` that work with any getter/setter functional objects. Note that these new functions works with Variant type due to performance reasons. Could be changed later.

**Benefits:**

- No UB in attributes anymore!

- No extra calls (or even less calls) comparing to old version. Every attribute is set or get via the following chain of calls: `AttributeAccessor::Set(virtual)->[internal lambda](probably inline)->member access or setter/getter call`

- No extra memory allocation even for lambda getters/setters

- No extra copying. Attribute actions are performed directly with Variant came from Serializable code.

- Exact type matching is not required anymore. It's enough for member attribure to be _convertible_ to corresponding Variant type. Same for getters and setters, no need in mixed accessors anymore.

- No more tons of accessors and traits. Compiler resolves all type stuff on its own.

- Any lambda could be passed as attribute accessors. Note: this lambda should work with Variant directly.

- Attribute with explicit post-set action is more straightforward than custom logic in OnSetAttribute.

**Disadvantages:**

- Old offset-based attribute identifying doesn't work anymore.

- Old type hacks like for Light cascade splits don't work enymore.

- Someone may dislike macro magic used to make lambdas. Probably will change it a bit...

- Attribute identifying may be considered less readable. Feel free to discuss.

-------------------------

