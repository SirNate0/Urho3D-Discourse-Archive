dertom | 2022-02-06 18:41:37 UTC | #1

Hi, I took part at a gamejam. Made the game with urho.net. Asset was a rogue-like-sheet and music were made custom by some cool guy :+1:

https://dertom1895.itch.io/dual-world-dash

PS: Well it is a two player game, so not sure who playable it is. But it was fun to make, and actually I want to do multiplayer, but.... the time the time. (same for AI ;) )
PPS: Web-Deploy is fast is though it was broken all the time, but it just takes 2seconds and it is read for publish @elix22 :+1: Only thing that got me, was that webgl seems not to like texture other than powerof2-sized....but once you know (actually I already knew but forgot :D )

-------------------------

elix22 | 2022-02-06 19:10:36 UTC | #2

Cool  :smiley: !! 
My 2 cents , maybe a small Youtube video showing how to play it 
As you might know ,  Urho vanilla Networking doesn't work on Web  ,you will get some exceptions if you call Networking API's (Web deployment) , I plan to add some stubs to bypass these exceptions . 
You will have to use some external C# Networking clients that do support web (such as [Nakama](https://heroiclabs.com/)) 

Yes WebGL can handle only powerof 2 sized textures :slightly_smiling_face:
Some cross platform engine agnostic tools to manipulate textures 
https://www.youtube.com/watch?v=kPWShsel6vo&t=10s

-------------------------

dertom | 2022-02-06 19:34:56 UTC | #3

Good point with the video. Once I get home....😉
Yeah with the network I had more the desktop clients in the eye. But if there is a way to use nakama it would be cool. Not planning to use vanilla urho network after all.

-------------------------

elix22 | 2022-02-07 10:39:13 UTC | #4

Works like a charm on mobile browsers (my IPad and my Android phone)

An issue that you mentioned in your page
If you leave the page and returning back to it , Input doesn't respond anymore , one needs to reload the page  , hopefully I will fix it once I have some time (not sure about the root cause , Emscripten , Urho , me).

Regarding Nakama client Web support , I have to do some additional work on my side (Mono Assembly loading errors) , will do once I will have some free time

-------------------------

