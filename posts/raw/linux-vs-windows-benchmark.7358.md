1vanK | 2022-11-18 02:32:37 UTC | #1

Useless but interesting test.

![2_dx11|639x500](upload://dQI10UCRfIjzNwbwOdOHruvGwAH.jpeg)

Application: 99_Benchmark 64 bit release

# Linux Mint 20.3 Cinnamon

NVIDIA proprietary drivers, X11

Compiler: GCC GNU 9.4.0

Static Scene: 4251 FPS (min: 4062, max: 4308)
Orcs & Humans: 1205 FPS (min: 430, max: 2272)
Molecules: 341 FPS (min: 340, max: 344)

# Windows

## Compiler: Visual Studio 2022

### D3D11

Static Scene: 3351 FPS (min: 3324, max: 3373) - GPU usage = 71% (CPU is bottleneck)
**Orcs & Humans: 1434 FPS (min: 529, max: 2613) - GPU usage = 98% (GPU is bottleneck)**
Molecules: 277 FPS (min: 257, max: 287) - GPU usage = 30% (heavy game logic, CPU is bottleneck)

### OpenGL

Static Scene: 2247 FPS (min: 2232, max: 2260) - GPU usage = 60% (CPU is bottleneck)
Orcs & Humans: 1166 FPS (min: 431, max: 2040) - GPU usage = 91-97% (CPU is bottleneck)
Molecules: 278 FPS (min: 262, max: 289) - GPU usage = 15% (?) (CPU is bottleneck)

## Compiler: MinGW (MSYS2, GNU 12.1.0)

### D3D11

Static Scene: 3299 FPS (min: 3263, max: 3333) - GPU usage = 70% (CPU is bottleneck)
**Orcs & Humans: 1419 FPS (min: 528, max: 2520) - GPU usage = 100% (GPU is bottleneck)**
Molecules: 287 FPS (min: 273, max: 298) - GPU usage = 30% (CPU is bottlenecks)

### OpenGL

Static Scene: 2226 FPS (min: 2206, max: 2240) - GPU usage = 58% (CPU is bottleneck)
Orcs & Humans: 1167 FPS (min: 438, max: 2039) - GPU usage = 92-97% (CPU is bottleneck)
Molecules: 308 FPS (min: 289, max: 324) - GPU usage = 39% (CPU is bottleneck)

# Conclusions

* Draw calls of OpenGL loads CPU much more than DX11, so the processor becomes a bottleneck. Vulkan can help here.

* The synthetic test remains a synthetic test, and when in a real game CPU process complex game logic, and GPU renders complex scene, then the difference between the APIs will be minimal. For simple scenes, FPS is always high, so there is also no advantage of one API over another.

* Linux have very good compiler and fast OpenGL implementation (but Dx11 stays faster Linux OpenGL). Vulkan can help here again.

-------------------------

1vanK | 2022-11-18 02:48:23 UTC | #2

Application: 42_PBRMaterials

Compiler: MinGW

OpenGL: FPS= 411, GPU usage = 82% (CPU is bottleneck)
D3D11: FPS = 591, GPU usage = 98%

-------------------------

1vanK | 2022-11-18 03:12:05 UTC | #3

Or DSA can help

https://www.youtube.com/watch?v=cadzqhqPqVA

-------------------------

