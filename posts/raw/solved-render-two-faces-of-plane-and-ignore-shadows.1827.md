Lichi | 2017-01-02 01:10:28 UTC | #1

Hi, im trying to make a plane of grass, and i have to make the grass plane visible of two faces. Anyone knows how?
The other problem I have is that if the light illuminates one side of the plane, the other is dark and the grass is not seen. I don't know if there's a material that ignore the shadows o something like this.
Screen of grass problem: [imgur.com/WU30Gc9](http://imgur.com/WU30Gc9)
Thanks! :smiley:

-------------------------

weitjong | 2017-01-02 01:10:28 UTC | #2

This is a FAQ. Turn off back face culling by setting the "cull" attribute to none in your material. See [urho3d.github.io/documentation/H ... rials.html](http://urho3d.github.io/documentation/HEAD/_materials.html)

-------------------------

rasteron | 2017-01-02 01:10:29 UTC | #3

Hey Lichi, just set the Cull to none in your plan grass material. There are a few methods to improve double sided mesh lighting like grass and branches, the best option that I know and a lot of game artists are doing is to edit the normals and make it to point upward or to a desired direction. You can easily do this in Blender by the Normal Edit Modifier:

[img]http://wiki.blender.org/uploads/thumb/8/8e/CustomNormals_grass_example.png/400px-CustomNormals_grass_example.png[/img]

[wiki.blender.org/index.php/User: ... als_Manual](http://wiki.blender.org/index.php/User:Mont29/Foundation/Split_Vertex_Normals/Custom_Split_Normals_Manual)

-------------------------

Lichi | 2017-01-02 01:10:29 UTC | #4

Thanks! :smiley:
Results without culling: [imgur.com/2ixBTyG](http://imgur.com/2ixBTyG)
PS1: rasteron I'm will implement the method of change the normal direction when in finish implementing grass density map, ty for the tip  :stuck_out_tongue: 
PS2: sorry for faq question :unamused:

-------------------------

