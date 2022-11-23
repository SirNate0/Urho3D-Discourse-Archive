dertom | 2021-10-25 10:33:06 UTC | #1

Hola,... started attending [trijams](https://trijam.itch.io/) (3h (loosly) jam you can do sometime the weekend). Using it for checking my setup and skills....or let's say train 'to know your tools'. At the moment I'm using Urho.net that feels quite good to me. I will post my entries here, not that those are master-piece (more the opposite)... :D

Would be great if more would like to attend trijam from time to time :+1:

-------------------------

dertom | 2021-10-25 10:40:57 UTC | #2

141 ('procedural world - no real gameplay, just looking for gate to teleport to next world which will be generated and get bigger ;) '):
https://dertom1895.itch.io/trijam141-gate-to-another-world

142 ('flying the balloon. struggled with UI therefore I missed the theme :D  and with feature adding multiple ambient sound with each restart '):
https://dertom1895.itch.io/tri142-balloonrider

-------------------------

elix22 | 2021-10-25 12:56:51 UTC | #3

For a 3 hour coding , BallonRider looks really cool , gameplay is nice (I can't pass the first level :joy: )

-------------------------

dertom | 2021-10-25 13:09:39 UTC | #4

[quote="elix22, post:3, topic:7021"]
For a 3 hour coding
[/quote]
...well in the end it was 5.5h. That is ok with the jam, but you get less points. I had some problems with urho-ui and burned 2.5h or so with that :D Need to have a deeper look into that.

[quote="elix22, post:3, topic:7021"]
I can’t pass the first leve
[/quote]
It is doable but I guess the level-design could have been better :smiley:

-------------------------

elix22 | 2021-10-25 21:18:36 UTC | #5

UI is a very painful subject .
That's the reason I have written a UIBuilder tool , I am actually using it for UI creation  for my own game.
This tool supports full **hot-reload** on desktop (Linux,Windows,Mac)   and preview on mobile (Android,iOS).
While the tool is running , any modification to file/s will instantly compile (less than 150 ms) and will be hot-reloaded and displayed.

https://github.com/Urho-Net/Samples/tree/main/UIBuilder

-------------------------

dertom | 2021-10-25 22:44:03 UTC | #6

That might become handy. 👍

-------------------------

Eugene | 2021-10-26 08:09:28 UTC | #7

[quote="dertom, post:1, topic:7021"]
At the moment I’m using [Urho.net](http://Urho.net) that feels quite good to me.
[/quote]
I was about ot ask why not going for a Web version when I saw this part.
@elix22 do you have any plans for enabling C# for Web builds? It was always a dealbreaker for me, the inability to use C# for all target platforms.

-------------------------

elix22 | 2021-10-26 08:42:58 UTC | #8

[quote="Eugene, post:7, topic:7021"]
@elix22 do you have any plans for enabling C# for Web builds? It was always a dealbreaker for me, the inability to use C# for all target platform
[/quote]

Yes , it is in my todo list 
There are 2 possibilities which I am investigating (when I am not working on my game) 
- My preferred way ,  using mono-wasm (Godot and probably Wave engine are using it)
https://github.com/mono/mono/tree/main/sdks/wasm
- Dotnet 6 , new feature , Blazor has the ability to compile native code 
https://devblogs.microsoft.com/aspnet/asp-net-core-updates-in-net-6-rc-2/#using-native-code-from-a-blazor-webassembly-app

-------------------------

elix22 | 2021-10-26 08:54:20 UTC | #9

@dertom 
I have some small comments on BalloonRider

* BalloonRider plays nicely on Windows and Linux ,  you do have the ability to publish for Mac , so why don't you ?  (We Mac users also like to play games :) )

* Since it's a full-screen mode , the player needs to be notified that the  Escape  button will exit the game.
* If it was up to me , I would have also generated and uploaded Android APK , even if it's not through Google Play , users will be able to install it.

-------------------------

dertom | 2021-10-26 09:01:21 UTC | #10

Yes, you are right in every point. With macos, I just wasn't sure to publish something, I cannot test before 'releasing' it... and still not tested the android publish,yet. But it is absolutely on my todo list. Maybe I will take this as 'side task' for the next jam.

-------------------------

dertom | 2021-10-29 21:22:45 UTC | #11

["TriJam 143 - Theme: Sleepless Nights"](https://itch.io/jam/trijam-143) 3h jam started today. (Do you 3hours whenever you want within the time-period. You can even split the 3hours up or even do longer if need be. There is one category just for the time....) I guess, I will try something again, even though I'm still ill (but I plan to be better tomorrow ;) )

-------------------------

elix22 | 2021-10-30 07:57:37 UTC | #12

Good luck 
Have fun in making your games , that’s the most important thing

-------------------------

dertom | 2021-11-21 21:35:33 UTC | #13

trijam146 - theme: fast food, fast dude.
Here my 5h entry. First time as web-deployment thanks to @elix22
https://dertom1895.itch.io/triburger-run

-------------------------

