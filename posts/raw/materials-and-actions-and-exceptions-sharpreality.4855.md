I3DB | 2019-01-23 22:55:49 UTC | #1

If I setup a box using:
```
var boxNode = Node.CreateChild();
var box = boxNode.CreateComponent<Box>(CreateMode.Local);
box.ViewMask = (uint)Masks.Hidden;
box.Color = Color.Magenta; 
```

Then call two actions on it
```
boxNode.RunActionsAsync(new FadeOut(2f));
boxNode.RunActionsAsync(new TintTo(2f,Color.Next());
```

This often, but not always, throws this exception:
```
Underlying native object was deleted for Handle=268256240. Material.SetShaderParameter
```

There are a couple items of interest that I observe.
If the boxNode.TintTo is called with no duration/delay, there is almost never an exception. 
The boxNode.FadeIn, boxNode.FadeOut don't recognize the new Color even with no exception, and upon invocation, the box reverts to the original color.

Even when the actions are called entirely separately (via time) and the box is tinted to an entirely different color, calling either fadein or fadeout will revert the box to its original color. 

It seems to me the TintTo sets a new material on the box, and FadeOut then throws the exception as the material it was using has been cleaned while the action was in progress.

This thread is a new thread that arose from the [last post on this previous thread](https://discourse.urho3d.io/t/is-the-resourcecache-known-to-be-buggy/4813/6), but it is a new topic so here is a new thread. 

Just trying to figure out what's happening, and to see if anyone who reads this might offer a clue, but can understand if no one does.

Anyway, it would seem to me there is an aggressive cleanup of materials occurring, too aggressive. In this case, I'm not sure how to handle it as I can't manually control the material deletion without significant re-coding effort, and using code that makes it all much more messy. Alternatively to never ever use those actions nearby each other.

The too aggressive cleanup, or the lack of reference detected by the cleanup mechanism, seems the issue here.

-------------------------

