Capital-Asterisk | 2019-07-31 22:56:18 UTC | #1

Hello, I've been lurking on these forums for about a year, so here's some stuff.

I wanted to learn how to use Urho3D because I was thinking of resurrecting a project known as Open Space Program. At that time, Ludum Dare 42 was coming up, and I thought it was the perfect opportunity to go face first into learning the engine. Urho3D has enough features for one to hammer together complete-ish games in less than two days.

For both of these entries, Urho3DPlayer and AngelScript was used because I didn't want to deal with any compile time. Blender exporter was used for all the assets.

**LD42: Electric Fence: Micro B**
https://www.youtube.com/watch?v=6yaoVGgF7GM
[Downloads](https://neal-nicdao.itch.io/electric-fence-micro-b)
[Source](https://github.com/Capital-Asterisk/LD42-ElectricFenceMicroB) 

My first Ludum Dare, the theme was "Running out of Space." You're this segway guy with a gun and there's stuff to shoot. The player has to navigate randomly generated rooms to destroy 3 targets, as a barrier shrinks around them.

This game was updated a few days ago to make it fun. The code is pretty ugly but it works. Some bits of code should have been in the render update, it's full of global variables, and all the player movement code is directly in the game loop.

**LD43: Manned Missile Master**
https://www.youtube.com/watch?v=8ST0udJRyj8
[Download](https://neal-nicdao.itch.io/manned-missile-master)
[Source](https://github.com/Capital-Asterisk/LD43-manned-missile)

This time the theme was "Sacrifices must be made," so I decided that flying a manned missile is a good idea. You fly through obstacles and avoid projectiles to ram into a target.

The code is much nicer than the previous game, but it's still written in two days. There are some issues related to moving the camera smoothly at render update: the sky and target indicator shakes. It also uses PBR materials, which looks great but PBR particles don't seem to be there yet. 

LD44 i missed.

I'm thankful to this community for creating a surprisingly capable game engine. There's a few techniques I used here that some may want to question, so feel free to ask.

-------------------------

Modanung | 2019-08-01 04:29:01 UTC | #2

Welcome to the forums, Dr. Strangelove!  
How appropriate of you to drop in right before the end-times. :radioactive: :confetti_ball: :slightly_smiling_face:
> :musical_note: [**Ritual Noise** by _Covenant_](https://www.youtube-nocookie.com/embed/qXcizY05ysw)

-------------------------

Leith | 2019-08-01 09:44:52 UTC | #3

Really nice work! I like your unconventional approach - our market wants fresh new concepts, not the same old thing reskinned :P

-------------------------

