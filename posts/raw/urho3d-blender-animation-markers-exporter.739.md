codingmonkey | 2017-01-02 01:02:35 UTC | #1

I'm write some add-on for blender that helps export animation markers from blender to urho3d.
maybe it will be useful not only to me )
note: I do not know why but before exporting animation marker the blend file must to be saved and then re-opened for export.

[video]http://www.youtube.com/watch?v=eYWBMf8BTJU[/video]

link: [github.com/MonkeyFirst/Urho3D-B ... on-Markers](https://github.com/MonkeyFirst/Urho3D-Blender-Animation-Markers)

-------------------------

weitjong | 2017-01-02 01:02:35 UTC | #2

Thanks for sharing it. It will be great to see this merged into reattiva's Urho3D blender mesh exporter.

-------------------------

Mike | 2017-01-02 01:02:35 UTC | #3

Note that timeline markers are already supported with the "Use markers as triggers" option.

-------------------------

codingmonkey | 2017-01-02 01:02:35 UTC | #4

yes, but i'm using only my favorite - "All Actions" then i'm do export, and in this case add-on don't save anything (
[img]http://savepic.ru/6602559.png[/img]

I don't know why addon has this limitation.


now add-on also support normalizedtime="0.00" export but by default this option is off, because i usually use time="0.00" markers
[img]http://savepic.ru/6613854.png[/img]

@weitjong
>It will be great to see this merged into reattiva's Urho3D blender mesh exporter.
yes it's will be the best solution if @reattiva's add-on supports action markers also

-------------------------

