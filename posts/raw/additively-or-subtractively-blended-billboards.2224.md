sabotage3d | 2017-01-02 01:14:02 UTC | #1

Hi what is the best way to blend the billboards additively or subtractively in the shader?

-------------------------

cadaver | 2017-01-02 01:14:02 UTC | #2

Since a (pixel) shader is always drawing a single billboard at a time and just outputs the color, it can't really control the framebuffer blending. Rather, blending is controlled as usual by the material technique's passes. Look for techniques with the word Add or Multiply in the name. I don't think there are subtract-blend techniques included by default, but you can make one quite trivially from an additive technique, just change blend="add" to blend="subtract".

-------------------------

sabotage3d | 2017-01-02 01:14:02 UTC | #3

Thanks I will try that. I need to disable the sorting as well right?

-------------------------

cadaver | 2017-01-02 01:14:02 UTC | #4

You can disable sorting for optimization, but don't have to, as addition / subtraction order doesn't matter.

-------------------------

