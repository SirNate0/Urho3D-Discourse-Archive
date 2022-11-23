George1 | 2017-01-07 15:20:46 UTC | #1

Hi is there priority queue in Urho3D?

I'm making a request to have this feature.

**User case**

For example: if I want to push a struct or object items with a variable of interest (e.g. double time value). What we need is to read the minimum time items and pop the minimum time object from the queue efficiently.

-------------------------

jmiller | 2018-02-24 06:52:34 UTC | #2

Code like this could benefit (**edit** from a minheap)
[code]
HashMap<String, Timer> changes_;

bool FileWatcher::GetNextChange(String& dest) {
    unsigned delayMsec = (unsigned)(delay_ * 1000.0f);
    if (changes_.Empty())
        return false;
    else {
        for (HashMap<String, Timer>::Iterator i = changes_.Begin(); i != changes_.End(); ++i) {
            if (i->second_.GetMSec(false) >= delayMsec) {
                dest = i->first_;
                changes_.Erase(i);
                return true;
            }
        }
        return false;
    }
}
[/code]

This article has some performance measurements:
https://schani.wordpress.com/2010/04/30/linear-vs-binary-search/

-------------------------

George1 | 2017-01-08 14:27:13 UTC | #3

Hi do you think this is faster compares to the insertion sort and pop end item method?

-------------------------

jmiller | 2018-02-24 14:09:59 UTC | #4

That article draws a conclusion for its own cases one can consider (finding that for more than 64 ints, binary search was faster). If it is that time-critical, maybe it should be tested for one's specific use case... I would only be speculating, but others may have a better idea.

edit:
Using std, it's as simple as
`priority_queue<int, std::vector<int>, std::greater<int>>`
Urho version would take more work; maybe a starting point
  https://codeconnect.wordpress.com/2013/09/05/max-min-heap-using-c-stl/

-------------------------

artgolf1000 | 2017-01-09 00:35:03 UTC | #5

Hi, you can use std::priority_queue to achieve it.

-------------------------

George1 | 2017-01-12 02:33:49 UTC | #6

Hi Guys,
Thanks for the comments.
I know about the std priority queue. But my code currently using Urho Vector, So I can use them in Lua script without making any change or adding effort to this feature.

-------------------------

Stinkfist | 2017-01-12 12:53:18 UTC | #7

The kNet library that Urho uses has a MaxHeap class - would that work?

-------------------------

George1 | 2017-01-13 04:06:58 UTC | #8

Thanks,
I think it would be also good to also have the MinHeap.
I think Urho3D events feature would be more benefit if there is also a min heap. 

For example a server based event framework game will execute all earlier events (e.g. distributed  events in order to the clients.). This behaviour may be more efficient than sorting of list of events.

Best

-------------------------

