sabotage3d | 2017-01-02 01:11:42 UTC | #1

I am getting weird behaviour with transparency in Urho3d. If I use NoTextureAlpha or DiffAlpha techniques and set the MatDiffColor's alpha to 1, I can see through jack's model. With DiffAlpha with no texture assigned, it picked some textures from other assets in the scene and started switching to textured and non-textured when I was moving the camera around the object. I am using Urho3D 1.5 under OSX.

-------------------------

cadaver | 2017-01-02 01:11:42 UTC | #2

Traditional alpha materials leave depth write off, which leads to issues when alpha materials with multiple overlapping parts like Jack's hands / body are drawn. You could enable depth write, with the risk of some other artifacts. In general: transparent rendering with GPUs is hard to do right, since it's a hack, and we can't reasonably sort per triangle.

Material's texture definitions are held in a map. At render time the map is iterated and textures from the material are set to texture units. A missing texture means the texture from whatever previous draw call is used (there is no "null texture" used as default.) If you don't want that to happen, don't use texture-requiring techniques like DiffAlpha with no texture assigned.

-------------------------

sabotage3d | 2017-01-02 01:11:42 UTC | #3

Thanks cadaver. Where do I have to set depth write off? With NoTextureAlpha and alpha 1.0 shouldn't we just completely ignore any transparency? I might be completely wrong but can't we just lerp from no-transparency to full transparency? I am trying to linearly fade a character.

-------------------------

cadaver | 2017-01-02 01:11:42 UTC | #4

Depth write is controlled by the technique, so you'd just remove depthwrite="false" from your copy of the DiffAlpha technique.

Unfortunately opaques and transparencys need to go to different render passes, and since we have the data-driven Renderpath system in Urho (which can have arbitrary pass setups) the engine cannot automatically guess into which pass the draw should go just depending on the alpha value. This means that you need a different material / different technique for fully opaque case and for the fading case, or alternatively you need custom logic to change the material's technique on the fly.

Some other engines no doubt have material systems that just automatically "do the right thing" but as a consequence they're bound to be less flexible.

-------------------------

sabotage3d | 2017-01-02 01:11:43 UTC | #5

Removing the depthwrite works really well. Are there any drawbacks?

-------------------------

cadaver | 2017-01-02 01:11:43 UTC | #6

Transparencies are rendered back to front, so there may be issues when your character is intersecting other transparent geometry like smoke clouds, and the sorting (which is per object) doesn't go exactly right.

-------------------------

sabotage3d | 2017-01-02 01:11:43 UTC | #7

Thanks cadaver. It it working excellent in my case.

-------------------------

