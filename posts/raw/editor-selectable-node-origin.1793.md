codingmonkey | 2017-01-02 01:10:11 UTC | #1

Hi folks )
I tried to add similar to Blender's object origins. Or whatever, just simple helper to select nodes in Editor's viewport even if node do not have own drawable or if node have only light component within. I guess now selection for all types objects (Drawables and Lights) are pretty handy.    
Also there is info feature about selected node and model format.

Options:
Shift = on/off text near origins
Left Ctrl =  Hide Extended info / Hide All origins names
Left Alt = show extra info (you probably need pressing few times for see all info about selected node (currently info about only model))
Left Ctrl + Origin click = select parent node (back)

There is one bug but I do not figure out with it yet: if you try open one by one various scenes, you probably got crash of editor :slight_smile:
So if this bug will be solved and this feature are needed in master I do PR.

[url=http://savepic.net/7793839.htm][img]http://savepic.net/7793839m.png[/img][/url]

Repo for testing : [github.com/MonkeyFirst/Urho3D/t ... AndAltInfo](https://github.com/MonkeyFirst/Urho3D/tree/EditorSelectableOriginsForNodesAndAltInfo)
(for testing you may just copy dir (Urho3D\bin\Data\Scripts) into your Urho3D dir )

-------------------------

codingmonkey | 2017-01-02 01:10:14 UTC | #2

1. add some fixes into Origins
2. also add style-fix to world Grid plane, now on view angles far planes are transparent.
two techniques with new GridShader.glsl
alpha tech 
[url=http://savepic.net/7792734.htm][img]http://savepic.net/7792734m.png[/img][/url]
addalpha tech
[url=http://savepic.net/7795806.htm][img]http://savepic.net/7795806m.png[/img][/url]
[url=http://savepic.net/7776350.htm][img]http://savepic.net/7776350m.png[/img][/url]

Repo : [github.com/MonkeyFirst/Urho3D/t ... dGridPlane](https://github.com/MonkeyFirst/Urho3D/tree/FixedGridPlane)

-------------------------

1vanK | 2017-01-02 01:10:14 UTC | #3

Nice!

-------------------------

codingmonkey | 2017-01-02 01:10:16 UTC | #4

>Nice!
 :wink: 

add Paint selection tool

Repo : [github.com/MonkeyFirst/Urho3D/t ... tSelection](https://github.com/MonkeyFirst/Urho3D/tree/PaintSelection)

[video]https://youtu.be/auu4ToZGT4E[/video]

-------------------------

weitjong | 2017-01-02 01:10:17 UTC | #5

Nice indeed

-------------------------

