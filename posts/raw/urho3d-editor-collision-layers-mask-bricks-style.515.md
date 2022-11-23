codingmonkey | 2017-01-02 01:01:01 UTC | #1

Hi folks! 
Could you make under or in place of the numeric field: such as - "collision mask" and "collision layer"  of rigidbody component, do just blocks-buttons like in blender 3d editor?

Current numeric field style
[url=http://savepic.org/6333173.png][img]http://savepic.org/6333173m.png[/img][/url]

This may look better
[url=http://savepic.org/6313717.png][img]http://savepic.org/6313717m.png[/img][/url]

-------------------------

hdunderscore | 2017-01-02 01:01:03 UTC | #2

I like this idea, as it's easier to come to the right mask without opening a calculator or doing math in your head.

-------------------------

codingmonkey | 2017-01-02 01:01:13 UTC | #3

Exactly ) so that about 15 possible layers
mb this feature-desire needed to bring on github as feature request? but i don't known how (

-------------------------

hdunderscore | 2017-01-02 01:01:14 UTC | #4

You could request it on github, but it could still take a while until someone gets to it. If you know any programming, you might be able to put something together -- the editor is written in angelscript and isn't hard to modify.

I decided to take a quick peek and see how easy it would be to add:
[url]http://i.imgur.com/loPgpNG.png[/url]

This doesn't function yet, but just a visual of using a grid of checkboxes to do it. If others think this method is ok, I could make it functional.

-------------------------

codingmonkey | 2017-01-02 01:01:14 UTC | #5

[quote]This doesn't function yet, but just a visual of using a grid of checkboxes to do it. If others think this method is ok, I could make it functional.[/quote]
it looks cool!), but i guess that it is necessary to leave the numeric field and a little higher above the grid of checkboxes for those who like to use numbers.

-------------------------

hdunderscore | 2017-01-02 01:01:14 UTC | #6

Here, try it out:
[github.com/hdunderscore/Urho3D/ ... skSelector](https://github.com/hdunderscore/Urho3D/tree/Editor_BitMaskSelector)

It's not implemented in the cleanest way, so if there happens to be attributes with the word 'Mask' that aren't supposed to be bitmasks, they'll have their property overwritten. I decided to make it so that you if you fill all the boxes, it will set the field to -1 instead of 255 -- otherwise, you can go beyond 255 but the boxes won't necessarily represent the entire mask value.

-------------------------

codingmonkey | 2017-01-02 01:01:14 UTC | #7

I think that what has been done is cool!) i little play with this checkboxes ) 
But I doubt that there should be only 8 cubes because bullet uses like word or signed-word sized numbers for these masks in his api. 
However, I am not much aware of this.


[url=http://savepic.org/6380137.htm][img]http://savepic.org/6380137m.png[/img][/url]

I think checkboxes works as it should, cool)
but sometimes you just leave one marked of all, can make this feature to middle or right mouse button? - disable all checkboxes, but not off selected.

-------------------------

hdunderscore | 2017-01-02 01:01:20 UTC | #8

Yeah there should probably be more boxes, but how many is enough? The UI will look very messy if you include the max possible.

True, unticking all the boxes to get what you want isn't the best.

I'm testing this out on my 7dfps entry, it's pretty useful.

-------------------------

codingmonkey | 2017-01-02 01:01:21 UTC | #9

Maybe you're right, too many buttons will look ugly. But, would buttons their size two time smaller, its could be located more )
[quote] it's pretty useful.[/quote]
Yes, even now I sometimes use these masks )

-------------------------

codingmonkey | 2017-01-02 01:01:38 UTC | #10

and you do not know why these blocks are still not added to the master?
yesterday I had to wrestle with these masks and calculate on the calculator for my hitfx system (

-------------------------

hdunderscore | 2017-01-02 01:01:38 UTC | #11

I didn't submit a pull-request yet, I'll look at it again today.

-------------------------

ucupumar | 2017-01-02 01:01:44 UTC | #12

This is so useful!
It's already on pull request, I hope it will get merged soon!  :mrgreen:

-------------------------

