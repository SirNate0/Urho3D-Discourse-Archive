gasp | 2017-01-02 00:58:22 UTC | #1

Hello i'm new to the Urho 3d engin ,
i'm a programmer but not a game programmer, a lot of concept are really new to me.  (i know SQL, php, Windev ..)
(i don"t see a presentation part in the forum and don't want to obfuscate the general discution with a simple "Hello World")


i start to explore the Urho3D engine, love it.

i'm a french, with a french keyboard (AZERTY) so the standard movment key 'AWSD' doesn't work.

Did we have a way to get the keyboard layout (sorry for my stupid question) so we can arrange the exemple via an Angel Script ?

-------------------------

cadaver | 2017-01-02 00:58:22 UTC | #2

SDL doesn't have functions to get the layout, but it has functions to query the relation of a specific scancode (physical location of key) and keycode, or the other way around. See

[wiki.libsdl.org/CategoryKeyboard](http://wiki.libsdl.org/CategoryKeyboard)

However, we need to expose these functions in the Urho input API first, they're not exposed yet. Also, the key events need to be expanded to contain SDL scancodes, as well as adding the possibility to query for key up/down by scancode, which should solve the WASD problem.

-------------------------

gasp | 2017-01-02 00:58:22 UTC | #3

Thanks you i have see the issue in GitHub.

-------------------------

