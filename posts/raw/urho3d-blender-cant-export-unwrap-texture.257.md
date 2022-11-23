umen | 2017-01-02 00:59:11 UTC | #1

Hey 
i opened issue in the Urho3D-Blender git repo , but here i guess there is more traffic 
so if someone tale a look at the issue and see if you know what im missing here 
basically i have unwrapped UV texture that is not exported with the script 
please take a look at this issue :
[url]https://github.com/reattiva/Urho3D-Blender/issues/18[/url]
thanks !

-------------------------

friesencr | 2017-01-02 00:59:11 UTC | #2

I would check to make sure the material is assigned the texture.  Blender is kind of tricksey that way.  You can be viewing the model in textured mode and have the uv apply the texture to viewport but not actually be assigned to the material.

-------------------------

umen | 2017-01-02 00:59:12 UTC | #3

Thanks for the answer , you are right there is part that i was missing , according to this tutorial :
[url]http://www.katsbits.com/tutorials/blender/learning-materials-textures-images.php[/url]
i did "Adding a Texture stage to a Material" from the tutorial .
you can see the image attached here :
[url]http://imgur.com/h1q7p87[/url]

then when i exported again with the script . 
still nothing ...  the material is not exported , what do i miss here ?
here is the exporter image :
[url]http://imgur.com/OvKtb7U[/url]

-------------------------

szamq | 2017-01-02 00:59:12 UTC | #4

And what the exporter log says? (small icon near to export button)

-------------------------

Mike | 2017-01-02 00:59:12 UTC | #5

And can you show the Material tab in edit mode.

-------------------------

umen | 2017-01-02 00:59:12 UTC | #6

Thanks for your quick answers the problem was fix , the reson is i didn't set the mapping type to uv map 
you can see the solution in the issue of the bug in git .

-------------------------

