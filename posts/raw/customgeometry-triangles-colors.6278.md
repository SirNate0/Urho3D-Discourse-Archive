lama2005 | 2020-07-19 08:28:23 UTC | #1

When I add two triangles into one CustomGeometry only one of them has the specified color, the other one is black.

            float y = 0.01f;

            var geom = Node.CreateComponent<CustomGeometry>();
            geom.BeginGeometry(0, PrimitiveType.TriangleList);

            geom.DefineVertex(new Vector3(X1, y, Z1));
            geom.DefineVertex(new Vector3(X1, y, Z2));
            geom.DefineVertex(new Vector3(X2, y, Z2));

            geom.DefineVertex(new Vector3(X1, y, Z1));
            geom.DefineVertex(new Vector3(X2, y, Z2));
            geom.DefineVertex(new Vector3(X2, y, Z1));

            geom.SetMaterial(Material.FromColor(Color));
            geom.Commit();
            return geom;

How can I set the color for the 2nd triangle?

-------------------------

SirNate0 | 2020-07-19 19:12:41 UTC | #2

Use vertex colors and a material that uses them rather than creative a material with 1 color. It's odd that one of the triangles is black, though. I'd have expected they'd be the same color. I'm not certain custom geometry supports vertex colors - it probably does, but if it doesn't I'd suggest looking at some of the other posts about how to create a geometry for a model.

-------------------------

lama2005 | 2020-07-19 19:14:39 UTC | #3

Thank you for your hint. Using the material VColUnlit.xml and setting Color by calling geometry.DefineColor before defining vertices solved the problem.
![rect_color|690x393](upload://ijWsXvJG5X7GJq9Q94qMkOz3rtQ.png)

-------------------------

