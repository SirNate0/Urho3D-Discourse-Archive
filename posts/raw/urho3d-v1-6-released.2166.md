cadaver | 2017-01-02 01:13:36 UTC | #1

Urho3D V1.6 is out! Again, thanks to everyone who contributed / made it possible. Highlights include among other things dragonCASTJosh's PBR rendering work and getting AngelScript to run on the Web platform (as well as 64-bit iOS).

Release post: [urho3d.github.io/releases/2016/ ... lease.html](https://urho3d.github.io/releases/2016/08/08/urho3d-1.6-release.html)
Source code: [github.com/urho3d/Urho3D/tree/1.6](https://github.com/urho3d/Urho3D/tree/1.6)
SourceForge file archives: [sourceforge.net/projects/urho3d/ ... rho3D/1.6/](http://sourceforge.net/projects/urho3d/files/Urho3D/1.6/)

Now the master branch is open for more adventurous work again :wink:

-------------------------

weitjong | 2017-01-02 01:13:36 UTC | #2

Congrats!

-------------------------

Lumak | 2017-01-02 01:13:36 UTC | #3

Awesome.  Thank you all for your hard work.

-------------------------

1vanK | 2017-01-02 01:13:37 UTC | #4

News is published on russian resource :) [opennet.ru/opennews/art.shtml?num=44929](http://www.opennet.ru/opennews/art.shtml?num=44929)

-------------------------

Egorbo | 2017-01-02 01:13:37 UTC | #5

Great work, guys!
That is a looong list of changes.

-------------------------

yushli | 2017-01-02 01:13:37 UTC | #6

Greate news! Thank you all for making this engine even more amazing. 
Now wait for more to happen!

-------------------------

aster2013 | 2017-01-02 01:13:37 UTC | #7

Congrats!

-------------------------

jenge | 2017-01-02 01:13:37 UTC | #8

Congrats on the release, very good change log and third party updates!

-------------------------

jmiller | 2017-01-02 01:13:37 UTC | #9

Congrats! And what a changelog! Urho's an ever mightier fish.

-------------------------

Victor | 2017-01-02 01:13:38 UTC | #10

Indeed, congrats you guys! :slight_smile:

-------------------------

Miegamicis | 2017-01-02 01:13:39 UTC | #11

Awesome! Thanks! Time to check it out!   :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:13:39 UTC | #12

Thanks guys. Awesome release.

-------------------------

dwlcj | 2017-01-02 01:13:39 UTC | #13

Thanks!

-------------------------

Bluemoon | 2017-01-02 01:13:40 UTC | #14

Congrats Everyone for yet another job well done :smiley:

-------------------------

boberfly | 2017-01-02 01:13:51 UTC | #15

A great new release, congrats! I haven't been around these parts in awhile too busy at work, but I've been lurking here and there and it's great to see so much progress!

-------------------------

zzz654321 | 2017-01-02 01:14:05 UTC | #16

I need Urho3D in win32 luajit version. 
please compile this to [www.sf.net](http://www.sf.net)   thanks!
if the lua51.dll outside urho3d.dll, that is very good!!!!!!!

-------------------------

itisscan | 2017-01-02 01:14:05 UTC | #17

Thanks for great work !

-------------------------

weitjong | 2017-01-02 01:14:05 UTC | #18

[quote="zzz654321"]I need Urho3D in win32 luajit version. 
please compile this to [sf.net](http://www.sf.net)   thanks![/quote]
The idea to upload those build artifacts to sf.net is really an afterthought, we originally just need to have CI test. There is no canonical way to configure Urho3D build tree. We have our own technical constraint and reasoning when choosing those build options for CI build. Take LuaJIT build option for example, we can only enable it whenever it is supported by the compiler toolchain provided by our CI server and unfortunately MinGW CI build on Travis CI server was found to be incapable to handle LuaJIT building. Travis VM is (still) running on the ancient Ubuntu 12.04 LTS operating system. You are better off building the Urho3D library yourself from source. Having said that, we do have Windows/DX11 build with LuaJIT enabled using MSVC compiler in AppVeyor (another CI server running on Windows Server).

[quote="zzz654321"]if the lua51.dll outside urho3d.dll, that is very good!!!!!!![/quote]
I think it is a design decision. We could have provided an option to build the 3rd-party libraries as SHARED library, however, we don't  provide one and instead always build them as STATIC and to be linked *internally* by Urho3D library. This is because in quite a number of cases we have made local patches to those 3rd-party libraries either for quick bug fixes or to change it to suit our own need. So even if we could build them as SHARED libraries, it was not really safe to replace them with other (presumably newer) version from outside of Urho3D build tree.

-------------------------

rasteron | 2017-01-02 01:14:14 UTC | #19

Congrats on 1.6!

-------------------------

