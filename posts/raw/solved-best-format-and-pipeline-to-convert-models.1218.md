rasteron | 2017-01-02 01:06:09 UTC | #1

Hi all,

I was wondering if anyone has a tip on getting a good export with models, static or animated as I am having recent problems with the quality, particularly when applying [b]normal maps[/b]. 

I'm currently using the commandline [b]AssimpImporter[/b] with the [b][u]tangent flags set[/u][/b] and still see some polygon edges. I've tried converting my models on other engines and it looks ok.

I've tried this:

- MS3D Format 
- Convert the model with tangent flags in importer
- Used DiffNormal or DiffNormalSpec 
- both DirectX/OpenGL version

Thanks!

[b]** No problems with FBX 2013 **[/b]

-------------------------

rasteron | 2017-01-02 01:06:09 UTC | #2

It's more like the tangents were not applied or producing a hard normal effect so there are uv edges, shaded sides or corners..

[img]http://i.imgur.com/QIpLq21.png[/img]

-------------------------

rasteron | 2017-01-02 01:06:10 UTC | #3

Yes, thanks for that. I think I am missing a step or something unless there's a good benchmark example model or process that I can check out and compare. I suspect that good anti-aliasing technique like Nvidia's built-in feature can improve and hide those seams but I am more concerned with the shaded areas with normal mapping. The seams does not show up though with Diffuse only technique so that adds to the weirdness.  :unamused:

-------------------------

rasteron | 2017-01-02 01:06:12 UTC | #4

Thanks again for the help Sinoid. Going through the formats, it looks like FBX 2013 is the way to go. The normals are now showing up properly :slight_smile:

-------------------------

