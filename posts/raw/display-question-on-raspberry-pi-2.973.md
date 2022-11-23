esak | 2017-01-02 01:04:32 UTC | #1

When I run the samples (from 1.32) on my Pi 2 connected to my TV, some of the graphics are drawn outside of the TV display (the samples run in full-screen).
This is especially visible when I activete the debug HUD, where some of the text is not visible (at the borders).
When I start a sample the debug info says that it's starting in screen mode 1920 x 1080 windowed.
The TV is in 1080p50Hz mode.
What can the problem be? Is it some setting on my Pi 2, my TV, or some bug in the samples?
(I don't have this problem in the Pi 2 console, nor in the startx mode.)

-------------------------

thebluefish | 2017-01-02 01:04:32 UTC | #2

Likely an overscan setting in your TV. Most TVs expect the signal to have ~10% of overscan, and will actually crop those edges out.

Each model does it differently. My plasma, for example, has an alternative HDMI option that disables overscan. My LED TV on the other hand actually has an "overscan" option.

-------------------------

esak | 2017-01-02 01:04:33 UTC | #3

I tried first to change the overscan settings in /boot/config.txt. But this had only effect on the terminal display, not on the samples.
Then I found the option on my TV to disable overscan, then it displayed right in the samples. :slight_smile:
I'm just a little confused why the settings in /boot/config.txt only affects the terminal window and not the samples!?

-------------------------

GoogleBot42 | 2017-01-02 01:04:33 UTC | #4

I think that this might be because X gets the resolution of the monitor/TV directly.  Thus, it ignores the settings in /boot/config.txt  Perhaps there is a way to force X to respect these settings.

EDIT: 100th post yay! :stuck_out_tongue:

-------------------------

