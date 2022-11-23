slapin | 2017-03-18 21:20:07 UTC | #1

Hi, all!
How do you sort Array<Vector2> by Atan2 value of coordinates?
Only way I found is to create ad-hoc class which overrides cmp operation, but it looks like really overkill...

-------------------------

Eugene | 2017-03-19 07:26:03 UTC | #2

There is Urho3D.Sort with predicate, why no?

-------------------------

slapin | 2017-03-19 14:32:36 UTC | #3

The predicate part is not exported to AngelScript, which makes using it quite a challenge... :(

-------------------------

