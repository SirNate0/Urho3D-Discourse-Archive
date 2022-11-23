rku | 2017-01-02 01:12:09 UTC | #1

I dont do anything fancy rendering-wise, just load a scene using default renderer and have some input handling. Very basic stuff. Everything looks fine on desktop, however on android part of curved ground mesh renders texture in sort of stepped pattern where it should be a straight line. Cant see anything of this sort on desktop. Any idea what could cause this?
[img]https://i.imgur.com/nr6K0eh.png[/img]

-------------------------

Bananaft | 2017-01-02 01:12:09 UTC | #2

My bet on floating point precision. Mobile GPUs can be really bad at it. If you have a very long and thin polygons here, try splitting them to shorter ones.

-------------------------

rku | 2017-01-02 01:12:10 UTC | #3

Spot on. Subdividing mesh horizontally few fixed it. As you said i had very long polygons going forward. Thank you o/

-------------------------

