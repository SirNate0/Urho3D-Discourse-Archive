tbutton2005 | 2019-03-12 06:58:36 UTC | #1

hello, i cant compile my urho3d application with visual studio 2019. full description here: https://github.com/urho3d/Urho3D/issues/2428

-------------------------

Leith | 2019-03-12 07:40:56 UTC | #2

I have replied there ;)

-------------------------

tbutton2005 | 2019-03-12 07:52:36 UTC | #3

i added these libraries to msvc compiler:
Urho3D_d.lib
user32.lib
gdi32.lib
winmm.lib
imm32.lib
ole32.lib
oleaut32.lib
version.lib
uuid.lib
ws2_32.lib
iphlpapi.lib
dbghelp.lib
d3dcompiler.lib
d3d9.lib
kernel32.lib
winspool.lib
shell32.lib
comdlg32.lib
advapi32.lib
msvcrtd.lib
Now there is one error:  =
Error LNK2019 link to unresolved external main symbol in the function "int __cdecl invoke_main (void)" (? Invoke_main @@ YAHXZ) helloworld C: \ Users \ tbutton \ source \ repos \ helloworld \ helloworld \ msvcrtd.lib (exe_main.obj) 1
and i dont know, how fix it

-------------------------

1vanK | 2019-03-12 07:58:43 UTC | #4

lib also required some defines, so use cmake to generate Urho3d app
 https://urho3d.github.io/documentation/HEAD/_using_library.html 
 https://habr.com/ru/post/280752/

-------------------------

Leith | 2019-03-12 08:05:55 UTC | #5

Good work, you are down to one bug.
You need to install the microsoft visual c runtime library.
You should not need to add any more libs in msvc studio, just check that you have the msvcrt installed, should cure it for you, and your app will need to ship with a copy of that installer, for end users using windows

" Download and **install** Visual C++ Redistributable for Visual Studio from Microsoft's website "

-------------------------

tbutton2005 | 2019-03-12 08:09:57 UTC | #6

but urho3d examples work, like, without redistributable, and i'm thinking maybe i'm something doing wrong
or i really need to install redistributable?

-------------------------

Leith | 2019-03-12 08:13:21 UTC | #7

Maybe not, show me your application entrypoint code, mine looks like this

[code]
class MyApp : public Urho3D::Application

{...}

URHO3D_DEFINE_APPLICATION_MAIN(MyApp)


[/code]

thats in main.cpp

-------------------------

tbutton2005 | 2019-03-12 08:14:56 UTC | #8

```using namespace Urho3D;
class MyApp : public Urho3D::Application
{
...
}
URHO3D_DEFINE_APPLICATION_MAIN(MyApp)
```
its mine

-------------------------

Leith | 2019-03-12 08:17:11 UTC | #9

if its the same, then do try to install the msvc runtimes, im seeing a linker error, so compiler finished with a thumbs up - im not on msvc right now, but happy to port projects across platforms

-------------------------

Leith | 2019-03-12 08:19:18 UTC | #10

under msvc, the linker stage wont even try to run, unless all the sourcecode compiled successfully into object files, or was already up to date - so the fact that your error is a linker error, is good... you're close.

-------------------------

tbutton2005 | 2019-03-12 09:10:39 UTC | #11

its easy to fix. i choose subsystem - Windows (/SUBSYSTEM:WINDOWS), and now it compiled.
but app im trying run, writes: 
EROR: failed to add resource path "CoreData", check the documentation or how to set resource path 'resource perifix path'
what need i do now?

-------------------------

Leith | 2019-03-12 09:18:25 UTC | #12

I remember being here recently, try to copy into your project folder, the bin folder from the urho3d build
I know its overkill, but try it.

-------------------------

tbutton2005 | 2019-03-12 09:13:53 UTC | #13

yes it works, thanks all, now i can make 3d game using urho3d!

-------------------------

Leith | 2019-03-12 09:14:29 UTC | #14

welcome to my world of not much help but trying

-------------------------

Leith | 2019-03-12 09:15:56 UTC | #15

you are very welcome, i am happy to have been of some help

-------------------------

