Mike | 2017-01-02 00:58:24 UTC | #1

When activating the console on Android, the virtual keyboard immediately pops up, which is not always desirable.

I'd like to know how to slightly tweak this behavior from lua script, so that virtual keyboard gets activated only when the console's lineEdit is touched.
I've already tried to modify lineEdit using console.lineEdit but with no success.

Currently the keyboard pops up and I press Enter to remove it.

-------------------------

cadaver | 2017-01-02 00:58:24 UTC | #2

There is now a property (focusOnShow) in Console to control the behavior. It defaults to false on platforms that show the screen keyboard for LineEdit's.

-------------------------

Mike | 2017-01-02 00:58:25 UTC | #3

Awesome, console is an invaluable tool  :slight_smile:
Many thanks.

-------------------------

