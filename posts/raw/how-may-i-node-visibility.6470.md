grokko | 2020-10-28 05:56:31 UTC | #1

Hi All!,
  How may I change the visibility (bool on/off) of a Node?

LF

-------------------------

Modanung | 2020-10-28 05:54:44 UTC | #2

Technically speaking, `Node`s are _always invisible_. It is the graphics components that adorn them which are visible. Both the nodes and components have `SetEnabled(bool)` functions.

-------------------------

grokko | 2020-10-29 01:31:52 UTC | #3

Okay...I figured it out...we had to make a hard register call...like

...Laser::RegisterObject(context);...once we had the template pointer 'Laser'.

Works perfectly, my objects are all on the queuing cycle!

Lord Fiction

-------------------------

