Mike | 2017-01-02 00:58:08 UTC | #1

Is the LoadLayout function missing or is there a more generic way to load xml layouts in lua?

-------------------------

cadaver | 2017-01-02 00:58:09 UTC | #2

It has not been exposed so far because it returns shared pointers and needs special handling. But it should be doable, similar to ResourceCache::GetFile().

-------------------------

cadaver | 2017-01-02 00:58:09 UTC | #3

Should be exposed now. As it's already somewhat of a tradition, I put in also the string filename overload.

When you get the element from LoadLayout, you should either add it to the UI hierarchy, or delete manually. Otherwise there will be a memory leak.

-------------------------

Mike | 2017-01-02 00:58:09 UTC | #4

Many thanks, was not sure if missing function was intentional.
Working with string filename overload makes it really convenient to use  :stuck_out_tongue:

-------------------------

