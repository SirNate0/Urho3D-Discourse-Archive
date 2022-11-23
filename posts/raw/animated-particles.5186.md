GoldenThumbs | 2019-05-25 04:28:20 UTC | #1

Like, a sprite sheet for particles. I know it's doable in Urho, I've done it before. I have the particle editor open, assigned a material with the "sprite sheet" and put down a texture frame, the issue I'm having now is that it works differently than most other engines I've used where you put in a sprite size then add an offset in pixels. I know that I figured it out before, but I seem to have deleted that project with that particle effect. How does this "particle sprite sheet" sort of thing work in Urho?

-------------------------

Leith | 2019-05-25 05:05:17 UTC | #2

Hi GoldenThumbs!

ParticleEmitter component has a ParticleEffect member, which we can edit.
The ParticleEffect lets us add "texture frames". These are a lot like animation keyframes.
They have five values we can set.
The first value is the time at which each frame occurs, relative to the time the particle was born, given as a floating point value, in Seconds. Therefore, your first TextureFrame should have a time of Zero.
The other four values, also floating-point, are the UV coordinates of the sprite frame (min/max corners) in the particle's material (diffuse/albedo) texture. For each sprite frame, create a texture frame, and fill in the information for the time and the upper/lower corner UV coords.
UV coordinates are unsigned normalized values, ie between 0 and 1 - so to convert from pixels to normalized coordinates, we just need to divide the pixel coordinate by the texture width and height to yield a value between 0 and 1 in both the X and Y axes (oh, and possibly account for "Y-Flipping") but basically mapping between any number range and the (signed or unsigned) normal range is straightforward.

-------------------------

Modanung | 2019-05-26 20:46:05 UTC | #3

Wrote a [console application](https://gitlab.com/snippets/1860709) that may be useful:

``` c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
    if (argc != 6 && argc != 4) {

        printf("Usage:\n");
        printf("columns rows interval\n");
        printf(" or\n");
        printf("columns rows width height interval\n");
        return 1;
    }


    int columns     = atoi(argv[1]);
    int rows        = atoi(argv[2]);
    double width    = 1.0 / columns;
    double height   = 1.0 / rows;
    double interval = atof(argv[3]);

    if (argc == 6) {

        width  = atof(argv[3]);
        height = atof(argv[4]);
        interval = atof(argv[5]);
    }

    for (int j = 0; j < rows; ++j) {
        for (int i = 0; i < columns; ++i) {

            printf("<texanim uv=\"");
            printf("%.3f ", i      * width);
            printf("%.3f ", j      * height);
            printf("%.3f ",(i + 1) * width);
            printf("%.3f" ,(j + 1) * height);
            printf("\" time=\"%.3f\" />\n", interval * (i + columns * j));
        }
    }

  return 0;
}
```

Example output for `anido 2 3 .17`:
```
<texanim uv="0.000 0.000 0.500 0.333" time="0.000" />
<texanim uv="0.500 0.000 1.000 0.333" time="0.170" />
<texanim uv="0.000 0.333 0.500 0.667" time="0.340" />
<texanim uv="0.500 0.333 1.000 0.667" time="0.510" />
<texanim uv="0.000 0.667 0.500 1.000" time="0.680" />
<texanim uv="0.500 0.667 1.000 1.000" time="0.850" />
```

-------------------------

