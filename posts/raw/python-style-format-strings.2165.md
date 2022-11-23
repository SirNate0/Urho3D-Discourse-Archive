Sir_Nate | 2017-01-02 01:13:36 UTC | #1

[url]http://fmtlib.net/latest/index.html[/url] provides such. I'll probably use it for my own project regardless, but some of the things provided by the python-style format strings (mostly specifying argument order and repetition) I find to be very useful. Mostly I just want to be able to specify argument order and repetition in strings, which could be done internally, but apparently this library has very good performance (and is already written).
(To be clear, the more recent python format strings, not the copy of the printf style ones, e.g:) Formatting such as ToString("{1} {0} {1}",3.14, "hello") -> "hello 3.14 hello", as opposed to manually having to add the third argument.

If it is added, I would suggest a different function name, such as AsString or FormatString to not break compatability.

-------------------------

rku | 2017-01-02 01:13:37 UTC | #2

I would love that, but i guess it would provide little to no benefit including it in engine. I mean it would work mostly the same then whats the point..

-------------------------

hdunderscore | 2017-01-02 01:13:38 UTC | #3

I had begun work on a pull request previously with this feature, although my implementation wasn't very clean as far as an engine-feature goes. If you come to a clean PR, feel free to submit !

-------------------------

