miz | 2017-02-14 19:15:59 UTC | #1

I'm trying to solve keyboard issues on the RPi, more info here:
http://discourse.urho3d.io/t/keyboard-keys-not-working-on-rpi-platform/2335

One approach I'm trying is to use RetroPie's SDL mirror instead of the SDL files Urho3d comes with. (They had similar issues by the looks of things and changed SDL source a bit)

What I've tried so far is replacing the SDL src and include folders and trying to build Urho3d as one would normally. 

I'm getting to [77%] stage (SDL builds) then I get loads of errors like:

`undefined reference to 'SDL_ShowSimpleMessageBox'`

So I did an:

`nm libSDL.a > funcsDefined.txt` 

to see if the functions that have undefined references are there. They were there (some with the suffix _REAL, not sure what that means?)

Any ideas what avenues I could explore to fix this? I've been pulling my hair out for 2 days :(

-------------------------

jmiller | 2017-02-15 00:10:02 UTC | #2

[quote="miz, post:1, topic:2795"]
_REAL
[/quote]
Related? http://stackoverflow.com/questions/30722266/sdl2-linker-errors-with-real

-------------------------

miz | 2017-02-15 11:38:11 UTC | #3

I think it isn't finding the libSDL.a correctly. When move/rename it I get the same errors

-------------------------

jmiller | 2017-02-16 02:43:34 UTC | #4

For me, Urho builds libSDL in $BUILD_TREE/Source/ThirdParty/SDL and finds it there (via $URHO3D_HOME set to build tree, building git version and not SDK).

Perhaps the Urho cmake cache and logs in the various CMakeFiles directories in your build tree will provide some clues.

-------------------------

miz | 2017-02-16 11:57:36 UTC | #5

I've definitely got it building in the right place -  $BUILD_TREE/Source/ThirdParty/SDL and have URHO3D_HOME set to the build tree. Do you know specifically where I can see where it is looking for it?

-------------------------

miz | 2017-02-16 12:13:52 UTC | #6

Does libSDL get bundled in with libUrho3D somehow? Could it be that It's not getting bundled in right?

-------------------------

miz | 2017-02-16 14:57:25 UTC | #7

Actually I was not paying enough attention to my nm output! Although the functions are present in the libSDL.a and libUrho3D.a they have a U next to them indicating they are undefined. Any ideas how this has happened?

-------------------------

jmiller | 2017-02-16 15:52:45 UTC | #8

If Urho properly built SDL before, it seems any errors must be 'caused' by the swapping of source files, correct?
Missing symbols can happen from differing build flags, so perhaps compare the cmake outputs (cmake VERBOSE=1 for more) in case something happens there?

-------------------------

weitjong | 2017-02-17 11:16:37 UTC | #9

Note that the Urho3D maintains its own fork of SDL repo, which contains the locally modified code changes. Replacing that with external sources wholesale is guaranteed to faill and not supported by us.

-------------------------

miz | 2017-02-17 14:45:24 UTC | #10

I think I'm giving up and going back to 1.5 but thanks for the help :slight_smile:

-------------------------

jmiller | 2017-02-17 21:28:22 UTC | #11

One more thing, potentially useful is the ability of github (and other tools) to compare/diff across forks.

-------------------------

weitjong | 2017-02-18 01:16:18 UTC | #12

Not sure I understand you completely, but anyway, our fork repo is [here](https://github.com/urho3d/SDL-mirror). We use a "moving" branch in the fork as the subtree for "Source/ThirdParty/SDL" in Urho3D master repo. The moving branch not only tracks the upstream commits from SDL developer, but also the local commits made by us on top of the original SDL. Currently that moving branch is "release-2.0.5-modified-for-urho3d". I hope that clarifies.

-------------------------

