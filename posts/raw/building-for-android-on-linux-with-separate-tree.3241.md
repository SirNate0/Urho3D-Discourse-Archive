slapin | 2017-06-12 14:11:08 UTC | #1

Hi, all!

How can I build for Android ***on Linux host*** when I have separate tree for my project?

i.e. I build Urho for Android as static library.
How can I build my project for Android? Are instruction are the same as for normal Linux build,
or there are differencies? How to make .apk with my project after this?
(yes, I tried searching the forum, but it seems my use case is unpopular)
(no, I'm not noob, I just not experienced developer ***for*** Android, while porting Android to various devices
is a part of my $$$ job, i.e. I extremely rarely do apps, I work with core system and frameworks)

Thanks!

Also, as my device is "rooted" (actually never was "unrooted"), is it possible to just put files on device and edit them there to save
on deployment during development? As I prototype using AngelScript, sometimes I want to check
if that will be good for Android or not...

-------------------------

weitjong | 2017-06-13 00:55:37 UTC | #2

Our build process is largely the same for different build/host system. Contrary to your view, Linux is a first class citizen as a build/host system as well as target platform. In fact it may work better than the rest simply because all our CI are tested on Ubuntu VM.

As for your problem, I don't see it in your post. Please try it first by following our online documentation page and report back exactly where you have failed.

-------------------------

