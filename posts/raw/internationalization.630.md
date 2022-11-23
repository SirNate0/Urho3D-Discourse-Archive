OvermindDL1 | 2017-01-02 01:01:45 UTC | #1

I was looking earlier for how to handle Internationalization but not finding anything in the system.  How does Urho3D handle Internationalization?  If it does not would you accept a license compatible embeddable library to handle the conversions?  Does the text rendering in Urho3D already handle unicode and right-to-left codepoints and are there any samples that I am missing?

-------------------------

weitjong | 2017-01-02 01:01:45 UTC | #2

I don't think we have internationalization support like you expect yet. At the moment the Text class supports rendering text string encoded in UTF8 format, but I think that's about it.

-------------------------

