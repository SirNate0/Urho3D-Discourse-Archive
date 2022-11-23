Dave82 | 2020-07-04 23:51:41 UTC | #1

My desktop resolution is 1920 x 1080. I 'm trying to run my game in fullscreen but using a smaller resolution : 1280 * 720. At this resolution the screen is always off.The width of the visible area is shorter , leaving a black unused stripe on the right side of the monitor and the height is "longer" . Unfortunately i can't take a snapshot because it captures only the rendered part leaving the black stripe out of the screenshot...
Hovever if i change my resolution to 1280 * 768 everything works as expected (no black stripe). But this is a 1.66667 ratio so it doesn't seem right. Had the same issue with my other GPU too.

EDIT tested with NinjaSnowWar and i have the same issue. (using Win7 64bit and Urho3D 1.7)
Is there a way to run the app in fullscreen and just stretch it to fit the screen ?
EDIT2 : Tested on another pc with and the issue is similar. Now the top of the screen is off. Makes the NinjaSnowWar's health hud not visible.
EDIT3: I have the same problem using other engines as well.
EDIT4 : So many edits :D ... Ok so it seems that some resolutions just doesn't want to work properly but some do. I tried 1600 x 900 and it worked perfectly. I even tried a 1600 x 960 which is a 1.66667 aspect resolution and it is stretched perfectly on my monitor.

-------------------------

JTippetts1 | 2020-07-16 22:31:32 UTC | #2

It's recommended that if you are going to run fullscreen, you use the user's native resolution rather than mode switching. As you've discovered, mode switching doesn't really work well sometimes, and some players get a little touchy if you run lower than their normal resolution.

-------------------------

Dave82 | 2020-07-16 22:27:04 UTC | #3

Well i will just go with that route then. My only concern was the size of the UI elements but just found out that Urho3D::UI has a SetScale method so the problem is solved.

-------------------------

