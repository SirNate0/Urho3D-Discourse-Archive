codexhound | 2019-08-03 22:18:56 UTC | #1

In 1.7.1 when implementing a raycasting feature I ran into a bug where the cursur of the UI subsystem was a nullptr.

-------------------------

Leith | 2019-08-04 08:56:06 UTC | #2

Hey codexhound, welcome to the community! :boom:

Be aware there are two kinds of cursors in Urho - the system cursor, and custom UI cursor - if you did not create a custom UI cursor, then none exists, and that would very likely explain the null exception.
Generally, I recommend using a custom cursor, if for no other reason, than this: not all platforms have a native cursor.

-------------------------

codexhound | 2019-08-04 09:20:48 UTC | #3

Thanks, this is my new favorite engine. Was looking for a broadly programmatic and lightweight one and finally found it. I highly dislike the UI based ones like unity. I'll keep that in mind about the cursor but I'm still not sure whether this a bug or a feature???!

-------------------------

Leith | 2019-08-04 09:31:11 UTC | #4

It's a feature - there is support for "native cursors" but I don't recommend that pathway. Use a virtual cursor, and it works on all platforms. I can provide more information on request. Don't want to poison your thread!

-------------------------

Leith | 2019-08-04 09:32:49 UTC | #5

- Yeah its my favourite engine lately as well. It's pretty solid, and it's free, like free beer, free.

-------------------------

