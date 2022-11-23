darkirk | 2017-06-17 00:41:08 UTC | #1

Coming from the UE4/Marmoset workflow for PBR, i'm having a hard time understanding how Urho does it. While messing around with the sample, i could not find the slot to put AO maps into the sample materials. 

https://www.marmoset.co/posts/physically-based-rendering-and-you-can-too/#ao

-------------------------

dragonCASTjosh | 2017-06-17 02:10:36 UTC | #2

AO Maps are currently not implemented as i havent had time to do it although it should be a very short task. The green and alpha channels of the PBR texture are currently unused so my plan was to re-purpose one of them as an AO map.

-------------------------

darkirk | 2017-06-18 18:31:56 UTC | #3

What do you mean by not used? You only read the Red channel from albedos?

-------------------------

dragonCASTjosh | 2017-06-18 19:07:20 UTC | #4

In the PBR properties texture only the red and blue channels are used by the shader, anything in the green or alpha is currently ignored. It should be a simple thing just to multiply the green channel into where the AO should be  applied.

-------------------------

darkirk | 2017-06-18 21:03:14 UTC | #5

Oh. That explains many issues i was having. Why don't you map to separate textures? I mean, abusing channels like this only makes the life of artists even harder. It's so much easier to export separate textures for each purpose: Albedo, microsurface, reflectance, etc.

-------------------------

dragonCASTjosh | 2017-06-18 21:08:25 UTC | #6

my combining textures it saves video memory, over the course of a full game it could cause large gains. Personally i come from a console background so its natural for me to try and lower costs as much as i can find.

-------------------------

darkirk | 2017-06-19 13:54:02 UTC | #7

Oh, i see. Is your technique similar to Substance's packed export for UE4? Is there any doc of what should go where and any caveats?

-------------------------

dragonCASTjosh | 2017-06-21 01:22:46 UTC | #8

Yes it works kinda the same as unreal packs export. Currently there are no docs, just remember Red = roughness, Green = metallic

-------------------------

darkirk | 2017-07-03 01:18:23 UTC | #9

I've noticed that this technique increases the amount of draw calls quite a bit. Also, since packing is just used for roughness and metallic, not a lot of memory is saved (in contrast to RMA). Are there any plans of adding uncombined texture support to the PBR shader anytime soon?

-------------------------

dragonCASTjosh | 2017-07-04 02:53:54 UTC | #10

AO textures will be added to the combined texture at some point and I'm sure I'll find a use for the alpha. As for splitting them there are many reasons I likely won't, biggest is time. But outside of that I'm 90% sure mobile has a limit on the number of textures you can use so dividing then will just cause problems. Large engines like unity and unreal combine the texture offline before passing it to the GPU but currently I'd have to say it's unneeded complexity. Maybe if an external editor project kicks off then I'll do is as part of that.

-------------------------

