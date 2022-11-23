SteveU3D | 2017-02-06 13:44:28 UTC | #1

Hi,

I would like to get images from a camera with openCV and then convert those images to display them on a 3D object in Urho3D. So I need to convert a cvMat to Texture2D.
I tried : 
Texture2D *videoTexture = new Texture2D(context_);
bool success = videoTexture->SetData(0,0,0,mycvmat.cols, mycvmat.rows,mycvmat.data); //where mycvmat is from cap = cv::VideoCapture(0); cap >> mycvmat;
But SetData keeps returning false.

Any ideas?
Thanks

-------------------------

cadaver | 2017-02-06 13:51:10 UTC | #2

You need to call Texture2D::SetSize to create the actual GPU texture with the specified size & format. Otherwise SetData will always fail, as there's nowhere to set the data to.

-------------------------

SteveU3D | 2017-02-06 13:06:09 UTC | #3

Indeed, it works with setSize.
Thanks!

-------------------------

