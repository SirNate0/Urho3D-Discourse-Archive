dhasenan | 2017-01-02 01:01:46 UTC | #1

I'd like to support rebindable keys in my game. As far as I can tell, this requires me to create a mapping from Urho key identifiers to user-visible names, poll for keyboard input while in rebinding mode, loop through all the keys to find out which ones are pressed, and then come up with the appropriate textual representation. Then I want to save this information to a config file in a human-readable format, so that means parsing that textual representation as well...

Repeat the same for mouse buttons.

For joysticks, it's even more fun. I can show the user "Joystick 1 Axis 3", but I'd rather be able to show them something like "XBox 360 Controller 1 Left Trigger", ideally with appropriate graphic.

Has anyone got a good library for this? I know it's not builtin because the editor keys are hard-coded (which is so fun with my Dvorak keyboard...)

-------------------------

GGibson | 2017-01-02 01:01:46 UTC | #2

I've been curious about this too so searched a bit. Here are a couple different approaches others are using or suggesting based on the underlying SDL.

[url]http://www.gamedev.net/topic/546583-sdl-custom-input/[/url]
[url]http://retrocenturygames.wordpress.com/2012/09/28/custom-key-binding-in-sdl/[/url]

Let us know if you get something good working!

-------------------------

thebluefish | 2017-01-02 01:01:55 UTC | #3

I made an InputManager class to support keybinding. You can find the original post here: [topic187.html](http://discourse.urho3d.io/t/a-little-inputmanager-and-dll-loader/203/1)

It doesn't have all of the features that you're looking for. However some of the features are UI-specific, such as setting a new keybind. You would want to get this yourself, then setup the keybinding in InputManager.

If you have any specific feature requests, feel free to respond to that thread and I will add them in.

-------------------------

friesencr | 2017-01-02 01:01:55 UTC | #4

I have an old branch that allows for rebindings in the editor.  I will try to get to it but I havn't had much time to do anything outside of work the past couple of months.

-------------------------

