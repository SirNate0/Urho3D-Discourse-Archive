dev4fun | 2018-02-02 02:12:51 UTC | #1

I was using this tutorial ([https://discourse.urho3d.io/t/levels-fade-effect/2257](https://discourse.urho3d.io/t/levels-fade-effect/2257)), and I believe that has memory leak on some part of the code, I dont know where. Everytime when I change level/scene, memory of game its increased. 

I would like to know if someone can help me to found this memory leak and fix it, Im newbie on Urho3D and Im appreciating it so much.

Thanks!

-------------------------

dev4fun | 2018-02-02 03:05:27 UTC | #2

#Update 1 : I used UI::Clear to release scene/level, and now looks better... have more something to release all correctly?

#Update 2 : I was debugging the code, and I see that was not running the code **Dispose** (where should be release scene and elements of current level). Someone know why it isnt called?

-------------------------

artgolf1000 | 2018-02-02 03:51:41 UTC | #3

I have fixed the code.

-------------------------

dev4fun | 2018-02-02 04:32:03 UTC | #4

@Fixed. Thanks for your help!

-------------------------

