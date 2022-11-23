Bananaft | 2017-01-02 01:05:36 UTC | #1

So, terrain generates tangent vectors, and stores it in vertexData, so it can then be used for normal mapping. But since terrain is pretty simple shape (a plane topologically), it's tangent vectors can easily be calculated in vertex shader.

Question is: is it worth anything to disable storing tangent vectors in vertexData and calculating 'em on gpu?

-------------------------

cadaver | 2017-01-02 01:05:36 UTC | #2

You can only know reliably by profiling on a variety of hardware. For Urho3D basic operation and the example assets included in the repo, I like the materials and shaders to be generic so that you could use a basic normalmapping shader on the terrain and it would just work, because the terrain vertices do include tangents. In your own projects you naturally can specialize everything.

-------------------------

GoogleBot42 | 2017-01-02 01:05:37 UTC | #3

It would decrease the amount of memory needed to store the mesh on the gpu.  Because of that it would also decrease the amount of data that needs to be sent to the gpu.  That is an interesting question.  Like cadaver said I think it would be best to try it and see on multiple gpu's...

This is very interesting to me because in a minecraft clone if one calculates the normals on the gpu vertices could be reused in different "cubes" in the world.  Thus, a lot of memory could be saved because this would at least cut in half the number of vertices and decrease the size of each vertex.

-------------------------

Bananaft | 2017-01-02 01:05:38 UTC | #4

[quote="GoogleBot42"] Because of that it would also decrease the amount of data that needs to be sent to the gpu.[/quote]
Does it always sends all vertex data to GPU, or only those utilized in shader?

[quote="cadaver"] I like the materials and shaders to be generic so that you could use a basic normalmapping shader on the terrain and it would just work[/quote]
That's reasonable, but It seems to me, that in real projects, terrain always need special treatment. And if you want a normal map on your terrain, DiffNormal technique is not a suitable option.

For my current project I'm messing with terrain shaders anyway, so this question popped up.

-------------------------

friesencr | 2017-01-02 01:05:38 UTC | #5

The shaders linking phase finds all the vertex attributes in the shader and binds them.  So only things used in the shader.  The same goes for uniforms.  I was debugging some shaders in RenderDoc and learned this :smiley:.  I was very confused for a bit but that is normal.

-------------------------

cadaver | 2017-01-02 01:05:38 UTC | #6

Since it's an interleaved stream of vertices, it likely still pays the memory bus transfer penalty for the unused vertex attributes. But the input assembler has less work to do per vertex.

-------------------------

Bananaft | 2017-01-02 01:05:39 UTC | #7

That's actually pretty cool.

-------------------------

GoogleBot42 | 2017-01-02 01:05:39 UTC | #8

Wow that is a really awesome feature!  I find myself constantly surprised about just how much Urho3D can do.  :slight_smile:

-------------------------

