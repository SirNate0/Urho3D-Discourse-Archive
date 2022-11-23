cin | 2017-01-02 00:57:41 UTC | #1

[video]http://www.youtube.com/watch?v=sENyBeweaUc[/video]

Scrolling prefabs is good looking idea. :bulb:

-------------------------

weitjong | 2017-01-02 00:57:42 UTC | #2

I have not tried BGE before. I wonder in the video how the side of wall is being selected as there are four possible sides in each tile.

-------------------------

Kamil | 2017-01-02 00:57:43 UTC | #3

[quote="weitjong"]I have not tried BGE before. I wonder in the video how the side of wall is being selected as there are four possible sides in each tile.[/quote]
You can see that the tile cursor has an "edge" pointer to show which side the wall is being placed on. I imagine the tile is split into 4 triangle hotspots for the 4 sides.

-------------------------

weitjong | 2017-01-02 00:57:43 UTC | #4

Thanks for your reply. I do see the "edge" thingy in the video but was wondering how it is being placed/chosen quickly like in the video. Your explanation makes sense.

It is wonderful if we could have something like that in our editor. I don't like everything to appear squarish though.

-------------------------

friesencr | 2017-01-02 00:57:44 UTC | #5

I have something that i wrote which browses all resources.  Problem is that it is a big pain in the butt.  It touches lots of parts of the editor code.

[github.com/friesencr/Urho3D/tre ... ce_browser](https://github.com/friesencr/Urho3D/tree/resource_browser)

It isn't pretty like your suggestion but it scans your hard drive, detects all the types,  and adds the editors abilities to all the files contextual via right click.  There are some drag and drop things I have added.  You can drag a prefab in the hierarchy and it instances a prefab there.  You can drag a material on a mesh and it will raycast and assign the material.  It has some really nice things but the code is very hard to make perfect (at least with my mediocre ability).  The search I added is genuinely a really nice feature.  I have put probably 150 hours into making it and it sucks that I haven't been able to get it to the 100% mark.

I personally don't think its that great right now but if other people think it is worth while then maybe I can work on it some more.

-------------------------

scorvi | 2017-01-02 00:57:48 UTC | #6

hey 

i am working this week on an object assembler (like this one from blender: [url=http://www.blendernation.com/2014/01/08/add-on-object-assembler/]object-assembler[/url]). 
so that i can create my ships with the model parts from: [url=http://www.blendernation.com/2011/09/14/model-download-shipyard-v0-7/]blend nation[/url] (example: [url=http://ship.shapewright.com/?name=asd]shapewright[/url])

i am working with this engine only for a month now and cannot say that i know every feature it has.
so if there are things predestined to be used for this, can you show it to me ^^ 

for now i am using the prefabs idea to describe the parts. 
the prefabs will contain the model component and a connector component.
the connector only has an array of the position and rotation of the connection points, where a new model object can be placed. 

so at first i have to load the model parts and give them connection points. then save them as prefabs. 
after creating these prefabs i can load them to the object assembler and create a new model with those parts ... 

thats my idea for now ... any ideas to do it better ? 

i wanted to implement it in the editor but dont know how.
i thought to create a window like the matrial editor, where you can load a model and then select a triangle or quad where to set the connection points. 
But then i have to create the object assembler in the editor ... can i just create a new picking state, where the conection points a visible as spheres and if you click on them the selected object part will be placed there ? 
is there a better way to create that ? one problem is that i am only coding in c++ and dont have an ide for AngelScript .. is there an IDE for AngelScript with auto completion ? 

ps: didnt know if i should create a new topic ... :-/

-------------------------

