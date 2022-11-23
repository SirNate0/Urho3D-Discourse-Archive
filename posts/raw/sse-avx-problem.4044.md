lexx | 2018-02-24 11:39:00 UTC | #1

I take this here because dont know should I write this to github issue
https://github.com/urho3d/Urho3D/issues/2238#issuecomment-368218426

I was thinking that if .exe is compiled with AVX, then it doesnt work on my quite old processor (above links shows it with cpu-z). 
But all games I have tested, at least starts (slow but starts).

What Im wondering, does these games have fallback to not use AVX and use AVX or different .exes?  I dont remember multiple exes. Can source code be compiled with and without using AVX? 

Because if one compile now trunk and create awesome game, I cant play it. 

Or am I totally off the tracks so to speak?

-------------------------

Pencheff | 2018-02-24 12:00:26 UTC | #2

I can confirm - tested my app on a modern low end Lenovo laptop with Pentium N3540 and NVidia GT820, it doesn't start, main reason is AVX. It will probably run fine with low resolution so maybe it is reasonable to fix this.

-------------------------

weitjong | 2018-02-24 16:06:21 UTC | #3

Also read this post in GitHub. I have asked the question months ago and got zero feedback.

https://github.com/urho3d/Urho3D/issues/2146#issuecomment-343940722

-------------------------

Pencheff | 2020-01-09 16:00:46 UTC | #4

Similar issue on Linux, program compiled with GCC 4.7 on one machine (gitlab CI/CD and docker environment) fires this:
[code]
Program received signal SIGILL, Illegal instruction.
0x0000000000e81051 in Urho3D::StringHashRegister::StringHashRegister(bool) ()
(gdb) bt
#0  0x0000000000e81051 in Urho3D::StringHashRegister::StringHashRegister(bool) ()
#1  0x0000000000e875cc in Urho3D::GetEventNameRegister() ()
#2  0x000000000080abcd in _GLOBAL__sub_I_player_application.cpp ()
#3  0x0000000001e9021d in __libc_csu_init ()
#4  0x00007fffedeb7150 in __libc_start_main (main=0x80e4b0 <main>, argc=2, argv=0x7fffffffe428, init=
    0x1e901d0 <__libc_csu_init>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffe418)
    at ../csu/libc-start.c:264
#5  0x000000000089239f in _start ()
[/code]

The machine it is running on has **Intel(R) Pentium(R) CPU G630T @ 2.30GHz**:
[code]
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              2
On-line CPU(s) list: 0,1
Thread(s) per core:  1
Core(s) per socket:  2
Socket(s):           1
NUMA node(s):        1
Vendor ID:           GenuineIntel
CPU family:          6
Model:               42
Model name:          Intel(R) Pentium(R) CPU G630T @ 2.30GHz
Stepping:            7
CPU MHz:             2294.638
CPU max MHz:         2300,0000
CPU min MHz:         1600,0000
BogoMIPS:            4589.27
Virtualization:      VT-x
L1d cache:           32K
L1i cache:           32K
L2 cache:            256K
L3 cache:            3072K
NUMA node0 CPU(s):   0,1
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave lahf_lm epb tpr_shadow vnmi flexpriority ept vpid xsaveopt dtherm arat pln pts
[/code]

There is no AVX on the target CPU, but there is AVX on the CI/CD machine. Any help will be appreciated, in the meantime I'm trying to find the problem myself.

-------------------------

weitjong | 2020-01-10 09:02:38 UTC | #5

By default our build system will try use the "native" instruction set of the build/host machine. If you want to target lower spec machine than your build/host then you should use the "URHO3D_DEPLOYMENT_TARGET" build option. This is quite similar in concept when targeting Apple platforms, where you need to specify the deployment target build option correctly. See https://urho3d.github.io/documentation/HEAD/_building.html#Build_Options for more detail.

-------------------------

Pencheff | 2020-01-09 18:22:34 UTC | #6

Thank you @weitjong, that fixed it. I wonder how I missed something that important, it even has the deployment keyword in it .

-------------------------

