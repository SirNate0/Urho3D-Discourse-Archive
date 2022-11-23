Sinoid | 2017-05-13 05:29:01 UTC | #1

Surround sound (3+ speakers) is largely done. The changes to update your code will be small, just the mono/stero bool has turned into an enum for the speaker mode. If you aren't working with audio directly then it's no change, you'll automatically get surround sound through the listener.

While I have exposed direct access to the LFE (subwoofer) channel, it is by default on a noised-bandpass (if you exceed the cap it injects noise). If you disable that bandpass do not cry to me about how you blew the diaphragm on your sub (tube-subs obviously don't have this issue, but there's no standard on enumerating tube-sub devices).

I'll post this to github in a few days, and once 1.7 is out I'll submit a PR.

-------------------------

