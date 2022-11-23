globus | 2017-01-02 01:05:35 UTC | #1

It's an interesting thing but not implemented in the examples.

I did not find the [b]position setting[/b] for a zone in the editor and in Zone.h
It is also not visible in the editor, if not highlighted in the scene tree.

I want ease of manipulation for the zones - how  for other (visible) objects in the scene.
Like:
[img]http://i.piccy.info/i9/74974ad7ff49e6cec1e518fc1d4dddfe/1434613593/21889/912050/zone.jpg[/img]
I think would be good if the dummy will be replaced with primitives in editor.
Primitives may take a material appropriate to their type (audio emmiter, trigger, zone, etc.)
Not the standard primitive form can be added by user from any editor of 3D.
As in Urho editor - Builting objects.

In addition, well, if there is a drop-down list to set the flag visibility of objects by type

-------------------------

globus | 2017-01-02 01:05:36 UTC | #2

Also, dummy objects can be visible in scene as icons
example - lamp icon [img]http://i.piccy.info/i9/714286015ccedc2571364862375be68b/1434662806/13649/912050/lamp.jpg[/img]
But should be able to be selected directly in scene.
and be able to move rotate et al.

-------------------------

globus | 2017-01-02 01:05:38 UTC | #3

[img]http://i.piccy.info/i9/fcd3fee8d0174d357b1dcead4a8ab5e3/1434982646/81620/912050/home.jpg[/img]

-------------------------

globus | 2017-01-02 01:05:38 UTC | #4

My final goal is to do realization for clipping geometry using portals.
Seamless transition for indoor/outdoor scenes.

[b]Torque 3D Portals[/b] is children from the [b]Zone[/b] objects (c ++)

Description of the [b]Portal[/b] under the spoiler:
[spoiler]An object that provides a "window" into a zone, allowing a viewer to see what's rendered in the zone. 

A portal is an object that connects zones such that the content of one zone becomes visible in the other when looking through the portal.

Each portal is a full zone which is divided into two sides by the portal plane that intersects it. This intersection polygon is shown in red in the editor. Either of the sides of a portal can be connected to one or more zones.

A connection from a specific portal side to a zone is made in either of two ways:

By moving a Zone object to intersect with the portal at the respective side. While usually it makes sense for this overlap to be small, the connection is established correctly as long as the center of the Zone object that should connect is on the correct side of the portal plane. 
By the respective side of the portal free of Zone objects that would connect to it. In this case, given that the other side is connected to one or more Zones, the portal will automatically connect itself to the outdoor "zone" which implicitly is present in any level. 
From this, it follows that there are two types of portals:

Exterior Portals 
An exterior portal is one that is connected to one or more Zone objects on one side and to the outdoor zone at the other side. This kind of portal is most useful for covering transitions from outdoor spaces to indoor spaces. 
Interior Portals 
An interior portal is one that is connected to one or more Zone objects on both sides. This kind of portal is most useful for covering transitions between indoor spaces./dd> 
Strictly speaking, there is a third type of portal called an "invalid portal". This is a portal that is not connected to a Zone object on either side in which case the portal serves no use.

Portals in Torque are bidirectional meaning that they connect zones both ways and you can look through the portal's front side as well as through its back-side.

Like Zones, Portals can either be box-shaped or use custom convex polyhedral shapes.

Portals will usually be created in the editor but can, of course, also be created in script code as such:

Script:
[code]// Example declaration of a Portal.  This will create a box-shaped portal.
new Portal( PortalToTestZone )
{
   position = "12.8467 -4.02246 14.8017";
    rotation = "0 0 -1 97.5085";
    scale = "1 0.25 1";
    canSave = "1";
    canSaveDynamicFields = "1";
};[/code]
Note:
Keep in mind that zones and portals are more or less strictly a scene optimization mechanism meant to improve render times.[/spoiler]

Description of the [b]Zone[/b] under the spoiler:
[spoiler]An object that represents an interior space. 

A zone is an invisible volume that encloses an interior space. All objects that have their world space axis-aligned bounding boxes (AABBs) intersect the zone's volume are assigned to the zone. This assignment happens automatically as objects are placed and transformed. Also, assignment is not exclusive meaning that an object can be assigned to many zones at the same time if it intersects all of them.

In itself, the volume of a zone is fully sealed off from the outside. This means that while viewing the scene from inside the volume, only objects assigned to the zone are rendered while when viewing the scene from outside the volume, objects exclusively only assigned the zone are not rendered.

Usually, you will want to connect zones to each other by means of portals. A portal overlapping with a zone

Script:
[code]// Example declaration of a Zone.  This creates a box-shaped zone.
new Zone( TestZone )
{
   position = "3.61793 -1.01945 14.7442";
   rotation = "1 0 0 0";
   scale = "10 10 10";
};[/code]
Zone Groups
Normally, Zones will not connect to each other when they overlap. This means that if viewing the scene from one zone, the contents of the other zone will not be visible except when there is a portal connecting the zones. However, sometimes it is convenient to represent a single interior space through a combination of Zones so that when any of these zones is visible, all other zones that are part of the same interior space are visible. This is possible by employing "zone groups".[/spoiler]

-------------------------

globus | 2017-01-02 01:05:38 UTC | #5

The class hierarchy for the [b]Portal[/b] with description:

[color=#008000] A transitioning zone that connects other zones.

 Basically a portal is two things:

1) A zone that overlaps multiple other zones and thus connects them.
2) A polygon standing upright in the middle of the portal zone's world box.

When traversing from zone to zone, portals serve as both zones in their own
right (i.e. objects may be located in a portal zone) as well as a peek hole
that determines what area of a target zone is visible through a portal.

Torque's portals are special in that they are two-way by default.  This greatly
simplifies zone setups but it also complicates handling in the engine somewhat.
Also, these portals here are nothing but peek holes--they do not define transform
portals that could be looking at a different location in space altogether.

Portals can be marked explicitly as being one-sided by flagging either of the portal's
sides as impassable.  This flagging can also be used dynamically to, for example, block
a portal while a door is still down and then unblock the portal when the door is
opened.

Portals are classified as either interior or exterior portals.  An exterior portal is
a portal that has only non-SceneRootZone zones on side of the portal plane and only the
SceneRootZone on the other side of it.  An interior portal is a portal that has only
non-SceneRootZone zones on both sides of the portal plane.  A mixture of the two is not
allowed &ndash; when adding SceneRootZone to a portal, it must exist alone on its portal
side.[/color]
[color=#0040BF]class[/color] [b]Portal[/b] : [color=#0040BF]public[/color] [b]Zone[/b]

----------------------------------------------
[color=#008000]A volume in space that encloses objects.

Zones do not physically contain objects in the scene.  Rather, any object
that has its world box coincide with the world box of a zone is considered
to be part of that zone.  As such, objects can be in multiple zones at
the same time.[/color]
[color=#0040BF]class[/color] [b]Zone[/b] : [color=#0040BF]public[/color] SceneAmbientSoundObject< [b]ScenePolyhedralZone[/b] >

----------------------------------------------
[color=#008000]A simple zone space that is described by a polyhedron.

By default, if no other polyhedron is assigned to a polyhedral zone, the
polyhedron is initialized from the zone's object box.[/color]
[color=#0040BF]class[/color] [b]ScenePolyhedralZone[/b] : [color=#0040BF]public[/color] ScenePolyhedralObject< [b]SceneSimpleZone[/b] >

----------------------------------------------
[color=#008000]Abstract base class for a zone space that contains only a single zone.

Simple zones are required to be convex.[/color]
[color=#0040BF]class[/color] [b]SceneSimpleZone[/b] : [color=#0040BF]public[/color] [b]SceneZoneSpace[/b]

----------------------------------------------
[color=#008000]Abstract base class for an object that manages zones in a scene.

This class adds the ability to SceneSpace to define and manage zones within the object's
space.  Zones are used to determine visibility in a scene.

Each zone space manages one or more zones in a scene.  All the zones must be within the
AABB of the zone space but within that AABB, the zone space is free to distribute and
manage zones in arbitrary fashion.

For scene traversal, zone spaces are interconnected.  By default, zone spaces get a chance
to connect to each other when being moved into each other's zones.  An exception to this
is the root zone since it is both immobile and without position and (limited) extents.  If
a zone space wants to connect to the root zone, it must do so manually (same goes for
disconnecting).[/color]
[color=#0040BF]class[/color] [b]SceneZoneSpace[/b] : [color=#0040BF]public[/color] [b]SceneSpace[/b]

----------------------------------------------
SceneSpace is class for all game objects.

-------------------------

globus | 2017-01-02 01:05:38 UTC | #6

The extracted files from the Torque 3D described above and additional (that would not download the entire engine) [url]https://yadi.sk/d/SQ9C83YrhQYWU[/url]

And see how it work:
[video]https://youtu.be/zSqMkbDwz28[/video]
[video]https://youtu.be/JXjTF2pndRc[/video]

-------------------------

weitjong | 2017-01-02 01:05:39 UTC | #7

Watch the language, guys.

-------------------------

globus | 2017-01-02 01:05:39 UTC | #8

Exist Occluders (in Urho) - it do part of scene invisible.
There is a desire to make antiOccluders (Portals) - it do part of scene visible.
It serves the same purpose, only for Indoor scenes.
Think this is the natural desire.

Well, i go read the theory and the source code.
Perhaps I do not understand something. :wink:

-------------------------

cadaver | 2017-01-02 01:05:40 UTC | #9

At the moment there is no plan to make a portal based visibility system. Rather, in indoor scenes you should make your walls occluders - if they're simple they should be extremely fast to rasterize for the software occlusion, and provide good hiding of geometry behind, while staying completely dynamic and allowing mixing of indoor / outdoor occlusion.

Also if you have a solid door between corridors which opens - just make it an occluder as well.

-------------------------

