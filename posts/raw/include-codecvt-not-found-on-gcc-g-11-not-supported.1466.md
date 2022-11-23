vivienneanthony | 2017-01-02 01:07:54 UTC | #1

Hello,

I  am trying to compile the ODBC support. I'm getting  #include <codecvt>  not found error. I'm using GCC and G++ above 4.8 which isn't the case. Codecvt is not standard across platforms. So, I am wondering if even stumbled on this problem. I'm using Ubuntu 12.04, Gcc 4.8+, G++ 4.8, mysql  Ver 14.14 Distrib 5.5.46, unixodbc 2.3, and  cmake version 3.3.2

Viv


[code]vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3D-MasterCurrent1.4$ ./cmake_generic.sh build  -DURHO3D_64BIT=1 -DURHO3D_SAMPLES=1 -DURHO3D_EXTRAS=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DURHO3D_DATABASE_ODBC=1
-- The C compiler identification is GNU 4.8.1
-- The CXX compiler identification is GNU 4.8.1
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found ODBC driver manager: odbc /usr/local/include
-- Looking for include file stdint.h
-- Looking for include file stdint.h - found
-- Found OpenGL: /usr/lib/x86_64-linux-gnu/libGL.so  
-- Looking for XOpenDisplay in /usr/lib/x86_64-linux-gnu/libX11.so;/usr/lib/x86_64-linux-gnu/libXext.so
-- Looking for XOpenDisplay in /usr/lib/x86_64-linux-gnu/libX11.so;/usr/lib/x86_64-linux-gnu/libXext.so - found
-- Looking for gethostbyname
-- Looking for gethostbyname - found
-- Looking for connect
-- Looking for connect - found
-- Looking for remove
-- Looking for remove - found
-- Looking for shmat
-- Looking for shmat - found
-- Looking for IceConnectionNumber in ICE
-- Looking for IceConnectionNumber in ICE - found
-- Found X11: /usr/lib/x86_64-linux-gnu/libX11.so
-- Performing Test HAVE_CONST_XEXT_ADDDISPLAY
-- Performing Test HAVE_CONST_XEXT_ADDDISPLAY - Failed
-- Performing Test HAVE_CONST_XDATA32
-- Performing Test HAVE_CONST_XDATA32 - Failed
-- Found ALSA: /usr/lib/x86_64-linux-gnu/libasound.so (found version "1.0.25") 
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Success
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Success
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success
-- Found Urho3D: as CMake target
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE) 
-- Configuring done
-- Generating done
-- Build files have been written to: /media/home2/vivienne/Urho3D-MasterCurrent1.4/build
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3D-MasterCurrent1.4$ cd build
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3D-MasterCurrent1.4/build$ make
Scanning dependencies of target FreeType
[  0%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.o
[  0%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftbase.c.o
[  0%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftbbox.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftbitmap.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftfstype.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftgasp.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftglyph.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftgxval.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftinit.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftlcdfil.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftmm.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftotval.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftpatent.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftpfr.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftstroke.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftsynth.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftsystem.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/fttype1.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftwinfnt.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/bdf/bdf.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/bzip2/ftbzip2.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/cache/ftcache.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/cff/cff.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/cid/type1cid.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/gxvalid/gxvalid.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/gzip/ftgzip.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/lzw/ftlzw.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/otvalid/otvalid.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/pcf/pcf.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/pfr/pfr.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/psaux/psaux.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/pshinter/pshinter.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/psnames/psmodule.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/raster/raster.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/sfnt/sfnt.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/smooth/smooth.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/truetype/truetype.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/type1/type1.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/type42/type42.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/winfonts/winfnt.c.o
[  4%] Linking C static library libFreeType.a
[  4%] Built target FreeType
Scanning dependencies of target JO
[  4%] Building CXX object Source/ThirdParty/JO/CMakeFiles/JO.dir/jo_jpeg.cpp.o
/media/home2/vivienne/Urho3D-MasterCurrent1.4/Source/ThirdParty/JO/jo_jpeg.cpp: In function ?bool jo_write_jpg(const char*, const void*, int, int, int, int)?:
/media/home2/vivienne/Urho3D-MasterCurrent1.4/Source/ThirdParty/JO/jo_jpeg.cpp:265:59: warning: narrowing conversion of ?(height >> 8)? from ?int? to ?const unsigned char? inside { } [-Wnarrowing]
  const unsigned char head1[] = { 0xFF,0xC0,0,0x11,8,height>>8,height&0xFF,width>>8,width&0xFF,3,1,0x11,0,2,0x11,1,3,0x11,1,0xFF,0xC4,0x01,0xA2,0 };
                                                           ^
/media/home2/vivienne/Urho3D-MasterCurrent1.4/Source/ThirdParty/JO/jo_jpeg.cpp:265:69: warning: narrowing conversion of ?(height & 255)? from ?int? to ?const unsigned char? inside { } [-Wnarrowing]
  const unsigned char head1[] = { 0xFF,0xC0,0,0x11,8,height>>8,height&0xFF,width>>8,width&0xFF,3,1,0x11,0,2,0x11,1,3,0x11,1,0xFF,0xC4,0x01,0xA2,0 };
                                                                     ^
/media/home2/vivienne/Urho3D-MasterCurrent1.4/Source/ThirdParty/JO/jo_jpeg.cpp:265:80: warning: narrowing conversion of ?(width >> 8)? from ?int? to ?const unsigned char? inside { } [-Wnarrowing]
  const unsigned char head1[] = { 0xFF,0xC0,0,0x11,8,height>>8,height&0xFF,width>>8,width&0xFF,3,1,0x11,0,2,0x11,1,3,0x11,1,0xFF,0xC4,0x01,0xA2,0 };
                                                                                ^
/media/home2/vivienne/Urho3D-MasterCurrent1.4/Source/ThirdParty/JO/jo_jpeg.cpp:265:89: warning: narrowing conversion of ?(width & 255)? from ?int? to ?const unsigned char? inside { } [-Wnarrowing]
  const unsigned char head1[] = { 0xFF,0xC0,0,0x11,8,height>>8,height&0xFF,width>>8,width&0xFF,3,1,0x11,0,2,0x11,1,3,0x11,1,0xFF,0xC4,0x01,0xA2,0 };
                                                                                         ^
[  4%] Linking CXX static library libJO.a
[  4%] Built target JO
Scanning dependencies of target LZ4
[  4%] Building C object Source/ThirdParty/LZ4/CMakeFiles/LZ4.dir/lz4.c.o
[  5%] Building C object Source/ThirdParty/LZ4/CMakeFiles/LZ4.dir/lz4hc.c.o
[  5%] Linking C static library libLZ4.a
[  5%] Built target LZ4
Scanning dependencies of target PugiXml
[  5%] Building CXX object Source/ThirdParty/PugiXml/CMakeFiles/PugiXml.dir/src/pugixml.cpp.o
[  5%] Linking CXX static library libPugiXml.a
[  5%] Built target PugiXml
Scanning dependencies of target rapidjson
[  5%] Built target rapidjson
Scanning dependencies of target SDL
[  5%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/SDL_error.c.o
[  5%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/SDL_hints.c.o
[  6%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/SDL_log.c.o
[  6%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/SDL_assert.c.o
[  6%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/SDL.c.o
[  6%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/atomic/SDL_atomic.c.o
[  6%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/atomic/SDL_spinlock.c.o
[  6%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/SDL_audio.c.o
[  6%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/SDL_audiodev.c.o
[  6%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/SDL_wave.c.o
[  6%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/SDL_audiotypecvt.c.o
[  6%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/SDL_audiocvt.c.o
[  7%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/SDL_mixer.c.o
[  7%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/disk/SDL_diskaudio.c.o
[  7%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/dummy/SDL_dummyaudio.c.o
[  7%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/cpuinfo/SDL_cpuinfo.c.o
[  7%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/events/SDL_keyboard.c.o
[  7%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/events/SDL_windowevents.c.o
[  7%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/events/SDL_dropevents.c.o
[  7%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/events/SDL_mouse.c.o
[  7%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/events/SDL_touch.c.o
[  7%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/events/SDL_gesture.c.o
[  7%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/events/SDL_events.c.o
[  8%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/events/SDL_quit.c.o
[  8%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/events/SDL_clipboardevents.c.o
[  8%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/file/SDL_rwops.c.o
[  8%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/haptic/SDL_haptic.c.o
[  8%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/joystick/SDL_gamecontroller.c.o
[  8%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/joystick/SDL_joystick.c.o
[  8%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/libm/s_scalbn.c.o
[  8%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/libm/e_sqrt.c.o
[  8%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/libm/e_atan2.c.o
[  8%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/libm/s_floor.c.o
[  8%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/libm/k_rem_pio2.c.o
[  9%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/libm/e_pow.c.o
[  9%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/libm/k_cos.c.o
[  9%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/libm/s_atan.c.o
[  9%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/libm/s_fabs.c.o
[  9%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/libm/e_rem_pio2.c.o
[  9%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/libm/s_copysign.c.o
[  9%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/libm/s_cos.c.o
[  9%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/libm/k_sin.c.o
[  9%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/libm/e_log.c.o
[  9%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/libm/s_sin.c.o
[ 10%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/power/SDL_power.c.o
[ 10%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/stdlib/SDL_string.c.o
[ 10%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/stdlib/SDL_stdlib.c.o
[ 10%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/stdlib/SDL_qsort.c.o
[ 10%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/stdlib/SDL_getenv.c.o
[ 10%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/stdlib/SDL_malloc.c.o
[ 10%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/stdlib/SDL_iconv.c.o
[ 10%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/thread/SDL_thread.c.o
[ 10%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/timer/SDL_timer.c.o
[ 10%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_blit_A.c.o
[ 10%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_RLEaccel.c.o
[ 11%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_stretch.c.o
[ 11%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_pixels.c.o
[ 11%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_shape.c.o
[ 11%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_video.c.o
[ 11%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_blit_auto.c.o
[ 11%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_bmp.c.o
[ 11%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_rect.c.o
[ 11%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_blit_1.c.o
[ 11%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_surface.c.o
[ 11%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_clipboard.c.o
[ 12%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_blit_copy.c.o
[ 12%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_blit.c.o
[ 12%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_egl.c.o
[ 12%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_blit_N.c.o
[ 12%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_fillrect.c.o
[ 12%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_blit_0.c.o
[ 12%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/SDL_blit_slow.c.o
[ 12%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/dummy/SDL_nullevents.c.o
[ 12%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/dummy/SDL_nullvideo.c.o
[ 12%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/dummy/SDL_nullframebuffer.c.o
[ 12%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/alsa/SDL_alsa_audio.c.o
[ 13%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/dsp/SDL_dspaudio.c.o
[ 13%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/haptic/linux/SDL_syshaptic.c.o
[ 13%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/joystick/linux/SDL_sysjoystick.c.o
[ 13%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/loadso/dlopen/SDL_sysloadso.c.o
[ 13%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/power/linux/SDL_syspower.c.o
[ 13%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/thread/pthread/SDL_systls.c.o
[ 13%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/thread/pthread/SDL_syscond.c.o
[ 13%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/thread/pthread/SDL_systhread.c.o
[ 13%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/thread/pthread/SDL_sysmutex.c.o
[ 13%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/thread/pthread/SDL_syssem.c.o
[ 14%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/timer/unix/SDL_systimer.c.o
[ 14%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/filesystem/unix/SDL_sysfilesystem.c.o
[ 14%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11window.c.o
[ 14%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11video.c.o
[ 14%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11keyboard.c.o
[ 14%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11modes.c.o
[ 14%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11messagebox.c.o
[ 14%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11xinput2.c.o
[ 14%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/edid-parse.c.o
[ 14%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/imKStoUCS.c.o
[ 14%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11opengl.c.o
[ 15%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11clipboard.c.o
[ 15%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11mouse.c.o
[ 15%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11events.c.o
[ 15%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11touch.c.o
[ 15%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11opengles.c.o
[ 15%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11framebuffer.c.o
[ 15%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11shape.c.o
[ 15%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11dyn.c.o
[ 15%] Linking C static library libSDL.a
[ 15%] Built target SDL
Scanning dependencies of target StanHull
[ 15%] Building CXX object Source/ThirdParty/StanHull/CMakeFiles/StanHull.dir/hull.cpp.o
/media/home2/vivienne/Urho3D-MasterCurrent1.4/Source/ThirdParty/StanHull/hull.cpp: In function ?int StanHull::overhull(StanHull::Plane*, int, StanHull::float3*, int, int, StanHull::float3*&, int&, int*&, int&, float)?:
/media/home2/vivienne/Urho3D-MasterCurrent1.4/Source/ThirdParty/StanHull/hull.cpp:2590:28: warning: converting to non-pointer type ?int? from NULL [-Wconversion-null]
  if(verts_count <4) return NULL;
                            ^
[ 15%] Linking CXX static library libStanHull.a
[ 15%] Built target StanHull
Scanning dependencies of target STB
[ 15%] Building C object Source/ThirdParty/STB/CMakeFiles/STB.dir/stb_image_write.c.o
[ 16%] Building C object Source/ThirdParty/STB/CMakeFiles/STB.dir/stb_vorbis.c.o
[ 16%] Building C object Source/ThirdParty/STB/CMakeFiles/STB.dir/stb_image.c.o
[ 16%] Linking C static library libSTB.a
[ 16%] Built target STB
Scanning dependencies of target AngelScript
[ 16%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_callfunc.cpp.o
[ 16%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_callfunc_x64_mingw.cpp.o
[ 16%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_callfunc_x64_msvc.cpp.o
[ 16%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_compiler.cpp.o
[ 16%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_tokenizer.cpp.o
[ 17%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_datatype.cpp.o
[ 17%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_callfunc_ppc.cpp.o
[ 17%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_callfunc_arm.cpp.o
[ 17%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_callfunc_x64_gcc.cpp.o
[ 17%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_memory.cpp.o
[ 17%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_string.cpp.o
[ 17%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_string_util.cpp.o
[ 17%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_context.cpp.o
[ 17%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_thread.cpp.o
[ 17%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_gc.cpp.o
[ 17%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_callfunc_mips.cpp.o
[ 18%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_scriptfunction.cpp.o
[ 18%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_typeinfo.cpp.o
[ 18%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_parser.cpp.o
[ 18%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_callfunc_x86.cpp.o
[ 18%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_scriptnode.cpp.o
[ 18%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_atomic.cpp.o
[ 18%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_restore.cpp.o
[ 18%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_globalproperty.cpp.o
[ 18%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_objecttype.cpp.o
[ 18%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_outputbuffer.cpp.o
[ 18%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_callfunc_ppc_64.cpp.o
[ 19%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_scriptengine.cpp.o
[ 19%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_variablescope.cpp.o
[ 19%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_callfunc_sh4.cpp.o
[ 19%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_builder.cpp.o
[ 19%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_bytecode.cpp.o
[ 19%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_callfunc_xenon.cpp.o
[ 19%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_module.cpp.o
[ 19%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_configgroup.cpp.o
[ 19%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_scriptobject.cpp.o
[ 19%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_scriptcode.cpp.o
[ 20%] Building CXX object Source/ThirdParty/AngelScript/CMakeFiles/AngelScript.dir/source/as_generic.cpp.o
[ 20%] Linking CXX static library libAngelScript.a
[ 20%] Built target AngelScript
Scanning dependencies of target Lua
[ 20%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lfunc.c.o
[ 21%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/ltm.c.o
[ 21%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lzio.c.o
[ 21%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/ldump.c.o
[ 21%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lauxlib.c.o
[ 21%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/loslib.c.o
[ 21%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lparser.c.o
[ 21%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lstate.c.o
[ 21%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lmem.c.o
[ 21%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/print.c.o
[ 21%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lbaselib.c.o
[ 21%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lundump.c.o
[ 22%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/ldo.c.o
[ 22%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lopcodes.c.o
[ 22%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/ltablib.c.o
[ 22%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/linit.c.o
[ 22%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/llex.c.o
[ 22%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lapi.c.o
[ 22%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lstrlib.c.o
[ 22%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/loadlib.c.o
[ 22%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/liolib.c.o
[ 22%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/ldebug.c.o
[ 23%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lvm.c.o
[ 23%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lobject.c.o
[ 23%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lmathlib.c.o
[ 23%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/ldblib.c.o
[ 23%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lcode.c.o
[ 23%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lgc.c.o
[ 23%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/lstring.c.o
[ 23%] Building C object Source/ThirdParty/Lua/CMakeFiles/Lua.dir/src/ltable.c.o
[ 23%] Linking C static library libLua.a
[ 23%] Built target Lua
Scanning dependencies of target lua_interpreter
[ 23%] Building C object Source/ThirdParty/Lua/CMakeFiles/lua_interpreter.dir/src/lua.c.o
[ 23%] Linking C executable ../../../bin/lua
[ 23%] Built target lua_interpreter
Scanning dependencies of target luac
[ 23%] Building C object Source/ThirdParty/Lua/CMakeFiles/luac.dir/src/luac.c.o
[ 23%] Linking C executable ../../../bin/luac
[ 23%] Built target luac
Scanning dependencies of target toluapp
[ 23%] Building C object Source/ThirdParty/toluapp/src/lib/CMakeFiles/toluapp.dir/tolua_is.c.o
[ 23%] Building C object Source/ThirdParty/toluapp/src/lib/CMakeFiles/toluapp.dir/tolua_map.c.o
[ 23%] Building C object Source/ThirdParty/toluapp/src/lib/CMakeFiles/toluapp.dir/tolua_push.c.o
[ 23%] Building C object Source/ThirdParty/toluapp/src/lib/CMakeFiles/toluapp.dir/tolua_to.c.o
[ 23%] Building C object Source/ThirdParty/toluapp/src/lib/CMakeFiles/toluapp.dir/tolua_event.c.o
[ 24%] Linking C static library libtoluapp.a
[ 24%] Built target toluapp
Scanning dependencies of target Civetweb
[ 24%] Building C object Source/ThirdParty/Civetweb/CMakeFiles/Civetweb.dir/src/civetweb.c.o
[ 25%] Linking C static library libCivetweb.a
[ 25%] Built target Civetweb
Scanning dependencies of target kNet
[ 25%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/64BitAllocDebugger.cpp.o
[ 25%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/DataSerializer.cpp.o
[ 25%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/Clock.cpp.o
[ 25%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/SerializationStructCompiler.cpp.o
[ 25%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/NetworkServer.cpp.o
[ 25%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/NetworkSimulator.cpp.o
[ 25%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/TCPMessageConnection.cpp.o
[ 26%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/NetworkMessage.cpp.o
[ 26%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/NetworkWorkerThread.cpp.o
[ 26%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/Network.cpp.o
[ 26%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/SerializedDataIterator.cpp.o
[ 26%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/NetworkLogging.cpp.o
[ 26%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/MessageConnection.cpp.o
[ 26%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/UDPMessageConnection.cpp.o
[ 26%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/FragmentedTransferManager.cpp.o
[ 26%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/Thread.cpp.o
[ 26%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/MessageListParser.cpp.o
[ 27%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/DataDeserializer.cpp.o
[ 27%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/Socket.cpp.o
[ 27%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/unix/UnixThread.cpp.o
[ 27%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/unix/UnixEventArray.cpp.o
[ 27%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/unix/UnixEvent.cpp.o
/media/home2/vivienne/Urho3D-MasterCurrent1.4/Source/ThirdParty/kNet/src/unix/UnixEvent.cpp: In member function ?void kNet::Event::Set()?:
/media/home2/vivienne/Urho3D-MasterCurrent1.4/Source/ThirdParty/kNet/src/unix/UnixEvent.cpp:157:32: warning: ignoring return value of ?ssize_t read(int, void*, size_t)?, declared with attribute warn_unused_result [-Wunused-result]
  read(fd[0], &val, sizeof(val));
                                ^
[ 27%] Linking CXX static library libkNet.a
[ 27%] Built target kNet
Scanning dependencies of target nanodbc
[ 27%] Building CXX object Source/ThirdParty/nanodbc/CMakeFiles/nanodbc.dir/src/nanodbc.cpp.o
/media/home2/vivienne/Urho3D-MasterCurrent1.4/Source/ThirdParty/nanodbc/src/nanodbc.cpp:9:19: fatal error: codecvt: No such file or directory
 #include <codecvt>
                   ^
compilation terminated.
make[2]: *** [Source/ThirdParty/nanodbc/CMakeFiles/nanodbc.dir/src/nanodbc.cpp.o] Error 1
make[1]: *** [Source/ThirdParty/nanodbc/CMakeFiles/nanodbc.dir/all] Error 2
make: *** [all] Error 2
[/code]

-------------------------

weitjong | 2017-01-02 01:07:55 UTC | #2

In Fedora distro this header is packaged under libstdc++-devel. I believe in Debian-based distros (like Ubuntu) it is packaged under libstdc++-dev. This kind of issue is not Urho3D specific.

-------------------------

vivienneanthony | 2017-01-02 01:07:55 UTC | #3

[quote="weitjong"]In Fedora distro this header is packaged under libstdc++-devel. I believe in Debian-based distros (like Ubuntu) it is packaged under libstdc++-dev. This kind of issue is not Urho3D specific.[/quote]

I know it's not specific to Urho3D but the thirdparty addon which does not seem to be fully with certain builds. I'm not sure what trickery has to be done.

-------------------------

weitjong | 2017-01-02 01:07:55 UTC | #4

I don't think you can call that trickery  :wink: . Ubuntu distro is well known to be oriented toward common desktop users. By default it does not install the other essential software packages for developer users. See [help.ubuntu.com/community/InstallingCompilers](https://help.ubuntu.com/community/InstallingCompilers). To be fair, it is also the case for Fedora distro, we all have to hunt down the development software packages required to get the build works. The devs are assumed to know about this already  :smiley: .

-------------------------

vivienneanthony | 2017-01-02 01:07:56 UTC | #5

[quote="weitjong"]I don't think you can call that trickery  :wink: . Ubuntu distro is well known to be oriented toward common desktop users. By default it does not install the other essential software packages for developer users. See [help.ubuntu.com/community/InstallingCompilers](https://help.ubuntu.com/community/InstallingCompilers). To be fair, it is also the case for Fedora distro, we all have to hunt down the development software packages required to get the build works. The devs are assumed to know about this already  :smiley: .[/quote]

I modified the Cmake text with this and copied the newer source of Nanobc to the Thirdparty folder.


[code]#
# Copyright (c) 2008-2015 the Urho3D project.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

# Define target name
set (TARGET_NAME nanodbc)

# Define source files
define_source_files (GLOB_CPP_PATTERNS src/*.cpp GLOB_H_PATTERNS src/*.h)

## find Boost if necessary
if(NANODBC_USE_BOOST_CONVERT)
	set(Boost_USE_STATIC_LIBS ON)
	set(Boost_USE_MULTITHREADED ON)
	find_package(Boost COMPONENTS unit_test_framework REQUIRED)
endif()

# Define dependency libs
if (ODBC_INCLUDE_DIRS)
    set (INCLUDE_DIRS ${ODBC_INCLUDE_DIRS})
endif ()
if (ODBC_DEFINES)
    add_definitions (${ODBC_DEFINES})
endif ()

# Setup target
setup_library ()

# Install headers for building and using the Urho3D library
install_header_files (DIRECTORY src/ DESTINATION ${DEST_INCLUDE_DIR}/ThirdParty/nanodbc FILES_MATCHING PATTERN *.h)  # Note: the trailing slash is significant[/code]

When I cmake_* I get. I'm not sure why the linker language is not defined?

[code]-- Performing Test HAVE_CONST_XEXT_ADDDISPLAY - Failed
-- Performing Test HAVE_CONST_XDATA32
-- Performing Test HAVE_CONST_XDATA32 - Failed
-- Found ALSA: /usr/lib/x86_64-linux-gnu/libasound.so (found version "1.0.25") 
-- Boost version: 1.46.1
-- Found the following Boost libraries:
--   unit_test_framework
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Success
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Success
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success
-- Found Urho3D: as CMake target
-- Found Doxygen: /usr/bin/doxygen (found version "1.7.6.1") 
-- Found Dot: /usr/bin/dot  
-- Configuring done
CMake Error: Cannot determine link language for target "nanodbc".
CMake Error: CMake can not determine linker language for target: nanodbc
-- Generating done
-- Build files have been written to: /media/home2/vivienne/Urho3D-MasterCurrent1.4/build
[/code]

-------------------------

weitjong | 2017-01-02 01:07:57 UTC | #6

Although it is still related to your own build problem, the latest issue you have seems to be off-topic with the original issue "#include <codecvt> not found on gcc/g++11". It would probably allow more people to help you if you create a new issue for this and it would also probably allow other people with similar issue than yours to find your post (hopefully with its answer as well) at later time.

BTW, I have no idea or don't see why adding those lines in CMakeLists.txt would have caused this. Perhaps it has something to do with what you have in that directory. That globbing of source code using a file pattern could be a double-edged sword some time. If I were you I would double check the final source list, lib dependency list, etc being added into this target. Most likely that is the reason why the linker complained.

-------------------------

vivienneanthony | 2017-01-02 01:07:57 UTC | #7

[quote="weitjong"]Although it is still related to your own build problem, the latest issue you have seems to be off-topic with the original issue "#include <codecvt> not found on gcc/g++11". It would probably allow more people to help you if you create a new issue for this and it would also probably allow other people with similar issue than yours to find your post (hopefully with its answer as well) at later time.

BTW, I have no idea or don't see why adding those lines in CMakeLists.txt would have caused this. Perhaps it has something to do with what you have in that directory. That globbing of source code using a file pattern could be a double-edged sword some time. If I were you I would double check the final source list, lib dependency list, etc being added into this target. Most likely that is the reason why the linker complained.[/quote]

I spent some time trying to isolate the problems and I downloaded the latest nanodbc.

1. The newest version had  some code specific to Microsoft ODBC(Probably the 2.2 installed on the Urho3D github 2.2 version). I removed those specific functions because it's not required to make it more non-platform specific.
2. Used some of the original of the updated version nanobc cmake information into the Thirdparty/nanobdc/CMakeList.txt(probably spelt wrong) to build and additionally add to the Urho3D library

Updated my GCC/G++ to 4.81, Cmake 3.3, Clang 3.3.2, libboost 1.48 and when compiling nano  C++11/c++03 turned on depending on the compiler.

It built  including the DatabaseDemo which crashed I think because I didn't move the resource folders.

So, it then compiled. I'm not certain about the SQLite aspect but I think it probably compiles fine because that was tested.

-------------------------

vivienneanthony | 2017-01-02 01:07:57 UTC | #8

Hi

I have been working on the ODBC as mentioned. This is a zip file of the plain Urho3D build

[dropbox.com/s/jp26tq84wk34k ... 4.zip?dl=0](https://www.dropbox.com/s/jp26tq84wk34k2t/Urho3D-MasterCurrent1.4.zip?dl=0)

Vivienne Anthony: I updated my GCC and G++ above 4.8 and my Cmake/Clang above 3.3. I updated the the thirdparty Urho3D nanodbc to the latest version with minor changes. Also the latest Boost development files with the locale header. Using this line I was able to build  Urho.

./cmake_generic.sh build  -DURHO3D_64BIT=1 -DURHO3D_SAMPLES=1 -DURHO3D_EXTRAS=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DURHO3D_DATABASE_ODBC=1 -DNANODBC_USE_BOOST_CONVERT=ON

Results

[pastebin.com/pcMUUsgh](http://pastebin.com/pcMUUsgh)

I also tried

Now with the following lines. I had some better results. I am thinking id the cmake detects boost, updated compiler, and a few flag changes. It would work in a Linux/MinGW cross-platform build

export MINGW_PREFIX=/usr/bin/x86_64-w64-mingw32

./cmake_mingw.sh buildWin  -DURHO3D_64BIT=1 -DURHO3D_SAMPLES=1 -DURHO3D_EXTRAS=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DURHO3D_DATABASE_ODBC=1 -DNANODBC_USE_BOOST_CONVERT=OFF -DMINGW_PREFIX=/usr/bin/x86_64-w64-mingw32

I am confident that the .bat files or other files in the first example would produce 100% compile but honestly a few changes(minor) after troubleshooting.

[pastebin.com/pLRC7kZy](http://pastebin.com/pLRC7kZy)

So, both Linux and Windows builds can be made.

Vivienne

-------------------------

weitjong | 2017-01-02 01:07:57 UTC | #9

Despite the nanodbc release version appears to have a big jump, there are really nothing much changed since the last time I check (the version we currently have in our master) with their latest version. The rather significant improvement is only in the area of async SQL execution which will only be available if the ODBC driver manager installed in the system supports ODBC 3.8. Since our database subsystem does not take advantage of any new features available in ODBC 3.8, there is not much incentive to upgrade to this latest release version. Having said that, I have attempted to merge the upstream changes in order to see if everything is still building. It is not, however, at least on my Linux host system. I have spotted bug(s) in their code in regards to async execution and will probably submit a PR to upstream later. Your Ubuntu probably only have ODBC driver manager that only support ODBC 3.0, so your build did not see any issues.

-------------------------

vivienneanthony | 2017-01-02 01:07:57 UTC | #10

[quote="weitjong"]Despite the nanodbc release version appears to have a big jump, there are really nothing much changed since the last time I check (the version we currently have in our master) with their latest version. The rather significant improvement is only in the area of async SQL execution which will only be available if the ODBC driver manager installed in the system supports ODBC 3.8. Since our database subsystem does not take advantage of any new features available in ODBC 3.8, there is not much incentive to upgrade to this latest release version. Having said that, I have attempted to merge the upstream changes in order to see if everything is still building. It is not, however, at least on my Linux host system. I have spotted bug(s) in their code in regards to async execution and will probably submit a PR to upstream later. Your Ubuntu probably only have ODBC driver manager that only support ODBC 3.0, so your build did not see any issues.[/quote]

It supports 3.8 I think. I might be wrong. The problem is the platform specific Async code which makes no sense for multiplatform  compiling. Although there might be no major updates with the two versions of nanodbc. I decided to go with the higher which has the detection of boost and codecvt (which is compatible with all platforms). At least with boost and codecvt detection. It leaves some room for just in case.

I'm curious to know what bugs you spotted. I'm going play with mine version with the latest code and put more/ better platform detection to allow cross-platform or multi-platform compiles within Urho library.

-------------------------

weitjong | 2017-01-02 01:07:57 UTC | #11

No, the unixodbc in Ubuntu 12.04 only defaulted to 3.51, or otherwise you will hit the bug also. As I said before, Ubuntu 12.04 is too ancient to be supported anymore. Any recent distros with GCC 4.9 or above should be able to handle nanodbc without boost library just fine. As you may have already noticed, I actually do not use the original CMakeLists.txt from nanodbc library. I will be probably continue to do that which means I probably won't include the bits that would integrate the boost library part. As for the bugs, try to make a build on a more recent distros yourself.

-------------------------

vivienneanthony | 2017-01-02 01:07:59 UTC | #12

I will when I get a new HDD soon upgrading my Ubuntu to 14.04 lts.

I ran into this error. [pastebin.com/XrZ6S4Mm](http://pastebin.com/XrZ6S4Mm) . I'm not sure what's going on.

Urho3D builds using odbc on both Windows and Linux desktops. When trying to compile some code all these messages pop up..

-------------------------

vivienneanthony | 2017-01-02 01:07:59 UTC | #13

[quote="weitjong"]Despite the nanodbc release version appears to have a big jump, there are really nothing much changed since the last time I check (the version we currently have in our master) with their latest version. The rather significant improvement is only in the area of async SQL execution which will only be available if the ODBC driver manager installed in the system supports ODBC 3.8. Since our database subsystem does not take advantage of any new features available in ODBC 3.8, there is not much incentive to upgrade to this latest release version. Having said that, I have attempted to merge the upstream changes in order to see if everything is still building. It is not, however, at least on my Linux host system. I have spotted bug(s) in their code in regards to async execution and will probably submit a PR to upstream later. Your Ubuntu probably only have ODBC driver manager that only support ODBC 3.0, so your build did not see any issues.[/quote]

I made a library that builds in the lib folder the same folder of libUrho3D. I tried to modify and look at the FindUrho3D.cmake to a version like FindEngineStd.cmake.

I am having no luck with looking at the cmake file and going to the cmake website for help. The source code .cpp and .h files are located in Source/EngineStd.Then headers are placed in  {build folder}include/EngineStd and the usual {build folder} include/Urho3D.  Maybe you can sport some error.

Find My EngineStd
[pastebin.com/DQcHeikL](http://pastebin.com/DQcHeikL)

Put Together Engine Std
[pastebin.com/WkJpnz0p](http://pastebin.com/WkJpnz0p)

-------------------------

vivienneanthony | 2017-01-02 01:08:00 UTC | #14

Hello

So I have better results now but I have problems adding the library to a executable.

[pastebin.com/Lii52sXM](http://pastebin.com/Lii52sXM)

That's the cmake. It should be linking EngineStd and Urho3D to the executable but it's not..

The results is 

[code]/media/home2/vivienne/Urho3D-Hangars/Source/EngineStd/EngineApplication.cpp|56|error: undefined reference to 'Urho3D::Script::Script(Urho3D::Context*)'|
/media/home2/vivienne/Urho3D-Hangars/Source/EngineStd/Actors/CharacterComponent/Character.cpp|4|error: undefined reference to 'Urho3D::LogicComponent::LogicComponent(Urho3D::Context*)'|
/media/home2/vivienne/Urho3D-Hangars/Source/EngineStd/Actors/CharacterComponent/Character.cpp|7|error: undefined reference to 'Urho3D::LogicComponent::SetUpdateEventMask(unsigned char)'|
/media/home2/vivienne/Urho3D-Hangars/Source/EngineStd/Actors/CharacterComponent/Character.cpp|4|error: undefined reference to 'Urho3D::LogicComponent::~LogicComponent()'|
/media/home2/vivienne/Urho3D-Hangars/Source/EngineStd/Actors/CharacterComponent/Character.h|18|error: undefined reference to 'Urho3D::LogicComponent::~LogicComponent()'|
/media/home2/vivienne/Urho3D-Hangars/Source/EngineStd/Actors/CharacterComponent/Character.h|18|error: undefined reference to 'Urho3D::LogicComponent::~LogicComponent()'|
../../lib/libEngineStd.a(Character.cpp.o):Character.cpp:function typeinfo for Character: error||undefined reference to 'typeinfo for Urho3D::LogicComponent'|
../../lib/libEngineStd.a(Character.cpp.o):Character.cpp:function vtable for Character: error||undefined reference to 'Urho3D::LogicComponent::OnSetEnabled()'|
../../lib/libEngineStd.a(Character.cpp.o):Character.cpp:function vtable for Character: error||undefined reference to 'Urho3D::LogicComponent::OnNodeSet(Urho3D::Node*)'|
../../lib/libEngineStd.a(Character.cpp.o):Character.cpp:function vtable for Character: error||undefined reference to 'Urho3D::LogicComponent::OnSceneSet(Urho3D::Scene*)'|
../../lib/libEngineStd.a(Character.cpp.o):Character.cpp:function vtable for Character: error||undefined reference to 'Urho3D::LogicComponent::Update(float)'|
../../lib/libEngineStd.a(Character.cpp.o):Character.cpp:function vtable for Character: error||undefined reference to 'Urho3D::LogicComponent::PostUpdate(float)'|
../../lib/libEngineStd.a(Character.cpp.o):Character.cpp:function vtable for Character: error||undefined reference to 'Urho3D::LogicComponent::FixedPostUpdate(float)'|
||=== Build finished: 13 errors, 0 warnings ===|
[/code]

Any help is appreciated.

Vivienne

-------------------------

