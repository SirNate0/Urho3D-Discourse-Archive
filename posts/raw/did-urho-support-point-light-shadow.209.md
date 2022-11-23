att | 2017-01-02 00:58:53 UTC | #1

Hi,
I created a point light and set it to shadow true, but nothing happened on my nexus4 device.
Dose the urho3d engine support point light shadow, or only support directional light shadow?

-------------------------

cadaver | 2017-01-02 00:58:53 UTC | #2

On mobiles only directional lights (1 cascade) and spot light shadows are supported. Point light shadows require two extra texture units for cube map lookups, which already exceed the typical 8 texture unit limit on GLES2 devices, and the shader math is heavy and induces dependent texture reads so you would not be looking at good performance.

-------------------------

