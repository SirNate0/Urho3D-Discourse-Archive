SirNate0 | 2019-01-08 22:07:05 UTC | #1

Before I assume that there isn't one, does anyone know if there is a limit on the number of geometries a model can have?

-------------------------

GodMan | 2019-01-09 02:02:28 UTC | #2

That really depends on your scene, and what your trying to do, and the system your running on.

-------------------------

Modanung | 2019-01-09 10:49:37 UTC | #3

There's always some limit somewhere. When in doubt, probe. (and/or ask of course)

-------------------------

cadaver | 2019-01-09 11:57:48 UTC | #4

The geometry count (and other loops or data structures related to it) use 32bit unsigneds, so the theoretical upper limit is‭ 4294967295‬.

In forward lighting there's an optimization that combines the first light and base pass, which needs a bitfield that also uses a 32-bit value, so the optimization can only be used for the first 32 geometries / batches. Based on that using more than 32 can't be recommended, unless you're using deferred lighting.

In general the lower the better, you always pay in performance for more geometries, as the engine needs to do more bookkeeping and issue more draw calls.

-------------------------

