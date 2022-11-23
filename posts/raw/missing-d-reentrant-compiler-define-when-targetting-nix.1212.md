weitjong | 2017-01-02 01:06:06 UTC | #1

Is this an oversight or intentional? Urho3D lib and its sub-libs like SDL uses pthread on Unix-like platforms. I have not observed an Urho3D app to bad-behave even though it was built without this define. When I call the "SDL-config --cflags", its output clearly states that SDL expects this define. Yet none have reported any problems. What gives?

I have time to do some research on this subject this morning and found this article that explains the potential danger of mixing supposedly multi-threading app linking with pthread but without the "_REENTRANT" define set with glibc that does. See [pauillac.inria.fr/~xleroy/linuxt ... faq.html#H](http://pauillac.inria.fr/~xleroy/linuxthreads/faq.html#H). It makes sense to me, which is why I even bother to search for the answer in the first place. I cannot explain why Urho3D app does not crash spectacularly on Linux/OSX though. Or is it just accident waiting to happen?

Separately, I have done a quick test using GCC and Clang on my Linux box and Clang on my OSX box. When given '-pthread' compiler flag, they all emit "-D_REENTRANT" compiler defines to the compiler. And I have done a quick build test using GCC on Linux, this flag also instructs linker to link against "pthread" implicitly. From what I read, it instructs linker to link against a platform-specific library for multi-threading automatically. So it is portable too although we do not really need it because we do not support other niche *nix platforms yet at the moment. It only took me awhile to reconfigure our build system to use this compiler flags. However, I would like to hear from others, especially from Lasse, on what yours/his take on this matter before pushing my changes.

-------------------------

cadaver | 2017-01-02 01:06:06 UTC | #2

We have a bastardized CMakeList for SDL which is missing a lot of platform checks for Unixes, as at the time of original SDL adoption SDL's own CMakeList was broken. Their own CMakeList does 
[code]
set(PTHREAD_CFLAGS "-D_REENTRANT")
set(PTHREAD_LDFLAGS "-pthread")
[/code]
so it's certainly what we should be doing as well. As a sidenote, once 2.0.4 is out it might be worth to migrate to their CMakeList, if it works right.

The reason for lack of problems is probably that using the affected C library functions happens only in the main thread, while the worker threads mostly do just basic memory allocation and data processing.

-------------------------

weitjong | 2017-01-02 01:06:06 UTC | #3

Thanks for the quick reply. Yes, your reasoning for lack of problem is plausible. I am making some build tests on my OSX box as I speak. I will push it when all are OK.

EDIT: I have pushed my changes. I forgot to reset the OS clock to current time before pushing (I usually just save/restore VM session without actually rebooting it), so the newly pushed changes appears to be made by me 25 days ago.  :wink:

-------------------------

