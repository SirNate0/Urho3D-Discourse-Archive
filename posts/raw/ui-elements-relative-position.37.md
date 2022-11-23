carlomaker | 2017-01-02 00:57:32 UTC | #1

I find it very useful to the editor and I'd like to have the  relative position option for  elements.

-------------------------

cadaver | 2017-01-02 00:57:32 UTC | #2

Do you mean in percentage relative to the parent element?

There was an issue for that on github posted by cin, but he closed it.

It's somewhat of a large change and may mean that all ints in UI elements related to position/size may need to be changed to floats.

-------------------------

carlomaker | 2017-01-02 00:57:32 UTC | #3

ok, but for me it 's really important to find a solution, 
? maybe it's not elegant but it works and I wanted to share it. 
This method seems to work, with my elements, maybe there could be other problems, however it could be a good starting point, 
just call GuiHelper :: Redraw after the reading of the layout.


[gist]https://gist.github.com/CarloMaker/8557193[/gist]

-------------------------

carlomaker | 2017-01-02 00:57:33 UTC | #4

i m doing some test...it seems work .

[b]1) 1280 x 960[/b] [size=70]Clickable.[/size]
[url=http://i.imgur.com/GrZ1AXA.jpg][img]http://i.imgur.com/GrZ1AXAl.jpg[/img][/url]

[b]2)1920 x 1080[/b] [size=70]Clickable.[/size]
[url=http://i.imgur.com/qFgYeEJ.jpg][img]http://i.imgur.com/qFgYeEJl.jpg[/img][/url]

-------------------------

