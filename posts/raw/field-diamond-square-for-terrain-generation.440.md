vivienneanthony | 2017-01-02 01:00:24 UTC | #1

Hey!

Does this make any sense to anyone? I'm trying to get the basic concept of this.I'm asking because if its done its pretty much a field diamond square procedual method that could use time and a hash table to create infinite terrain with wrapping.

Generated picture [tinypic.com/view.php?pic=aaho3t&s=8#.VBjW3K1hWio](http://tinypic.com/view.php?pic=aaho3t&s=8#.VBjW3K1hWio)

Javascript demostration [tatarize.nfshost.com/FieldDiamondSquare.htm](http://tatarize.nfshost.com/FieldDiamondSquare.htm)
Basic Algorithm and theory of use [godsnotwheregodsnot.blogspot.com ... rrain.html](http://godsnotwheregodsnot.blogspot.com/2013/11/field-diamond-squared-fractal-terrain.html)

Vivienne

The Javascript Code 
[code]
function diamondSquaredMap(x, y, width, height, iterations) {
    var map = fieldDiamondSquared(x, y, x+width, y+height, iterations);

    var maxdeviation = getMaxDeviation(iterations);

    for (var j = 0; j < width; j++) {
        for (var k = 0; k < height; k++) {
            map[j][k] = map[j][k] / maxdeviation;
        }
    }
    return map;

    function create2DArray(d1, d2) {
        var x = new Array(d1),
                i = 0,
                j = 0;

        for (i = 0; i < d1; i += 1) {
            x[i] = new Array(d2);
        }
        return x;
    }

    function fieldDiamondSquared(x0, y0, x1, y1, iterations) {
        if (x1 < x0) { return null; }
        if (y1 < y0) { return null; }
        var finalwidth  = x1 - x0;
        var finalheight = y1 - y0;
        var finalmap = create2DArray(finalwidth, finalheight);
        if (iterations === 0) {
            for (var j = 0; j < finalwidth; j++) {
                for (var k = 0; k < finalheight; k++) {
                    finalmap[j][k] =  displace(iterations,x0+j,y0+k) ;
                }
            }
            return finalmap;
        }
        var ux0 = Math.floor(x0 / 2) - 1;
        var uy0 = Math.floor(y0 / 2) - 1;
        var ux1 = Math.ceil(x1 / 2) + 1;
        var uy1 = Math.ceil(y1 / 2) + 1;
        var uppermap = fieldDiamondSquared(ux0, uy0, ux1, uy1, iterations-1);

        var uw = ux1 - ux0;
        var uh = uy1 - uy0;

        var cx0 = ux0 * 2;
        var cy0 = uy0 * 2;

        var cw = uw*2-1;
        var ch = uh*2-1;
        var currentmap = create2DArray(cw,ch);

        for (var j = 0; j < uw; j++) {
            for (var k = 0; k < uh; k++) {
                currentmap[j*2][k*2] = uppermap[j][k];
            }
        }
        var xoff = x0 - cx0;
        var yoff = y0 - cy0;
        for (var j = 1; j < cw-1; j += 2) {
            for (var k = 1; k < ch-1; k += 2) {
                currentmap[j][k] = ((currentmap[j - 1][k - 1] + currentmap[j - 1][k + 1] + currentmap[j + 1][k - 1] + currentmap[j + 1][k + 1]) / 4) + displace(iterations,cx0+j,cy0+k);
            }
        }
        for (var j = 1; j < cw-1; j += 2) {
            for (var k = 2; k < ch-1; k += 2) {
                currentmap[j][k] = ((currentmap[j - 1][k]     + currentmap[j + 1][k]     + currentmap[j][k - 1]     + currentmap[j][k + 1]) / 4) + displace(iterations,cx0+j,cy0+k);
            }
        }
        for (var j = 2; j < cw-1; j += 2) {
            for (var k = 1; k < ch-1; k += 2) {
                currentmap[j][k] = ((currentmap[j - 1][k]     + currentmap[j + 1][k]     + currentmap[j][k - 1]     + currentmap[j][k + 1]) / 4) + displace(iterations,cx0+j,cy0+k);
            }
        }

        for (var j = 0; j < finalwidth; j++) {
            for (var k = 0; k < finalheight; k++) {
                finalmap[j][k] = currentmap[j+xoff][k+yoff];
            }
        }

        return finalmap;
    }

    // Random function to offset
    function displace(iterations, x, y) {
        return (((PRH(iterations,x,y) - 0.5)*2)) / (iterations+1);
    }

    function getMaxDeviation(iterations) {
        var dev = 0.5 / (iterations+1);
        if (iterations <= 0) return dev;
        return getMaxDeviation(iterations-1) + dev;
    }

    //This function returns the same result for given values but should be somewhat random.
    function PRH(iterations,x,y) {
        var hash;
        x &= 0xFFF;
        y &= 0xFFF;
        iterations &= 0xFF;
        hash = (iterations << 24);
        hash |= (y << 12);
        hash |= x;
        var rem = hash & 3;
        var h = hash;

        switch (rem) {
            case 3:
                hash += h;
                hash ^= hash << 32;
                hash ^= h << 36;
                hash += hash >> 22;
                break;
            case 2:
                hash += h;
                hash ^= hash << 22;
                hash += hash >> 34;
                break;
            case 1:
                hash += h;
                hash ^= hash << 20;
                hash += hash >> 2;
        }
        hash ^= hash << 6;
        hash += hash >> 10;
        hash ^= hash << 8;
        hash += hash >> 34;
        hash ^= hash << 50;
        hash += hash >> 12;

        return (hash & 0xFFFF) / 0xFFFF;
    }[/code]

C++ Code / Somewhat functional at least no memory leak error
[code]///Headers
#include <vector>
#include <cstdio>
#include <cmath>
#include <iostream>

#include <stdio.h>
#include <stdlib.h>

#include <png++/png.hpp>
#include <png++/image.hpp>
#include <png++/rgb_pixel.hpp>



using namespace std;

/// Terraub Functions
double * getFieldSquareTerrain(int x0,int y0, int x1, int y1, unsigned int iterations);
double displace(unsigned int iterations,int x, int y);
double getMaxDeviation(unsigned int iterations);
double PRH(unsigned iterations, int x, int y);
double * getFieldDiamondSquaredMap(int x, int y, int width, int height, unsigned int iterations);

//Size of the grid to generate
//This must be 2^n+1 (e.g. 257)
const int DATA_SIZE = 1024;

void SaveTerrFile(const double * image);

/// Main function
int main()
{
    /// Define Settings
    int width=1024;
    int height=1024;
    int iterations=1023;
    int x=0;
    int y=0;

    // allocate memory
    double * map=new double[width*height];

    map=getFieldDiamondSquaredMap(x,y,width,height,iterations);

    SaveTerrFile(map);

    return 1;
}

double * getFieldDiamondSquaredMap(int x, int y, int width, int height, unsigned int iterations)
{
    /// Allocate memory for final mapdouble
    double * map = new double[width*height];

    map = getFieldSquareTerrain(x, y, x+width, y+height, iterations);

    double maxdeviation = getMaxDeviation(iterations);

    for (unsigned int x = 0; x < width; x++)
    {
        for (unsigned int  y = 0; y < height; y++)
        {
            map[x*y] = map[x*y] / maxdeviation;
        }
    }

    return map;
}

double * getFieldSquareTerrain(int x0, int y0, int x1, int y1, unsigned int iterations)
{
    /// Define final height and width
    int finalwidth  = x1 - x0;
    int finalheight = y1 - y0;

    /// Allocate memory for final map
    double * finalmap = new double[finalwidth*finalheight];

    /// Test iteration
    if (iterations == 0)
    {
        for (unsigned int x = 0; x < finalwidth; x++)
        {
            for (unsigned int y = 0; y < finalheight; y++)
            {
                finalmap[x*y] =  displace(iterations,x0+x,y0+y) ;
            }
            return finalmap;
        }
    }

    /// Define ceil and floor
    int upper_x0=floor(x0/2) - 1;
    int upper_y0=floor(y0/2) - 1;
    int upper_x1=ceil(x1/2)+1;
    int upper_y1=ceil(y1/2)+1;

    /// Define upper height and width for upper maps
    int upper_xwidth= upper_x1-upper_x0;
    int upper_yheight= upper_y1-upper_y0;

    /// Allocate memory for upper map width and height
    double * uppermap = new double[upper_xwidth*upper_yheight];

    /// Pass another iteration
    uppermap = getFieldSquareTerrain(upper_x0, upper_y0, upper_x1, upper_y1, iterations-1);

    /// Define counter height and width
    int counter_x0= upper_x0 * 2;
    int counter_y0= upper_y0 * 2;

    int counter_width = upper_xwidth*2-1;
    int counter_height = upper_yheight*2-1;

    /// Allocate memory for currentmap using counter height and width
    double * currentmap = new double[counter_width*counter_height];

    /// Copy information to double map
    for (unsigned int x = 0; x < upper_xwidth; x++)
    {
        for (unsigned int y = 0; y< upper_yheight; y++)
        {
            currentmap[(x*2)*(y*2)] = uppermap[x*y];
        }
    }

    /// Define offset
    int xoff = x0 - counter_x0;
    int yoff = y0 - counter_y0;

    /// Use a diamond mehod algorithm
    for (unsigned int x = 1; x < counter_width-1; x += 2)
    {
        for (unsigned int y = 1; y < counter_height-1; y += 2)
        {
            currentmap[x*y] = ((currentmap[(x - 1)*(y - 1)] + currentmap[(x - 1)*(y + 1)] + currentmap[(x + 1)*(y - 1)] + currentmap[(x + 1)*(y + 1)]) / 4) + displace(iterations,counter_x0+x,counter_y0+y);
        }
    }
    for (unsigned int x = 1; x < counter_width-1; x += 2)
    {
        for (unsigned int y = 2; y < counter_height-1; y += 2)
        {
            currentmap[x*y] = ((currentmap[(x - 1)*y]     + currentmap[(x + 1)*y]     + currentmap[x*(y - 1)]     + currentmap[x*(y + 1)]) / 4) + displace(iterations,counter_x0+x,counter_y0+y);
        }
    }
    for (unsigned int x = 2; x < counter_width-1; x += 2)
    {
        for (unsigned int y = 1; y < counter_height-1; y += 2)
        {
            currentmap[x*y] = ((currentmap[(x - 1)*y]     + currentmap[(x + 1)*y]     + currentmap[x*(y - 1)]     + currentmap[x*(y + 1)]) / 4) + displace(iterations,counter_x0+x,counter_y0+y);
        }
    }

    /// Copy actual information to returned map
    for (unsigned int x = 0; x < finalwidth; x++)
    {
        for (unsigned int y = 0; y < finalheight; y++)
        {
            finalmap[x*y] = currentmap[(x+xoff)*(y+yoff)];

        }
    }

    return finalmap;
}

/// Random function to offset
double displace(unsigned int  iterations, int x, int y)
{
    return (((PRH(iterations,x,y) - 0.5)*2)) / (iterations+1);
}

/// Get maximum deviations
double getMaxDeviation(unsigned int iterations)
{
    double dev = 0.5 / (iterations+1);
    if (iterations <= 0) return dev;
    return getMaxDeviation(iterations-1) + dev;
}

///This function returns the same result for given values but should be somewhat random.
double PRH(unsigned iterations, int x, int y)
{
    unsigned long long hash;
    x &= 0xFFF;
    y &= 0xFFF;
    iterations &= 0xFF;
    hash = (iterations << 24);
    hash |= (y << 12);
    hash |= x;
    unsigned long long rem = hash & 3;
    unsigned long long h = hash;

    switch (rem)
    {
    case 3:
        hash += h;
        hash ^= hash << 32;
        hash ^= h << 36;
        hash += hash >> 22;
        break;
    case 2:
        hash += h;
        hash ^= hash << 22;
        hash += hash >> 34;
        break;
    case 1:
        hash += h;
        hash ^= hash << 20;
        hash += hash >> 2;
    }
    hash ^= hash << 6;
    hash += hash >> 10;
    hash ^= hash << 8;
    hash += hash >> 34;
    hash ^= hash << 50;
    hash += hash >> 12;

    return (hash & 0xFFFF) / static_cast<double>(0xFFFF);
}


void SaveTerrFile(const double * image)
{
    png::image< png::rgb_pixel > newimage(1024, 1024);


    for (unsigned int y = 0; y < newimage.get_width(); ++y)
    {
        for (unsigned int x = 0; x < newimage.get_height(); ++x)
        {
            int col=(int)(image[x*y]+1)*255;
            newimage[y][x] = png::rgb_pixel(col,col,col);
            // non-checking equivalent of image.set_pixel(x, y, ...);
        }
    }

    newimage.write("rgb.png");
}
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:26 UTC | #2

Non-Working revised for the 1d array

[code]///Headers
#include <vector>
#include <cstdio>
#include <cmath>
#include <iostream>

#include <stdio.h>
#include <stdlib.h>

#include <png++/png.hpp>
#include <png++/image.hpp>
#include <png++/rgb_pixel.hpp>



using namespace std;

/// Terraub Functions
double * getFieldSquareTerrain(int x0,int y0, int x1, int y1, unsigned int iterations);
double displace(unsigned int iterations,int x, int y);
double getMaxDeviation(unsigned int iterations);
double PRH(unsigned iterations, int x, int y);
double * getFieldDiamondSquaredMap(int x, int y, int width, int height, unsigned int iterations);

//Size of the grid to generate
//This must be 2^n+1 (e.g. 257)
const int DATA_SIZE = 1024;

void SaveTerrFile(const double * image);

/// Main function
int main()
{
    /// Define Settings
    int width=1024;
    int height=1024;
    int iterations=12;
    int x=0;
    int y=0;

    // allocate memory
    double * map=new double[width*height];

    map=getFieldDiamondSquaredMap(x,y,width,height,iterations);

    SaveTerrFile(map);

    return 1;
}

double * getFieldDiamondSquaredMap(int x, int y, int width, int height, unsigned int iterations)
{
    /// Allocate memory for final mapdouble
    double * map = new double[width*height];

    map = getFieldSquareTerrain(x, y, x+width, y+height, iterations);

    double maxdeviation = getMaxDeviation(iterations);

    for (unsigned int x = 0; x < width; x++)
    {
        for (unsigned int  y = 0; y < height; y++)
        {
            map[x+(y*width)] = map[x+(y*width)] / maxdeviation;
        }
    }

    return map;
}

double * getFieldSquareTerrain(int x0, int y0, int x1, int y1, unsigned int iterations)
{
    /// Define final height and width
    int finalwidth  = x1 - x0;
    int finalheight = y1 - y0;

    /// Allocate memory for final map
    double * finalmap = new double[finalwidth*finalheight];

    /// Test iteration
    if (iterations == 0)
    {
        for (unsigned int x = 0; x < finalwidth; x++)
        {
            for (unsigned int y = 0; y < finalheight; y++)
            {
                finalmap[x+(y*finalwidth)] =  displace(iterations,x0+x,y0+y) ;
            }
            return finalmap;
        }
    }

    /// Define ceil and floor
    int upper_x0=floor(x0/2) - 1;
    int upper_y0=floor(y0/2) - 1;
    int upper_x1=ceil(x1/2)+1;
    int upper_y1=ceil(y1/2)+1;

    /// Define upper height and width for upper maps
    int upper_xwidth= upper_x1-upper_x0;
    int upper_yheight= upper_y1-upper_y0;

    /// Allocate memory for upper map width and height
    double * uppermap = new double[upper_xwidth*upper_yheight];

    /// Pass another iteration
    uppermap = getFieldSquareTerrain(upper_x0, upper_y0, upper_x1, upper_y1, iterations-1);

    /// Define counter height and width
    int counter_x0= upper_x0 * 2;
    int counter_y0= upper_y0 * 2;

    int counter_width = upper_xwidth*2-1;
    int counter_height = upper_yheight*2-1;

    /// Allocate memory for currentmap using counter height and width
    double * currentmap = new double[counter_width*counter_height];

    /// Copy information to double map
    for (unsigned int x = 0; x < upper_xwidth; x++)
    {
        for (unsigned int y = 0; y< upper_yheight; y++)
        {
            currentmap[(x*2)+((y*counter_width)*2)] = uppermap[x+(y*upper_xwidth)];
        }
    }

    /// Define offset
    int xoff = x0 - counter_x0;
    int yoff = y0 - counter_y0;

    /// Use a diamond mehod algorithm
    for (unsigned int x = 1; x < counter_width-1; x += 2)
    {
        for (unsigned int y = 1; y < counter_height-1; y += 2)
        {
            currentmap[x+(y*counter_width)] = ((currentmap[(x - 1)+((y-1)*counter_width)] + currentmap[(x - 1)+((y+1)*counter_width)] + currentmap[(x + 1)+((y-1)*counter_width)] + currentmap[(x + 1)+((y+1)*counter_width)]) / 4) + displace(iterations,counter_x0+x,counter_y0+y);
        }
    }
    for (unsigned int x = 1; x < counter_width-1; x += 2)
    {
        for (unsigned int y = 2; y < counter_height-1; y += 2)
        {
            currentmap[x+(y*counter_width)] = ((currentmap[(x - 1)+(y*counter_width)]     + currentmap[(x + 1)+(y*counter_width)]     + currentmap[x+((y-1)*counter_width)]     + currentmap[x+((y+1)*counter_width)]) / 4) + displace(iterations,counter_x0+x,counter_y0+y);
        }
    }
    for (unsigned int x = 2; x < counter_width-1; x += 2)
    {
        for (unsigned int y = 1; y < counter_height-1; y += 2)
        {
            currentmap[x+(y*counter_width)] = ((currentmap[(x - 1)+(y*counter_width)]     + currentmap[(x + 1)+(y*counter_width)]     + currentmap[x+((y-1)*counter_width)]     + currentmap[x+((y+1)*counter_width) ]) / 4) + displace(iterations,counter_x0+x,counter_y0+y);
        }
    }

    /// Copy actual information to returned map
    for (unsigned int x = 0; x < finalwidth; x++)
    {
        for (unsigned int y = 0; y < finalheight; y++)
        {
            finalmap[x+(y*finalwidth)] = currentmap[(x+xoff)+((y+yoff)*counter_width)];

        }
    }

    return finalmap;
}

/// Random function to offset
double displace(unsigned int  iterations, int x, int y)
{
    return (((PRH(iterations,x,y) - 0.5)*2)) / (iterations+1);
}

/// Get maximum deviations
double getMaxDeviation(unsigned int iterations)
{
    double dev = 0.5 / (iterations+1);
    if (iterations <= 0) return dev;
    return getMaxDeviation(iterations-1) + dev;
}

///This function returns the same result for given values but should be somewhat random.
double PRH(unsigned iterations, int x, int y)
{
    unsigned long long hash;
    x &= 0xFFF;
    y &= 0xFFF;
    iterations &= 0xFF;
    hash = (iterations << 24);
    hash |= (y << 12);
    hash |= x;
    unsigned long long rem = hash & 3;
    unsigned long long h = hash;

    switch (rem)
    {
    case 3:
        hash += h;
        hash ^= hash << 32;
        hash ^= h << 36;
        hash += hash >> 22;
        break;
    case 2:
        hash += h;
        hash ^= hash << 22;
        hash += hash >> 34;
        break;
    case 1:
        hash += h;
        hash ^= hash << 20;
        hash += hash >> 2;
    }
    hash ^= hash << 6;
    hash += hash >> 10;
    hash ^= hash << 8;
    hash += hash >> 34;
    hash ^= hash << 50;
    hash += hash >> 12;

    return (hash & 0xFFFF) / static_cast<double>(0xFFFF);
}


void SaveTerrFile(const double * image)
{
    png::image< png::rgb_pixel > newimage(1024, 1024);


    for (unsigned int y = 0; y < newimage.get_width(); ++y)
    {
        for (unsigned int x = 0; x < newimage.get_height(); ++x)
        {
            int col=(int)(image[x+(y*newimage.get_width())]+1)*255;
            newimage[y][x] = png::rgb_pixel(col,col,col);
            // non-checking equivalent of image.set_pixel(x, y, ...);
        }
    }

    newimage.write("rgb.png");
}

[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:26 UTC | #3

This code test resulted in. The image before additional processing and saving to disk in a png.

0
-0.000926858
-8.59313e-05
0.000740951
-0.00112015
-0.00146794
0.000344809
1.85939e-05
-0.000501624
0.000191158
[code]
void SaveTerrFile(const double * image)
{
    png::image< png::rgb_pixel > newimage(1024, 1024);


    cout << "\r\n" << image[0];
    cout << "\r\n" << image[1];
    cout << "\r\n" << image[2];
    cout << "\r\n" << image[3];
    cout << "\r\n" << image[4];
    cout << "\r\n" << image[5];
    cout << "\r\n" << image[6];
    cout << "\r\n" << image[7];
    cout << "\r\n" << image[8];
    cout << "\r\n" << image[9];


    for (unsigned int y = 0; y < newimage.get_width(); ++y)
    {
        for (unsigned int x = 0; x < newimage.get_height(); ++x)
        {
            int col=(int)(image[x+(y*newimage.get_width())]+.1)*255;
            newimage[y][x] = png::rgb_pixel(col,col,col);
            // non-checking equivalent of image.set_pixel(x, y, ...);
        }
    }

    newimage.write("rgb.png");
}
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:26 UTC | #4

Current Code (Still little bug - [tinypic.com/r/oistxi/8](http://tinypic.com/r/oistxi/8))

Close but still. Argh :-/

[code]///Headers
#include <vector>
#include <cstdio>
#include <cmath>
#include <iostream>

#include <stdio.h>
#include <stdlib.h>

#include <png++/png.hpp>
#include <png++/image.hpp>
#include <png++/rgb_pixel.hpp>

using namespace std;

/// Terraub Functions
double * getFieldSquareTerrain(int x0,int y0, int x1, int y1, double iterations);
double displace(double iterations,int x, int y);
double getMaxDeviation(double iterations);
double PRH(unsigned iterations, int x, int y);
double * getFieldDiamondSquaredMap(int x, int y, int width, int height, double iterations);

//Size of the grid to generate
//This must be 2^n+1 (e.g. 257)
const int DATA_SIZE = 1024;

void SaveTerrFile(const double * image);

/// Main function
int main()
{
    /// Define Settings
    int width=1024;
    int height=1024;
    double iterations=12.0f;
    int x=0;
    int y=0;

    // allocate memory
    double * map=new double[width*height];

    map=getFieldDiamondSquaredMap(x,y,width,height,iterations);

    SaveTerrFile(map);

    return 1;
}

double * getFieldDiamondSquaredMap(int x, int y, int width, int height, double iterations)
{
    /// Allocate memory for final mapdouble
    double * map = new double[width*height];

    map = getFieldSquareTerrain(x, y, x+width, y+height, iterations);

    double maxdeviation = getMaxDeviation(iterations);

    for (unsigned int x = 0; x < width; x++)
    {
        for (unsigned int  y = 0; y < height; y++)
        {
            map[x+(y*width)] = map[x+(y*width)] / maxdeviation;
        }
    }

    return map;
}

double * getFieldSquareTerrain(int x0, int y0, int x1, int y1, double iterations)
{
    /// Define final height and width
    int finalwidth  = x1 - x0;
    int finalheight = y1 - y0;

    /// Allocate memory for final map
    double * finalmap = new double[finalwidth*finalheight];

    /// Test iteration
    if (iterations == 0)
    {
        for (unsigned int x = 0; x < finalwidth; x++)
        {
            for (unsigned int y = 0; y < finalheight; y++)
            {
                finalmap[x+(y*finalwidth)] =  displace(iterations,x0+x,y0+y) ;
            }
            return finalmap;
        }
    }

    /// Define ceil and floor
    int upper_x0=floor(x0/2) - 1;
    int upper_y0=floor(y0/2) - 1;
    int upper_x1=ceil(x1/2)+1;
    int upper_y1=ceil(y1/2)+1;

    /// Define upper height and width for upper maps
    int upper_xwidth= upper_x1-upper_x0;
    int upper_yheight= upper_y1-upper_y0;

    /// Allocate memory for upper map width and height
    double * uppermap = new double[upper_xwidth*upper_yheight];

    /// Pass another iteration
    uppermap = getFieldSquareTerrain(upper_x0, upper_y0, upper_x1, upper_y1, iterations-1);

    /// Define counter height and width
    int counter_x0= upper_x0 * 2;
    int counter_y0= upper_y0 * 2;

    int counter_width = upper_xwidth*2-1;
    int counter_height = upper_yheight*2-1;

    /// Allocate memory for currentmap using counter height and width
    double * currentmap = new double[counter_width*counter_height];

    /// Copy information to double map
    for (unsigned int x = 0; x < upper_xwidth; x++)
    {
        for (unsigned int y = 0; y< upper_yheight; y++)
        {
            currentmap[(x*2)+((y*counter_width)*2)] = uppermap[x+(y*upper_xwidth)];
        }
    }

    /// Define offset
    int xoff = x0 - counter_x0;
    int yoff = y0 - counter_y0;

    /// Use a diamond mehod algorithm
    for (unsigned int x = 1; x < counter_width-1; x += 2)
    {
        for (unsigned int y = 1; y < counter_height-1; y += 2)
        {
            currentmap[x+(y*counter_width)] = ((currentmap[(x - 1)+((y-1)*counter_width)] + currentmap[(x - 1)+((y+1)*counter_width)] + currentmap[(x + 1)+((y-1)*counter_width)] + currentmap[(x + 1)+((y+1)*counter_width)]) / 4) + displace(iterations,counter_x0+x,counter_y0+y);
        }
    }
    for (unsigned int x = 1; x < counter_width-1; x += 2)
    {
        for (unsigned int y = 2; y < counter_height-1; y += 2)
        {
            currentmap[x+(y*counter_width)] = ((currentmap[(x - 1)+(y*counter_width)]     + currentmap[(x + 1)+(y*counter_width)]     + currentmap[x+((y-1)*counter_width)]     + currentmap[x+((y+1)*counter_width)]) / 4) + displace(iterations,counter_x0+x,counter_y0+y);
        }
    }
    for (unsigned int x = 2; x < counter_width-1; x += 2)
    {
        for (unsigned int y = 1; y < counter_height-1; y += 2)
        {
            currentmap[x+(y*counter_width)] = ((currentmap[(x - 1)+(y*counter_width)]     + currentmap[(x + 1)+(y*counter_width)]     + currentmap[x+((y-1)*counter_width)]     + currentmap[x+((y+1)*counter_width) ]) / 4) + displace(iterations,counter_x0+x,counter_y0+y);
        }
    }

    /// Copy actual information to returned map
    for (unsigned int x = 0; x < finalwidth; x++)
    {
        for (unsigned int y = 0; y < finalheight; y++)
        {
            finalmap[x+(y*finalwidth)] = currentmap[(x+xoff)+((y+yoff)*counter_width)];

        }
    }

    return finalmap;
}

/// Random function to offset
double displace(double iterations,int x, int y)
{
    return (((PRH(iterations,x,y) - 0.5)*2)) / (iterations+1);
}

/// Get maximum deviations
double getMaxDeviation(double iterations)
{
    double dev = 0.5 / (iterations+1);
    if (iterations <= 0) return dev;
    return getMaxDeviation(iterations-1) + dev;
}

///This function returns the same result for given values but should be somewhat random.
double PRH(unsigned iterations, int x, int y)
{
    unsigned long long hash;
    x &= 0xFFF;
    y &= 0xFFF;
    iterations &= 0xFF;
    hash = (iterations << 24);
    hash |= (y << 12);
    hash |= x;
    unsigned long long rem = hash & 3;
    unsigned long long h = hash;

    switch (rem)
    {
    case 3:
        hash += h;
        hash ^= hash << 32;
        hash ^= h << 36;
        hash += hash >> 22;
        break;
    case 2:
        hash += h;
        hash ^= hash << 22;
        hash += hash >> 34;
        break;
    case 1:
        hash += h;
        hash ^= hash << 20;
        hash += hash >> 2;
    }
    hash ^= hash << 6;
    hash += hash >> 10;
    hash ^= hash << 8;
    hash += hash >> 34;
    hash ^= hash << 50;
    hash += hash >> 12;

    return (hash & 0xFFFF) / static_cast<double>(0xFFFF);
}


void SaveTerrFile(const double * image)
{
    png::image< png::rgb_pixel > newimage(1024, 1024);



    for (unsigned int y = 0; y < newimage.get_width(); ++y)
    {
        for (unsigned int x = 0; x < newimage.get_height(); ++x)
        {
            int col=(int)(image[x+(y*newimage.get_width())]+1)*255;
            newimage[y][x] = png::rgb_pixel(col,col,col);
            // non-checking equivalent of image.set_pixel(x, y, ...);
        }
    }

    newimage.write("rgb.png");
}

    [/code]

-------------------------

hdunderscore | 2017-01-02 01:00:26 UTC | #5

You left out a few functions from the last snippet.

-------------------------

vivienneanthony | 2017-01-02 01:00:26 UTC | #6

[quote="hd_"]You left out a few functions from the last snippet.[/quote]

Thanks. I placed the whole code.

-------------------------

hdunderscore | 2017-01-02 01:00:26 UTC | #7

The last thing I can think of is this:
[code]double PRH(unsigned iterations, int x, int y)[/code]

Probably should be double too.

Edit:

Nevermind, it should probably be a signed int:
[stackoverflow.com/questions/1822 ... you-use-it](http://stackoverflow.com/questions/1822350/what-is-the-javascript-operator-and-how-do-you-use-it)

In Javascript, numbers are usually doubles but when you bit shift them they are treated as signed ints. In JavaScript, there is a special operator for unsigned bit shift but the code supplied only uses the signed bit shift, so you probably want to use signed int on PRH.

-------------------------

vivienneanthony | 2017-01-02 01:00:26 UTC | #8

[quote="hd_"]The last thing I can think of is this:
[code]double PRH(unsigned iterations, int x, int y)[/code]

Probably should be double too.[/quote]

Changing that causes a  error.

[code]/media/home2/vivienne/testingc++/HeightWidth.cpp||In function ?double PRH(double, int, int)?:|
/media/home2/vivienne/testingc++/HeightWidth.cpp|186|error: invalid operands of types ?double? and ?int? to binary ?operator&?|
/media/home2/vivienne/testingc++/HeightWidth.cpp|186|error:   in evaluation of ?operator&=(double, int)?|
/media/home2/vivienne/testingc++/HeightWidth.cpp|187|error: invalid operands of types ?double? and ?int? to binary ?operator<<?|[/code]

in

[code]
    iterations &= 0xFF;
    hash = (iterations << 24);[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:27 UTC | #9

This is a modification. I converted of final image to range to 0 to 1, then muiltiplied that to 255. Which gets better results but.

I rather the final image to be 0 and above only, no negative before saving without extra processing. I'm assuming the floor and ceil has to be changed??? This would allow infinite terrain a lot better. If it went from 0 to 1(or above)  without disturbing produced double data.

The extra c++ library I used is libpng.

Image produced from this method [tinypic.com/r/2rr2cqt/8](http://tinypic.com/r/2rr2cqt/8)

[code]///Headers
#include <vector>
#include <cstdio>
#include <cmath>
#include <iostream>

#include <stdio.h>
#include <stdlib.h>

#include <png++/png.hpp>
#include <png++/image.hpp>
#include <png++/rgb_pixel.hpp>

using namespace std;

/// Terraub Functions
double * getFieldSquareTerrain(int x0,int y0, int x1, int y1, double iterations);
double displace(double iterations,int x, int y);
double getMaxDeviation(double iterations);
double PRH(unsigned iterations, int x, int y);
double * getFieldDiamondSquaredMap(int x, int y, int width, int height, double iterations);

//Size of the grid to generate
//This must be 2^n+1 (e.g. 257)
const int DATA_SIZE = 1024;

void SaveTerrFile(const double * image);

/// Main function
int main()
{
    /// Define Settings
    int width=1024;
    int height=1024;
    double iterations=52.0f;
    int x=0;
    int y=0;

    // allocate memory
    double * map=new double[width*height];

    map=getFieldDiamondSquaredMap(x,y,width,height,iterations);

    /// Set maxY and minY to 0.0f
    double maxY = map[2];
    double minY = map[2];

    for (int x = 0; x<width; x++)
    {
        for(int y = 0; y<height; y++)
        {
            if ((double)map[x+(y*width)] > maxY)
            {
                maxY = map[x+(y*width)];
            }
            if ((double)map[x+(y*width)] < minY)
            {
                minY = map[x+(y*width)];
            }
        }
    }

    /// Calculate height_ from 0 to 1
    for(int x=0; x < width; x++)
    {
        for(int y=0; y < height; y++)
        {
            //change range to 0..1
            map[x+(y*width)]  = (map[x+(y*width)] - minY) / (maxY - minY);


        }
    }

    SaveTerrFile(map);

    return 1;
}

double * getFieldDiamondSquaredMap(int x, int y, int width, int height, double iterations)
{
    /// Allocate memory for final mapdouble
    double * map = new double[width*height];

    map = getFieldSquareTerrain(x, y, x+width, y+height, iterations);

    double maxdeviation = getMaxDeviation(iterations);

    for (unsigned int x = 0; x < width; x++)
    {
        for (unsigned int  y = 0; y < height; y++)
        {
            map[x+(y*width)] = map[x+(y*width)] / maxdeviation;

        }
    }

    return map;
}

double * getFieldSquareTerrain(int x0, int y0, int x1, int y1, double iterations)
{
    /// Define final height and width
    int finalwidth  = x1 - x0;
    int finalheight = y1 - y0;

    /// Allocate memory for final map
    double * finalmap = new double[finalwidth*finalheight];

    /// Test iteration
    if (iterations == 0)
    {
        for (unsigned int x = 0; x < finalwidth; x++)
        {
            for (unsigned int y = 0; y < finalheight; y++)
            {
                finalmap[x+(y*finalwidth)] =  displace(iterations,x0+x,y0+y) ;
            }
            return finalmap;
        }
    }

    /// Define ceil and floor
    int upper_x0=floor(x0/2) - 1;
    int upper_y0=floor(y0/2) - 1;
    int upper_x1=ceil(x1/2)+1;
    int upper_y1=ceil(y1/2)+1;

    /// Define upper height and width for upper maps
    int upper_xwidth= upper_x1-upper_x0;
    int upper_yheight= upper_y1-upper_y0;

    /// Allocate memory for upper map width and height
    double * uppermap = new double[upper_xwidth*upper_yheight];

    /// Pass another iteration
    uppermap = getFieldSquareTerrain(upper_x0, upper_y0, upper_x1, upper_y1, iterations-1);

    /// Define counter height and width
    int counter_x0= upper_x0 * 2;
    int counter_y0= upper_y0 * 2;

    int counter_width = upper_xwidth*2-1;
    int counter_height = upper_yheight*2-1;

    /// Allocate memory for currentmap using counter height and width
    double * currentmap = new double[counter_width*counter_height];

    /// Copy information to double map
    for (unsigned int x = 0; x < upper_xwidth; x++)
    {
        for (unsigned int y = 0; y< upper_yheight; y++)
        {
            currentmap[(x*2)+((y*counter_width)*2)] = uppermap[x+(y*upper_xwidth)];
        }
    }

    /// Define offset
    int xoff = x0 - counter_x0;
    int yoff = y0 - counter_y0;

    /// Use a diamond mehod algorithm
    for (unsigned int x = 1; x < counter_width-1; x += 2)
    {
        for (unsigned int y = 1; y < counter_height-1; y += 2)
        {
            currentmap[x+(y*counter_width)] = ((currentmap[(x - 1)+((y-1)*counter_width)] + currentmap[(x - 1)+((y+1)*counter_width)] + currentmap[(x + 1)+((y-1)*counter_width)] + currentmap[(x + 1)+((y+1)*counter_width)]) / 4) + displace(iterations,counter_x0+x,counter_y0+y);
        }
    }
    for (unsigned int x = 1; x < counter_width-1; x += 2)
    {
        for (unsigned int y = 2; y < counter_height-1; y += 2)
        {
            currentmap[x+(y*counter_width)] = ((currentmap[(x - 1)+(y*counter_width)]     + currentmap[(x + 1)+(y*counter_width)]     + currentmap[x+((y-1)*counter_width)]     + currentmap[x+((y+1)*counter_width)]) / 4) + displace(iterations,counter_x0+x,counter_y0+y);
        }
    }
    for (unsigned int x = 2; x < counter_width-1; x += 2)
    {
        for (unsigned int y = 1; y < counter_height-1; y += 2)
        {
            currentmap[x+(y*counter_width)] = ((currentmap[(x - 1)+(y*counter_width)]     + currentmap[(x + 1)+(y*counter_width)]     + currentmap[x+((y-1)*counter_width)]     + currentmap[x+((y+1)*counter_width) ]) / 4) + displace(iterations,counter_x0+x,counter_y0+y);
        }
    }

    /// Copy actual information to returned map
    for (unsigned int x = 0; x < finalwidth; x++)
    {
        for (unsigned int y = 0; y < finalheight; y++)
        {
            finalmap[x+(y*finalwidth)] = currentmap[(x+xoff)+((y+yoff)*counter_width)];

        }
    }

    /// Clear Memory
    delete currentmap;
    delete uppermap;

    return finalmap;
}

/// Random function to offset
double displace(double iterations,int x, int y)
{
    return (((PRH(iterations,x,y) - 0.5)*2)) / (iterations+1);
}

/// Get maximum deviations
double getMaxDeviation(double iterations)
{
    double dev = 0.5 / (iterations+1);
    if (iterations <= 0) return dev;
    return getMaxDeviation(iterations-1) + dev;
}

///This function returns the same result for given values but should be somewhat random.
double PRH(unsigned iterations, int x, int y)
{
    unsigned long long hash;
    x &= 0xFFF;
    y &= 0xFFF;
    iterations &= 0xFF;
    hash = (iterations << 24);
    hash |= (y << 12);
    hash |= x;
    unsigned long long rem = hash & 3;
    unsigned long long h = hash;

    switch (rem)
    {
    case 3:
        hash += h;
        hash ^= hash << 32;
        hash ^= h << 36;
        hash += hash >> 22;
        break;
    case 2:
        hash += h;
        hash ^= hash << 22;
        hash += hash >> 34;
        break;
    case 1:
        hash += h;
        hash ^= hash << 20;
        hash += hash >> 2;
    }
    hash ^= hash << 6;
    hash += hash >> 10;
    hash ^= hash << 8;
    hash += hash >> 34;
    hash ^= hash << 50;
    hash += hash >> 12;

    return (hash & 0xFFFF) / static_cast<double>(0xFFFF);
}

void SaveTerrFile(const double * image)
{
    png::image< png::rgb_pixel > newimage(1024, 1024);

    for (unsigned int y = 0; y < newimage.get_width(); ++y)
    {
        for (unsigned int x = 0; x < newimage.get_height(); ++x)
        {
            int col = int(image[x+(y*newimage.get_width())]*255);
            newimage[y][x] = png::rgb_pixel(col,col,col);
            // non-checking equivalent of image.set_pixel(x, y, ...);
        }
    }

    newimage.write("rgb.png");
}
[/code]

-------------------------

