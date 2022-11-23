glebedev | 2020-10-24 22:27:58 UTC | #1

I've started a branch to update SDL from 2.0.10 to 2.0.12 as hdiapi gamepad support in 2.0.10 is awful.

https://github.com/urho3d/Urho3D/pull/2706

It doesn't even compile on windows yet. Any help is welcome.

-------------------------

weitjong | 2020-10-25 06:21:44 UTC | #2

I could have a look but not after I wrap up a few other things in the dev branch I am currently working on. But I will most probably start a new instead of fixing on top of yours.

-------------------------

glebedev | 2020-10-25 07:19:26 UTC | #3

Shall I abandon this one then?

-------------------------

weitjong | 2020-10-25 10:10:16 UTC | #4

If you still want to try to get it work then no harm to keep the PR there first. I actually haven't looked at it though. Who knows it is just a simple mistake.

-------------------------

glebedev | 2020-10-25 13:33:59 UTC | #5

I suspect the problem is in cmake file.

If you going to do it yourself in next couple weeks I can wait. Otherwise I'll try to make it work.

-------------------------

weitjong | 2020-10-25 15:29:06 UTC | #6

We are using heavily modified CMake build scripts. For sure you cannot just simply replace that with the original but upgraded scripts from SDL and expect it to work.

-------------------------

glebedev | 2020-10-25 15:35:19 UTC | #7

I didn't replace it, I kept the one that was in Urho. Although it is hard to track what is different there since it is very different from original SDL 2.0.10 cmake.

-------------------------

glebedev | 2020-10-25 15:36:35 UTC | #8

My question is if you have a SDL upgrade timeline on mind or it may happen "some time in future".

-------------------------

weitjong | 2020-10-26 01:54:03 UTC | #9

I know exactly what you are saying. Believe me. Over the years, I have come up with my own way to keep track of the local as well as the upstream changes and able to "systematically" merge the changes together. However, it is still rather a convoluted process using git and vi to resolve any conflicts. Not easy for me to elaborate here, although I have written the gist of it in my personal github account. It was a mental notes for myself and I don't expect anyone else to read and understand from it.

I don't have a specific timeline for it. Actually I have another bigger fish to fry in my current dev branch.

-------------------------

glebedev | 2020-10-25 17:34:04 UTC | #10

Ok, then  I'll try to make it work myself.

-------------------------

glebedev | 2020-10-25 17:35:58 UTC | #11

Btw do you know how to switch joystick support from hid to xinput or xinput? This would also work for me fine.

-------------------------

Modanung | 2020-10-26 11:12:43 UTC | #12

7 posts were split to a new topic: [Return of the nag](/t/return-of-the-nag/6459)

-------------------------

weitjong | 2020-10-27 00:54:25 UTC | #13

I am also not the expert of SDL. I just know one thing or two on how to get the upstream changes merge into the Urho3D from earlier experience through trial and error. Practice makes perfect, they say. However, in actual fact, for each upgrade I have to spend a lot of time and energy to reconcile the conflict, but I am not as fit anymore. I just have a systematical way to identify the changes (thanks to Git), but the hard labor is in conflict resolution. In other words, whether you and I have the systematic way for performing the upgrade or not, we both will face the same daunting task. And, no, I don't know the answer to your last question.

-------------------------

weitjong | 2020-10-27 05:08:05 UTC | #14

What happened to 2.0.11? They just jumped from 2.0.10 to 2.0.12?

-------------------------

glebedev | 2020-10-27 07:23:53 UTC | #15

Looks like it... I don't know why.

I also wonder if they going to produce 2.0.13 in the middle of the merge... That would be unfortunate :slight_smile:

-------------------------

glebedev | 2020-10-27 13:17:57 UTC | #16

May I ask you where SDL_EXPORTS is defined? I can't find it in cmake files...

-------------------------

glebedev | 2020-10-27 14:29:42 UTC | #18

It is used there but I can't find where it is defined...

    // Urho3D: Only export when it is being requested
    #ifdef SDL_EXPORTS

-------------------------

weitjong | 2020-10-27 14:42:04 UTC | #19

I think it is basically just a way to make it not exported. Urho3D builds all its sub-libraries as STATIC.

-------------------------

glebedev | 2020-10-28 08:05:08 UTC | #20

Samples reference Urho3D. Urho3D reference SDL. Sample compilation fails because of missing SDL functions like SDL_free.

Any ideas why it would be?

-------------------------

weitjong | 2020-10-28 08:40:12 UTC | #21

You meant building “Urho3D” lib itself is fine? And only failed in samples?

-------------------------

glebedev | 2020-10-28 08:49:39 UTC | #22

Exactly.

And now few words to make reply longer than 20 chars.

-------------------------

weitjong | 2020-10-28 09:53:33 UTC | #23

It means the symbol is eliminated in the final Urho3d lib, but that’s not correct. It’s hard to guess the root cause though. Ensure you are using STATIC lib type for SDL. Check the generated SDL config file is identical to previous one before upgrade, or at least it should be similar and diffs are acceptable.

I suppose you are using SHARED lib type for Urho3D lib itself?

-------------------------

weitjong | 2020-10-28 10:12:48 UTC | #24

Also you have to use the same Urho3D-specific macro to add/setup the SDL lib. You cannot use the CMake command as per original build script from SDL. In the background our macro does a number of heavy lifting. One of the task is to mark which archive containing the *.obj should be used in building the final engine lib.

-------------------------

glebedev | 2020-10-28 10:28:02 UTC | #25

I'm not using SDL cmake script. I moved all changes to 2.0.12 I could move to the existing Urho3D SDL file.

I'm running cmake script for vs2019 from scripts folder with default settings, so whatever is by default...

-------------------------

weitjong | 2020-10-28 10:35:56 UTC | #26

By that you should be using STATIC lib type for the engine too. The STATIC lib type is just an archive of all *.obj from Urho3D and all its sub-libs including SDL. So there is no reason for the downstream using the final lib to have missing symbol, unless the symbol is not there in the first place. Can you check the archive from SDL to see if it still has SDL_free? In Linux the archive file is the *.a. Not sure on Windows, *.lib perhaps. In Linux we use “nm” command to check the content of the archive file. Again, not sure on Windows.

-------------------------

weitjong | 2020-10-28 10:43:31 UTC | #27

Perhaps you should try to use SHARED lib type for the Urho3D lib. This way it should be linked against the SDL lib, so if you have issue with SDL then the problem should hopefully show up while building the engine lib.

-------------------------

glebedev | 2020-10-28 15:13:43 UTC | #28

`Section length  9AA, #relocs   6A, #linenums    0, checksum 5E719D6B`
`00F 00000000 UNDEF  notype ()    External     | SDL_free`

With the new SDL build:
`00C 00000000 UNDEF  notype ()    External     | SDL_free_REAL`

Wtf is that _REAL part?

-------------------------

glebedev | 2020-10-28 15:22:26 UTC | #29

So it seems dynapi wasn't disabled properly?

-------------------------

glebedev | 2020-10-28 15:31:52 UTC | #30

@weitjong ok, I've missed a change in dynapi header.

Looking into .lib was a good idea, thanks!

-------------------------

glebedev | 2020-10-28 15:38:22 UTC | #31

Well, it's a start!

![image|641x499](upload://xu0ICjowwThnodVVAo2X7BQek1b.png)

-------------------------

glebedev | 2020-10-28 16:00:47 UTC | #32

Also my xbox controller works now. So it wasn't for nothing.I have around 10 files to merge and then it should be ready for review.

-------------------------

Modanung | 2020-10-28 16:39:38 UTC | #33

@glebedev You must know, it's good to see you working on Urho proper. :slight_smile:

-------------------------

glebedev | 2020-10-29 13:34:27 UTC | #34

I guess I didn't break the LSEEK, right? https://github.com/urho3d/Urho3D/pull/2706/checks?check_run_id=1326432936

-------------------------

weitjong | 2020-10-29 15:15:34 UTC | #35

No, you didn’t. I have explained it to you separately in the PR.

-------------------------

Pencheff | 2022-06-26 11:56:02 UTC | #36

I'm also trying to update, SDL 2.0.22, some builds are failing:
https://github.com/PredatorMF/Urho3D/actions/runs/2563944700

Suggestions are welcome

-------------------------

