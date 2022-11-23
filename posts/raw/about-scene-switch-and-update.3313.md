ChunFengTsin | 2017-07-03 03:19:33 UTC | #1

Dear all,
In my project , have three scene class and a MainGame class:
StartScene 
MainMenuScene
BattleScene

everyone of the three class include a Scene object and  not inherit Application.

MainGame is inherit Application.

But the scene can't update ,and  the event of scene is lose efficacy.

Now I want to know how to update scene.

Is I have to let them inherit Application ??

-------------------------

ChunFengTsin | 2017-07-05 15:06:22 UTC | #2

I have solved this problem , just a small mistake. 
I forget to run the function about loading scene after i instantiation the scene class.
:joy:

-------------------------

