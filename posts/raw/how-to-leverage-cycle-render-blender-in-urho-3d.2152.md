saket | 2017-01-02 01:13:30 UTC | #1

Hi, 
My accept my warm love to community , i am an iOS developer by profession and looking for making 3d apps ( idea is apps with game graphics  ) .
I found urho samples enough for motivation .

as the documentation is still in progress i found U-tube is rich with blender example ([b]i couldn't learn Urho editor  as there is no docs or videos[/b] ) 

Problem that i am facing is , every video in u-tube uses cycle renderer and urho3d exporter doesnt support it .

is there a workaround for this pain? 

Please guide me through it .
Thanks in advance

-------------------------

1vanK | 2017-01-02 01:13:30 UTC | #2

Cycles uses nodebased materials, so that they can be whatever complexity. Urho3d usues a fixed set of textures, so Blender Internal is ideal for exporting.

-------------------------

hdunderscore | 2017-01-02 01:13:31 UTC | #3

You can bake cycles renders to textures and load them into Urho. Baking in cycles isn't super straight forward, so you'd need to look up a tutorial.

-------------------------

Sir_Nate | 2017-01-02 01:13:32 UTC | #4

Other than that you can probably try writing your own shaders and techniques to try and imitate the cycles effects, but baking is almost certainly the way to go (far less complex, likely a far better result given that you get to employ Blender's renderer that is meant for what you're editing).
I myself haven't messed with Cycles, so I can't really help you other than my above postulation.

-------------------------

Modanung | 2017-01-02 01:13:34 UTC | #5

Could it be you're looking for something like [url=https://www.youtube.com/watch?v=DiIoWrOlIRw]this[/url]?

-------------------------

