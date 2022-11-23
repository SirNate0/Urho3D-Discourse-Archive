rku | 2017-01-02 01:13:32 UTC | #1

Why Text ui element has SetText() and SetTextAttr()? SetTextAttr() does less stuff and setting text attribute does not update text that is rendered as a result. This was rather unexpected. I am making UI editor and now it warrants a special case handling. I would love to understand why.

-------------------------

1vanK | 2017-01-02 01:13:32 UTC | #2

[github.com/urho3d/Urho3D/issues/1451](https://github.com/urho3d/Urho3D/issues/1451)

-------------------------

cadaver | 2017-01-02 01:13:32 UTC | #3

Call ApplyAttributes() when you're finished setting attributes in the editor tool. Sometimes this does late operations that would be too costly to do for every attribute access. Deserialization (LoadXML and such.) automatically calls that after looping through attributes.

SetXXXXAttr() functions in various classes are just internal functions used for attribute access when side-effects or somehow different behavior from the actual public API is necessary.

-------------------------

rku | 2017-01-02 01:13:32 UTC | #4

oh i see, thank you

-------------------------

