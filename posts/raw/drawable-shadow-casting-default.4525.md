QBkGames | 2018-09-07 08:41:49 UTC | #1

Just wondering why the cast shadow flag of the Drawable is false by default? I find that I have to add code to enable shadow casting all throughout my game project.
Wouldn't the most common scenario be to have shadow casting enabled and require that you manually disable it for a few exceptional cases?

-------------------------

Modanung | 2018-09-07 11:28:46 UTC | #2

Performance says no. :slight_smile:

It's better to add shadow where you want it, than having to remove it where you don't see it. When you don't care about having shadows, they shouldn't be there.
Admittedly this is something that made sigh a bit once in a while, but I do not think the default should be changed.

-------------------------

WangKai | 2018-09-08 14:21:39 UTC | #3

You can have a loop to change the shadow casting logic. Maybe we can add an editor operator for it.

-------------------------

