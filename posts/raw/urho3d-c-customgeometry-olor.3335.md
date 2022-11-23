Artemprodigy | 2017-07-10 12:16:03 UTC | #1

It's necessary to draw semitransparent triangles that would be visible where they intersect. I tried different CoreAssets.Techniques but unseccessfully. And how to choose special color for imposing triangles, not default mixed color?

CustomGeometry geom = geomNode.CreateComponent<CustomGeometry>();
Material geomMaterial = new Material();
geomMaterial.SetTechnique(0, CoreAssets.Techniques.NoTextureUnlitVCol, 50, 0.5f);
geom.SetMaterial(0, geomMaterial);                    
geom.BeginGeometry(0, PrimitiveType.TriangleList);

Urho.Color color = new Urho.Color(0.85f, 0.8f, 0.2f, 0.35f);
geom.DefineVertex(list[0]);
geom.DefineColor(color);
geom.DefineVertex(list[i]);
geom.DefineColor(color);   
geom.DefineVertex(list[i+1]);
geom.DefineColor(color);

geom.Commit();

-------------------------

