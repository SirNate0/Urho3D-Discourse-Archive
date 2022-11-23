gawag | 2017-01-02 01:09:57 UTC | #1

There's this super long thread regarding an Urho wiki ([topic778.html](http://discourse.urho3d.io/t/urho-wiki/760/1)):
In short there are wishes for a wiki and I accidentally started one at [github.com/urho3d/Urho3D/wiki](https://github.com/urho3d/Urho3D/wiki). So there's some activity and need for more (Urho) resources.

What kind of wishes and ideas are there regarding Urho or game development resources in general (doesn't have to be a wiki)? For example Unity has this asset store with assets being in a format for their toolset and engine.

Are there some libraries or something that extend Urho? There's also a thread regarding a 3rd party GUI. Is there something usable around? Does someone have something that could be turned into a piece that can be used by other Urho users as well? It doesn't have to be free if someone wants some kind of compensation, but of course free would be better. For example there's this commercial SpeedTree library around and some engines have a wrapper for that.
Like Ogre has these pages about libraries that can extend their engine and their are often with wrappers: [ogre3d.org/tikiwiki/tiki-ind ... +Libraries](http://www.ogre3d.org/tikiwiki/tiki-index.php?page=List+Of+Libraries)

Stuff that I would like for the Urho projects that I started or plan:
- grass and other vegetation (like [ogre3d.org/tikiwiki/tiki-ind ... try+Engine](http://www.ogre3d.org/tikiwiki/tiki-index.php?page=PagedGeometry+Engine))
- weather system with a day night system, clouds and effects (like [ogre3d.org/tikiwiki/tiki-index.php?page=SkyX](http://www.ogre3d.org/tikiwiki/tiki-index.php?page=SkyX))
- water (like [ogre3d.org/tikiwiki/Hydrax](http://www.ogre3d.org/tikiwiki/Hydrax))
- GUI (CEGUI, MyGUI,... I was never happy with any system that I tried in my Ogre days)
- maybe voxel based terrain (smooth one like in SpaceEngineers, MedievalEngineers and TUG, or those block based systems like in Minecraft, FortressCraft,...)
- assets, a variate of Urho ready models (with Blender files if available) and materials would be a great help to start a project or game dev in general

I'm actually currently working on a GUI and the Urho wrapper is making great progress. A first prototype could be released relatively soon.
First image: [i.imgur.com/sTEVNfz.jpg](http://i.imgur.com/sTEVNfz.jpg) On the top is the Urho version with the output left and in the bottom the Qt version with the output on its right.

So:
Is there something around?
Does someone have something made in/with/for Urho that could be turned into a library or whatever?
Is someone willing to participate in some area?
What is mostly needed?
What about "documentation" stuff like articles and howtos? Wiki? Wishes? Ideas? Help offerings?
Other ideas/wishes?

-------------------------

Sir_Nate | 2017-01-02 01:10:11 UTC | #2

Well, I've added a few features to theBlueFish's libRocket integration, though it isn't exactly finished (I think I would call it usable, though one might have to make a few fixes or add a few more features as desired):
[url]https://github.com/SirNate0/libRocket-Urho3D[/url]

There's also the ProcSky stuff for basic sky effects (it gives excellent sky color, but it presently lacks clouds).
A nice thing would be to port SkyX/Hydrax to Urho, but with the fairly different coding model (and the difficulty in actually finding them with all of the needed resources), this could prove challenging.

OpenGameArt(.org) is a decent resource site -- I've found quite a bit of music I like there, but as to the 3d assets, I haven't looked much as I make my own to suite my needs...

-------------------------

TheComet | 2017-01-02 01:10:12 UTC | #3

One thing I really had trouble with when starting with Urho3D is understanding just the basic concepts of how to work with the engine. Stuff like how intrusive shared pointers work, what SharedPtr is for and how to use them, or stuff like how the ResourceCache works, or a basic overview of how events work (what is a VariantMap, what is P_KEY, etc.)

The very basic information is missing and it's pretty hard for the total newcomer to wrap their head around this engine. I would like to see this kind of information in the wiki. I can help with writing about this if you need someone.

-------------------------

gawag | 2017-01-02 01:10:13 UTC | #4

...somehow I didn't get notified that there have been posts to this thread... just saw that by random... weird.

libRocket and ProcSky sound great!
I tinkered a bit with billboard clouds in my first Urho project which was a flight simulator and they worked quite well (if I remember correctly) unless you flew through them (the rotation looked weird). Maybe that could be improved and turned into something primitive or extend ProcSky. I'm scheduling that to somewhere in the future...
Could there be 3D/volumetric textures be used for clouds? I have never used 3D/volumetric textures and have no idea how they work (could someone make a wiki article? added to wishlist: [github.com/urho3d/Urho3D/wiki/Wishlist](https://github.com/urho3d/Urho3D/wiki/Wishlist)).

I made a new page for the (two) existing libraries: [github.com/urho3d/Urho3D/wiki/Libraries](https://github.com/urho3d/Urho3D/wiki/Libraries)

I'm currently quite focusing on my GUI project: [lfgui.github.io/](http://lfgui.github.io/) It's not that super far but some things are already working and it could be used depending on what someone needs. I'm currently working on a real font system, keyboard events and lineedits.

[quote]One thing I really had trouble with when starting with Urho3D is understanding just the basic concepts of how to work with the engine. Stuff like how intrusive shared pointers work, what SharedPtr is for and how to use them, or stuff like how the ResourceCache works, or a basic overview of how events work (what is a VariantMap, what is P_KEY, etc.)
The very basic information is missing and it's pretty hard for the total newcomer to wrap their head around this engine. I would like to see this kind of information in the wiki. [/quote]

Good ideas.
Shared pointer are already familiar for those who know C++11, but Urho is a bit weird as it sometimes gives/uses SharedPtr and sometimes nacked pointer. I think I read about that somewhere. That should be explained especially for those unfamiliar with memory management / smart pointer.
There was already the idea to make an article about the event system and which event sends what kind of data and with which values. Like a reference list.
Does the ResourceCache store every requested resource indefinitely? It may be needed to unload no longer needed stuff. I don't really know how it works.

[quote]I can help with writing about this if you need someone.[/quote]
Oh yes always!  :smiley: 
There's the wishlist where I have no ideas about most of the points. I scheduled for myself to work on the first three points and look into asynchronous resource loading where I have at least an idea.
You could pick something from the list or write about something else or add ideas to the list. There's also the idea to make simpler step by step setup and "first project" tutorials like the ones on the Unofficial Wikis. There may be more ideas in the wiki thread or in the unofficial wikis.

Oh, it would be also helpful to get more information (from newcomers and others as well): What was hard? What was not really explained? What was unexpected or weird? What should be explained (differently)? Where is Urho3D weird (to use)?

-------------------------

Modanung | 2017-01-02 01:10:26 UTC | #5

The page on [url=http://urho3d.github.io/documentation/1.5/_conventions.html]conventions[/url] of the documentation mentions the Ptrs.

-------------------------

