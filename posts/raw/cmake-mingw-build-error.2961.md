cnccsk | 2017-03-28 16:55:24 UTC | #1

Hi, 
I built urho3d with mingw, but has error:

    Source\ThirdParty\SDL\src\audio\winmm\SDL_winmm.c:57:33: error: unknown type name 'WAVEOUTCAPS2W'
     DETECT_DEV_IMPL(SDL_FALSE, Out, WAVEOUTCAPS)
                                 ^

any help?

Thanks.

-------------------------

cnccsk | 2017-03-28 16:54:38 UTC | #2

Fixed, 

My mingw is wrong, everything is ok after installed mingw-w64

-------------------------

