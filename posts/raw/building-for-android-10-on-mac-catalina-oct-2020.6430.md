drohen | 2020-10-11 22:52:10 UTC | #1

Not having too much luck. I've found various articles and threads, just can't seem to get any to work. 

There are outdated by use of gradle (and are Win-centric):
https://discourse.urho3d.io/t/solved-build-urho-and-my-app-for-android-step-by-step/655
https://discourse.urho3d.io/t/howto-urho3d-android-setup-on-win7/1938

I thought this might work:
https://gamedevtodied.blogspot.com/2017/10/urho3d-build-sample-on-android.html
But not really, however it made me consider just purely using Android Studio.

I tried just setting up with Android Studio. Got pretty far except needed to set a bunch of env vars to finally get some progress, but then it seems a kotlin plugin warning kept blocking everything. Not sure if I should uninstall the plugin, disabling it made android studio stop working altogether.

Some/most of the info on the main pages seem out of date, but the information about using `./gradlew` from the command line got me the furthest (also was recommended in a thread I can't find now).
https://urho3d.github.io/documentation/HEAD/_building.html#Building_Android

However it failed with lots of errors that looked like:
`Library/Android/sdk/ndk/21.0.6113669/toolchains/llvm/prebuilt/darwin-x86_64/lib64/clang/9.0.8/include/mmintrin.h:33:5: error: use of undeclared identifier '__builtin_ia32_emms'`

I see this mentioned in some Stack Overflow posts:
https://stackoverflow.com/questions/53805054/androidstudio-compile-c-met-a-problem-like-thismmintrin-h-builtin-ia32-em
https://stackoverflow.com/questions/5217812/c-compilation-issue-with-emmintrin-h-on-linux-gcc
There it references SSE, and I see there's a flag for this: `URHO3D_SSE` so should I set this? Unfortunately I've run out of time, and the build was already taking quite a while, so I don't have time to test again for a while.

I was hoping to learn this engine and create something for my phone, but I can't really get anywhere and it seems due to lots of changes in the mac and android worlds, there's no one really making up-to-date tutorials/how-tos, which is a shame because that's basically how many projects attract new users. I would love to contribute and write the tutorial, I'd even make a video or whatever, but someone might have to help me step-by-step first so I can at least see it running.

Looking forward to some feedback, thanks in advance for anyone who is willing to put something together for me.

-------------------------

weitjong | 2020-10-12 08:26:00 UTC | #2

Android uses arm so SSE is not applicable. Our Android build will use NEON when it is available, well not fully, but at least on a few sub-libraries that engine uses. 

Don’t hold your breath but in the coming weeks we will have a new officially supported approach for Android build using AAR. Keep an eye on the “migration to GitHub actions” dev branch.

-------------------------

drohen | 2020-10-12 08:59:29 UTC | #3

> Android uses arm so SSE is not applicable. Our Android build will use NEON when it is available, well not fully, but at least on a few sub-libraries that engine uses.

Thanks for letting me know. I think for now, it feels like the main problem is having a very clear way of getting anything running at all on catalina. If I see that this engine lives up to expectations and is enjoyable to work with, then I'd be happy to contribute some nicely formatted and well-written English documentation. But for now, I don't have enough to work with to get something running reliably.

-------------------------

vmost | 2020-10-12 20:28:06 UTC | #4

Normal Urho3D builds fine on macs [with a few tricks](https://discourse.urho3d.io/t/info-using-urho3d-with-old-mac-osx-10-11/6304).

-------------------------

drohen | 2020-10-12 20:50:36 UTC | #5

Thanks but the post refers to El Capitan, would be good if were confirmed for Catalina. Not expecting people to do something for me but life feels too short to not expect at least some kind of script to automate these processes. Also makes me wonder, why write a game engine if you can't write a script or a straight forward setup guide for the platforms that are said to be supported? Trying not to be too critical, it is open source and I pay nothing to use it, but its a bummer to want to dig in only to realise it's just not going to happen.

-------------------------

vmost | 2020-10-12 22:03:21 UTC | #6

Well these things are only possible if someone who actually has the specific OS and specific build requirements goes and does it. There wasn't a guide for El Capitan before I needed to compile the engine on El Capitan, probably because no one ever tried to compile on El Capitan before.

-------------------------

weitjong | 2020-10-17 14:41:04 UTC | #7

The Urho3D AAR is finally ready. After the dev branch is merged into master branch, new downstream projects using Urho3D AAR could be as easy as below (assuming the AAR is available in one of maven repo near you):

    $ cd /path/to/urho3d/project/root
    $ rake new
    $ cd ~/project/UrhoApp
    $ ./gradlew build

The new Android build is tested with Linux host system. However, it should work the same for macOS.

-------------------------

