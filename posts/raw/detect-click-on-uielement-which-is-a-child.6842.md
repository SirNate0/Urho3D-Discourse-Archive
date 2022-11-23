HappyWeasel | 2021-05-12 20:01:17 UTC | #1

Hi Guys,

I have a Sprite as a child of a Window and want to catch clicks on it.
I registered for E_UIMOUSECLICK or E_CLICK but this gives me the parent (the Window)
Is there any way to register for the child element specifically ? 

Thanks

-------------------------

JTippetts1 | 2021-05-12 20:27:03 UTC | #2

Sprite isn't set up to do that, but you could probably fake it by attaching each Sprite as the sole child of a proxy transparent Button and detecting the events fired by clicking on the Button. Doing it that way, you could still set Sprite rotation directly on the Sprite, but would have to move the Button instead of the Sprite to get the thing to move around.

-------------------------

HappyWeasel | 2021-05-12 20:22:44 UTC | #3

Hehe, sounds bit hacky but if it does the job..
The main reason I used sprite was the need to conveniently update the bitmap every now and then
(every few seconds at most )..  
Thanks !

-------------------------

1vanK | 2021-05-12 20:27:08 UTC | #4

```
SetEnabled(true);
```

-------------------------

JTippetts1 | 2021-05-12 20:25:59 UTC | #5

If you're not using the unique features of Sprite (eg. rotation) you might be better off just using Button directly instead of Sprite. It derives from BorderImage, so you can set the image rectangle easily and with little cost.

-------------------------

HappyWeasel | 2021-05-12 20:27:26 UTC | #6

Thanks guys for the quick feedback and tips

-------------------------

