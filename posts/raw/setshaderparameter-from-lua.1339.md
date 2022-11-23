theak472009 | 2017-01-02 01:06:57 UTC | #1

Hello,
I have got zerobranestudio integrated and now I am trying to do some nice lua scripting but when I try to call renderpath SetShaderParameter from lua, it either passes garbage or null

Garbage:
renderPath:SetShaderParamter ("ShaderParameter", Variant (0.2))
Null:
renderPath:SetShaderParamter ("ShaderParameter", 0.2)

I even tried to allocate a Variant on the stack (local value = Variant (0.2), renderPath:...) but it still passes garbage value.

Any idea how to fix this?

Thanks.

-------------------------

rasteron | 2017-01-02 01:06:57 UTC | #2

It should be Variant with [b]Vector2()[/b] if you have 2 parameters..
[code]effectRenderPath:SetShaderParameter("BloomMix", Variant(Vector2(0.9, 0.6)))[/code]

see [b]09_MultipleViewports.lua[/b] as the above is the example provided.

I'm not sure though if it is right to use Variant in single parameters. You can try float..

-------------------------

theak472009 | 2017-01-02 01:06:58 UTC | #3

Nope, it only seems to work for anything that is a user defined data type like Vector2

renderPath:SetShaderParameter ("BloomMix", Variant (Vector2 (...))) works but
renderPath:SetShaderParameter ("BloomThreshold", 0.2) crashes the program and
renderPath:SetShaderParameter ("BloomThreshold",Variant (0.2)) passes a garbage value

-------------------------

rasteron | 2017-01-02 01:06:59 UTC | #4

Yes, I see the BloomThreshold is a single paramater value and there was no given example (afaik) so if you think this is a bug then you should post this issue on Github...

-------------------------

weitjong | 2017-01-02 01:06:59 UTC | #5

By default Lua number uses double as primitive data type. Probably the shader only expects to get a float. So, I would try to use this variant constructor: Variant(VAR_FLOAT, 0.2)

-------------------------

rasteron | 2017-01-02 01:06:59 UTC | #6

[quote="weitjong"]By default Lua number uses double as primitive data type. Probably the shader only expects to get a float. So, I would try to use this variant constructor: Variant(VAR_FLOAT, 0.2)[/quote]

Well there's your answer [b]theak472009 [/b]. I'm not into Lua at the moment so I don't even bother checking for these type of issues.. 

Thanks weitjong. :slight_smile:

[bookmarked]

-------------------------

theak472009 | 2017-01-02 01:06:59 UTC | #7

Thanks. It works perfectly now.

-------------------------

