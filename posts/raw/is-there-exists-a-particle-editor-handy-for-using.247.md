hualin | 2017-01-02 00:59:07 UTC | #1

Hi,
I am using unity for editor because the official editor is not perfect for artists and designers use, but its particle system is too complex to export to urho3d.
Is there exists another particle editor for using? 

Thank you.

-------------------------

cadaver | 2017-01-02 00:59:08 UTC | #2

Considering that the 3D particle effects use a custom XML format, I doubt that there exist external editors for it. Using the built-in Urho editor, you can edit a ParticleEmitter's attributes and either save the scene node with the particle effect as a node prefab (Save Node from the File menu) or save/load the XML particle data (bottom of Edit menu)

The 2D particle effects, which were added later, use the .pex file format as used by the Starling / Sparrow frameworks.

-------------------------

hualin | 2017-01-02 00:59:08 UTC | #3

I see now. 
And I export the particle data from unity, I will test the way would work or not. It's paid me a lot of time to do this.
And if this way can't work, I will let the designer and artist using the official Editor.

Thank you , cadaver.

-------------------------

