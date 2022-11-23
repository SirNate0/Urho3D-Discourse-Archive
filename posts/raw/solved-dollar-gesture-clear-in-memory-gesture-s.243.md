Mike | 2017-01-02 00:59:07 UTC | #1

Multi gestures and Dollar gesture work great.  :slight_smile: 

When recording multiple gestures in a row, it's good to be able to discard the last one if we're not satisfied with it, and then continue the records.
Also it can be useful to clear all the in-memory gestures (both recorded and loaded) before starting recording a new one.

I'd like to know how we can achieve this. (I know I can save selectively by IDs, but it's not really convenient)

-------------------------

cadaver | 2017-01-02 00:59:07 UTC | #2

Best would be if SDL had a function to remove a gesture by ID, or all gestures. Currently it seems we'd have to add those ourselves.

-------------------------

cadaver | 2017-01-02 00:59:08 UTC | #3

Functions to remove a gesture by ID or to remove all gestures have been added.

-------------------------

Mike | 2017-01-02 00:59:08 UTC | #4

Many thanks cadaver, this will make life much easier  :wink:

-------------------------

