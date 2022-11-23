rasteron | 2017-01-02 01:09:50 UTC | #1

Reading knet's doc [url=http://clb.demon.fi/knet/_kristalli_u_d_p.html]here[/url], it mentioned support for NAT punchthrough, so I was wondering how this can be done with udp.

-------------------------

smellymumbler | 2018-04-10 18:24:47 UTC | #2

Anyone found out anything about this?

-------------------------

Enhex | 2018-04-10 19:05:40 UTC | #3

Look into:
https://en.wikipedia.org/wiki/NAT_traversal

In general the best solution is to use UPnP if the router supports it.

-------------------------

smellymumbler | 2018-04-10 20:42:51 UTC | #4

Does kNet support UPnP?

-------------------------

Enhex | 2018-04-11 08:23:04 UTC | #5

No AFAIK. UPnP is high level protocol. IIRC Its NAT traversal feature requires broadcasting HTTP request over UDP.
There are few C libs, but they're quite low quality IMO.
I considered making a C++ lib for it, though didn't have a need for it so far.

https://en.wikipedia.org/wiki/Internet_Gateway_Device_Protocol

-------------------------

