spwork | 2018-02-21 14:06:43 UTC | #1

I 'm newer programming with linux,i use cmake and make compile Urho3d sample, it generate a lot of file,such as 01_Hello World.
but the filetype of 01_Hello World is `ELF 64-bit LSB shared object`,
how can i generate a 01_Hello World the type is `ELF 64-bit LSB executable`

-------------------------

weitjong | 2018-02-21 17:11:56 UTC | #2

Nuke your build tree and regenerate it again. What you have described does not make any sense and could possibly only happened because at some point you have mixed the build tree with Android build configuration.

If you have Ruby/Rake installed, you can regenerate and rebuild everything with one liner. ^_^

```$ rake cmake && rake make```

-------------------------

