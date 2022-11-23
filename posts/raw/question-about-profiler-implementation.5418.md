WangKai | 2019-08-06 22:57:19 UTC | #1

I'm checking the code. Why we use array instead of something like hashmap? Array is O(n) while hashmap can be regard of almost O(1)

```c++
    /// Return child block with the specified name.
    ProfilerBlock* GetChild(const char* name)
    {
        for (PODVector<ProfilerBlock*>::Iterator i = children_.Begin(); i != children_.End(); ++i)
        {
            if (!String::Compare((*i)->name_, name, true))
                return *i;
        }

        auto* newBlock = new ProfilerBlock(this, name);
        children_.Push(newBlock);

        return newBlock;
    }
```

-------------------------

SirNate0 | 2019-08-06 23:11:21 UTC | #2

It's just a guess without looking at the other code, but it's probably to preserve the order of the profiler blocks.

-------------------------

TheComet | 2019-08-06 23:55:07 UTC | #3

That, and how many sub-functions does a function typically call? A standard program will probably at most call 10, _maybe_ 20 different sub-functions per function if you're super crazy. On systems that use cached memory, a linear search can be much faster and more memory efficient on small datasets than a hashmap lookup, because when you access an element from a contiguous section of memory such as a vector, the CPU will cache the surrounding elements too, making the next few accesses basically free. This is not the case with a hashmap.

With that said, Urho3D does not add the PROFILE() macro to every function, so maybe there are hundreds of child blocks being created?

-------------------------

Leith | 2019-08-07 05:43:00 UTC | #4

I don't see any reason why a hash map is not being used in this case.
I concur, and note that there are many small places in urho where the code is less than optimal, though possibly more readable for it - fixing one or two is not going to make much difference in the long run, but if a concerted effort was made to stamp out such foolishness, I predict a marked and measurable improvement in overall performance across all platforms.

-------------------------

SirNate0 | 2019-08-07 07:18:50 UTC | #5

That seems like decent reasoning to leave it as a vector (though someone could always profile both options to give us a definitive answer). At the very least, it seems to me that we could improve the linear search if we stored the hash of the block name and compared with that rather than with a series of string comparisons.

-------------------------

TheComet | 2019-08-07 08:11:34 UTC | #6

It should also be noted that this doesn't impact the measurements, because the child is searched before the time is queried. At most it slightly decreases application performance when URHO3D_PROFILER=ON. I would assume one would configure URHO3D_PROFILER=OFF when shipping the final application, making this a non-issue for the end user.

-------------------------

Leith | 2019-08-08 10:44:21 UTC | #7

A hashmap is clearly cheaper than a string keyed map - thats what the OP intended, if I may jump in and assume... its at least one order cheaper, and this does add up quickly at runtime. There is no good reason why not, quoth I.

-------------------------

