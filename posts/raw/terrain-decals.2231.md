Dal | 2017-01-02 01:14:05 UTC | #1

I'm struggling a bit with applying decals to the terrain... I can only seem to apply them to a single patch at a time and then they don't affect other patches. Am I missing something, is there a better way to do it?

-------------------------

cadaver | 2017-01-02 01:14:05 UTC | #2

Each patch is an actual Drawable, so if you're following the 08_Decals example, you'd add a DecalRenderer component to each patch node when you first need to create a decal to the patch in question. Since decals are clipped to the individual patch geometry, on the edges you would have to add the decal to several DecalRenderers.

-------------------------

Dal | 2017-01-02 01:14:05 UTC | #3

OK. Thanks, I'll give it a go.
A feature suggestion could be a TerrainDecal that is applied to a terrain rather than a drawable, and does that working out of which patches to apply on internally :smiley:

-------------------------

Dal | 2017-01-02 01:14:05 UTC | #4

Actually, I think it's not as simple as just applying to more than one patch when it is at the border... because when only a small part of the image overlaps the other patch, the centre of the image needs to be in the OTHER patch, so we'd need some pretty complex chopping up of images and drawing it to the correct side/corner of the decal texture in order to draw it properly :frowning:
I think definitely it would be much better if the engine allowed a decal to be applied to the terrain as a whole and took care of which parts should appear on which drawable.

I guess for my purposes it will be easier to just draw some geometry and snap the vertices to the terrain height for now.

-------------------------

cadaver | 2017-01-02 01:14:05 UTC | #5

I believe you should be able to "shoot" the same decal frustum to all terrain patches intersecting your decal and the DecalSet should take care of applying the proper clipping and UV's. Terrain itself is not a Drawable and it has no special knowledge of DecalSet at the moment, so to support this automatically would need special-case code. What would complicate this is that DecalSet has quite a few parameters (like max. vertices and indices) and these don't have obvious "right" values, which the Terrain could assign.

-------------------------

Dal | 2017-01-02 01:14:06 UTC | #6

How would that be done? The only way I know to use it is to pass the position to the constructor, but since the position is outside the bounds it doesn't draw anything...

-------------------------

cadaver | 2017-01-02 01:14:06 UTC | #7

Using DecalSet::AddDecal(), it should create a frustum of the decal for clipping calculations.

-------------------------

Dal | 2017-01-02 01:14:07 UTC | #8

Sorry if I am being dumb, but I don't get what you mean... AddDecal only returns a boolean and I don't see how I can get a handle on the decal itself or the frustum.  I tried creating a DecalSet on all the neighbours and calling AddDecal on them, but nothing gets drawn on the others (presumably because my worldPosition I am passing is not inside the other patches).

EDIT: Ah ignore me, I was just doing something wrong, it does seem to work now :slight_smile:

-------------------------

