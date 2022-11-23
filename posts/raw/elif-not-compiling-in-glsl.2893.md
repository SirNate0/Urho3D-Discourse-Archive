Bananaft | 2017-03-13 20:33:51 UTC | #1

So i have:

    #ifdef PARAM_1

    #elif PARAM_2

    #else

    #endif
I'm getting compile error: "Syntax error in #if" as soon as I'm setting PARAM_2
But this:

    #ifdef PARAM_1

    #else
    #ifdef PARAM_2

    #else

    #endif
    #endif
works fine with no errors.

Is it a bug? Or just something Urho does or does not?

I'd like to have #elif to work, because I going to have many such params.

-------------------------

1vanK | 2017-03-21 20:17:31 UTC | #2

try #elif defined(...)

p.s. #ifdef is equivalent to #if defined (not just #if), so #elif can not be part of #ifdef ... #endif

-------------------------

