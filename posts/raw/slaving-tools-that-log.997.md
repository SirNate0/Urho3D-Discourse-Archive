cadaver | 2017-01-02 01:04:42 UTC | #1

Any tool that creates the Context instance (which is a prerequisite for the Log subsystem to exist) should result in Thread::SetMainThread() being called. Is this not working? What is the system call you're using to spawn the tool?

-------------------------

cadaver | 2017-01-02 01:04:42 UTC | #2

This might be worth trying, which rather sets the console codepage and uses wprintf:
[stackoverflow.com/questions/2492 ... onsole-app](http://stackoverflow.com/questions/2492077/output-unicode-strings-in-windows-console-app)

Ideally strings should always be interpreted as unicode when printed to console and there should not be a separate function for that. On Unix PrintLine() & PrintUnicodeLine() already map to the same system call.

-------------------------

cadaver | 2017-01-02 01:04:43 UTC | #3

Trying to get sensible Unicode output on Windows through functions that are also capable of redirecting to a file seemed like an endless pit. Therefore it now simply detects whether stdout / stderr is redirected, and uses fprintf() in that case.

-------------------------

