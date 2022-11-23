Enhex | 2017-01-02 01:09:04 UTC | #1

Is there a way to have a parent node with a body, and a child node with a body, without having the child body parented to the parent body?

I need this behavior so I could have a character controller which uses cast "leg", which means it's body hovers over the ground, and an interaction body that spans all the way down to the ground for proper interactions.
I want the child node to follow the parent node, the body shouldn't be controlling it's position and shouldn't be parented to the parent body, so it doesn't become static.
If it's static, static-inactive collisions aren't reported and that means pickups don't report collision, thus can't be picked up.

It might be possible to have a parent node with 2 child nodes, one for the controller body and one for the interaction body, and then manually set the position of the parent node to the position of the controller node. But in the end all it does is simulate having a not-parented child body, so why not let the user enable the intended behavior?

Should I use a constraint instead?

EDIT:
Using constraint worked.

-------------------------

miz | 2017-01-02 01:09:07 UTC | #2

Could you not get the behaviour you wanted with making them as separate nodes (i.e. non parent child relationship) and then program one to track the other how ever you want?

-------------------------

Enhex | 2017-01-02 01:09:07 UTC | #3

[quote="miz"]Could you not get the behaviour you wanted with making them as separate nodes (i.e. non parent child relationship) and then program one to track the other how ever you want?[/quote]
Like I said that's possible but it's basically the same as creating a child node without parenting the child body. Though then there'll be a problem with the child body position, since it would need to more relative to the other body.
So a possible solution is to used fixed constraint to make sure the interaction body follows the controller body when they are in separate nodes.

Here's a nice video demonstrating constraints in Bullet:
[video]https://www.youtube.com/watch?v=9MveTfRNWEU[/video]

-------------------------

