Egorbo | 2017-01-02 01:07:21 UTC | #1

Hello,
I am looking at 35_SignedDistanceFieldText sample and I found this line of code:
mushroomTitleText->SetFont(cache->GetResource<Font>("Fonts/BlueHighway.sdf"), 24);
where 24 is a font size, however it seems it doesn't respect that value - nothing changes if I set it to 124. So what the purpose of it?  :slight_smile: 

Thanks in advance.

-------------------------

thebluefish | 2017-01-02 01:07:21 UTC | #2

I'm not getting the same issue. I am first noticing a typo, though. The extension 'sdf' should be 'ttf'.

Here's a couple examples:

[url=http://i.imgur.com/zOF8PeF.png][img]http://i.imgur.com/zOF8PeFm.png[/img][/url]
[code]mushroomTitleText->SetFont(cache->GetResource<Font>("Fonts/BlueHighway.ttf"), 24);[/code]

[url=http://i.imgur.com/oZORWm7.png][img]http://i.imgur.com/oZORWm7m.png[/img][/url]
[code]mushroomTitleText->SetFont(cache->GetResource<Font>("Fonts/BlueHighway.ttf"), 124);[/code]

-------------------------

aster2013 | 2017-01-02 01:07:21 UTC | #3

The SDF font is a special bitmap font. The font size of SDF is the size to build SDF font, if you need a large SDF font, you can build it yourself with bigger font size.

-------------------------

Egorbo | 2017-01-02 01:07:22 UTC | #4

Oh thanks, guys! I didn't notice it was not ttf.

-------------------------

