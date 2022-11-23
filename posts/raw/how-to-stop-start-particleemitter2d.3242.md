ricab | 2017-06-12 20:45:05 UTC | #1

What is the proper way to enable/disable the emitter? 

My question is pretty much the same as [this](https://discourse.urho3d.io/t/any-way-to-stop-particleemitter2d/2728), which did not have a conclusion. Was something like `void SetEmitting(bool enable)` ever planned for 2d particles? Thanks

-------------------------

kostik1337 | 2017-06-13 07:45:03 UTC | #2

I implemented this by myself in my local repository. Implementation is pretty simple - check out this patch
https://gist.github.com/kostik1337/d50faf715489face99cd233760ca7dae

-------------------------

Modanung | 2017-06-13 11:08:45 UTC | #3

[quote="kostik1337, post:2, topic:3242"]
I implemented this by myself in my local repository.
[/quote]

Would make a great pull-request.

-------------------------

ricab | 2017-06-13 15:55:06 UTC | #4

Indeed, it works for me and the code looks good. It would be nice to get this in. Thanks a lot.

-------------------------

kostik1337 | 2017-06-14 06:50:16 UTC | #5

OK, I think, it requires some more changes to be in engine (angelscript/lua bindings). I'll prepare pull request in the near future.

-------------------------

Modanung | 2017-08-25 21:32:25 UTC | #6

https://github.com/urho3d/Urho3D/pull/1987

-------------------------

