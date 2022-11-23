OvermindDL1 | 2017-01-02 01:01:19 UTC | #1

I whipped up a build dependency graph for Urho3D, took about 48 minutes to compile it and the resultant SVG is *huge* so it takes a minute or two to load in Chrome for example, but if anyone wants it as it is interesting to look at:  [url]http://overminddl1.com/Urho3D/Urho3DBuildDependencyGraph.svg[/url]

Conclusion:  Urho3D has a fairly flat dependency graph, it is beautiful.  :slight_smile:

-------------------------

weitjong | 2017-01-02 01:01:19 UTC | #2

I think I need a bigger screen! :slight_smile:

Could you share how you generate it?

-------------------------

OvermindDL1 | 2017-01-02 01:01:19 UTC | #3

[quote="weitjong"]I think I need a bigger screen! :slight_smile:

Could you share how you generate it?[/quote]
It is Ninja.  Ninja is a replacement build system for makefiles, same task, it is just not for humans to write, it is designed to be generated by machines, like by CMake, and it is extremely fast compared to make with a lot of features from distribution to graph generation.  I have my local Urho3D cmake_gcc.sh file modified to default to "Ninja" instead of "Unix Makefiles" to help my build time and I use a few of its features.  Really wish that "Unix Makefiles" were not hardcoded, though I really wish the sh file was not necessary.  ^.^

[code]
ninja -t graph | dot <whatever args you want>
[/code]

As an example, ninja generates the graph in a couple of seconds, dot/graphviz is what takes forever depending on your settings, and I had mine set fairly high.

-------------------------

weitjong | 2017-01-02 01:01:19 UTC | #4

I am curious about Ninja for quite some time now. Cool stuff. 

[quote="OvermindDL1"]Really wish that "Unix Makefiles" were not hardcoded, though I really wish the sh file was not necessary.[/quote]
I do not see it that way. Our CMake build scripts are not hardcoded to only work with "Unix Makefiles", or otherwise the build scripts would not work with Xcode or VS generator; or that your simple search-and-replace to the cmake_gcc.sh shell script would actually work. The shell script is there just to help to save us to key in a few keystrokes, especially when cross-compiling. On native build, I think one could just type in this manually "cmake -E chdir Build -G your-generator Source" and it should work. However, I believe some of us are even too lazy to type even just that :slight_smile:. And that's where the batch file and shell script come in.

-------------------------

OvermindDL1 | 2017-01-02 01:01:20 UTC | #5

[quote="weitjong"]I am curious about Ninja for quite some time now. Cool stuff. 

[quote="OvermindDL1"]Really wish that "Unix Makefiles" were not hardcoded, though I really wish the sh file was not necessary.[/quote]
I do not see it that way. Our CMake build scripts are not hardcoded to only work with "Unix Makefiles", or otherwise the build scripts would not work with Xcode or VS generator; or that your simple search-and-replace to the cmake_gcc.sh shell script would actually work. The shell script is there just to help to save us to key in a few keystrokes, especially when cross-compiling. On native build, I think one could just type in this manually "cmake -E chdir Build -G your-generator Source" and it should work. However, I believe some of us are even too lazy to type even just that :slight_smile:. And that's where the batch file and shell script come in.[/quote]
Heh, I use either KDevelop (which works well with Urho3D) or Jenkins/gitlab-ci to do it all so I rarely touch things, just the main thing about some vars not being exposed as Options through CMake (been a while since I double checked those though...).

-------------------------

weitjong | 2017-01-02 01:01:20 UTC | #6

We have done some minor refactoring on how we handle the build options not too long ago. Most of the build options (if not all) should be now accounted for. Of course we don't necessarily see all our CMake variables should be exposed as build options.

-------------------------

OvermindDL1 | 2017-01-02 01:01:21 UTC | #7

[quote="weitjong"]We have done some minor refactoring on how we handle the build options not too long ago. Most of the build options (if not all) should be now accounted for. Of course we don't necessarily see all our CMake variables should be exposed as build options.[/quote]
It seems they are all listed now, fantastic, however some of them do not appear at all unless certain others are chosen, like the URHO3D_LUAJIT_AMALG does not appear until URHO3D_LUAJIT is chosen first for example, then regenerated, which makes me have to generate it three times in the IDE, first to get the options, second to select the first set, and third to select the new ones that appear.  Any user-settable options should always be visible even if not used, it is usually good to have a section in the main file that defines all of the options so they will appear, and used where-ever they need to be used just as they already are.  :slight_smile:

-------------------------

weitjong | 2017-01-02 01:01:22 UTC | #8

Well, it depends on who you ask. I personally actually like it this way. Unless you are using LuaJIT then LuaJIT specific options are unavailable. Similarly for Lua. Unless you are targeting Windows platform then OpenGL option is not available, i.e. only on Windows platform one can choose to use D3D9 or OpenGL; in other platforms this option is useless if it were defined (which is exactly why it is not). In short a few build options are purposely designed to be dependent on other build option and CMake variable.

-------------------------

OvermindDL1 | 2017-01-02 01:01:22 UTC | #9

[quote="weitjong"]Well, it depends on who you ask. I personally actually like it this way. Unless you are using LuaJIT then LuaJIT specific options are unavailable. Similarly for Lua. Unless you are targeting Windows platform then OpenGL option is not available, i.e. only on Windows platform one can choose to use D3D9 or OpenGL; in other platforms this option is useless if it were defined (which is exactly why it is not). In short a few build options are purposely designed to be dependent on other build option and CMake variable.[/quote]
Understandable, it just breaks the GUI's is all so it is not as clean, but understandable.  :slight_smile:

-------------------------
