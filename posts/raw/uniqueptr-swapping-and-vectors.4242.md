TheTophatDemon | 2018-05-19 17:25:24 UTC | #1

When compiling my project with Visual Studio 2015 (64-bit, project configured for C++11) I discovered some
errors when working with UniquePtrs. I am using Urho3D 1.7.

Firstly, attempting to swap two UniquePtrs like so:
```C++
UniquePtr<Thing> thing;
thing.Reset(new Thing());
UniquePtr<Thing> thing2;
thing.Swap(thing2);
```
Produces this error: 
```'Urho3D::UniquePtr<Thing>::Swap': function does not take 2 arguments	UrhoTest	c:\users\andso\desktop\tools\urho3d-1.6-binaries\include\urho3d\Container\Ptr.h	598	```
(I know the folder says it's version 1.6, but it's 1.7. I did not wish to bother changing all of the environment variables just to rename it)

With "Thing" being a simple class defined like so:
```C++
class Thing 
{
public:
	int diddly = 0;
};
```

Secondly, I find that making a Urho3D::Vector of UniquePtrs does not work. I suspect this may be an intentional design tradeoff but I am unsure. My code looks like this:
```C++
UniquePtr<Thing> thing;
thing.Reset(new Thing());
...
Vector<UniquePtr<Thing>> things = Vector<UniquePtr<Thing>>();
things.Push(thing); //From my understanding, move semantics will transfer ownership from "thing" to the vector
```
And the following error is produced:

```'Urho3D::UniquePtr<Thing>::operator =': cannot access private member declared in class 'Urho3D::UniquePtr<Thing>'	UrhoTest	c:\users\andso\desktop\tools\urho3d-1.6-binaries\include\urho3d\Container\Vector.h	526	```

I have isolated these two issues into their own Urho3D project that I have uploaded [here](https://drive.google.com/file/d/1850F6ZHvh99d5WO1Zmdf-aRqY0-lncgl/view?usp=sharing).
(Because the project I'm working on is much too large)

These issues are not urgent; I merely felt that I should report the problem.

-------------------------

S.L.C | 2018-05-20 14:44:00 UTC | #2

Despite the fact that the engine switched to c++11, that does not really mean what you think it means. So far it just means you can safely use c++11 code in your pull request and not be rejected because of that.

Other than slapping a bunch of `noexcept`, default initializatiom, auto deduction, range loops and the use of `std::function` in the event system. Not much was done to actually use c++11. And everything I mentioned was done automatically via tooling.

Neither `UniquePtr`, nor `Vector` implement move semantics. I believe I saw a WIP pull request from @Eugene attempting something like that https://github.com/urho3d/Urho3D/pull/2310 And another abandoned one from another user https://github.com/urho3d/Urho3D/pull/2274

Move semantics can be a little tricky if you build the engine as a DLL. Not sure how that plays out. Last time I checked, sharing memory across DLLs was not the best of idea. But maybe that's limited to just the standard library. TBH, I haven't studied much in that area to say for sure.

So yeah, that `cannot access private member declared in class ` error message was probably due to the fact that `UniquePtr` does not implement move semantics and since it cannot be copied, the copy constructor and assignment operators were declared as private. At least now they're deleted and the error message will be more clear if you attempt the same with a master version of the code https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Container/Ptr.h#L531


And also, this might not true:
```cpp
UniquePtr<Thing> thing;
thing.Reset(new Thing());
...
Vector<UniquePtr<Thing>> things = Vector<UniquePtr<Thing>>();
things.Push(thing); //From my understanding, move semantics will transfer ownership from "thing" to the vector
```
  Because `thing` is an lvalue, and unless the compiler tries to be smart (_or dumb if you think about it_), it shouldn't try to move that lvalue unless explicitly specified. Like this:
```cpp
things.Push(std::move(thing));
```
What if you want to use `thing` after you push it into the vector and expect move semantics to occur? Isn't `thing` left in an unusable state after a move has taken place? If it was done correctly, ofc.

As for that first error `function does not take 2 arguments`. I believe you've either omitted some details, the compiler wen't crazy somehow or is just bad at reporting errors. Because it does not make sense in that context. Unless we talk about the `Urho::Swap` function used in the `Swap` method. Which is the only thing that comes to my mind when I see that error.

I need to look at older code and see if something changed. Because that error message doesn't make any sense with the code in the master.

**EDIT**: I think I've found the culprit of that weird `Swap` error message: https://github.com/urho3d/Urho3D/commit/b84239a3aeb2cbf9b04875d73ee47adfecb704f0#diff-4bb46169126ea0f8ac2273a595c59207

That happened after the 1.7 release. If that's what you're using. I honestly recommend the master version. You're missing out on a lot of fixes.

-------------------------

Eugene | 2018-05-20 12:21:12 UTC | #3

[quote="TheTophatDemon, post:1, topic:4242"]
Secondly, I find that making a Urho3D::Vector of UniquePtrs does not work
[/quote]
This really annoyed me too. 
The fix is ready, I just don’t have time to finish and merge my PR.

-------------------------

TheTophatDemon | 2018-05-20 14:42:25 UTC | #4

Oh, alright. Thank you.

-------------------------

