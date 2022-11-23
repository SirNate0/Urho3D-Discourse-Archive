Askhento | 2020-12-23 14:07:54 UTC | #1

Is it possible to know what is current OS inside angel script?

-------------------------

throwawayerino | 2020-12-23 14:37:32 UTC | #2

Is there even a way to get OS in C++ that doesn't involve macros? If there is, then the function is probably exposed to script.
If you're not using the Urho3DPlayer you could check for compile time defines and pass them to your init script. Which isn't an acceptable solution but can be a temporary fix.

-------------------------

1vanK | 2020-12-23 21:23:15 UTC | #3

GetOSVersion

Post must be at least 20 chars

-------------------------

