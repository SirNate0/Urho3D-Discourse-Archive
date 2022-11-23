smellymumbler | 2017-12-14 19:01:19 UTC | #1

I'm using XML for my serialized scenes in Urho and I'm trying to find out an efficient way of updating the scene in realtime, whenever the XML file changes. My first prototype makes use of this: 

http://doc.qt.io/qt-5/qfilesystemwatcher.html

But I don't want to bundle the entire QT framework just for this. Does anyone know any elegant way of achieving this task?

-------------------------

Elendil | 2017-12-13 21:24:49 UTC | #2

OS Api 
if you are on windows check [this](https://msdn.microsoft.com/en-us/library/aa364391(v=vs.85).aspx) or [this](https://msdn.microsoft.com/en-us/library/aa365465(v=vs.85).aspx).
There is some [example1](https://msdn.microsoft.com/en-us/library/aa365261(VS.85).aspx) and [example2](https://msdn.microsoft.com/en-us/library/aa364052(v=vs.85).aspx).

or

try [poco](https://pocoproject.org/index.html) library.

-------------------------

Eugene | 2017-12-14 19:01:31 UTC | #3

Urho already sends `E_RELOADSTARTED`/`E_RELOADFINISHED`/`E_RELOADFAILED` for each changed resource. Isn't it enough?

-------------------------

smellymumbler | 2017-12-13 21:54:57 UTC | #4

I didn't know that. Thanks for the info!

-------------------------

