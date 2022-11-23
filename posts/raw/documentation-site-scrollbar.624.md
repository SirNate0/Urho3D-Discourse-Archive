OvermindDL1 | 2017-01-02 01:01:43 UTC | #1

For some reason there is a bit of CSS on the documentation site [urho3d.github.io/](http://urho3d.github.io/) that is making the scrollbar [size=85]tiny[/size] on webkit in main.css (main-min.css):
[code]
::-webkit-scrollbar {
width: 6px;
}
::-webkit-scrollbar-thumb {
border-radius: 10px;
-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.5);
}
::-webkit-scrollbar-track {
-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
border-radius: 10px;
}
[/code]
And maybe others, but it is making the scrollbar utterly tiny on my screen, extremely thin and hard to click.  Could this CSS and any related be removed?  :slight_smile:

-------------------------

weitjong | 2017-01-02 01:01:44 UTC | #2

Thanks for the feedback. It is actually "designed" to look that way  :laughing: . Or should I say the website is designed for user who has a mouse with mouse wheel. You are right to say that it is not designed to be clicked at. I guess the beauty of a design is in the eye of the beholder. Personally I hardly remember when the last time I click on the vertical scrollbar in order to scroll the page. If it really troubles you then perhaps you can use Tampermonkey to change the CSS of the website in your browser locally.

-------------------------

OvermindDL1 | 2017-01-02 01:01:45 UTC | #3

[quote="weitjong"]Thanks for the feedback. It is actually "designed" to look that way  :laughing: . Or should I say the website is designed for user who has a mouse with mouse wheel. You are right to say that it is not designed to be clicked at. I guess the beauty of a design is in the eye of the beholder. Personally I hardly remember when the last time I click on the vertical scrollbar in order to scroll the page. If it really troubles you then perhaps you can use Tampermonkey to change the CSS of the website in your browser locally.[/quote]
Heh, I can change it locally easily enough but my usecase is actually a touchscreen and trying to tap on that very thin bar is a bit... difficult.  Takes a few attempts.  Web standards are good.  :wink:

-------------------------

weitjong | 2017-01-02 01:01:45 UTC | #4

I just wonder. If you have a touchscreen, don't you just swipe up and down to scroll the page? The chosen WebKit design is exactly to match the look of Safari/Chrome on mobile device. If I could make FireFox looks that way with CSS, I may have done it too.

-------------------------

OvermindDL1 | 2017-01-02 01:01:46 UTC | #5

[quote="weitjong"]I just wonder. If you have a touchscreen, don't you just swipe up and down to scroll the page? The chosen WebKit design is exactly to match the look of Safari/Chrome on mobile device. If I could make FireFox looks that way with CSS, I may have done it too.[/quote]
Not here, it is still a desktop computer with normal desktop chrome with a wifi mini-screen touchpad I use when I am sitting on the couch, usually not an issue unless the scrollbar is 6px wide.  :wink:

-------------------------

weitjong | 2017-01-02 01:01:46 UTC | #6

I have an Apple bluetooth Magic TrackPad which are "connected" to my workstation running Linux OS which is not officially supported by the TrackPad, but yet it is awfully easy these days to pair them up in Linux and setup the gestures to perform certain tasks. I can use a two finger swipe to scroll the page up or down and it scrolls in a "natural way" too as if I am using a touch device. :wink:

-------------------------

OvermindDL1 | 2017-01-02 01:01:49 UTC | #7

[quote="weitjong"]I have an Apple bluetooth Magic TrackPad which are "connected" to my workstation running Linux OS which is not officially supported by the TrackPad, but yet it is awfully easy these days to pair them up in Linux and setup the gestures to perform certain tasks. I can use a two finger swipe to scroll the page up or down and it scrolls in a "natural way" too as if I am using a touch device. :wink:[/quote]
Ooo, I have looked at those, they work well?  I actually use an old HTC One M7 with a VNC session through ssh to my desktop to use anywhere in my home (or, well, elsewhere when I am not home too) with a programmers keyboard on it (so I have all my function keys and more in easy access).  It is convenient to lay back on my couch while relaxing and read articles or code or so on my big screen while controlling from my HTC One-remote.  ^.^

-------------------------

