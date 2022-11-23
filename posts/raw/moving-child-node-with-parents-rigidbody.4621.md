mrchrissross | 2018-10-27 13:00:34 UTC | #1

Hi,

I'm trying to move my spaceship. My spaceship has two parts: The body, and the hood.

I've made the hood a child of the body node. However when I move the body rigidbody, the child does not move with it.

I know that if I move the body node using translate, that moves the child but that sacrifices collision detection.

Any help would be brilliant :slight_smile:

-------------------------

mrchrissross | 2018-10-27 13:00:28 UTC | #2

Solved my own question. It seems you need to remove the rigidbody from the child.

-------------------------

jmiller | 2018-10-27 14:58:15 UTC | #3

Hi mrchrissross,

You also have the option of constraints, which work much better in Urho than in reality. :)

  https://urho3d.github.io/documentation/HEAD/_physics.html
  ref: Samples 19_VehicleDemo

-------------------------

mrchrissross | 2018-10-27 15:09:06 UTC | #4

Thanks a lot mate :slight_smile:

-------------------------

