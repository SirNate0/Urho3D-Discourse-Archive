toliaferrode | 2017-01-02 01:10:35 UTC | #1

Hi, I'm relatively new to Urho3D and am just trying to master compiling it.

I started with compiling on PC, and it works as expected. When I try to compile on the Pi, it compiles, but when I try to run the samples I get "Could not initialize EGL." I tried searching for my problem but nothing came up.

I might be putting the cart before the horse, but my game idea eventually requires the Raspberry Pi. Any help would be greatly appreciated, thanks.

-------------------------

weitjong | 2017-01-02 01:10:35 UTC | #2

It's a long shot. The minimum requirement is stated in our online documentation.
[quote]Raspberry Pi: Model B revision 2.0 with at least 128 MB of 512 MB SDRAM allocated for GPU.[/quote]
Have you changed the configuration of your Pi to allocate more memory for GPU?

-------------------------

toliaferrode | 2017-01-02 01:10:37 UTC | #3

Thanks for the reply. I realized that I only had 64 MB for the GPU. I changed it to 128, 256, and even 512 and it still says the same thing.

It also says "DR12: xcb_connect failed." twice and "DR13: xcb_connect failed."

-------------------------

toliaferrode | 2017-01-02 01:10:37 UTC | #4

I should note that I got the precompiled binary distribution to work months ago.

-------------------------

weitjong | 2017-01-02 01:10:38 UTC | #5

Were you building the binaries from source this time round? Or they are pre-built version again? We have upgraded the sysroot for RPI CI build to Raspbian Jessie just recently. Is your RPI still running Wheezy?

-------------------------

toliaferrode | 2017-01-02 01:10:38 UTC | #6

Hey again. I built it from source and am on Raspbian Jessie.

Decided to re-test the pre-built package again today and it works like a charm.

-------------------------

