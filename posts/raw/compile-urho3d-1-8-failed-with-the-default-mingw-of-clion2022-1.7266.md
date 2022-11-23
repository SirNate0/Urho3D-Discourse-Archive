ChunFengTsin | 2022-05-14 06:22:45 UTC | #1

OS: Windows10 
Compiler: the default MinGW of Clion2022.1.

Error: 
![微信图片_20220514142156|690x242](upload://A3RC5jUtQURjlYHCr68fehNTpip.png)

-------------------------

SirNate0 | 2022-05-14 14:34:28 UTC | #2

Seems like this might be related. Try disabling the PCH and see if that works. (Also, personally I'd recommend switching to master over 1.8)

https://sourceforge.net/p/mingw-w64/bugs/382/

-------------------------

1vanK | 2022-05-14 15:16:52 UTC | #3

U need use latest MinGW in any case <https://github.com/urho3d/Urho3D/issues/2887>

-------------------------

ChunFengTsin | 2022-05-16 06:45:54 UTC | #4

Thanks for reply, I  used the latest MinGW, it works, but it was so slowly when link.

-------------------------

