lebrewer | 2022-03-14 15:23:58 UTC | #1

https://github.com/jrouwe/JoltPhysics

Very surprising release. And very high quality codebase as well.

-------------------------

JSandusky | 2022-03-15 02:53:49 UTC | #2

Deliberately accounting for streaming is nice.

Couldn't help but laugh at the accursed "*support double precision*" github issue that plagues everything.

-------------------------

Eugene | 2022-03-15 10:47:46 UTC | #3

Too bad platform support is worse than e.g. PhysX. I would have used it otherwise.

-------------------------

JSandusky | 2022-03-21 03:19:58 UTC | #4

The unrooted include directives are a name collision nightmare. I did not appreciate that one bit, even if it's a simple find-and-replace-all to transform every `#include <` into `#include <Jolt/` then fix up the std-lib includes. You really think there's not going to be a `<Math/float4.h>` in my paths to conflict with?

The library itself compiled nice and easy though I guess.

-------------------------

