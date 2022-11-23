slapin | 2017-05-17 23:31:00 UTC | #1

Does Urho crowd supports individual agent targets?

-------------------------

Sinoid | 2017-05-18 05:31:53 UTC | #2

Do you mean target *destination* to move to? Yes, the sample just has them all move to the same point both for simplicity and it's easier to see how wrong things can go when a ton of agents pile in on one point.

If you mean different "agent targets" where there are different kinds of agents ... no - that isn't actually difficult to do in DetourCrowd but it's invasive and would not be easy to keep up to date.

-------------------------

TheSHEEEP | 2017-05-18 08:11:36 UTC | #3

Any kind of thing that isn't standard in DetourCrowd is always pretty hard to pull off and requires a good understanding of the underlying mechanics. It can all be done, and IMO there's no real alternative to Recast/DetourCrowd (if you are not working a square/hex grid), but it really is not very flexible, so it always requires quite some coding.

I tried to do different agent sizes once and that was a LOT of work. Basically required having two different pathfinding "worlds", yet keeping them interacting with each other. x.x

If I were you, I would really try to find workarounds if you are not 100% sure that you cannot do something with what is offered out of the box. Even if it means some more CPU/memory usage.

-------------------------

slapin | 2017-05-18 11:11:00 UTC | #4

@Sinoid do you mean that individual target to move to should work?
About diffrent kinds of agents - as I understand I can have multiple crowds
(I don't really know how to set them up yet)  so I could set up some different
macro parameters...

-------------------------

Sinoid | 2017-05-18 23:18:46 UTC | #5

@slapin, yes.

**C++** `void CrowdAgent::SetTargetPosition(const Vector3& position);`
**Angelscript** `myCrowdAgent.targetPosition = targetVec3`

-------------------------

