codexhound | 2019-08-05 00:01:18 UTC | #1

Trying to get the pointer of the UI sender element on a handler and I am getting P_ELEMENT undef. Where is that defined or do I have to define it.

-------------------------

Pencheff | 2019-08-05 00:01:31 UTC | #2

It is defined inside a namespace of the event you are handling. 
[code]using namespace Pressed;[/code]

-------------------------

codexhound | 2019-08-04 22:37:56 UTC | #3

Thanks for the quick response

-------------------------

