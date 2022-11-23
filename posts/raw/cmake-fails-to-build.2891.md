NiteLordz | 2017-03-13 16:19:46 UTC | #1

I have Visual Studio 2015 and 2017 installed on my machine.  When i go to run "cmake_vs2015.bat" i get the following error

"No CMAKE_CXX_COMPILER could be found"

I know that the visual studio's are installed properly, as they both compile out other c++ applications an engines.  

Ideas or thoughts....

-------------------------

1vanK | 2017-03-13 16:45:53 UTC | #2

Create bat file (fix pathes):
```
set "PATH=c:\Program Files (x86)\Git\bin;c:\Programs\Cmake\bin;c:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\Tools\;c:\Windows\System32"
Urho3D/cmake_vs2015.bat Build -DURHO3D_OPENGL=ON -DURHO3D_SAMPLES=OFF -DURHO3D_LUA=OFF -DURHO3D_STATIC_RUNTIME=ON -DURHO3D_TOOLS=0
```

-------------------------

NiteLordz | 2017-03-13 17:07:56 UTC | #3

that did not solve the problem

-------------------------

Lumak | 2017-03-13 17:51:34 UTC | #4

I had a similar problem last year when I installed vs2015 for the 1st time.  It turns out the default express install for 2015 didn't include tools for me and I had to do a custom install to correct it.

-------------------------

NiteLordz | 2017-03-13 17:57:48 UTC | #5

It would appear that the base install for VS 2017 doesn't include some of the C++ tools.  Installing and will report back.

-------------------------

rasteron | 2017-03-14 02:20:38 UTC | #6

I just got the latest commit to cmake and build with VS2015 earlier, it must have something to do with your setup.

-------------------------

yushli1 | 2017-03-14 04:25:11 UTC | #7

Try cmake_clean.bat first.

-------------------------

weitjong | 2017-03-14 11:29:29 UTC | #8

I remember the base installation for VS2015 does not include C++ development tool by default. I think the default is web development now.

-------------------------

