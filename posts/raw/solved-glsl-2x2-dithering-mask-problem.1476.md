Bananaft | 2017-01-02 01:08:02 UTC | #1

So I want to generate 2x2 dithering mask, simple checkers pattern. Here is my code:

[code]  float mask= float(fract((vScreenPos.x / cGBufferInvSize.x + vScreenPos.y / cGBufferInvSize.y) * 0.5) > 0.5);[/code]

It looks fine, but unfortunately, there are some ugly artifacts, that will twink and twitch if you move the camera even slightest.

Pics:
[i.imgur.com/6Vf1T89.jpg](http://i.imgur.com/6Vf1T89.jpg)
[i.imgur.com/XPEqWTp.jpg](http://i.imgur.com/XPEqWTp.jpg)

I've tried to change my expression a bit, shuffle summands, but result is always the same.

What is it? Float float precision error? Any ideas how to fix it?

-------------------------

Bananaft | 2017-01-02 01:08:04 UTC | #2

Thank you very much. That's looks more tidy, and actually work.

So you have G-buffer compression in your PBR thingy? I should probably check it out.

-------------------------

