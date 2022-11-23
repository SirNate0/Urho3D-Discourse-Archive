vivienneanthony | 2017-01-02 01:12:55 UTC | #1

Hey,

How doable is it to do something like:

[youtube.com/watch?v=dZvsazWNOq4](https://www.youtube.com/watch?v=dZvsazWNOq4)
[youtube.com/watch?v=Ovfhv_9-KIg](https://www.youtube.com/watch?v=Ovfhv_9-KIg)


Im assuming first you need a galaxy procedural system that regions can be selected to finite levels of a planet, second a translaton of xyz to eucledrian system, then a procedural system for the planets.

So scene would be current world or scene view.

Vivienne

-------------------------

Enhex | 2017-01-02 01:12:56 UTC | #2

You have to deal with these problems:

1. Content. Would most likely require procedural generation to be feasible.

2. Level of Detail features. This will be more than the model-level LOD (which Urho provides you with).

3. Floating point precision. 

4. Relative gravity, easy one. Bullet natively support gravity from a single direction (AFAIK), you'll have to manually apply gravitational force of nearby planets.

All problems are above the engine level.

This is a big project, I'd recommend you to start with a project that only require a subset of these features so you can incrementally build up your features.

-------------------------

namic | 2017-01-02 01:12:57 UTC | #3

Looks like a Unigine tech demo, btw: [unigine.com/](http://unigine.com/)

-------------------------

codingmonkey | 2017-01-02 01:13:01 UTC | #4

hi, the second video it's Neptune's engine also known as Space engine. there is his topic on gamedev.ru 
[gamedev.ru/projects/forum/?id=122716](http://www.gamedev.ru/projects/forum/?id=122716)

-------------------------

