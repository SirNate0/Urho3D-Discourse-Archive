Teknologicus | 2020-06-23 23:37:00 UTC | #1

> cmake -DURHO3D_LIB_TYPE=SHARED .

Output at [https://pastebin.com/BMGXuTL2](https://pastebin.com/BMGXuTL2)

> make -j4 VERBOSE=1

Linker stage output [https://pastebin.com/BvurSkFJ](https://pastebin.com/BvurSkFJ)

-------------------------

jmiller | 2020-06-24 13:42:57 UTC | #2

GCC v10 flipped a default option (common to no-common).
  https://gcc.gnu.org/bugzilla/show_bug.cgi?id=85678

I presume most projects like SDL will address the root causes in due course. As a temporary workaround, I built Urho with 
 `cmake -D CMAKE_CXX_FLAGS:string=-fcommon -D CMAKE_C_FLAGS:string=-fcommon ` (*edit*: Added cflags)

-------------------------

Teknologicus | 2020-06-24 01:01:49 UTC | #3

Thank you @jmiller.  Something additionally must be amiss on my Linux distro because I still get the linker errors even with doing a "cmake -D CMAKE_CXX_FLAGS:string=-fcommon" (on a freshly extracted Urho3D source code tree).

Fortunately I still have a functional build of Urho3D (prior to Manjaro updates) on my system that I'm using.

-------------------------

trillian | 2020-06-24 08:04:52 UTC | #4

I had that too, also on Manjaro. I disabled VIDEO_WAYLAND and it worked. I don't use Wayland and I don't have it installed, btw.

cmake -D VIDEO_WAYLAND=OFF

-------------------------

Teknologicus | 2020-06-24 08:06:46 UTC | #5

Thank you @trillian!  That solves my link issue.

-------------------------

jmiller | 2020-06-24 13:59:49 UTC | #6

I added `CMAKE_C_FLAGS` (which I forgot) above, which should help link SDL in the case of Wayland.

-------------------------

