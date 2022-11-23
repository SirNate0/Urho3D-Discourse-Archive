Avagrande | 2020-08-14 19:04:37 UTC | #1

Hi. 
I have compiled with the safe lua option and when I try to enable or disable SetCastShadow I get "argument #1 is 'AnimatedModel'; 'Drawable' expected"  

It appears that I cannot do anything Drawable related when using AnimatedModel

Any hints on how to solve this?

-------------------------

evolgames | 2020-08-26 17:30:05 UTC | #2

Does /18_CharacterDemo work?
I've used the following from the Character sample and it works and lets me enable/disable shadows:

```
    -- Create the rendering component + animation controller
    local object = adjNode:CreateComponent("AnimatedModel")
    object.model = cache:GetResource("Model", "Models/Mutant/Mutant.mdl")
    object.material = cache:GetResource("Material", "Models/Mutant/Materials/mutant_M.xml")
    object.castShadows = true
    adjNode:CreateComponent("AnimationController")
```

I've also done object.castShadows with other things. I'm not having issues with animated models.

-------------------------

Avagrande | 2020-08-27 09:32:24 UTC | #3

This only affects functions that are present in the Drawable class. 
by using 
    object.castShadows = true
you are avoiding the problem as it occurs only when using the function  'SetCastShadows' therefore you won't get the error. 
The problem is Safe Lua as it checks the pointer ( in this case Object ) if its a Drawable and AnimatedModel is not a Drawable from Safe Lua perspective. 

I fixed this by copying Drawable functions into the AnimatedModel .pkg and it fixed it for now, its not ideal but so far AnimatedModel is the only class I had the error with so it will do for now.

-------------------------

evolgames | 2020-08-27 14:55:51 UTC | #4

Ah I see what you mean. That's interesting.

-------------------------

