Victor | 2017-01-02 01:14:54 UTC | #1

I just stumbled upon an interesting library for doing some advanced image manipulation. It can do some pretty cool stuff like making occlusion and normal maps.

Repo
[github.com/prideout/heman](https://github.com/prideout/heman)

Documentation
[heman.readthedocs.io/en/latest/](http://heman.readthedocs.io/en/latest/)

Here's a code snippet on converting image from heman -> Urho and Urho -> heman

[code]
/// Convert heman image to Urho3D image.
void ImageHelper::ConvertHeman2Urho(Context* context, heman_image* image, Image*& result)
{
    for (int y = 0; y < image->height; y++) {
        for (int x = 0; x < image->width; x++) {
            kmVec3 color = *((kmVec3*) heman_image_texel(image, x, y));
            Color pixel(color.x, color.y, color.z);
            result->SetPixel(x, y, pixel);
        }
    }
}

// Convert image to Urho from heman
// (could be a heightmap so we check the nbands
void ImageHelper::ConvertUrho2Heman(Image* image, heman_image*& result)
{
    if (result->nbands == 3) {
        kmVec3* colors = (kmVec3*) result->data;

        for (int y = 0; y < image->GetHeight(); y++) {
            kmVec3* color = colors + y * result->width;

            for (int x = 0; x < image->GetWidth(); x++, color++) {
                Color pixel = image->GetPixel(x, y);
                color->x = pixel.r_;
                color->y = pixel.g_;
                color->z = pixel.b_;
            }
        }

        return;
    }

    float* colors = result->data;
    for (int y = 0; y < image->GetHeight(); y++) {
        float* color = colors + y * result->width;

        for (int x = 0; x < image->GetWidth(); x++, color++) {
            Color pixel = image->GetPixel(x, y);
            *color = pixel.r_;
        }
    }
}
[/code]

Here's how I've used it in my Urho app:

[img]http://i.imgur.com/6hRIrnd.png[/img]

-------------------------

TheSHEEEP | 2017-01-02 01:14:54 UTC | #2

By the power of Greyskull!

-------------------------

namic | 2017-01-02 01:15:10 UTC | #3

Amazing library. Thanks for the info!

-------------------------

