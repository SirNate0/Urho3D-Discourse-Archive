Hevedy | 2017-01-02 00:57:37 UTC | #1

Hi.
Im making a 3d model and dont find to apply textures for double side in the model and with texture for alpha channel.
What need make, change or add for this ? (In the material files... ?)

[img]https://dl.dropboxusercontent.com/u/28070491/URho3D/DoubleSided.png[/img]

Thanks.

-------------------------

Hevedy | 2017-01-02 00:57:38 UTC | #2

Alpha added in the diffuse texture:

[img]https://dl.dropboxusercontent.com/u/28070491/URho3D/AlphaAdded.png[/img]

But now need the double side...

-------------------------

Mike | 2017-01-02 00:57:38 UTC | #3

Did you check [url]http://discourse.urho3d.io/t/double-side-rendering-using-materials-list/44/1[/url] or is it something else you want to achieve?

-------------------------

Hevedy | 2017-01-02 00:57:38 UTC | #4

[quote="Mike"]Did you check [url]http://discourse.urho3d.io/t/double-side-rendering-using-materials-list/44/1[/url] or is it something else you want to achieve?[/quote]

Impossible to see this in the editor?

-------------------------

Mike | 2017-01-02 00:57:38 UTC | #5

It is already in the editor:
- open the Material editor by clicking "Edit" in Material inspector > Material.
- then modify Cull mode (at the botom)from CCW (default) to None.

-------------------------

Hevedy | 2017-01-02 00:57:38 UTC | #6

[quote="Mike"]It is already in the editor:
- open the Material editor by clicking "Edit" in Material inspector > Material.
- then modify Cull mode (at the botom)from CCW (default) to None.[/quote]

O wow no see that  :confused: 
Sorry thanks.

Ty.

-------------------------

