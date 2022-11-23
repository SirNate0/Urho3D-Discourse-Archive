orefkov | 2017-12-21 22:15:29 UTC | #1

Hi All!
I present my new game - "Adrenalin Sky".

[Link to Play Market](https://play.google.com/store/apps/details?id=com.horovo.games.sky.r)

> Exciting races in free fall. When a racing car is just your body.
> Go through five high-speed trails, controlling your fall with accelerometer.

Gameplay video

https://www.youtube.com/watch?v=6A_32_10tQA

[details="Screenshots"]
![2017-12-17 09-23-25|690x388](upload://oiZuvrU0ID34jDvrlw6f0f8VhLR.jpg)![2017-12-17 09-36-16|690x388](upload://rFazadf6AUDIEZAA6xoJPJd2bZK.jpg)
![2017-12-17 11-35-22|690x388](upload://6FMHsCfqGP97ZptYTTOH7M02S5s.jpg)![2017-12-17 09-31-17|690x388](upload://lEKkjkjT0fwVKhbk38iIkVDhgUl.jpg)![2017-12-17 09-23-01|690x388](upload://hFbdDdvlufEZCHll6MQigsB6es4.jpg)![2017-12-17 09-27-10|690x388](upload://3LtxRKHQ6OKJYpzQoP3kVwfTNjh.jpg)![2017-12-17 09-28-05|690x388](upload://nakwvjt1njGzpAQJCsBqNEjXnJb.jpg)
[/details]

Game was created in two weeks from first idea to play market. Based on urho3dplayer and implemented in AngelScript.
If there are technical questions on the implementation of the game - I am ready to respond.

-------------------------

Miegamicis | 2017-12-18 07:26:40 UTC | #2

Awesome! Will try this out!

-------------------------

elix22 | 2017-12-18 07:51:10 UTC | #3

Tried it 
It's crashing on 7.0 device 
It's working on 4.4 device , however very unstable , it gets stuck during the game .

It's a nice idea , my advice is to make it much more stable prior of releasing it to the Market .
Due to the overwhelming amount of games , players tend to ditch unstable games and never try them again.

Crash log snippet:
12-18 09:40:00.670  3293  3293 E art     : No implementation found for void org.libsdl.app.SDLActivity.onNativeResize(int, int, int, float) (tried Java_org_libsdl_app_SDLActivity_onNativeResize and Java_org_libsdl_app_SDLActivity_onNativeResize__IIIF): com.horovo.games.sky.r
12-18 09:40:00.676  3293  3293 D AndroidRuntime: Shutting down VM: com.horovo.games.sky.r
12-18 09:40:00.677  1748  6937 I am_crash: [3293,0,com.horovo.games.sky.r,948452932,java.lang.UnsatisfiedLinkError,No implementation found for void org.libsdl.app.SDLActivity.onNativeResize(int, int, int, float) (tried Java_org_libsdl_app_SDLActivity_onNativeResize and Java_org_libsdl_app_SDLActivity_onNativeResize__IIIF),SDLActivity.java,-2]: system_server
12-18 09:40:00.678  1748  6937 I am_finish_activity: [0,260378209,225,com.horovo.games.sky.r/com.horovo.games.all.Urho3D,force-crash]: system_server

-------------------------

orefkov | 2017-12-18 07:53:51 UTC | #4

Thanks for test and log!

-------------------------

orefkov | 2017-12-18 08:09:52 UTC | #5

Can you look at log some one about errors in loading urho3dplayer.so - seems it can not loaded.

-------------------------

johnnycable | 2017-12-18 09:43:10 UTC | #6

Post the monitor log about the errors... My android setup is broken atm, but maybe I can recognise an error I've already seen in the past...

-------------------------

orefkov | 2017-12-19 10:50:06 UTC | #7

I do not have device with Android 7. I tested game on all my five android devices, and on all it worked well.
In any case, if there are problems on android 7, then they are hidden in the urho3d engine itself, since I use the stock urho3Dplayer plus several of my scripts on AngelScript.
In the given piece of the log it is written that the function Java_org_libsdl_app_SDLActivity_onNativeResize is not found, but it is exist in libUrho3DPlayer.so. Likely libUrho3DPlayer.so could not loaded.

-------------------------

orefkov | 2017-12-19 13:32:24 UTC | #8

Im install Android7 emulator and can solve problem with onNativeResize.

The reason was not in the version of the android, but in the architecture of the processor.
In my build, I included armv7 and x86 version of urho3DPlayer, but in the librarys for displaying ads were included native libraries for armv8 and x86_64, located in separate folders. So when the game was run on an armv8 or x86_64 processor, the android found these libraries first and used them, and set path for load native libraries to lib/armv8 or lib/x86_x64, and not load armv7 or x86 versions of urho3DPlayer. When I removed these versions of the libraries and left only armv7 and x86 - everything started. Now I will updated release in google play.

-------------------------

elix22 | 2017-12-19 15:54:25 UTC | #9

Downloaded from Google Play
I verified it on real Android 7 device .
It works fine now.

-------------------------

orefkov | 2017-12-19 16:09:14 UTC | #10

Many thanks for help in testing

-------------------------

Eugene | 2017-12-19 16:13:23 UTC | #11

Suggestions:

1. Reduce background parallax
2. (Complicated) Add some simple version of parallax mapping for background.

-------------------------

orefkov | 2017-12-19 17:05:18 UTC | #12

In theory, given that the approximate altitude of the flight is 3 km, and the shift of the character in the sides is 3-5 meters, the geometrically correct paralax will simply be a stationary background :) Therefore, I did an exaggeratedly large paralax to accentuate the movement.

-------------------------

johnnycable | 2017-12-19 18:30:26 UTC | #13

It confirm that building for android in st different than armv7 looks like to be no point. Complicacies and potential bugs are a lot in respect to apparently scarce performance gains...
Also, few devices have more than 3 gb mem... so no mem gains...
And X86... just tegra out there, if I'm not mistaken... but how many tegra tablets are still there? 0,7%?

-------------------------

Eugene | 2017-12-19 19:58:47 UTC | #14

[quote="orefkov, post:12, topic:3863"]
the geometrically correct paralax will simply be a stationary background
[/quote]

I'm not against accentuating. I suggest you to make it smaller. It's too unreal now.
Like iOS floating desktop, if you know. Desktop background on iOS is shifting for few millimeters when phone/tab is physically rotated.

-------------------------

Lumak | 2018-01-03 21:28:08 UTC | #15

This is so inspiring. One of my biggest set back in game dev is coming up with great game ideas. I have many but none that's inspiring. I hope this game will be successful!

Suggestion: adding codingmonkey's tail generator might enhance the game -- I can't find the link to it, though.

-------------------------

Modanung | 2018-01-03 22:05:56 UTC | #16

@Lumak These days Urho3D comes with a `RibbonTrail` component.

-------------------------

orefkov | 2018-01-03 22:12:13 UTC | #17

RibbonTrail worked on moves in world coordinates, but in this game character in world coordinates stay on one place, only rings and coins moved, due on float precession on mobile GPUs. Therefore, I use particles that fly upward to simulate motion.

-------------------------

Eugene | 2018-01-04 22:34:24 UTC | #18

[quote="orefkov, post:17, topic:3863"]
RibbonTrail worked on moves in world coordinates, but in this game character in world coordinates stay on one place
[/quote]

It doesn't look like hard changes tho.
Try this
https://github.com/eugeneko/Urho3D/commit/8e947952d69a0d50daef42a948c05e1194b86c22
If it works as I suppose, I'll make PR.

-------------------------

extobias | 2018-04-06 21:59:11 UTC | #19

Nice, this style of play would be good in a procedurally generated world, like those of @Bananaft

-------------------------

