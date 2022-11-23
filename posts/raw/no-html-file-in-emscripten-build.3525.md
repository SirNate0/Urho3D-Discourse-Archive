rifai | 2017-09-03 09:38:53 UTC | #1

Hi, I successfully build Urho3d with emscripten. In bin directory, I got some *.pak & js files. No html file. How do I run this files?

-------------------------

weitjong | 2017-09-03 09:56:10 UTC | #2

This is the expected result in 1.7. Check the release/migration notes. https://urho3d.github.io/documentation/1.7/_porting_notes.html

-------------------------

Eugene | 2018-05-31 22:21:03 UTC | #3

I want to raise this topic.
When I build Emscripten build, I expect to have samples built too. However, there's no run-able htmls in `bin` folder. Damn. I built samples, but in fact I didn't.

-------------------------

weitjong | 2018-06-01 05:27:17 UTC | #4

This has been discussed before and also Lasse agrees with the changes. I can’t remember where we discussed that though. Before the change, the build system prepared a very basic and simple HTML shell and used that to wrap around the JS output. This was fine, however, in the real application you will most probably have a better or more customized HTML shell you want to use, and there was no way to tell the build system to do that. The change addresses all these. It now simply does not assume too much. It will use the very basic and simple shell if you tell it that you are too lazy to provide one and that you still want to a quick test afterward (URHO3D_TESTING option). Otherwise, it will just produce the output in the form of JS or WASM, and will only wrap it inside a shell when you explicitly specified one.

-------------------------

johnnycable | 2018-06-01 08:06:18 UTC | #5

I confirm URHO3D_TESTING does it like it was before

-------------------------

Eugene | 2018-06-01 08:47:13 UTC | #6

[quote="johnnycable, post:5, topic:3525, full:true"]
I confirm URHO3D_TESTING does it like it was before
[/quote]

[quote="weitjong, post:4, topic:3525"]
It will use the very basic and simple shell if you tell it that you are too lazy to provide one and that you still want to a quick test afterward (URHO3D_TESTING option)
[/quote]

Yep, I figured it out after an hour on my own.
I just want to say that our build system must either build samples in the way I could run them as is or don't build them at all.

I wanted to try Web samples locally. I followed build instructions, `URHO3D_SAMPLES` on, it was slow as hell (maybe 1h to build everything). And I got no samples in the result. That was just annoying.
What was the point of 30-40 min of linking samples if they can't be run in any way?..

-------------------------

weitjong | 2018-06-01 10:39:03 UTC | #7

The idea is someone may wrap the generated output(s) after the fact. But you do have a point also, having a URHO3D_SAMPLE should be enough for the build system to make certain assumptions. Having said that, if we do this then it would just mean the build system has this extra logic when building Urho3D library (with the samples); BUT when building for downstream app what I have described above still applies. Not sure it is a good idea but definitely make the life easier for newcomers.

-------------------------

Eugene | 2018-06-01 11:16:11 UTC | #8

[quote="weitjong, post:7, topic:3525"]
Having said that, if we do this then it would just mean the build system has this extra logic when building Urho3D library
[/quote]

AFAIK there's a command to specify shell. Could all the samples specify this shell on their own?
It would be copy-paste in CMake, but not that much of it.

-------------------------

weitjong | 2018-06-01 12:59:08 UTC | #9

That new macro was part of the changes in the commit. Putting it back there actually makes the whole thing back to where I started. Originally I envision to create an SPA using React or Angular that requests those JS or WASM files on the fly and wraps it from the client side. Let me think about it.

-------------------------

Eugene | 2018-06-01 13:11:54 UTC | #10

[quote="weitjong, post:9, topic:3525"]
That new macro was part of the changes in the commit. Putting it back there actually makes the whole thing back to where I started
[/quote]

I got an impresson that changes you mentioned was about user executables generated when Urho3D is used as 3rdparty library.
However, I'm talkina about Urho3D samples only and I suggest to edit their own CMakeList-s so samples pick default shell.

-------------------------

weitjong | 2018-06-01 13:34:01 UTC | #11

I am referring to the sample web pages hosted in github pages. Since we have the WASM variant, I have wanted to do an SPA for the samples. With the current basic/simple approach we can only have either JS variant or WASM variant, but not both. However, wanting or thinking about it is one thing, actually having time and energy to do it is another.

-------------------------

Eugene | 2018-06-01 15:08:54 UTC | #12

[quote="weitjong, post:11, topic:3525"]
I am referring to the sample web pages hosted in github pages.
[/quote]

I see.
At least, I'm going to note in docs that TESTING must be set if one want to build Web samples. I'm talking about main "How to build" page, not these porting notes or other forgotten places that nobody reads.
If you change it at some point, just remove the note.

-------------------------

johnnycable | 2018-06-01 18:58:08 UTC | #13

Yes, it's slow, and moreover, I was never been able to build it in debug, just release mode. In debug it stops with an error st. like "too many symbols..."
I checked my builds and I see it's a lot I don't build those web examples... probably since 1.6...
I'll give them a try tomorrow.

-------------------------

weitjong | 2018-06-02 02:24:53 UTC | #14

After sleeping on it (literally), in order to make life easier for newcomer and for consistency with other platforms, the default HTML shell will be used if user doesn’t provide one explicitly. Then I will introduce yet another EMSCRIPTEN specific build option to suppress this logic of falling back to use default shell. That should keep everyone happy.

-------------------------

weitjong | 2018-06-02 03:18:59 UTC | #15

I have never had the patient to build all the samples (its number keep growing BTW) in one go as well. So, normally I just build one sample at a time via CLI. Building all only when I don't need to attend the build process.

    rake make web target=01_HelloWorld

The "target=...." is an option from "cmake --build" command and not GNU "make" command. So, it actually works across other platforms too. YMMV.

-------------------------

johnnycable | 2018-06-02 11:14:01 UTC | #16

Building emsc in release mode with example works. Used master some commits ago. Of course is damn slow, and anyway you get a 642 mb data.pak which makes the whole thing just an exercise...

-------------------------

Eugene | 2018-06-02 13:08:45 UTC | #17

[quote="johnnycable, post:16, topic:3525"]
Of course is damn slow, and anyway you get a 642 mb data.pak which makes the whole thing just an exercise…
[/quote]

You are doing something wrong... For `06_SkeletalAnimation` I have 17mb *.data and 3mb wasm. Not that much.
The interesting thing that 25% of samples just hang when I build them locally.
Especially 08_Decals. It work fine if I look straight or rotate camera exactly at left or right, but hangs if I try to look down.

-------------------------

weitjong | 2018-06-02 14:35:56 UTC | #18

If your local means Windows host system then I have no more comment to add. I have not done any Web build on Windows host for quite some time now. All the samples in our github pages are built using Linux host system. Do you get the similar issue when testing the same there online?

Also, just a head up. The next one or two CI build on master branch will upload those samples from WASM CI instead of JS.

-------------------------

weitjong | 2018-06-03 08:54:51 UTC | #19

The first upload of WASM variant can be tested now on the main website.

-------------------------

Eugene | 2018-06-03 09:05:29 UTC | #20

Now I have the same problem online :laughing:
https://urho3d.github.io/samples/08_Decals.html
Just look down and it will crash.
Uncaught RuntimeError: float unrepresentable in integer range

-------------------------

weitjong | 2018-06-03 09:12:07 UTC | #21

You are right. Never see it before. So the issue is related to WASM. In JS I believe we just throwaway the runtime exception. In WASM, we may have to capture and handle it. Need to check.

-------------------------

Eugene | 2018-06-03 10:20:04 UTC | #22

I’m trying to find the root cause. It seems that there’s a problem in drawing occlusion triangles.

-------------------------

