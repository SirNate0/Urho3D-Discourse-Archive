Andre_B | 2017-01-19 12:31:46 UTC | #1

Im developing an app for ios and i was mostly testing it on a iphone 6 plus, where everything was working correctly.

However when i started testing on a iphone 5 some 3d lines simply did not draw at all, while drawing correctly on a iphone 6 plus.

I tried everything form turning off depth test, to changing depth compare mode to even changing the render passes the result was the same. Everything rendered correctly on 6 plus while on the Iphone 5 these specific lines did not render at all.

The only differences i can think of is float precision issues, anny ideas?

-------------------------

Andre_B | 2017-01-19 14:22:46 UTC | #2

Nevermind it was a clipping issue, different phones have different resolution coordinates for clipping.

-------------------------

