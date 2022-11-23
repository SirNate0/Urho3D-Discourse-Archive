vmost | 2020-09-26 17:59:45 UTC | #1

Hi, I'd like to have a switch statement for events, but can't seem to figure it out.
```
switch (eventType)
{
case E_KEYUP:
...
break;
case E_KEYDOWN:
...
break;
default:
};
```
Seems like it should be simple, right? My compiler complains
```
error: switch condition type
      'Urho3D::StringHash' requires explicit conversion to 'bool'
        switch (eventType)
...
error: value of type
      'const Urho3D::StringHash' is not implicitly convertible to 'int'
                case E_KEYUP:
```

-------------------------

vmost | 2020-09-27 19:22:37 UTC | #2

Apparently you can [only use switch statements with integer types](https://en.cppreference.com/w/cpp/language/switch). I'll just use if-else branches...

P.S. Trying to use `.Value()` had const-ness issues.

-------------------------

SirNate0 | 2020-09-27 03:00:18 UTC | #3

I think can get around that problem by defining some constexpr methods, I think (the hashing ones) and/or adding a user defined literal, but it might require c++14 for the while loop or a recursive style rewrite of the function.

But yes, if-else is probably easier.

-------------------------

S.L.C | 2020-09-27 19:22:40 UTC | #4

If you really want that approach, without having to dig into the engine and modify things, then you could modify the `Source/Urho3D/Math/MathDefs.h` file and simply add near the `SDBMHash` function the following:

    /// Retrieve the lowercase version of an ASCII character.
    inline constexpr int tolower_cx(int c) { return (c > 64 && c < 91) ? (c + 32) : c; }

    /// Retrieve the uppercase version of an ASCII character.
    inline constexpr int toupper_cx(int c) { return (c > 96 && c < 123) ? (c - 32) : c; }

    /// Calculate the hash of the given ASCII string using the SDBM algorithm at compile time.
    inline constexpr unsigned SDBMHash_Cx(const char* s, unsigned i, unsigned n, unsigned h) {
        return i < n ? SDBMHash_Cx(s, i + 1, n, tolower_cx(s[i]) + (h << 6) + (h << 16) - h) : h;
    }

    /// User defined literal for converting strings to hashes at compile time.
    inline constexpr unsigned operator "" _H(const char* str, size_t len) { return SDBMHash_Cx(str, 0, len, 0); }

Or even add it to your files if that's all you need. Doesn't matter where you add it as long as it can be used.

And then use the event name directly instead of it's ID:

    switch (eventType.Value())
    {
        case "KeyUp"_H:
        
        break;
        case "KeyDown"_H:
        
        break;
        default:
    };

And if you want, you could change the user defined literal name from `_H` to `_E` or `_Event` if you want it to make sense. Or you could keep all of them since they'll be discarded after compile.

There are a bunch of places where Urho could've make use of `constexpr`. But it's using C++11 `constexpr`. Which is somewhat limited. Wish the engine would've jumped straight to C++14 since that's the sweet spot between compiler support and language features. 17 would be too high but 11 is too low.

C++14 removes some `constexpr` limitations and would've made some things easier and probably better looking.

But at this point, the engine would require some major changes as it wasn't initially designed with that in mind.

-------------------------

vmost | 2020-09-27 19:26:23 UTC | #5

Why not just jump to C++14 now? Would the engine have to be refactored? I haven't tried compiling it with C++14, but my own project needs it and compiles fine with Urho3D as library. EDIT: I suppose using a new C++ version would break the API, so perhaps it would be appropriate for Urho3D2.0.

Then just use 6-year lead time as policy for updating basic C++ version, or 4/5year idk.

-------------------------

S.L.C | 2020-09-27 19:44:37 UTC | #6

The engine just recently "*switched*" to C++11. But only on paper. Not a lot of C++11 was adopted. And I honestly don't mind. It would take a significant amount work to rewrite all parts of the engine to use C++11 or newer. So I don't/can't blame anyone for not happening. I'm certainly not helping in that regard. Even though I could. But time issues :smiley:

So yes, you can enable C++14 if your project needs it. Engine has no issue regardless of what C++ version you use as long as it's newer than what it needs.

MSVC likely played an important role in people adopting these new standards. Since it lags behind with implementing newer standards.

For example, the extended/relaxed `constexpr` from C++14 that I was talking about earlier was implemented in MSVC 2017 but IIRC it had issues which were addressed later on.

For comparison, GCC had it since version 5 from 2015 and Clang had it since version 3.4 from 2013.

https://imgur.com/a/7AacLFB

-------------------------

