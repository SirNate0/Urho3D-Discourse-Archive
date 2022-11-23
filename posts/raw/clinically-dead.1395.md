szamq | 2017-05-16 13:16:55 UTC | #1

Hi,
I'm a part of Urho3D community and using it since I found it by accident in 2013. At the beginning it was mostly learning about how the engine works etc. More than one year ago I started developing Clinically Dead. It's a puzzle FPP game where you play as a guy who is dying and the game itself is the last 30 seconds of his life. Everything in game happens in his brain and he is talking with his subconsciousness which is a narrator in the game. I would say this game is for people who liked games like Portal 2 and Antichamber.

The core mechanics in the game is the connection between time and space. Time doesn't flow normally in this game, instead each place on the map has each own time. The time field is shown to the player as colors. Blue color is cold, so the time is near to zero there. Red color is warm, so there is high value of time. Blackish color is time below zero = player's death. Each level is different, which means that on some levels there are different time pointers - it can be every object on the map including the player. If the  time pointer moves on the map then it changes the time... and the level reacts to this time change by moving platforms or changing any attribute.

I have all game mechanics working, shaders etc. Playable 9 levels, need 21 more(one level, one second closer to the death).
I will need probably one more year to finish the game. I will post here in this thread all future important news.
If you are interested more about the game feel free to ask:)

[url]http://www.mogilagames.com/clinically-dead/[/url]
[url]https://www.facebook.com/MogilaGames[/url]
(Watch in 720p, youtube bitrate messed up the video too much on others)
https://www.youtube.com/watch?v=rpGXgn2Qze8&feature=youtu.be

-------------------------

codingmonkey | 2017-01-02 01:07:27 UTC | #2

Wow, your game have a very unusual kaleidoscopic color style, great work! )

-------------------------

ghidra | 2017-01-02 01:07:27 UTC | #3

Impressive!

I love the style, and the colors. As well the rendering/shader effects. This looks really great!

-------------------------

Bananaft | 2017-01-02 01:07:27 UTC | #4

Really cool. I recognised the influence of Zdzis?aw Beksi?ski's art. Especially the scene with campfires on rock poles.

Looking forward to try it out.

How do you planning to distribute it?

-------------------------

sabotage3d | 2017-01-02 01:07:27 UTC | #5

Great work really interesting style. Are you going to do a development blog ? Can you reveal a bit more of the programming techniques you used ?

-------------------------

szamq | 2017-01-02 01:07:28 UTC | #6

Thanks guys for the kind words. Working hard on this.

@Bananaft Yes exactly, it's from one of his paintings. But I'm not sure if I remove that scene before releasing the game. I may be sued for breaking the copyright law. Zdzis?aw Beksi?ski is dead but all intellectual rights are transferred to museum in Sanok where his paintings are. Probably I will ask for permission soon.

I plan to release this game on Steam for windows mac and linux in Q3 2016, maybe I will create some kickstarter before that, not sure. Eventually, I will probably release source code on open source license.

@sabotage3d I have dev blog on my site [url]http://www.mogilagames.com/blog/[/url] But I don't write much there, besides the important news.I still use pre 1.3 urho3d version, need force myself to update the code to the master someday, as I saw a lot of bugs fixed in the newer versions. I use 99% angelscript and the urho3d editor where I create scenes/levels which later I load in the game. I created lot of custom code and scripts in Angelscript which I attach to the objects, for example:
- impact and scratching sound for physical objects.
- character controller (started from the one of the urho's samples)
- buoyancy forces for water
- switching between scenes - choosing the level is in fact going into the right door from the hub level like in Quake or The talos pronciple.
Also, i wrote lot of custom post process shaders. The most complex is the time shader which renders rainbow colors depending on the actual time for each pixel. Blue = low amount of time, Red = high value of time. Time is interpolated across the map.

-------------------------

Bananaft | 2017-01-02 01:07:28 UTC | #7

[quote="szamq"]But I'm not sure if I remove that scene before releasing the game. I may be sued for breaking the copyright law.[/quote]
Nonsense, you are not breaking a copyright in any way. Can call it a tribute.

Think of how many games and movies are influenced by H.R. Giger. Not to mention, 99% of all those fantasy and sci-fi games coming out every day, looking absolutely same.

-------------------------

rasteron | 2017-01-02 01:07:28 UTC | #8

This looks great szamq!

-------------------------

weitjong | 2017-01-02 01:07:28 UTC | #9

Psychedelic!

When it is available on Linux then I might play it.

-------------------------

cadaver | 2017-01-02 01:07:28 UTC | #10

This is looking sweet! Some of the transitions bring to mind the 2009 Wolfenstein game where you transported in/out of the occult realm, and the general gameplay / level design feel seem to slightly echo the Xen levels of the original Half-Life, but more psychedelic.

-------------------------

bvanevery | 2017-01-02 01:07:53 UTC | #11

Regardless of how the gameplay turns out to be, that's the most visually interesting game I've seen in awhile.  And as I'm an Impressionist-y painter who dislikes the math-y-ness of a lot of 3d games, that's saying a lot... not that anyone would have any way of knowing or calibrating anything I would say.  Anyways, good job!

-------------------------

szamq | 2017-05-16 13:18:04 UTC | #12

https://giant.gfycat.com/UnderstatedFittingBongo.webm

Thanks for your feedback. Posting some more stuff, for all you who liked the graphical aspect of the game [gfycat.com/UnderstatedFittingBongo](http://gfycat.com/UnderstatedFittingBongo)
But in my opinion the real strong point of the game is the time based game mechanics. The lines and the colors on the map show the time flow and its value. Like a rainbow colors - where the map is blue there is lower value of time than in place which is painted(postprocess) on the red color. The level changes with the time change and of course the time field can be dynamic and can change in realtime. To understand better the time field - actually, it's like a isolines that show the temperature 
[img]http://2.bp.blogspot.com/-aXeLo4ykrxc/T3juZYMm1SI/AAAAAAAAAA8/5RqL5dO4nXA/s400/isoline.png[/img]
Currently have 12 levels, 18 more to finish the game.

-------------------------

Canardian | 2017-01-02 01:08:41 UTC | #13

Amazingly good looking style! :slight_smile:
I can't even begin to imagine how much efforts were needed for all those special effects.
I like it when games are made with imagination, while still retaining realistic aspects, maybe even more realistic than what we think reality is...

-------------------------

Dave82 | 2017-01-02 01:08:42 UTC | #14

The effects are really awesome ! And the gameplay looks interesting too.
Good luck with the project !

-------------------------

szamq | 2017-05-16 13:19:43 UTC | #15

Created new story gameplay trailer for Clinically Dead. 
(watch in 1080p please)
https://www.youtube.com/watch?v=a44jMjJNnHY

-------------------------

bvanevery | 2017-01-02 01:11:52 UTC | #16

Well ain't that different!  Previously I wasn't sure what the game itself was actually going to be asking me to do.  Now I get it.  Good job.

-------------------------

szamq | 2017-05-16 12:59:47 UTC | #17

Still making this game :D
https://www.youtube.com/watch?v=eNO7zx7XrEs

-------------------------

szamq | 2017-07-02 21:01:23 UTC | #18

Glass alike impact and drag sounds.

https://www.youtube.com/watch?v=oaJOimHtlDE

-------------------------

Modanung | 2017-07-03 10:27:58 UTC | #19

Nice progress! :grinning:

-------------------------

szamq | 2018-11-01 21:00:08 UTC | #20

It's been long time. If everything goes well game will be released on Steam in about month.
https://store.steampowered.com/app/927840/Clinically_Dead/

-------------------------

Eugene | 2018-11-02 15:02:12 UTC | #21

Oh, great! I've waited for this. Any chance to get some new vids?

-------------------------

szamq | 2018-11-02 18:48:43 UTC | #22

here is new trailer from this year https://www.youtube.com/watch?v=nMxLbjezEkY best wath in 4k because of  lots of color change on the screen that affects the bitrate. Probably will create walkthrough video after the game release.

-------------------------

szamq | 2018-12-06 15:45:06 UTC | #23

Hi, 
The game is just released on Steam here 
https://store.steampowered.com/app/927840/Clinically_Dead/

I also created new video where I'm explaining the core mechanics in the game

https://youtu.be/WwYjgUQpcD8

Thanks to Lasse and all contributors for the great engine. The game uses Urho3D version from 2016 i believe.

-------------------------

Modanung | 2018-12-06 20:58:52 UTC | #24

That new video is very clarifying. Interesting dynamic.

Are you planning to release a Linux version as well?

-------------------------

dertom | 2018-12-06 21:18:07 UTC | #25

Just played the first three/four Levels. Looks great. Well done :+1:

-------------------------

szamq | 2018-12-06 23:52:58 UTC | #26

I complied it on Linux but I had a problem with shaders and the post processes looked differently than on windows, which was weird since it was the same glsl code.

-------------------------

cadaver | 2018-12-10 11:52:30 UTC | #27

Congratulations on your game release!

-------------------------

GoldenThumbs | 2018-12-10 23:18:36 UTC | #28

Dude this looks cool! I have been watching project this for a lil' while and it's so awesome to see you release it.

-------------------------

