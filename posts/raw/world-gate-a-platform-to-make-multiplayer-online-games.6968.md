DinS | 2021-08-14 07:00:59 UTC | #1

![wg_main|690x388](upload://qpcte2nw4QywwdR4EOBlc1Y6kzN.jpeg)

**World_Gate, the gate to unlimited worlds.**
World_Gate is a platform where you can build, run and share a multi-agent strategic environment, i.e., a world. The engine to execute a world is made with Urho3D.
Too abstract? Let me explain a little more.

In the context of gaming from the developer's side, World_Gate provides the infrastructure for multi-player online strategic games.
Now developers don't need to rent a server, code server logic, deploy a server and worry about network error. All they need to focus on is game logic.
Even for game logic, the don't need to start from scratch. They can build their world on top of other world, like making an expansion.
With the platform's IDE, making an online board game is just a piece of cake. It's ideal to try out new ideas, make a prototype at minimum cost and get it online instantly
Here is a workflow demo video
https://dins.site/wp-content/uploads/2021/08/workflow.mp4
(For how to build a world, please see [tutorials](https://dins.site/world-gate-tutorial-index-eng/))     

In the context of gaming from the user's side, World_Gate provides multi-player online strategic games that normally can't be seen outside, since it is a breeding field for new ideas.
Users can even tweak some existing worlds and brew their own without the knowledge of a professional game developer or coding experience.
With creativity, they see/make uncommon games and get uncommon experience.
For example, you can make an auction type board game with Skyrim modding as theme.
https://dins.site/wp-content/uploads/2021/08/nexusskyrim_demo.mp4

(World_Gate can also be used to do acedemic research and AI research, but I'll skip here)

So why am I keep talking about board games? Because that's how it all started.
I am a fan of board games, but, you know, it's hard to gather friends together to play.
I am also a fan of DIY, and like to tweak some rules to make the board games more interesting.
As a result, I start to wonder if there's a tool to let everybody, amateur or pro, make their own board game and share it online to play with friends.
Then I spend three years developing this World_Gate platform alone. During the process I keep refining my ideas and refactoring the codes.
In the end the platform has gone beyond board game. Now theoretically you can even build a MOBA game with this platform.
This video demonstrates World_Order, which is the very first game I want to make. It is a combination of turn-based strategy and real-time strategy game.
https://dins.site/wp-content/uploads/2021/08/worldorder_demo.mp4

World_Gate platform consists of these parts:
**World_Creator** is the IDE for building worlds, which is developed with Qt and released under GPL license.
**World_Mind** is the IDE for building AIs, which is developed with Qt and released under GPL license.
**World_Gate** is the client for running a world online with others, which is developed with Urho3D engine and I intent to make it open source in the future.
**Servers** are developed with plain C++ codes. For all the servers I am paying out of my own pocket.
AngelScript is used for the world scripting part.
You can find the [download links here]( https://dins.site/world-gate-index/).  

World_Gate is currently a hobby project. It's free to use. It doesn't collect any personally identifiable information (PII). There's no background activity.
If you are interested in multi-player games, why not give it a try?
To get an idea how to build a world, you can watch this [20-minute video](https://dins.site/world-gate-creator-tutorial-beginner-12-eng/) walkthrough to make a simple 2-player online rock-scissors-paper game.


_____
Finally a vision:
I have a dream that one day we, regardless of our experience and background, will be able to build the world we want.
I have a dream that one day we will become our own master and can create world without being first approved by others.
I have a dream that one day we can bring out our world and sit down together to enjoy and appreciate each other's world.

-------------------------

vmost | 2021-08-14 10:16:35 UTC | #2

Very impressive work!

-------------------------

DinS | 2021-08-14 10:19:04 UTC | #3

Thank you! I'm glad you like it.

-------------------------

throwawayerino | 2021-08-14 11:51:07 UTC | #4

This reminds me alot of the BYOND engine. If you can pull it off, this would be a really awesome party game maker.

-------------------------

DinS | 2021-08-14 12:33:07 UTC | #5

That's the goal to aim. I have plans to build the mobile version in the near future. 
I also want to target different users with different skills. For newbie, they can just pick a framework and change some textures and texts to make their own game. For pro, they can code really complicated stuffs in this platform, for example designing OOP, performing network and disk I/O.
So yeah, it has some potentials.

-------------------------

