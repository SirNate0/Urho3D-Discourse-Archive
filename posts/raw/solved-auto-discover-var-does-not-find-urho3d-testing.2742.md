ricab | 2017-02-05 17:55:50 UTC | #1

Hello,

I am trying to setup a project using Urho3D, built from source (tag 1.6) in a linux environment. I am having trouble reusing Urho's cmake macros for testing. 

I see that URHO3D_TESTING needs to be defined for test support, but when I try to build my project with this option, I get the following warning, despite having built urho with the same option: "conflicting URHO3D_TESTING build option is ignored."

The "AUTO_DISCOVER_VAR" mechanism in FindUrho3d.cmake does not find it and after some cmake debugging I found that, indeed, the output of CheckUrho3DLibrary.cpp does not include the define, even though the option was taken into account when building urho (I can run urho's tests with make test).

My search in the forums and issues did not yield much, only [this thread](http://discourse.urho3d.io/t/cmake-variable-urho3d-testing/1689) from a year ago mentioning the intention to discover the variable automatic. So, even though I am new to both Urho and CMake, I wonder if this is a bug that could have gone unnoticed so far?

BTW, sorry if you are reading this twice: I also asked pretty much the same in gitter, but did not get any replies and only now found the time to sign up to the forums and post here.

Cheers,
Ricardo

-------------------------

weitjong | 2017-01-24 15:57:25 UTC | #2

This part of the script hasn't changed much since then. All I can say is, it works. The logic of auto-discovering the variables, especially the URHO3D_TESTING, is being tested in CI build. So, if it didn't work for you then it probably means your build tree might have been using a different Urho3D library than the one you believe you are.

The whole thing about finding Urho3D library is a little brittle, but that's the best we can do considering we need to make it work on the ancient CMake 2.8.7. There is an attempt to upgrade our build scripts to use a more modern CMake version in one of our development branch, although its development has stale somewhat lately. Expect things would be different when that branch sees the light of day.

-------------------------

ricab | 2017-01-24 17:47:05 UTC | #3

Thanks for the reply weitjong. The right Urho3D library is being found, but I investigated some more and the problem only happens when I have ccache enabled. After rebuilding with ccache disabled, the define is then correctly picked up. Does this make sense to you?

This worries me: I would have hoped ccache would see the new define and do new compilations as needed. Strangely, I could not find URHO3D_TESTING in any of the compilation commands during the build. How is this variable baked into the library?

-------------------------

weitjong | 2017-01-25 11:23:21 UTC | #4

Yeah, it makes sense to me although it is totally unexpected. I would never have thought of that, so thank you for bringing this up. The issue is not with ccache being unreliable, it is because our detection mechanism relies on the runtime output of a probe executable which ccache helped to build quicker but it couldn't possibly know the function output is mutating during runtime. 

The variables are baked as compiler defines in the export header, Urho3D.h, during library-building time. Those variables are auto-discovered again during library-using time in your own project by detecting which defines are there in the export header. I hope this clarifies. There are in fact two ways how this is being carried out. One by using runtime output (native build) and one by parsing the export header file directly (cross-compiling build). Perhaps we can simplify it to always use the second way even for native build.

-------------------------

ricab | 2017-01-25 18:33:33 UTC | #5

Another option would be to somehow force ccache to do the required compilation fully (there must be a way to do that.)

BTW, if anyone is interested, a quick way to disable ccache is to set the environment variable CCACHE_DISABLE=1.

-------------------------

weitjong | 2017-01-26 01:28:20 UTC | #6

As you aware all our build is configured to execute from a single parent process. So, it may not be as easy to disable ccache in the sub process via environment variable. Otherwise, I agree it is another option.

-------------------------

ricab | 2017-01-26 16:04:33 UTC | #7

Sorry, I was not clear enough. I suggested disabling ccache merely as a workaround for other people that face the same issue, not as an actual fix.

For a proper fix, I "guessed" there must be a way to make ccache redo the required compilation, but am not very familiar with ccache so I am not sure how exactly. Perhaps touching some file so that ccache sees a more recent date?

-------------------------

weitjong | 2017-02-06 13:48:47 UTC | #8

The problem ```ccache``` interfering with ```try_run``` should be fixed after the commit mentioned in the [#1796](https://github.com/urho3d/Urho3D/issues/1796) is merged to master branch.

-------------------------

ricab | 2017-02-05 17:55:01 UTC | #9

Good to know. I haven't tried it yet, but I am marking it solved since it could at least be overcome by disabling ccache.

-------------------------

