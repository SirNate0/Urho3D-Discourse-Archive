ArXen42 | 2017-07-13 14:44:10 UTC | #1

If I understand correctly, the only way to get my component visible in the editor is to follow this workflow:

1. Create standard component with appropriate RegisterObject() method inside my project.
2. Symlink or copy that component to somewhere inside the engine code.
3. Call RegisterObject() of that copied component from somewhere in the engine initialization code (or anything that invoked when starting Urho3DPlayer, may be Player's cpp file).
4. Compile that new version of the engine with my components built in. The Editor should see them now.
5. Do some work in the editor, save the scene to my project files and compile project using unmodified version of Urho.

According to this workflow I need two engine versions:

* Clear Urho3D build version used to compile my project.
* Modified Urho3D version with all my code embedded into it.

Is that the right way?

Alternatively, I can fork Urho3D and use the whole engine as the base for my project (and place my code directory along with Tools, Samples, etc). I'm not very familliar with C++ build systems and development process, will that way cause problems? Seems like overkill and a bit dirty way, I'm not sure if it is better.

-------------------------

Eugene | 2017-07-13 15:45:47 UTC | #2

You don't need to touch engine code, you just need to use your own player.

-------------------------

ArXen42 | 2017-07-13 15:50:30 UTC | #3

So I need to insert my registration code inside Urho3DPlayer::Start and compile it and that would be normal practice?

-------------------------

Eugene | 2017-07-13 16:13:25 UTC | #4

Yes.
You will get problems with Lua binding integration, but usually people don't bother about it.

-------------------------

ArXen42 | 2017-07-13 16:18:33 UTC | #5

Ok, thanks for making it clear for me.

-------------------------

