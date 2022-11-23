Leith | 2019-02-10 02:39:46 UTC | #1

What is the best way to get the (current) bounding box of (animatedmodel) ?

Please see my attached issue.
![wed|690x194](upload://xgGOykADeJEzURlFfUUgZSJD1jT.jpeg)

-------------------------

Modanung | 2019-01-30 16:51:48 UTC | #2

The capsules seem like `CollisionShape`s. Maybe you could draw a debug box to visualize the model's bounding box?
Something like:
```
debugRenderer->AddBoundingBox(animModel->GetBoundingBox(), ...);
```

-------------------------

GodMan | 2019-01-30 17:53:58 UTC | #3

That looks like the character demo. If so then those white capsules are the physics capsules for the character in the demo. Like @Modanung said.

-------------------------

Leith | 2019-01-31 09:56:29 UTC | #4

The capsule, in those samples, does not account for animation, even in the absence of root motion.
I will make a post soon about my improvements to the Character class, and offer some solutions to dealing with these issues.

-------------------------

GodMan | 2019-01-31 19:14:02 UTC | #5

My projects work fine. I have my characters animated, and they do not do this.

-------------------------

Leith | 2019-02-02 03:16:32 UTC | #6

Yes there is something more happening here.
My application creates a scene, saves it, and reloads it... I have hassles with the latest build of Editor on Linux, and I'm too focused on making code work to worry about downloading the old stable version.

Occasionally, it appears that after loading, some booleans are not being set correctly - Despite being serialized to disk!

EDIT:
OK! It seems that our Factory function is not clearing the memory on new objects, and that serialized variables which have default values at the time of serialization are not serialized at all, and not initialized to default values by the factory. This means that if you have a serialized member, with a default value, and don't initialize it yourself, it could have any random value at runtime, and not what you expected, given that you declared it as serialized and gave a default value that was never applied. This seems like something I might elect to remedy with a PR.

-------------------------

Leith | 2019-02-04 03:56:53 UTC | #7

Yeah, something funky going on, other than my animations having root motions
I consider this thread solved, despite having no clear answer, my issue is purely caused by loading a scene, and the factory not setting default values on my serialized members. I would like to see this resolved but I am lazy, and writing about it at least there is some record of the issue and how to resolve it. Should be fixed in the head of the repo.

I know right, I should be responsible for initializing my own data - but if I went to the trouble of registering my data as serialized class members, I would expect that the defaults I provided would be applied by the factory. Does that sound like a reasonable suggestion?

-------------------------

Leith | 2019-02-06 08:53:33 UTC | #8

This case is solved - when deserializing, the Urho3D factory will not automatically apply any default values you defined as serializable, unless you changed the value from what you declared as default prior to serializing - we end up with a situation that is unsafe unless you (eg in constructor) manually apply the same values you already declared to be defaults - you're expected to initialize your values as WELL as define the default values that will never be applied during deserialization but only used to filter some data during serialization - I would like to hear some talk about this because really, it's pretty cheap to fix this.

-------------------------

