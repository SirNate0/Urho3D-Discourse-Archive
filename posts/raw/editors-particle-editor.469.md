Bluemoon | 2017-01-02 01:00:41 UTC | #1

Its unfortunate that I just realised that there has been a change in the way particles emitter was handled in Urho3d editor. I have the official Urho3d release build and also a snapshot build of some couple of weeks back. I realised that in the release build it had a fairly decent function to create particle emitters but in the other build it makes use of a definition file. I would like to know why the change was carried out so as to update my brain's logic :slight_smile:...

-------------------------

weitjong | 2017-01-02 01:00:42 UTC | #2

Read this [github.com/urho3d/Urho3D/issues/258](https://github.com/urho3d/Urho3D/issues/258).

-------------------------

cadaver | 2017-01-02 01:00:42 UTC | #3

Sometimes refactoring to a cleaner system unfortunately removes functionality. ParticleEmitter attributes, though good for editing, were not nice overall because of ambiguity (is the "true" state in the particle resource or in the attributes?) and network replication effectiveness. Much shorter to transfer just the particle resource name instead. To regain the old functionality would need making an editor window similar to the Material editor.

-------------------------

Bluemoon | 2017-01-02 01:00:42 UTC | #4

[quote="weitjong"]Read this [github.com/urho3d/Urho3D/issues/258](https://github.com/urho3d/Urho3D/issues/258).[/quote]

Just what I was looking for.

@cadaver I guess the reason for the change is clearer now :slight_smile:

-------------------------

