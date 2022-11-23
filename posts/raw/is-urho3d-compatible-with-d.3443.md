LiamM32 | 2017-08-13 22:25:32 UTC | #1

D is a language that aims to be a successor to C++, and I know it's much cleaner than it.  I haven't used it myself though, as I haven't had a project to work on with D.

I know that D is compatible with some but not all C++ libraries.  So is it compatible with Urho3D.  Is it possible for the entire game project to be written in D?

-------------------------

Eugene | 2017-08-13 23:05:34 UTC | #2

No, unless someone is ready to do huge amount of porting work.

-------------------------

slapin | 2017-08-13 23:29:58 UTC | #3

If anybidy cares at all.

If the interest is not pure academic, there were some discussions on web
aboiut interoperability of C++ and D and it is heavily compiler-dependent now.
gcc-7.x adopts D compiler, so there is some chance that if your code is built using gcc.
But I would not get high hopes. Also there is always Qt path - you can implement pure C binding
and use that from D (or anywhere like Python and other languages).

-------------------------

LiamM32 | 2017-08-16 18:45:16 UTC | #4

The interest is not pure academic.  I would actually want to write my game in D if I could.  But I don't think I will as making the binding appears to be more complicated than just writing it in C++.

Isn't the GDC compiler fairly new?  LLVM has a D compiler.  Is Urho3D compatible with LLVM?

It would be nice though if someone ported Urho3D to D.  Yes it would take some work, but compared to writing a new game engine?  If someone did, they should not bother with some features like Direct3D.

-------------------------

TheComet | 2017-08-16 19:20:26 UTC | #5

It might be possible to auto generate the majority of the bindings. (http://www.swig.org)

If you port Urho3D to D then you'll be facing the same issue you're facing now, only much larger: There are no D bindings for all of the thirdparty libraries used by Urho3D.

-------------------------

kostik1337 | 2017-08-17 17:04:47 UTC | #6

AFAIK, D is compatible with C++ in terms that you can use C++ classes, which are stored in linked library, so you can build Urho3D as .so/.a library and just link it with your D code, of course, you should somehow provide interface of Urho3D classes and methods in D, isn't that right?

-------------------------

