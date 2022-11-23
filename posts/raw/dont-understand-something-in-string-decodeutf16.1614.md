graveman | 2017-01-02 01:08:56 UTC | #1

Hello! I thought a lot of  time and could not understand why in String::DecodeUTF16 method  is it used bitwise "or" operator instead of sum in this code:
[code]return ((word1 & 0x3ff) << 10) | (word2 & 0x3ff) | 0x10000;[/code]

Why not [code]return ((word1 & 0x3ff) << 10) | (word2 & 0x3ff) + 0x10000;[/code] ?

-------------------------

cadaver | 2017-01-02 01:08:57 UTC | #2

You have uncovered a bug :slight_smile: Thanks!

-------------------------

graveman | 2017-01-02 01:08:57 UTC | #3

Wow, really? I'm glad I could help.

-------------------------

