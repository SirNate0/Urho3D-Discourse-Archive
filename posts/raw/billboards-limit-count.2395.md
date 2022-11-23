dakilla | 2017-01-02 01:15:10 UTC | #1

Hi

Is it possible to enlarge the max number of Billboards in BillboardSet ?
it is actually limited to  : MAX_BILLBOARDS = 65536 / 4 => (16384)

I tried to set 500'000 and using index buffer with large indices, but it draw nothing...

-------------------------

cadaver | 2017-01-02 01:15:16 UTC | #2

It should just need writing 32bit indices properly, so this shouldn't be impossible to add. 

I wouldn't necessarily recommend using more than what fits to 16bit indices, since it's more data to write and slower to access, however the indices just need to be written once.

-------------------------

cadaver | 2017-01-03 20:18:38 UTC | #3

Optional 32bit indices for billboards are in the master branch. Thinking of it, same could be done to DecalSet quite easily, it's just not necessarily a wise thing to do.

-------------------------

dakilla | 2017-01-02 01:15:22 UTC | #4

great, thanks  :slight_smile:

-------------------------

