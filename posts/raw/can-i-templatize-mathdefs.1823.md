TheComet | 2017-01-02 01:10:28 UTC | #1

I'm getting these errors when using Urho3D's math functions because there exist no overloads of Clamp() (or any of the other math functions) that use double.
[code]error: call of overloaded ?Clamp(double&, double&, double&)? is ambiguous[/code]

I took a look at MathDefs.h and I feel like there are two big improvements that can be made.


[b]1) Use templates[/b]

This:
[code]inline float Clamp(float value, float min, float max)
{
    if (value < min)
        return min;
    else if (value > max)
        return max;
    else
        return value;
}[/code]

should be this:
[code]template <class T>
inline T Clamp(T value, T min, T max)
{
    if (value < min)
        return min;
    else if (value > max)
        return max;
    return value;
}[/code]


[b]2) We should be using std::numeric_limits instead of trying to define our own epsilon, our own infinity etc.[/b]

This:
[code]inline bool Equals(float lhs, float rhs) { return lhs + M_EPSILON >= rhs && lhs - M_EPSILON <= rhs; }[/code]

would be much better as:
[code]template <class T>
bool Equals(T lhs, T rhs) { return lhs + std::numeric_limits<T>::epsilon >= rhs && lhs - std::numeric_limits<T>::epsilon <= rhs; }[/code]

that way these defines can be eliminated:
[code]static const int M_MIN_INT = 0x80000000;
static const int M_MAX_INT = 0x7fffffff;
static const unsigned M_MIN_UNSIGNED = 0x00000000;
static const unsigned M_MAX_UNSIGNED = 0xffffffff;

static const float M_EPSILON = 0.000001f;
static const float M_LARGE_EPSILON = 0.00005f;
static const float M_LARGE_VALUE = 100000000.0f;
static const float M_INFINITY = (float)HUGE_VAL;[/code]

Can I apply these changes and make a PR, or are there objections?

-------------------------

cadaver | 2017-01-02 01:10:28 UTC | #2

Scripting doesn't generally support templates, so if you ensure scripting and platform and compiler compatibility there shouldn't be a problem.

Urho should still compile on VS2008, though it's becoming fairly ancient, but naturally it's better if this PR doesn't become the straw that breaks the camel's back.

-------------------------

TheComet | 2017-01-02 01:10:28 UTC | #3

I created a PR for the changes I mentioned above. The exact changes are detailed in the message there: [url]https://github.com/urho3d/Urho3D/pull/1220[/url]

Please let me know if you disagree with anything.

Shall I go ahead and also templatize the other math classes?

-------------------------

TheComet | 2017-01-02 01:10:28 UTC | #4

I realized it's probably not a good idea to have std::numeric_limits spread everywhere, so I created a template M_LIMITS that wraps std::numeric_limits in MathDefs.h. Using it looks like this:

[code]float infinity = M_LIMITS<float>::Infinity;
double largeEpsilon = M_LIMITS<double>::LargeEpsilon;
int maxInt = M_LIMITS<signed>::Max;[/code]

This also makes the AngelScript bindings much better.

-------------------------

cadaver | 2017-01-02 01:10:31 UTC | #5

Thanks, will look at the PR. I don't recommend templatizing the math classes overall, as the engine is still bound to support only a specific kind of them (e.g. float vectors / matrices), as well as data that is being fed to shaders, Variant to/from serialization, and possibly other things I forgot.

-------------------------

TheComet | 2017-01-02 01:10:31 UTC | #6

Yeah, I noticed how heavily dependent everything is on floats. Would it be worth considering the introduction of a URHO3D_FLOAT that's typedef'd to double/float depending on the build configuration?

-------------------------

cadaver | 2017-01-02 01:10:31 UTC | #7

Not convinced that's a good idea, because usually the reason to do that would be large world support, on the other hand there is a lot of data that is fine being float (double would be a waste of memory), and doubles would need conversion before feeding to the GPU, which would complicate the code.

-------------------------

rku | 2017-01-02 01:13:16 UTC | #8

For my own purposes i turned Vector3 into a template class because i needed Vector3 with 64bit integers that seamlessly integrate with rest of engine parts. It certainly isnt the best or complete implementation but it does what i need. I was wondering if there was interest to have it in engine. Check it out at [github.com/rokups/Urho3D/commit ... 03dcc81a85](https://github.com/rokups/Urho3D/commit/5686901df53804910c4ab32c77f42503dcc81a85)

-------------------------

rku | 2017-01-02 01:13:38 UTC | #9

Shameless bump.

I fixed link in my previous post. It getting broken was probably why noone replied here :wink: So please read my previous post if you havent.

All in all i would love to see all vector classes turned into templates. Now we have IntVector2 and Vector2. However Vector2 has more utility functions than IntVector2 but those functions are valid for both int and float types. I doubt copying them does any good to the codebase. And we all could benefit for vector classes of other data types. So what do you people think?

-------------------------

Stinkfist | 2017-01-02 01:13:40 UTC | #10

Templatized vector and matrix classes would be tricky for script bindings.

-------------------------

cadaver | 2017-01-02 01:13:41 UTC | #11

Practically how it could work, and how I'd accept it would be to have template classes which you can alternatively use for your own purposes, while the engine is locked to Vector3<float>. And to not break the existing API it would be preferable that Vector3<float> was still called Vector3, while the template type would be called something else. Getting rid of separate IntVector2 would be smart if it worked without trouble in practice (though again, to not break API it could still be called IntVector2 through a typedef)

-------------------------

TheComet | 2017-01-02 01:13:44 UTC | #12

[quote="Stinkfist"]Templatized vector and matrix classes would be tricky for script bindings.[/quote]
Yeah I noticed that too when I tried.

-------------------------

