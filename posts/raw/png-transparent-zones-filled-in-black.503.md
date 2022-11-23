rogerdv | 2017-01-02 01:00:55 UTC | #1

I was testing some models with png textures and found that the transparent zones are filled with black instead of being transparent. Didnt had any way to convert them when that happened, so I just wanted to know, how should I save the png files to make them compatible with the engine?

-------------------------

friesencr | 2017-01-02 01:00:55 UTC | #2

Are you using an alpha supported technique such as DiffAlpha.xml.  All of the stock techniques with Alpha in the name support transparency.  Alpha is is much more expensive then non Alpha techniques.

-------------------------

rogerdv | 2017-01-02 01:00:55 UTC | #3

Stupid me, didnt know about that. By the way, the material editor does not allow me to change techniques in existing materials, or it requires some specific steps to do it. My solution has been creating a new material when I need to change the technique of an existing material.

-------------------------

