Bluemoon | 2017-01-02 00:59:58 UTC | #1

I am a bit confused on the uses of the snap tools included in the Editor horizontal tool bar, are they meant to snap the transformation to the nearest of a particular value or to increments of a value? I tried to use it but, honestly, can't figure out how it works.

-------------------------

friesencr | 2017-01-02 00:59:58 UTC | #2

The adjustment is snapped

[code]            if (moveSnap)
            {
                float moveStepScaled = moveStep * snapScale;
                adjust.x = Floor(adjust.x / moveStepScaled + 0.5) * moveStepScaled;
                adjust.y = Floor(adjust.y / moveStepScaled + 0.5) * moveStepScaled;
                adjust.z = Floor(adjust.z / moveStepScaled + 0.5) * moveStepScaled;
            }[/code]

It rounds the movement to the nearest wholementment.  If the position of x is 1.5 and the snap size is set to 1 it will move to 1.5 + 1 = 2.5 and not in absolute terms like setting 1.5 -> 2.0.

The snapping size is configurable in the settings per move, rotate, scale.

-------------------------

Bluemoon | 2017-01-02 01:00:00 UTC | #3

Thanks for the explanation :slight_smile:

-------------------------

