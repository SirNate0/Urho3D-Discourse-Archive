slapin | 2017-06-02 07:41:00 UTC | #1

How would you check that Vector2 point is inside Vector<Vector2> polygon?

I mean polygons. Concave ones. I need this for some growth algorithm.

-------------------------

Eugene | 2017-06-02 11:37:12 UTC | #2

Have you tried that nice algo from wiki?
https://en.wikipedia.org/wiki/Point_in_polygon

-------------------------

slapin | 2017-06-02 15:37:04 UTC | #3

Nah, that is too complicated.
I use one found somewhere else:

    bool PointInPolygon(Vector2 point, Array<Vector2> points)
    {
            int i, j, nvert = points.length;
            bool c = false;

            j = nvert - 1;
            for (i = 0; i < nvert; j = i++) {
                    if (((points[i].y >= point.y ) != (points[j].y >= point.y) ) &&
                            (point.x <= (points[j].x - points[i].x) * (point.y -
                            points[i].y) / (points[j].y - points[i].y) + points[i].x))
                            c = !c;
            }
            return c;
    }

but was hoping there was something internal in Urho.

-------------------------

