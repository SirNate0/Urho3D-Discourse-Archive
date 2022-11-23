evolgames | 2021-03-22 04:54:51 UTC | #1

I've been doing a simple HUD with some windows and text elements. Stroke effects work as expected, and thickness can be changed from its default of 1. I've set stroke effects on the bottom right text. However, setting shadow offset with:
```
SetEffectShadowOffset (const IntVector2 &offset)
```
doesn't seem to work. The shadow only disappears. Here is the default (which is Vector2(1,1) which I've applied to the (crude) fps counter in the top left.
![Screenshot_2021-03-22_00-45-45|690x388](upload://k8spIniDsVzg0GYbOdmkKMpXJVa.png) 
![Screenshot_2021-03-22_00-50-45|456x378, 50%](upload://bl0G47tKnzY8CFX5pf9yAL9ZcY1.png) 

It's alright for the default, but when *any* offset value is set it is gone. I've tried 1.1, .99, even PIXEL_SIZE but nothing seems to work.
![Screenshot_2021-03-22_00-46-35|690x388](upload://xP5hnHEIs7XNP95FqR55YQgBebE.png) 
![Screenshot_2021-03-22_00-52-02|690x475, 50%](upload://t0QjA2O8YD0OtOYeHeTJSYI2fpi.png) 

I can use stroke effects only I guess, but I was hoping to use drop shadows with variable offset. Anyone run into the same issue?

-------------------------

Lys0gen | 2021-03-23 02:35:29 UTC | #2

[quote="evolgames, post:1, topic:6766"]
I’ve tried 1.1, .99,
[/quote]

*SetEffectShadowOffset (const **Int**Vector2 &offset)*

Note that it's an IntVector.


                        font->SetTextEffect(Urho3D::TextEffect::TE_SHADOW);
                        font->SetEffectShadowOffset(Urho3D::IntVector2(10, 10));
Works fine for me.

-------------------------

evolgames | 2021-03-23 02:38:17 UTC | #3

Oh whoops. Just needed 'int' before it. I'm a dummy. Thank you

-------------------------

