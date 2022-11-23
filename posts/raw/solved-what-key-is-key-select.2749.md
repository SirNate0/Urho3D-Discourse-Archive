ricab | 2017-05-04 00:12:44 UTC | #1

This key is used to pause samples (see Sample::HandleKeyDown). I have tried a bunch of keys and combinations, but I haven't found out which one it is...

-------------------------

TheComet | 2017-01-26 20:59:31 UTC | #2

Most keyboards don't have a `Select` key. It appears to be something from the old days.

I tried looking for an image of a keyboard that has a `Select` key but was not successful. Maybe Cadavar can take a picture of his keyboard? ;)

-------------------------

ricab | 2017-01-26 22:07:36 UTC | #3

I see, thanks. I wonder why it was chosen to pause the samples, and only when touch input is enabled. The corresponding bit of code, from HandleKeyDown, is:

```cpp
        // Preferences / Pause
        if (key == KEY_SELECT && touchEnabled_)
        {
            paused_ = !paused_;
            //...
        }
```

Is a KEY_SELECT KeyDown event generated in some special case in touch-enabled devices?

-------------------------

TheComet | 2017-01-26 22:15:48 UTC | #4

Maybe KEY_SELECT has a special function on tablets/mobile?

-------------------------

weitjong | 2017-01-27 06:24:14 UTC | #5

When touch is enabled, we can use the UI-elements to emulate buttons or joystick hats or what have you and bind them to any keys. In our samples we have that demonstrated by binding one of the button to KEY_SELECT for pause/unpause toggle, mimicking the behavior of "Select" button on DualShock gamepad. In hindsight, we should not have added the condition to check for touch-enabled flag in the sample code because user may actually have a real gamepad attached.

-------------------------

ricab | 2017-01-27 15:36:11 UTC | #6

Thanks, much clearer now.

-------------------------

