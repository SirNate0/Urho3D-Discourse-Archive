Mike | 2017-01-02 01:13:30 UTC | #1

I have some trouble converting a hexadecimal String to unsigned.
For example, converting "0xFFFFFF" to 0xFFFFFF or directly to unsigned.
Using String::ToUInt() returns 0.

-------------------------

cadaver | 2017-01-02 01:13:30 UTC | #2

It uses the strtoul function using base 10 so it doesn't support that notation. Exposing the base as a parameter or adding an overload would work, though.

EDIT: The original reason for that decision (instead of defaulting the base parameter to 0 so it autodetects) is that a string containing beginning zeroes would be autodetected as octals, which is possibly unwanted.

-------------------------

cadaver | 2017-01-02 01:13:31 UTC | #3

Base parameter added in master branch.

-------------------------

Mike | 2017-01-02 01:13:31 UTC | #4

Many thanks for the quick fix, works perfectly  :stuck_out_tongue: 
Can ToColor() benefit from the same kind of improvement ?

-------------------------

cadaver | 2017-01-02 01:13:31 UTC | #5

We define Color as floats, its string conversion is "r g b a" which is used throughout in Urho's materials and it's the format which ToColor() handles.

Handling the common hex encoding of 8-bit RGB colors is outside of what Urho itself requires. It could be added, sure, but I don't see it especially important.

-------------------------

Mike | 2017-01-02 01:13:31 UTC | #6

OK, it is not mandatory at all, getting the hex is enough.

-------------------------

