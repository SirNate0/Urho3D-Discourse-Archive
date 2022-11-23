seven | 2017-09-17 23:55:05 UTC | #1

I compiled the urho3d under Fedora26,
and the compilation process is：
```
mkdir build
cd build
cmake ..
make
cd bin
./06_SkeletalAnimation
```
![2017-09-18 07-54-18 的屏幕截图|690x388](upload://jkbF6ZVMXQ3OaI3G4j3UuoThEpe.jpg)

-------------------------

weitjong | 2017-09-18 04:10:05 UTC | #2

Make sure you are using proprietary graphics driver (kernel module) and not those from Mesa.

-------------------------

