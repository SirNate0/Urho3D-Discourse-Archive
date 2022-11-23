SeeSoftware | 2017-11-14 21:00:05 UTC | #1

Looking at the documentation i dont really see an obvious difference. 
Is there a performance difference between those 2?

-------------------------

jmiller | 2017-11-14 21:01:29 UTC | #2

Yes. From https://urho3d.github.io/documentation/HEAD/_containers.html
"PODVector is only to be used when the elements of the vector need no construction or destruction and can be moved with a block memory copy."

PODVector ("Plain Old Data" vector) is more performant than Vector and is unsafe for self-insertion.
There may be other notes in the class APIs or mentions on the forum.

[url=https://github.com/urho3d/Urho3D/search?q=PODVector]Uses of PODVector in the repo[/url]

HTH

-------------------------

SeeSoftware | 2017-11-14 21:18:01 UTC | #3

thanks for the help!

-------------------------

