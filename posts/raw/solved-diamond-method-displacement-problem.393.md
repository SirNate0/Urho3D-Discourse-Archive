vivienneanthony | 2017-01-02 01:00:06 UTC | #1

Hello,

I'm working on the procedural terrain and trying to implement a different noise type. The problem I have is with the floats. It seems to work but oddly the color is cycling isntead of 0 to 1. I'm getting 0 to 1, 0 to 1, repeatedly. Basically destryoing the elevation.

Here is the code and a link to the results from it.

[en.wikipedia.org/wiki/Diamond-sq ... _algorithm](http://en.wikipedia.org/wiki/Diamond-square_algorithm#Midpoint_displacement_algorithm)

Current results picture.

[tinypic.com/view.php?pic=2kotwx&s=8](http://tinypic.com/view.php?pic=2kotwx&s=8)




[code]/// Cold to create noise through the Diamond method. Requires offset and better hash table to create random heightmaps but repeatable
bool Image::generateDiamondMethod1 (float * buffer,const int &width, const int &height, const float &maxYcoords,const float &minYcoords)
{
    //an initial seed value for the corners of the data
    float SEED = 0.0f;
    unsigned int DATA_SIZE=width+1;
    float diamond[DATA_SIZE][DATA_SIZE];

    //initialise the values of the corners++
    diamond[0][0] = SEED;
    diamond[0][DATA_SIZE-1] = SEED;
    diamond[DATA_SIZE-1][0] = SEED;
    diamond[DATA_SIZE-1][DATA_SIZE-1] = SEED;

    float h =100.0; 	//the range (-h -> h) for the average offset
    srand(1);		//seed the random generator

    //side length is the distance of a single square side
    //or distance of diagonal in diamond
    //each iteration we are looking at smaller squares and diamonds, we decrease the variation of the offset
    for (int sideLength = DATA_SIZE-1; sideLength >= 2; sideLength /= 2, h /= 2.0)
    {

        int halfSide = sideLength/2;

        //generate new square values
        for(int x=0; x<DATA_SIZE-1; x+=sideLength)
        {
            for(int y=0; y<DATA_SIZE-1; y+=sideLength)
            {

                //x,y is upper left corner of the square
                //calculate average of existing corners
                float avg = diamond[x][y] + 				//top left
                            diamond[x+sideLength][y]   +				//top right
                            diamond[x][y+sideLength]   + 				//lower left
                            diamond[x+sideLength][y+sideLength]; 	//lower right
                avg /= 4.0;

                //center is average plus random offset in the range (-h, h)
                float offset = (-h) + rand() * (h - (-h)) / RAND_MAX;
                diamond[x+halfSide][y+halfSide] = avg + offset;

            } //for y
        } // for x

        //Generate the diamond values
        //Since diamonds are staggered, we only move x by half side
        //NOTE: if the data shouldn't wrap the x < DATA_SIZE and y < DATA_SIZE
        for (int x=0; x<DATA_SIZE-1; x+=halfSide)
        {
            for (int y=(x+halfSide)%sideLength; y<DATA_SIZE-1; y+=sideLength)
            {

                //x,y is center of diamond
                //we must use mod and add DATA_SIZE for subtraction
                //so that we can wrap around the array to find the corners

                float avg =
                    diamond[(x-halfSide+DATA_SIZE)%DATA_SIZE][y] +	//left of center
                    diamond[(x+halfSide)%DATA_SIZE][y]				+	//right of center
                    diamond[x][(y+halfSide)%DATA_SIZE]				+	//below center
                    diamond[x][(y-halfSide+DATA_SIZE)%DATA_SIZE];	//above center

                avg /= 4.0;

                //new value = average plus random offset
                //calc random value in the range (-h,+h)
                float offset = (-h) + rand() * (h - (-h)) / RAND_MAX;
                avg = avg + offset;

                //update value for center of diamond
                diamond[x][y] = avg;

                //wrap values on the edges
                //remove this and adjust loop condition above
                //for non-wrapping values
                if (x == 0) diamond[DATA_SIZE-1][y] = avg;
                if (y == 0) diamond[x][DATA_SIZE-1] = avg;
            } //for y
        } //for x
    } //for sideLength

    /// Set maxY and minY to 0.0f
    float maxY = diamond[1][1];
    float minY = diamond[1][1];

    /// Calculate minY and maxY values
    for (int x = 0; x<DATA_SIZE-1; x++)
    {
        for(int y=0; y<DATA_SIZE-1; y++)
        {
            if (diamond[x][y] > maxY)
                maxY = diamond[x][y];
            if (diamond[x][y] < minY)
                minY = diamond[x][y];
        }
    }

    /// Calculate height from 0 to 1
    for(int x=0; x < DATA_SIZE-1; x++)
    {
        for(int y=0; y < DATA_SIZE-1; y++)
        {
            //change range to 0..1
            diamond[x][y] = (diamond[x][y] - minY) / (maxY - minY);
        }

    }

    /// Copy color float from create texture
    for(unsigned x = 0; x<width; x++)
    {
        for(unsigned y = 0; y<height; y++)
        {
            /// incremennt memory which seems to work
            int index = x+(y*width);

            buffer[index]=diamond[x][y];
        }
    }

    return true;
}[/code]

Code to produce output
[code]/// generate perlin output
bool Image::GenerateBuild(float * buffer, unsigned *output)
{
    int width=width_;
    int height=height_;
    int components=components_;
    int depth=1;

    // loop through all the floats then convert to grayscale setting the color basis to .5 (forcing values 0 to 1)
    for(unsigned x = 0; x<width; x++)
    {
        for(unsigned y = 0; y<height; y++)
        {

            /// incremennt memory which seems to work
            int index = x+(y*height);

            unsigned col = buffer[index]* 255;  /// create color value

            col = rgba32ToUInt(col,col,col, 255);

            output[index] = col;      /// set grayscale - rgba is not needed. it seems to be screwy with this type of code.
        }
    }

    return true;
}
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:06 UTC | #2

Can the problem be with this code below? When I change the offset to be 0. to[b] float offset=0.1;[/b]

I get. 

[tinypic.com/r/20r4did/8](http://tinypic.com/r/20r4did/8)

[code]        //x,y is upper left corner of the square
                //calculate average of existing corners
                float avg = diamond[x][y] + 				//top left
                            diamond[x+sideLength][y]   +				//top right
                            diamond[x][y+sideLength]   + 				//lower left
                            diamond[x+sideLength][y+sideLength]; 	//lower right
                avg /= 4.0;

                //center is average plus random offset in the range (-h, h)
                float offset = (-h) + rand() * (h - (-h))  / RAND_MAX;[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:06 UTC | #3

Problem partially fixed.

Could use help on the last part. Check out my response to dhayden.

Vivienne

[quote]dhayden,

I looked and modified the code as such . It is partially fixed. Here is a link of the produced image so I am trying to figure out the rest of the problem.

Main Picture
[tinypic.com/r/23ser1s/8](http://tinypic.com/r/23ser1s/8)

Troubled area after I inverted in a paint program (If that helps)
[tinypic.com/r/2irlxsz/8](http://tinypic.com/r/2irlxsz/8)

code segment
[code]  //calculate average of existing corners
                float avg = diamond[x][y] + 				//top left
                            diamond[(x+sideLength)%DATA_SIZE][y]   +				//top right
                            diamond[x][ (y+sideLength)%DATA_SIZE]   + 				//lower left
                            diamond[(x+sideLength)%DATA_SIZE][(y+sideLength)%DATA_SIZE]; 	//lower right

                avg /= 4.0;

[/code]code segment
 [code]   for (int x = 0; x<DATA_SIZE;x++)
    {
        for(int y=0; y<DATA_SIZE; y++)
        {
            if (diamond[x][y] > maxY)
                maxY = diamond[x][y];
            if (diamond[x][y] < minY)
                minY = diamond[x][y];
        }
    }

    /// Calculate height from 0 to 1
    for(int x=0; x < DATA_SIZE; x++)
    {
        for(int y=0; y < DATA_SIZE; y++)
        {
            //change range to 0..1
            diamond[x][y] = (diamond[x][y] - minY) / (maxY - minY);
        }

    }
[/code]

[quote]
In that code, I think you need to change x+sideLength to (x+sideLength)%DATA_SIZE, and change y+sideLength to (y+sideLength)%DATA_SIZE.

And are you sure your loop bounds are correct? Diamond is defined with DATA_SIZE items in each index, but some of your loops (e.g.. line 89) are:

[code]for (int x = 0; x<DATA_SIZE-1; x++)[/code]

The largest value of x in this loop will be DATA_SIZE-2, which is one less than the largest index. This should be:
[code]for (int x = 0; x<DATA_SIZE; x++)[/code]

dhayden,

[/quote][/quote]

-------------------------

vivienneanthony | 2017-01-02 01:00:06 UTC | #4

This code produces this output.  What the heck!!

Code
[code]   cout << "\r\nlocation1 "<< diamond[305][742];
    cout << "\r\nlocation2 " <<diamond[288][732];

    /// Set maxY and minY to 0.0f
    float maxY = diamond[1][1];
    float minY = diamond[1][1];

    for (int x = 0; x<DATA_SIZE;x++)
    {
        for(int y=0; y<DATA_SIZE; y++)
        {
            if (diamond[x][y] > maxY)
                maxY = diamond[x][y];
            if (diamond[x][y] < minY)
                minY = diamond[x][y];
        }
    }

    cout << "\r\nminY"<< minY;
    cout << "\r\nmaxY"<< maxY;[/code]

Output - Command Line (Debug)
[code]location1 -24.0164
location2 -13.1731
minY-21.6058
maxY186.181[/code]
The for loop is not catching the minY and maxY!!!

-------------------------

