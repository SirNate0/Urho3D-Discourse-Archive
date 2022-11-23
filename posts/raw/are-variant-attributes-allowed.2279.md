Eugene | 2017-01-02 01:14:28 UTC | #1

Update: I see that answer is 'no'
But maybe it could be reached?

-------------------------

cadaver | 2017-01-02 01:14:28 UTC | #2

I think you could get it to work with slight hackery. You could have a VAR_VARIANT type, which in itself is kind of nonsense, but when the serialization code encounters that it knows that it must read both the type & value from the xml/json/binary.

A current workaround would be to use a VariantVector that contains only 1 element, but it'll have some overhead.

Don't think I would especially encourage it though, and haven't personally seen the need for it so far.

-------------------------

