vivienneanthony | 2017-01-02 01:00:02 UTC | #1

Hi

Is this correct in converting any image to grayscale? Depending on what rotation I do the for loop? The image is affected which I know it's working but I think it's just the calculation.

Vivienne

I'm trying the first method [tannerhelland.com/3643/grays ... rithm-vb6/](http://www.tannerhelland.com/3643/grayscale-image-algorithm-vb6/)


[code]{
    // create temporary area
    unsigned char * tempdata_ = new unsigned char[width_ * height_ * depth_*components_];
    unsigned char grey;

    // loop
    for(unsigned width=0; width<width_;width++)
    {
        for(unsigned height=0; height<height_;height++)
        {
                grey=(data_[(width*height)+0]+data_[(width*height)+1]+data_[(width*height)+2])/3;

                tempdata_[(width*height)+0]=grey;
                tempdata_[(width*height)+1]=grey;
                tempdata_[(width*height)+2]=grey;
        }
    }

    // copy data
    memcpy(data_, tempdata_, width_*height_*depth_*components_);

    return;

}[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:02 UTC | #2

I also tried with no luck.

[quote]void Image::generateGrayScale(void)
///
{
    // create temporary area
    unsigned  int * tempdata_ = new unsigned int[width_ * height_ * depth_*components_];
    unsigned char grey;

    // loop
    for(unsigned x=0; x<width_;x++)
        {
            for(unsigned y=0; y<height_;y++)
            {
                    grey=(data_[(y*components_)+x+0]+data_[(y*components_)+x+1]+data_[(y*components_)+x+2])/3;

                    tempdata_[(y*components_)+x+0]=grey;
                    tempdata_[(y*components_)+x+1]=grey;
                    tempdata_[(y*components_)+x+2]=grey;
            }
        }


    // copy data
    memcpy(data_, (unsigned char *)  tempdata_, width_*height_*depth_*components_);


    return;

}[/code][/quote]

-------------------------

cadaver | 2017-01-02 01:00:03 UTC | #3

Each row in the image data is (components_ * width_) bytes, and they're laid out sequentially. Your second code snippet is missing the multiply with width_, and you should also change the tempData to unsigned char*. Finally I recommend having Y as the outer loop for better cache-friendliness.

-------------------------

vivienneanthony | 2017-01-02 01:00:03 UTC | #4

[quote="cadaver"]Each row in the image data is (components_ * width_) bytes, and they're laid out sequentially. Your second code snippet is missing the multiply with width_, and you should also change the tempData to unsigned char*. Finally I recommend having Y as the outer loop for better cache-friendliness.[/quote]


I modified it to this. I get some image now of the original but the transparency is half of the original and also thw width is  a quarter of the original. 

[code]void Image::generateGrayScale(void)
///
{
      // create temporary area
        unsigned char * tempdata_ ;

        tempdata_=(unsigned char*) malloc(width_ * height_ * depth_*components_);

        unsigned char grey;
        unsigned width = components_;

        // loop
        for(unsigned int y=0; y<height_;y++)
        {
            for(unsigned int x=0; x<width_;x++)
            {
                grey=(data_[(y*components_*width_)+x+0]+data_[(y*components_*width_)+x+1]+data_[(y*components_*width_)+x+2])/3;

                tempdata_[(y*components_*width_)+x+0]=grey;
                tempdata_[(y*components_*width_)+x+1]=grey;
                tempdata_[(y*components_*width_)+x+2]=grey;
                tempdata_[(y*components_*width_)+x+3]=255;
            }
        }

        /// Point pixelData to buffer memory
        memcpy(data_, (unsigned char *)tempdata_, width_ * height_ * depth_ * components_);

        return;

    }


[/code]

-------------------------

cadaver | 2017-01-02 01:00:03 UTC | #5

Forgot that you should also multiply x by components_ when accessing the pixels.

-------------------------

vivienneanthony | 2017-01-02 01:00:03 UTC | #6

[quote="cadaver"]Forgot that you should also multiply x by components_ when accessing the pixels.[/quote]

This seems to be a working version.

[code]void Image::generateGrayScale(void)
///
{
      // create temporary area
        unsigned char * tempdata_ ;

        tempdata_=(unsigned char*) malloc(width_ * height_ * depth_*components_);

        unsigned char grey;
        unsigned width = components_;

        // loop
        for(unsigned int y=0; y<height_;y++)
        {
            for(unsigned int x=0; x<width_;x++)
            {
                grey=(data_[(y*components_*width_)+(x*components_)+0]+data_[(y*components_*width_)+(x*components_)+1]+data_[(y*components_*width_)+(x*components_)+2])/3;

                tempdata_[(y*components_*width_)+(x*components_)+0]=grey;
                tempdata_[(y*components_*width_)+(x*components_)+1]=grey;
                tempdata_[(y*components_*width_)+(x*components_)+2]=grey;
                tempdata_[(y*components_*width_)+(x*components_)+3]=255;
            }
        }

        /// Point pixelData to buffer memory
        memcpy(data_, (unsigned char *)tempdata_, width_ * height_ * depth_ * components_);

        return;

    }

}



[/code]

So, now I think procedureal generated terrain is way possible.

-------------------------

friesencr | 2017-01-02 01:00:03 UTC | #7

[quote="cadaver"]Each row in the image data is (components_ * width_) bytes, and they're laid out sequentially. Your second code snippet is missing the multiply with width_, and you should also change the tempData to unsigned char*. Finally I recommend having Y as the outer loop for better cache-friendliness.[/quote]

Lasse when you talk about cache friendliness are you talking about cpu cache?  How do you learn about those subjects?

-------------------------

cadaver | 2017-01-02 01:00:04 UTC | #8

Yes, CPU cache. Here is one article that deals with the subject:

[gameprogrammingpatterns.com/data-locality.html](http://gameprogrammingpatterns.com/data-locality.html)

Note that for small images and anything that is processed only once it doesn't really matter, as the image data will eventually be fully loaded in the cache no matter how you access it.

-------------------------

