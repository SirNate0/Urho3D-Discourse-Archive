cftvgybhu549 | 2019-01-11 17:20:46 UTC | #1

I think that there is an error in this function at line 842 in Batch.cpp, where it remaps the material IDs in the sort key:  
`unsigned short materialID = (unsigned short)(batch->sortKey_ & 0xffff0000);`.
The materialID is always 0 no matter what sortKey_  value.
Because the data type of sortKey_   is unsigned long long.
when `(unsigned short) unsigned long long`, it will get the value in low 16 bit, that is 0.
 
I make the following modification.
 `unsigned short materialID = (unsigned short)((batch->sortKey_ & 0xffff0000) >> 16);`
the materialID will get the correct value and the function will go correct.

Welcome discussion.

-------------------------

WangKai | 2019-01-11 12:25:49 UTC | #2

It seems right to me.

-------------------------

cadaver | 2019-01-11 16:21:56 UTC | #3

Looks like a bug. There should be a shift of 16 bits to the right.

-------------------------

