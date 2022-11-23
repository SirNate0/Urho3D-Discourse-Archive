Pencheff | 2020-05-26 09:56:23 UTC | #1

I have a bunch of old machines that need to run my Urho3D based app on Windows. Some of them don't support **SM 3.0**, which is required in **D3D9Graphics.cpp**:
[code]
if (impl_->deviceCaps_.PixelShaderVersion < D3DPS_VERSION(3, 0))
{
    URHO3D_LOGERROR("Shader model 3.0 display adapter is required");
    return false;
}
[/code]

I will probably disable this check in my code and test, however the machines are remote (client) hardware and I don't have access, so testing will require some time. If anyone knows if Urho3D can function without this requirement, please answer.

PS: I'm not using anything fancy as graphics, I'm mostly using DiffUnlit shaders

-------------------------

cadaver | 2020-05-26 13:50:23 UTC | #2

The SM2 requirements are very limiting, especially in pixel shaders. The current shaders will definitely not work without modifications! If you want it to work for real, you should go back in revision history to the time when Urho3D actually aimed for SM2 compatibility, and copy at least the shaders from there.

It was commit hash 88080dad3122cebe2450f276f621d172a485aa0b in February 2015 that removed separate SM2 support and removed the limits from shaders.

Note that you can force shader compilation for vs2 / ps2 profile, to test even on newer GPUs. Urho3D used to do this with the "forceSM2" flag. However actual SM2 GPUs may be otherwise limited, which that flag doesn't catch or emulate.

-------------------------

Pencheff | 2020-05-26 13:50:19 UTC | #3

Thanks, @cadaver. Looking at the commit, it could turn out that I only have to revert  the SM2/3 detection and use it when compiling the shaders. If I'm not using any lighting it would work fine. I will give it a try.

-------------------------

