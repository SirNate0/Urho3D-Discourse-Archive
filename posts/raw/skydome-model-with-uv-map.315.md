rasteron | 2017-01-02 00:59:34 UTC | #1

As an alternative to skyboxes:

[img]http://i.imgur.com/lmUDOwv.jpg[/img]

Model is already UV Mapped,  just create or duplicate the skybox material and add your own sky/background textures.

Just added this resource and created a pull request..

cheers.

-------------------------

horvatha4 | 2017-01-02 01:11:41 UTC | #2

Hi rasteron, hi Forum!
Just for info, what about this project?
Your code is reachable somewhere or not?
I found this one too: [url]http://discourse.urho3d.io/t/solved-projectionmatrix-and-modelviewmatrix-glsl/1690/1[/url]
It is the same code or not?  :slight_smile: 

Arpi

-------------------------

rasteron | 2017-01-02 01:11:54 UTC | #3

Hi horvatha4,

Yes, that's a recent post and the shader part of the Skydome entity, so it will act more like your typical Skybox and make it virtually unreachable.

You can setup this Skydome model and material/shaders which are all already included in the latest Urho3D repo. Just look for Skydome under Source Assets, Materials, Shaders, Postprocess and Models folder. You just need to use your own texture, manage it via the editor and you're good to go. :slight_smile:

-------------------------

