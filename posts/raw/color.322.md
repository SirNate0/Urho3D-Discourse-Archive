jorbuedo | 2017-01-02 00:59:37 UTC | #1

I found something a bit inconvenient. The Color class uses floating point numbers from 0.0 to 1.0 instead of 8 bit integers.
Working with terrain, that means I can't calculate heights just with a plain number, a have a float representing the percentage from min to max height.
That's still manageable, but I'm trying to use terrain with 16 bit resolution, which requieres using two color components, and instead of two 8 bit numbers that I can shift to make it 16, I have 2 floats.

Any suggestion?

-------------------------

cadaver | 2017-01-02 00:59:38 UTC | #2

An integer pixel setting API has been added to Image. You probably still need some bit shifting due to the bit order (R goes to lowest bits) but I suppose we could change the two-channel terrain height system to use G as the most significant bits and R for added detail, after that it would be very straightforward.

-------------------------

jorbuedo | 2017-01-02 00:59:38 UTC | #3

Great! I'll try it later. Little typo in the API description, 
SetPixelInt (int x, int y, int z, unsigned uintColor)
 	Set a 2D pixel with an integer color. R component is in the 8 lowest bits. 

Should be 3D.

-------------------------

jorbuedo | 2017-01-02 00:59:38 UTC | #4

Yes, I need the shifting. Would be better to change it in terrain.

-------------------------

