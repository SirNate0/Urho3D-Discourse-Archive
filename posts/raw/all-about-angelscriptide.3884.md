f1af | 2017-12-26 22:38:41 UTC | #1

- I cant find any screenshots of this IDE. Can anyone get me screenshots?
- Can I find another way for syntax hightlight of AngelScript?
- I have trouble with building AngelscriptIDE for linux. I fix some bug in CMakeLists, but I cant find "AngelScriptsUtils" source code. In this repo, its util-lib placed as static *.lib for windows only.
.
.

https://github.com/SamVanheer/AngelscriptIDE

-------------------------

elix22 | 2017-12-26 23:42:41 UTC | #2

https://github.com/SamVanheer/AngelscriptUtils

-------------------------

f1af | 2017-12-27 01:00:53 UTC | #3

![изображение|690x387](upload://3cJNVXERPeLTCcewgT4FpfnpboJ.png)

-------------------------

f1af | 2017-12-27 01:03:09 UTC | #4

so, thank u.
but I cant open any file. I see just only this is (on screenshot).

Can you tell my screenshot of working version of AngelscriptIDE?

-------------------------

globus | 2017-12-27 12:43:33 UTC | #5

How variant, you can get Code::Blocks IDE for AngelScript coding.

https://www.gamedev.net/forums/topic/626832-angelscript-coding-with-codeblocks/

Author provide Win32 release (~25mb):
https://docs.google.com/open?id=0B3MVwL3eqJwFRTBNNjh0a284Vnc

Settings file:
https://docs.google.com/open?id=0B3MVwL3eqJwFTTd5Ny12dEVmSkE
put this file at C:\Users\[username]\AppData\Roaming\CodeBlocks (highlight, *.as extension etc..)

Source code:
https://docs.google.com/open?id=0B3MVwL3eqJwFX1JjV212ZmRHWjg
Small changes in parser code.

What it do?

Sintax Highlight and IntelliSense support.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/5/59b6038b0a345bad6590b4667b320ef0775709f2.png'>

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/e/e75c00c7a2fb3990f6b60e0ce9050d7a9672b07c.png'>

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/4/42276ee03cbb9a45ba6fb9bf46cc42b6196607fc.png'>

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/d/df2b26ea51d5350726585bf1c2b662346b0ac9d0.png'>

But not all constructions can be parsed.
For example:
`Array<MyClass@>@ testlist;`
Parse only Array and MyClass
This testlist can not be parsed and if you call it.
`testlist[3].doSomething();`

-------------------------

kostik1337 | 2017-12-27 12:10:42 UTC | #6

Also, there was thread about configuring CodeLite with actionscript. I haven't tried it.
https://discourse.urho3d.io/t/configuring-codelite-for-editing-as-scripts/68

-------------------------

globus | 2017-12-27 12:55:03 UTC | #7

If you use for Windows the above Code::Block (win32),
then you can download the Launcher for its launch in portable mode.
binary with source code
http://cblauncher.codecutter.org/CbLauncher_1.0.zip
only source code
http://cblauncher.codecutter.org/CbLauncher_1.0.1_src.zip

-------------------------

f1af | 2017-12-27 13:47:37 UTC | #8

and what about realtime debuging?
have any tools for debug angelscript in realtime, like a Python scripts..?

-------------------------

globus | 2017-12-27 21:50:45 UTC | #9

https://discourse.urho3d.io/t/angelscript-debugging/36
AngelScript source: sdk/add_on/debugger/

https://github.com/codecat/asdbg

-------------------------

