sabotage3d | 2017-01-02 01:01:54 UTC | #1

Hello ,

Is it currently possible to visualize vectors as lines, edges as lines and positions as points ?
I know that the Physics Debug Drawer is already doing a similar thing but I would like to do it directly.

[img]http://i.imgur.com/Dqs8WEn.jpg[/img]

-------------------------

codingmonkey | 2017-01-02 01:01:54 UTC | #2

add your points to vb create ib(1,2,3...)

add vb and ib to geom

set geom - Geometry::SetDrawRange() method to LINE_STRIP or  POINT_LIST

enum PrimitiveType
{
    TRIANGLE_LIST = 0,
    LINE_LIST,
    POINT_LIST,
    TRIANGLE_STRIP,
    LINE_STRIP,
    TRIANGLE_FAN
};

i suppose it's must work

-------------------------

