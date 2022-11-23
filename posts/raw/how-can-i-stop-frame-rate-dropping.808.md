att | 2017-01-02 01:03:02 UTC | #1

Hi,
How can I stop the dropping of frame rate when no input actions?

-------------------------

hdunderscore | 2017-01-02 01:03:37 UTC | #2

This is difficult to answer without knowing what's causing the frame drops. Have you profiled the code at all ?

-------------------------

cadaver | 2017-01-02 01:03:37 UTC | #3

Which platform or OS are you talking about?

Urho has a default framerate throttle for when the application window does not have input focus, but loss of input focus should not happen on any OS automatically just due to lack of input. Rather, this sounds like a power saving feature kicking in. Urho doesn't expose any settings for power management so you would have to use the native OS API if you want, or just try adjusting the device settings.

-------------------------

