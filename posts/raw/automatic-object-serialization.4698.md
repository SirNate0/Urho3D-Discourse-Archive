rku | 2018-11-27 15:50:16 UTC | #1

We discussed this briefly with @Eugene

A very cool feature would be automatic serialization of attributes that point to `Serializable` or it's subclass.

My proposed implementation of this is to have `Serializer` track serialization of objects by their pointer. Object would be serialized when it is encountered for the first time. If any other objects reference same object - a reference entry should be serialized instead.
Deserialization would happen in similar manner: deserialized objects are put to the map and pointer is served from the map when object reference entry is encountered.

Caveats:
* A bit of extra state is added to `Serializer` and `Deserializer`. Not perfect, but on the other hand `Deserializer` already has some state.
* Attributes may store any instance of `RefCounted` while we can serialize only instances of `Serializable`.
* Proposed scheme gets in a way of parallel (de)serialization. On the other hand engine does not do any of that.

If implemented, this would give us automagic serialization of objects referenced engine attributes. Even circular references would work. Imagine that - entire game state could be saved/loaded in one swoop with a bit of care.

What are your thoughts? Maybe anyone has a better idea how this could be implemented? or maybe we do not want this at all?

-------------------------

rku | 2019-01-13 08:10:04 UTC | #2

Looks like noone cares. Sigh.

In the meantime i implemented proof of concept serialization using [cereal](http://uscilab.github.io/cereal/) library.

To my surprise API is pretty non-invasive.
```cpp
    /// Load from binary data. Return true if successful.
    bool Load(Deserializer& source, SerializationFormat format);
    /// Save as binary data. Return true if successful.
    bool Save(Serializer& dest, SerializationFormat format) const;
```
These serialize object to binary/xml/json. You probably noticed that they are not virtual. This is because user is supposed to implement a single `template<typename Archive> void serialize(Archive& ar, uint32_t version)` for both serialization and deserialization. Down to one function from six, quite an upgrade i would say. This function can also be hidden from public API *i think*, but `cereal` would still be required to be included in SDK as user would have to interact with it if user decided to serialize extra stuff that is not registered as attributes.

Binary output format is ok. It suffers from same issues like current urho's one, which is not saving attribute names and being dependent on serialization order. On the other hand `serialize()` function has a `version` variable which can be used to make code support both older and newer versions, so if you use binary serialization for save files - new game versions could support older saves.

JSON and XML serialization is a considerable downgrade from aesthetic point of view.
```json
{
    "value0": {
        "cereal_class_version": 1,
        "Integer Foo": {
            "value0": 1234
        }
    }
}
```
```xml
<?xml version="1.0" encoding="utf-8"?>
<root>
	<value0>
		<cereal_class_version>1</cereal_class_version>
		<Integer_Foo>
			<value0>123</value0>
		</Integer_Foo>
	</value0>
</root>
```
Maybe `cereal` could be patched to produce a bit more user-friendly output.

Things to be explored:
* Inheritance. `cereal` supports that.
* Serialization of `Serializable` instances. Pretty confident that can be pulled off. `cereal` already supports serializing instances and saves them only once even if multiple objects reference same thing.

-------------------------

Modanung | 2019-01-13 10:11:55 UTC | #3

[quote="rku, post:2, topic:4698"]
Looks like noone cares. Sigh.
[/quote]

I care about Urho without having something useful to say about each of its workings. Your proposal sounds nice and more efficient, but I must admit the exact technicalities are a bit over my head. The same may be true for many others.

Sometimes its the least appreciated efforts which bear most value. :slightly_smiling_face:

-------------------------

JTippetts | 2019-01-13 17:06:14 UTC | #4

I'm in the same boat as @Modanung here. I care about Urho3D, and if something makes it better I'm all for it, but serialization isn't something that I think about (or even use, for that matter) all that often, so I'm not likely to pipe up about it.

-------------------------

Leith | 2019-01-14 06:04:37 UTC | #5

I care about serialization.
In fact, I believe I just fixed a bug in networked scene replication.

Serializing matters, but we should observe, there are several kinds of serializing!
We may serialize to, and from, the following: memory, network, and disk.

I don't understand the engine well enough to comment further, but the point is,
it depends on your application, and the context, what we serialize, how we serialize it,
and how we reconstruct it later! Serialization is possibly one of the most complex subjects
that we could talk about - how does it serialize across platforms? What about Endian issues?
There is a lot of things to talk about with respect to serializing, and getting it right is very cool.

-------------------------

rku | 2019-01-14 10:06:59 UTC | #6

[quote="Leith, post:5, topic:4698"]
how does it serialize across platforms?
[/quote]

Automagically ;)

[quote="Leith, post:5, topic:4698"]
What about Endian issues?
[/quote]

Cereal provides a separate portable binary archive serializer which takes care of that. Most of the time we dont care though. Even current urho serializer does not.


And a small update on progress:
```cpp
class CerealTest : public Serializable
{
    URHO3D_OBJECT(CerealTest, Serializable);
    virtual void Serialize(::cereal::BinaryInputArchive& ar) { ar(*this); }
    virtual void Serialize(::cereal::BinaryOutputArchive& ar) { ar(*this); }
    virtual void Serialize(::cereal::PortableBinaryInputArchive& ar) { ar(*this); }
    virtual void Serialize(::cereal::PortableBinaryOutputArchive& ar) { ar(*this); }
    virtual void Serialize(::cereal::XMLInputArchive& ar) { ar(*this); }
    virtual void Serialize(::cereal::XMLOutputArchive& ar) { ar(*this); }
    virtual void Serialize(::cereal::JSONInputArchive& ar) { ar(*this); }
    virtual void Serialize(::cereal::JSONOutputArchive& ar) { ar(*this); }

public:
    explicit CerealTest(Context* context) : Serializable(context)
    {
    }

    static void RegisterObject(Context* context)
    {
        context->RegisterFactory<CerealTest>();
        URHO3D_ATTRIBUTE("Integer Foo", int, foo_, 0, AM_DEFAULT);
    }

    template<typename Archive>
    void serialize(Archive& ar)
    {
        ar(::cereal::make_nvp(BaseClassName::GetTypeNameStatic().CString(), cereal::base_class<BaseClassName>(this))
            ,CEREAL_NVP(hash_)
            ,CEREAL_NVP(vector2_)
        );
    }

    int foo_ = 0;
    Vector2 vector2_{12, 34};
    StringHash hash_;
};
```
Produces:
```xml
<?xml version="1.0" encoding="utf-8"?>
<root>
	<value>
		<value name="Serializable">
			<value name="Integer Foo">123</value>
		</value>
		<value name="hash_">555</value>
		<value name="vector2_">12 34</value>
	</value>
</root>
```
```json
[
    {
        "Serializable": {
            "Integer Foo": 1234
        },
        "hash_": 555,
        "vector2_": [
            12.0,
            34.0
        ]
    }
]
```

XML output required some modifications to cereal, but they are pretty minor. Overall i am pretty happy with output. There are a few things to note.

Cereal has support for polymorphic types. Problem with that is that it requires extra macro to be used at global scope. This example would have required following:
```cpp
CEREAL_REGISTER_TYPE(CerealTest);
CEREAL_REGISTER_POLYMORPHIC_RELATION(CerealTest::BaseClassName, CerealTest)
```
This sucks as it is extra bookkeeping user must not forget about. Besides we already have this information recorded using `URHO3D_OBJECT()` macro. Those macros are also used to enable cereal to serialize object from most derived to the base. I could not get that part working however, so as a workaround i added bunch of `virtual void Serialize()` that call a correct templated serialization function variant. At least these can be hidden behind `URHO3D_OBJECT()` macro if need be.

Lets look at actual serialization function:
```cpp
    template<typename Archive>
    void serialize(Archive& ar)
    {
        ar(::cereal::make_nvp(BaseClassName::GetTypeNameStatic().CString(), cereal::base_class<BaseClassName>(this))
            ,CEREAL_NVP(hash_)
            ,CEREAL_NVP(vector2_)
        );
    }
```
Single function handles serialization *and* deserialization to any number of supported formats. I am still stunned about this ;) `make_nvp()` (stands for "make name-value-pair") for serialization of base class is not strictly necessary, but it makes output nicer. One thing you may find confusing is that `Integer Foo` attribute is registered to `CerealTest` class, but it is serialized as part of `Serializable` class. This is because `Serializable` class manages all attributes. This could probably be solved though.

As you see `StrignHash` and `Vector2` types are serialized transparently to the user as well. Their values in XML and JSON look user-friendly, but it comes at a cost of implementing serialization a little bit differently for every format.
```cpp

// Vector2
template <class Archive> inline
void CEREAL_SAVE_FUNCTION_NAME(Archive& ar, const Urho3D::Vector2& value)
{
    if (std::is_same<Archive, JSONInputArchive>::value || std::is_same<Archive, JSONOutputArchive>::value)
    {
        size_type size = 2;
        ar(make_size_tag(size));    // Make json use array. Without this output would be {"value0": 12.0, "value1": 34.0}
        ar(value.x_, value.y_);
    }
    else if (std::is_same<Archive, XMLInputArchive>::value || std::is_same<Archive, XMLOutputArchive>::value)
        ar(std::string(value.ToString().CString()));    // Serialize as string to make everything fit into one xml tag.
    else
        ar(value.x_, value.y_);  // Binary archives, at least they are trivial
}

template <class Archive> inline
void CEREAL_LOAD_FUNCTION_NAME(Archive& ar, Urho3D::Vector2& value)
{
    if (std::is_same<Archive, JSONInputArchive>::value || std::is_same<Archive, JSONOutputArchive>::value)
    {
        size_type size = 2;
        ar(make_size_tag(size));
        ar(value.x_, value.y_);
    }
    else if (std::is_same<Archive, XMLInputArchive>::value || std::is_same<Archive, XMLOutputArchive>::value)
    {
        std::string text;
        ar(text);
        value = Urho3D::ToVector2(text.c_str());
    }
    else
        ar(value.x_, value.y_);
}
URHO3D_SERIALIZE_PLAIN(XML, Urho3D::Vector2);  // Hint cereal that this type is simple enough that it does not need multi-level xml tree.
```

For time being i removed versioning. This matter still needs some thought. Object version has has also to be declared with a macro `CEREAL_CLASS_VERSION(Type, Version)` at global scope. Maybe versioning could be achieved by defining `using Version = 1;` in the class and have cereal use that automatically if it is present.

---

Conclusion: current implementation is very early WIP, but it holds promise to satisfy all requirements. Implementation that is on par with current features is possible now (although file formats would change). More concerning part is support for polymorphism, so we could also serialize any subclasses of `Serializable` stored in shared pointers and have them restored properly. This would likely require some serious work reimplementing bulk of cereal's features to use metadata defined in `URHO3D_OBJECT()` macro.

-------------------------

Leith | 2019-01-15 01:22:29 UTC | #7

Very nice!
I've just quit playing around with using RTTR to automate angelscript bindings at runtime.
Cereal looks quite tidy!

A few questions though.
#1 - Can it serialize private members?
#2 - Can we tag public members to NOT be serialized?
#3 - How does it serialize object references / deal with circular references? I mean - are referenced objects serialized uniquely, or entirely serialized every time a reference is encountered?

-------------------------

rku | 2019-01-15 07:32:00 UTC | #8

[quote="Leith, post:7, topic:4698"]
I’ve just quit playing around with using RTTR to automate angelscript bindings at runtime.
[/quote]

If you are interested in the topic you should drop by to Urho's gitter chat and talk to @hugoam. He is working on his own [toy](https://github.com/hugoam/toy/) engine which automatic binding at runtime to lua and now javascript.

[quote="Leith, post:7, topic:4698"]
#1 - Can it serialize private members?
[/quote]
Yes! It can serialize anything that serialization function has access to. We can even make serialization function private and still allow cereal to access it through friendling a class.

[quote="Leith, post:7, topic:4698"]
#2 - Can we tag public members to NOT be serialized?
[/quote]

Serialization is not automatic.
```cpp
    template<typename Archive>
    void serialize(Archive& ar)
    {
        ar(::cereal::make_nvp(BaseClassName::GetTypeNameStatic().CString(), cereal::base_class<BaseClassName>(this))
            ,CEREAL_NVP(hash_)
            ,CEREAL_NVP(vector2_)
        );
    }
```
To stop serializing `hash_` you would just remove `,CEREAL_NVP(hash_)` from `ar()` call.

[quote="Leith, post:7, topic:4698"]
#3 - How does it serialize object references / deal with circular references? I mean - are referenced objects serialized uniquely, or entirely serialized every time a reference is encountered?
[/quote]

cereal takes care of that as well. Raw pointers are not serialized, but shared/weak pointers are. Cereal takes care to track references and serialize object only once even if it occurs multiple times during serialization. When deserializing it automatically puts same reference to multiple shared pointers as it was seen during serialization. This part needs some work though, because cereal supports only shared pointers from stdlib.

-------------------------

glitch-method | 2019-08-25 23:54:24 UTC | #9

this is fantastic, thanks! 
i'm just a hobbyist and mostly in over my head around here, but this is sort of important. my project is still in the sketching stages, but it absolutely depends on this kind of data-oriented feature. i had been looking at ASN.1 (+xer/ber) recently with this kind of mechanic in mind.

-------------------------

rku | 2019-08-26 04:18:39 UTC | #10

This won't make into upstream but we made our own solution in rbfx. And uniform serialization is pending. So check it out if that is something you need.

-------------------------

glitch-method | 2019-08-26 04:27:30 UTC | #11

i already expect to follow your fork as well as main for a few reasons. ;p  figured i'd mention though, since the thread didn't get a grand reception.

-------------------------

