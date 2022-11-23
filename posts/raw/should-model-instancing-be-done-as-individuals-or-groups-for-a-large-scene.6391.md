evolgames | 2020-09-15 05:34:44 UTC | #1

So I get that there is the [resource cache](https://discourse.urho3d.io/t/managing-large-scenes/1346/8) of .mdl data which batch processes models.
The application here is a low poly city scene with several types of buildings (some scaled or with different materials). Nothing too crazy.
I'm trying to plan this out before I go down the wrong path. Not using the editor, just scripting. I'm making some simple models in blender. I figure I have the following options:

1. Model each "piece" of my city (i.e. road, building 1, building 2, lamp, car, etc) and use a tile system to place the main static pieces in game, with some randomness perhaps. Maybe using nested tables to create a city grid and all that.
2. Model groups of objects. For example I load premade complete city blocks or areas as .mdl. I piece *those* blocks together in a larger grid to make the city.
3. Model a large blender scene of the whole city (or big parts of it) and import that as one huge mesh.
4. Something else.

So what's the smartest way to do this? What's the performance impact between one large object (city block) vs. individual ones (singular objects), assuming the former is just the sum of the parts? Both cases would have multiple instances, but the premade blocks would be repeated less for sure... Or is there much a difference? I know Urho handles many objects very well, but does it do better with fewer large objects vs. much more smaller ones amounting to the same amount of polygons overall?

-------------------------

Modanung | 2020-09-15 08:17:45 UTC | #2

I use `StaticModelGroup`s in cases like these.

-------------------------

evolgames | 2020-09-15 14:17:29 UTC | #3

Oh okay, so I could easily group like models. That'd be easy.
So you think I should stick to individual building models with static groups rather than a large city block as an .mdl file?

-------------------------

Modanung | 2020-09-15 15:43:18 UTC | #4

Well, I'm no performance artist... but that's how sample 20 demonstrates handling large object counts.

I've been wanting to edit normals in Blender [about half my life](https://blenderartists.org/t/editing-normals/368427), for this exact purpose. You may be interested in [TiNA](https://blenderartists.org/t/tina-transfer-normals-add-on/1124593) and [Edddy](https://discourse.urho3d.io/t/edddy-a-block-based-map-editor/2486). The first is a Blender add-on to alleviate control of normals, the second is a map editor intended to function something like a 3D [Tiled](https://www.mapeditor.org/). Part of my plans for Edddy is adding "local" grid support. Until then it may already help in assembling (parts of) buildings... or entire levels if all their blocks reside on the same square prism grid.

-------------------------

Modanung | 2020-09-15 15:38:12 UTC | #5

For the _best_ performance you may even want to merge co-planar surfaces, either programmatically or by stretching blocks with sticky UVs. Anything that makes sense as a generalization could be built into Edddy, its EMP map format and `BlockMap` component.

-------------------------

evolgames | 2020-09-15 19:05:12 UTC | #6

Oh wow Edddy looks very useful in this situation! I see a demo of a little town, too. I will definitely be checking this out. I guess I'll experiment between block sizes and see what works best for this situation.

-------------------------

Modanung | 2020-09-15 19:15:49 UTC | #7

Cool, glad you like it.

I wouldn't exactly call it "production ready", but it *has* been used to create levels for [A-Mazing Urho](https://gitlab.com/luckeyproductions/AmazingUrho). Basic layer support was added in the meantime.

Since it's all in relatively early development and nothing is set in stone, your experimentation is not unlikely to provide valuable guidance.

-------------------------

evolgames | 2020-09-15 19:28:22 UTC | #8

No worries, I probably won't require too much. I'll be sure to provide some feedback on my experience with it. Just need to make some more blender models first ;)

-------------------------

QBkGames | 2020-09-16 01:44:48 UTC | #9

Also depends how much of the city do you see most of the time.

If it's a flying simulator and you see most of the city (from high above) almost all the time, you are better off making the city one big model, to reduce draw calls (especially since it's a low poly asset). 

If it's a FPS and you are inside the city and you only see a small number of buildings most of the time, then separating the city into individual blocks may make more sense as most of it is culled by the camera view.

-------------------------

evolgames | 2020-09-16 02:15:33 UTC | #10

Oh that's a good point. This is for an fps game so I guess I'll go with the latter in this case.

-------------------------

