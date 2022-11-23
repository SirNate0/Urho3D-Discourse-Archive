slapin | 2017-05-24 17:10:49 UTC | #1

To: @cadaver, @weitjong  
Cc: @Modanung 

I need K-D tree for my project to find nearest members, it is needed as abstraction, not attached to spatial system.
I need it to generate some things, also for building of AI influence maps.

I was pointed to a project
https://github.com/jlblancoc/nanoflann

Which does have compatible license, or I can implement my own (which will take 10 times more
but still possible). Will it be acceptable for inclusion in Urho?

It will be abstract thing in terms of Spline, so just standalone data object usable for everything.
It is not something which can be done quickly, so I ask.
If not accepted I still can use it locally, but having Urho object would make it more easily accessible
to others.

-------------------------

cadaver | 2017-05-26 08:22:15 UTC | #2

If you implement an Urho class (or classes) that hide the library and allow interacting with it with Urho math types and it's usable from script, then it would certainly sound worthwhile and would be accepted. And if I understood right that the library itself is only a single header without other dependencies.

-------------------------

