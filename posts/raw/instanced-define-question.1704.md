theak472009 | 2017-01-02 01:09:36 UTC | #1

Hello!
I was able to add dx11 geometry shaders to urho but I am not able to do instancing correctly. Where exactly is the "INSTANCED" define set. I could never find a place where it is set.
Is it an hlsl built in define?

Thanks

-------------------------

theak472009 | 2017-01-02 01:09:36 UTC | #2

Nevermind, found it in Renderer.cpp.

-------------------------

franck22000 | 2017-01-02 01:09:36 UTC | #3

Oh nice :slight_smile: I have tried to add it myself but i was not able to sort every bugs that i had...

Will you make a pull request in github for this ? :slight_smile:

-------------------------

theak472009 | 2017-01-02 01:09:42 UTC | #4

I have some issues like how to handle culling of objects with geometry shader.
For instance, the bounding box of a model has no idea of the real bounding box after applying some offset in the geometry shader. Hence, this will result in culling of the object even if it is visible.
It will be really cool if someone could offer some help with this issue.

-------------------------

