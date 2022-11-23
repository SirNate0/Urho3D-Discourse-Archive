slapin | 2017-03-04 16:52:33 UTC | #1

I look for someone who will teach me about how things are done in gamedev world.

I need to know the following:

1. How can I make live GTA-style city work. My challenge is bigger - I want all buildings enterable
and keep track of all cars and NPCs in city.

2. How to properly organize AI in such game, so it would be easily extensible.

I have enough knowledge to generate such city procedurally (including building interriors.
I have trouble with straight game stuff. Code examples, links to articles, etc. would be
heavily appreciated. And I know about $500/year fee of GDC, but I can't afford it now.

The project is planned to be Open Source under MIT license.

-------------------------

monkeyface | 2017-03-05 22:54:04 UTC | #2

http://en.wikigta.org/wiki/Credits_(GTA_V)

-------------------------

slapin | 2017-03-05 23:24:03 UTC | #3

Too many rockstars over there. No, I don't plan to make something like AAA game,
I'm just interested in city sandbox doing it as long as time permints.

-------------------------

rku | 2017-03-06 15:20:59 UTC | #4

You are asking this like it was asking to teach play chess. It is not. Topic at hand is way broader and more complex. If you want to learn something - go and make a pacman. Then go make a 3d pacman with some cool effects and what not. You want to fly before you know how to walk and it only ends up with a nose deep in mud. I do not want to be mean and discourage you but this reality check is something you seem to need. Start small if you want to get anywhere at all.

-------------------------

slapin | 2017-03-06 16:29:22 UTC | #5

Please don't overreact, we're not stacking beans here.

I mean something like this (it is very old video): https://www.youtube.com/watch?v=mdix7qwJGuk

I learn a lot of things for quite a while to make things in motion. Look at other videos there.

I have no problems generating such stuff (I have a lot of info to grasp here, no problem
with experimenting), main problem is more common gameplay stuff. I watch GDC and wonder how they did this and that, i.e. 300 bones per character, etc.
Now I found very cool concept - behavior trees, and now I need some help organizing it. This should help
scripts turn from mess to something which is easy to maintain. As game is very complex thing with many
systems, and I'm very new to this, so I ask.

-------------------------

monkeyface | 2017-03-06 21:46:53 UTC | #6

The thing is, if you have to ask how to do it, the chances are you can't do it. More often than not with 3d game dev, even when you have fully researched something and know exactly how it is done, you will still find you can't do it.
The only solution is reading a LOT and studying other people's code a LOT, and trying and failing a LOT until you achieve what you want.  But - start with something small. If you start with something like an open world city you will need to spend about 6 or 7 years failing before you achieve anything and probably never have anything good enough to share with others (GTA needed 100s of people to make). If you start with something simpler you might start to have something playable within a few weeks.

-------------------------

slapin | 2017-03-07 13:23:05 UTC | #7

This is what I'm looking for - a stuff to research and study. Starting small doesn't boost my motivation enough,
but there is a lot of things I need to do indeed. And knowing how other people do it is priceless.

-------------------------

slapin | 2017-03-07 13:29:59 UTC | #8

I know about manpower needed for making good stuff. And I do small scale where big scale will end up in
huge amount of work. But I want to have PoC algorithmic stuff working to stage where all I need is
just add content without global changes (and I know the process is cyclic). I try to use as many art-related
shortcuts as possible at this stage, as I want to make code do the right thing first and have feature-complete tool set before taking art seriously.

-------------------------

glebedev | 2017-05-29 18:11:58 UTC | #9

I had a plan to try something for city rendering in urho. My plan was:
- generate a mesh from Open Street Map XML file
- merge it and split it into blocks to fit into urho's octree. Strip off all unnecessary data like textures and make it occluders.
- generate building models and street blocks and find a way to generate few LODs off it.
- make an app to render high LODs into low LOD textures to automate the process a bit
- give it to community so people would create high LODs for buildings and make games on top of it.

I've stopped somewhere half way into this. But I've managed to try occluders in urho and it was looking promising.

Do you want to continue my work?

-------------------------

slapin | 2017-05-29 22:19:55 UTC | #10

Well, my plan is a bit different.

I'm fully randomly generate the data, the idea is that game starts with full new world (city), so it is different every time game starts.
The biggest problem is generating LODs. But regardless, I'm on algorithmic part now, so Ieave implementation details for time when all algorithms are in place.
I do: roadmap + lots generation, individual building generation, building interior generation. Now I work of AI data integration to be able to run traffic in city and walk people on sidewalks, then I plan to go for macro-level details and
small details like traffic lights. I think in about 3-4 months I will have something I could show to others...

-------------------------

