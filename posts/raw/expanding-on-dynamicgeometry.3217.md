smellymumbler | 2017-06-06 21:13:54 UTC | #1

I have a few questions about the DynamicGeometry demo, mostly related to mesh manipulation:

* How would you implement extrusion?
* How would you implement inset?

-------------------------

George1 | 2017-06-08 07:04:36 UTC | #2

Look up CSG library for boolean, extrude and loft operations. There are a number of open source libraries out there.

-------------------------

smellymumbler | 2017-06-08 14:10:43 UTC | #3

Can't i just manipulate vertices and copy them around? :slight_smile:

What i mean is, do i really need a full-blown CSG library for doing object manipulation like this? I'm not doing brushes, addition or deletion, just face/vertex manipulation.

-------------------------

Modanung | 2017-06-09 20:24:07 UTC | #4

[quote="smellymumbler, post:3, topic:3217"]
Can't i just manipulate vertices and copy them around?
[/quote]

I guess you could start with a copy of the selected veritces' data, offset/scale that, remove the original faces and bridge the old and new with a tri strip. But there might be a more efficient - though probably very similar - method.

-------------------------

