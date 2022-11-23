godan | 2017-01-02 01:01:26 UTC | #1

How would I go about turning off backface culling in one of the prebuilt shaders? Does this happen in the technique file? Or in the shader itself?

-------------------------

godan | 2017-01-02 01:01:26 UTC | #2

Nevermind, figured it out.

It's specified in the material xml file:

<material>
    <technique name="Techniques/NoTexture.xml" />
    <parameter name="MatDiffColor" value="0 1 0 0.25" />
    <parameter name="MatSpecColor" value="1 1 1 16" />
   [b] <cull value="none" />[/b]
</material>

-------------------------

codingmonkey | 2017-01-02 01:01:27 UTC | #3

thus easier way
[url=http://savepic.ru/6316937.htm][img]http://savepic.ru/6316937m.png[/img][/url]

-------------------------

