Alex-Doc | 2017-06-27 10:42:30 UTC | #1

Hi everyone, my first topic here!
I've just noticed that some Events I send from C++ won't get called into my AngelScript scripts if the frame rate is low and the minimum frame rate is set lower(so it does not kick in).

I'm not sure whether it is a known normal behavior, a logic error of mine or something that needs further investigation.
Any clues?

The event is called in the Update function.

-------------------------

Alex-Doc | 2017-06-27 10:40:00 UTC | #2

A quick update in case someone else is getting this problem:

1) Be careful when mixing FixedUpdate and Update.
2) Seems that node.GetChild() and GetChildren() doesn't always return the child pointer if under stress.(AngelScript)

About point 2, I'm not sure if it's a wanted behavior or not.
I'm setting this topic as solved, but it surely needs some more investigation.

I'm also renaming the topic since it was unrelated to actual events.

-------------------------

