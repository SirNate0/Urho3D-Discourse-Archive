graveman82 | 2020-09-13 09:35:16 UTC | #1

Hi! I found some confusing place in Urho3D1.7 Vector.h:
    > /// Move a range of elements within the vector.
>     void MoveRange(unsigned dest, unsigned src, unsigned count)
>     {
>         T* buffer = Buffer();
>         if (src < dest)
>         {
>             for (unsigned i = count - 1; i < count; --i) // THIS IS VERY STRANGE CODE
>                 buffer[dest + i] = buffer[src + i];
>         }
>         if (src > dest)
>         {
>             for (unsigned i = 0; i < count; ++i)
>                 buffer[dest + i] = buffer[src + i];
>         }
>     }
shouldn't it be **"for (unsigned i = count - 1; i > 0; --i)"**?

-------------------------

Modanung | 2020-09-13 19:26:20 UTC | #2

1.7 is getting old and this code has been [reformulated](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Container/Vector.h#L1163) in the meantime:

```
/// Move a range of elements within the vector.
void MoveRange(unsigned dest, unsigned src, unsigned count)
{
    if (count)
        memmove(Buffer() + dest, Buffer() + src, count * sizeof(T));
}
```
...and welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

graveman82 | 2020-09-13 10:05:46 UTC | #3

I am too lazy to build new version

-------------------------

Modanung | 2020-09-13 18:36:15 UTC | #4

Can't help with that. :slightly_smiling_face:

Though the scripts included with the engine make it a breeze, once the dependencies are installed.

-------------------------

Eugene | 2020-09-13 11:08:46 UTC | #5

[quote="graveman82, post:1, topic:6389"]
shouldn’t it be **“for (unsigned i = count - 1; i > 0; --i)”** ?
[/quote]
0 has to be included as well, so your code is incorrect.

-------------------------

1vanK | 2020-09-13 19:23:19 UTC | #6

[quote="graveman82, post:1, topic:6389"]
shouldn’t it be **“for (unsigned i = count - 1; i > 0; --i)”** ?
[/quote]

usigned always >= 0, old code is correct because overflow occurs and the cycle ends

-------------------------

graveman82 | 2020-09-14 07:17:45 UTC | #7

Ou, that's very original approach, thank's!

-------------------------

graveman82 | 2020-09-14 07:18:42 UTC | #8

You are right, damn, I didn't noticed that

-------------------------

