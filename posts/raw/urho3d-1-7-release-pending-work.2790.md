cadaver | 2017-02-13 15:16:06 UTC | #1

The topic of a new stable release came up in the C++11 topic http://discourse.urho3d.io/t/moving-to-c-11/2788

For core devs: please list here all the pending work you'd like to complete before it.

JSandusky has some upcoming PR work that would include large changes (RakNet, compute support) so it'd be better to get this release out before merging those.

For me: I'd like to complete the pending library updates (Assimp, libcpuid), nothing else at least at this point.

-------------------------

sabotage3d | 2017-02-13 18:42:41 UTC | #2

Would it be possible to have refactor-buildsystem merged in the main branch for the 1.7 release? I think the Android build-system improvements addressing these issues: https://github.com/urho3d/Urho3D/issues/1441 are working quite well.

-------------------------

cadaver | 2017-02-13 19:00:45 UTC | #3

Just a note: though my list is exceedingly small and practically completable within days, I don't mean that the release would need to be imminent, at all, but that we start moving toward it.

-------------------------

Eugene | 2017-02-13 20:07:50 UTC | #4

[quote="sabotage3d, post:2, topic:2790"]
Would it be possible to have refactor-buildsystem merged in the main branch for the 1.7 release?
[/quote]
I think this is mandatory per-condition of moving to C++11, according to
https://github.com/urho3d/Urho3D/pull/1818#issuecomment-279365537

-------------------------

cadaver | 2017-02-15 09:23:26 UTC | #5

@weitjong Do you think refactor-buildsystem could make it in this time in some kind of timeframe? Or if it's too much work total still, maybe a cherry-pick of the Android toolchain changes + CI changes (and anything else which is nice to have and doesn't wreak havoc)

-------------------------

weitjong | 2017-02-15 11:26:00 UTC | #6

The commits that could be cherry-picked have already been picked in the last release. What left  there have dependency on each other and should go in together. So, the question is, how much time it needs to get "completed"? That depends on how we define the complete. I have a few things in mind actually but have no time/commitment to carry them out. The good news is, that branch is always in compilable state. So, I could also say I don't have any more plan and the branch is merge-ready after I have done a simple rebase tonight.

-------------------------

weitjong | 2017-02-15 11:43:11 UTC | #7

We should probably fix the keyboard problem on the RPI platform before making a new release.

-------------------------

cadaver | 2017-02-15 12:08:51 UTC | #8

Regarding the branch, that sounds good. I'll let you be the final judge, but I'd vouch for merging it then.

I also hope to solve the constraint2D load/save issue.

-------------------------

weitjong | 2017-02-15 13:33:54 UTC | #9

One thing to note though. The new Android toolchain has Android NDK r12b as the *minimum* requirement and it uses Clang compiler toolchain by default. But I think we have waited long enough. It is not a bleeding edge version anymore.

-------------------------

cadaver | 2017-02-15 14:14:49 UTC | #10

Sounds reasonable. With NDKs, the worse problem is a new version appearing (while download of old is well hidden) and our build no longer working :) Can give a test-spin of a Windows/Android compile of the branch, hopefully tonight.

-------------------------

cadaver | 2017-02-16 08:49:45 UTC | #11

Current status for me on Windows: merging the buildsystem branch, installing NDK13b and running cmake_android resulted in the NDK's Clang erroring on not finding various C++ headers, while it was building the Urho PCH.

In file included from D:/Lasse/Programs/urho3d-clean2/Source/Urho3D/Precompiled.
h:28:
In file included from D:/Lasse/Programs/urho3d-clean2/Source/Urho3D/Container/Ha
shMap.h:25:
In file included from D:/Lasse/Programs/urho3d-clean2/Source/Urho3D/Container/..
/Container/HashBase.h:32:
D:/Lasse/Programs/urho3d-clean2/Source/Urho3D/Container/../Container/Hash.h:25:1
0: fatal error: 'cstddef' file not found

-------------------------

weitjong | 2017-02-16 01:09:06 UTC | #12

I have not tested it on a Windows host yet. I will try upgrade to 13b in one of the Linux VM to see if the error can be reproduced there. And if so, then it is caused by newer NDK, which I believe has dropped GCC compiler toolchain all together. Our CMake/Android toolchain file still relies on the legacy GCC bits to be around, although it uses Clang already. Will check later tonight and report back.

-------------------------

weitjong | 2017-02-16 17:09:11 UTC | #13

I had problem also with NDK 13b on Linux host system, although my build error was at an earlier stage. The problem was caused by NDK 13b changing the internal structure slightly for LLVM libC++ STL runtime. I will check in my tweak shortly. It builds fine afterwards on both NDK 12b and 13b. I didn't test on Windows host though.

-------------------------

cadaver | 2017-02-17 13:05:22 UTC | #14

Thanks! Will be sure to re-check then.

-------------------------

weitjong | 2017-02-17 17:32:19 UTC | #15

The keyboard input problem on the RPI platform is now fixed in master branch. It was SDL bug all along.

-------------------------

Eugene | 2017-02-27 11:01:35 UTC | #16

I want to finish work on my PR before 1.7
I'm going to close this PR when I ensure that dynamic resource path changing works correctly.
https://github.com/urho3d/Urho3D/pull/1832

-------------------------

weitjong | 2017-03-04 11:45:05 UTC | #17

If there are no objections, by end of today or may be tomorrow the "refactoring-buildystem" will be merged into master branch.

-------------------------

cadaver | 2017-03-04 18:40:10 UTC | #18

Great! I compiled the refactor branch now successfully on Windows / Android after installing NDK14. On NDK13b I got the earlier discussed va_args error from Clang while compiling. But since the newest works, I have no objections.

-------------------------

slapin | 2017-03-04 19:09:38 UTC | #19

Sorry for offtopic question but will latest NDK14 work on Android-4.0 ICS?

-------------------------

cadaver | 2017-05-03 07:55:11 UTC | #20

Ok.. It's been a while. IK is in, RaycastVehicle is in. The Nuklear PR is still ongoing and will take some weeks, but don't think we have to wait for that, as it's kind of outside the "norm" for Urho features anyway, ie. no script support, and not completely flexible regarding resources.

There is the Retina Sierra fullscreen issue ( https://github.com/urho3d/Urho3D/issues/1917 ) which is kind of a bummer, but I don't foresee at least myself having time to properly investigate it until mid-summer. There's also a smaller Retina UI bug which makes UI textures bleed from the adjacent shapes, since the UI spritesheet does not have padding, but that's easily fixable either by adjusting the trouble shape UV's, or switching to nearest filtering.

So, might as well move on with the release by starting to compile the changelog. Any objections?

-------------------------

Eugene | 2017-05-03 09:29:27 UTC | #21

I'd like to push few minor things today. No objections.

-------------------------

godan | 2017-05-03 13:36:08 UTC | #22

Also, just FYI - I was starting to create the PR for webGL compatible PBR. However, from what I can tell, the changes I made are actually already in the shader source. So, although I haven't tested, I am pretty sure that webGL PBR should work with no further changes. (I generally work from a forked repo, so I'm not always up to date with the master branch).

I will try to verify this claim today.

Some notes:
- I use ForwardDepth renderpath
- Must use square (?), powers of two textures.

-------------------------

cadaver | 2017-05-03 19:08:40 UTC | #23

Cool, make a PR if necessary, if there are minor shader changes needed they should be quick to verify.

-------------------------

TheComet | 2017-05-03 20:57:39 UTC | #24

I'd like to get some of the bugfixes I've made for IK support into master for 1.7 (there's stack corruption being caused by the angelscript bindings [fixed], a segfault occurs when cutting and pasting a node with effectors in the editor [not fixed], a segfault occurs when changing the algorithm [fixed]).

I'll work on getting a PR together for this.

-------------------------

Sinoid | 2017-05-04 02:04:49 UTC | #25

Awesome. Just as I'm wrapping up with multi-channel audio and compute/API-hell.

-------------------------

cadaver | 2017-05-04 10:25:17 UTC | #26

Thanks, that sounds good to get in. Each platform manual tests & compiling the changelog will take some time (over the weekend, likely) in any case.

-------------------------

weitjong | 2017-05-05 01:55:22 UTC | #27

Hope to spend some time tonight to provide "glue" JS for the MODULE lib type so that the web samples with our default HTML shell run out of the box.

-------------------------

Lumak | 2017-05-06 22:12:25 UTC | #28

Are you going to investigate the bug that @Enhex discovered before the 1.7 release?
[quote="Enhex, post:12, topic:3063, full:true"]
Running sample 04 with -deferred also allocates and removes the same screen buffers several times:
https://pastebin.com/URHmY90Q

I think there's also a bug that the new graphics::monitor_ never initialized or assigned by Urho. You can see its value in the log is -842150451.
[/quote]

[quote="Enhex, post:16, topic:3063, full:true"]
In the end it turns out users were running out of GPU RAM.
[/quote]

-------------------------

Enhex | 2017-05-06 22:33:44 UTC | #29

It was my fault, the reason was using too much GPU RAM.
I have more GPU RAM than the users that had the freezes so I couldn't reproduce it, and couldn't see it in the profiling tools because they don't include GPU stuff.

-------------------------

sabotage3d | 2017-05-06 23:58:21 UTC | #30

Can anyone else confirming this bug: https://github.com/urho3d/Urho3D/issues/1860? It is super annoying as it wasn't happening before. When the window opens if I press with the mouse I cannot get any events, If I loose focus and click on something else and then again on the Urho3D window I am getting events.

-------------------------

weitjong | 2017-05-13 15:11:33 UTC | #31

I encountered a blocker <s>(a bug from Emscripten) and will submit a PR to fix the bug first</s>. In other words, don't wait for me for the release.

EDIT: after going through their change history, I now think the current Emscripten behavior is as per their design on how the main/side module should work. Thus, the problem is on our side.

-------------------------

cadaver | 2017-05-07 17:22:34 UTC | #32

I switched machine to another Sierra Mac in the meanwhile, I think I've seen the cursor staying visible for some time in the beginning, but not missed events. Will still retest before release. Is your application using visible cursor, or a locked invisible cursor (like NinjaSnowWar)?

-------------------------

sabotage3d | 2017-05-07 18:39:01 UTC | #33

I have mouse visible to true. I also have touch emulation enabled.
`GetSubsystem<Input>()->SetMouseVisible(true);` 
`GetSubsystem<Input>()->SetTouchEmulation(true);`
These are the events I am using:
E_TOUCHMOVE, E_TOUCHBEGIN, E_TOUCHEND.
I only happens in window mode these are my settings:
`engineParameters_["FullScreen"] = false;
engineParameters_["WindowWidth"] = 1200/2;
engineParameters_["WindowHeight"] = 1920/2;`

-------------------------

cadaver | 2017-05-13 11:55:10 UTC | #34

@TheComet how is it going with the IK fixes, any ETA? I still need to compile the changelog and I've had minimal free time lately, so no absolute hurry.

-------------------------

TheComet | 2017-05-13 16:48:10 UTC | #35

It's about 40% done. I've been super busy with exam hell lately, sorry it's taking this long. I think I should be able to get it to you by next Weekend if that's alright.

-------------------------

cadaver | 2017-05-13 20:13:41 UTC | #36

No problem, that sounds good.

-------------------------

weitjong | 2017-05-21 01:01:36 UTC | #37

I have solved my blocker issue. The web samples with MODULE lib type for Web platform now built and run out of the box on my test environment. Still not super happy about it because I have to disable the dead-code-elimination on the main module in order to preserve the "exported symbols". Tomorrow will try to re-enable the DCE on the main module and passing the exported functions (with mangle names) explicitly to Emscripten, if it is even possible.

-------------------------

weitjong | 2017-05-21 13:12:03 UTC | #38

The EXPORTED_FUNCTIONS setting from Emscripten does not work with C++ mangled symbol names. Similarly, the EMSCRIPTEN_KEEPALIVE attribute only works for C functions and not for C++ type. If only we could tell Emscripten to automatically keep all the symbols that we have tagged with URHO3D_API attribute, that would solve the problem. Unfortunately for that, we have to go deeper into Emscripten itself. Perhaps another time then. I have just merged the feature branch into master and call it a day.

-------------------------

Eugene | 2017-05-29 08:59:15 UTC | #39

I want to investigate this one a bit before 1.7

https://github.com/urho3d/Urho3D/issues/1958

-------------------------

ricab | 2017-05-30 13:13:00 UTC | #40

Please note also [issue #1960](https://github.com/urho3d/Urho3D/issues/1960), for which I submitted a pull request.

-------------------------

weitjong | 2017-05-31 09:32:46 UTC | #41

I think I am done with AppleTV port, didn't think I could make it in time for 1.7 release previously. Just need a confirmation or two whether the feature branch is worthy to be merged into master.

-------------------------

cadaver | 2017-05-31 15:08:05 UTC | #42

Don't have the HW to test, though I can of course build on Mac just to see the branch runs OK for me on both Mac + iOS.

The physics 2D issues and other recent issues that can be easily solved are of course good to check, while waiting for the IK fixes.

Then it could be at last time :)

-------------------------

weitjong | 2017-06-02 06:49:10 UTC | #43

I would not expect any regression issue with iOS in the new branch, but no harm to double check that. In fact the tvOS platform is so similar to iOS platform, I am also almost certain that Urho3D game engine will render correctly on the actual device. It is the input subsystem that I have my doubt to get it right at first try.

Probably I should have created another thread for discussion about the MODULE lib type for Web platform. Anyway, I just want to update that I have some success today to build a working main module with DCE enabled, which tremendously reduce the size of the main module and the time to build it. However, the process requires manual exporting of the mangled symbol names and feed them to the Emscripten's EXPORTED_FUNCTIONS setting during linking phase (finally I figure out how to pass that setting correctly via CMake to Emscripten). Perhaps it is time to revisit our Clang tool branch to auto-prepare the exported symbols list (easier to do); or as I commented before, hack into Fastcomp to auto-preserve URHO3D_API (harder to pull off).

EDIT: It is actually easier than I originally thought to hack into Fastcomp to auto-preserve the symbols with URHO3D_API attribute, however, by automatically including all the Urho exported public API symbols then the main module size increases back in size :slight_smile:

Main module size:
   - without global DCE = 56MB
   - with DCE + hack to auto-preserve = 51MB

In short, it does not worth it. So, the best way to do this is to disable the DCE; OR manually extract the required symbols for each individual project but with DCE enabled, which is unfortunate, cause I am not able to add that kind of logic in our build system for the latter. BTW, for those who still doesn't get it why we need a new lib type. The use case of MODULE lib type is to link the main module to asm.js only once which takes relatively a long time, so that the side module (which contains only the application-specific code) can be linked to asm.js in a short time. Good for fast iteration during development.

-------------------------

cadaver | 2017-06-04 14:08:44 UTC | #44

Verified the AppleTV branch successful run on OSX / iOS.

-------------------------

Modanung | 2017-07-18 13:15:55 UTC | #45

8 posts were split to a new topic: [New codestyle for C++ 11](/t/new-codestyle-for-c-11/3365)

-------------------------

cadaver | 2017-08-17 07:53:21 UTC | #46

IK work / fixes / docs are in, and I have nothing more on my list of waiting things, so I could go ahead and start compiling the final changelog.

-------------------------

cadaver | 2017-08-17 20:02:52 UTC | #47

Initial changelog is in. Feel free to amend where necessary.

-------------------------

TheComet | 2017-08-17 20:50:37 UTC | #48

- %XMLFile GetOrCreateRoot() function, and %XMLElement **GetOrCreateChild(9** function.

You let go of shift too soon :P

-------------------------

rku | 2017-08-18 09:56:28 UTC | #49

I am bit late to the party but maybe [3D UI](https://github.com/urho3d/Urho3D/pull/2074) would make it to release too? It is pretty much complete as far as i can tell, except for that OpenGL issue. If OpenGL fix isnt easy one then it can be left out. I really do not mind one way or the other.

-------------------------

cadaver | 2017-08-18 11:17:50 UTC | #50

Better to leave post release now, since the release was only waiting for IK fixes and a few smaller fixes, and there's a bit of risk involved in UI / UIElement modifications.

-------------------------

1vanK | 2017-08-19 19:32:31 UTC | #51

news on russian site https://www.opennet.ru/opennews/art.shtml?num=47054

p.s. what about news on https://urho3d.github.io/latest-news.html ?

-------------------------

cadaver | 2017-08-19 19:39:11 UTC | #52

Site update and announcement is going online just now, it was just that the tag / builds came first.

-------------------------

Victor | 2017-08-19 19:39:47 UTC | #53

Awesome! Congrats guys for the 1.7 release! :)

-------------------------

