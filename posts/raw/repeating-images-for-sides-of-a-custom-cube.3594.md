ppsychrite | 2017-09-22 02:42:42 UTC | #1

Hello!

My current system for giving a cube repeating textures is to SetNumGeometries(6) and set texcoords to 

    0.0f 0.0f
    repeat.x, 0.0f 
    repeat.x, repeat.y
    0.0f, repeat.y

While this works fine it seems to lag when spawning in 1000 of these custom cubes compared to 1000 textured cube models. 

What I think would be better now is to have a texture with 6 spaces on it ( (64 * 3) * (64 * 2) )
This would work find if the texture wasn't repeating but I want it to be repeating. How would I go around to doing it? :thinking:

-------------------------

Eugene | 2017-09-23 08:01:37 UTC | #2

How many textures and materials do you actually use?

-------------------------

ppsychrite | 2017-09-23 11:56:06 UTC | #3

Originally, I used only two materials and two textures.
I now plan on merging it into one texture and one material, unless there's a way to have multiple textures per mesh.

-------------------------

