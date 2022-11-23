JimMarlowe | 2017-01-02 01:06:16 UTC | #1

This is a typical feature that allows networked applications to know something about the connections. 
The RoundTripTime value is already already being collected from kNet, in Connection::SendRemoteEvents(), but you need to log statistics to see it, and then it only comes out in a log message. Can a rtt float value be added to the Connection class? It can still be copied from kNet in SendRemoteEvents, but outside of the logStatistics_ block.

-------------------------

cadaver | 2017-01-02 01:06:17 UTC | #2

Has been exposed, along with other stats that are being logged + last heard time. Note that these are rolling averages updated by kNet each few seconds.

-------------------------

JimMarlowe | 2017-01-02 01:06:17 UTC | #3

Thank you sir fish. The kNet rolling averages are acceptable.

-------------------------

