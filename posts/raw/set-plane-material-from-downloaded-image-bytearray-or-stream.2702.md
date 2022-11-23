Jimmy781 | 2017-01-14 04:21:40 UTC | #1

Hey guys , 

I am downloading an image from the web : 

                    using (HttpClient x = new HttpClient())
                    {
                        var y = await x.GetStreamAsync(url);
                    }

plane.SetMaterial(Material.FromImage(y));


I can get y as a byte array or a stream . However i have no idea how to set the plane texture based on them . 

Any ideas ?

-------------------------

SirNate0 | 2017-01-14 04:25:57 UTC | #2

Will Texture2D's `SetData (unsigned level, int x, int y, int width, int height, const void *data)` work? (Perhaps with SetSize beforehand, unless you know the image's height and such before). Unless the image in question is a file (e.g. a png) and not raw pixel data, in which case you would have to load it differently.

-------------------------

