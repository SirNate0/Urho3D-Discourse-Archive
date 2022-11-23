Modanung | 2017-01-02 01:11:56 UTC | #1

As it is now, Light::SetShadowIntensity works counter-intuitively to me. Do others feel this as well?
In my eyes a shadow is more intense if it is more visible and full black should be 1, not 0. The way the value is handled now I'd call it shadow transparency. I'd like to suggest to keep the name and reverse the scale.

-------------------------

cadaver | 2017-01-02 01:11:56 UTC | #2

The accurate meaning of this value is "light intensity in shadow" (since there's only ever light addition in Urho's lighting passes, not reduction due to shadow) which is an easy fix in the header comment. Actually reversing the value would break existing scenes in which this attribute has been edited.

-------------------------

Modanung | 2017-01-02 01:11:56 UTC | #3

[quote="cadaver"]The accurate meaning of this value is "light intensity in shadow" (since there's only ever light addition in Urho's lighting passes, not reduction due to shadow)...[/quote]
I see. I guess some things just confuse. :wink:

-------------------------

