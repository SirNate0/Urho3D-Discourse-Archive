cadaver | 2017-01-02 01:05:29 UTC | #1

The window focus knowledge originally comes from SDL, so theoretically you could detect the situation there and fix SDL. If not, your solution sounds as good as any. Another thing to investigate is whether there's any ill effects from assuming that an external window always has focus, since we shouldn't ever be doing invasive procedures like hidden mouse centering on it anyway.

-------------------------

