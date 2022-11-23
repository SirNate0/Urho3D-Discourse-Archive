Mike | 2017-01-02 00:59:07 UTC | #1

It would be cool if there was an option to automatically size a Billboard according to its texture width and height, so that its aspect ratio match.

Currently I'm using piece of code below to achieve this (in lua):

[code]
billboardSet:GetBillboard(0).size = Vector2(texture.width / texture.height, 1)
[/code]

-------------------------

