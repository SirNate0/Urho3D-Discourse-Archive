Eugene | 2017-07-18 13:16:25 UTC | #1

I suppose that coding conventions shall be updated after C++11 introduction. I'm going to write my proposal and rationale. Please, comment.

- The macro `NULL` or integer constant 0 should not be used for null pointers, `nullptr` is used instead. Replace 0-s in old code. **(VA)**
  - **Why:** Best way to declare null pointer.
- The keyword `override` shall be used wherever possible (_?? except destructors ??_). Update old codebase. **(VA)**
  - **Why:** Prevent errors.
- The keyword `final` shall not be used except rare specific cases (e.g. virtual interface wrapping)
  - **Why:** It makes code reuse hard. Think twice before sealing the interface.
- The `using` shall be used instead of `typedef`. Replace typedefs in old code. **(VA)**
  - **Why:** More readable.
- The `{}` constructor shall never be used.
  - **Why:** Keep code consistent. It gives too few benefit to update the whole codebase.
    - IMO, the = initialization is the most readable.
- The range-based `for` loop shall be used wherever possible. Update old codebase when possible. **(VA)**
  - **Why:** More readable.
- `auto` shall not be used for one-word types and simple templates.
  - **Why:** Keep code readablilty when type name is short enough. Keep code consistent.
- `auto` shall be used for unknown types in templates (avoid `typename` and `decltype`) and long nested types (aka `HashMap<String, int>::KeyValue`). _?? Shall other cases be here ??_ **(VA)**
  - **Why:** Improve code readability when type name gives no information. Check the link for example: https://clang.llvm.org/extra/clang-tidy/checks/modernize-use-auto.html
- Inplace member initialization shall be used wherever possible. Update old codebase.
  - **Why:** Easier to read, harder to mistake.

I've marked with **(VA)** tag items that could be done automatically via Visual Assist.

-------------------------

Modanung | 2017-07-18 09:23:26 UTC | #2

[quote="Eugene, post:45, topic:2790"]
The {} constructor shall never be used.
[/quote]

IMO the `=` is for assignments and `{}` are for initialization, since the latter provides more type safety.
Also the `{}` can both be used in the constructor's head as well as in the body of a function. Adding consistency.

-------------------------

Eugene | 2017-07-18 10:27:39 UTC | #3

That's why I sometimes dislike C++

> Adding consistency

You may notice that items in the list that require updating old codebase are automatized, except inplace member initialization that I am ready to upgrade on my own.

If one is ready to port _all_ Urho codebase to such constructor, it will be consistent. If we just start to use new style, we end up in codestyle mess. Two different styles is always worse than one.

> IMO the = is for assignments and {} are for initialization, since the latter provides more type safety.

That's holywarable whether the type safety costs it.
IMO objective decision isn't posible here

[details=here is my point of view...]
`int some_name = 10;` and `some_name = 10;` have similar meaning and semantics. We assign here some value to some name. Here is very distinguishable `" = "` pattern that is used _only_ for assignments (including construction). The only difference here is that  new name is created in the first case, while old name is used in the second one.

Then...

`int some_name { 10 }` and `some_name = 10` have too different semantic for the similar action. The `" { } "` pattern is much less distinguishable than `" = "` because it's similar to other language constructions.

Choosing between ghost type safety and visual nicety, I prefer the second one
[/details]

-------------------------

Modanung | 2017-07-18 13:22:36 UTC | #4

[details=Consider]
```
Class::Class(),
a{1},
b{2}
{
    const int c{ a + b };
    a = 4;
    b = c;
}
```
[/details]
[details=VS]
```
Class::Class(),
a(1),
b(2)
{
    const int c = a + b;
    a = 4;
    b = c;
}
```
[/details]

-------------------------

Modanung | 2017-07-18 12:58:46 UTC | #5

[quote="Eugene, post:47, topic:2790"]
If we just start to use new style, we end up in codestyle mess. Two different styles is always worse than one.
[/quote]

I'm not suggesting multiple styles. And if you change the rules, past results are bound to break the newly instated ones.

-------------------------

Eugene | 2017-07-18 11:04:41 UTC | #6

>  Consider 1 VS 2

Ok, there is probably not so big difference.
I actually don't care very much. Hidden part was just IMO.

> I'm not suggesting multiple styles.

The only thing I really care about is to have single style in the end.

If you suggest codestyle change that breaks code consistency, be ready to fix unconsistency on your own.

_I am ready to upgrade old codebase on my own for each item in the list above that is broken by existing codebase_

-------------------------

kostik1337 | 2017-07-18 11:45:27 UTC | #7

[quote="Eugene, post:47, topic:2790"]
int some_name = 10; and some_name = 10; have similar meaning
[/quote]

As for me, this is true only for local non-static variables. Static initialization happens while your program is uploading to memory, while local variable initializations means just "put that value into memory on that address in runtime", the same as variable assignment.

So, here I partially agree with Modanung. {} initialization is reasonable for local non-static initialization, but it could be hard to update all codebase with it.

-------------------------

Modanung | 2017-07-18 13:17:51 UTC | #8

[quote="Eugene, post:6, topic:3365"]
Ok, there is probably not so big difference.
[/quote]

Agreed. Still, I would argue the first of the two code examples to be more semantically consistent.

On updating the code base:
The bright side of this is that it's easy to see what part of the engine has been c++11-ified (by hand and eye) and which parts are 'old'.

-------------------------

Enhex | 2017-07-19 14:30:36 UTC | #9

Note: In general you should never say "never use feature `X`", it usually means you just don't know what it's useful for.


0 isn't guaranteed to represent null pointer on all systems (ex. some embedded systems use 0 as valid memory address)


regarding `override` I want to mention useful use case:
when declaring a virtual function in a base class, it's already[ implicitly declared virtual](http://en.cppreference.com/w/cpp/language/virtual#In_detail) in derived classes, so writing virtual for derived class functions which is completely redundant, and can lead to bugs - ex. if the base class renames the virtual function, the derived class will still use virtual function when it isn't needed, degrading performance.
`override` becomes handy with virtual functions when you want to make sure you're overriding the base class's virtual function.
```C++
struct A {
    virtual f();
}

struct B : A {
    virtual f();
}
```
Should be replaced with:

```C++
struct A {
    virtual f();
}

struct B : A {
    f() override; //already implicitly virtual
}
```
Urho does use `virtual` for derived class functions (ex. SoundSource3D::Update)


`using` can be templated ([alias template](http://en.cppreference.com/w/cpp/language/type_alias)), typedef cant.
typedef is obsolete.

list initialization (`{}`) is very handy and has useful use cases. examples:
```C++
void f(Vector3 x) {
//...
}
f(Vector3(1,2,3)); // without list initialization
f({1,2,3}) // with list initialization

// without list initialization
vector<int> v;
v.emplace_back(1);
v.emplace_back(2);
//...

// with list initialization
vector<int> v{1, 2,/*...*/};
```

-------------------------

Eugene | 2017-07-19 14:51:18 UTC | #10

[quote="Enhex, post:9, topic:3365"]
0 isn’t guaranteed to represent null pointer on all systems (ex. some embedded systems use 0 as valid memory address)
[/quote]
How this is related to `nullptr` codestyle proposal?

[quote="Enhex, post:9, topic:3365"]
Should be replaced with
[/quote]
I definetely dislike implicit virtuals because leading keyword `virtual` is much noticeable than trailing `override`, maybe because of alignment.
C++ would be much better if `override` and `final` were used _instead_ of `virtual` in the beginning.
This is impossible, so I'd like to avoid implicit virtual at all.

[quote="Enhex, post:9, topic:3365"]
list initialization ({}) is very handy and has useful use cases
[/quote]
I completely agree here, but I don't want to end up with mixed ctors styles. If one write a script for automatic upgrade, it wold be great.

_TODO: Update proposal somehow_

-------------------------

Enhex | 2017-07-19 15:18:56 UTC | #11

[quote="Eugene, post:10, topic:3365"]
How this is related to nullptr codestyle proposal?
[/quote]

Just showing how NULL defines are less correct.


You can have a derived class that defines a new virtual function (not override).
You can override non-virtual function.
(point is that you need `virtual`)

technically list initialization isn't exactly the same as using regular constructor syntax since it can be overloaded, so it isn't just style. example:
```C++
std::vector v(2);
// not the same as:
std::vector v{2};
```
Regular constructors and list initialization have different use cases. Use whichever is better for your case.

-------------------------

Eugene | 2017-07-19 15:56:57 UTC | #12

[quote="Enhex, post:11, topic:3365"]
technically list initialization isn’t exactly the same as using regular constructor syntax since it can be overloaded, so it isn’t just style.
[/quote]

Huh, I've completely forgotten about this case...

My initial proposal was to use `Class object(params);` for constructors and `Class object = anotherObject;` for copy constructors for consistency with old code.

Then, brace constructor _can_ be used to avoid writing class name at all, e.g. `SetPosition({ 1, 2, 3 });`. I haven't thought about this case at all...

Then, I prefer `vector<int> v = {1, 2, 3};` over `vector<int> v{1, 2, 3};` because it make construction and initialization with elements sematically different.

-------------------------

theak472009 | 2017-07-20 07:33:30 UTC | #13

The beauty of Urho3D is it compiles on all platforms. Please don't spoil it by adding C++11 filth. This is why we have our own containers and pointers and memory management.

-------------------------

Eugene | 2017-07-20 08:38:56 UTC | #14

> The beauty of Urho3D is it compiles on all platforms

How does migration to C++11 breaks "all platforms" compilation? I think that there are C++11-compatible compilers for any more or less modern platform.

> Please don’t spoil it by adding C++11 filth

Urho 1.7 will stay C++98 compatible forever.
Why do you want to use 20-years-old language with its unsafeties and limitations when we can drop'em with zero cost?

Do you know that now _Urho heavily rely on undefined behavior_?
We just hope that these hacks won't suddenly explode sometimes and somewhere.
And this can be fixed only with power of C++11.

-------------------------

yushli1 | 2017-07-20 09:08:04 UTC | #15

I am all for moving to C++11. Just please keep the Urho Variant, Containers and pointers and memory management. It is simple and powerful and easy to understand.

-------------------------

Eugene | 2017-07-20 09:33:55 UTC | #16

[quote="yushli1, post:15, topic:3365"]
Just please keep the Urho Variant, Containers and pointers and memory management. It is simple and powerful and easy to understand.
[/quote]

Don't worry, nobody is goind to break old functionality.

However, I have some ideas about Urho.Container, Variant and Serializable :upside_down_face:

-------------------------

Alex-Doc | 2017-07-20 10:44:19 UTC | #17

[quote="Eugene, post:14, topic:3365"]
Urho heavily rely on undefined behavior?
[/quote]
This sounds pretty scary: Can you please provide an example and eventually how would C++11 features help?

-------------------------

Eugene | 2017-07-20 11:14:32 UTC | #18

[quote="Alex-Doc, post:17, topic:3365"]
This sounds pretty scary: Can you please provide an example and eventually how would C++11 features help?
[/quote]
I know only one place. `URHO3D_ATTRIBUTE` uses `offsetof` for non-POD types, this may accidently explode if use multiple inheritance with serializables. I'm going to use lambdas+function accessors here and retire "offset" attributes completely.

Variant is also pretty scary but probably not UB. I'll try to rewrite it using C++11 non-pod unions.

-------------------------

theak472009 | 2017-07-21 05:11:57 UTC | #19

The goal is to keep the engine code consistent. Either you completely switch to C++11 or you dont. Usually having two code styles in the same project will make a mess. And we all know that STL is the worst possible thing for games. So I assume you wont be using STL code in the engine. So that makes it pointless to port the engine to use C++11. These are just my thoughts :smile:

-------------------------

Eugene | 2017-07-21 05:51:37 UTC | #20

[quote="theak472009, post:19, topic:3365"]
The goal is to keep the engine code consistent.
[/quote]

Then, my goal is the same. This topic was created because of that concern.

[quote="theak472009, post:19, topic:3365"]
So I assume you wont be using STL code in the engine. So that makes it pointless to port the engine to use C++11.
[/quote]
I don't really understand how the second sentence is derived from the first one.
I am goind to use C++11 but I am not goind to use STL.

-------------------------

S.L.C | 2017-07-22 15:58:08 UTC | #21

STL uses exceptions Urho does not AFAIK. STL has quirks between compilers AFAIK. Therefore discarding STL is understandable in the context of this engine.

VS is likely to play an important role in these decisions.

-------------------------

slapin | 2017-07-24 01:44:52 UTC | #22

what is wrong with NULL?

-------------------------

jmiller | 2017-07-24 06:43:42 UTC | #23

My comments? I think most of my concerns have been addressed. I follow the OP's conventions already in my own code. :wink:

[quote="slapin, post:22, topic:3365, full:true"]
what is wrong with NULL?
[/quote]
 https://stackoverflow.com/questions/1282295/what-exactly-is-nullptr

-------------------------

slapin | 2017-07-25 06:38:05 UTC | #24

Ah, I don't see a point having another synonym for 0. NULL was fine all these years until some hype folk came
raging for changes (looks like somebody was drowning in boredom).

Anyway myself I prefer to avoid using strange C++ stuff as much as possible just having C with classes
so to not diverge too far out of comfort zone. But this is personal preference.

-------------------------

Eugene | 2017-07-25 08:39:46 UTC | #25

[quote="slapin, post:24, topic:3365"]
NULL was fine all these years
[/quote]
Yeah, NULL is fine... except:
1) It's ugly uppercase macro, the only uppercase macro in the whole C++;
2) It doesn't have its own type so you can't make your smart handle or pointer `nullptr`-constructible.

So, there is no reason to use NULL when there is better counterpart.

-------------------------

slapin | 2017-07-25 08:56:33 UTC | #26

Well, I can't find these cases anything but nitpicking.
By canon one uses macros as uppercase. This is not ugly, it just says it is macro.
You also generally use uppercase for enum constants. This is just taste. Bad taste (IMHO).
I wonder why you want to construct nullptr - there is .bss for that. For smart handle you use normal pointers,
as there is no reason for smart handle to be working on NULLs. Also nullptr will not do anything more than NULL, as nullptr_t is equivalent of void* as it is compatible with all pointer types and bool.
So it is just another syntax sugar for hipsters, thats all.

-------------------------

Eugene | 2017-07-25 09:15:08 UTC | #27

> This is not ugly, it just says it is macro.

I don't say that uppercase macros are ugly. Actually, non-uppercase marcros are ugly...
I say that null pointer constant defined as `#define NULL 0` is ugly.

> For smart handle you use normal pointers,
as there is no reason for smart handle to be working on NULLs

What if I don't want implicit handle construction from pointer?
You actually **cannot** write nice smart handle without nullptr or your own custom null.

> Well, I can’t find these cases anything but nitpicking.

Let's imagine some abstract situation...

There is the Tool A and Tool B that help you reach your goal. Tool B has disadvantages comparing to the Tool A and you can switch from Tool B to Tool A with zero effort. What will you do?

-------------------------

S.L.C | 2017-07-25 12:23:10 UTC | #28

You clearly haven't played with templates and overloading to realize the usefulness of nullptr. Therefore, your opinion about it is equal to that of a virgin about s3x life. No offence.

-------------------------

slapin | 2017-07-25 17:30:39 UTC | #29

Heh, no, I actually did have extensive C++ learning. I just don't like many of these things as they
tend to make code less manageable in the long run, so need to be limited.

-------------------------

slapin | 2017-07-25 17:40:04 UTC | #30

Well, my analogy is - there is good known tool used for ages. Somebody came with
new tool which is completely different, but without any visible advantage. Everyone around cries
"drop old toys they are obsolete, use new ones!" but nobody provides any real example of
the advantage. I know some people tend to use abstractions just for abstractions, this is nice thing for them,
otherwise I don't see any reason to use new thing until it is proven better.

btw, through ages I seen NULL defined in the following ways:
```c++
#define ((void *) 0) NULL
const void * NULL = 0;
```

But never seen ```#define NULL 0``` - it looks really dangerous. As C++ probably allows assigning 0
as value to any pointer it is generally not C thing.

-------------------------

1vanK | 2017-07-25 18:00:08 UTC | #31

[quote="slapin, post:30, topic:3365"]
But never seen #define NULL 0 - it looks really dangerous. As C++ probably allows assigning 0

as value to any pointer it is generally not C thing.
[/quote]

WinDef.h

(+20 characters)

-------------------------

Eugene | 2017-07-25 18:13:28 UTC | #32

> Somebody came with new tool which is completely different

The only difference is to change old typing habit and do Ctrl+H NULL->nullptr once.

> but nobody provides any real example of the advantage.

Actually, I provided above. NULL is a kind of cripple.

> But never seen #define NULL 0 - it looks really dangerous

This is required by the standard.
http://en.cppreference.com/w/cpp/types/NULL
https://ideone.com/hbXK1i

-------------------------

slapin | 2017-07-25 21:01:18 UTC | #33

I wonder since when (void *) type became prohibited in C++ since 25 years ago when I learned C++
it was always (void *) 0. Anyway I rarely use C++ in practice (basically only with Urho) so I might
miss some C++ stuff (I work almost solely with C, with some use of Python and Lua, with very primitive knowledge in Java, only about running native code in Android and server Java). Is there any official rationale to this change?

-------------------------

Eugene | 2017-07-25 21:47:53 UTC | #34

[quote="slapin, post:33, topic:3365"]
Is there any official rationale to this change?
[/quote]

In C you can implicitly cast any pointer to any, in C++ you cannot.
So, in C you can define NULL as (void*)0 and intialize any pointer with it. In C++ you cannot.

-------------------------

slapin | 2017-07-25 22:19:08 UTC | #35

I see, but is there any public discussion regarding this? I used to the times before <stddef> and <cstdio>,
when one used <stddef.h> and <stdio.h> with C++, so used #define NULL ((void *)0)
so it worked fine with C++ at some stage. Also in C you can't implicitly convert pointers,
void * type is special "any" pointer type. BTW same thing still works with C++ for void * notation
(at least with gcc).

-------------------------

jmiller | 2017-07-26 01:02:14 UTC | #36

There's always a lot of discussion about features of ISO standards like C++.

 https://isocpp.org/faq
The ISO C++ FAQ seems relevant here. :)

It's a merger of the FAQs by Marshall Cline and Bjarne Stroustrup, whom I always found a good read: http://www.stroustrup.com/C++11FAQ.html

-------------------------

theak472009 | 2017-07-27 06:44:00 UTC | #37

All talk and no real substance. That is what C++ stands for when it comes to game development. Unless the changes provide real performance gains or improve the engine interface, there is really no point in changing anything.

-------------------------

Eugene | 2017-07-27 07:41:57 UTC | #38

Try different point of view here.

First of all, we _have to_ migrate to C++11, I've explained reasons above.

Then, we actually cannot forbid people to use C++11 features when is simplifies their code. Even now our simple code guidelines are sometimes ignored. It would be impossible to force people write 40-symbols-length type name instead of auto or functor class instead of lambda if it doesn't cause compiler error.

So, the only way here is to specify rules for new standard.

-------------------------

slapin | 2017-07-27 08:30:11 UTC | #39

The guidelines exist not to limit people, but to improve code manageability.
Each language feature used should be questioned in regards of this.
If feature hides code workings and makes managing/debugging hard, the feature should not be used.
The sole thing from C++11 which is really step forward is variadic templates.
Everything else to me looks like pile of BS to make hipsters/newcomers happy.

Don't rush and be practical, and that will not be catastrophic.

-------------------------

Eugene | 2017-07-27 09:22:03 UTC | #40

[quote="slapin, post:39, topic:3365"]
Everything else to me looks like pile of BS to make hipsters/newcomers happy.
[/quote]

It's a king of unlogical to avoid things that make code simpler and safer just because they are new.

> Pointer-to-member-function, NULL and autoinline of member functions is syntax surag from C++98, so let's use it!

> Labmbdas, nullptr and override is syntax surag from C++11, so f~ it, it's piece of bullshit for hipsters!

Wow, such consistent relation to syntax sugar.

-------------------------

slapin | 2017-07-27 09:27:48 UTC | #41

Well, proof by trolling is some kind of proof by intimidation. As the discussion is not constructive
it looks like I don't have to waste any more time.

The only thing I say here is that look how serious people start using C++11 features
and other C++X features - slowly implement one by one for project usefulness.
As features are not yet used in project, they all should be thought over one by one.
Don't rush. That's all from my side.

-------------------------

SirNate0 | 2017-07-28 01:09:27 UTC | #42

What about use of `constexpr`, variadic templates, raw string literals, and user defined literals (e.g. one for `Urho3D::String`)?

-------------------------

theak472009 | 2017-07-28 05:25:37 UTC | #43

If C++11 simplifies code for you, it doesn't mean thats the case for everyone else. For me it actually looks confusing. It might be just me but I prefer simple C style code over any new fancy coding standard. Thats why its still the language used by most developers in the world.
Urho3D currently has that perfect balance of C and uses C++ only where its really necessary (like abstraction of APIs). Why do you want to spoil this perfect harmony XDD? Has the evil C++ committee brain-washed you too?

-------------------------

1vanK | 2017-07-28 07:24:49 UTC | #44

box2D also goes to c++11

-------------------------

Eugene | 2017-07-28 09:44:04 UTC | #45

[quote="SirNate0, post:42, topic:3365, full:true"]
What about use of constexpr, variadic templates, raw string literals, and user defined literals (e.g. one for Urho3D::String)?
[/quote]
I doubt that such features will be frequently used in Urho internals. It could be decided "inplace" when someone deicde to write one more user defined literal for some type.

[quote="slapin, post:41, topic:3365"]
Well, proof by trolling is some kind of proof by intimidation. As the discussion is not constructive
it looks like I don’t have to waste any more time.
[/quote]
It was a kind of, sorry. But this trolling is not _mostly_ trolling.

[quote="theak472009, post:43, topic:3365"]
If C++11 simplifies code for you, it doesn’t mean thats the case for everyone else.
[/quote]
Some features of C++11 are not subjective and actualy close some holes in the original. If C++98 had such features, everybody would have used them everywhere.

-------------------------

Modanung | 2017-07-28 10:46:18 UTC | #46

[quote="slapin, post:41, topic:3365"]
As the discussion is not constructive it looks like I don’t have to waste any more time.
[/quote]
I feel like you just kicked over a Jenga tower and then walked away claiming it's not a game.

-------------------------

slapin | 2017-07-28 10:50:16 UTC | #47

Nah. I just have nothing more to say in current circumstances, and really are not interested in heated discussion of something I don't want to waste time on (I'd better work on game or do some important stuff).
Making things short - no fun.

-------------------------

slapin | 2017-07-28 11:03:31 UTC | #49

Is there anything new on your game?

-------------------------

Modanung | 2017-07-28 13:29:43 UTC | #50

[quote="slapin, post:49, topic:3365, full:true"]
Is there anything new on your game?
[/quote]

Working on several, mostly graphics lately. But let's try to get back on topic.
luckeyproductions.nl/gifs/WhiteRabbug.gif

-------------------------

Eugene | 2017-08-21 19:35:00 UTC | #51

I made a PR. This is the last chance to say if someone want to.
https://github.com/urho3d/Urho3D/pull/2088

-------------------------

1vanK | 2017-08-21 19:39:34 UTC | #52

I think Cadaver should decide on the style of the code. We can only offer ideas.

-------------------------

Eugene | 2017-08-21 19:52:10 UTC | #53

So, this PR is mostly for cadaver as he didn't participate in the discussion.

-------------------------

1vanK | 2017-08-21 19:55:42 UTC | #54

Hm, everyone should do PR with their own varioant?

-------------------------

Eugene | 2017-08-21 20:12:33 UTC | #55

I have no idea. Let's write thoughts in that PR for now.

-------------------------

Enhex | 2017-08-21 20:16:12 UTC | #56

Write code instead of guidelines :sleepy:

-------------------------

Eugene | 2017-08-21 21:15:32 UTC | #57

My work project is ugly 25-years-old multi-layered chimera. Codestyles are mixed and merged like tree rings. They have just written code instead of guidelines. This is so fuckin' ugly. I don't want such future for the Urho.

-------------------------

Enhex | 2017-08-21 21:44:00 UTC | #58

Urho isn't your work project neither heading in that direction, quite the opposite.

If you want good guidelines u can use [C++ Core Guidelines](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md). It's already a very well made and detailed document, with a ton of contributors.

You can submit refactoring PRs. There's a lot of work that can be done to modernize Urho and make the code simpler and more concise. I believe that 1000's of lines can be removed with simple straight forward modernization.

Would be interesting if someone could run Clang Tidy on Urho. Last time I tried using Linux virtual machine didn't play well with OpenGL support, and getting Tidy to work on windows was a PITA because CMake only supports generating compile commands for Makefiles/ninja.
 ([Premake got a user module that can export with any generator](https://github.com/tarruda/premake-export-compile-commands))

-------------------------

Eugene | 2017-08-21 21:52:58 UTC | #59

[quote="Enhex, post:58, topic:3365"]
If you want good guidelines u can use C++ Core Guidelines. It’s already a very well made and detailed document, with a ton of contributors.
[/quote]

I agree. This is good guideline. But...

For example, `enum class` is better than old `enum` (of course). How to start using `enum class` in Urho? Any practical ideas?

-------------------------

Enhex | 2017-08-21 22:11:38 UTC | #60

From my experience enum class is kinda tricky because there are no implicit conversions - for example using it for indexing arrays isn't straight forward.
IIRC I also had issues with AngelScript only working with default type enums.

There are other obvious things we can start working on right now.
For example Urho added MakeUnique/MakeShared - we can reduce the usage of "new" for better memory safety.
We can use [default member initialization](http://en.cppreference.com/w/cpp/language/data_members#Member_initialization) and [inheriting constructors](http://en.cppreference.com/w/cpp/language/using_declaration#Inheriting_constructors) to eliminate **tons** of redundant code.
Moderate usage of auto where the type is already explicit such as `GetSubsystem<T>()`.
And so on...

-------------------------

Eugene | 2017-08-21 22:33:43 UTC | #61

[quote="Enhex, post:60, topic:3365"]
For example Urho added MakeUnique/MakeShared - we can reduce the usage of “new” for better memory safety.
[/quote]
I made first step of this refactoring and it took some time. It would be time-consuming to get rid of all new/delete ops.

[quote="Enhex, post:60, topic:3365"]
We can use default member initialization and inheriting constructors to eliminate tons of redundant code.
[/quote]
Things like default member initialization, inheriting constructors, lambdas, variadics and so on are unconditionally useful and straightforward, so I didn't even mentioned them in the guideline. These things just shall be used as soon as they needed.

I want to make guideline for things that could be done in the multiple different ways. A kind of checklist for contributors.
It will be a bit too ugly if one write `auto width = 10` and another `int width = 10`, `0` and `nullptr`, `using` and `typedef` and so on...

[quote="Enhex, post:60, topic:3365"]
Moderate usage of auto where the type is already explicit such as GetSubsystem&lt;T&gt;()
[/quote]
I admit that such usage of auto is perfectly readable too, even if I am not used to write in this way.

-------------------------

johnnycable | 2017-08-22 10:20:21 UTC | #62

I see much arguing about this topic. As usual. Anyway, it looks like unopinionated reference for such c++ things is, nowadays, the [google c++ style guide](https://google.github.io/styleguide/cppguide.html).
That's true; just google for it... :wink:

-------------------------

Eugene | 2017-08-22 10:46:28 UTC | #63

The idea of this thread and my PR is not to re-invent code standard or write my own guidelines. I want to make small and sufficient checklist for contributors basing on Urho legacy and C++ best practices.

I have read both google standard and GSL core guidelines long time ago, BTW.

-------------------------

