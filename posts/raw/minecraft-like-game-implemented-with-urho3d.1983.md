xyz | 2017-01-02 01:12:03 UTC | #1

Hi, I have released a minecraft like game demo implemented with urho3d. :smiley:

google play link:
[url]https://play.google.com/store/apps/details?id=com.xygamestudio.lostworld[/url]

app store link:
[url]https://itunes.apple.com/cn/app/lost-world-building/id1106404042?l=en&mt=8[/url]

-------------------------

rku | 2017-01-02 01:12:03 UTC | #2

Thats pretty cool *thumbs-up*. Whats your experience using urho for mobile? Anything you would like to share?

-------------------------

cadaver | 2017-01-02 01:12:03 UTC | #3

Nice! Minecraft scenario is something I don't think the engine would do well out of the box - done naively (StaticModel per block) you'd likely get horrible performance, so custom geometry generation is a must. I'd be interested to know, did you feel like the engine helped or hindered the rendering, compared to e.g. if you had done everything using raw OpenGL?

-------------------------

Bananaft | 2017-01-02 01:12:04 UTC | #4

Philips i928, works alright. Great work. Don't like the movement buttons, wold prefer virtual joystick. Also, I suggest adding fog.

-------------------------

xyz | 2017-01-02 01:12:04 UTC | #5

[quote="cadaver"]Nice! Minecraft scenario is something I don't think the engine would do well out of the box - done naively (StaticModel per block) you'd likely get horrible performance, so custom geometry generation is a must. I'd be interested to know, did you feel like the engine helped or hindered the rendering, compared to e.g. if you had done everything using raw OpenGL?[/quote]

No, everything is just using urho3d, the chunks of the world is generated with custom geometry, and only generated the visible faces. :slight_smile:

-------------------------

xyz | 2017-01-02 01:12:04 UTC | #6

[quote="Bananaft"]Philips i928, works alright. Great work. Don't like the movement buttons, wold prefer virtual joystick. Also, I suggest adding fog.[/quote]

I have added fog, but not look good.

-------------------------

sabotage3d | 2017-01-02 01:12:12 UTC | #7

I tested your game on snapdragon 650, but I can only see white screen and the controls. Can you share a bit more on how did you implement adds for Android and IOS?

-------------------------

umen | 2017-01-02 01:12:19 UTC | #8

Hey
I tested the game on simple  iphone 5 iOS 8.2 and it is working great! fast and smooth . 
I have question , 
as Urho3d do not compile outof the box with real iOS device which are lower then iOS 9 
How did you succeed to compile it for iOS?
Did you apply the fixes which needed to the engine? 
As i had always problem with the iOS port .
see my topics
[url]http://discourse.urho3d.io/t/ios-8-getting-resource-prefix-path-in-01-helloworld/1831/1[/url]
[url]http://discourse.urho3d.io/t/ios-skipped-autoload-path-autoload-exception-in-deployme/1624/1[/url]

Its will be  much appreciated if you share your experience with the process 
Thanks!

-------------------------

xyz | 2017-01-02 01:12:20 UTC | #9

[quote="umen"]Hey
I tested the game on simple  iphone 5 iOS 8.2 and it is working great! fast and smooth . 
I have question , 
as Urho3d do not compile outof the box with real iOS device which are lower then iOS 9 
How did you succeed to compile it for iOS?
Did you apply the fixes which needed to the engine? 
As i had always problem with the iOS port .
see my topics
[url]http://discourse.urho3d.io/t/ios-8-getting-resource-prefix-path-in-01-helloworld/1831/1[/url]
[url]http://discourse.urho3d.io/t/ios-skipped-autoload-path-autoload-exception-in-deployme/1624/1[/url]

Its will be  much appreciated if you share your experience with the process 
Thanks![/quote]

Sorry, I have't encountered your compiling problem, I just build urho3d code like this,
[code]
./cmake_ios.sh $URHO3D_BUILD_DIR/ios -DURHO3D_SAMPLES=0 -DURHO3D_LUA=0 -DURHO3D_ANGELSCRIPT=0 -DURHO3D_NETWORK=0 -DURHO3D_PHYSICS=1 -DURHO3D_NAVIGATION=0 -DURHO3D_URHO2D=1 -DURHO3D_TOOLS=0 -DURHO3D_PROFILING=0 -DURHO3D_LOGGING=0
[/code]
You can enable build sample by -DURHO3D_SAMPLES=1

If you want to create your own Xcode project, you can run
[code]
rake scaffolding dir=/to/your/project/path  project=yourProjectName  target=yourTargetName
[/code]
then, enter your project dir, and run
[code]
./cmake_ios.sh  /to/your/build/path  -DURHO3D_SAMPLES=0 -DURHO3D_PHYSICS=1 -DURHO3D_HOME=/to/urho3d/build/path/ios
[/code]

Good luck!  :smiley:

-------------------------

xyz | 2017-01-02 01:12:22 UTC | #10

[quote="sabotage3d"]I tested your game on snapdragon 650, but I can only see white screen and the controls. Can you share a bit more on how did you implement adds for Android and IOS?[/quote]

Thank you, I have fixed the bug, you can update the new version.  :wink:  About adds implementation, I just referenced google admob doc.

-------------------------

umen | 2017-01-02 01:12:22 UTC | #11

Thanks , i will try it
Question :
Did you mange to run the examples on the device ?

-------------------------

xyz | 2017-01-02 01:12:22 UTC | #12

[quote="umen"]Thanks , i will try it
Question :
Did you mange to run the examples on the device ?[/quote]

I just tested the samples on my ipad4, and every thing is ok, just change the bundle id by removing '_' character.

-------------------------

umen | 2017-01-02 01:12:22 UTC | #13

Thanks! 
is the iOS version is below 9 ? i had problems with iOS 8+

-------------------------

xyz | 2017-01-02 01:12:22 UTC | #14

[quote="umen"]Thanks! 
is the iOS version is below 9 ? i had problems with iOS 8+[/quote]

My device version is 9.3, but I think iOS 7+ is ok.

-------------------------

