Lumak | 2017-01-02 01:15:10 UTC | #1

I saw a Urho3D video on youtube some months ago demonstrating replicated grass in the scene.  I don't know how many grass nodes were placed in the scene, but I clearly remember the low frame rate at around 20 - 35 fps.

I wanted to test this and test to see if some optimization can be made for sometime now and got a chance to today.
Rendering 10k grass nodes created individually using staticModel, the frame rate sat around 67 fps.

Repo: [url]https://github.com/Lumak/Urho3D-Geom-Replication/[/url]

Replication w/ normals overriden:
[img]http://i.imgur.com/7Aes0LJ.jpg[/img]

Added wind animation:
[img]http://i.imgur.com/nKJHVKP.jpg[/img]

Edit: added another screenshot

-------------------------

Lumak | 2017-01-02 01:15:10 UTC | #2

Just curious if I had 50k replicated grass:

replicated w/ normals overriden:
[img]http://i.imgur.com/OSz00ye.jpg[/img]

FPS is still decent.  Note: you'll want to make these replicated models in small patches, and not like the 50k example shown  :wink:

-------------------------

rasteron | 2017-01-02 01:15:10 UTC | #3

great stuff Lumak! I think this should be added to the examples. :slight_smile:

-------------------------

NiteLordz | 2017-01-02 01:15:11 UTC | #4

Agree, this should become a sample, i have been looking for a solid vegetation sample, and this could definitely help out ( or integrate into the Terrain sample even )

-------------------------

Lumak | 2017-01-02 01:15:11 UTC | #5

I'll try to push a PR for this. I think a Replicate() function in the StaticModel would be ideal.

-------------------------

Lumak | 2017-01-02 01:15:12 UTC | #6

Added simple wind velocity animation.

-------------------------

Lumak | 2017-01-02 01:15:12 UTC | #7

Added an option to override geom normals.

-------------------------

coldev | 2017-01-02 01:15:12 UTC | #8

Thanks 4 share..

God Bless You

-------------------------

Lumak | 2017-01-02 01:15:13 UTC | #9

10k grass animated:
[img]http://i.imgur.com/nKJHVKP.jpg[/img]

-------------------------

