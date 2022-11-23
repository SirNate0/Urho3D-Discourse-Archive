thebluefish | 2017-01-02 00:58:50 UTC | #1

Hi guys,

Thought I would share a couple little snippets of mine. You can find them [url=https://github.com/thebluefish/Urho3D-Misc]at my github repository[/url]. All are MIT licensed, so do what you wish with them. 

[u]InputManager:[/u]
- I have submitted a pull request to the main Urho3D branch to fix the joystick and controller support. The latest branch for InputManager reflects this.
- If you are using any older version of Urho3D, the changes that I have submitted should still work, but will not support joysticks. [url=https://github.com/thebluefish/Urho3D-Misc/tree/9345f652652a135eae66cbf5c9442c1031723409]Please use this branch instead[/url] if you are working with any older build of Urho3D.

Each project should each be sufficiently documented, and I will provide updates as they come along. If you have any changes, suggestions, or comments then please let me know.

-------------------------

cadaver | 2017-01-02 00:58:50 UTC | #2

The idea of the InputManager is very nice, a bit similar to Unity's input axes abstraction. Something like this could be useful directly in Urho3D, would just have to make sure it stays as simple and generic as possible, as game-specific input has potential to turn into a complex subject, with various smoothing and dead zone settings.

-------------------------

thebluefish | 2017-01-02 00:58:51 UTC | #3

[quote="cadaver"]The idea of the InputManager is very nice, a bit similar to Unity's input axes abstraction. Something like this could be useful directly in Urho3D, would just have to make sure it stays as simple and generic as possible, as game-specific input has potential to turn into a complex subject, with various smoothing and dead zone settings.[/quote]

Mine is definitely not a perfect fit for Urho3D, it's just something that worked for my particular game. Although [url=http://urho3d.prophpbb.com/topic183.html]this particular issue[/url] is the only game-breaking problem that I've been dealing with.

Feel free to integrate what you want though. Most of my works are going to be contributed back to the Urho3D project at some time or another.

-------------------------

