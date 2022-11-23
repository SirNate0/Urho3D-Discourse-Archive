greenhouse | 2017-01-02 01:08:49 UTC | #1

Hi, I'm interested in trying develop games with Urho3D/C++.

Currently I'm developing 2D games (with physics) for mobile (iOS/Android) with Cocos2d-x/C++.

I always find it hard to integrate 3rd side services to game rather then developing a game itself.
Cocos2d-x has added recently SDKBOX to ease services integration such as Analytics (Flurry, GA, etc), Ads (Chartboost, Appodeal, etc..), Social (Facebook) and etc which is a big help for any indie developer I guess.
I want to know how hard it will be to integrate all those services into Urho3D game?

-------------------------

greenhouse | 2017-01-02 01:08:58 UTC | #2

Anybody writing a games with Urho3D who uses such services in their games? :slight_smile:

-------------------------

umen | 2017-01-02 01:09:09 UTC | #3

First of all try to make Urho3d to work on real device , i had allot of problem with it and still can't make it work.
see this thread .
[url]http://discourse.urho3d.io/t/ios-skipped-autoload-path-autoload-exception-in-deployme/1624/1[/url]

i had always problems with iOS real device . 

you could integrated the third party libs easily . from cocos2d-x world you can take what sonar offers and modify it to be used with Urho3d they both c++ 
[url]http://www.sonarlearning.co.uk/coursepage.php?topic=game&course=sonar-cocos-helper&videoindex=6467#6467[/url]

-------------------------

