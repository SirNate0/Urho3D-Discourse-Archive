Lumak | 2017-01-02 01:12:44 UTC | #1

In my terrain editor, I have a call to:
        m_pTexture2DSource->SetData( 0, 0, 0, GetWidth(), GetHeight(), GetData() );
which worked fine in 1.4, but doesn't do a thing in 1.5.  Stepped through the function and there are no error exit but still doesn't refresh the texture.

Do I have to do anything more than what was done in 1.4?  This problem happens on d3d9 and gl.

-------------------------

Lumak | 2017-01-02 01:12:44 UTC | #2

I think this is related to Nvidia's driver update. I ran my 1.4 that I built and has the same problem.  Then I ran the editor that was built back on May 18 and it works fine. 

There was an nvidia update just last week and it may be related. 
I wish I knew exactly what.  If anyone know anything about this, please let me know. thx.

-------------------------

TheComet | 2017-01-02 01:12:44 UTC | #3

I suspect you have gawag (and potentially myself) to thank for that!  :unamused: 

[url]http://discourse.urho3d.io/t/sharedptr-potential-pitfall-that-can-be-easily-fixed/1954/18[/url]

[quote="cadaver"]Texturexxx::SetData() has been changed in master branch to use just a raw pointer. It will now rather manage the created MIP images internally by a different shared pointer.[/quote]

Could this be related?

-------------------------

Lumak | 2017-01-02 01:12:45 UTC | #4

Thank you for pointing that out, but that wasn't it. It was my own doing. When the height map and the color map are different sizes, the area of color map that gets updated is offset and are not where you're painting.  I was testing optimization to see how small the vertex count on the terrain could be and still look good and the physics would still behave properly.  I forgot I made several heightmaps but never changed the color map. :unamused:

-------------------------

