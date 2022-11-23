TheComet | 2019-05-23 13:20:01 UTC | #1

Way back in the day when I made games with DarkBASIC, I wrote a fun little online multiplayer arcade game that was based on a game mechanic I first saw in a Mario Party 7 minigame:

https://www.youtube.com/watch?v=NsEBCZfrVBU

I took this idea of driving over a grid of tiles to claim them as your own and scaled it way up. Bigger maps, more players, fun powerups. Here's a video of my DarkBASIC implementation in action:

https://www.youtube.com/watch?v=M-5yaHqDP8o

I've decided to re-implement this game in Urho3D and add even more stuff to it. I'll also be giving it a graphics overhaul.

It's still in it's extremely early stages, as of now I wrote the map loader so I can import all of the old maps from the DarkBASIC game (which uses some ungodly binary format). Here you can see a map loaded in Urho3D:

![IMG-20170801-WA0009|690x479](upload://9JRURb9zEiEBQ0JEvskdsZbcCsL.jpg)

I created new models for the various tile types (Tile, Wall and Teleporter) as well as a new player model. You can see them here:

![IMG-20170801-WA0010|566x500](upload://xWQFWbRZiA3I2NVDsGuKzAO05xE.jpg)

That is all for now!

-------------------------

johnnycable | 2017-08-04 16:36:28 UTC | #2

SuperDuper! Looks really funny!
Darkbasic! (What's darkbasic?):no_mouth:
Joking... It reminds me of good ol' times when I programming machine language on C64...:blush:
I like the warp special effect! Go on!

-------------------------

slapin | 2017-08-04 16:37:05 UTC | #3

What a cool tiny game!

I think that could make a great tutorial material for Urho to attract new youtube users...

-------------------------

TheComet | 2019-05-23 13:20:01 UTC | #4

Thanks!

I bounced some ideas off of an artist friend of mine, and a cool idea that popped up is to add some actual scenery objects to the level in addition to the tiles and walls to make the levels feel more alive. 

We thought about creating different themes or "biomes", too. One might be a snow theme, another might be a desert theme, etc.

Here's a wooden house he made that could fit into a snow themed map:

![1|690x468](upload://kwaSTvKKDoXlmnXTgA8DwabuKn7.jpg)

-------------------------

Modanung | 2017-08-05 09:58:19 UTC | #5

Could one paint the floor inside the house? That would raise the roof! :stuck_out_tongue:

-------------------------

slapin | 2017-08-05 13:05:36 UTC | #6

How is your game feels? There is no updates for so long time :(

-------------------------

TheComet | 2017-08-23 23:43:07 UTC | #7

[quote="Modanung, post:5, topic:3418"]
Could one paint the floor inside the house? That would raise the roof! :stuck_out_tongue:
[/quote]
I like the idea and will keep it in mind. Supporting buildings with interiors will make the map editor a lot more complicated, though, but maybe I can come up with something.

**Updates**
I've mostly been learning how Urho3D's networking works, and have been doing so by implementing menu system.

When you start the game, you will be presented with this screen:

![1|517x500](upload://jVSBlKua7BqYMHfQqNQBQqfJovw.png)

From there you can connect to a server with a username and address:

![2|652x478](upload://fn8vK5bqPGf9VlRvH1kpyqXbSzN.png)

And here's the main server menu, where you can chat with people, join queued games, or create your own games (which other people can then join).

![3|638x500](upload://qyZRF7iTfRvfNoHycntvl5DIXZ3.png)

-------------------------

