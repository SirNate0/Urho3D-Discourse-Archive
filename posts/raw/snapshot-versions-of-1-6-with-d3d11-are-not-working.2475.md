cusean | 2017-01-02 01:15:40 UTC | #1

Hello. I'm new to Urho3d. 
When I launch samples with d3d11 stable version 1.6 samples its works correctly, but snapshot version samples have no graphics. So how to use Urho3d 1.6 with MinGW-64 with Direct3D11?
MinGW-64 1.6 snapshot builds with Direct3D11 have ERROR: Failed to reflect vertex shader's input signature (HRESULT 80070057)
My system is Win8 x64 GTX 460 MinGW-64 x86_64-6.2.0-posix-seh-rt_v5-rev1

-------------------------

cadaver | 2017-01-02 01:15:40 UTC | #2

I believe this is some mismatch happening when linking against the shader compiler library. 

Perhaps trying some other MinGW versions or builds could help. Unfortunately the only solution which I know to work for certain is to use MSVC for D3D11 work.

-------------------------

