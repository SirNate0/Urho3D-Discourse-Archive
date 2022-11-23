SeeSoftware | 2018-04-18 21:52:09 UTC | #1

I only looked at PodVector and Vector but im seeing that operator[] uses a unsigned (assumed int) instead of a size_t wich could limit the maximum index to 0xFFFFFFFF even if you compile for x64. Is that a oversight ?

-------------------------

weitjong | 2018-04-19 10:10:26 UTC | #2

I am not the original author of the code. If I have to guess a reason, I would say it is done for portability. Urho3D is a cross-platform engine supporting both 32 and 64 bit architecture. The “unsigned” data type is the same in any platforms that Urho3D supports.

-------------------------

Eugene | 2018-04-19 10:35:47 UTC | #3

[quote="SeeSoftware, post:1, topic:4187"]
im seeing that operator[] uses a unsigned (assumed int) instead of a size_t wich could limit the maximum index to 0xFFFFFFFF even if you compile for x64. Is that a oversight ?
[/quote]
AFAIK it was intentional decision
1) To keep things the same on x86 and x64 as far as it's possible.
2) To use as few integer types in codebase as possible.

size_t is viral: once you use it in one place, you have to either use it in many places or cast away high part of 64-bit integer. Both ways are nasty.

-------------------------

S.L.C | 2018-04-19 15:37:57 UTC | #4

I'm guessing that everyone assumed you wont be using a vector or string bigger than 4gb. This is a game engine, not a general purpose library. Here you have to be reasonable about this particular usage of the library and not in general. If your game does need that then you're doing something wrong and need to look for another solution.

And I have to agree that`size_t ` is not for everyone.

-------------------------

