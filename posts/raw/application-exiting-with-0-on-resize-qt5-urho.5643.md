VladBolotov | 2019-10-25 09:38:11 UTC | #1

I am integrating Urho3D into Qt. But I am stuck with weird bug. When a window is resizing application can randomly exit with 0 without exceptions, errors and so on. Breakpoints at the end of the main are totally ignored. I made a short video about this problem: https://youtu.be/6d7mBhbmT7U

Can somebody give me an advice how can I debug such thing or how can I figure out where the problem is?

-------------------------

Modanung | 2019-10-03 12:20:55 UTC | #2

Welcome to the forums! :confetti_ball: :slightly_smiling_face:  

Are you using xorg video drivers? I've had several people tell me they experienced this problem with both [Edddy](https://luckeyproductions.itch.io/edddy) and [ManaWarg](https://luckeyproductions.itch.io/manawarg). @kapil suggested this could be solved using `QThread`s. 

Please _do_ share your implementation if it works.

-------------------------

VladBolotov | 2019-10-03 12:18:26 UTC | #3

`Welcome to the forums!` 
Thank you! :) 
`Are you using xorg video drivers?` 
I used Windows and MSVC for this. So... Video drivers are from nvidia_drivers.exe. ;)
`... suggested this could be solved using  `QThread` s.`
Sorry, but I did not get what are you trying to say. 
Basically I am trying to use SDL_CreateWindowFrom via [Urho3D::EP_EXTERNAL_WINDOW] = reinterpret_cast<void *>(winId()); where winid is a native handler of QWidget. And here is the "dirty" code from the video.  https://github.com/VladBolotov/QUrho3D

-------------------------

Modanung | 2019-10-03 12:19:36 UTC | #4

I have no personal experience with `QThread`s. Maybe its [documentation](https://doc.qt.io/qt-5/qthread.html) could help understand their use?

-------------------------

VladBolotov | 2019-10-03 12:27:49 UTC | #5

I mean why do I need QThreads here? For what purposes? Think about QThred like it Qt specific std::thread. :)

-------------------------

Modanung | 2019-10-03 12:45:31 UTC | #6

Oh, you could use the `std` variant just as well, I guess.

-------------------------

Elendil | 2019-10-03 14:22:16 UTC | #7

Interesting, I have same problem, but I use WPF instead QT. But problem is only with Urho builded from github, If I remember right, old Urho from 2018 1.7 (from SourceForge) dont have this problem.

-------------------------

Modanung | 2019-10-03 14:34:06 UTC | #8

I'm increasingly baffled by the fact I am _not_ experiencing this problem.

-------------------------

Elendil | 2019-10-03 15:03:26 UTC | #9

Which version Urho you use and from what source you downloaded it? And do you use Urho with external window?

I switch back to old Urho and it working without crash.

-------------------------

Modanung | 2019-10-03 16:11:05 UTC | #10

I basically always use a locally compiled recent version of the official master branch.

[quote="Elendil, post:9, topic:5643"]
And do you use Urho with external window?
[/quote]

Sort of...
```
QWidget*    fishTrap{ new QWidget() };
engineParameters_[EP_EXTERNAL_WINDOW] = (void*)(fishTrap->winId());
delete      fishTrap;
```

But it's not the code that shields me from this issue, as others _are_ experiencing it with the same programs.

I'm on Linux Mint with Xfce using version 430 of the Nvidia drivers, btw.

-------------------------

Elendil | 2019-10-03 17:24:27 UTC | #11

[quote="Modanung, post:10, topic:5643"]
But it’s not the code that shields me from this issue, as others *are* experiencing it with the same programs.
[/quote]

Who knows... for example Urho 1.7.1 source from SourceForge (5.24.2019) doesn't have included UIComponent class which was added 9months ago, but github version have it.

Maybe github version is always new version but not stable?

-------------------------

weitjong | 2019-10-17 11:09:10 UTC | #12

This is what immediately come to my mind regarding resizing on Windows platform.

https://github.com/urho3d/Urho3D/pull/2256

I am not saying for sure that is the cause of your issue, but no harm to try to revert that commit to see if it fixes the issue or better yet find the solution to fix if it indeed was the cause. I have no Windows to test any of this.

-------------------------

VladBolotov | 2019-10-04 02:51:57 UTC | #13

I've played a little bit with WinDbg and got this stack trace. 

```
(3230.c44): Access violation - code c0000005 (first chance)
First chance exceptions are reported before any exception handling.
This exception may be expected and handled.
Qt5Guid!std::_Fetch_add_seq_cst_4+0x12:
00007ff9`9c9c7582 f00fc101        lock xadd dword ptr [rcx],eax ds:00000001`00000023=????????
0:000> k
 # Child-SP          RetAddr           Call Site
00 00000007`aeaf83a8 00007ff9`9c9c7277 Qt5Guid!std::_Fetch_add_seq_cst_4+0x12 [c:\program files (x86)\microsoft visual studio\2017\professional\vc\tools\msvc\14.11.25503\include\xatomic.h @ 1543] 
01 00000007`aeaf83b0 00007ff9`9c9c81d8 Qt5Guid!std::_Atomic_fetch_add_4+0x77 [c:\program files (x86)\microsoft visual studio\2017\professional\vc\tools\msvc\14.11.25503\include\xatomic.h @ 1584] 
02 00000007`aeaf8400 00007ff9`9c9c81a1 Qt5Guid!std::atomic_fetch_add_explicit+0x28 [c:\program files (x86)\microsoft visual studio\2017\professional\vc\tools\msvc\14.11.25503\include\xxatomic @ 987] 
03 00000007`aeaf8430 00007ff9`9c9c6a08 Qt5Guid!std::atomic_fetch_add+0x21 [c:\program files (x86)\microsoft visual studio\2017\professional\vc\tools\msvc\14.11.25503\include\xxatomic @ 999] 
04 00000007`aeaf8460 00007ff9`9c9c4923 Qt5Guid!std::_Atomic_int::operator+++0x18 [c:\program files (x86)\microsoft visual studio\2017\professional\vc\tools\msvc\14.11.25503\include\xxatomic @ 1133] 
05 00000007`aeaf8490 00007ff9`9c9cb0d6 Qt5Guid!QAtomicOps<int>::ref<int>+0x13 [c:\users\qt\work\qt\qtbase\src\corelib\thread\qatomic_cxx11.h @ 265] 
06 00000007`aeaf84d0 00007ff9`9cba8f59 Qt5Guid!QBasicAtomicInteger<int>::ref+0x16 [c:\users\qt\work\qt\qtbase\src\corelib\thread\qbasicatomic.h @ 114] 
07 00000007`aeaf8500 00007ff9`9cb9ee00 Qt5Guid!QExplicitlySharedDataPointer<QFontPrivate>::QExplicitlySharedDataPointer<QFontPrivate>+0x39 [c:\users\qt\work\qt\qtbase\src\corelib\tools\qshareddata.h @ 185] 
08 00000007`aeaf8530 00007ff9`9caaf6aa Qt5Guid!QFont::QFont+0x20 [c:\users\qt\work\qt\qtbase\src\gui\text\qfont.cpp @ 662] 
09 00000007`aeaf8560 00007ff9`9caa8c39 Qt5Guid!QVariantPrivateSharedEx<QFont>::QVariantPrivateSharedEx<QFont>+0x3a [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qvariant_p.h @ 114] 
0a 00000007`aeaf8590 00007ff9`9caa7db3 Qt5Guid!v_construct_helper<QFont>+0x39 [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qvariant_p.h @ 130] 
0b 00000007`aeaf85d0 00007ff9`9caa7dfa Qt5Guid!v_construct<QFont>+0x23 [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qvariant_p.h @ 153] 
0c 00000007`aeaf8610 00007ff9`9caacad7 Qt5Guid!v_construct<QFont>+0x2a [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qvariant_p.h @ 161] 
0d 00000007`aeaf8650 00007ff9`9ca9e4ed Qt5Guid!QVariantConstructor<`anonymous namespace'::GuiTypesFilter>::FilteredConstructor<QFont,1>::FilteredConstructor<QFont,1>+0x27 [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qvariant_p.h @ 352] 
0e 00000007`aeaf8690 00007ff9`9caa3100 Qt5Guid!QVariantConstructor<`anonymous namespace'::GuiTypesFilter>::delegate<QFont>+0x1d [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qvariant_p.h @ 373] 
0f 00000007`aeaf86d0 00007ff9`9ca9a544 Qt5Guid!QMetaTypeSwitcher::switcher<void,QVariantConstructor<`anonymous namespace'::GuiTypesFilter> >+0x4a0 [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qmetatypeswitcher_p.h @ 74] 
10 00000007`aeaf8710 00007ff9`9dcbb84f Qt5Guid!`anonymous namespace'::construct+0x44 [c:\users\qt\work\qt\qtbase\src\gui\kernel\qguivariant.cpp @ 108] 
11 00000007`aeaf8760 00007ff9`9dcbebae Qt5Cored!QVariant::QVariant+0x9f [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qvariant.cpp @ 1840] 
12 00000007`aeaf87a0 00007ff9`9d83318d Qt5Cored!QVariant::cmp+0xde [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qvariant.cpp @ 4038] 
13 00000007`aeaf8810 00007ff9`9d82ce42 Qt5Cored!QVariant::operator!=+0x1d [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qvariant.h @ 457] 
14 00000007`aeaf8850 00007ff9`9d82d33d Qt5Cored!QVariantAnimationPrivate::setCurrentValueForProgress+0x1e2 [c:\users\qt\work\qt\qtbase\src\corelib\animation\qvariantanimation.cpp @ 290] 
15 00000007`aeaf88e0 00007ff9`9d82cc52 Qt5Cored!QVariantAnimationPrivate::recalculateCurrentInterval+0x4bd [c:\users\qt\work\qt\qtbase\src\corelib\animation\qvariantanimation.cpp @ 270] 
16 00000007`aeaf89f0 00007ff9`9d83d9bc Qt5Cored!QVariantAnimationPrivate::setDefaultStartEndValue+0x32 [c:\users\qt\work\qt\qtbase\src\corelib\animation\qvariantanimation.cpp @ 332] 
17 00000007`aeaf8a20 00007ff9`9d81b155 Qt5Cored!QPropertyAnimation::updateState+0x2ac [c:\users\qt\work\qt\qtbase\src\corelib\animation\qpropertyanimation.cpp @ 278] 
18 00000007`aeaf8c40 00007ff9`9d81a45b Qt5Cored!QAbstractAnimationPrivate::setState+0x1f5 [c:\users\qt\work\qt\qtbase\src\corelib\animation\qabstractanimation.cpp @ 989] 
19 00000007`aeaf8cc0 00007ff9`9c04c7e7 Qt5Cored!QAbstractAnimation::start+0x5b [c:\users\qt\work\qt\qtbase\src\corelib\animation\qabstractanimation.cpp @ 1358] 
1a 00000007`aeaf8d00 00007ff9`9c0b579c Qt5Widgetsd!QWidgetAnimator::animate+0x4f7 [c:\users\qt\work\qt\qtbase\src\widgets\widgets\qwidgetanimator.cpp @ 114] 
1b 00000007`aeaf8e70 00007ff9`9c106cfb Qt5Widgetsd!QDockAreaLayout::apply+0xdc [c:\users\qt\work\qt\qtbase\src\widgets\widgets\qdockarealayout.cpp @ 3228] 
1c 00000007`aeaf8ec0 00007ff9`9c10d7fa Qt5Widgetsd!QMainWindowLayoutState::apply+0x3b [c:\users\qt\work\qt\qtbase\src\widgets\widgets\qmainwindowlayout.cpp @ 678] 
1d 00000007`aeaf8ef0 00007ff9`9c10ad67 Qt5Widgetsd!QMainWindowLayout::applyState+0x3da [c:\users\qt\work\qt\qtbase\src\widgets\widgets\qmainwindowlayout.cpp @ 2710] 
1e 00000007`aeaf8fe0 00007ff9`9becb17c Qt5Widgetsd!QMainWindowLayout::setGeometry+0x247 [c:\users\qt\work\qt\qtbase\src\widgets\widgets\qmainwindowlayout.cpp @ 1957] 
1f 00000007`aeaf90a0 00007ff9`9bec9c8a Qt5Widgetsd!QLayoutPrivate::doResize+0x10c [c:\users\qt\work\qt\qtbase\src\widgets\kernel\qlayout.cpp @ 594] 
20 00000007`aeaf9160 00007ff9`9be8c150 Qt5Widgetsd!QLayout::widgetEvent+0x9a [c:\users\qt\work\qt\qtbase\src\widgets\kernel\qlayout.cpp @ 617] 
21 00000007`aeaf91c0 00007ff9`9be898c4 Qt5Widgetsd!QApplicationPrivate::notify_helper+0x160 [c:\users\qt\work\qt\qtbase\src\widgets\kernel\qapplication.cpp @ 3731] 
22 00000007`aeaf9220 00007ff9`9dc3ef96 Qt5Widgetsd!QApplication::notify+0x32f4 [c:\users\qt\work\qt\qtbase\src\widgets\kernel\qapplication.cpp @ 3687] 
23 00000007`aeaf9c20 00007ff9`9dc3f03c Qt5Cored!QCoreApplication::notifyInternal2+0x116 [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qcoreapplication.cpp @ 1084] 
24 00000007`aeaf9ca0 00007ff9`9bf372c8 Qt5Cored!QCoreApplication::forwardEvent+0x6c [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qcoreapplication.cpp @ 1100] 
25 00000007`aeaf9cd0 00007ff9`9bf35606 Qt5Widgetsd!QWidgetWindow::handleResizeEvent+0x78 [c:\users\qt\work\qt\qtbase\src\widgets\kernel\qwidgetwindow.cpp @ 803] 
26 00000007`aeaf9d50 00007ff9`9be8c188 Qt5Widgetsd!QWidgetWindow::event+0x2b6 [c:\users\qt\work\qt\qtbase\src\widgets\kernel\qwidgetwindow.cpp @ 304] 
27 00000007`aeaf9dd0 00007ff9`9be86c0f Qt5Widgetsd!QApplicationPrivate::notify_helper+0x198 [c:\users\qt\work\qt\qtbase\src\widgets\kernel\qapplication.cpp @ 3737] 
28 00000007`aeaf9e30 00007ff9`9dc3ef96 Qt5Widgetsd!QApplication::notify+0x63f [c:\users\qt\work\qt\qtbase\src\widgets\kernel\qapplication.cpp @ 3093] 
29 00000007`aeafa830 00007ff9`9dc3ee3b Qt5Cored!QCoreApplication::notifyInternal2+0x116 [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qcoreapplication.cpp @ 1084] 
2a 00000007`aeafa8b0 00007ff9`9ca547f3 Qt5Cored!QCoreApplication::sendSpontaneousEvent+0x3b [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qcoreapplication.cpp @ 1485] 
2b 00000007`aeafa8e0 00007ff9`9ca5525b Qt5Guid!QGuiApplicationPrivate::processGeometryChangeEvent+0x283 [c:\users\qt\work\qt\qtbase\src\gui\kernel\qguiapplication.cpp @ 2428] 
2c 00000007`aeafaa50 00007ff9`9ca231a5 Qt5Guid!QGuiApplicationPrivate::processWindowSystemEvent+0xeb [c:\users\qt\work\qt\qtbase\src\gui\kernel\qguiapplication.cpp @ 1855] 
2d 00000007`aeafaad0 00007ff9`9ca233d2 Qt5Guid!QWindowSystemInterface::sendWindowSystemEvents+0xd5 [c:\users\qt\work\qt\qtbase\src\gui\kernel\qwindowsysteminterface.cpp @ 1157] 
2e 00000007`aeafab40 00007ff9`a268bb6d Qt5Guid!QWindowSystemInterface::flushWindowSystemEvents+0x172 [c:\users\qt\work\qt\qtbase\src\gui\kernel\qwindowsysteminterface.cpp @ 1117] 
2f 00000007`aeafabd0 00007ff9`a26b0ecd qwindowsd!QWindowsWindow::handleWmPaint+0x21d [c:\users\qt\work\qt\qtbase\src\plugins\platforms\windows\qwindowswindow.cpp @ 2031] 
30 00000007`aeafacb0 00007ff9`a26a7845 qwindowsd!QWindowsContext::windowsProc+0x100d [c:\users\qt\work\qt\qtbase\src\plugins\platforms\windows\qwindowscontext.cpp @ 1221] 
31 00000007`aeafb1c0 00007ffa`02f6681d qwindowsd!qWindowsWndProc+0x105 [c:\users\qt\work\qt\qtbase\src\plugins\platforms\windows\qwindowscontext.cpp @ 1583] 
32 00000007`aeafb330 00007ffa`02f663ec USER32!UserCallWinProcCheckWow+0x2bd
33 00000007`aeafb4c0 00007ffa`02f72d03 USER32!DispatchClientMessage+0x9c
34 00000007`aeafb520 00007ffa`03d3fe24 USER32!_fnDWORD+0x33
35 00000007`aeafb580 00007ffa`01601184 ntdll!KiUserCallbackDispatcherContinue
36 00000007`aeafb608 00007ffa`02f64f7a win32u!NtUserMessageCall+0x14
37 00000007`aeafb610 00007ffa`02f6470f USER32!RealDefWindowProcWorker+0x1fa
38 00000007`aeafb710 00007ff9`feef984e USER32!RealDefWindowProcW+0x4f
39 00000007`aeafb750 00007ff9`fef125a2 UxTheme!DoMsgDefault+0x2e [shell\themes\uxtheme\handlers.cpp @ 550] 
3a 00000007`aeafb790 00007ff9`feefc49f UxTheme!OnDwpSysCommand+0x32 [shell\themes\uxtheme\nctheme.cpp @ 7568] 
3b 00000007`aeafb7c0 00007ff9`feefbf81 UxTheme!_ThemeDefWindowProc+0x50f [shell\themes\uxtheme\sethook.cpp @ 1068] 
3c 00000007`aeafb9a0 00007ffa`02f64c4f UxTheme!ThemeDefWindowProcW+0x11 [shell\themes\uxtheme\sethook.cpp @ 1110] 
3d 00000007`aeafb9e0 00007ff9`a26a7a77 USER32!DefWindowProcW+0x1bf
3e 00000007`aeafba50 00007ffa`02f6681d qwindowsd!qWindowsWndProc+0x337 [c:\users\qt\work\qt\qtbase\src\plugins\platforms\windows\qwindowscontext.cpp @ 1593] 
3f 00000007`aeafbbc0 00007ffa`02f663ec USER32!UserCallWinProcCheckWow+0x2bd
40 00000007`aeafbd50 00007ffa`02f72d03 USER32!DispatchClientMessage+0x9c
41 00000007`aeafbdb0 00007ffa`03d3fe24 USER32!_fnDWORD+0x33
42 00000007`aeafbe10 00007ffa`01601184 ntdll!KiUserCallbackDispatcherContinue
43 00000007`aeafbe98 00007ffa`02f64f7a win32u!NtUserMessageCall+0x14
44 00000007`aeafbea0 00007ffa`02f6470f USER32!RealDefWindowProcWorker+0x1fa
45 00000007`aeafbfa0 00007ff9`feef984e USER32!RealDefWindowProcW+0x4f
46 00000007`aeafbfe0 00007ff9`fef124f7 UxTheme!DoMsgDefault+0x2e [shell\themes\uxtheme\handlers.cpp @ 550] 
47 00000007`aeafc020 00007ff9`feefc49f UxTheme!OnDwpNcLButtonDown+0xa7 [shell\themes\uxtheme\nctheme.cpp @ 7159] 
48 00000007`aeafc060 00007ff9`feefbf81 UxTheme!_ThemeDefWindowProc+0x50f [shell\themes\uxtheme\sethook.cpp @ 1068] 
49 00000007`aeafc240 00007ffa`02f64c4f UxTheme!ThemeDefWindowProcW+0x11 [shell\themes\uxtheme\sethook.cpp @ 1110] 
4a 00000007`aeafc280 00007ff9`a26a7a77 USER32!DefWindowProcW+0x1bf
4b 00000007`aeafc2f0 00007ffa`02f6681d qwindowsd!qWindowsWndProc+0x337 [c:\users\qt\work\qt\qtbase\src\plugins\platforms\windows\qwindowscontext.cpp @ 1593] 
4c 00000007`aeafc460 00007ffa`02f66212 USER32!UserCallWinProcCheckWow+0x2bd
4d 00000007`aeafc5f0 00007ff9`9dd00a4a USER32!DispatchMessageWorker+0x1e2
4e 00000007`aeafc670 00007ff9`a2765c34 Qt5Cored!QEventDispatcherWin32::processEvents+0x56a [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qeventdispatcher_win.cpp @ 640] 
4f 00000007`aeaff800 00007ff9`9dc39173 qwindowsd!QWindowsGuiEventDispatcher::processEvents+0x34 [c:\users\qt\work\qt\qtbase\src\platformsupport\eventdispatchers\qwindowsguieventdispatcher.cpp @ 74] 
50 00000007`aeaff840 00007ff9`9dc393ae Qt5Cored!QEventLoop::processEvents+0x63 [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qeventloop.cpp @ 139] 
51 00000007`aeaff880 00007ff9`9dc3cadf Qt5Cored!QEventLoop::exec+0x18e [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qeventloop.cpp @ 225] 
52 00000007`aeaff930 00007ff9`9ca4f838 Qt5Cored!QCoreApplication::exec+0x15f [c:\users\qt\work\qt\qtbase\src\corelib\kernel\qcoreapplication.cpp @ 1385] 
53 00000007`aeaff9e0 00007ff9`9be865ba Qt5Guid!QGuiApplication::exec+0x18 [c:\users\qt\work\qt\qtbase\src\gui\kernel\qguiapplication.cpp @ 1785] 
*** WARNING: Unable to verify checksum for QUrhoApp_d.exe
54 00000007`aeaffa10 00007ff6`efece1ae Qt5Widgetsd!QApplication::exec+0xa [c:\users\qt\work\qt\qtbase\src\widgets\kernel\qapplication.cpp @ 2894] 
55 00000007`aeaffa40 00007ff6`efed1181 QUrhoApp_d!QUrho::Application::execute+0xee [D:\projects\QUrhoApp\Sources\Application.cpp @ 15] 
56 00000007`aeaffc10 00007ff6`f0a778f5 QUrhoApp_d!main+0x51 [D:\projects\QUrhoApp\Sources\Main.cpp @ 5] 
57 00000007`aeaffd30 00007ff6`f0a73e22 QUrhoApp_d!WinMain+0xf5 [c:\users\qt\work\qt\qtbase\src\winmain\qtmain_win.cpp @ 97] 
58 00000007`aeaffdb0 00007ff6`f0a73d0e QUrhoApp_d!invoke_main+0x32 [d:\agent\_work\2\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl @ 107] 
59 00000007`aeaffdf0 00007ff6`f0a73bce QUrhoApp_d!__scrt_common_main_seh+0x12e [d:\agent\_work\2\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl @ 288] 
5a 00000007`aeaffe60 00007ff6`f0a73eb9 QUrhoApp_d!__scrt_common_main+0xe [d:\agent\_work\2\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl @ 331] 
5b 00000007`aeaffe90 00007ffa`03337bd4 QUrhoApp_d!WinMainCRTStartup+0x9 [d:\agent\_work\2\s\src\vctools\crt\vcstartup\src\startup\exe_winmain.cpp @ 17] 
5c 00000007`aeaffec0 00007ffa`03d0cee1 KERNEL32!BaseThreadInitThunk+0x14
5d 00000007`aeaffef0 00000000`00000000 ntdll!RtlUserThreadStart+0x21

```
Looks like problem inside Qt. I will try to recompile Qt (for now I am using prebuild binaries), hope it will help. 

@Elendil 
For now I am using Urho 1.7.1 from GithHub release tag. I will try to use older version if recompilation of Qt will not help. 

@weitjong
I will give it a try and report here.

-------------------------

VladBolotov | 2019-10-04 05:28:10 UTC | #14

Looks like my problem was solved by switching back from 1.7.1 (2ac4f89) to 1.7 ( 9941b25) from GitHub Release. Updating/Recompiling Qt did not solve my problem. 
@weitjong 
Reverting the #2256 did not help at all. Looks like there is regression since 1.7.

UPD:
Just created thread on Qt forum: https://forum.qt.io/topic/107442/random-crash-on-window-resize may be Its internal Qt problem.

-------------------------

weitjong | 2019-10-04 05:46:38 UTC | #15

It does not make any sense to me because 1.7.1 is basically a re-release of 1.7 with a very minor change for GCC. It does not explain why 1.7 works but 1.7.1 failed for your Windows problem.

-------------------------

VladBolotov | 2019-10-04 06:50:35 UTC | #16

I don't know either. I've just tested app with 1.7 and 1.7.1 and here is the difference: https://youtu.be/toyjULLPoyk . 

If I can help you somehow determine where the problem is just let me know.

-------------------------

weitjong | 2019-10-04 08:12:59 UTC | #17

The release 1.7.1 is a tag from this commit SHA.

https://github.com/urho3d/Urho3D/commits/9941b25502c7fe96d5a3c11b0f574d95d043b04f

It is one commit after the commit 2ac4f89a86bc9f978a8212883ebeb82ba873b53c (which is exactly 1.7).

The only thing I need you to do is to double check how you build the library.

-------------------------

VladBolotov | 2019-10-04 08:30:53 UTC | #18

Oh... Sorry looks like I made mistake and put master branch into 1.7.1 folder. Sorry for this. 

How do I build Urho3D for Windows:
1. Download ZIP file.
2. Unzip it into D:\libs\urho3Dxxx
3. Open CMD
4. cmake . -DCMAKE_BUILD_TYPE=Debug -DURHO3D_SAMPLES=Disable
5. cmake --build . -j4
6. Add set(ENV{URHO3D_HOME} D:/lib/urho3Dxxx) to my CMakeLists.txt

-------------------------

weitjong | 2019-10-04 16:52:45 UTC | #19

At this point I cannot really trust your past test result. I will really appreciate if you can retest building from master branch after reverting the commit I suspected that causing your QT problem. If you do have time to retest, please ensure you are using out-of-source build tree. Otherwise you may be just seeing things again in your retest.

-------------------------

VladBolotov | 2019-10-07 06:14:26 UTC | #20

So. I am feeling dumb now.

I’ve just clone master branch and revert commit that you mentored. Here is the patch.
```
commit 13cf594c94272e3dbb3919eb38bb1b5106d5e2cb
Author: VladBolotov <vladislav.bolotov@gmail.com>
Date:   Mon Oct 7 14:05:14 2019 +1000

    Revert "On Windows use SDL event watch to repaint the window while resizing"
    
    This reverts commit b3d2573eb5e2bb57e99750b12994c6dbdfbeb113.

diff --git a/Source/Urho3D/Input/Input.cpp b/Source/Urho3D/Input/Input.cpp
index f96e49fdc..cf10b2e98 100644
--- a/Source/Urho3D/Input/Input.cpp
+++ b/Source/Urho3D/Input/Input.cpp
@@ -38,11 +38,6 @@
 #include "../UI/Text.h"
 #include "../UI/UI.h"
 
-#ifdef _WIN32
-#include "../Engine/Engine.h"
-#endif
-
-
 #include <SDL/SDL.h>
 
 #ifdef __EMSCRIPTEN__
@@ -300,32 +295,6 @@ int EmscriptenInput::HandleSDLEvents(void* userData, SDL_Event* event)
 
 #endif
 
-#ifdef _WIN32
-// On Windows repaint while the window is actively being resized.
-int Win32_ResizingEventWatcher(void* data, SDL_Event* event)
-{
-    if (event->type == SDL_WINDOWEVENT && event->window.event == SDL_WINDOWEVENT_RESIZED)
-    {
-        SDL_Window* win = SDL_GetWindowFromID(event->window.windowID);
-        if (win == (SDL_Window*)data)
-        {
-            if (auto* ctx = (Context*)SDL_GetWindowData(win, "URHO3D_CONTEXT"))
-            {
-                if (auto* graphics = ctx->GetSubsystem<Graphics>())
-                {
-                    if (graphics->IsInitialized())
-                    {
-                        graphics->OnWindowResized();
-                        ctx->GetSubsystem<Engine>()->RunFrame();
-                    }
-                }
-            }
-        }
-    }
-    return 0;
-}
-#endif
-
 void JoystickState::Initialize(unsigned numButtons, unsigned numAxes, unsigned numHats)
 {
     buttons_.Resize(numButtons);
@@ -1543,15 +1512,6 @@ void Input::Initialize()
     SubscribeToEvent(E_ENDFRAME, URHO3D_HANDLER(Input, HandleEndFrame));
 #endif
 
-#ifdef _WIN32
-    // Register callback for resizing in order to repaint.
-    if (SDL_Window* window = graphics_->GetWindow())
-    {
-        SDL_SetWindowData(window, "URHO3D_CONTEXT", GetContext());
-        SDL_AddEventWatch(Win32_ResizingEventWatcher, window);
-    }
-#endif
-
     URHO3D_LOGINFO("Initialized input");
 }
```
I did everything in the same way what that I did before. But good news, I can not reproduce this error anymore. I have no idea what I did wrong before. Thank you for your help.

**UPD**: 
Never mind I am just the victim of my retardness. 

~~But one more thing.~~

~~Now compiler complain about unresolved symbols:~~
```
LINK Pass 1: command "C:\PROGRA~2\MICROS~1\2019\COMMUN~1\VC\Tools\MSVC\1421~1.277\bin\Hostx64\x64\link.exe /nologo @CMakeFiles\QUrhoApp.dir\objects1.rsp /out:bin\QUrhoApp_d.exe /implib:QUrhoApp_d.lib /pdb:D:\projects\QUrhoApp\cmake-build-debug\bin\QUrhoApp_d.pdb /version:0.0 /machine:x64 /debug /INCREMENTAL /subsystem:windows D:\lib\Urho3D\lib\Urho3D_d.lib user32.lib gdi32.lib winmm.lib imm32.lib ole32.lib oleaut32.lib version.lib uuid.lib ws2_32.lib iphlpapi.lib winmm.lib dbghelp.lib d3dcompiler.lib d3d9.lib D:\tools\vcpkg\installed\x64-windows\debug\lib\Qt5Widgetsd.lib D:\tools\vcpkg\installed\x64-windows\debug\lib\Qt5Guid.lib D:\tools\vcpkg\installed\x64-windows\debug\lib\Qt5Xmld.lib imm32.lib ole32.lib oleaut32.lib version.lib uuid.lib ws2_32.lib iphlpapi.lib dbghelp.lib d3dcompiler.lib d3d9.lib D:\tools\vcpkg\installed\x64-windows\debug\lib\Qt5Cored.lib D:\tools\vcpkg\installed\x64-windows\debug\lib\manual-link\qtmaind.lib kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib /MANIFEST /MANIFESTFILE:CMakeFiles\QUrhoApp.dir/intermediate.manifest CMakeFiles\QUrhoApp.dir/manifest.res" failed (exit code 1120) with the following output:
   Creating library QUrhoApp_d.lib and object QUrhoApp_d.exp
Urho3D_d.lib(hid.obj) : error LNK2019: unresolved external symbol __imp_SetupDiEnumDeviceInfo referenced in function hid_enumerate
Urho3D_d.lib(hid.obj) : error LNK2019: unresolved external symbol __imp_SetupDiDestroyDeviceInfoList referenced in function hid_enumerate
Urho3D_d.lib(hid.obj) : error LNK2019: unresolved external symbol __imp_SetupDiEnumDeviceInterfaces referenced in function hid_enumerate
Urho3D_d.lib(hid.obj) : error LNK2019: unresolved external symbol __imp_SetupDiGetDeviceInterfaceDetailA referenced in function hid_enumerate
Urho3D_d.lib(hid.obj) : error LNK2019: unresolved external symbol __imp_SetupDiGetClassDevsA referenced in function hid_enumerate
Urho3D_d.lib(hid.obj) : error LNK2019: unresolved external symbol __imp_SetupDiGetDeviceRegistryPropertyA referenced in function hid_enumerate
bin\QUrhoApp_d.exe : fatal error LNK1120: 6 unresolved externals
NMAKE : fatal error U1077: '"C:\Users\omfg\AppData\Local\JetBrains\CLion 2019.2.1\bin\cmake\win\bin\cmake.exe"' : return code '0xffffffff'
Stop.
NMAKE : fatal error U1077: '"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.21.27702\bin\HostX64\x64\nmake.exe"' : return code '0x2'
Stop.
NMAKE : fatal error U1077: '"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.21.27702\bin\HostX64\x64\nmake.exe"' : return code '0x2'
Stop.
NMAKE : fatal error U1077: '"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.21.27702\bin\HostX64\x64\nmake.exe"' : return code '0x2'
Stop.
```
~~This problem appears just now. And was solved by adding setupapi into UrhoCommon.~~
```
commit 150e98c798938c70e4322ecb3d614db21b190ed9 
Author: VladBolotov <vladislav.bolotov@gmail.com>
Date:   Mon Oct 7 14:31:58 2019 +1000

    Add missing win32 library (setupapi)

diff --git a/CMake/Modules/UrhoCommon.cmake b/CMake/Modules/UrhoCommon.cmake
index e715a4807..d56ad8146 100644
--- a/CMake/Modules/UrhoCommon.cmake
+++ b/CMake/Modules/UrhoCommon.cmake
@@ -861,7 +861,7 @@ macro (define_dependency_libs TARGET)
     # ThirdParty/SDL external dependency
     if (${TARGET} MATCHES SDL|Urho3D)
         if (WIN32)
-            list (APPEND LIBS user32 gdi32 winmm imm32 ole32 oleaut32 setupapi version uuid)
+            list (APPEND LIBS user32 gdi32 winmm imm32 ole32 oleaut32 setupapi version uuid setupapi)
         elseif (APPLE)
             list (APPEND LIBS iconv)
         elseif (ANDROID)
```

-------------------------

JTippetts1 | 2019-10-07 05:42:30 UTC | #21

You might have some build environment problems, if you had to add setupapi to UrhoCommon yourself, since it should be in there already from commit [bcd8715](https://github.com/urho3d/Urho3D/commit/bcd8715e222723498e1e9d44ba12f239655d194c). You might try building g completely clean from master, entirely fresh pull, otherwise it appears your results are untrustworthy.

-------------------------

VladBolotov | 2019-10-07 06:16:58 UTC | #22

Stupid me. I've just double added setupapi. "**setupapi** version uuid **setupapi**". Problem appears because I've used old UrhoCommon inside my CMAKE_MODULE_PATH.

-------------------------

weitjong | 2019-10-18 06:07:49 UTC | #23

Thanks for confirming the revert of the commit fixes your issue. I wonder the crash just manifests itself for Qt external window use case or it also crashes for normal Windows use case (window managed by SDL)?

-------------------------

VladBolotov | 2019-10-18 06:28:53 UTC | #24

For now It’s looks like Qt internal bug for me (https://bugreports.qt.io/browse/QTBUG-64375). I will try to use SDL “native” window on Monday or Tuesday and let you know in this thread. Is it okay?

-------------------------

VladBolotov | 2019-10-22 07:01:33 UTC | #25

I’ve played with samples resizing and could not get it crashed. So, the problem appears only with external Window which is not created by SDL (Qt in my case) and looks like problem is Windows specific.  One more thing, I did not saw glitches shown in https://github.com/urho3d/Urho3D/issues/2150. 

![Capture|629x500,50%](upload://6vAovpiS0FZ5J4aSaDvHBftxOvW.png)

-------------------------

weitjong | 2019-10-22 07:56:54 UTC | #26

Thanks for your time investigating this.

-------------------------

Modanung | 2019-10-22 13:59:57 UTC | #27

Related ManaWarg issue:

https://gitlab.com/luckeyproductions/manawarg/issues/1

-------------------------

