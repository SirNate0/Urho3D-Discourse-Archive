rku | 2019-07-24 12:08:37 UTC | #1

Some of you may be aware that @Eugene put together [Urho3D.natvis](https://github.com/eugeneko/Urho3D-Debug/blob/master/Urho3D.natvis). It works on visual studio, but not on Linux.

Today i released my new project - [natvis4gdb](https://github.com/rokups/natvis4gdb). It is still quite limited, but already useful. Viewing strings and arrays is working. Now you can use your windows natvis files on linux.

-------------------------

Miegamicis | 2019-07-25 08:02:59 UTC | #3

~~Stop spamming nonsense, it's that easy.~~

Regarding the actual topic - cool stuff. Btw does this work with CLion once the gdb is set up?

-------------------------

Modanung | 2019-07-24 14:32:38 UTC | #4

2 posts were split to a new topic: [About Leith and others](/t/about-leith-and-others/5338)

-------------------------

rku | 2019-07-24 14:19:16 UTC | #5

Yes it does. I did not find automatic per-project way to set it up so what i do is modify my `~/.gdbinit` and add `add-natvis /full/path/to/Urho3D.natvis`.

-------------------------

