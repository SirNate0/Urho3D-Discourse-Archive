att | 2017-01-02 00:59:11 UTC | #1

Hi,

I encountered a problem, when setting portrait orientation on iPhone device, the app just crashed.
Here is the crash log,

2014-05-16 22:24:15.754 Urho3DPlayer[10484:60b] *** Terminating app due to uncaught exception 'UIApplicationInvalidInterfaceOrientation', reason: 'Supported orientations has no common orientation with the application, and shouldAutorotate is returning YES'
*** First throw call stack:
(
	0   CoreFoundation                      0x031311e4 __exceptionPreprocess + 180
	1   libobjc.A.dylib                     0x03dac8e5 objc_exception_throw + 44
	2   CoreFoundation                      0x03130fbb +[NSException raise:format:] + 139
	3   UIKit                               0x020285f2 -[UIViewController __supportedInterfaceOrientations] + 509
	4   UIKit                               0x0202861e -[UIViewController __withSupportedInterfaceOrientation:apply:] + 34
	5   UIKit                               0x02028c92 -[UIViewController setInterfaceOrientation:] + 139
	6   UIKit                               0x0201da8d -[UIViewController viewDidMoveToWindow:shouldAppearOrDisappear:] + 999
	7   UIKit                               0x01f6340c -[UIView(Internal) _didMoveFromWindow:toWindow:] + 1534
	8   UIKit                               0x01f5a96f __45-[UIView(Hierarchy) _postMovedFromSuperview:]_block_invoke + 158
	9   UIKit                               0x01f5a7fb -[UIView(Hierarchy) _postMovedFromSuperview:] + 260
	10  UIKit                               0x01f65dd4 -[UIView(Internal) _addSubview:positioned:relativeTo:] + 1875
	11  UIKit                               0x01f58dba -[UIView(Hierarchy) addSubview:] + 56
	12  Urho3DPlayer                        0x0082c31d UIKit_GL_CreateContext + 973
	13  Urho3DPlayer                        0x00827e42 SDL_GL_CreateContext + 226
	14  Urho3DPlayer                        0x000e3e7a _ZN6Urho3D8Graphics7RestoreEv + 74
	15  Urho3DPlayer                        0x000e3398 _ZN6Urho3D8Graphics7SetModeEiibbbbbi + 2024
	16  Urho3DPlayer                        0x00062327 _ZN6Urho3D6Engine10InitializeERKNS_7HashMapINS_15ShortStringHashENS_7VariantEEE + 12407
	17  Urho3DPlayer                        0x00051c6e _ZN6Urho3D11Application3RunEv + 270
	18  Urho3DPlayer                        0x0000506b _Z14RunApplicationv + 187
	19  Urho3DPlayer                        0x0000517c SDL_main + 44
	20  Urho3DPlayer                        0x00829ceb -[SDLUIKitDelegate postFinishLaunch] + 75
	21  Foundation                          0x018d15ec __NSFireDelayedPerform + 372
	22  CoreFoundation                      0x030efac6 __CFRUNLOOP_IS_CALLING_OUT_TO_A_TIMER_CALLBACK_FUNCTION__ + 22
	23  CoreFoundation                      0x030ef4ad __CFRunLoopDoTimer + 1181
	24  CoreFoundation                      0x030d7538 __CFRunLoopRun + 1816
	25  CoreFoundation                      0x030d69d3 CFRunLoopRunSpecific + 467
	26  CoreFoundation                      0x030d67eb CFRunLoopRunInMode + 123
	27  GraphicsServices                    0x045575ee GSEventRunModal + 192
	28  GraphicsServices                    0x0455742b GSEventRun + 104
	29  UIKit                               0x01ef9f9b UIApplicationMain + 1225
	30  Urho3DPlayer                        0x008294bb main + 347
	31  libdyld.dylib                       0x03b7a701 start + 1
	32  ???                                 0x00000001 0x0 + 1

-------------------------

cadaver | 2017-01-02 00:59:11 UTC | #2

What do you mean by setting portrait orientation? Do you mean physically turning the device so that it changes to portrait mode, or using the engine startup parameters to configure the allowed orientations to portrait?

-------------------------

att | 2017-01-02 00:59:12 UTC | #3

I just set the portrait orientation in Xcode, how can I set allowed orientations by engine startup parameters?

-------------------------

friesencr | 2017-01-02 00:59:12 UTC | #4

Startup parameters can be entered via command line or during the setup method of application.

On mobile devices command line args are spoofed via text file.

To quote the docs:
On Android and iOS the command line can not be entered, so it is instead read from the file Bin/Data/CommandLine.txt. By default the NinjaSnowWar example will be run.

Command line options:
-landscape   Use landscape orientations (iOS only, default)
-portrait    Use portrait orientations (iOS only)

To set it programatically an engine paparameter can be set during initialization.  In engine.cpp you can see how the engine parameters are initialized.  There is a parameter called "Orientation"

[code]
            else if (argument == "landscape")
                ret["Orientations"] = "LandscapeLeft LandscapeRight " + ret["Orientations"].GetString();
            else if (argument == "portrait")
                ret["Orientations"] = "Portrait PortraitUpsideDown " + ret["Orientations"].GetString();[/code]

I believe these orientation settings are being passed directly to sdl.

[wiki.libsdl.org/SDL_HINT_ORIENTATIONS](http://wiki.libsdl.org/SDL_HINT_ORIENTATIONS)

-------------------------

cadaver | 2017-01-02 00:59:13 UTC | #5

Likely, setting the orientations through Xcode causes a mismatch with how SDL will setup them. Using the commandline / engine parameters should work OK.

-------------------------

