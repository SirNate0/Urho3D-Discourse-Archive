codder | 2017-01-02 01:12:00 UTC | #1

Hello,

I'm trying to render the scene normals as post effect. Is possible to achieve something like this with post processing?
[img]https://snakehillgames.files.wordpress.com/2013/12/hoboculvert_normals.png[/img]

Or any ideas how to achieve something like that? Thanks.

-------------------------

1vanK | 2017-01-02 01:12:00 UTC | #2

as material

gl_FragColor = vec4(vNormal.x, vNormal.y, vNormal.z, diffColor.a);

[url=http://savepic.ru/9460900.htm][img]http://savepic.ru/9460900m.png[/img][/url]

U can create custom pass, save normals to texture and use as postpocess

EDIT: with considering a normal map:

gl_FragColor = vec4(normal.x, normal.y, normal.z, diffColor.a);

-------------------------

codder | 2017-01-02 01:12:00 UTC | #3

By creating custom pass do you mean doing it in a technique? Can you make a longer example? thanks. I'm very very new to CG and I'm trying to learn it with Urho3D.
I saw normals are very important to achieve different effects and I simply got stuck :slight_smile:

-------------------------

1vanK | 2017-01-02 01:12:00 UTC | #4

> By creating custom pass do you mean doing it in a technique?

in a technique and in renderpath

> Can you make a longer example? thanks. I'm very very new to CG and I'm trying to learn it with Urho3D.

renerpath Deffered.xml writes normals to texture
for custom passes u can see also  [github.com/1vanK/Urho3DOutlineSelectionExample](https://github.com/1vanK/Urho3DOutlineSelectionExample)

-------------------------

