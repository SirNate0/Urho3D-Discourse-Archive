indie.dev | 2017-01-02 00:59:39 UTC | #1

Hi, there.
I would like to add a color picker to the Editor and I guess it would be quite necessary for a comfortable experience.
However, there is a big question for me, that is, currently, every color parameter in Urho3D can be 'boosted', we can input any value larger than zero.
e.g. we can have a redder color (2.0, 0.0, 0.0)  that a normal red (1.0, 0.0, 0.0) which is important when we want to emphasize it.
I don't see any way that a standard color picker can do that.

Any ideas? Thanks.

-------------------------

cadaver | 2017-01-02 00:59:41 UTC | #2

A simple solution would be to have both a slider and a textedit for the value. The slider is clamped to 0-1 values, but if you want to use the extended range, you need to use the textedit.

-------------------------

indie.dev | 2017-01-02 00:59:41 UTC | #3

[quote="cadaver"]A simple solution would be to have both a slider and a textedit for the value. The slider is clamped to 0-1 values, but if you want to use the extended range, you need to use the textedit.[/quote]

Thank you cadaver! Your idea is definitely right. However, if we use a pie shape color picker, how can we handle the > 1.0 part of the color component? The deep question is, when and why should we keep the >1.0 part of the color. Or, shall we just use the [0, 1.0] clamped color?

-------------------------

cadaver | 2017-01-02 00:59:42 UTC | #4

If the color value is outside 0-1, then perhaps the pie should show no selection. Clicking on the pie selects a color in the 0-1 range, while using the R,G,B,A textedits only should preserve any values. The overbright values are less important after the addition of Light's brightness multiplier, but they may still be useful for eg. overbright material parameters.

-------------------------

boberfly | 2017-01-02 00:59:42 UTC | #5

Hi,

The colour picker GUI could indicate if the value is >1 (or potentially negative, depending on the signed/unsigned framebuffer used) by putting a small warning icon in a corner somewhere whenever any component isn't in the 0.0-1.0 range. This is how Nuke works and it comes in handy.

-------------------------

