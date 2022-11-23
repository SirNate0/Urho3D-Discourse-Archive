ucupumar | 2017-01-02 00:59:14 UTC | #1

From Water.xml material, I found this:
[code]<!-- The water example will assign the reflection texture to the diffuse unit -->
<!-- The engine will automatically assign the refraction (viewport) texture to the environment unit during refract pass --> [/code]
After trying to use the material, it looks like diffuse map only assigned if there is object using skybox material in scene.
And after investigated some more, assigned diffuse map is actually just viewport texture. 
Is this supposed behavior?
Why not use already assigned viewport texture? Refract pass always use viewport texture as environment map anyway.

-------------------------

cadaver | 2017-01-02 00:59:14 UTC | #2

To work properly, a reflection texture needs to use a different camera for rendering, so it's not the same as the viewport texture. The reflection texture is created by the application, the engine cannot know about it automatically.

-------------------------

ucupumar | 2017-01-02 00:59:14 UTC | #3

Ohh, my bad. I don't know if there's sample project for water setup already.
So, I need to setup reflection camera first, then use render texture result from that camera to water diffuse map.
Before looking the sample, I thought that diffuse map probably is used to something kind of screen space reflection technique.  :unamused: 
Thanks for the answer anyway.  :slight_smile:

-------------------------

cadaver | 2017-01-02 00:59:15 UTC | #4

Reflective water is example number 23.

-------------------------

ucupumar | 2017-01-02 00:59:17 UTC | #5

Thanks, already checked on it.  :slight_smile:

-------------------------

