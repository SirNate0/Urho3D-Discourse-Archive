Jimmy78 | 2017-01-02 01:15:39 UTC | #1

Hey guys , is there any guide/documentation on how to use the Urho3D editor ?

I just opened it and i'm completely lost . 

I tried to check some youtube videos but they all already have the scene , plane etc..already setup and they don;t show how to get things started ...

This is the only documentation i found which is pretty bad : [urho3d.github.io/documentation/ ... tions.html](https://urho3d.github.io/documentation/1.3/_editor_instructions.html)

-------------------------

rasteron | 2017-01-02 01:15:40 UTC | #2

Hey there Jimmy78,

Welcome to the forums! I think the best way to get started is to learn by example. The package already has a lot of demo/example scenes by feature for the purpose of learning as well. You can just open and examine them one by one, so start from Hello World.. :slight_smile:

-------------------------

Vincentwx | 2017-01-02 01:15:41 UTC | #3

I found this one very helpful when I played with the editor. 

[darkdove.proboards.com/thread/15 ... mple-guide](http://darkdove.proboards.com/thread/15/urho3d-editor-simple-guide)

-------------------------

hicup_82017 | 2017-09-01 19:47:52 UTC | #4

Hi,
I had hard time understanding how the editor starts the game.
I read the documentation few times and surfed the blogs and videos, and below is my understanding.

Can you guys correct my understanding?

**My understanding:**
1. Editor is just like 3d paint (editor) tool, it does not start whole game by itself.
2. However, it might support playing of animations or some physics things as shown in, last part of  http://darkdove.proboards.com/thread/15/urho3d-editor-simple-guide. 
3. We got to run the game separately and use editor capabilities to modify the scene files. These files can be dynamically loaded in to the game, via scripts or C++ code.
3.1 I tried to save a scene while running example 18_CharacterDemo as suggested by Mike and Editor played the walk animation as explained in that thread. 
**Confusing part is:**
4. I see in some videos, the editor looks like its playing the game, for example, 
https://www.youtube.com/watch?v=H-hZ6JegDe0. But I doubt designer just put some animations, which can be played by Editor.

-------------------------

Eugene | 2017-09-01 20:15:02 UTC | #5

[quote="hicup_82017, post:4, topic:2472"]
But I doubt designer just put some animations, which can be played by Editor.
[/quote]
If you organize your scene to be "self-executed" via script and logic components, you could perfectly run it within the Editor. The only exception is controllable characters and other user input that is obviously interfered by the Editor.

-------------------------

lezak | 2017-09-01 20:21:15 UTC | #6

Basically Your understending is right, as for confusing part: by default scene in editor doesn't update (is paused), but pressing "play" button will unpause it and therefore it will start updating (children and physics). Easiest way to see this in action is placing some physics object in the scene or You can add some component that uses sceneupdate event ( for example "rotator" from Scripts/Utilities). 
Note that in Urho You have seperate events for application update and scene updates. Scirpted components and objects derived from LogicComponent in their update() and postupdate() functions use scene events.

-------------------------

hicup_82017 | 2017-09-03 13:24:09 UTC | #7

Thanks @lezak and @Eugene  
Any chance that you have an example that i can look, which shall help me to understand, how sample scripts can be bind to nodes.
I searched over examples, and tried to load Ninjasnow war example from editor, just to see how the scripts can be associated to nodes. 
But, I could not see any script associations if i just loaded the scene.
I tried the 18- character demo example, but it still did not help me with this part.

My plan is to stick with C++ , but just want to understand how I can use scripts along with editor.

**Update:** Able to save Ninja Snow war, when the game is running. Now, I am able to see how the script instances are linked to nodes.

-------------------------

