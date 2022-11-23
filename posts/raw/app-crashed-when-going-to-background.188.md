att | 2017-01-02 00:58:44 UTC | #1

Hi,
I upgrade the engine code and run my demo, but when the demo go background, it crashed, this is the logcat, anybody can help me? thank you,

I/WindowManager(  591): Screen frozen for +232ms due to Window{657fd150 u0 com.android.systemui/com.android.systemui.recent.RecentsActivity}
I/DEBUG   (  171): *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
I/DEBUG   (  171): Build fingerprint: 'google/occam/mako:4.4.2/KOT49H/937116:user/release-keys'
I/DEBUG   (  171): Revision: '11'
I/DEBUG   (  171): pid: 15094, tid: 15120, name: SDLThread  >>> com.github.urho3d <<<
I/DEBUG   (  171): signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 00000168
I/DEBUG   (  171):     r0 48876a04  r1 533ec2d7  r2 688f08cb  r3 00000168
I/DEBUG   (  171):     r4 4ad09d98  r5 49906558  r6 48876a08  r7 48876a04
I/DEBUG   (  171):     r8 00000000  r9 00000000  sl 48761b18  fp 00000000
I/DEBUG   (  171):     ip 48876a04  sp 488769b8  lr 485791c9  pc 485f3b20  cpsr 00090030
I/DEBUG   (  171):     d0  6e65704f206f7420  d1  5041205345204c47
I/DEBUG   (  171):     d2  6e20687469772049  d3  6e6572727563206f
I/DEBUG   (  171):     d4  7865746e6f632074  d5  6567676f6c282074
I/DEBUG   (  171):     d6  702065636e6f2064  d7  3f8000003f800000
I/DEBUG   (  171):     d8  4440000000000000  d9  0000000000000000
I/DEBUG   (  171):     d10 0000000000000000  d11 0000000000000000
I/DEBUG   (  171):     d12 0000000000000000  d13 0000000000000000
I/DEBUG   (  171):     d14 0000000000000000  d15 0000000000000000
I/DEBUG   (  171):     d16 416efe4844145530  d17 3f925fc4748856e9
I/DEBUG   (  171):     d18 4059000000000000  d19 c000000000000000
I/DEBUG   (  171):     d20 3f811110896efbb2  d21 000001ff000001ff
I/DEBUG   (  171):     d22 0000000000000000  d23 3ff0000000000000
I/DEBUG   (  171):     d24 416fffffe0000000  d25 3e9b8aef7b944000
I/DEBUG   (  171):     d26 3e9b8aef7b944000  d27 3fb18bc451eed100
I/DEBUG   (  171):     d28 3f991df3908c33ce  d29 3fac335e0ef66a24
I/DEBUG   (  171):     d30 3f1618a9e702cd8d  d31 3fd5eb17d03928a5
I/DEBUG   (  171):     scr 60000013
I/DEBUG   (  171): 
I/DEBUG   (  171): backtrace:
I/DEBUG   (  171):     #00  pc 00276b20  /data/app-lib/com.github.urho3d-1/libcarparking3d.so (Urho3D::View::ExecuteRenderPathCommands()+483)
I/DEBUG   (  171):     #01  pc 001fc1c5  /data/app-lib/com.github.urho3d-1/libcarparking3d.so (Urho3D::HiresTimer::Reset()+8)
I/DEBUG   (  171): 
I/DEBUG   (  171): stack:
I/DEBUG   (  171):          48876978  44145360  [anon:libc_malloc]
I/DEBUG   (  171):          4887697c  486d809f  /data/app-lib/com.github.urho3d-1/libcarparking3d.so (__gnu_ldivmod_helper+14)
I/DEBUG   (  171):          48876980  487659d4  
I/DEBUG   (  171):          48876984  487659c0  
I/DEBUG   (  171):          48876988  49ff1c18  [anon:libc_malloc]
I/DEBUG   (  171):          4887698c  48718161  /data/app-lib/com.github.urho3d-1/libcarparking3d.so
I/DEBUG   (  171):          48876990  48718161  /data/app-lib/com.github.urho3d-1/libcarparking3d.so
I/DEBUG   (  171):          48876994  48221e68  [anon:libc_malloc]
I/DEBUG   (  171):          48876998  533ec2d7  
I/DEBUG   (  171):          4887699c  0009e50b  
I/DEBUG   (  171):          488769a0  48221e68  [anon:libc_malloc]
I/DEBUG   (  171):          488769a4  484f708b  /data/app-lib/com.github.urho3d-1/libcarparking3d.so (Urho3D::AutoProfileBlock::AutoProfileBlock(Urho3D::Profiler*, char const*)+28)
I/DEBUG   (  171):          488769a8  4ad09d98  [anon:libc_malloc]
I/DEBUG   (  171):          488769ac  49906558  [anon:libc_malloc]
I/DEBUG   (  171):          488769b0  48876a08  [stack:15120]
I/DEBUG   (  171):          488769b4  485f3afd  /data/app-lib/com.github.urho3d-1/libcarparking3d.so (Urho3D::View::ExecuteRenderPathCommands()+448)
I/DEBUG   (  171):     #00  488769b8  49ff19b0  [anon:libc_malloc]
I/DEBUG   (  171):          488769bc  488769d4  [stack:15120]
I/DEBUG   (  171):          488769c0  4ad09d98  [anon:libc_malloc]
I/DEBUG   (  171):          488769c4  00000000  
I/DEBUG   (  171):          488769c8  00000006  
I/DEBUG   (  171):          488769cc  485f3315  /data/app-lib/com.github.urho3d-1/libcarparking3d.so (Urho3D::View::IsNecessary(Urho3D::RenderPathCommand const&)+42)
I/DEBUG   (  171):          488769d0  4ad09d98  [anon:libc_malloc]
I/DEBUG   (  171):          488769d4  e653591e  
I/DEBUG   (  171):          488769d8  00000000  
I/DEBUG   (  171):          488769dc  4ad09db0  [anon:libc_malloc]
I/DEBUG   (  171):          488769e0  00000001  
I/DEBUG   (  171):          488769e4  485f3443  /data/app-lib/com.github.urho3d-1/libcarparking3d.so (Urho3D::View::AllocateScreenBuffers()+168)
I/DEBUG   (  171):          488769e8  00000003  
I/DEBUG   (  171):          488769ec  48876a00  [stack:15120]
I/DEBUG   (  171):          488769f0  48876a04  [stack:15120]
I/DEBUG   (  171):          488769f4  4857b0b3  /data/app-lib/com.github.urho3d-1/libcarparking3d.so (Urho3D::HashSet<Urho3D::Object*>::~HashSet()+86)
I/DEBUG   (  171): 
I/DEBUG   (  171): memory near r0:
I/DEBUG   (  171):     488769e4 485f3443 00000003 48876a00 48876a04  
I/DEBUG   (  171):     488769f4 4857b0b3 49906ca8 4871819b 48221e68  
I/DEBUG   (  171):     48876a04 48221e68 3f800000 3f800000 3f800000  
I/DEBUG   (  171):     48876a14 3f800000 4826f78c 4ad09d98 4ad09da8  
I/DEBUG   (  171):     48876a24 48761b18 4826f430 48876a9c 48876a98  
I/DEBUG   (  171):     48876a34 00000002 48768dac 485f3ff5 4a3e9384  
I/DEBUG   (  171):     48876a44 4a3e9384 482533e8 48550a89 482533e8  
I/DEBUG   (  171):     48876a54 00000000 482539ac 48253328 48253338  
I/DEBUG   (  171):     48876a64 48253328 48253338 00000008 4826f430  
I/DEBUG   (  171):     48876a74 48553c8f 48876a88 4857b609 00000000  
I/DEBUG   (  171):     48876a84 d473d803 4a4776c4 4a4776c4 48768d94  
I/DEBUG   (  171):     48876a94 48768d70 48221e68 eccb3364 0000000d  
I/DEBUG   (  171):     48876aa4 48876ad4 44145e68 48876acc 48761b18  
I/DEBUG   (  171):     48876ab4 48240590 44145530 600bd8f0 48876be0  
I/DEBUG   (  171):     48876ac4 485f8d69 44145e68 00008183 00000dd5  
I/DEBUG   (  171):     48876ad4 48221e68 44145e68 48224ba8 44145f30  
I/DEBUG   (  171): 
I/DEBUG   (  171): memory near r1:
I/DEBUG   (  171):     533ec2b4 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171):     533ec2c4 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171):     533ec2d4 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171):     533ec2e4 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171):     533ec2f4 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171):     533ec304 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171):     533ec314 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171):     533ec324 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171):     533ec334 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171):     533ec344 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171):     533ec354 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171):     533ec364 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171):     533ec374 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171):     533ec384 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171):     533ec394 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171):     533ec3a4 ffffffff ffffffff ffffffff ffffffff  
I/DEBUG   (  171): 
I/DEBUG   (  171): memory near r2:
I/DEBUG   (  171):     688f08a8 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     688f08b8 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     688f08c8 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     688f08d8 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     688f08e8 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     688f08f8 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     688f0908 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     688f0918 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     688f0928 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     688f0938 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     688f0948 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     688f0958 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     688f0968 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     688f0978 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     688f0988 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     688f0998 00000000 00000000 00000000 00000000  
I/DEBUG   (  171): 
I/DEBUG   (  171): memory near r4:
I/DEBUG   (  171):     4ad09d78 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     4ad09d88 00000000 00000000 00000000 000001b3  
I/DEBUG   (  171):     4ad09d98 4875af98 482f3728 44145b88 00000000  
I/DEBUG   (  171):     4ad09da8 48240590 4823f360 48253328 48252ca8  
I/DEBUG   (  171):     4ad09db8 00000000 00000000 00000000 49926de8  
I/DEBUG   (  171):     4ad09dc8 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     4ad09dd8 00000000 00000000 00000000 00000000  
I/DEBUG   (  171):     4ad09de8 00000000 00000000 00000000 000004ac  
I/DEBUG   (  171):     4ad09df8 00000300 000004ac 00000300 000004ac  
I/DEBUG   (  171):     4ad09e08 00000300 00000018 3dcccccd 000004ac  
I/DEBUG   (  171):     4ad09e18 00000300 00000000 c3fb4b49 43f9589b  
I/DEBUG   (  171):     4ad09e28 00000002 00001388 00000002 00000000  
I/DEBUG   (  171):     4ad09e38 00000100 00000101 4990c870 00000001  
I/DEBUG   (  171):     4ad09e48 00000001 482f3bf0 00000001 00000001  
I/DEBUG   (  171):     4ad09e58 482f3c00 00000001 00000001 482f1920  
I/DEBUG   (  171):     4ad09e68 00000003 00000003 482f63e8 00000000  
I/DEBUG   (  171): 
I/DEBUG   (  171): memory near r5:
I/DEBUG   (  171):     49906538 00000038 0000001b 74786554 73657275  
I/DEBUG   (  171):     49906548 6f70532f 6e702e74 00000067 000009cb  
I/DEBUG   (  171):     49906558 00000000 00000000 487694b0 00000001  
I/DEBUG   (  171):     49906568 00000001 00000000 00000000 487694b0  
I/DEBUG   (  171):     49906578 00000000 00000000 487694b0 00000000  
I/DEBUG   (  171):     49906588 00000000 487694b0 00000000 00000000  
I/DEBUG   (  171):     49906598 487694b0 00000000 00000000 487694b0  
I/DEBUG   (  171):     499065a8 00000000 00000000 487694b0 00000000  
I/DEBUG   (  171):     499065b8 00000000 487694b0 00000000 00000000  
I/DEBUG   (  171):     499065c8 487694b0 00000000 00000000 487694b0  
I/DEBUG   (  171):     499065d8 00000000 00000000 487694b0 00000000  
I/DEBUG   (  171):     499065e8 00000000 487694b0 00000000 00000000  
I/DEBUG   (  171):     499065f8 487694b0 00000000 00000000 487694b0  
I/DEBUG   (  171):     49906608 00000000 00000000 487694b0 00000000  
I/DEBUG   (  171):     49906618 00000000 487694b0 00000000 00000000  
I/DEBUG   (  171):     49906628 487694b0 00000000 00000000 487694b0  
I/DEBUG   (  171): 
I/DEBUG   (  171): memory near r6:
I/DEBUG   (  171):     488769e8 00000003 48876a00 48876a04 4857b0b3  
I/DEBUG   (  171):     488769f8 49906ca8 4871819b 48221e68 48221e68  
I/DEBUG   (  171):     48876a08 3f800000 3f800000 3f800000 3f800000  
I/DEBUG   (  171):     48876a18 4826f78c 4ad09d98 4ad09da8 48761b18  
I/DEBUG   (  171):     48876a28 4826f430 48876a9c 48876a98 00000002  
I/DEBUG   (  171):     48876a38 48768dac 485f3ff5 4a3e9384 4a3e9384  
I/DEBUG   (  171):     48876a48 482533e8 48550a89 482533e8 00000000  
I/DEBUG   (  171):     48876a58 482539ac 48253328 48253338 48253328  
I/DEBUG   (  171):     48876a68 48253338 00000008 4826f430 48553c8f  
I/DEBUG   (  171):     48876a78 48876a88 4857b609 00000000 d473d803  
I/DEBUG   (  171):     48876a88 4a4776c4 4a4776c4 48768d94 48768d70  
I/DEBUG   (  171):     48876a98 48221e68 eccb3364 0000000d 48876ad4  
I/DEBUG   (  171):     48876aa8 44145e68 48876acc 48761b18 48240590  
I/DEBUG   (  171):     48876ab8 44145530 600bd8f0 48876be0 485f8d69  
I/DEBUG   (  171):     48876ac8 44145e68 00008183 00000dd5 48221e68  
I/DEBUG   (  171):     48876ad8 44145e68 48224ba8 44145f30 48224940  
I/DEBUG   (  171): 
I/DEBUG   (  171): memory near r7:
I/DEBUG   (  171):     488769e4 485f3443 00000003 48876a00 48876a04  
I/DEBUG   (  171):     488769f4 4857b0b3 49906ca8 4871819b 48221e68  
I/DEBUG   (  171):     48876a04 48221e68 3f800000 3f800000 3f800000  
I/DEBUG   (  171):     48876a14 3f800000 4826f78c 4ad09d98 4ad09da8  
I/DEBUG   (  171):     48876a24 48761b18 4826f430 48876a9c 48876a98  
I/DEBUG   (  171):     48876a34 00000002 48768dac 485f3ff5 4a3e9384  
I/DEBUG   (  171):     48876a44 4a3e9384 482533e8 48550a89 482533e8  
I/DEBUG   (  171):     48876a54 00000000 482539ac 48253328 48253338  
I/DEBUG   (  171):     48876a64 48253328 48253338 00000008 4826f430  
I/DEBUG   (  171):     48876a74 48553c8f 48876a88 4857b609 00000000  
I/DEBUG   (  171):     48876a84 d473d803 4a4776c4 4a4776c4 48768d94  
I/DEBUG   (  171):     48876a94 48768d70 48221e68 eccb3364 0000000d  
I/DEBUG   (  171):     48876aa4 48876ad4 44145e68 48876acc 48761b18  
I/DEBUG   (  171):     48876ab4 48240590 44145530 600bd8f0 48876be0  
I/DEBUG   (  171):     48876ac4 485f8d69 44145e68 00008183 00000dd5  
I/DEBUG   (  171):     48876ad4 48221e68 44145e68 48224ba8 44145f30  
I/DEBUG   (  171): 
I/DEBUG   (  171): memory near sl:
I/DEBUG   (  171):     48761af8 4875e6a0 486d8809 486d880f 486d8815  
I/DEBUG   (  171):     48761b08 40085091 486efe8c 486d9e3c 486a65bc  
I/DEBUG   (  171):     48761b18 00000000 00000000 00000000 4009e799  
I/DEBUG   (  171):     48761b28 400df8d4 40083920 400723b1 45ec80fb  
I/DEBUG   (  171):     48761b38 45ec8127 400963b0 400836b4 40083c01  
I/DEBUG   (  171):     48761b48 40098f85 40083bed 40097fcd 400962bc  
I/DEBUG   (  171):     48761b58 40087ef5 400980dc 4009928c 40097b70  
I/DEBUG   (  171):     48761b68 400b0025 400affd9 400a1219 40099283  
I/DEBUG   (  171):     48761b78 400aff13 400a12b1 400a16a1 4009f609  
I/DEBUG   (  171):     48761b88 400a0d31 400a0e8d 400a0e89 400a0fb5  
I/DEBUG   (  171):     48761b98 40098138 400afe9d 400a119d 400a11c5  
I/DEBUG   (  171):     48761ba8 4009e5ed 4009e535 400e0c10 400d81a8  
I/DEBUG   (  171):     48761bb8 400d7688 400d7df0 400e1a08 400e1f60  
I/DEBUG   (  171):     48761bc8 400e23a0 400e5460 400dd730 400ddc38  
I/DEBUG   (  171):     48761bd8 400e7ad8 400e7dc0 400e8210 400df6dc  
I/DEBUG   (  171):     48761be8 4008bec1 40083c15 40083c29 4009eaf9  
I/DEBUG   (  171): 
I/DEBUG   (  171): memory near ip:
I/DEBUG   (  171):     488769e4 485f3443 00000003 48876a00 48876a04  
I/DEBUG   (  171):     488769f4 4857b0b3 49906ca8 4871819b 48221e68  
I/DEBUG   (  171):     48876a04 48221e68 3f800000 3f800000 3f800000  
I/DEBUG   (  171):     48876a14 3f800000 4826f78c 4ad09d98 4ad09da8  
I/DEBUG   (  171):     48876a24 48761b18 4826f430 48876a9c 48876a98  
I/DEBUG   (  171):     48876a34 00000002 48768dac 485f3ff5 4a3e9384  
I/DEBUG   (  171):     48876a44 4a3e9384 482533e8 48550a89 482533e8  
I/DEBUG   (  171):     48876a54 00000000 482539ac 48253328 48253338  
I/DEBUG   (  171):     48876a64 48253328 48253338 00000008 4826f430  
I/DEBUG   (  171):     48876a74 48553c8f 48876a88 4857b609 00000000  
I/DEBUG   (  171):     48876a84 d473d803 4a4776c4 4a4776c4 48768d94  
I/DEBUG   (  171):     48876a94 48768d70 48221e68 eccb3364 0000000d  
I/DEBUG   (  171):     48876aa4 48876ad4 44145e68 48876acc 48761b18  
I/DEBUG   (  171):     48876ab4 48240590 44145530 600bd8f0 48876be0  
I/DEBUG   (  171):     48876ac4 485f8d69 44145e68 00008183 00000dd5  
I/DEBUG   (  171):     48876ad4 48221e68 44145e68 48224ba8 44145f30  
I/DEBUG   (  171): 
I/DEBUG   (  171): memory near sp:
I/DEBUG   (  171):     48876998 533ec2d7 0009e50b 48221e68 484f708b  
I/DEBUG   (  171):     488769a8 4ad09d98 49906558 48876a08 485f3afd  
I/DEBUG   (  171):     488769b8 49ff19b0 488769d4 4ad09d98 00000000  
I/DEBUG   (  171):     488769c8 00000006 485f3315 4ad09d98 e653591e  
I/DEBUG   (  171):     488769d8 00000000 4ad09db0 00000001 485f3443  
I/DEBUG   (  171):     488769e8 00000003 48876a00 48876a04 4857b0b3  
I/DEBUG   (  171):     488769f8 49906ca8 4871819b 48221e68 48221e68  
I/DEBUG   (  171):     48876a08 3f800000 3f800000 3f800000 3f800000  
I/DEBUG   (  171):     48876a18 4826f78c 4ad09d98 4ad09da8 48761b18  
I/DEBUG   (  171):     48876a28 4826f430 48876a9c 48876a98 00000002  
I/DEBUG   (  171):     48876a38 48768dac 485f3ff5 4a3e9384 4a3e9384  
I/DEBUG   (  171):     48876a48 482533e8 48550a89 482533e8 00000000  
I/DEBUG   (  171):     48876a58 482539ac 48253328 48253338 48253328  
I/DEBUG   (  171):     48876a68 48253338 00000008 4826f430 48553c8f  
I/DEBUG   (  171):     48876a78 48876a88 4857b609 00000000 d473d803  
I/DEBUG   (  171):     48876a88 4a4776c4 4a4776c4 48768d94 48768d70  
I/DEBUG   (  171): 
I/DEBUG   (  171): code around pc:
I/DEBUG   (  171):     485f3b00 f8d59314 9315311c 3120f8d5 f8d59316  
I/DEBUG   (  171):     485f3b10 93173124 3131f895 6b63b12b 73b4f503  
I/DEBUG   (  171):     485f3b20 e886cb0f 4620000f f7fd4629 f104fce5  
I/DEBUG   (  171):     485f3b30 f7040010 f8d5fb25 4632312c f8d59300  
I/DEBUG   (  171):     485f3b40 f8d51114 f74e3128 e054fbe5 0314f105  
I/DEBUG   (  171):     485f3b50 f5044630 930b72b6 92074619 fde8f73e  
I/DEBUG   (  171):     485f3b60 46319807 fb80f7ff fda7f7f9 f0402800  
I/DEBUG   (  171):     485f3b70 46208150 fabaf703 4afbaf13 447a4601  
I/DEBUG   (  171):     485f3b80 f7034638 4620fa74 f7fd4629 4620fcb5  
I/DEBUG   (  171):     485f3b90 f7fc4629 f104fbe1 46400810 faf0f704  
I/DEBUG   (  171):     485f3ba0 f8d36aa3 f74c11c8 4640f8ba fae8f704  
I/DEBUG   (  171):     485f3bb0 6aa09010 72f8f500 f890920f 910e123f  
I/DEBUG   (  171):     485f3bc0 f815f779 6aa04680 fd66f778 46439000  
I/DEBUG   (  171):     485f3bd0 990e9810 f74c9a0f 4630f8a3 f73e990b  
I/DEBUG   (  171):     485f3be0 9807fda7 f7ff4631 4621fb3f 2132f895  
I/DEBUG   (  171):     485f3bf0 f0032300 4638fbff 4620e109 fa76f703  
I/DEBUG   (  171): 
I/DEBUG   (  171): code around lr:
I/DEBUG   (  171):     485791a8 b002fef5 81f0e8bd 000f4240 001e89aa  
I/DEBUG   (  171):     485791b8 ffffed74 4604b513 46682100 ef94f745  
I/DEBUG   (  171):     485791c8 48049a01 17d39900 2301fbc0 2300e9c4  
I/DEBUG   (  171):     485791d8 bd10b002 000f4240 4604b510 ffeaf7ff  
I/DEBUG   (  171):     485791e8 bd104620 4606b573 ff7cf77d 90004604  
I/DEBUG   (  171):     485791f8 4913b160 44796900 fee0f77d 61204605  
I/DEBUG   (  171):     48579208 f7ff3008 6a2bffd7 622b3301 a9024b0d  
I/DEBUG   (  171):     48579218 447b4630 f841681b f0023d04 4668f9ce  
I/DEBUG   (  171):     48579228 fb3ef77d f77d4630 b138ff5d f90cf001  
I/DEBUG   (  171):     48579238 4668e004 fb34f77d ef7af12c bd70b002  
I/DEBUG   (  171):     48579248 0019464e 001f0222 41f3e92d 69434604  
I/DEBUG   (  171):     48579258 1c5a6181 6142bf12 61433302 ff42f77d  
I/DEBUG   (  171):     48579268 f001b108 4620fadf ff3cf77d 90004605  
I/DEBUG   (  171):     48579278 491fb160 44796900 fea0f77d 61284606  
I/DEBUG   (  171):     48579288 f7ff3008 6a33ff97 62333301 f0014620  
I/DEBUG   (  171):     48579298 4918fca5 44794606 f948f768 46072101

-------------------------

Canardian | 2017-01-02 00:58:45 UTC | #2

Did you recompile also your libcarparking3d.so?

-------------------------

cadaver | 2017-01-02 00:58:45 UTC | #3

I can confirm that I'm seeing a black screen by using the home key and then going back to the app, or when switching to another app in the meanwhile.

This is why I hate SDL updates, they typically always change something related to the background / minimizing behavior, which introduces subtle problems or crashes.

EDIT: it's not the SDL update, the engine worked after that, but the crash has been introduced by Urho3D code later.

-------------------------

gasp | 2017-01-02 00:58:45 UTC | #4

i can confirm i get crash each time i switch app or go back to the main menu

-------------------------

weitjong | 2017-01-02 00:58:45 UTC | #5

It runs fine for me using the latest version from GitHub repo.

-------------------------

cadaver | 2017-01-02 00:58:45 UTC | #6

I don't fully understand what caused the crash; it started happening onwards from the commit that fixed null exceptions in OpenGL sceneless renderpath handling (changed some code flow and added a bool variable to the View class.) That commit is now reverted and the fixes done without the extra variable, and for me eg. NinjaSnowWar is minimizing and restoring cleanly now too.

-------------------------

gasp | 2017-01-02 00:58:45 UTC | #7

last GitHUb repo is fine (have to switch TranslateRelative => Translate but it's fine :p)

it's normal to not store the state of the scene when going back to the app in android ?

-------------------------

weitjong | 2017-01-02 00:58:45 UTC | #8

It depends on whether you are just pausing/resuming or stopping/restarting the activity. Destroying the activity would for sure keep no state unless it is being persisted externally.

-------------------------

