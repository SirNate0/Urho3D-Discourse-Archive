stark7 | 2017-08-21 02:47:24 UTC | #1

Would it be possible to add:

public Task<ActionState> RunActionsAsync(FiniteTimeAction action);
public Task<ActionState> RunActionsAsync(params FiniteTimeAction[] actions);

To Animatable 

Such that UIElement would also be able to benefit from them?

I would love to be able to do something like EaseBounceOut on a UIElement Text.

Also, is there maybe another way to accomplish this?

-------------------------

stark7 | 2017-08-22 21:30:58 UTC | #2

I just saw:

https://github.com/urho3d/Urho3D/pull/2074

so yeah, these are exciting times indeed.

-------------------------

