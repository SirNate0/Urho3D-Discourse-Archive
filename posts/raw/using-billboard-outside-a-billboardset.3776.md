nergal | 2017-11-24 18:00:17 UTC | #1

Is it possible to use Billboard without a BillboardSet and handle all Billboards manually?

According to the documentation it seems to require BillboardSet, but I'm not quite sure. At least it's not possible to use Billboard as a component. 

The reason I want to use Billboards without a set is because I want to have a dynamic sized set of Billboard and still be able to get the specific Billboard in the set by giving a predefined Index (such as a 3D array flatten as a 1D array).

Since a BillboardSet creates each Billboard beforehand it creates a lot of overhead memory wise.

-------------------------

Eugene | 2017-11-24 19:30:06 UTC | #2

[quote="nergal, post:1, topic:3776"]
Since a BillboardSet creates each Billboard beforehand it creates a lot of overhead memory wise.
[/quote]
You are tryin' to do something unlogical. The main purpose of `BillboardSet` is to optimize things by grouping.
You would have x10 overhead if allocate billboards one by one e,g, in `StaticModel`. x100, if you create a lot of `BillboardSet`s with single element.
If you want to have _a lot_ of billboards without pre-allocating storage, you could resize `BillboardSet` on demand or create a few of them to avoid buffers re-allocation.

-------------------------

