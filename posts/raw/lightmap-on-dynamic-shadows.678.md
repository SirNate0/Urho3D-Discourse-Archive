rasteron | 2017-01-02 01:02:04 UTC | #1

So... has anyone ever tried lightmap texture blending on dynamic shadows?

I would like to provide and submit a sample demo in Urho, but I really don't know where to start if it involves shaders.

Thanks.

-------------------------

hdunderscore | 2017-01-02 01:02:19 UTC | #2

Have you tested to see if the effect works? Just looking at the shaders, I believe lightmap and dynamic shadows should work together (maybe that's not what you mean?). The lightmap UV's are stored in a second uv set.

-------------------------

friesencr | 2017-01-02 01:02:19 UTC | #3

try {
  my memory is way foggy but i think the lightmap doesn't mix light but the ao does mix.    however the ao is using the wrong uv set so you want the behavior of ao with the uv set of lightmap. are you talking about mixing light?
}
catch {
 ignore_chrisman_\m/();
}

-------------------------

rasteron | 2017-01-02 01:02:24 UTC | #4

Thanks guys. I'm referring to seamless shadows in lightmaps and dynamic shadows like this in Unreal 4..

[answers.unrealengine.com/questi ... ethod.html](https://answers.unrealengine.com/questions/48053/unreal-engine-udk-shadow-blending-method.html)

[quote]ignore_chrisman_\m/();[/quote]

Lol. hey Chris, all ideas are welcome of course.  :slight_smile:

-------------------------

ucupumar | 2017-01-02 01:02:25 UTC | #5

I have actually kind of do this, but not that quite exactly like what you want.
My implementation is lightmap only store indirect light, so direct light still using dynamic lamp. Because of this, dynamic and static object will had same shadow buffer and it will blend perfectly.
And I do think this technique is used on Last of Us too. Look at this screenshot for example.
[img]http://i.minus.com/iboYPAs5J258mU.jpg[/img]
If you look at bottom of window shadow, it's really jagged and I suspect this isn't produced from a lightmap. 
But there's indirect light on top of the picture that kind of produced from a lightmap.

-------------------------

rasteron | 2017-01-02 01:02:26 UTC | #6

Thanks ucupumar. Do you have a shader code sample to accomplish this? I was hoping for maintaining the quality of the lightmap rather than altering it but any demo is worth a try :slight_smile:

cheers.

-------------------------

