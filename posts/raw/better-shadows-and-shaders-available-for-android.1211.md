rasteron | 2017-01-02 01:06:05 UTC | #1

Hey gang,

It's been a while since I experimented some project with Android build and now I'm trying it out again. Tested some samples and the build process worked flawlessly. Now I was wondering how can I improve shadow rendering or quality and what available shaders that can be used. 

I have tried it with emulator and my new android phone which runs most recent 2D/3D games. Using the default player with as scripts.

Thanks.

-------------------------

rasteron | 2017-01-02 01:06:05 UTC | #2

I was able to sort out with snowwar to get to default quality by omitting android for experiment and it works ok..

[code]    // On mobile devices render the shadowmap first. Also adjust the shadow quality for performance
    String platform = GetPlatform();    
    if (platform == "iOS" || platform == "Raspberry Pi")
    {
        renderer.reuseShadowMaps = false;
        renderer.shadowQuality = SHADOWQUALITY_LOW_16BIT;[/code]

-------------------------

