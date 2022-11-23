Enhex | 2017-08-30 15:39:09 UTC | #1

**TL;DR:** Choose official coding guideline to shut down wasteful pointless arguments.

While Urho3D have coding style guidelines (stuff like naming & indentation), it doesn't have coding guidelines.

Considering arguments [block PRs](https://github.com/urho3d/Urho3D/pull/2106#issuecomment-325223425), and since @cadaver left, I think it's important to have agreed upon official guidelines so we can point [bikeshedders](https://en.wiktionary.org/wiki/bikeshedding) to them to shut down the argument, so they won't waste time and block progress.

Since it's pointless to try to argue with "Poisonous People"<sup>[1]</sup>, because:
* They don't listen
* They just want to keep arguing forever

I'm in favor of using [C++ Core Guidelines](https://github.com/isocpp/CppCoreGuidelines), and here are the reasons:
* It's written and reviewed by a lot of people, including experts like C++ committee members.
* It addresses a lot of topics - less opportunities for arguments.
* At least with Visual Studio, there's static analysis checker for the Core Guidelines.
* It's designed for modern C++

Note that the goal of using a coding guideline (at least for me) is not to fanatically follow it, but to shut down wasteful arguments by already having official rules in place.

1 - Poisonous People:

https://www.youtube.com/watch?v=-F-3E8pyjFo

Please vote:
[poll type=regular public=true]
* Let's use C++ Core Guidelines
* Let's use some other guideline (please explain which and why)
* I'm against using guidelines
[/poll]

-------------------------

Eugene | 2017-08-30 13:47:27 UTC | #2

My answer is 2. Detailed _opinion_ is below.

C++ Core Guidelines pros:

- Reasonable guideline designed by many clever people;
- Already written;

Cons:

- Hard to check code conformity. All contributors literally have to read and re-read 100-pages paper.
- **The guideline interferes with Urho legacy code;**

The last item is most important here.

If there is a conflict between contribution and legacy, it must be resolved before merge. This rule is obvious for code contributions.

I don't think that _code standard_ contribution is too different from code. If you introduce code standard changes that interfere with legacy code, you should resolve the conflict.

My recent actions is a kind of example.
1. I _committed_ three strict rules into code standard (override is required, typedef is forbidden, 0 and NULL pointer constants are forbidden)
2. There become a conflict;
3. I resolved the conflict. Urho master branch is fully conformant with newly committed coding conventions;

Some new C++11 features doesn't replace old counterparts. `{}`-ctor cannot completely replace `()`-ctor, `auto` cannot completely replace explicit type, inplace member initalization cannot completely replace initializer lists, range-based `for` cannot completely replace index-based `for` and so on.

I also committed some _weak_ rules related to these features. These rules are not requirements but suggestions. Such rules doesn't interfere with legacy code due to their weak nature.

**C++ Core Guidelines are in the conflict with Urho code, so they couldn't be commited until the conflicts are resolved either on the guidelines or on the code side.**

If the project's code doesn't meet the project's codestyle, it is equal to the absence of the codestyle.
So, "Let's use C++ Core Guidelines" is equal to "Let's drop codestyle requirements".
I couldn't vote for such item, with all due respect to C++ Core Guidelines itself (no sarcasm)

----------

Wow, I almost forget about an answer. We should use guidelines that are not in the conflict with Urho legacy.

-------------------------

Enhex | 2017-08-30 14:02:06 UTC | #3

[quote="Eugene, post:2, topic:3509"]
Hard to check code conformity. All contributors literally have to read and re-read 100-pages paper.
[/quote]
You literally have [static analysis tool that automatically do it](https://blogs.msdn.microsoft.com/vcblog/2017/08/11/c-core-guidelines-checker-in-visual-studio-2017/) (didn't you read what I wrote?). Also you don't have to read it all, it's very organized and broken into categories and short points on each topic.

[quote="Eugene, post:2, topic:3509"]
The guideline interferes with Urho legacy code;
[/quote]
Doesn't matter. There's absolutely 0 need to go back and upgrade all existing code.
Just apply it to new code.
Your "conflict" is a non-issue.

There's no need to fanatically follow a guideline.

-------------------------

1vanK | 2017-08-30 14:09:22 UTC | #4

I can not block anything, since I do not have the authority, I can only express my point of view. 
Poisonous People? Ok. Everyone whose opinion does not match yours is a "toxic person". It turns out from my point of view that you. Just answer the question whether your PR code is more understandable. Why do we need PR, which makes the code less understandable?

-------------------------

Eugene | 2017-08-30 14:11:52 UTC | #5

[quote="Enhex, post:3, topic:3509"]
You literally have static analysis tool that automatically do it (didn’t you read what I wrote?). Also you don’t have to read it all, it’s very organized and broken into categories and short points on each topic.
[/quote]

This is not a problem for me. Try to convince remaining 100 contibuitors to check their code. They sometimes don't even follow indentation rules... /_-

BTW, some people don't use Visual Studio.

[quote="Enhex, post:3, topic:3509"]
Doesn’t matter. There’s absolutely 0 need to go back and upgrade all existing code.

Just apply it to new code.

Your “conflict” is a non-issue.

There’s no need to fanatically follow a guideline.
[/quote]
It's highly depends on guideline items. I agree that we could follow many of them, but definetely not all. So, the 1st item in the vote is just unrealistic. We will have to tune C++ Core Guidelines anyway.

-------------------------

HplusDiese | 2017-08-30 14:17:31 UTC | #6

What about UE4 code style?
It looks like my code style, but with some refinements. I use it in my personal project.
https://docs.unrealengine.com/latest/INT/Programming/Development/CodingStandard/

-------------------------

Enhex | 2017-08-30 14:25:57 UTC | #7

You block it in the sense you create an argument over a tiny detail you personally don't like.

Regarding "Poisonous People" just watch the talk. The term sounds nasty but in short it just means redirecting peoples time and energy to pointless stuff and thus stalling progress.

[quote="Eugene, post:5, topic:3509"]
Try to convince remaining 100 contibuitors to check their code.
[/quote]
You don't need to. You're not listening.
I wrote in the previous reply you don't need to go back and upgrade everything.

[quote="Eugene, post:5, topic:3509"]
1. I agree that we could follow many of them, but definetely not all.
2. So, the 1st item in the vote is just unrealistic.
3. We will have to tune C++ Core Guidelines anyway.
[/quote]
1. That's only your opinion.
2. It's more realistic than you writing your own guidelines that no one else agreed upon.
3. Why? Because there are things you personally don't like?

[quote="Eugene, post:5, topic:3509"]
some people don’t use Visual Studio.
[/quote]
It's enough that 1 contributor does. He can run it once in a while, find and fix problems, and submit fixes.

-------------------------

1vanK | 2017-08-30 14:21:04 UTC | #8

"pointless stuff" is rewriting exiting and working code

-------------------------

1vanK | 2017-08-30 14:29:05 UTC | #9

In any case, when you plan to add new cool features to Urho?

-------------------------

Eugene | 2017-08-30 14:32:31 UTC | #10

[quote="Enhex, post:7, topic:3509"]
You don’t need to. You’re not listening.

I wrote in the previous reply you don’t need to go back and upgrade everything.
[/quote]
I am. I meant that it may be harder to enforce people follow the rules when they make PRs.

> It’s more realistic than you writing your own guidelines that no one else agreed upon.

I don't suggest this.

> That’s only your opinion.
> Why? Because there are things you personally don’t like?

My personal tastes doesn't matter here. Personally I _do_ like e.g. standard containers and leading-comma initializer lists, but I don't push them to Urho out of respect for legacy.

The main and the only mission of the code standard is to keep code consistent by enforcing rules. If code doesn't meet the code standard, this standard is a pointless bullshut.

I'll revise Core Guidelines and list concrete 'bad' items to be less unfounded.

-------------------------

Enhex | 2017-08-30 15:00:18 UTC | #11

It's very basic.
It seems to be mostly about formatting style choices. Urho3D already has style guideline.
(personally I don't care much about if u break line before braces and other such style decisions).
It also had good non-style advice.
And some things I don't want such as Hungarian Notation for some classes. It only increases maintenance and has no value (already saw code that had wrong types embedded in names).

Also it isn't as complete as C++ Core Guidelines, which leaves more room for arguments.

[quote="Eugene, post:10, topic:3509"]
but I don’t push them to Urho out of respect for legacy.
[/quote]
Again, there's no need to upgrade existing code. New code can be written in better ways. Things should compile just fine.

[quote="Eugene, post:10, topic:3509"]
The main and the only mission of the code standard is to keep code consistent by enforcing rules. If code doesn’t meet the code standard, this standard is a pointless bullshut.
[/quote]
If the goal of a code standard is to follow a code standard, what's the point?
It doesn't solve any problems.

If the goal of a code standard is to prevent errors/bugs, improve readability, improve correctness, resolve arguments, and so on, it doesn't matter if 100% of your code follows it or not, since more is always better.

-------------------------

Eugene | 2017-08-30 15:08:29 UTC | #12

> Again, there’s no need to upgrade existing code. New code can be written in better ways. Things should compile just fine.

I agree with you _with exceptions_, that's the point.

> it doesn’t matter if 100% of your code follows it or not, since more is always better.

I have a dirty analogy for you.

> "Helicopter is better than car. So I added some blades on top of my car. It's not 100% helicopter, but more is always better."

----------

Here is the list of items that I don't want to be in the Urho. This is quite small subset of C++ Core Guidelines, isn't it?

### Block

ES.107: Don't use unsigned for subscripts
C.133: Avoid protected data

### Block or perform API-breaking refactoring:

Enum.3: Prefer class enums over "plain" enums
Enum.5: Don't use ALL_CAPS for enumerators

### Block or perform refactoring

C.128: Virtual functions should specify exactly one of virtual, override, or final

### Block or use EASTL

ES.1: Prefer the standard library to other libraries and to "handcrafted code"
ES.27: Use std::array or stack_array for arrays on the stack

-------------------------

Enhex | 2017-08-30 15:38:01 UTC | #13

I agree with you against:
ES.107: Don’t use unsigned for subscripts -
use what the container's size type. The claim about performance needs to be proved.

C.133: Avoid protected data

I disagree with you against (not saying we should use them, just that they're not wrong):
Enum.3: Prefer class enums over “plain” enums -
prefer only. They're hard to use for indexing anyway so they're aren't the default choice. I'm not sure if they work with AngelScript too.

Enum.5: Don’t use ALL_CAPS for enumerators -
just easier to read non-all caps.

C.128: Virtual functions should specify exactly one of virtual, override, or final -
override is implicitly virtual. mixing final with the others doesnt make sense

ES.1: Prefer the standard library to other libraries and to "handcrafted code" -
[standard STL is actually faster than Urho's in some cases](https://discourse.urho3d.io/t/urho-vs-stdlib-small-benchmark-vs2015/1225). Need to benchmark EASTL against STL/Urho. Using STL is easier. An argument against std STL is that different compilers got different implementations which can lead to inconsistency.

ES.27: Use std::array or stack_array for arrays on the stack -
std::array is more convenient than C array.


There's no need to 100% follow everything in it.

-------------------------

Eugene | 2017-08-30 16:02:13 UTC | #14

> use what the container’s size type

Exactly.

> I disagree with you against (not saying we should use them, just that they’re not wrong)

I didn't completely understand you, elaborate, please.

> prefer only. They’re hard to use for indexing anyway so they’re aren’t the default choice.

`enum class`es will bring inconsistency into Urho public interface. Inconsistent public interface is a bullshit. So I am against using `enum class` at all in the entire Urho3D Core. Let's leave them for community modules.

> just easier to read non-all caps

Agree. But: see above.

> override is implicitly virtual. mixing final with the others doesnt make sense

I know >5 people who prefer to always keep virtual, but it's just personal taste.
The more important thing is that inconsistency here is misleading and confusing for readers.
Before following this rule in new code all redundand virtuals shall be removed. It's not so hard, actually.

> Using STL is easier. An argument against std STL is that different compilers got different implementations which can lead to inconsistency.

STL may be slower in debug mode. Moreover, we still shall not use neither STL nor EASTL in public API because Urho already uses its own containers to interact with user.

> std::array is more convenient than C array.

It is. This item depends on the previous.

> There’s no need to 100% follow everything in it.

If we don't follow C++ Core Guidelines in 100%, I consider it as _different_ guideline and item 2 in vote. Probably, I misunderstood the vote.

-------------------------

