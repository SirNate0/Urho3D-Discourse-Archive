Dave82 | 2019-12-28 22:18:32 UTC | #1

So for testing and educational purposes tried to create a rendertarget inside the render path xml file like this

[code]
<rendertarget name="silhouetteRT" sizedivisor="1 1" />
[/code]

The clear command works fine but once i try to output a scenepass to it the app crashes or freezes
[code]
 <command type="scenepass" pass="base" vertexlights="true" metadata="base" output="silhouetteRT" /> 
[/code]
Adding this line to the render path crashes the app. Is it valid to output predefined passes or only custom passes are allowed in RTT ?

-------------------------

Bananaft | 2020-01-05 09:52:57 UTC | #2

maybe you should specify RT's format?

-------------------------

GodMan | 2020-01-05 17:11:02 UTC | #3

I think he may have fixed this issue.

-------------------------

