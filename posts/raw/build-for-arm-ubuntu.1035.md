amit | 2017-01-02 01:04:58 UTC | #1

How do we build for arm ubuntu/linux?
the cross tool chain is setup.
I have a number of arm boards, so wanted to test them!

-------------------------

weitjong | 2017-01-02 01:04:59 UTC | #2

Assuming your cross-compiler toolchain is GCC then you should be able to adapt from the CMake/Toolchains/raspberrypi.toolchain.cmake to create your own new CMake toolchain file. If your ARM board is similar to chipset used by the Raspberry-Pi, you can quicly test the build using "-DRPI=1". If it is much different then you will have to do the porting work as usual.

-------------------------

amit | 2017-01-02 01:04:59 UTC | #3

I have one based on Mali-T628 MP6 based and another is Allwinner A80 board,
would try them both.

Thanks

-------------------------

