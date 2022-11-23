practicing01 | 2017-01-02 01:04:24 UTC | #1

Any links on figuring this out would be cool too.  Thanks!

-------------------------

cadaver | 2017-01-02 01:04:25 UTC | #2

You would likely be using the lan broadcast address to send a message asking "anyone here?" and any running servers could respond with their IP address. It's likely the kNet library doesn't help in this, as it's about making point-to-point connections between a client and server. But you should be able to accomplish the broadcast with raw socket programming.

-------------------------

practicing01 | 2017-01-02 01:04:25 UTC | #3

Would "raw socket programming" be crossplatform compatible (my main targets are android and linux)?

-------------------------

cadaver | 2017-01-02 01:04:25 UTC | #4

You'll be looking at the Berkeley sockets API, which is the same anywhere, except for some minor differences on Windows. Android is basically Linux.

-------------------------

