GodMan | 2020-03-15 19:43:12 UTC | #1

So I have this, but it does not work. I see under bone you can get the initial scale. 

    handBoneNodeAI = zombie1->GetChild("r hand", true);
    handBoneNodeAI->SetScale(Vector3(0.05f,0.05f,0.05f));

This won't work though.

-------------------------

Dave82 | 2020-03-15 21:37:10 UTC | #2

You can't transform bones in a scene update process because it will be overridden in the skinning update.
Subscribe to the post render update and scale your bone there.

-------------------------

GodMan | 2020-03-15 19:55:34 UTC | #3

Okay that sounds to be the issue. Thanks

-------------------------

GodMan | 2020-03-15 21:37:04 UTC | #4

My mistake I had issue with my event.

Thanks for the help

-------------------------

