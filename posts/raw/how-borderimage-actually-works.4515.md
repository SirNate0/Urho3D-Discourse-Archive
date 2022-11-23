anako126n | 2018-09-02 03:41:15 UTC | #1

Hi All,

After several days of looking around, playing with it I have no other choice but to ask for help.

If I understand it correctly, border image should scale an image based on Image Rect? It is working fine on default UI elements but acts really weird on my textures.

What actually happens?

Texture is 512x512, if I use an element starting at top it scales as expected. As soon as I set the rectangle for next element below it suddenly stops scaling the height (texture is multiplying itself). 

By setting the element size to 1024 the outcome would be as follows:

Image stretched to 1024 pixels width
Image duplicated to two on height.

![problem|690x370](upload://6FmokC877fOU45kT2JlGw0E1Kcb.jpeg)

What am I missing?

Thanks for help in advance

-------------------------

lezak | 2018-09-02 10:25:53 UTC | #2

Image Rect is defining what part of the texture to use as an image, it is specified (in pixels) in this order: left - top - right - bottom. It seems from Your screenshot, that You are using the same value for top and bottom (149), when bottom should be top + element height.

-------------------------

