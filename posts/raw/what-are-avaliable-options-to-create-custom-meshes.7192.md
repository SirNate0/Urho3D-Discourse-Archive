Kest | 2022-02-11 21:27:42 UTC | #1

Hi everyone,

So I have a custom mesh file format that is not natively supported by Assimp or any other importer. Leading me to write my own importer. My question is what options do I have to create meshes? So far I've looked into CustomGeometry, but doesn't seem like you can edit/add indices. Anyone got any ideas?

Thanks!

-------------------------

Eugene | 2022-02-11 21:57:54 UTC | #2

Nothing really stops you from filling `Model` from scratch on your own.
I would have shared a code that I personally use, but it would be easier for you to write your own specialized loader, than to learn and port the generic solution.

-------------------------

Kest | 2022-02-11 22:17:29 UTC | #3

Oh okay, thank you for the idea. I just started using this engine so any option is appreciated.

-------------------------

Lys0gen | 2022-02-12 01:12:56 UTC | #4

Sample 34 shows you how to build a model from indices.

-------------------------

