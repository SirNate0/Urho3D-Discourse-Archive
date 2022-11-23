1vanK | 2018-06-04 19:10:45 UTC | #1

What about using enum class instead identifiers in global namespace

Old:
```
enum MouseMode
{
    MM_ABSOLUTE = 0,
    MM_RELATIVE,
    MM_WRAP,
    MM_FREE,
    MM_INVALID
};

input->SetMouseMode(MM_FREE);
```

New:
```
enum class MouseMode
{
    Absolute = 0,
    Relative,
    Wrap,
    Free,
    Invalid
};

input->SetMouseMode(MouseMode::Free);
```

-------------------------

Eugene | 2018-06-04 19:35:45 UTC | #2

It was my deep hidden dream, to replace all enums in Urho. 
Impossible w/o breaking a lot of legacy things. Even replacement within the engine would be painful. If only we have automatic tool...
It could be just some python script or native tool tho. Just find and replace fixed list of entries.

Hmmm, maybe even header with defines.... I’ve just started to like this idea.

-------------------------

S.L.C | 2018-06-05 10:17:26 UTC | #3

It starts to get nasty when you convert to and from their fundamental type. You need explicit cast everywhere. They're not called strongly typed enums for nothing.

And a bunch of code still relies on behavior similar to old enums.

What you're seeking is closer to being called scoped enums. Which can be achieved with empty enums inside structs/namespaces. Or even constexpr variables at the cost of loosing warnings about unhandled enumerations in switch cases.

Either way,  code doesn't get prettier with strongly typed enums. I can tell you that.

-------------------------

rku | 2018-06-06 07:31:15 UTC | #4

My secret dream is to actually use enums instead of integer constants to get more type safety. For people with experience this may not be a problem, but for less experienced it is damn confusing when you see function taking int. Good luck guessing where from you should pull that int. The only downside is that enums which serve as flags need extra code to allow painless flag manipulation without extra casts:
```cpp
#define URHO3D_TO_FLAGS_ENUM(t) \
    inline t operator|(t a, t b) { return static_cast<t>(static_cast<size_t>(a) | static_cast<size_t>(b)); }\
    inline t operator|=(t& a, t b) { a = static_cast<t>(static_cast<size_t>(a) | static_cast<size_t>(b)); return a; }\
    inline t operator&(t a, t b) { return static_cast<t>(static_cast<size_t>(a) & static_cast<size_t>(b)); }\
    inline t operator&=(t& a, t b) { a = static_cast<t>(static_cast<size_t>(a) & static_cast<size_t>(b)); return a; }\
    inline t operator^(t a, t b) { return static_cast<t>(static_cast<size_t>(a) ^ static_cast<size_t>(b)); }\
    inline t operator^=(t& a, t b) { a = static_cast<t>(static_cast<size_t>(a) ^ static_cast<size_t>(b)); return a; }\
    inline t operator~(t a) { return static_cast<t>(~static_cast<size_t>(a)); }
```

Edit: By the way this also sucks somewhat because macro has to be used on the enum outside of any namespace in order to allow user code not from `Urho3D` namespace to use these operators.

-------------------------

Eugene | 2018-06-06 08:42:45 UTC | #5

[quote="rku, post:4, topic:4285"]
Edit: By the way this also sucks somewhat because macro has to be used on the enum outside of any namespace in order to allow user code not from `Urho3D` namespace to use these operators.
[/quote]

You know, in my childhood, when I was working on my own game engine...
I was able to write this piece of code:
https://gist.github.com/eugeneko/03defe82d3536ef9cef7121895678950
[damn, I got a stike of nostalgia and probably going looking at my old code]

-------------------------

rku | 2018-06-06 09:36:31 UTC | #6

Yes i am aware of these tricks. Not sure how well they would play with backwards compatibility so not suggesting any of that. What do you thin about this solution? Is it feasible to have it some time?

-------------------------

Eugene | 2018-06-06 09:48:41 UTC | #7

[quote="rku, post:6, topic:4285"]
Not sure how well they would play with backwards compatibility
[/quote]

Just make bunch of `static const MyEnum EN_VALUE = MyEnum::Value` in special header, maybe?

-------------------------

WangKai | 2018-06-06 13:43:10 UTC | #8

This is relatively small comparing to other important things.:smile:

-------------------------

Eugene | 2018-06-06 14:18:44 UTC | #9

True. Let's do Vulkan first.

-------------------------

weitjong | 2018-06-06 14:45:58 UTC | #10

Damn! I need to replace my old GTX 580 soon then. LOL.

-------------------------

rku | 2018-06-06 18:04:05 UTC | #11

Which is more kosher:

In `Urho3D` namespace:
```cpp
enum class DrawableFlags
{
    UNDEFINED = 0x0,
    GEOMETRY = 0x1,
    LIGHT = 0x2,
    ZONE = 0x4,
    GEOMETRY2D = 0x8,
    ANY = 0xff,
};
```

Or in `Drawable` class:
```cpp
enum Flags
{
    UNDEFINED = 0x0,
    GEOMETRY = 0x1,
    LIGHT = 0x2,
    ZONE = 0x4,
    GEOMETRY2D = 0x8,
    ANY = 0xff,
};
```
?

In first case enum would be accessed as `DrawableFlags::ANY` + `FlagSet<DrawableFlags>` and in second case it would be `Drawable::ANY` + `FlagSet<Drawable::Flags>`.

-------------------------

SirNate0 | 2018-06-06 18:46:14 UTC | #12

I would opt for the enum class since so many things inherit from Drawable. Maybe call it DrawableKind, though?

-------------------------

S.L.C | 2018-06-06 20:34:37 UTC | #13

While on the topic of scoping. Is the uppercase necessary? I usually keep it with a capital letter for each word (_including the first one_).

As a bonus, since you can actually forward declare strongly typed enumerations. I'm guessing that would help to avoid including headers unnecessarily.

But still, using this for flags. I can't say I'm very fond of it. Can also be achieved with:

```cpp
struct DrawableKind
{
	enum Type {
		Undefined		= 0x0,
		Geometry		= 0x1,
		Light			= 0x2,
		Zone			= 0x4,
		Geometry2d		= 0x8,
		Any				= 0xff
	};
	// not sure this is necessary
	DrawableKind() = delete;
};
```

-------------------------

rku | 2018-06-07 06:59:43 UTC | #14

`FlagSet<DrawableKind::Type>` feels like overkill :)

Edit:
Actually im thinking maybe best approach for starters would be:
```cpp
enum DrawableFlags
{
    DRAWABLE_UNDEFINED = 0x0,
    DRAWABLE_GEOMETRY = 0x1,
    DRAWABLE_LIGHT = 0x2,
    DRAWABLE_ZONE = 0x4,
    DRAWABLE_GEOMETRY2D = 0x8,
    DRAWABLE_ANY = 0xff,
};
```
This only requires changing parameter types to `FlagSet<...` while any other code does not need modifications. Including user code. This could be a perfect middle ground for backwards compatibility for now.

-------------------------

Eugene | 2018-06-07 08:53:53 UTC | #15

[quote="rku, post:14, topic:4285"]
This only requires changing parameter types to `FlagSet<...`
[/quote]
BTW it's not bad idea even regardless of `enum class`.
Parameters like `unsigned flags` suck.

[quote="rku, post:14, topic:4285"]
Actually im thinking maybe best approach for starters would be:
[/quote]
Actually, `DrawableFlags` are needed only for nice querying.
In real classes only one bit is set.

-------------------------

slapin | 2018-06-09 09:32:40 UTC | #16

From DOD point of view simple enum is superior to enum class.

-------------------------

Eugene | 2018-06-09 09:56:36 UTC | #17

[quote="slapin, post:16, topic:4285, full:true"]
From DOD point of view simple enum is superior to enum class.
[/quote]
Could you explain? I don't get how DOD is ever related to `enum` vs `enum class` choose.

-------------------------

slapin | 2018-06-09 10:01:25 UTC | #18

As I currently being tutored, using class where POD can do same thing is BAD. Don't blame me too much though - I'm still openning amusing world of gamedev and every hour of it is fascinating.

-------------------------

S.L.C | 2018-06-09 10:04:18 UTC | #19

You're not making any sense tho. POD?

-------------------------

slapin | 2018-06-09 10:06:01 UTC | #20

Plain old data. As you probably know, enum is essentially int.

-------------------------

Eugene | 2018-06-09 10:23:54 UTC | #21

[quote="slapin, post:18, topic:4285"]
As I currently being tutored, using class where POD can do same thing is BAD
[/quote]
1. Enum class _is_ POD.
2. Enum class _is **not**_ a class. It's integer.
3. Non-virtual class is just syntax sugar for bunch of variables and free functions so I don't know how it can be "bad" or "good".

-------------------------

S.L.C | 2018-06-09 11:09:07 UTC | #22

I know what POD means. I just didn't knew what POD had to do in the context of strongly typed enums.

As Eugene mentioned. A strongly typed enumeration is whatever integral type you need it to be. And integral types are part of the fundamental types, thus POD types.

For some reason I tend to think that you were under the impression that by adding `class` after the `enum` keyword, the enumeration becomes a non-POD type. And by the way, you can use `struct` instead of `class`. Either works and has the same effect.

-------------------------

slapin | 2018-06-09 11:58:25 UTC | #23

Well, as for 3. it is not so,  as for some of my larger classes splitting them improved performance,
as decreasing amount of conditionals, etc. They say it is to do with caches (they also say you do only algorithmic optimizations and DOD optimizations these days as all the rest are too minor to care).

for 1 and 2 I probably agree but still do not understand why use more verbose syntax for the same thing,
but probably I consider "just because" an answer as I am not of evangelist public and always thought of C as enough and complete and everything else as burden. So I might not be worthy of the answer.

-------------------------

Eugene | 2018-06-09 12:02:22 UTC | #24

[quote="slapin, post:23, topic:4285"]
Well, as for 3. it is not so, as for some of my larger classes splitting them improved performance,
as decreasing amount of conditionals, etc. They say it is to do with caches
[/quote]

If your class is large enough and you have heavy algos that access multiple instances of these classes multiple times, it's true.
In most cases it's not.

[quote="slapin, post:23, topic:4285"]
for 1 and 2 I probably agree but still do not understand why use more verbose syntax for the same thing
[/quote]
Because grouping is better than no grouping.

-------------------------

slapin | 2018-06-09 12:02:54 UTC | #25

I think you're right, I'm just traditionalist C programmer forced to do C++ occasionnaly, so I might be biased there. Also in my environment recent C++ additions are heavily frowned upon, so this might be added to the bias. When I optimized my Urho stuff I got a lot of improvement from using of plain arrays instead of vectors, combining variables together and using small classes, and got about 20% performance boost in world generation algorithms. Because of that I ended up in DOD sect and truly believe in their majic.

-------------------------

slapin | 2018-06-09 12:09:11 UTC | #26

for the case of magic making parts of class into static classes and referencing them by a pointer
heavily increased performance for classes with large amount of short methods.
(as well as converting Component into Subsystem fixed archtecture problem, but that is far fetched too)

I just want to tell there is truth that these things are important. Sorry for diverging the discussion, thank you I always happy to learn new things on these forums through discussions.

-------------------------

slapin | 2018-06-09 12:10:36 UTC | #27

Well about grouping - you can use anonymous and non-anonymous enums and put enums into classes and namespaces, right?

-------------------------

Eugene | 2018-06-09 12:25:40 UTC | #28

[quote="slapin, post:27, topic:4285, full:true"]
Well about grouping - you can use anonymous and non-anonymous enums and put enums into classes and namespaces, right?
[/quote]

AFAIK any solution except `enum class` plus `FlagSet` has its own unsafety and/or ugliness.

If you use `enum` as is, guts are leaking into the outer scope.
If you use scoped `enum` in struct or namespace, you have to write the scope every time you access the enum type.

-------------------------

rku | 2018-06-10 08:28:26 UTC | #29

To be fair `FlagSet` sucks as well. But it is by far best workaround for something that should be core feature of the language.

-------------------------

Eugene | 2018-06-10 08:31:02 UTC | #30

[quote="rku, post:29, topic:4285"]
To be fair `FlagSet` sucks as well.
[/quote]
Y?
I mean, how could it be language feature?

-------------------------

rku | 2018-06-10 08:32:18 UTC | #31

https://msdn.microsoft.com/en-us/library/system.flagsattribute%28v=vs.110%29.aspx

-------------------------

1vanK | 2018-11-18 22:20:21 UTC | #33

> Edit: By the way this also sucks somewhat because macro has to be used on the enum outside of any namespace in order to allow user code not from  `Urho3D`  namespace to use these operators.

hm, it works

```
namespace Opop
{

#define DEFINE_FLAGS_OPERATIONS(enumName, typeName) \
    inline enumName operator | (enumName lhs, enumName rhs) { return (enumName)(static_cast<typeName>(lhs) | static_cast<typeName>(rhs)); } \
    inline enumName& operator |= (enumName& lhs, enumName rhs) { lhs = (enumName)(static_cast<typeName>(lhs) | static_cast<typeName>(rhs)); return lhs; }

enum class Flags : unsigned
{
    A = 1u,
    B = 1u << 1,
    C = 1u << 2
};
DEFINE_FLAGS_OPERATIONS(Flags, unsigned);

}

int main()
{
    Opop::Flags q = Opop::Flags::A | Opop::Flags::B;

    q |= Opop::Flags::C;
}

```

-------------------------

Eugene | 2018-11-19 11:40:11 UTC | #34

Oh, I've just thought about FlagSet. I think that enabler should be removed and macro with global ops like you do should be used instead.

-------------------------

1vanK | 2019-12-19 01:06:57 UTC | #35

 https://github.com//grisumbras/enum-flags

-------------------------

