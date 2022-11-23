TikariSakari | 2017-01-02 01:06:49 UTC | #1

Hello I have been working on a tactics type of a game now for quite a while. It has been quite on/off kind of a project, but I have enjoyed using Urho3D and it really is a nice engine to work with. 

There really isn't much to show, but maybe one day I will have my first game finished. Hopefully.

[video]https://www.youtube.com/watch?v=JHCmFYFg8FQ[/video]

The enemy players are AI-controlled, although the AI is extremely simple one.

-------------------------

Bananaft | 2017-01-02 01:06:49 UTC | #2

Looks neat.

Are you aiming at mobile platform(Judging by interface)?

-------------------------

TikariSakari | 2017-01-02 01:06:49 UTC | #3

[quote="Bananaft"]Looks neat.

Are you aiming at mobile platform(Judging by interface)?[/quote]

Ty. Yes, mobile device, well mostly android, since I don't have idevices, has been my #1 priority. I still have no idea if the camera controlling is intuitive for others. Basically one finger = camera movement, 2 rotation. "The more down I look" the further the camera distances. I was trying to figure out something that would take away the need to have the camera distance slider and came up the idea to have both zooming and pitch being on same function. I still can change camera distance with mouse scroll or using the slider, but maybe I can completely toss them away.

As for testing it out, I bought myself today samsung galaxy J1 for kind of low level device to test the project with. I was happy to notice that even that phone could run the game 60fps, altho as you probably can see, only one character at a time is actually moving. Basically on every single unit on the screen I have 2 models. One is static mesh and one is the animated one. When the turn comes to the selected player, it disables the static mesh and enables the animated one. At least I noticed that on my nexus 5, which most likely gets more likely gpu bottlenecked, models that had less bones had higher fps, even though it used exactly same model. On the other hand my quick speed tests with urho (that are quite questionable to begin with), swapping models from static to animated, didn't really have that much impact. So I suspect that the J1 gets more likely cpu-bottle necked with the dual core processor and Mali400 gpu.

I accidentally had some specularity on the grass and the J1 had quite some frame drops until I noticed that turning off the specularity had quite a high boost on performance, so it could be that J1 bottle neck is actually on gpu and nexus 5 on cpu as in vice versa.

The UI tries to scale according to screen resolution, where I put the texts original font size on 1080p on the texts name. Then I use that information during the resize and count the new font size by simply calculating the font multisizemultiplier.
[code]
	if (screenHeight < screenWidth)
		return screenHeight / 1080.f;
	else
		return screenWidth / 1080.f;
[/code]
I've been using the vertical layout mode as vertical and horizontal for containers, so that everything pretty much scales on depending on the font size. The bad thing is, that for images, I am not able to use the same logic.

-------------------------

Bananaft | 2017-01-02 01:06:50 UTC | #4

[quote="TikariSakari"]I still have no idea if the camera controlling is intuitive for others.[/quote]

I was about to comment on this. Does this game really needs camera rotation? I think, it does not, unless you have some really complex vertical landscapes on mind, like tall walls and hills. I guess, mobile gameplay can benefit, if you fix the view angle, and leave only zoom to be changable.

Since it's will be still in 3D and you probably want to show your assets better, you can change camera pitch with the zoom like in some games, low camera - lower camera angle, far camera - steep angle, giving more tactical view. You can also add cinematic cameras on attacks, and while it's enemy turn.

-------------------------

TikariSakari | 2017-01-02 01:06:50 UTC | #5

[quote="Bananaft"][quote="TikariSakari"]I still have no idea if the camera controlling is intuitive for others.[/quote]

I was about to comment on this. Does this game really needs camera rotation? I think, it does not, unless you have some really complex vertical landscapes on mind, like tall walls and hills. I guess, mobile gameplay can benefit, if you fix the view angle, and leave only zoom to be changable.

Since it's will be still in 3D and you probably want to show your assets better, you can change camera pitch with the zoom like in some games, low camera - lower camera angle, far camera - steep angle, giving more tactical view. You can also add cinematic cameras on attacks, and while it's enemy turn.[/quote]

I do agree that rotating camera is questionable if its a good or bad thing, but at least I have learned to use it after fiddling with it. Maybe it can turn people away from the game, if it ever gets finished, but it is not like I think the game would even ever be popular to begin with. I just figured out to make a game that I would like and have a scope that is somewhat doable. But yes having a fixed angle camera might be better overall or fixed step turns such as 22.5 degrees turn per press of a button, although that would add more stuff on the UI, which I would prefer to be as minimalistic as possible.

Actually the rotating of camera came to exist by accident. I was  testing out unity, when the unity5 came out, and tried to make the bare bones of the game with unity to see if it would be any easier/faster/see the performance on unity. So I made the camera controller for mouse and made it move around with right mouse button and by default I think Unitys behavior for android for the right mouse button is actually having 2 touches. So when I tested it on my phone, i noticed that i can rotate the camera around when holding 2 fingers at the same time. So I figured if people can associate 2 finger movement with same as using mouse right button, which seems to be the way Unity does things, I decided to make the camera work the similar way on my game.

Then to get rid of the slider, I wanted to try implementing camera distance and pitch into same rotation. It is an assumption that if people want more of an overview of the situation they would prefer to zoom out when watching down from the sky, so it is bit of experimental thing atm.

I also noticed that this game seems to use something similar for their camera with the exception of having pinch as zooming, which I thought to try out couple of times, but never did. [video]https://www.youtube.com/watch?v=vecJydg-2L0[/video]

-------------------------

rasteron | 2017-01-02 01:06:51 UTC | #6

Good start, looks nice and keep it up. :slight_smile:

-------------------------

Lumak | 2017-01-02 01:07:15 UTC | #7

I would like to see this game completed, as I'm curious as to see how well it does in the Android market.  A turn-base style game that I really enjoyed was XCom.  While xcom (2012) was solid, I enjoyed the original xcom (1994) on ps2 more. It was much simpler game but great game play, and this game could be as good.

edit: title names - the original xcom was a 1994 release, the reboot in 2012 was also called xcom, and the xcom2 is scheduled for 2016.

-------------------------

TikariSakari | 2017-01-02 01:07:16 UTC | #8

I too hope that I will be able to one day finish the game, but with the pace this is going now, I doubt I have much to show before this year ends, not even sure about before next year ends. I feel that there will be in future / are a lot of turn based games for android already, so by the time I might have this at least up to playable state there is already a flood of turn based games.

I think the first xcom was called UFO:enemy unknown here in Europe. It is/was awesome game, but I am kind of trying to go more in the direction of Final Fantasy Tactics / Tactics Ogre or Fire Emblem. Basically some sort of rpg-like story with turn based combat. As for combat I was thinking more of having a system where the turn is based on some speed-like thing, such that every action increases the amount of time needed before the character gets new turn instead of having team moves, where you can move each person on your team then end the turn. I am going to go with this route to have simpler AI or at least hopefully it will be simpler to code. Currently the AI is pretty dumb, it counts every possible move, and makes one that causes most damage/heals most on that one turn. In future I am planning on improving the AI, at least trying to guess the threat of things, something like influence map. I found interesting post in gamedev.net forums, there are couple of lectures about some AI things, and it gave me some ideas on how I could improve the AI to make it seem smarter. [url]http://www.gamedev.net/topic/671663-turn-based-rpg-ai-how-can-i-handle-risk-reward/[/url]

Going for rpg-like story, which most likely turns out bad any way, is most likely a terrible idea. Currently I have been trying to think of a way to implement some sort of way to do cut scenes, and with the fact that my skills on modeling/drawing are mediocre at best, there is no way to know how long this project will take. As for cut scenes, I have thought of using blender and simply creating action for whole sequence and play it as an animation. At least when I tried the editors bezier curves, I couldn't see any object moving along the points, or maybe I just set the points wrongly. On the other hand, I wasn't able to import bezier curves from blender either, so I figured that easiest way would be to just make a single action for whole cut scene. Other possibility is to have lots of empties being exported from blender, then using some naming convention, during the loading of the scene, parse the names and create bezier curves out of them. But since there are 1 million other things to do before this, I haven't really figured out what way I should go.

-------------------------

