slapin | 2017-05-22 13:37:27 UTC | #1

Hi, all!

I created CrowdManager and Agent.
Now I want several agents as parts of different crowd.
More than that, I want them to migrate from one crowd ot another from time to time.
How to do this?
I know DetourCrowd can do this, but how to do this in Urho?

Also, I have various surfaces I want agents to avoid, but walk on last resort (if no other path available).
Like roads and sidewalks. How could I make so that crowd paths are preferred to be on sidewalk?

Thanks!

-------------------------

Sinoid | 2017-05-22 19:22:48 UTC | #2

[quote="slapin, post:1, topic:3142"]
Now I want several agents as parts of different crowd.
[/quote]

Although I recall someone fiddling with multiple crowd support it was never merged. The CrowdAgent asks the scene for a `CrowdManager` (to create or return). You'll have to settle on some sort of scene structure and seek upward to find the `CrowdManager` component you want to use during `CrowdAgent::OnSceneSet`.

[quote="slapin, post:1, topic:3142"]
More than that, I want them to migrate from one crowd ot another from time to time.
[/quote]

That is dependent on how you implement the above. I have no idea as to what the consequences are. I never looked at whoever's code that was that gave this a whirl.

[quote="slapin, post:1, topic:3142"]
Also, I have various surfaces I want agents to avoid, but walk on last resort (if no other path available).
Like roads and sidewalks. How could I make so that crowd paths are preferred to be on sidewalk?
[/quote]

You have to use NavAreas for that. Costs are assigned/read through the SetAreaCost/GetAreaCost methods. Beware though that these work with dtQueryFilter, and the filter used for the `NavigationMesh` is not the same as the one used for the `CrowdManager`.

---

In general, when exploring the Detour code NavAreas are the place to begin tracing through as they're simple to understand and run through most of the really important areas of Detour.

-------------------------

slapin | 2017-05-22 23:07:59 UTC | #3

Hi, all!

BTW, is it possible to use CrowdNavigation for traffic simulation instead of crowds?
Would be interesting to try...

-------------------------

slapin | 2017-05-23 00:22:02 UTC | #4

btw, do NavAreas work, is there some demo somewhere?
Also can I assign costs per agent?

-------------------------

Sinoid | 2017-05-23 03:59:26 UTC | #5

> btw, do NavAreas work, is there some demo somewhere?

Unless they've been broken they should work. You have to place them and then build the navmesh. So if they don't work be sure to say something.

> Also can I assign costs per agent?

Sort of, you really wouldn't want to do it per-agent (more like per-many agents - there's a cap on how many filters), but the `CrowdAgent::SetQueryFilterType` and  everything in `CrowdManager` containing the text "queryfilter" deal with that, including exclusion from area-types.

-------------------------

