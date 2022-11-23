friesencr | 2017-01-02 01:05:06 UTC | #1

The ability to set geometry raw data on a range.

-------------------------

cadaver | 2017-01-02 01:05:07 UTC | #2

This would be an unsafe function as the raw data size is not tracked by the Geometry. All Geometry does is to store the buffer pointer you have given it (SetRawVertexData() / SetRawIndexData()) I recommend managing it yourself and simply rewriting parts of the buffer.

-------------------------

friesencr | 2017-01-02 01:05:07 UTC | #3

Thank you for the advice.

-------------------------

