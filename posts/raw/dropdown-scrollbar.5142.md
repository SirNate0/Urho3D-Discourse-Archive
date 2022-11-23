NessEngine | 2019-05-08 22:50:12 UTC | #1

How do I add a scrollbar to a dropdown GUI element, so I can limit its height but still have really large lists?

Thanks!

-------------------------

Leith | 2019-05-09 17:28:00 UTC | #2

Hi, NessEngine!

I've got almost no experience with Urho3D GUI stuff, so I went looking for an answer to your question.
Chances are I'll be needing this kind of thing very soon...

DropDownList has a method called GetListView(), which returns a ListView object representing your dropdown element... as it so happens, the ListView class derives from ScrollView, which has a method called SetScrollBarsVisible, and another called SetScrollBarsVisibleAuto.
I hope that helps! :)

-------------------------

NessEngine | 2019-05-09 14:53:01 UTC | #3

Works great, thank you! :)

-------------------------

