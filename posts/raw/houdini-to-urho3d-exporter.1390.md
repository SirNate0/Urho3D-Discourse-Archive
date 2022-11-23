ghidra | 2017-01-02 01:07:24 UTC | #1

[url]https://github.com/ghidra/htou/blob/master/README.md[/url]

[img]https://cloud.githubusercontent.com/assets/5643219/10115780/a1682e58-63e3-11e5-8c42-fdadf75d6fcc.png[/img]

I've been spending some time building a bare bones mesh expoter to get geometry from houdini into urho with out the blender middle man. (dont get me wrong I do love blender, but removing a step, actualy 2 exports, makes me feel better).

Houdini offers some great node basesd/ visual programming style workflow that is quite fun. And now I'm able to build levels in there and export them straight out to urho.

The exporter is very limited at the moment, and only supports the simple things that are relevant to my projects at the moment. It might be worth a look to anyone that is interested in houdini and urho.

(side note, the images are low poly simply because that is the aesthetic I am going for right now. the exporter handles smooth normals, and uv and uv2 for textures)

-------------------------

Enhex | 2017-01-02 01:07:25 UTC | #2

Looks great! Time for oldschool Runescape clone :wink:

-------------------------

rasteron | 2017-01-02 01:07:25 UTC | #3

I haven't tried Houdini yet, but this is looking good Jimmy :slight_smile:

-------------------------

boberfly | 2017-01-02 01:07:25 UTC | #4

I'm a huge fan of Houdini! Thanks for sharing.

I've not looked into this, but have you seen houdini engine? That could be quite powerful for Urho3D integration, for smart assets.

-------------------------

ghidra | 2017-01-02 01:07:25 UTC | #5

Houdini Engine is a promising plug in. But so far in the existing implmentation it's not really so great. In maya its excruciatingly slow. And as far as unreal and unity go, i assume its not any faster, and the most exicting part, the posibilty of it being runtime, it IS NOT. Which kind of removes any real advantage other than having access to the libraries under the hood of houdini. 

Thus this exporter. I kind of get the same value I would using houdini engine, albiet not "inside" of urho. But that's no great loss. 

Until SideFX figures out how to make the engine work during run time, I have no interest in it for game engines. I assume that they havent looked too much into it, because of the licensing. How would they charge someone that can package up the engine and send it along with games to run on all client machines? 

I'd rather just build the components inside of urho, and build the node based interface to have real native to urho runtime proceduralism. But I am not the person to do that, unless you want to wait a decade. and even then I'll still be trying to figure out how to seprate namespaces, or cmake, or any other simple c++ concept that I get hung up everyday.

-------------------------

sabotage3d | 2017-01-02 01:07:25 UTC | #6

Thanks for sharing, will be quite useful.

-------------------------

