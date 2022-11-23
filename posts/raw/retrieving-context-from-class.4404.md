nergal | 2018-07-23 17:40:16 UTC | #1

Is there a way to retrieve a pointer to the context from a class that's not a LogicComponent or Application subclass?

I'm trying to make some classes generic without tight coupling to Urho3D. So I got my World, Chunk and ChunkModel classes. My World has many Chunks that has one ChunkModel. Both World and Chunk are "generic" and no 3D context is needed. But I don't want to pass the context pointer through World and chunk just to get it in my ChunkModel class that actually requires it.

I would like to do something as GetSubsystem<Game>->context_ from my ChunkModel class. Any ideas or pointers(pun intended)?

-------------------------

Eugene | 2018-07-23 21:13:35 UTC | #2

Literally any `Object` has `GetContext` method.
I can't imagine that you're unable to find any.

Well, if you have _really_ separate hierarchy totally unrelated to Urho, then either push Context with somebody or make it global.

-------------------------

nergal | 2018-07-24 11:16:29 UTC | #3

Seems like the only way for me would be to pass the argument through my World class, down to the Chunk class and then to the ChunkModel class in order to get the context. Without creating some global variable for it.

Currently I don't have any Urho3D objects in these classes to fetch context from.

-------------------------

Eugene | 2018-07-24 11:29:51 UTC | #4

Why not to make `Context` global? Urho implements logging this way.

-------------------------

nergal | 2018-07-24 11:29:46 UTC | #5

Ah I see. I'll use a global for the context. I guess that's the easiest way to get around my design-problem :slight_smile:
Thanks for your help!

-------------------------

