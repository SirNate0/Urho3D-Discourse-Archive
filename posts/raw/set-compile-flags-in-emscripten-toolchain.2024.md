godan | 2017-01-02 01:12:21 UTC | #1

How can I pass an Emscripten compile flag to the toolchain? Specifically, I need to change use:
[code]-s ALLOW_MEMORY_GROWTH=1[/code]
or one of the settings that adjust the total allowable memory. As a note, the default memory limit for a web build is way too low.

I'm foggy (at best) on how the whole Emscripten toolchain thing works, so any help is most appreciated!

-------------------------

weitjong | 2017-01-02 01:12:21 UTC | #2

Use the build option to control this compiler flag. See [urho3d.github.io/documentation/H ... ld_Options](http://urho3d.github.io/documentation/HEAD/_building.html#Build_Options) for more detail. Scroll to those options prefixed by "EMSCRIPTEN_".

-------------------------

godan | 2017-01-02 01:12:23 UTC | #3

doh!

-------------------------

