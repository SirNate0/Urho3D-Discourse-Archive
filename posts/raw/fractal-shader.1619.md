ghidra | 2017-01-02 01:08:58 UTC | #1

[url=http://i.imgur.com/nbIShnP.png][img]http://i.imgur.com/nbIShnPl.png[/img][/url]
[url=http://imgur.com/0OqIqWB.png][img]http://i.imgur.com/0OqIqWBl.png[/img][/url]

I've been spending some time learning a few aspects of the engine, that all kind of came together in this little fractal shader example.
The fractal shader code I adapted from [url]http://hirnsohle.de/test/fractalLab/[/url].

The example is written in angelscript, the shader in glsl. Also, it is perpetually a work in progress. It employs several elements provided by the engine that might be useful for learning purposes other than just the shader. Like saving and loading a file, and building a specific type of gui ( more involved than the gui example, and less involved than the editor gui code ). I think that it would be super cool to include in the engine as an example.. but I fear that the fractal shader license might prohibit that. however, it's here otherwise.

As, well I'm not sure the best way to post this information..

It's part of a repository i maintain that also houses a few other experimental things ( which I am happy to share as well ). So for now, I will just list the relevant files to this specific file.

[b]Where to get the files:[/b]
Here is the repo: [url]https://github.com/ghidra/urho_research[/url]

[b]Relevant files:[/b]
[ul]
Scripts/fractal.as
Shaders/GLSL/fractal.glsl
RenderPaths/Fractal.xml
fractal_settings/*
[/ul]

fractal_settings holds the "bookmark" files. A save file of settings. There are 4 currently saved.
I have a launch script that I run from the root of that repo. Totally optional, but I find it useful. the shell script is this:

[code]
if [ $# -eq 0 ]; then echo "what script should i run?"; else /PATH_TO_URHO/bin/Urho3DPlayer /Scripts/$1.as -pp /PATH_TO_URHO/bin -p "CoreData;Data;Research"; fi
[/code]

It requires that you have a "Resource" directory next to Data and CoreData, or remove that from the script. You can then run this like:

[code]
sh launch.sh fractal
[/code]

[b]Controls:[/b]
P - toggle parameter pane
F - toggle fullscreen (fullscreen will be slow)
F1-F10 - save bookmarks
1-0 - load bookmarks
Shift - camera speed * 0.01
Ctrl - camera speed *0.01
Alt - camera speed *0.01
(Shift-Ctrl-Alt stack to make the camera move super slow, you'll notice why)

[b]Just some notes:[/b]
I'll probably spend some time to make more preset bookmarks
Might do some extra work on the gui to be able to type in a value next to the slider
There are a few more shader attributes that I need to expose (having issues using int uniforms as iterators)
Happy Holidays!

-------------------------

sabotage3d | 2017-01-02 01:08:59 UTC | #2

That's really cool.

-------------------------

TikariSakari | 2017-01-02 01:08:59 UTC | #3

The pictures look really awesome. First one makes me think of some futuristic city, where the pollution has landed and second one could be a space station. That is what I thought when I saw the images, I didn't really think of fractals there. Nice work!

-------------------------

weitjong | 2017-01-02 01:08:59 UTC | #4

Cool!

-------------------------

codingmonkey | 2017-01-02 01:09:00 UTC | #5

Nice! But how many FPS you are have with this?

-------------------------

Modanung | 2017-01-02 01:09:01 UTC | #6

That's friggin' awesome!  :astonished:
Thanks for sharing.

-------------------------

ghidra | 2017-01-02 01:09:02 UTC | #7

[quote]But how many FPS you are have with this?[/quote]

It varies. Depending on the type of fractal algorithm used, and the settings dialed in relative to your hardware and resolution.
There are a few paramaters that might also assist in getting faster. Right now its a hard coded 8 iterations (That's also the setting that I was having issues passing in as a uniform. If I pass it in, it just doesnt iterate).

Lenovo y480 (Nvidia GeForce GT 640M)
-------------------------
full screen (1366 x 768 ): 12 fps
half sceen (683 x 383 ): 30 fps

Desktop (Nvidia GeForce GTX 570)
-------------------------
full screen (1920 x 1080 ): 15-30 fps
half sceen (960 x 540 ): 70-120+ fps

On the laptop, i didnt spend too much time testing. On the desktop, I ran the 2 examples seen above. The blue, mandlebox example was the slowest frame rate, and the pinkish mengersponge example ran the quickest.

-------------------------

rasteron | 2017-01-02 01:09:03 UTC | #8

This looks great Jimmy! :slight_smile:

-------------------------

