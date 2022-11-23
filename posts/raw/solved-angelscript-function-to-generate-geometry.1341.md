Bananaft | 2017-01-02 01:06:59 UTC | #1

Hello,

I want to write a script function, that will generate some custom geometry, something like this:

[code]
Geometry GustomGeom(uint16 param)
{
   Geometry@ geom = Geometry();  
   ...
   Do stuff, Generating and assigning vertex and index buffers
   ...
  
   return geom;
{

[/code]

It does not work. I've tried returning Model type, I've tried to pass Model or Geometry as a parameter into void function, so it can do it's stuff to it, but outcome is always the same:

[code]
[Mon Sep 07 03:31:12 2015] INFO: Scripts/game.as:117,1 Compiling void MakeObjects()
[Mon Sep 07 03:31:12 2015] ERROR: Scripts/game.as:124,13 No appropriate opAssign method found in 'Geometry' for value assignment
[Mon Sep 07 03:31:12 2015] ERROR: Scripts/game.as:125,11 No appropriate opAssign method found in 'Geometry' for value assignment
[Mon Sep 07 03:31:12 2015] ERROR: Scripts/game.as:125,11 Previous error occurred while attempting to create a temporary copy of object
[Mon Sep 07 03:31:12 2015] ERROR: Failed to compile script module Scripts/game.as
[/code]

I feel, I'm missing something essential.

Full code just in case:
[spoiler][code]
void MakeObjects()
{
      
    Model@ rb_Model = Model();
    
   Geometry geom = Ribbon(50);

    
   rb_Model.numGeometries = 1;
   rb_Model.SetGeometry(0, 0, geom);
   rb_Model.boundingBox = BoundingBox(Vector3(-0.5, -0.5, -0.5), Vector3(0.5, 0.5, 0.5));
   
   Node@ node = scene_.CreateChild("rb_Model");
   node.position = Vector3(0.0, 0.0, 0.0);
    StaticModel@ object = node.CreateComponent("StaticModel");
   object.model = rb_Model;
}

Geometry Ribbon(uint16 numVertices)
{
    Array<float> vertexData(numVertices * 6, 0.0f);
    Array<uint16> indexData(numVertices);
    
    for (uint16 i = 0; i<numVertices; ++i) vertexData[i] = Random();
    
    for (uint16 i = 0; i<numVertices; ++i) indexData[i] = i;


    VertexBuffer@ vb = VertexBuffer();
    IndexBuffer@ ib = IndexBuffer();
    Geometry@ geom = Geometry();
    
    vb.shadowed = true;
    vb.SetSize(numVertices, MASK_POSITION|MASK_NORMAL);
    VectorBuffer temp;
    for (uint i = 0; i < numVertices * 6; ++i)
        temp.WriteFloat(vertexData[i]);
    vb.SetData(temp);

    ib.shadowed = true;
    ib.SetSize(numVertices, false);
    temp.Clear();
    for (uint i = 0; i < numVertices; ++i)
        temp.WriteUShort(indexData[i]);
    ib.SetData(temp);

    geom.SetVertexBuffer(0, vb);
    geom.SetIndexBuffer(ib);
    geom.SetDrawRange(TRIANGLE_LIST, 0, numVertices);

    return geom;
}
[/code][/spoiler]

-------------------------

Bananaft | 2017-01-02 01:07:00 UTC | #2

[quote="Sinoid"]
Should be:
[code]Geometry@ GustomGeom(uint16 param)[/code][/quote]

Daaaamn, shame I didn't figured myself, to try that.

Thank you very much.

-------------------------

