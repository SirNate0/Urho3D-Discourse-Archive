kapsloki | 2019-09-17 08:48:17 UTC | #1

taking a look at source i realized a lut file but its different of standards

and what are differences between CLUT and LUT? and how CLUT can be readed if its differente? I have a CLUT file and is black white and gray

LUT on Source 

https://raw.githubusercontent.com/urho3d/Urho3D/master/bin/CoreData/Textures/LUTIdentity.png

Standard LUT

![neutral-lut|500x500](upload://7POtJLRerQI4D7zF5cFIu0Ki5eb.png)

-------------------------

kapsloki | 2019-09-17 09:05:20 UTC | #2

Double post for upload more than 1 image

They're .tga but i'm posting here png, i have a just black and white too (CLUT file)

![T_ShadowCLUT2|64x64](upload://9ULu38QNHGfejlFb8p82zxeoTSV.png)

-------------------------

Modanung | 2019-09-17 13:17:55 UTC | #3

I have no personal experience with LUTs, but found [this](https://mixinglight.com/color-tutorial/understanding-luts/).


Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

brojonisbro | 2019-09-17 10:18:06 UTC | #4

@kapsloki u can take a look about CLUT on UE4 documentation, i think that is into "PostProcess" section

or here: http://www.quelsolaar.com/technology/clut.html

Any color correction can be expressed as a Color LookUp Table or CLUT (some times written as "Color LUT"). This a 3D dimensional table where all colors are represented in color space. For each color in the color lookup table there is a destination color value that corresponds to what the particular color becomes when it is corrected using the CLUT. These tables are by nature 3-dimensional (Red Green and Blue) and therefore special file formats are used to store them. Hald CLUTs however have been converted to a 2D space and since tables store colors the CLUT can be be saved as a image, in any non destructive image format.

@offtopic
@Modanung Looking at some of ur answers on the forum, how much fast you are? lol

-------------------------

kapsloki | 2019-09-17 11:37:29 UTC | #5

Sorry take a little time to answer, i was searching about this so, LUT is related to 2D, right? Like camera. And CLUT is CubeLUT and directly related to 3D objects and materials. Right?

-------------------------

brojonisbro | 2019-09-17 12:20:24 UTC | #6

i don't know if u're into glsl but
google search: "opengl glsl lut tutorial"

down the page and its explaining what is and how to use

https://partlyshaderly.com/2019/02/08/the-programming-behind-cel-shading/

good luck :stuck_out_tongue:

-------------------------

johnnycable | 2019-09-19 15:28:49 UTC | #7

Afaik, only professional monitor are able to do color management... it's mostly ignored on consumer devices... LUTs are color tables issued for the sake of sharing profiles among people working on color correction, so they start from a common base... think of a movie who must share the same (for instance) "dark horror" flavor while different takes are managed by different departments...

-------------------------

