Lumak | 2017-01-02 01:07:18 UTC | #1

I've been investigating why a model in Blender with a x-number of vertices is exported with ~4 times as many verts.  
For example, a default sphere has 482 verts but when exported there's 1984 verts.

And I found a problem in decompose.py, line 1777:
[code]
            tVertexIndex = None
            for j in verticesMapList:
                if verticesList[j].isEqual(tVertex):
                    tVertexIndex = j
                    break
[/code]

Debugging this, the size of [b]verticesMapList[/b] is always 0 (empty), hence, will generate new verts for every face instead of reusing previously stored vert info.

I've changed this to:
[code]
            tVertexIndex = None
            iIterator = 0
            for j in verticesList:
                if j.blenderIndex == tVertex.blenderIndex:
                #if j.isEqual(tVertex):
                    tVertexIndex = iIterator
                    break
                else:
                    iIterator += 1

[/code]

And the number of verts exported from this routine is = 482,  exactly what Blender shows.  The exported sphere model renders correctly.  Consequently, there is no longer a duplicate verts issue when using a model with softbody.
I don't have a skinned model to test the exporter, but I'm curious as to whether this change will break it.

-------------------------

Lumak | 2017-01-02 01:07:18 UTC | #2

UV mapping doesn't come out right with what I posted, but adding uv check:
[code]
    if j.blenderIndex == tVertex.blenderIndex and j.uv == tVertex.uv:
[/code]

correct the UV problem. I guess all other conditions must be checked: uv2, tangents, weights, etc.

-------------------------

codingmonkey | 2017-01-02 01:07:19 UTC | #3

>vertices is exported with ~4 times as many verts. 
hmm... and this for all models ? and I think why so slow exported models.
 
Did you test your fixes on textured sphere (with UV layout, few UV lands) ?
Or with applying to it few MarkSharp seams + Edge Split modificator (only Sharp Edges)
UVs and MarkSharp produce additional vertexes, are your code save these part properly?

-------------------------

Lumak | 2017-01-02 01:07:19 UTC | #4

I applied UV on the sphere and tested it twice. In my first test case with the original condition, there was a line of seams that stretched the UV and on my 2nd test case with the UV condition applied, it fixed the problem.

I just started learning Blender and had a hard time even applying UV. I won't be able to do much else with it atm.

-------------------------

codingmonkey | 2017-01-02 01:07:19 UTC | #5

>but when exported there's 1984 verts.
How did you measure this count of vertices ?

Currently I just create std sphere with 482 vertexes + add std sphere UV + default grey material, and got the same number in exported model
[url=http://savepic.su/6115950.htm][img]http://savepic.su/6115950m.jpg[/img][/url]

-------------------------

Lumak | 2017-01-02 01:07:19 UTC | #6

482 verts is what's decomposed, not what's exported.  You can see the exported vertex count in the system console (toggle system console).  It doesn't show up in the export dialog window.

But the issue is that the [b]verticesMapList is always empty[/b]. If this works for others then it could be because I'm using Blender 2.75...

-------------------------

codingmonkey | 2017-01-02 01:07:19 UTC | #7

I try load exported sphere and got [b]512 verts[/b] and 2880 indexes

[url=http://savepic.su/6128224.htm][img]http://savepic.su/6128224m.jpg[/img][/url]

using 2.75.4 blender

But if I switch smooth mode to flat I got 1984 vertexes and 2880 indexes
and I think that this is right vertexes count, because in case of flat edges, for draw this mini - "quad" on sphere are still needed 4 vertexes with || normal (one direction for 4 normal)
next near "quad" it also have it own 4 vertexes, but 2 of then in same position as previous quad, but again all of them have other normals - because this quad also have own flat surface - unique normal direction.

In case smooth faces: we have faces with vertexes that have same pos and normal that maybe shared between quads and basically we have model with a lot verts duplicates that we may do not save to file and save just unique. And then just connect this vertexes in some way by IndexBuffer to Triangle strips
sorry for my eng if what )

-------------------------

Lumak | 2017-01-02 01:07:19 UTC | #8

Thank you for your explanation as to why I'm getting so many verts exported.

I reverted the python changes and verified that I don't have smooth normals, but I still get 1984 verts.  If this happens because of some configuration that I'm not aware of then I don't want to waste anyone's time on this. I just need to get more familiar with Blender.

-------------------------

TikariSakari | 2017-01-02 01:07:19 UTC | #9

I tried with the modified python, and well at least I didn't notice it making anything worse, but since most of my models are only ~1500 vertex. I didn't check if it made the model use less or more things, but at least the file size remained the same in kilobyes, might be bit smaller if I had looked the byte count. Also the animations seemed to look the same. I am not sure how the optimize indices affects these things though, since I have that on.

-------------------------

