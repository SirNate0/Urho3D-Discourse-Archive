Sunc | 2022-08-18 13:41:49 UTC | #1

It seems treating this platform as android and failed building with lots of error messages, since the M1 is an arm based CPU.

-------------------------

SirNate0 | 2022-08-18 17:28:44 UTC | #2

What are the error messages, especially the earliest ones? I don't have a Mac, and I'm not sure others here do, at least an M1 based one, so I think we'll need more details to be able to help you.

-------------------------

Sunc | 2022-08-19 14:57:34 UTC | #3

The problem get solved when I try the new 1.8 tag version, building target to My Mac(Rosetta). With the only issue about macro "DEBUG_ASSERT" at civetweb.c, which calls the c lib function "exit" without including stdlib.h at a leading place, do it or just comment the calling segment both working.

-------------------------

