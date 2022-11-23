Eugene | 2017-04-26 08:42:20 UTC | #1

Inspired by https://github.com/urho3d/Urho3D/pull/1818
Are there any plans to migrate to C++11 and break old compilers support?

Urho doesn't seem to be rapidly developed right now. It may make sense to publish some stable C++98 version and then go to C++11.

-------------------------

cadaver | 2017-02-13 12:23:52 UTC | #2

Apart from JSandusky's upcoming PRs, it's true there's not a lot going on, so yes it sounds like a good idea to push a stable version out in near future.

After that it's fine by me to break old compiler support, at least I test old VS versions very rarely by now.

-------------------------

Eugene | 2017-02-13 13:01:28 UTC | #3

Then I want to raise another question.

C++ has nasty trend to bring style ambigity in new standards. I think that codestyle guidlines have to be updated _and most of new C++11 features shan't be used in Urho core code_.

For example, there are some ambigity in the following cases:

- Variable declaration: explicit-type **vs** auto 
- Type declaration: typedef **vs** using
- Variable initialization: `A a = 10` **vs** `A a(10)` **vs** `A a{10}`
- Member initialization: `: a_(10)` **vs** `a_ = 10` **vs** `a_{10}`

I suggest to _avoid_ in Urho core things like auto, inplace member initialization, curly braces initialization. All `typedef`s are probably may be converted to `using` since it is not hard 'regexpable' change. Also, `nullptr` IMO shall be used instead of pure 0. Some `override`s are also useful.

I suggest it not because I hate C++11, but because I thing that style consistency of Urho costs more than minor benefit from syntax sugar like auto.

-------------------------

1vanK | 2017-02-13 13:08:03 UTC | #4

I like initialisation members in class
```
class A
{
    int b_ = DEFAULT_VALUE;
}
```
This allows not forget initialisation for members (such errors have repeatedly been)

-------------------------

1vanK | 2017-02-13 13:11:06 UTC | #5

auto can be used in iterators i think

-------------------------

Eugene | 2017-02-13 13:17:16 UTC | #6

I like inplace member init too! However, Urho shall IMO use either such notation everywhere or nowhere. So another option is to rewrite class declarations step by step into new style.

> auto can be used in iterators i think

Such exceptions will also lead to inconsistent codestyle.

-------------------------

Enhex | 2017-02-13 20:49:45 UTC | #7

First of all I disagree with the "all or nothing" approach because it usually means not doing anything because it will take huge effort and in the meanwhile you just pile up more legacy code, which makes it a huger effort which means it becomes less likelier, which means more legacy code, recursively, which converges to the "nothing" part of the "all or nothing".

I'm in favor of writing new code in the most optimal way, and going back to refactor old code when revisiting it or when there's nothing better to do.

regarding new C++11 features you mentioned, they aren't a style choice.

**auto**
- removes the need to maintain and refactor code when changing types
- eliminates the possibility of implicit conversion bugs
- less writing. Container iterators are a good example
- more readable. Container iterators are a good example
- easy to use. No need to look up what type is being returned and such

I only know 2 cases when you shouldn't use auto - if you write something like an number type (f.e. auto = 0), in which case the intention behind the value itself is ambiguous (0/0.f/0.0? char/short/int/long?).
Second case is expression templates, in which they return some abstract reference instead of evaluating the expression.

**Alias declarations (using)**
Personally I prefer their syntax because it's similar to variable assignment.
Alias declaration is compatible with templates, so AFAIK it's always better than using typedef so there's no reason to use typedef anymore.
http://stackoverflow.com/questions/10747810/what-is-the-difference-between-typedef-and-using-in-c11

**List initialization**
This one is nuanced, and shouldn't be used everywhere possible.
http://stackoverflow.com/questions/18222926/why-is-list-initialization-using-curly-braces-better-than-the-alternatives

They're usually preferable because they provide better type safety & correctness.
On the other hand you can write a constructor that takes an initializer_list and that means calling class{x,y,z} **_may_** not be the same as class(x,y,z)

Other features that can be useful constexpr, lambdas, unique_ptr, ranged for loops, Expression SFINAE...

BTW, we could use [Clang Tidy](http://clang.llvm.org/extra/clang-tidy/) to automatically refactor things to C++11.
Perhaps it can be used with CI too (?)

-------------------------

1vanK | 2017-02-13 20:50:27 UTC | #8

When auto are everywhere it is very difficult to know what type of returns some functions. Currently I open any file on github and know it without looking function definition

-------------------------

Enhex | 2017-02-13 20:55:14 UTC | #9

In Visual Studio you just have to hover over a variable/function too see a tooltip with the type.
I assume this is a basic IDE feature.

-------------------------

1vanK | 2017-02-13 21:03:34 UTC | #10

Even when I am writing my project in Visual Studio  I am using Alt+F7 in Total Commander for search in engine sources and F3 for looking, so no any tooltip xD

-------------------------

Eugene | 2017-02-13 22:30:35 UTC | #11

[quote="Enhex, post:7, topic:2788"]
First of all I disagree with the "all or nothing" approach because it usually means not doing anything
[/quote]
I mean that there shall be somebody who has enough passion to refactor old codebase step by step to new style. E.g. I prefer inplace initialization and I am ready to periodically migrate old stuff.

> auto

Absence of `auto` was the best thing in Urho codestyle. Yes, I dislike auto.

> removes the need to maintain and refactor code when changing types
> eliminates the possibility of implicit conversion bugs

I have never faced such bugs, so I think they are quite rare. However, I can also imagine bugs that are caused by implicit changing of type of `auto` variable. So it eliminates one kind of bugs and introduce another.

```
String A::foo(); // -> const char* foo()
...
auto a = foo();
if (a == "1") { ... }
```

> less writing. Container iterators are a good example

Of course, impossible to argue. I use auto when WIP or for some simple local projects.

> more readable. Container iterators are a good example- easy to use.

No, no, no, NO. `auto` is more readable for some complex temporary types and _it completely ruins readability in most other cases_. It literally brings strong-typed language into don't-give-a-fuck-about-type script language like python.

- It's harder to explore code via file manager
- It's harder to code via browser
- It's harder to review diff in classical merge tools
- It's harder to review diff in browser
- It's harder to visually check dependencies of some piece of code
- It's harder to determine type usage among codebase
- Search became useless

Programmer saves a minute by writing `auto`. Readers waste an hour/day/??? by reading this mess.
So... Almost-Never-Auto is my choise.
Almost-Always-Auto guys say that reader don't need to know about the type.
I say that if writer is writing code for people, he has no right to decide whether the reader needs type or not.
Almost-Always-Auto guys say that variable name is enough.
I say that type name is a 'part' of variable name and dropping of type is almost like dropping the name.

The worst thing is that experienced developeds have an immunity to such `auto` disadvantages because they are familiar with codebase and they really don't need explicit type. Problems started to appear as time passes, old developers forget codebase and new developers come.

In such big project as Urho, usage of auto IMO shall be strictly limited. Otherwise, its currently perfect readability will be partially destroyed.

> This one is nuanced, and shouldn't be used everywhere possible.

It is just almost unneeded. So I see no reason to bring inconsistency to codebase.

Huh, I finihed.

-------------------------

Enhex | 2017-02-14 00:04:21 UTC | #12

I encountered bugs that auto would avoid, implicit conversions.
Your auto "bug" example is wrong, it just shows you don't understand what auto is. if you don't want to use the type foo returns you shouldn't use auto.

auto doesn't disable strong typing, I'm not sure if you know what that means.
It isn't dynamic typing, you can't change the type of a variable defined with auto, and it's statically checked.

all auto does it tell the compiler "this variable is of the same type that is being assigned to it". If that's your intent, auto is **the correct** way to write your code.

Did you use auto? I never encountered any of the "harder" problems you describe.
I suspect the reason is because they're problems caused by not using auto in the first place, like changing the return value of a function and now you have to use search to replaces all the types of the variables that use it.

Herb Sutter had a talk in CppCon 2014 - "Back to the Basics! Essentials of Modern C++ Style", at ~28:20 he talks about auto:
https://youtu.be/xnqTKD8uD64?t=28m23s

[quote="Eugene, post:11, topic:2788"]
It is just almost unneeded. So I see no reason to bring inconsistency to codebase.
[/quote]

Show me a better way to initialize a vector with the following values than this:
```C++
std::vector<int> v{5, 10, 3, 9, -3, 2500};
```

-------------------------

1vanK | 2017-02-14 05:43:08 UTC | #13

[quote="Enhex, post:12, topic:2788"]
Herb Sutter had a talk in CppCon 2014 - "Back to the Basics! Essentials of Modern C++ Style", at ~28:20 he talks about auto:
[/quote]

He can say any thing, but if I had to guess the type or move mouse to read the tooltip, it does not simplify my life :) it just slows down the perception of the code

-------------------------

1vanK | 2017-02-14 05:47:10 UTC | #14

I open random files:

```
    XMLElement rootElem = file->GetRoot();
    XMLElement paramElem = rootElem.GetChild();
```
```
    UI* ui = GetSubsystem<UI>();
    UIElement* uiRoot = ui->GetRoot();
```
Imagine this code with auto.

-------------------------

Eugene | 2017-02-14 13:24:57 UTC | #15

[quote="Enhex, post:12, topic:2788"]
Show me a better way to initialize a vector with the following values than this
[/quote]

```std::vector<int> v = {5, 10, 3, 9, -3, 2500};```
is good enough

> auto doesn't disable strong typing, I'm not sure if you know what that means.

I didn't say 'disable'. I meant that strong-typed language with `auto` loses its readability advantages and became scripty.

> Did you use auto?

Yes.
I always use `auto` in small projects that I am not going to maintain. It's okay.
I also use `auto` at work because it is our style. I put up with it.

> I never encountered any of the "harder" problems you describe.

I did.
Have you ever tried to explore big infamiliar codebase written in AAA?

Look at @1vanK example and imange that you know nothing about types `XMLElement`, `UI` and `UIElement`.
How do you recognize this piece of code then?


    auto rootElem = file->GetRoot();
    auto paramElem = rootElem.GetChild();
    //< These guys might be similar, yep?
    //< Nodes of some hierarchy, probably. What hierarchy?
    //< Values or pointers? Must be values because I see dot.
    //< What about const?
   
    auto ui = GetSubsystem<UI>();
    //< Ok, here I can guess the type. It is some singleton.
    //< So it's non-unique pointer
    //< Is it shared or raw? What about const?
    //< Probably it is just UI*, because it is a singleton.
    //< Or maybe weak ptr, who knows?

    auto uiRoot = ui->GetRoot();
    //< No ideas WTF is it
    //< Root element of some hierarchy.
    //< Is the same type as rootElem from first part of code??

-------------------------

Enhex | 2017-02-14 19:09:14 UTC | #16

I had to make this:
https://www.youtube.com/watch?v=V4DkJtT2jdE

 :^)

-------------------------

Eugene | 2017-02-14 20:11:46 UTC | #17

I hope you understand that IDE tooltops is not a solution for explained problem.
Code shall be readable enough for reviewing via notepad/browser/difftool/etc.
Code is all that we always have. IDE is optional.

So, briefly, my thoughts and proposal:

- `auto` saves time when writitng code
    - It is the main advantage of `auto` and the main reason for programmers to use it
        - Other advantages are less important and affect some rare corner cases
- You can comfortable work with `auto` variable if one of the following conditions is true:
    - If you ask IDE for tooltips (i.e. use mouse when reading code)
    - If you explore variable context (i.e. spend time on checking related functions and objects)
    - If you are familiar enough with codebase/architecture to guess the type by name and context
- Explicit variable decalration is easy to read and understand without any conditions or extra effort.
    - So explicit type is _objectively_ more readable than `auto`
    - Exception: ugly big types
        - Probably such types need or already have an alias
            - If they don't, `auto` is a perfect solution!
- Programmers always say that good readablility is more important than quick writing
    - Why `auto` shall be an exception?
- It's not so hard to replace dozen of `auto`s in your commit when you finish your work
    - Especially with these nice tooltips
        - Why not to make life easier for others?

-------------------------

Enhex | 2017-02-14 20:23:50 UTC | #18

Consider the following piece of code:

```C++
int x = f();
```
Can you know the return type of f() from reading it?

The answer is no.

auto isn't about quick writing.
If that's your understanding of auto, you didn't watch the video I linked or wasn't capable of understanding it.

If you want to stick with C++98 why did you suggest moving to C++11?
Especially considering you don't understand and like C++11.

-------------------------

1vanK | 2017-02-14 21:22:38 UTC | #19

if f() return not int it should be fixed - "I need int, but it not, wtf" - auto hide this problem

> auto isn't about quick writing

auto not about quick learning unknown code

>  you didn't watch the video

I can found 1000 links criticized auto

> Herb Sutter (Microsoft)

I will not say anything about quality of code in Microsoft's products xD

-------------------------

Eugene | 2017-02-15 08:47:26 UTC | #20

[quote="Enhex, post:18, topic:2788"]
auto isn't about quick writing
[/quote]

Phew. If auto was long and complex, would anybody use it? I am sure no.
There are two groups of people who use auto: ones use auto because it is shorther, others don't want to admit it and try to find another reasons. A kind of lying to yourself.

> If that's your understanding of auto, you didn't watch the video I linked or wasn't capable of understanding it.

If somebody change return type of function, he **must** revise all places where function is used just because they are affected by this change. Regardless of using or not using auto.

I didn't watched the video because:

- I've read Sutter and Co and know almost all this stuff about `auto`
- Nobody explains how to solve readability issues except selfish phrases like >>you don't need to know a type because I don't<<
- When project is big and maintained by many people, other pros and cons of auto are negilible comparing to readability problem

> If you want to stick with C++98 why did you suggest moving to C++11?
Especially considering you don't understand and like C++11.

С++11 has many cool features (including auto) but it doesn't mean that they shall be thoughtlessly used everywhere.

-------------------------

Eugene | 2017-02-15 15:37:05 UTC | #21

Okay, here is another, style question.

Without `auto` there is only one style of declaring variables.
With `auto` there are two styles, because `auto` can't replace all explicit declarations.

I dislike this ambigity, but it's not very bad.

In _your_ opinion, where `auto` shall be used and where shan't?
Do you have some strict rules that can be enforced in guideline?

This criteria is very subjective:

[quote="Enhex, post:12, topic:2788"]
if you don't want to use the type foo returns you shouldn't use auto.
[/quote]

-------------------------

Modanung | 2017-02-15 16:06:00 UTC | #22

### See also: [C++ Core Guidelines](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md).

-------------------------

Eugene | 2017-02-15 17:02:51 UTC | #23

I tried to read it some time ago. It's quite big, I am on 25% now.
Did you want to accent some part of this document?

-------------------------

Enhex | 2017-02-15 18:59:34 UTC | #24

It isn't a stylistic issue.
It's correctness, type safety, and maintainability.

I think the same as Herb Sutter: if you want to track a type you should use auto, if you want to stick with a type you shouldn't. Tracking is the common case.
Also auto can be used in other cases to keep things DRY, like new, static casts, example:
```C++
auto user = static_cast<Node*>(eventData[Use::P_USER].GetPtr()); // type already mentioned in the static cast
```

Watch the video I linked, it has excellent examples of cases that not using auto will cause problems.

"This criteria is very subjective:"
This isn't subjective at all, it's a fact.
```C++
int f();
long x = f(); // f() returns int, we want long. using auto here will result int
```

-------------------------

1vanK | 2017-02-15 19:01:43 UTC | #25

[quote="Enhex, post:24, topic:2788"]
int f();
long x = f(); // f() returns int, we want long. using auto here will result int
[/quote]

long and int is same type :)

-------------------------

Enhex | 2017-02-15 21:10:05 UTC | #26

Wrong, it's compiler implementation defined and the requirements are different:
http://en.cppreference.com/w/cpp/language/types#Integer_types

So you just created a very subtle bug that may or may not happen to some users on different compilers (including different versions of the same compiler).

-------------------------

1vanK | 2017-02-15 19:11:01 UTC | #27

Ok, I posted answer above already. I expect one type, but function return other. Complier (VS at least) will warn. But if a will using auto, I would not notice this problem

-------------------------

Enhex | 2017-02-15 19:32:28 UTC | #28

they won't warn because there's no truncation unless they're implemented as different sizes. (and even then only VC++ by default)

This was an example for not using auto anyway, when the intention is to stick with long.
(the bug is something else - assuming long is same type as int)

-------------------------

1vanK | 2017-02-15 19:27:12 UTC | #29

Ah, ok I understood what you mean

-------------------------

Eugene | 2017-02-15 21:32:55 UTC | #30

[quote="Enhex, post:24, topic:2788"]
if you want to track a type you should use auto, if you want to stick with a type you shouldn't.
...
"This criteria is very subjective:"
This isn't subjective at all, it's a fact.
[/quote]

Okay, let's imagine. One guy insist that the type of some variable shall be explicit. Another guy insist that type of some variable shall be auto. If your criteria is a fact, please logically solve this argument.

    const String::operator std::string() { /* cast to std string here with copying */}
    const String& Node::GetName();
    ...
    const auto& name = node->GetName(); // vs const String& name
    if (name == "Player") { ... }

One guy said that explicit type is better because if we change String to const char* the nasty bug will appear:

> if you don't want to use the type foo returns you shouldn't use auto.

Another guy said that auto type is better because if we write explicit `String` and change `String` to `std::string` in function signature, the redundand copying will appear. Also, code is generic enough to work with different types of strings. According to all guidelines, `auto` shall be used here.

-------------------------

hdunderscore | 2017-02-15 21:37:24 UTC | #31

In practice code will be contributed to Urho using the contributors preference, and it is unlikely an issue will arise unless they are going full-auto and it has become hard to read. If there is a bug identified, the contributor will surely feel compelled to correct the bug.

-------------------------

Eugene | 2017-02-15 21:58:07 UTC | #32

[quote="hdunderscore, post:31, topic:2788"]
In practice code will be contributed to Urho using the contributors preference, and it is unlikely an issue will arise unless they are going full-auto and it has become hard to read.
[/quote]

That's the problem.
Some guys like me will probably almost avoid `auto` in commits.
Some guys like @1vanK will use `auto` somewhere for long types.
Some guys like @Enhex will prefer using `auto` in declarations.
Then, code _may_ stay readable enough.
However, code will be a mess of different styles. That's ugly.
Urho3D has so nice style now, because it was written by single person in a languare that has no `auto`.
It's hard for me to admit that this will be lost.

-------------------------

hdunderscore | 2017-02-15 23:05:40 UTC | #33

Looking through the urho codebase, I don't see many instances of where code would be improved by auto. For entertainment value, an automated tool can be used to put that to the test (eg, https://github.com/steveire/clazy).

Moving on to other C++11 features, I think brace initialization is clearer and more convenient when extended with initialization_lists. I think ```typedef```s should be upgraded to use ```using```. ```enum```s upgraded to ```enum class```es (as long as scripting doesn't choke on it).

I think an upgrade to use ```move``` could be worthwhile. With the change to c++11 we could maybe re-evaluate using our custom containers vs the stl.

I would probably avoid lambdas for the most part.

-------------------------

Eugene | 2017-02-15 23:32:02 UTC | #34

I hate such disputes, trust me... *sigh* :weary:

There is interface-oriented AAA (yep, I've read Sutter and his articles).
There is type-oriented... huh, let's call it 98 

AAA is nice-looking. 98 is bulky.
AAA is theorectically perfect. 98 has theoretical pitfalls.
Yes, they are more theorethical than practical since function signature is rarerly changed.
You have much more chances to inject bug e.g. in logic or catch a problem with implicit casting from SharedPtr<T> to T*.

98 is used for all legacy code. AAA is used nowhere.
98 is simpler to understand. AAA is more puzzled.

I don't say that AAA has no benefits.
However, I think that benefits of 98 cost more than benefits of AAA when we are talking about Urho (old big project).
If we were talking about new small project, AAA'd be better.
If we were talking about new big project... questionable. Maybe I have to try big AAA project at some point.

[quote="hdunderscore, post:33, topic:2788"]
enums upgraded to enum classes
[/quote]
Then we will have to write some migration script to Find&Replace old enums with new ones in client (and Urho) code.

> With the change to c++11 we could maybe re-evaluate using our custom containers vs the stl.

Unsure that it's good idea. This will break a lot of code unless wrappers over STL are written.

-------------------------

cadaver | 2017-02-16 08:45:17 UTC | #35

Guaranteed binary size is to me still the biggest advantage of the custom containers, which allows storing them "inside" Variant. Moving to STL containers the only safe thing to do would be to always heap allocate them instead, which would add some overhead. I don't pretend that the custom containers are a performance advantage nowadays, and if I was starting a new engine today I would likely avoid them, just to reduce maintenance cost / codebase size / possibility of errors.

-------------------------

1vanK | 2017-02-16 08:59:25 UTC | #36

In https://github.com/1vanK/Urho3DSpriteBatch/blob/master/SpriteBatch.h I compared Urho3D::PODVector vs std::vector, and Urho3D::PODVector won :)

-------------------------

Eugene | 2017-02-16 09:14:50 UTC | #37

[quote="cadaver, post:35, topic:2788"]
I don't pretend that the custom containers are a performance advantage nowadays, and if I was starting a new engine today I would likely avoid them, just to reduce maintenance cost / codebase size / possibility of errors.
[/quote]

However, your containers are much faster than STL ones in debug mode.
It's getting too hard to debug something when you have 5 FPS on complex scene with these safe iterators.

-------------------------

cadaver | 2017-02-16 12:22:28 UTC | #38

Does the iterator debug level help, though?

https://msdn.microsoft.com/en-us/library/hh697468.aspx

-------------------------

Eugene | 2017-02-16 13:10:49 UTC | #39

I haven't managed to make it work last time when I tried it. It was long time ago.

-------------------------

Enhex | 2017-02-16 18:20:51 UTC | #40

[quote="cadaver, post:35, topic:2788"]
Guaranteed binary size is to me still the biggest advantage of the custom containers
[/quote]
What about STL implementations which aren't bundled with the compiler? Like [EASTL](https://github.com/electronicarts/EASTL) (haven't looked into it myself).

[Boost.Container](http://www.boost.org/doc/libs/1_63_0/doc/html/container.html) also provides some nice optimized containers.
I benchmarked its small_vector and it's very fast for its purpose:
https://plot.ly/~Enhex/74.embed
(source: https://github.com/Enhex/Benchmarks/tree/master/boost%20small_vector)
Tho I'm getting off topic.

[quote="Eugene, post:37, topic:2788"]
much faster than STL ones in debug mode.
[/quote]

That's because they don't provide any debugging information, which defeats the purpose.
I know that in my code I had to replace things like HashMap with std::unordered_map to be able to debug their content.

it's like saying:
```C++
int main() {
  while(true) {}
}
```
is the fastest game engine. It's fast because it doesn't do anything useful.

-------------------------

Eugene | 2017-02-16 18:41:48 UTC | #41

[quote="Enhex, post:40, topic:2788"]
What about STL implementations which aren't bundled with the compiler? Like EASTL (haven't looked into it myself).
[/quote]

I think that the biggest issue is not about implementation, but about interfaces. There are a lot of downstream projects. It would be cruel to make their authors to fix their code.
It is possible to rewrite e.g. EASTL to fit it into legacy interface of Urho containers, but it will require some effort.

> That's because they don't provide any debugging information, which defeats the purpose.
> I know that in my code I had to replace things like HashMap with std::unordered_map to be able to debug their content.

wat? :confused:

What kind of STL debug garbage do you need?
If I want to debug Urho containers, I do it in debugger.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/c94cbcd77f2bc21120ed6809214bc8d18272a7dd.png" width="690" height="167">

-------------------------

Enhex | 2017-02-16 18:56:51 UTC | #42

[quote="Eugene, post:41, topic:2788"]
If I want to debug Urho containers, I do it in debugger.
[/quote]
[quote="Enhex, post:40, topic:2788"]
...be able to debug their content.
[/quote]
Try doing that.

Here's what I see:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/9c2c5aeb5fcf1e4954fa6b85e444d4eb3251aaf4.png'>

Which doesn't happen with std containers.

-------------------------

Eugene | 2017-02-16 19:42:15 UTC | #43

Huh.
Additionally, you'll need some knowledge about debug visualizers. Complex stuff like HashMap also requires VS 2015.
It's not very hard to make it work, check this.
https://github.com/eugeneko/Urho3D-Debug

-------------------------

yushli1 | 2017-02-17 02:16:52 UTC | #44

Thanks for the VS2015 Visualizer file! That really works. It helps a lot when debugging.

-------------------------

Enhex | 2017-02-18 09:51:37 UTC | #45

Thanks!

BTW when debugging std::unordered_map you can see the original strings (with the visualizer you only see hashes).
I assume std::unordered_map stores the strings in debug which makes it slower, but provides useful information.

-------------------------

Eugene | 2017-02-18 10:24:10 UTC | #46

[quote="Enhex, post:45, topic:2788"]
with the visualizer you only see hashes
[/quote]

That's because `Urho3D::VariantMap` is `HashMap<StringHash, Variant>` and don't contain names.
So, that's not a question to visualizer or debug info. More likely, it's about performance and amount of allocations made by `VariantMap`.

`HashMap<String, Variant>` will give you real strings, of course.
I mean I hope so because I tested my visulaized long time ago.

-------------------------

Sinoid | 2017-02-22 06:16:04 UTC | #47

Don't wait on me. An upgrade to C++11 will be massively beneficial to most of the pending stuff. Variadic templates could really simplify shaders (aside from the hash-code ... which will just get fatter, but the pipeline looks pretty fixed now so that's just 64bit int).

The only thing I'd like to push out before then would be cubemap filtering (that also means DDS writing, have to write those mipmaps for filtering them to really be worth anything).

- Offtopic, is there a footer sytem so I can indicate "keep it on technical point" or such? I want to keep my involvement to task at hand, not idealogy and such.

-------------------------

TheSHEEEP | 2017-02-22 06:45:22 UTC | #48

 
Rule no. 1 for system changes:
If it ain't broken, don't fix it.

If the custom containers work just fine and impose no performance/memory downside, there's no reason to switch to STL ones. Obviously, this can be tested and it seems some did that already (and seemingly there's no reason to switch).

Auto... oh, auto... Let's not. Please. I like to read my code and understand it without having to move back through functions until a **real** type appears somewhere.
I see the point in using it for abbreviation purposes, though. Iterators are a good example, because their type declaration usually looks like it was made to make people suffer. If there is a "auto iter = someContainer.begin();", everybody will understand it and some (like me) will be thankful. A typedef is IMO not a solution here because it just moves the problem out of sight (you got the ugly piece of code elsewhere, but it is still present).
But in all other cases, auto just adds confusion instead of clarity.
Either way, there is no gain in replacing working existing code with it.

I can't say much about other issues like with variadic templates. Personally, I avoid templates like the plague, because I like to retain my sanity when reading error outputs. Of course, I see the point in them, so if existing code can actually be made **more** readable or more performant with them, I'm all for it. 
As long as I don't have to write them, I really don't care if a library I use makes use of them :D

-------------------------

Eugene | 2017-02-22 10:58:16 UTC | #49

[quote="TheSHEEEP, post:48, topic:2788"]
A typedef is IMO not a solution here because it just moves the problem out of sight (you got the ugly piece of code elsewhere, but it is still present).
[/quote]
If you need iterator, you probably have container, e.g. `Vector<SharedPtr<Object>>`.
Such container is probably used in several places and may be typedef-ed.
`ObjectArray::Iterator` is much less scary, isn't it?
But it is an issue what is more readable: long name with all related types or typedef abbreviation.

[quote="TheSHEEEP, post:48, topic:2788"]
But in all other cases, auto just adds confusion instead of clarity.
[/quote]
This is not a problem of `auto` itself. It's mostly about 'interface-oriented' programming style when you work with public interfaces (e.g. public methods or properties) instead of concrete types. C++ templates are usually written in such style, and this style is common for script languages like Lua or Pyhton.
And I agree that 'interface-oriented' code is harder to understand than classic 'object-oriented'.

[quote="TheSHEEEP, post:48, topic:2788"]
I see the point in using it for abbreviation purposes, though. Iterators are a good example, because their type declaration usually looks like it was made to make people suffer. If there is a "auto iter = someContainer.begin();",
[/quote]

Urho has a bucket of rules like 'no tabs', 'use camel case' etc. They are strict and easy to follow.

The probem with `auto` is that anybody have his own criteria where to use `auto` and where not to use.
If @cadaver just say 'follow the common sence', Urho may end up in codestyle mess because everybody has its own (of course, evident) rules.

Just look at these examples and try to answer where to use `auto` and where not to (and why):

1) `Vector<HashMap<String, Pair<Node, Component>>>::Iterator`
very long and ugly iterator

2) `Vector<SharedPtr<Component>>::Iterator`
just quite long iterator

3) `Vector<SharedPtr<Component>>`
this type is not an iterator, but still long

4) `Vector<SharedPtr<Component::Data>>`
as long as 2) but _almost_ the same as 3)

5) `const Vector<SharedPtr<Component>>&`
as long as 2) but _the same_ as 3)

6) `Vector<int>::Iterator`
pretty short iterator

7) `HashMap<String, int>`
as long as 6) but not an iterator

8) `const HashMap<String, int>&`
longer than 6) but not an iterator

-------------------------

cadaver | 2017-02-24 13:54:45 UTC | #50

I just looked at the Turso3D codebase and there I have used auto for iterators only (shortening & convenience). That could be one possible rule that's at least easy to follow. But I don't want to say it should be *the* rule, or that I'd want final authority on this matter. I agree that it's just important that we decide something that is clear to follow.

-------------------------

Victor | 2017-02-24 14:55:36 UTC | #51

[quote=cadaver]I just looked at the Turso3D codebase and there I have used auto for iterators only (shortening & convenience). That could be one possible rule that's at least easy to follow. But I don't want to say it should be the rule, or that I'd want final authority on this matter. I agree that it's just important that we decide something that is clear to follow.[/quote]

That's pretty much how I've been using 'auto' as well.

-------------------------

Eugene | 2017-02-24 15:04:35 UTC | #52

I have two more cases. `auto` shall (may?) be used

- with _any_ iterators if there is no one-word alias
- with _any_ pairs and pair-like structures (e.g. `HashMap<T, U>::KeyValue>`) if there is no one-word alias
  - However, prefer to extract pair content into variables with meaningful names
- with unknown template types if there is no one-word alias 
  - So, use `auto` instead of those ugly `typename`s and `decltype`s

Such rules are also pretty clear to follow, IMO.

-------------------------

rku | 2017-02-26 13:59:29 UTC | #53

[quote="TheSHEEEP, post:48, topic:2788"]
If the custom containers work just fine and impose no performance/memory downside, there's no reason to switch to STL ones. Obviously, this can be tested and it seems some did that already (and seemingly there's no reason to switch).
[/quote]

I am in favor of using standard containers. Less confusion and better interoperability with other libraries not to mention not having to maintain said containers. Custom stuff is only useful if it provides something standard stuff does not. But is there really any benefit nowdays?

-------------------------

Enhex | 2017-02-26 22:02:55 UTC | #54

Urho's HashMap doesn't handle collisions, so it's faster but less reliable than std::unordered_map.

-------------------------

Eugene | 2017-02-27 07:28:12 UTC | #55

[quote="Enhex, post:54, topic:2788, full:true"]
Urho's HashMap doesn't handle collisions, so it's faster but less reliable than std::unordered_map.
[/quote]

Why do you think so? This sounds _very_ strange. Generic HashMap container must handle collisions.

-------------------------

Enhex | 2017-02-27 17:53:38 UTC | #56

It seems I'm wrong, for some reason I remembered it doesn't handle collisions.

-------------------------

rku | 2017-03-01 08:23:51 UTC | #57

At the same note we really should drop old cmake support. New versions have some useful goodies that would help simplifying build system, and boy oh boy we do need that. For example i came upon [target_compile_definitions](https://cmake.org/cmake/help/v3.0/command/target_compile_definitions.html) just now. The only reason to hold back on cmake would be having easy support for linux distributions, however new ubuntu LTS (16.04) already ships cmake v3.5. For windows it does not matter as user just installs latest and greatest from cmake website.

-------------------------

Sinoid | 2017-04-21 06:21:12 UTC | #58

I rescind a desire to squeeze out cubemap filtering, I'm butting heads intensely with just interacting with cmft and the like remotely without crashing as a post process, that's a red flag. It's also just not going to fit even in a case of relying on other tools. I would much rather see a hard release and then work on finishing surround and LFE sound.

-------------------------

TheComet | 2017-04-24 17:53:21 UTC | #59

Travis CI still uses an ancient version of cmake. You'd break integration tests by using newer cmake stuff.

-------------------------

weitjong | 2017-04-25 09:59:24 UTC | #60

Just dropping by to say that there is no reason to set the minimum required CMake version higher than it needs to be. That is, we should only increase the version to the level our script really utilizes. Setting a high version number does not automatically make our build system better. I do agree on the point that we should modernize the scripts to take the advantage of some of the newer features and idioms provided by newer CMake though.

Also keep in mind there is more Linux distros out there than Ubuntu. So what CMake version it shipped in what LTS version does not have too much bearing on our decision making, except for our CI need as highlighted by TheComet. 

And lastly. please stay on topic.

-------------------------

Modanung | 2017-04-25 10:03:33 UTC | #61

[Here](https://repology.org/metapackage/cmake/versions)'s an overview of CMake versions in different repositories.

-------------------------

