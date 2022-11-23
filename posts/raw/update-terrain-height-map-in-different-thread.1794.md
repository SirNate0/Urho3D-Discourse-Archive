George | 2017-01-02 01:10:12 UTC | #1

Hi
I found out that terrain_->ApplyHeightMap() takes a bit of time to update. e.g. 131milisec.

Is it possible to call terrain_->ApplyHeightMap() on a different thread? It would be great for realtime operation.

Thanks

-------------------------

gawag | 2017-01-02 01:10:13 UTC | #2

Additional idea: It would be also good if the geometry (height map) could be changed per terrain chunk so that not the whole terrain has to be changed. This would greatly improve performance as changes could be done over several frames. No idea if this is already possible but it could be done and could fix the problem. I had the same problem and didn't fix it as it was just a test. Post your solution if you have one.   :wink:

-------------------------

