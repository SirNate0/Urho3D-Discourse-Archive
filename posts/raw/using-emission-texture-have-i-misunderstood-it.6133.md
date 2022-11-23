NessEngine | 2020-05-01 19:48:11 UTC | #1

Hi all,
I'm trying to use emission texture to make parts of a texture fully lit at all times. I noticed in shader code that since sample from emission map is multiplied by emission color, I should probably set emission color to white:

https://github.com/xamarin/urho/blob/master/Urho3D/CoreData/Shaders/HLSL/LitSolid.hlsl#L312

So I did, and it looks great when in full darkness. But when scene is lit, suddenly these areas turn too bright. So I looked at the technuique:

https://github.com/xamarin/urho/blob/master/Urho3D/CoreData/Techniques/DiffEmissiveAlpha.xml#L2

And it looks like emission is just additive render on top of the diffuse map? As a workaround, I made the parts that are fully lit in the emission map completely black in the diffuse map, and now it looks great in any light. But this doesn't sound right.

Am I misusing the emission map, or is it really expected to have lit areas darken in diffuse map in order to work in all lights?

Thanks,

-------------------------

Eugene | 2020-05-01 20:54:03 UTC | #2

[quote="NessEngine, post:1, topic:6133"]
And it looks like emission is just additive render on top of the diffuse map?
[/quote]

Yes, this is correct.
What kind of behavior you expected/wanted/find appropriate?

-------------------------

NessEngine | 2020-05-01 20:59:39 UTC | #3

Didn't mean to sound like criticism :)
But what I expected is that emission would go into lighting calculation, meaning that emission of 1,1,1 will just be the color in the diffuse map, and not actually white.

So if its additive, that means that if I create emission map with fully lit parts I'm expected to black them out in the diffuse texture?

-------------------------

SirNate0 | 2020-05-01 21:02:54 UTC | #4

You could try multiplying by it or adding it to the lighting or something, or you could try replacing the `+=` with an `= Max(finalColor, cMatEmissiveColor * Sample2D(EmissiveMap, iTexCoord.xy).rgb);` and see if one of those gets you more desirable results. (I may have the function name for Max wrong)

-------------------------

Eugene | 2020-05-01 21:08:49 UTC | #5

As you can see, light maps multiply emission with diffuse (they have to).
It cannot be default behavior because it will limit use cases of emission maps.
E.g. one will be unable to create emissive black (i.e. not reflecting light) object.

-------------------------

NessEngine | 2020-05-02 07:42:17 UTC | #6

Thanks @SirNate0, if I'd be too bothered by it ill change the shader, right now I'm ok with darkening diffuse I just wanted to make sure I'm not misusing it.

@Eugene  yeah I understand the extra use case additive gives (making areas brighter due to environmental lights + emission),  but imo its not very usable for natural surfaces and specular is more suitable for this purpose anyway. And I don't think it worth the price of having counter intuitive textures (now instead of normal diffuse texture I need to darken areas which are lit to avoid over brightness). Also I may be wrong here because its been long since I used one of the big commercial engines, but if I recall at least in unity emission would go 0 to diffuse, not above that. 

But as I said I'm not really bothered by it, just my two cents on this matter :)

-------------------------

Eugene | 2020-05-02 16:38:34 UTC | #7

[quote="NessEngine, post:6, topic:6133"]
And I don’t think it worth the price of having counter intuitive textures
[/quote]
Diffuse light is the light reflected by the object.
Emission light is the light emitted by the object itself.
These types of light are completely unrelated to each other (by definition), therefore there's no reason to have them entangled.

Although I admit I have made the same mistake as you, a while ago.

[quote="NessEngine, post:6, topic:6133"]
but imo its not very usable for natural surfaces and specular is more suitable for this purpose anyway
[/quote]
Heated metal or lava is quite natural phenomena and I can imagine games wanting to render it.

-------------------------

NessEngine | 2020-05-02 17:36:46 UTC | #8

Edit: never-mind I checked with other engines and it seems to be the standard so no reason for Urho to do differently. I still think emission tied with diffuse makes more sense (and doesn't prevent heated metal or lava in any way),  but that's just me I guess.

-------------------------

Eugene | 2020-05-02 18:04:36 UTC | #9

[quote="NessEngine, post:8, topic:6133"]
and doesn’t prevent heated metal or lava in any way
[/quote]
I'm now curious. How would it work?

Assume user wants animated heated metal (from almost black when cold to glowing red when heated).
User sets diffuse (which is black), emissive (grayscale mask), and emissive color multiplier.
So the metal goes from dark gray to red/orange/white when user tweaks color multiplier.

On the other hand, if you have emissive multiplied with diffuse, you won't get anything because black stays black no matter what you multiply it with.

-------------------------

NessEngine | 2020-05-02 18:18:34 UTC | #10

Something like this:
![Untitled-1|690x243](upload://44TDETIQpUuxegDHQLkNb8uSBQD.jpeg) 

Or maybe I didn't understand what you mean exactly?

-------------------------

Eugene | 2020-05-02 18:57:39 UTC | #11

I mean that diffuse texture (without any emission applied) should correspond to cold dark metal.
It’s not the case in your example. I cannot render cold metal with such texture. Moreover, such diffuse texture will result in incorrect lighting: if I change the intensity of the incoming light, the brightness of the object will change too, which is physically incorrect for black body.

-------------------------

NessEngine | 2020-05-06 17:55:02 UTC | #12

Sorry forgot to reply. 

[quote="Eugene, post:11, topic:6133"]
I cannot render cold metal with such texture.
[/quote]

Yeah I agree with this point, it is a limitation.

[quote="Eugene, post:11, topic:6133"]
Moreover, such diffuse texture will result in incorrect lighting: if I change the intensity of the incoming light, the brightness of the object will change too, which is physically incorrect for black body.
[/quote]

Not sure I understand this point, I meant in my example that black bodies will also have black emission, so lighting won't make them brighter?

Anyway I'm convinced, you were right (+ checking other engines and seeing this is the standard behavior had its impact), so feel free to explain further if you want, or not :) Anyway it was interesting and eye opening.

-------------------------

Eugene | 2020-05-06 18:08:48 UTC | #13

[quote="NessEngine, post:12, topic:6133"]
Not sure I understand this point, I meant in my example that black bodies will also have black emission, so lighting won’t make them brighter?
[/quote]
“Black body” is physical term for the body that doesn’t reflect incoming light and is illuminated only by internal heat radiation.
Things like lava and heated metal are quite close to theoretical black bodies.

To render them properly you should use black (or nearly black) diffuse texture so the lighting of the object is not affected by the incoming light.

-------------------------

NessEngine | 2020-05-06 18:18:53 UTC | #14

Thanks for the clarification, but that's not the part I didn't understand. If the black parts of my bodies are black in both diffuse and emission, that would not be a problem (which is what I tried to show with the screenshots earlier - the darker parts which are not glowing have darker / black emission) . 

So in this case I don't see how multiplying the emission with diffuse, which would only reduce it, would make black bodies less black? Edit: plus in the end it all multiplied by diffuse.

Thanks!

-------------------------

Eugene | 2020-05-06 18:24:14 UTC | #15

If you have both black diffuse and black emission, then the object will stay black, sure.

But if you want to have non-zero emission somewhere and you multiply emission with diffuse, you must have non-zero diffuse in the same place of the texture.

And as soon as you have non-zero diffuse, the body is no longer black body. Therefore, you cannot render black body with non-zero emission, if you multiply diffuse and emission during rendering. Meaning that you cannot render physically realistic lava/metal/whatever.

-------------------------

NessEngine | 2020-05-06 18:32:58 UTC | #16

[quote="Eugene, post:15, topic:6133"]
And as soon as you have non-zero diffuse, the body is no longer black body. Therefore, you cannot render black body with non-zero emission, if you multiply diffuse and emission during rendering. Meaning that you cannot render physically realistic lava/metal/whatever.
[/quote]

Ah yes, I understand what you mean now, but that's a problem we face anyway when emission is additive like in Urho. As soon as emission is > 0, result pixel will never be black. That's sort of the problem that made me investigate in the first place (not exactly black body, but something that went brighter than it should).

Thanks for the info

-------------------------

Eugene | 2020-05-06 18:50:11 UTC | #17

[quote="NessEngine, post:16, topic:6133"]
but that’s a problem we face anyway when emission is additive like in Urho. As soon as emission is > 0, result pixel will never be black
[/quote]
I’m talking about how the pixel reacts to the change of lighting, not the exact color itself.

Additive emission let you make glowing material that has the same appearance regardless of the incoming light (black body).
Multiplicative emission forbids it.

Regarding your initial problem—I think it stems from the fact that the textures you use were made without considering physical meaning of the diffuse/emission. Light emitted by the heated body is by definition emission, so the physically sane diffuse texture must never have any red/yellow “glowing” parts.

-------------------------

NessEngine | 2020-05-06 18:57:36 UTC | #18

[quote="Eugene, post:17, topic:6133"]
Regarding your initial problem—I think it stems from the fact that the textures you use were made without considering physical meaning of the diffuse/emission.
[/quote]

That is a very true conclusions, the textures in questions are actually more of a cartoonish sprites than realistic materials. The discussion was hypothetical, but my use case is far from being realistic.

-------------------------

