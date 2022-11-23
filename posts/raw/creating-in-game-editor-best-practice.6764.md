HappyWeasel | 2021-03-20 08:39:01 UTC | #1

Hi Guys,

I want to create a kind of level/terrain editor part of the game experience.. think about something like the AOE2 built-in-editor ... something the user could use from within the game... 

Should I just "bundle" the urho3d editor right away, starting the whole thing with the editor as "main", having the editor disabled during normal gameplay (bascially editor f12 mode) and when In editor mode, the editor would popup, where I would have added  the needed funcitonality and UI there (both probably in angelscript) and  disabled  some of the unneeded (in the context of my game editor) editor stuff ..

or or should I write an own in-game editor "mode" (at present everything is C++, so that probably would be totally C++ aswell) ... that's the current status.. 

I think both ways are possible.. 

If its the editor, then I probably need syntax hightlighting for angelscript in the IDE somehow :-)

-------------------------

JTippetts1 | 2021-03-20 23:04:50 UTC | #2

IMO, you should build your own editor. The Urho3D editor is pretty janky, and if you're looking for a game-specific experience like the AOE2 editor, it's not really easy to customize in that way. I built my [terrain editor](https://github.com/JTippetts/U3DTerrainEditor) separate from the Urho3D editor specifically because I was looking for a more specific tool and was partially inspired by the Age of Empires editor. Trying to repurpose the Urho3D editor just didn't really appeal to me, because I didn't need general purpose scene editing; I needed terrain tools and doodad scattering.

-------------------------

JSandusky | 2021-03-21 02:47:47 UTC | #3

I second write the editor yourself (though you might want to graft some parts from the existing one).

You probably want the editor to be more tied to your actual game-data than entirely free access, even if only to lower your support headache. It's far more likely you just want to be editing terrain and placing "TroopUnits" (or w/e) than looking at entire scene tree complete with bones and other gobbly-gook.

-------------------------

HappyWeasel | 2021-03-22 19:36:24 UTC | #4

Thanks guys for your freedback. That's probably want I am gonna do..

-------------------------

