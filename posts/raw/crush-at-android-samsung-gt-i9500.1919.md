cnccsk | 2017-01-02 01:11:29 UTC | #1

samsung GT-I9500	4.2.2	1080x1920	1.5 GHz	1861 MB

Build fingerprint: 'samsung/ja3gzc/ja3g:4.2.2/JDQ39/I9500ZCUAMDH:user/release-keys'
Revision: '10'
pid: 13330, tid: 13350, name: SDLThread >>> com.github.urho3d <<<
signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 00000124
r0 00000480 r1 00000000 r2 00000000 r3 001550fe
r4 110d6000 r5 001110f8 r6 00000400 r7 0000048c
r8 00001702 r9 77ca3010 sl 00000400 fp 00000488
ip 00000001 sp 74daa844 lr 71124a24 pc 71122f08 cpsr 20000010
d0 0000000000000000 d1 0000000000000000
d2 3f80000000000000 d3 000000003f800000
d4 0000000000000000 d5 000000003f800000
d6 0000043800000000 d7 3f8000003f800000
d8 0000000000000000 d9 0000000000000000
d10 0000000000000000 d11 0000000000000000
d12 0000000000000000 d13 0000000000000000
d14 0000000000000000 d15 0000000000000000
d16 3fad52658fefd831 d17 3fda8279abb38cf9
d18 3f5798966f109e41 d19 3f985a2eb9a334dc
d20 3f7229781f202a7c d21 3fd6a65513619f6d
d22 0000009000000061 d23 00000090000000b5
d24 3ff500001e5ad586 d25 3fe55567cb1939ea
d26 3fa555555555551c d27 3fc55555555554db
d28 3fe0000000000000 d29 0000000000000001
d30 fff0000000000000 d31 0000000000000040
scr 60000019
backtrace:
#00 pc 00012f08 /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so (SetupFrameBufferZLS+400)
#01 pc 00014a20 /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so (GetFrameBufferCompleteness+3516)
#02 pc 0000c5ec /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so (glClear+52)
#03 pc 00301555 /data/app-lib/com.github.urho3d-1/libUrho3DPlayer.so (Urho3D::Graphics::Clear(unsigned int, Urho3D::Color const&, float, unsigned int)+200)
#04 pc 002ded63 /data/app-lib/com.github.urho3d-1/libUrho3DPlayer.so (Urho3D::View::RenderShadowMap(Urho3D::LightBatchQueue const&)+278)
stack:
74daa804 77cb2f78 
74daa808 00000002 
74daa80c 7116e5f0 /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so (TexFormatFloatDepth)
74daa810 00000008 
74daa814 7117ae9c /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so
74daa818 00000001 
74daa81c 7106e008 
74daa820 00000000 
74daa824 7113f32c /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so (SetupTextureRenderTargetControlWords+856)
74daa828 00000000 
74daa82c 00000001 
74daa830 923ff3ff 
74daa834 00000000 
74daa838 df0027ad 
74daa83c 00000000 
74daa840 00000000 
#00 74daa844 77c362d8 
74daa848 00000000 
74daa84c 00000001 
74daa850 00000400 
74daa854 00000400 
74daa858 77ca3010 
74daa85c 00000001 
74daa860 00000000 
74daa864 71124a24 /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so (GetFrameBufferCompleteness+3520)
#01 74daa868 77c36a08 
74daa86c 3f800000 
74daa870 00000000 
74daa874 7116e5f0 /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so (TexFormatFloatDepth)
74daa878 7106e008 
74daa87c 00000000 
74daa880 00000000 
74daa884 00000000 
74daa888 00000000 
74daa88c 00000000 
74daa890 00000010 
74daa894 00000000 
74daa898 00000000 
74daa89c ffffffff 
74daa8a0 ffffffff 
74daa8a4 7106e008 
........ ........
#02 74daa8c8 00000100 
74daa8cc 00000000 
74daa8d0 00000000 
74daa8d4 6115d008 
74daa8d8 74b9b16c 
74daa8dc 00000100 
74daa8e0 00000002 
74daa8e4 7485b559 /data/app-lib/com.github.urho3d-1/libUrho3DPlayer.so (Urho3D::Graphics::Clear(unsigned int, Urho3D::Color const&, float, unsigned int)+204)
memory near r3:
001550dc ffffffff ffffffff ffffffff ffffffff 
001550ec ffffffff ffffffff ffffffff ffffffff 
001550fc ffffffff ffffffff ffffffff ffffffff 
0015510c ffffffff ffffffff ffffffff ffffffff 
0015511c ffffffff ffffffff ffffffff ffffffff 
0015512c ffffffff ffffffff ffffffff ffffffff 
0015513c ffffffff ffffffff ffffffff ffffffff 
0015514c ffffffff ffffffff ffffffff ffffffff 
0015515c ffffffff ffffffff ffffffff ffffffff 
0015516c ffffffff ffffffff ffffffff ffffffff 
0015517c ffffffff ffffffff ffffffff ffffffff 
0015518c ffffffff ffffffff ffffffff ffffffff 
0015519c ffffffff ffffffff ffffffff ffffffff 
001551ac ffffffff ffffffff ffffffff ffffffff 
001551bc ffffffff ffffffff ffffffff ffffffff 
001551cc ffffffff ffffffff ffffffff ffffffff 
memory near r4:
110d5fe0 ffffffff ffffffff ffffffff ffffffff 
110d5ff0 ffffffff ffffffff ffffffff ffffffff 
110d6000 ffffffff ffffffff ffffffff ffffffff 
110d6010 ffffffff ffffffff ffffffff ffffffff 
110d6020 ffffffff ffffffff ffffffff ffffffff 
110d6030 ffffffff ffffffff ffffffff ffffffff 
110d6040 ffffffff ffffffff ffffffff ffffffff 
110d6050 ffffffff ffffffff ffffffff ffffffff 
110d6060 ffffffff ffffffff ffffffff ffffffff 
110d6070 ffffffff ffffffff ffffffff ffffffff 
110d6080 ffffffff ffffffff ffffffff ffffffff 
110d6090 ffffffff ffffffff ffffffff ffffffff 
110d60a0 ffffffff ffffffff ffffffff ffffffff 
110d60b0 ffffffff ffffffff ffffffff ffffffff 
110d60c0 ffffffff ffffffff ffffffff ffffffff 
110d60d0 ffffffff ffffffff ffffffff ffffffff 
memory near r5:
001110d8 ffffffff ffffffff ffffffff ffffffff 
001110e8 ffffffff ffffffff ffffffff ffffffff 
001110f8 ffffffff ffffffff ffffffff ffffffff 
00111108 ffffffff ffffffff ffffffff ffffffff 
00111118 ffffffff ffffffff ffffffff ffffffff 
00111128 ffffffff ffffffff ffffffff ffffffff 
00111138 ffffffff ffffffff ffffffff ffffffff 
00111148 ffffffff ffffffff ffffffff ffffffff 
00111158 ffffffff ffffffff ffffffff ffffffff 
00111168 ffffffff ffffffff ffffffff ffffffff 
00111178 ffffffff ffffffff ffffffff ffffffff 
00111188 ffffffff ffffffff ffffffff ffffffff 
00111198 ffffffff ffffffff ffffffff ffffffff 
001111a8 ffffffff ffffffff ffffffff ffffffff 
001111b8 ffffffff ffffffff ffffffff ffffffff 
001111c8 ffffffff ffffffff ffffffff ffffffff 
memory near r8:
000016e0 ffffffff ffffffff ffffffff ffffffff 
000016f0 ffffffff ffffffff ffffffff ffffffff 
00001700 ffffffff ffffffff ffffffff ffffffff 
00001710 ffffffff ffffffff ffffffff ffffffff 
00001720 ffffffff ffffffff ffffffff ffffffff 
00001730 ffffffff ffffffff ffffffff ffffffff 
00001740 ffffffff ffffffff ffffffff ffffffff 
00001750 ffffffff ffffffff ffffffff ffffffff 
00001760 ffffffff ffffffff ffffffff ffffffff 
00001770 ffffffff ffffffff ffffffff ffffffff 
00001780 ffffffff ffffffff ffffffff ffffffff 
00001790 ffffffff ffffffff ffffffff ffffffff 
000017a0 ffffffff ffffffff ffffffff ffffffff 
000017b0 ffffffff ffffffff ffffffff ffffffff 
000017c0 ffffffff ffffffff ffffffff ffffffff 
000017d0 ffffffff ffffffff ffffffff ffffffff 
memory near r9:
77ca2ff0 402dac74 0000001b 6d290b18 00000086 
77ca3000 00000000 00000000 00000001 0000027b 
77ca3010 00000001 77ba8bb8 00000000 77ca4230 
77ca3020 77ca4230 77ca41e0 77ca4250 00000979 
77ca3030 00000000 00000000 00000000 00000000 
77ca3040 77ca42a0 77ea3400 00000400 f9017400 
77ca3050 77ea50cc 00000200 00000240 00000240 
77ca3060 00000240 00000400 f9017400 00000000 
77ca3070 00000010 70cf741c 00000056 77ca4310 
77ca3080 0000000c f1b00000 00000000 7fffffff 
77ca3090 747db829 00000000 003ff3ff 00000a5c 
77ca30a0 f0023b00 00000a60 00000003 00000a64 
77ca30b0 00004000 00000001 7143fb00 77ea3600 
77ca30c0 0f000800 0801e000 170023b8 77ca4360 
77ca30d0 77ca43b0 77ca4400 00000030 001f001f 
77ca30e0 f24000c0 f2400140 00000010 f2400100 
memory near sp:
74daa824 7113f32c 00000000 00000001 923ff3ff 
74daa834 00000000 df0027ad 00000000 00000000 
74daa844 77c362d8 00000000 00000001 00000400 
74daa854 00000400 77ca3010 00000001 00000000 
74daa864 71124a24 77c36a08 3f800000 00000000 
74daa874 7116e5f0 7106e008 00000000 00000000 
74daa884 00000000 00000000 00000000 00000010 
74daa894 00000000 00000000 ffffffff ffffffff 
74daa8a4 7106e008 00000000 00000000 00000100 
74daa8b4 00000001 00000000 3f800000 74b9b9e4 
74daa8c4 7111c5f0 00000100 00000000 00000000 
74daa8d4 6115d008 74b9b16c 00000100 00000002 
74daa8e4 7485b559 00000400 00000400 00000004 
74daa8f4 74b95af4 74b9b9e4 7485b6c1 77c392b0 
74daa904 74daa948 77c28fd8 77c392a0 74daa944 
74daa914 00000004 74b95af4 74838d67 00000000 
code around pc:
71122ee8 0a000004 e2455001 e1a05185 e3855811 
71122ef8 e3855a01 e1833005 e5911044 e3a00d12 
71122f08 e5813124 e3003484 e5810120 e5813128 
71122f18 e3a03e49 e581412c e581b130 e5814134 
71122f28 e5817138 e581213c e5813140 e5812144 
71122f38 e8bd8ff0 e5913044 e3a01d12 e5832124 
71122f48 e5831120 e2811004 e583212c e5831128 
71122f58 e3a01e49 e583b130 e5832134 e5837138 
71122f68 e583213c e5831140 e5832144 e8bd8ff0 
71122f78 e3a0c001 e3a04000 e1a03004 eaffffb1 
71122f88 00044006 e92d47f0 e1a04000 e1a07001 
71122f98 e1a06001 e3a05003 e308ad41 e3019702 
71122fa8 e3018790 e5962214 e3520000 0a00000c 
71122fb8 e5923018 e153000a 07943008 01a00004 
71122fc8 059310f4 0a000005 e1530009 1a000004 
71122fd8 e7943008 e1a00004 e5922044 e59310e8 
code around lr:
71124a04 e2840f4b ebffba13 e5943028 e59d0010 
71124a14 e1a01004 e3530000 0584312c ebfff8d4 
71124a24 e3083cd5 e59d0010 e1a01004 e5843010 
71124a34 e2842f4b e2843044 ebfffb8e ea0000dd 
71124a44 e59f529c e3a00002 e59f3298 e3a02000 
71124a54 e08f5005 e08f3003 e1a01005 ebffb9be 
71124a64 e59d0010 e3001505 e1a02005 e3a03000 
71124a74 eb00171b e3083cdd eafffe9c e3560000 
71124a84 0a0000b6 e5963014 e3530000 0a0000b3 
71124a94 e5960048 e3a0100d ebffb9d9 e5968044 
71124aa4 e3a03000 e5863014 e598a020 e7eb765a 
71124ab4 e1a0aa0a e2877001 e1a0aa2a e28aa001 
71124ac4 e1a0200a e1a00001 e1a01007 eb00603d 
71124ad4 e5963040 e5939004 e598304c e3530001 
71124ae4 e0050099 1a00001b e5960048 e3a0100d 
71124af4 ebffb9c0 e1a01007 e1a0200a e1a0b000 
!@dumpstate -k -t -z -d -o /data/log/dumpstate_app_native -m 13330

Build: samsung/ja3gzc/ja3g:4.2.2/JDQ39/I9500ZCUAMDH:user/release-keys
Hardware: universal5410
Revision: 10
Bootloader: I9500ZCUAMDH
Radio: unknown
Kernel: Linux version 3.4.5-465806 (se.infra@SEP-129) (gcc version 4.6.x-google 20120106 (prerelease) (GCC) ) #1 SMP PREEMPT Mon Apr 29 21:05:55 KST 2013
*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
Build fingerprint: 'samsung/ja3gzc/ja3g:4.2.2/JDQ39/I9500ZCUAMDH:user/release-keys'
Revision: '10'
pid: 13330, tid: 13350, name: SDLThread >>> com.github.urho3d <<<
signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 00000124
r0 00000480 r1 00000000 r2 00000000 r3 001550fe
r4 110d6000 r5 001110f8 r6 00000400 r7 0000048c
r8 00001702 r9 77ca3010 sl 00000400 fp 00000488
ip 00000001 sp 74daa844 lr 71124a24 pc 71122f08 cpsr 20000010
d0 0000000000000000 d1 0000000000000000
d2 3f80000000000000 d3 000000003f800000
d4 0000000000000000 d5 000000003f800000
d6 0000043800000000 d7 3f8000003f800000
d8 0000000000000000 d9 0000000000000000
d10 0000000000000000 d11 0000000000000000
d12 0000000000000000 d13 0000000000000000
d14 0000000000000000 d15 0000000000000000
d16 3fad52658fefd831 d17 3fda8279abb38cf9
d18 3f5798966f109e41 d19 3f985a2eb9a334dc
d20 3f7229781f202a7c d21 3fd6a65513619f6d
d22 0000009000000061 d23 00000090000000b5
d24 3ff500001e5ad586 d25 3fe55567cb1939ea
d26 3fa555555555551c d27 3fc55555555554db
d28 3fe0000000000000 d29 0000000000000001
d30 fff0000000000000 d31 0000000000000040
scr 60000019
backtrace:
#00 pc 00012f08 /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so (SetupFrameBufferZLS+400)
#01 pc 00014a20 /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so (GetFrameBufferCompleteness+3516)
#02 pc 0000c5ec /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so (glClear+52)
#03 pc 00301555 /data/app-lib/com.github.urho3d-1/libUrho3DPlayer.so (Urho3D::Graphics::Clear(unsigned int, Urho3D::Color const&, float, unsigned int)+200)
#04 pc 002ded63 /data/app-lib/com.github.urho3d-1/libUrho3DPlayer.so (Urho3D::View::RenderShadowMap(Urho3D::LightBatchQueue const&)+278)
stack:
74daa804 77cb2f78 
74daa808 00000002 
74daa80c 7116e5f0 /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so (TexFormatFloatDepth)
74daa810 00000008 
74daa814 7117ae9c /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so
74daa818 00000001 
74daa81c 7106e008 
74daa820 00000000 
74daa824 7113f32c /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so (SetupTextureRenderTargetControlWords+856)
74daa828 00000000 
74daa82c 00000001 
74daa830 923ff3ff 
74daa834 00000000 
74daa838 df0027ad 
74daa83c 00000000 
74daa840 00000000 
#00 74daa844 77c362d8 
74daa848 00000000 
74daa84c 00000001 
74daa850 00000400 
74daa854 00000400 
74daa858 77ca3010 
74daa85c 00000001 
74daa860 00000000 
74daa864 71124a24 /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so (GetFrameBufferCompleteness+3520)
#01 74daa868 77c36a08 
74daa86c 3f800000 
74daa870 00000000 
74daa874 7116e5f0 /system/vendor/lib/egl/libGLESv2_POWERVR_SGX544_115.so (TexFormatFloatDepth)
74daa878 7106e008 
74daa87c 00000000 
74daa880 00000000 
74daa884 00000000 
74daa888 00000000 
74daa88c 00000000 
74daa890 00000010 
74daa894 00000000 
74daa898 00000000 
74daa89c ffffffff 
74daa8a0 ffffffff 
74daa8a4 7106e008 
........ ........
#02 74daa8c8 00000100 
74daa8cc 00000000 
74daa8d0 00000000 
74daa8d4 6115d008 
74daa8d8 74b9b16c 
74daa8dc 00000100 
processName:com.github.urho3d
storeEvent : com.github.urho3d SYSTEM_TOMBSTONE

-------------------------

rasteron | 2017-01-02 01:11:30 UTC | #2

You could post your script/code or details of the app that you are trying to run, or at least try the stable 1.5 release build.

[urho3d.github.io/releases/2015/1 ... lease.html](http://urho3d.github.io/releases/2015/11/11/urho3d-1.5-release.html)

-------------------------

