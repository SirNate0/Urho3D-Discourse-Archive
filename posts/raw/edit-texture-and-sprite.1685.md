Tobi3245 | 2017-01-02 01:09:28 UTC | #1

Hello
I just started Urho3d. How can we change or edit the texture or sprite pixel wise in run-time ?
Basically i want to change the color of certain pixels in run-time.
Thank you,
tobi3245

-------------------------

Sir_Nate | 2017-01-02 01:09:34 UTC | #2

You should be able to use SetData and GetData from Texture2D. Just get the data, edit the pixels you want (and then you probably have to set it again, but I'm not certain, as I've never tried it).

-------------------------

