Hevedy | 2017-01-02 01:02:15 UTC | #1

How set the alpha by color in a 2d sprite or tiles ?

-------------------------

codingmonkey | 2017-01-02 01:02:15 UTC | #2

1. open image with gimp and edit it )
2. texture.getData() and go with "for" on each rgba color if rgb==userAlpha then a=0 then put back this data.
3. write custom shader ( if (rgb==userAlpha) discard ) for sprites and assign it for sprite.  
(but i'm not see any methods to manage with shader/matarials or something like that for sprites)

-------------------------

Hevedy | 2017-01-02 01:02:16 UTC | #3

[quote="codingmonkey"]1. open image with gimp and edit it )
2. texture.getData() and go with "for" on each rgba color if rgb==userAlpha then a=0 then put back this data.
3. write custom shader ( if (rgb==userAlpha) discard ) for sprites and assign it for sprite.  
(but i'm not see any methods to manage with shader/matarials or something like that for sprites)[/quote]

Then don't have, thanks.

-------------------------

