smellymumbler | 2017-03-03 03:15:32 UTC | #1

In UDK, it's possible to blend materials together in order to break repetitive patterns: http://www.chrisalbeluhn.com/UT3_Add_variation_to_repeating_textures_Tutorial.html

Is that something doable with the built-in Urho material system?

-------------------------

rku | 2017-03-03 08:15:48 UTC | #2

No, you will have to implement it yourself in the shader, just like in UDK. The only difference is that in UDK you use node graph to assemble shader and in urho you write shader code.

-------------------------

