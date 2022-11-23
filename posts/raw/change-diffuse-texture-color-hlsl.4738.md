GodMan | 2018-12-12 19:00:22 UTC | #1

Okay so I have done this in hlsl before, but I always felt that my method was not that great or efficient. My goal is to change a characters color, and there diffuse texture is white already which can be broken down into any other color. I then use a mask that is black and white. White represents color change area and black area is left alone.

Code Snippet
`float4 NewColor = multiMap * reColor * fvBaseColor - (multiMap * 0.9);`

multiMap is the 2D mask, and reColor is the float4 color change. Is there a better way of doing this?

-------------------------

Modanung | 2018-12-12 22:02:40 UTC | #2

[quote="GodMan, post:1, topic:4738"]
`- (multiMap * 0.9)`
[/quote]

This bit seems unnecessary to me.
Or rather it seems like you'd want something closer to:
```
float4 NewColor = multiMap * reColor * fvBaseColor + fvBaseColor * (1.0 - multiMap);
```

-------------------------

GodMan | 2018-12-12 22:38:00 UTC | #3

Well I want it were the character is a constant color. So any light in the scene do not change his primary color.

That code actually turns the character almost entirely white. Even though reColor is set to blue.

-------------------------

GodMan | 2018-12-12 22:41:21 UTC | #4

Modifying this line: `(1.0 - multiMap);`

Seems to make the color change more accurate. A smaller value brings it closer to the value of reColor.

-------------------------

