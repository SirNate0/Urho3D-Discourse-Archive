alexhawk | 2017-09-21 12:58:56 UTC | #1

It looks that urho3d is what I`m really waiting for. (Finnish quality)
But I have some questions:
1. I want to animate pivot of walking character. Can I do it? When my walking character stays on the left leg he must turn around left leg, and when he stays on the right one he must turn around right leg. I try to make in blender sometimesh ago, but how I can understand most of ways to make it were closed.
2. There was question from somebody about mipmapping with turned off filtration, I cannot clearly understand all. Can I use nearest filtration with linear mipmapping?
3. Can I make combined by stencil mask texture maps?

-------------------------

jmiller | 2017-09-26 16:17:25 UTC | #2

1.
One way, assuming model node as child of pivot...
Backup model world position: pivot->GetChild()->GetWorldPosition()
move pivot
Restore world model position: pivot->GetChild()->SetWorldPosition()

2.  Perhaps: ```renderer->SetTextureFilterMode(FILTER_NEAREST_ANISOTROPIC);```

3. I find a number of posts about using the stencil; maybe [url=https://discourse.urho3d.io/search?q=stencil]some[/url] will be useful?

HTH

-------------------------

