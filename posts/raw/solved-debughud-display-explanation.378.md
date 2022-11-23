Bluemoon | 2017-01-02 00:59:58 UTC | #1

It's unfortunate that the only information I can interpret from the DebugHud display are those listed on the left hand side of the screen when it appears, i.e Triangle , Batches, View, Lights, ShadowMaps and Occluders. But for the table on the right hand side, I'm pretty lost. I understand the column labelled "Block" to be the subroutines called for each RunFrame loop of the engine and the "Cnt" to possibly be the frame count per seconds, however, for the remaining, which are "Avg", "Max", "Frame" and "Total", I'm not really sure of what I think they are.

A little explanation on these will be highly appreciated.

-------------------------

reattiva | 2017-01-02 00:59:59 UTC | #2

It should be something like this:

Cnt = number of block calls in the last interval
Avg = average block time in ms in the last interval
Max = maximum block time in ms in the last interval
Frame = per frame average block time in ms in the last interval
Total = accumulative block time in ms in the last interval

The default interval is 1 second.

For example:
interval = 1 second
block calls in the interval = 10
block call time = 10ms for 9 times, 20ms for 1 time
frames in the interval = 5

cnt = 10
total = 10ms * 9 + 20ms * 1 = 110ms
avg = total / cnt = 110ms / 10 = 11ms
max = 20ms
frame = total / frames = 110ms / 5 = 22ms

-------------------------

Bluemoon | 2017-01-02 01:00:00 UTC | #3

I guess I made some terrible assumptions there  :smiley: , thanks for putting me through

-------------------------

