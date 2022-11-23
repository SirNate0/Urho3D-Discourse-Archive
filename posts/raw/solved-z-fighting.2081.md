1vanK | 2017-01-02 01:12:53 UTC | #1

[url=http://savepic.ru/10156698.htm][img]http://savepic.ru/10156698m.png[/img][/url]

I need draw one geometry on top of another geometry. How to solve the problem with z-fightnig? I see, that "forwardlight" pass does not have this problem. I try to repeat this approach and use technique
[code]
<technique vs="Unlit" ps="Unlit" psdefines="DIFFMAP">
    <pass name="alpha" depthwrite="false" depthtest="equal" />
</technique>[/code]

but it does not works

-------------------------

cadaver | 2017-01-02 01:12:53 UTC | #2

Use a small depth bias in the material.

The equal test works in the forward lights pass because it's about drawing the same geometries again, but when you're drawing a different geometry, subtle differences in math could still cause Z-fighting.

-------------------------

1vanK | 2017-01-02 01:12:53 UTC | #3

Thank you, bias works perfect!

-------------------------

