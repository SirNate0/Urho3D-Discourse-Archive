keepclear | 2021-08-02 01:51:37 UTC | #1

Hello,

I see a difference between the memory use shown by "F2" in-game versus the one in task manager. Although a gap is normal and expected, the behavior is a bit surprising.
I took the Hello World sample (VS2019, master), made it resizable with:
> engineParameters_[EP_WINDOW_RESIZABLE] = true;

and then I resize the window by up/downsizing it a couple dozen times and I see memory growing significantly in windows task manager whereas in-game memory stats are stable. 
In task manager, when I stop resizing the window, memory seems to be slowly "shrinking back" over time but remain bigger from what it is when freshly started.
I should mention that memory grows even when the up/downsizing cycle is kept smaller than the window size when the app starts.

Any idea what could cause this behavior?

-------------------------

