Jetmate | 2017-11-19 06:25:19 UTC | #1

From what I've seen, the Controls class can be summarized by these three functions:
```
void Set(unsigned buttons, bool down = true)
{
    if (down)
        buttons_ |= buttons;
    else
        buttons_ &= ~buttons;
}

/// Check if a button is held down.
bool IsDown(unsigned button) const
{
    return (buttons_ & button) != 0;
}

/// Check if a button was pressed on this frame. Requires previous frame's controls.
bool IsPressed(unsigned button, const Controls &previousControls) const
{
    return (buttons_ & button) != 0 && (previousControls.buttons_ & button) == 0;
}
```
How is this code able to keep track of the state of any number of buttons in a single `button` variable? Is this the standard way to keep track of user input?

-------------------------

Eugene | 2017-11-19 10:08:24 UTC | #2

[quote="Jetmate, post:1, topic:3760"]
How is this code able to keep track of the state of any number of buttons in a single button variable?
[/quote]

It is supposed that user don't need more than 32 separate controls.

[quote="Jetmate, post:1, topic:3760"]
Is this the standard way to keep track of user input?
[/quote]
It is. Note that you always can pass as much data as you need in `extraData_`

-------------------------

Jetmate | 2017-11-19 15:00:42 UTC | #4

I guess my question is more about how `buttons_`, which is just an `unsigned` value, can keep track of multiple values.

-------------------------

Eugene | 2017-11-20 19:32:56 UTC | #5

It's not _just_ unsigned integer, it's up to 32 binary controls in bitfield ;)
But it isn't designed to keep multiple _integers_ like keycodes, that's true. Only multiple bits.

-------------------------

Jetmate | 2017-11-19 15:30:39 UTC | #6

What's the advantage to using bitfields? They seem very confusing, especially for beginners.

-------------------------

Eugene | 2017-11-19 15:46:22 UTC | #7

Bitfield is small and enough for the most cases, that's all. If you don't like bitfields or it's not enough for you, just push whatever you want into extraData_.

-------------------------

Modanung | 2017-11-19 17:53:56 UTC | #8

If you just want to make things work at first (without networking down the pipeline) you could just read your input directly from the `Input` SubSystem with:
```
GetSubsystem<Input>()->GetKeyDown(int key)
```

-------------------------

