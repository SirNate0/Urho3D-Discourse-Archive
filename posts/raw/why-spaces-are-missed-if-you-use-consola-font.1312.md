codingmonkey | 2017-01-02 01:06:45 UTC | #1

I trying to use other font for editor and found what there are some bug with spaces.
i'm just put to font folder the consolas regular font from windows\fonts\ dir, and make some changes with default style.xml
[url=http://savepic.net/7257122.htm][img]http://savepic.net/7257122m.png[/img][/url]


and that I got in editor, all spaces are missed in text between words

[url=http://savepic.net/7244834.htm][img]http://savepic.net/7244834m.png[/img][/url]

-------------------------

rasteron | 2017-01-02 01:06:45 UTC | #2

I have noticed this as well. There are some fonts that have very little or no space in them in the engine. 

In your particular case, you can try the free alternative [b]Inconsolota[/b] font which is similar to Consolas. The font is under Open Font License. 

[img]http://i.imgur.com/FnAS5Ua.jpg[/img]

Here is the [url=https://goo.gl/mYBv5F]download to the converted TTF format[/url]

Reference:
[johndcook.com/blog/2009/09/2 ... olas-font/](http://www.johndcook.com/blog/2009/09/21/free-alternative-to-consolas-font/)

Hope that helps.  :slight_smile:

-------------------------

codingmonkey | 2017-01-02 01:06:45 UTC | #3

Thanks [b] Sinoid [/b]and [b]rasteron[/b].
I think the using inconsolata font its way to solve this problem, without any additional code fixes.
Also I trying to use old slyle font like - "kex.fon" (ke7x14) and I guess that *.fon files don't supported by engine ?
It have tiny lines, without blurred char contours
link to font: [rghost.ru/6wlsyGyx5](http://rghost.ru/6wlsyGyx5)

-------------------------

jmiller | 2017-01-02 01:06:46 UTC | #4

[quote="codingmonkey"]
Also I trying to use old slyle font like - "kex.fon" (ke7x14) and I guess that *.fon files don't supported by engine ?
It have tiny lines, without blurred char contours[/quote]

Hi codingmonkey,
You might try to convert that to another format.
[stackoverflow.com/questions/3750 ... e-font-ttf](http://stackoverflow.com/questions/3750124/how-to-convert-a-bitmap-font-fon-into-a-truetype-font-ttf)

-------------------------

codingmonkey | 2017-01-02 01:06:46 UTC | #5

thanks  [b]carnalis[/b]
i'm try figure out with this converter

-------------------------

szamq | 2017-01-02 01:07:31 UTC | #6

Same here, I tried to use the lately famous Lato Fonts and the space characters are simply ignored. I also used the font editor mentioned before to modify the space character to some random lines to check if it will be rendered. After the change the spaces should appear because it has width and height, but no. Modification of other regular characters works. So I think it may be some bug in the engine, that didn't even send the spaces to the render(taken from font).

-------------------------

cadaver | 2017-01-02 01:07:32 UTC | #7

Could be a FreeType bug, or some unhandled convention like "if advance is zero in the space glyph then some default value has to be used", which would seem stupid. There shouldn't be special-case code in the engine for the space character.

EDIT: Consola font has missing space glyph.

-------------------------

franck22000 | 2017-01-02 01:07:32 UTC | #8

Maybe it's time to update Freetype library ? There has been quite a lot of bugfixes since the 2.5 version and i have myself some bugs while testing some fonts in Urho.

-------------------------

cadaver | 2017-01-02 01:07:32 UTC | #9

Updating might be a good idea, however (according to a quick test) it didn't affect the space issue.

However I believe it's solvable on the Urho side.

EDIT: the master branch now tries to load the space glyph regardless of whether the font's charcode list (as given out by FreeType) mentions it or not. This seems to fix Consola space.

-------------------------

franck22000 | 2017-01-02 01:07:32 UTC | #10

Waiting for the latest Freetype version to be merged in Urho and then if my issue persist i will fill a bug report.

-------------------------

