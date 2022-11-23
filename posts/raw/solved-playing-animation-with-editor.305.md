Bluemoon | 2017-01-02 00:59:30 UTC | #1

Is there a way to play animation in the Editor, if there is, can someone be kind enough to explain to me how (or would I have to use scripts). If there isn't yet, then is there any plan of implementing it later as time goes by. Humbly waiting for your replies, thanks alot :smiley:

-------------------------

friesencr | 2017-01-02 00:59:30 UTC | #2

On the animation model, up the animation count and set the animation you want to see.

Made a video of it: [youtube.com/watch?v=wwI4iumgZKQ](https://www.youtube.com/watch?v=wwI4iumgZKQ)

-------------------------

Mike | 2017-01-02 00:59:30 UTC | #3

Not as fast as friesencr, here are some more tips:

Almost any kind of animation can be played in the Editor:

AnimatedModel:
- Select the AnimatedModel in 'Hierarchy' panel
- In 'Attribute inspector' panel > AnimatedModel, scroll to bottom and set Anim State Count to the number of animation files (*.ani) and press enter
- Scroll to bottom and click 'Pick' buttons to browse to your animation files (for Jack it is Jack_Walk.ani located in 'Bin/Data/Models' folder)
- Set Weight to 1 and click on the 'Test' button to play/pause your animation
If you want to test it instantly, run example 18_CharacterDemo, press one of the WSAD keys (to trigger walk animation) and simultaneously press the 'F5' key to save the scene.
Then open this scene (located in Bin/Data/Scenes/CharacterDemo.xml) in the Editor, press the 'Play' button located top-left, select Jack and check the AnimatedModel settings in the 'Hierarchy' panel

For AnimatedSprite2D, ParticleEmitter2D, ParticleEmitter and shader animations, simply press the 'Play' button located top-left.
I think BillboardSet and animations from examples 30 and 31  are the only exceptions.

-------------------------

Bluemoon | 2017-01-02 00:59:31 UTC | #4

Thanks a lot Mike and Friesencr, I now have it figured out :smiley: . I never knew it was just there staring at me :astonished:

-------------------------

