rku | 2017-10-21 11:46:48 UTC | #1

I propose adopting `clang-format` for keeping code style in check. I worked out rather similar [.clang-format](https://github.com/rokups/Urho3D/blob/feature/clang-format/.clang-format) config for the project. See a resulting [diff](https://github.com/rokups/Urho3D/commit/4a4a7dfbe1bdb1816368cd5d8ed241646f50b8a4). Style applied by config is pretty much same as described in project style guide.

What do you think?

-------------------------

weitjong | 2017-10-21 13:37:55 UTC | #2

That is the direction we would like to go eventually. The rule should be configured that it didn't cause too much unnecessary changes, IMHO.

-------------------------

rku | 2017-10-22 07:41:00 UTC | #3

That is what i aimed for. Thing is style was not really followed to the letter in some places, and some details were not in the style guide altogether so big diff cant be avoided. Given that i say its pretty small.

I Maybe it is a good place to discuss one style bit too. Naturally i would not suggest it, but if clang-format is adopted it may be a good opportunity for a change.

Currently engine uses:

```cpp
MyClass::MyClass() :
    member1_(0),
    member2_(42)
{
}
```

This is a tiny bit suboptimal, because adding new member initializer to constructor causes two line change. New comma after `member2_(42)` and a next new line.

Maybe it would be a good idea to adopt this?

```cpp
MyClass::MyClass()
    : member1_(0)
    , member2_(42)
{
}
```

Adding a new member or removing last member would never cause extra line modifications.

This really is a non-issue, but just a nice thing to have. It is unfortunate that we can have comma after last item of enum, but not after last member initializer in constructor.

-------------------------

Eugene | 2017-10-22 08:17:28 UTC | #4

[quote="rku, post:3, topic:3677"]
Maybe it would be a good idea to adopt this?
[/quote]

I like this style too. Yeah... It'd be great if there is some tool for migration.

-------------------------

rku | 2017-10-22 08:29:41 UTC | #5

[quote="Eugene, post:4, topic:3677"]
It’d be great if there is some tool for migration.
[/quote]

I just proposed such tool and you can see it in action (links in the first post) :)

-------------------------

Eugene | 2017-10-22 10:04:05 UTC | #6

Huh, I didn't read the first post because I thought for some reason that you are talking about linter tools @weitjong is working on.

-------------------------

rku | 2017-11-04 16:46:22 UTC | #7

Is there anything i could do to make this happen sooner than later?

-------------------------

weitjong | 2017-11-05 00:25:17 UTC | #8

Usually we do not block contributors from contributing, but in this case since we are in the middle of Clang-tidy refactoring with many code being changed, the last thing we want is to have a potential version conflict (caused by code formatting change) everywhere. So, definitely it should be later.

-------------------------

rku | 2017-11-05 08:58:54 UTC | #9

Oh cool. I did not notice this was already in flight. If anyone else is interested, the branch: https://github.com/urho3d/Urho3D/commits/clang-tidy-up

Good stuff, thank you!

-------------------------

