vivienneanthony | 2017-01-02 01:03:30 UTC | #1

Hey,

I took a crack at converting some JAVA procedural method to c++. I'm getting the following compile error.

[code]/media/home2/vivienne/testingc++/olsen2dwip.cpp||In member function ?int* OlsenNoise2D::olsennoise(int, int, int, int)?:|
/media/home2/vivienne/testingc++/olsen2dwip.cpp|79|error: no matching function for call to ?OlsenNoise2D::hashrandom(int, int, int&)?|
/media/home2/vivienne/testingc++/olsen2dwip.cpp|79|note: candidate is:|
/media/home2/vivienne/testingc++/olsen2dwip.cpp|17|note: int OlsenNoise2D::hashrandom(int*)|
/media/home2/vivienne/testingc++/olsen2dwip.cpp|17|note:   candidate expects 1 argument, 3 provided|
/media/home2/vivienne/testingc++/olsen2dwip.cpp||In member function ?int OlsenNoise2D::hashrandom(int*)?:|
/media/home2/vivienne/testingc++/olsen2dwip.cpp|144|error: request for member ?size? in ?elements?, which is of non-class type ?int*?|
/media/home2/vivienne/testingc++/olsen2dwip.cpp|147|error: ?hash? cannot be used as a function|
||=== Build finished: 6 errors, 0 warnings ===|
[/code]


The code is at PasteBin is [pastebin.com/gh6P5zf3](http://pastebin.com/gh6P5zf3)

[code]
int * OlsenNoise2D::olsennoise(int x, int y, int width, int height)
{
    int maxiterations = 7;
    int cx, cy;
    int cxh, cyh;
    int cwidth, cheight;
    int xoff, yoff;
    int nwidth, nheight;
    int nx, ny;
    int nxh, nyh;
    int m=0;
    int n=0;
    int * field = NULL;

    for (int iteration = 0; iteration < maxiterations; iteration++)
    {
        nx = x;
        ny = y;

        nxh = x + width;
        nyh = y + width;

        n = maxiterations - iteration;

        for (int i = 1; i < n; i++)
        {
            nx = (nx / 2) - 1;
            ny = (ny / 2) - 1;
            nxh = 1 -(-nxh/2);
            nyh = 1 -(-nyh/2);
        }

        xoff = -2*((nx/2)) + nx + 1;
        yoff = -2*((ny/2)) + ny + 1;

        cx = (nx / 2) - 1;
        cy = (ny / 2) - 1;
        cxh = 1 -(-nxh/2);
        cyh = 1 -(-nyh/2);

        nwidth = nxh - nx;
        nheight = nyh - ny;

        cwidth = cxh - cx;
        cheight = cyh - cy;


        /// Field
        m=cwidth;
        n=cheight;

        if (field == NULL) field = new int[m*(n*m)];

        for (int j = 0; j < m; j++)
        {
            for (int k = 0; k < n; k++)
            {
                field[j+(k*m)] += (hashrandom(cx + j, cy + k, iteration) & (1 << (7 - iteration)));
            }
        }

        /// Up sampled
        //m=field.length * 2;
        //n=field[0].length * 2;
        m=cwidth*2;
        n=cheight*2;


        int * upsampled = new int[m*(n*m)];

        for (int j = 0; j < m; j++)
        {
            for (int k = 0; k < n; k++)
            {
                upsampled[j+(k*m)] = field[(j / 2)+((k / 2)*cwidth)];
            }
        }
        field = upsampled;

        /// Blur field
        //int m=field.length - 2;
        //int n=field[0].length - 2;
        m=cwidth-2;
        n=cheight-2;

        int * blurfield = new int[m*(n*m)];

        for (int j = 0; j < m; j++)
        {
            for (int k = 0;  k < n; k++)
            {
                for (int h = 0; h < 9; h++)
                {
                    blurfield[j+(k*m)] += field[(j + (h % 3))+((k + (h / 3))*(cheight*2))];
                }
                blurfield[j+(k*m)] /= 9;
            }
        }
        field = blurfield;

        /// Trim field
        m=nwidth;
        n=nheight;

        int * trimfield = new int[m*(n*m)];

        for (int j = 0;j < m; j++)
        {
            for (int k = 0; k < n; k++)
            {
                trimfield[j+(k*m)] = field[(j + xoff)+((k + yoff)*(nheight-2))];
            }
        }
        field = trimfield;
    }
    return field;
}

int OlsenNoise2D::hashrandom(int elements[])
{
    long hash = 0;

    for (int i = 0; i < elements.size; i++)
    {
        hash ^= elements[i];
        hash = hash(hash);
    }
    return (int) hash;
};

long OlsenNoise2D::hash(long v)
{
    long hash = v;
    long h = hash;

    switch ((int) hash & 3)
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
    return hash;
};


int main()
{

    return 1;
}[/code]

-------------------------

vivienneanthony | 2017-01-02 01:03:30 UTC | #2

Revised

[code]/*
 * @author Tat
 * c++ rewrite vivienne (WIP)
 */

#include <iostream>
#include <vector>

#include <stdio.h>
#include <stdlib.h>
#include <png++/png.hpp>

using namespace std;

void SaveTerrFile(const int * image, int size);


class OlsenNoise2D
{

public:
   int * olsennoise(int x, int y, int width, int height);

private:
    int hashrandom(std::vector<int> elements);
    long hash(long v);

};

int * OlsenNoise2D::olsennoise(int x, int y, int width, int height)
{
    int maxiterations = 7;
    int cx, cy;
    int cxh, cyh;
    int cwidth, cheight;
    int xoff, yoff;
    int nwidth, nheight;
    int nx, ny;
    int nxh, nyh;
    int m=0;
    int n=0;
    int * field = NULL;

    for (int iteration = 0; iteration < maxiterations; iteration++)
    {
        nx = x;
        ny = y;

        nxh = x + width;
        nyh = y + width;

        n = maxiterations - iteration;

        for (int i = 1; i < n; i++)
        {
            nx = (nx / 2) - 1;
            ny = (ny / 2) - 1;
            nxh = 1 -(-nxh/2);
            nyh = 1 -(-nyh/2);
        }

        xoff = -2*((nx/2)) + nx + 1;
        yoff = -2*((ny/2)) + ny + 1;

        cx = (nx / 2) - 1;
        cy = (ny / 2) - 1;
        cxh = 1 -(-nxh/2);
        cyh = 1 -(-nyh/2);

        nwidth = nxh - nx;
        nheight = nyh - ny;

        cwidth = cxh - cx;
        cheight = cyh - cy;


        /// Field
        m=cwidth;
        n=cheight;

        if (field == NULL) field = new int[m*(n*m)];

        for (int j = 0; j < m; j++)
        {
            for (int k = 0; k < n; k++)
            {
                field[j+(k*m)] += (hashrandom({cx + j, cy + k, iteration}) & (1 << (7 - iteration)));
            }
        }

        /// Up sampled
        //m=field.length * 2;
        //n=field[0].length * 2;
        m=cwidth*2;
        n=cheight*2;

        int * upsampled = new int[m*(n*m)];

        for (int j = 0; j < m; j++)
        {
            for (int k = 0; k < n; k++)
            {
                upsampled[j+(k*m)] = field[(j / 2)+((k / 2)*cwidth)];
            }
        }
        field = upsampled;

        /// Blur field
        //int m=field.length - 2;
        //int n=field[0].length - 2;
        m=cwidth-2;
        n=cheight-2;

        int * blurfield = new int[m*(n*m)];

        for (int j = 0; j < m; j++)
        {
            for (int k = 0;  k < n; k++)
            {
                for (int h = 0; h < 9; h++)
                {
                    blurfield[j+(k*m)] += field[(j + (h % 3))+((k + (h / 3))*(cheight*2))];
                }
                blurfield[j+(k*m)] /= 9;
            }
        }
        field = blurfield;

        /// Trim field
        m=nwidth;
        n=nheight;

        int * trimfield = new int[m*(n*m)];

        for (int j = 0;j < m; j++)
        {
            for (int k = 0; k < n; k++)
            {
                trimfield[j+(k*m)] = field[(j + xoff)+((k + yoff)*(nheight-2))];
            }
        }
        field = trimfield;
    }
    return field;
}

int OlsenNoise2D::hashrandom(std::vector<int> elements)
{
    long hashcalc = 0;

    for (int i = 0; i < elements.size(); i++)
    {
        hashcalc ^= elements[i];
        hashcalc = hash(hashcalc);
    }
    return (int) hashcalc;
};

long OlsenNoise2D::hash(long v)
{
    long hash = v;
    long h = hash;

    switch ((int) hash & 3)
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
    return hash;
};


int main()
{
    /// Test
    int ImageSize=2049;

    int * imageInput = new int[ImageSize*ImageSize];

    /// Image
    OlsenNoise2D testingolsen;
    imageInput=testingolsen.olsennoise(0,0,ImageSize,ImageSize);


    SaveTerrFile(imageInput, ImageSize);

    return 1;
}


void SaveTerrFile(const int * image, int size)
{
    png::image< png::rgb_pixel > newimage(size, size);

    for (unsigned int y = 0; y < newimage.get_width(); ++y)
    {
        for (unsigned int x = 0; x < newimage.get_height(); ++x)
        {
            int col = int(image[x+(y*newimage.get_width())]*255);
            newimage[y][x] = png::rgb_pixel(col,col,col);
            // non-checking equivalent of image.set_pixel(x, y, ...);
        }
    }

    newimage.write("rgbOlsen.png");
}


[/code]

-------------------------

JTippetts | 2017-01-02 01:03:30 UTC | #3

The revision compiles, I take it? (It does for me, at least.)

In the original, the clue lies in the error message itself.
"error: no matching function for call to ?OlsenNoise2D::hashrandom(int, int, int&)"
This means that you are trying to call a function called hashrandom that takes two ints and a reference to a third int, but the only candidate function it can find that's called hashrandom expects an array of ints instead. Also, in C++, an array of ints is just a "dumb" sequential array of values, and not a "smart" array that includes a size() method. The solution (as you discovered) is to use a vector.

-------------------------

vivienneanthony | 2017-01-02 01:03:30 UTC | #4

[quote="JTippetts"]The revision compiles, I take it? (It does for me, at least.)

In the original, the clue lies in the error message itself.
"error: no matching function for call to ?OlsenNoise2D::hashrandom(int, int, int&)"
This means that you are trying to call a function called hashrandom that takes two ints and a reference to a third int, but the only candidate function it can find that's called hashrandom expects an array of ints instead. Also, in C++, an array of ints is just a "dumb" sequential array of values, and not a "smart" array that includes a size() method. The solution (as you discovered) is to use a vector.[/quote]

The whole thing is weird I think. Usually I translate  array[x][y] to a sequential difference of  array[x+(y+width)] like you said a sequence. The first for loop does fit thtat after looking at it.

Its like
field 0
field 01 
field 012 (set limit based on the previous level)

-------------------------

JTippetts | 2017-01-02 01:03:31 UTC | #5

One potential source of problems that I see by looking at the compile warnings is that in the hash() function you are using [b]long int[/b], but you are attempting to bitshift by large amounts such as 36 or 50. long is only guaranteed by the standard to be at least a 32-bit type, so on platforms where it is implemented as 32 bits (including Windows) all of your bits are going to be shifted out completely when you shift by more than 32. Likely what you want to use instead is a [b]long long int[/b] which is guaranteed to be at least 64 bits.

Also, you're going to leak memory like crazy. In your main, you allocate imageInput as an array sized 2049x2049, but then you immediately overwrite it with the return result of the olsennoise() function, leaving the chunk you had allocated hanging out there in limbo rather than being properly freed. In addition, inside olsennoise you allocate an array of ints using new, assign the allocated block to the field variable, later allocate another array and assign it to upsample, then assign that to field, leaving the previously allocated block hanging out in the wind. Then you allocate [i]another[/i] array, assign it to blurfield, then assign that to field: again, overwriting the previous address and leaving another allocated block in limbo. Then you do the same with a variable called trimfield. That's a whole lot of memory you're leaving allocated and twisting in the wind each time you call olsennoise(). You then return field, but nowhere in main is this returned array ever deleted. 

You have to remember that C++ [b]new[/b] doesn't work like Java [b]new[/b], in that you have to explicitly call [b]delete[/b] on anything you [b]new[/b] or it will leak.

Another problem is that in olsennoise you allocate memory for field, then in the following loop you modify the values of field using the += operator (adding values to what was already there) without ever initializing the values you allocated to 0. That's undefined behavior right there. It's possible that the allocated chunk is 0 already, but not certain, and you could in fact be adding values to garbage. C++ new doesn't automatically initialize non-class objects to 0.

-------------------------

vivienneanthony | 2017-01-02 01:03:31 UTC | #6

[quote="JTippetts"]One potential source of problems that I see by looking at the compile warnings is that in the hash() function you are using [b]long int[/b], but you are attempting to bitshift by large amounts such as 36 or 50. long is only guaranteed by the standard to be at least a 32-bit type, so on platforms where it is implemented as 32 bits (including Windows) all of your bits are going to be shifted out completely when you shift by more than 32. Likely what you want to use instead is a [b]long long int[/b] which is guaranteed to be at least 64 bits.

Also, you're going to leak memory like crazy. In your main, you allocate imageInput as an array sized 2049x2049, but then you immediately overwrite it with the return result of the olsennoise() function, leaving the chunk you had allocated hanging out there in limbo rather than being properly freed. In addition, inside olsennoise you allocate an array of ints using new, assign the allocated block to the field variable, later allocate another array and assign it to upsample, then assign that to field, leaving the previously allocated block hanging out in the wind. Then you allocate [i]another[/i] array, assign it to blurfield, then assign that to field: again, overwriting the previous address and leaving another allocated block in limbo. Then you do the same with a variable called trimfield. That's a whole lot of memory you're leaving allocated and twisting in the wind each time you call olsennoise(). You then return field, but nowhere in main is this returned array ever deleted. 

You have to remember that C++ [b]new[/b] doesn't work like Java [b]new[/b], in that you have to explicitly call [b]delete[/b] on anything you [b]new[/b] or it will leak.

Another problem is that in olsennoise you allocate memory for field, then in the following loop you modify the values of field using the += operator (adding values to what was already there) without ever initializing the values you allocated to 0. That's undefined behavior right there. It's possible that the allocated chunk is 0 already, but not certain, and you could in fact be adding values to garbage. C++ new doesn't automatically initialize non-class objects to 0.[/quote]

I'll look at the code today. It was a rough rough conversion. I'm going make the change. I have to figure out how it fully functions tho but the way the person has it shifting the memory is not typically a way I would do it.

-------------------------

JTippetts | 2017-01-02 01:03:31 UTC | #7

Well, bit-shifting is a common component of hashing in noise implementations like this. The idea of hashing is to take values in a sequence (such as the coordinate pairs iterating a grid) and convert them to something random-seeming yet deterministic: ie, the output looks random, but calling hash on a given coordinate always results in the same output each call.

I'm not sure I really understand the need for this algorithm. For generating a terrain, it seems needlessly convoluted, and allocates a whole lot of large memory chunks. (In your code, I see allocations of the form m*m*n which, if m and n are equal to 2049, comes out to a whopping 32GB for a 32-bit int array.)  I understand from skimming the guy's original blog post that it's supposed to filter better than Perlin noise, but if you're generating a terrain you're not filtering it anyway. Perlin noise can be evaluated in-place without the need for allocating huge workspace buffers, and can produce roughly comparable and eminently acceptable results.

-------------------------

vivienneanthony | 2017-01-02 01:03:32 UTC | #8

[quote="JTippetts"]Well, bit-shifting is a common component of hashing in noise implementations like this. The idea of hashing is to take values in a sequence (such as the coordinate pairs iterating a grid) and convert them to something random-seeming yet deterministic: ie, the output looks random, but calling hash on a given coordinate always results in the same output each call.

I'm not sure I really understand the need for this algorithm. For generating a terrain, it seems needlessly convoluted, and allocates a whole lot of large memory chunks. (In your code, I see allocations of the form m*m*n which, if m and n are equal to 2049, comes out to a whopping 32GB for a 32-bit int array.)  I understand from skimming the guy's original blog post that it's supposed to filter better than Perlin noise, but if you're generating a terrain you're not filtering it anyway. Perlin noise can be evaluated in-place without the need for allocating huge workspace buffers, and can produce roughly comparable and eminently acceptable results.[/quote]

That was a error on my part trying to figure out whats going on. The results to me isn't very acceptable. I'm picky.

Also diamond square method is another method but I haven't  find any good resource to allow offsetting. With STB I can choose a offset. This guys code I can choose a offset also.

I changed the code to this [pastebin.com/bkeSiXgb](http://pastebin.com/bkeSiXgb)

If I set the interation to 1.  The equivalent of this in a image. [imgur.com/BzDWARK](http://imgur.com/BzDWARK)

Now if I set it higher to 1, I get a segmentation fault which I think lays in this code and the length of elements vector

[code]  field[j+(k*m)] += (hashrandom( {cx + j, ((cy + k)*m), iteration}) & (1 << (7 - iteration)));[/code]

-------------------------

vivienneanthony | 2017-01-02 01:03:32 UTC | #9

Hi JTippett

This is the code I modified [pastebin.com/PBCzcH3Q](http://pastebin.com/PBCzcH3Q)

If I set the interations to 2. It creates [imgur.com/u4o8732](http://imgur.com/u4o8732)

So, I made the pointers and removed the allocated memory when need be.   The original code is [godsnotwheregodsnot.blogspot.com ... -java.html](http://godsnotwheregodsnot.blogspot.com/2014/09/olsen-noise-source-code-in-java.html)

I don't think I should be using memcpy that way I am. Usually I just reference a pointer or whatever.

Maybe you'll notice something. The speed of it is about 2 seconds when ran.  If done right, infinite terrain like [imgur.com/f2aanDf](http://imgur.com/f2aanDf) can be done.

Vivienne

-------------------------

vivienneanthony | 2017-01-02 01:03:32 UTC | #10

Current not working fully code

This is the code so far I converted to C++ (Olsen 2D)
[pastebin.com/qbgBL0Hq](http://pastebin.com/qbgBL0Hq)

This is the image produce
[imgur.com/nb2pMjP](http://imgur.com/nb2pMjP)

Original source code
[pastebin.com/gh6P5zf3](http://pastebin.com/gh6P5zf3)

Demo Online(You should see what it should produce at 5 interations)
[tatarize.nfshost.com/OlsenNoise.htm](http://tatarize.nfshost.com/OlsenNoise.htm)

-------------------------

vivienneanthony | 2017-01-02 01:03:34 UTC | #11

Hello,

Could someone take a look at this. I'm not sure what's wrong or a simple solution. The discussion between the original developer is here.

[godsnotwheregodsnot.blogspot.com ... noise.html](http://godsnotwheregodsnot.blogspot.com/2014/08/3d-olsen-noise.html)

The code is below. It works 90%. My goal is 100% plus throw in another 15%. 

A image produced is [imgur.com/P8EYbPn](http://imgur.com/P8EYbPn)

[code]/*
 * @author Tat
 * c++ rewrite vivienne (WIP)
 * verion .01
 */

#include <iostream>
#include <vector>

#include <stdio.h>
#include <stdlib.h>
#include <png++/png.hpp>

using namespace std;

void SaveTerrFile(const int * image, int size, char * filename);


class OlsenNoise2D
{

public:
    int * olsennoise(int x, int y, int width, int height);

private:
    int hashrandom(std::vector<long long int> elements);
    long long hash(long long v);

};

int * OlsenNoise2D::olsennoise(int x, int y, int width, int height)
{
    int maxiterations = 4;
    int cx, cy;
    int cxh, cyh;
    int cwidth, cheight;
    int xoff, yoff;
    int nwidth, nheight;
    int nx, ny;
    int nxh, nyh;
    int m=0;
    int n=0;
    int fieldwidth=0;
    int fieldheight=0;

    int * field = NULL;

    for (int iteration = 0; iteration < maxiterations; iteration++)
    {
        nx = x;
        ny = y;

        nxh = x + width;
        nyh = y + height;

        for (int i = 1,n = maxiterations - iteration; i < n; i++)
        {
            nx = (nx / 2) - 1;
            ny = (ny / 2) - 1;
            nxh = 1 -(-nxh/2);
            nyh = 1 -(-nyh/2);
        }

        xoff = -2*((nx/2)) + nx + 1;
        yoff = -2*((ny/2)) + ny + 1;

        cx = (nx / 2) - 1;
        cy = (ny / 2) - 1;
        cxh = 1 -(-nxh/2);
        cyh = 1 -(-nyh/2);

        nwidth = nxh - nx;
        nheight = nyh - ny;

        cwidth = cxh - cx;
        cheight = cyh - cy;

        /// rest
        fieldwidth=cwidth;
        fieldheight=cheight;

        /// Only happens once
        if (field==NULL)
        {
            /// allocate memory
            field = new int[height * width];

            /// blank value
            for (int x = 0; x < width; x++)
            {
                for (int y = 0; y < height; y++)
                {
                    field[x+(y*width)]=0;
                }
            }
        }

        /// First loop
        for (int j = 0, m=cwidth; j < m; j++)
        {
            for (int k = 0, n=cheight; k < n; k++)
            {
                field[j+(k*m)] += (hashrandom( {cx + j, cy + k, iteration}) & (1 << (7 - iteration)));
            }
        }

        /// Up sampled
        int * upsampled = new int[(fieldwidth*2)*(fieldheight*2)];
        long int upsampledsize=(fieldwidth*2)*(fieldheight*2);

        for (int j = 0, m=fieldwidth*2; j < m; j++)
        {
            for (int k = 0,n=fieldheight*2; k < n; k++)
            {
                upsampled[j+(k*m)] = field[(j / 2)+((k / 2)*fieldwidth)];
            }
        }

        memmove((void *)field,(void *) upsampled,upsampledsize*sizeof(int));
        delete upsampled;

        /// rest
        fieldwidth=fieldwidth*2;
        fieldheight=fieldheight*2;

        /// Blur field
        int * blurfield =new int[(fieldwidth-2)*(fieldheight-2)];
        long int blurfieldsize = (fieldwidth-2)*(fieldheight-2);

        for (int j = 0,m=fieldwidth-2; j < m; j++)
        {
            for (int k = 0, n=fieldheight-2;  k < n; k++)
            {
                for (int h = 0; h < 9; h++)
                {
                    blurfield[j+(k*m)] += field[(j + (h % 3))+((k+(h/ 3))*fieldwidth)];
                }
                blurfield[j+(k*m)] /= 9;
            }
        }

        memmove((void *)field,(void *)blurfield,blurfieldsize*sizeof(int));
        delete blurfield;

        /// rest
        fieldwidth=fieldwidth-2;
        fieldheight=fieldheight-2;

        /// Trim field
        int * trimfield = new int[nwidth*nheight];
        long int trimfieldsize = nwidth*nheight;

        for (int j = 0, m=nwidth; j < m; j++)
        {
            for (int k = 0, n=nheight; k < n; k++)
            {
                trimfield[j+(k*m)] = field[(j + xoff)+((k + yoff)*fieldwidth)];
            }
        }

        /// create new
        memmove((void *)field,(void *)trimfield,trimfieldsize*sizeof(int));

        delete trimfield;
    }

    SaveTerrFile(field, width, "output.png");

    return field;
}

int OlsenNoise2D::hashrandom(std::vector<long long int> elements)
{
    long long hashcalc = 0;


    for (int i = 0; i < elements.size(); i++)
    {
        hashcalc ^= elements[i];
        hashcalc = hash(hashcalc);
    }
    return (int) hashcalc;
};

long long OlsenNoise2D::hash(long long v)
{
    long long hash = v;
    long long h = hash;

    switch ((int) hash & 3)
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
    return hash;
};


int main()
{
    /// Test
    int ImageSize=2048;

    int * imageInput = new int[ImageSize*ImageSize];

    /// Image
    OlsenNoise2D testingolsen;
    imageInput=testingolsen.olsennoise(1,1,ImageSize,ImageSize);

    // SaveTerrFile(imageInput, ImageSize, "rgbOlsen.png");

    delete imageInput;

    return 1;
}


void SaveTerrFile(const int * image, int size, char * filename)
{
    png::image< png::rgb_pixel > newimage(size, size);

    for (unsigned int y = 0; y < newimage.get_width(); ++y)
    {
        for (unsigned int x = 0; x < newimage.get_height(); ++x)
        {
            int col = int(image[x+(y*newimage.get_width())]);
            newimage[y][x] = png::rgb_pixel(col,col,col);
            // non-checking equivalent of image.set_pixel(x, y, ...);
        }
    }

    newimage.write(filename);
}

[/code]

-------------------------

JTippetts | 2017-01-02 01:03:35 UTC | #12

I get a segfault at the line [b]memmove((void *)field,(void *) upsampled,upsampledsize*sizeof(int));[/b]

That olsennoise() method looks like a prime candidate for being broken up into smaller functions. You'd probably have better luck isolating your bug that way.

-------------------------

vivienneanthony | 2017-01-02 01:03:35 UTC | #13

[quote="JTippetts"]I get a segfault at the line [b]memmove((void *)field,(void *) upsampled,upsampledsize*sizeof(int));[/b]

That olsennoise() method looks like a prime candidate for being broken up into smaller functions. You'd probably have better luck isolating your bug that way.[/quote]

Yea. I was working on the code last night.

Working copy image
The [imgur.com/a/ei4dF](http://imgur.com/a/ei4dF)

Working copy
[pastebin.com/iZUPJThc](http://pastebin.com/iZUPJThc)

There is a slight issue with the edge maybe because of low numbers from the calculation process since(Mentioned by the author). I removed memmov. I was mixing memmov with c++ allocation methods of delete[] and new. If that's figured out as to the edge, then you have infinite terrain dirt fast that's reasonable and probably better then diamond square method.

The developer is trying to work on a fix to the problem [godsnotwheregodsnot.blogspot.com ... noise.html](http://godsnotwheregodsnot.blogspot.com/2014/08/3d-olsen-noise.html)

His code is at [pastebin.com/BdVY9wXN](http://pastebin.com/BdVY9wXN)

My code is at [pastebin.com/LTww8EQr](http://pastebin.com/LTww8EQr)

Since I changing code from a array to a pointer array. Basically [x][y] to [x*(y*width)]. I have to find every [y] and change it to [y*width] that matches that specific code and function which takes me longer. Since, I already converted the previous code, it is a little bit faster and deciphering Java.

Vivienne

BTW, the guy wants to make a Android app to Demostrate. I see this as a possible why to get a noise generator in Urho3d and to highlight Urho3D. He made a 3D version also.

-------------------------

vivienneanthony | 2017-01-02 01:03:36 UTC | #14

[quote="JTippetts"]I get a segfault at the line [b]memmove((void *)field,(void *) upsampled,upsampledsize*sizeof(int));[/b]

That olsennoise() method looks like a prime candidate for being broken up into smaller functions. You'd probably have better luck isolating your bug that way.[/quote]

These are images of the generated textured loaded into the Urho3D editor Terrain node.

[imgur.com/a/p42gb](http://imgur.com/a/p42gb)

I think it's infinite like STB Perlin just setting (x,y).

Since the terrain blend works. It sounds like a fresh mix of infinite terrain.

Note, just want to create a way to make roads, maybe generate a path then use it to mask or alter the heightmap,

-------------------------

