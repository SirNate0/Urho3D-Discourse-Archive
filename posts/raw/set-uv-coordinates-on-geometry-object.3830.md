IvanP | 2017-12-08 22:56:04 UTC | #1

I have viewed DynamicGeometry sample. Author there constructs Geometry instance and uses index buffer to optimize vertex usage and to improve calculation of normals on constructed object. But Geometry does not allow you to set UV coordinates needed to map a texture. A CustomGeometry class has this method, but it does not allow you to use index buffer. 
Is there any way to set UV coordinates on Geometry?

-------------------------

1vanK | 2017-12-08 23:45:40 UTC | #2

```
        PODVector<VertexElement> elements;
        elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));
        elements.Push(VertexElement(TYPE_VECTOR3, SEM_NORMAL));
       // Add any vertex attributes
```

-------------------------

