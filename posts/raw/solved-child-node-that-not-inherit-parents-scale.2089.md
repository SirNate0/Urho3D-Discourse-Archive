1vanK | 2017-01-02 01:12:56 UTC | #1

I need child node that moved with parent, but do not inherit its scale. How to do it? I see 2 approach for it:

1) Add flags for the nodes: inherit scale, move, rotation.
2) Add event "E_SCALECHANGED" and fix sizes of child nodes with SetSizeSilent().

Of course I can check sizes of schild nodes everey frame
[code]
Update()
{
    if (childNode_.GetWorldScale() != x)
        childNode_.SetWorldScale(x);
}
[/code]
but it looks as dirty hack

-------------------------

cadaver | 2017-01-02 01:12:56 UTC | #2

These kind of booleans is what Ogre does / used to do and they're quite nasty, as they'd fall directly on the fast path required to calculate global matrices.

If possible, I suggest keeping a non-scaled parent hierarchy, and adding a separate child for the scaled parent model.

-------------------------

1vanK | 2017-01-02 01:12:56 UTC | #3

This will help me, but in my case it will be ugly. Anyway, if it strongly affects the performance, it is not necessary.

-------------------------

