miz | 2017-01-02 01:09:07 UTC | #1

Hi, When I have TMX maps loaded in the game I am getting lines appearing around the tiles that make up the TMX map. Below are some pictures.
[imgur.com/Is0W2A9](http://imgur.com/Is0W2A9)
[imgur.com/NCb2hYl](http://imgur.com/NCb2hYl)

Could it be something to do with rounding of the positions of the tiles? Has anyone else had this? Any fixes?

Thanks :slight_smile:

-------------------------

Mike | 2017-01-02 01:09:07 UTC | #2

As mentioned in the [url=http://urho3d.github.io/documentation/1.5/_urho2_d.html]documentation[/url], if 'seams' between tiles are obvious then you should make your tilesets images nearest filtered.

-------------------------

miz | 2017-01-02 01:09:07 UTC | #3

Ahh I missed that. Just tried it and it works. Thanks!  :smiley:

-------------------------

