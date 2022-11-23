slapin | 2017-01-02 01:14:35 UTC | #1

I decided to share a piece in AngelScript. It is useful to greatly reduce number of tests looking for neighbours.

Main code:
[code]
class Vertex {
    Vector2 coords;
    Vertex(Vector2 c)
    {
        this.coords = c;
    }
    int opCmp(Vertex@ other)
    {
        if (coords.x > other.coords.x)
            return 1;
        else if (coords.x < other.coords.x)
            return -1;
        else if (coords.y > other.coords.y)
            return 1;
        else if (coords.y < other.coords.y)
            return -1;
        else return 0;
    }
    bool opEquals(Vertex@ other)
    {
        if (other.coords == coords)
            return true;
        else
            return false;
    }
    String ToString() {
        return "Vertex [" + String(coords.x) + " " + String(coords.y) + "]";
    }
};
class Quadtree {
    Array<Vertex@> vertices(4);
    Rect rect;
    int num_stored = 0;
    bool split = false;
    Quadtree@ NE;
    Quadtree@ NW;
    Quadtree@ SW;
    Quadtree@ SE;
    Array<Quadtree@> sa(4);
    int count()
    {
        int ret = num_stored;
        if (split) {
           for (int i = 0; i < sa.length; i++)
               ret += sa[i].count();
        }
        return ret;
    }
    String ToString()
    {
        String rectstr = rect.ToVector4().ToString();
        return rectstr;
    }
    private void do_split()
    {
        float midx = (rect.left + rect.right) / 2.0;
        float midy = (rect.top + rect.bottom) / 2.0;
        NE = Quadtree(Rect(midx, rect.top, rect.right, midy));
        NW = Quadtree(Rect(rect.left, rect.top, midx, midy));
        SW = Quadtree(Rect(rect.left, midy, midx, rect.bottom));
        SE = Quadtree(Rect(midx, midy, rect.right, rect.bottom));
        split = true;
        sa[0] = NE;
        sa[1] = NW;
        sa[2] = SW;
        sa[3] = SE;
    }
    bool insert(Vertex@ vertex)
    {
        if ((rect.IsInside(vertex.coords) == OUTSIDE)) {
            return false;
        }
        if (num_stored < 4) {
            vertices[num_stored] = vertex;
            num_stored++;
            return true;
        } else {
            if (!split)
                do_split();
            for (int i = 0; i < sa.length; i++)
                if (sa[i].insert(vertex))
                    return true;
        }
        return false;
    }
    Array<Vertex@> search(Rect r)
    {
        int intersecting = 0, i, j;
        Array<Vertex@> ret;
        if (num_stored == 0 && !split)
            return ret;
        Rect tr(r);
        tr.Clip(rect);
        if (tr.size.length == M_INFINITY)
            return ret;
        ret.Resize(num_stored);
        for (i = 0; i < num_stored; i++)
            ret[i] = vertices[i];
        if (split) {
            for (i = 0; i < sa.length; i++) {
                Array<Vertex@> tmp = sa[i].search(r);
                int offset = ret.length;
                ret.Resize(offset + tmp.length);
                for (j = 0; j < tmp.length; j++) {
                    ret[offset + j] = tmp[j];
                }
            }
        }
        return ret;
    }
    Rect find_rect(Vertex@ v)
    {
        vertices.Resize(num_stored);
        if (vertices.Find(v) >= 0)
            return rect;
        else if (split)
            for (int i = 0; i < sa.length; i++) {
                Rect r = sa[i].find_rect(v);
                if (r.size.length > 0)
                    return r;
            }
         return Rect();
    }
    Quadtree(Rect r)
    {
        rect = r;
    }
};
[/code]
Test program / usage example:

[code]
#include "Vertex2.as"

void Start()
{
    Quadtree q(Rect(-500, -500, 500, 500));
    Image img;
    Rect search_rect(-100, -100, 100, 100);
    img.SetSize(1000, 1000, 3);
    img.ClearInt(0);
    int inrect = 0;
    int count = 0;
    Array<Vertex@> all_points;
    for (int i = 0; i < 100000; i++) {
        Vertex v(Vector2(Random(-500, 500), Random(-500, 500)));
        if (q.insert(v)) {
            count++;
            if (search_rect.IsInside(v.coords) != OUTSIDE) {
                all_points.Push(v);
                inrect++;
                img.SetPixel(v.coords.x + 500, v.coords.y + 500, Color(1.0, 1.0, 0.0));
            } else
                img.SetPixel(v.coords.x + 500, v.coords.y + 500, Color(1.0, 0.0, 0.0));
        } else
            img.SetPixel(v.coords.x + 500, v.coords.y + 500, Color(0.1, 0.1, 1.0));
    }
    Print("Searching");
    Array<Vertex@> vs = q.search(search_rect);
    Print("Search done");
    for (int i = 0; i < vs.length; i++)
        img.SetPixel(vs[i].coords.x + 500, vs[i].coords.y + 500, Color(0.6, 1.0, 0.6));
    Print("inrect: " + String(inrect));
    img.SavePNG("quadtree.png");
    Print("Saved");
    engine.Exit();
}

[/code]

The idea is that you use "insert" method to insert vertices and search for looking at them.

On image - red vertices are all vertices, green - the ones found by search.

-------------------------

