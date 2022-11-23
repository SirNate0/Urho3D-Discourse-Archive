Canardian | 2017-01-02 00:58:54 UTC | #1

Are there any plans to add a MultiLineEdit UI item, or should I try to implement my own based on LineEdit?
I assume it would work if I make a "class MultiLineEdit : public LineEdit", or should LineEdit be expanded to support multiple linked LineEdits?

-------------------------

cadaver | 2017-01-02 00:58:54 UTC | #2

The thought has crossed my mind that it would be useful for things like in-game description editing, scripting, or even more sophisticated chat. However I'm not aware of concrete plans for this from myself or any core contributors so it will certainly be appreciated if you can implement / contribute one.

The Text class itself supports line splitting / word wrapping. and it should also handle multi-line selection rendering, it's only LineEdit that assumes it's editing a single line.

I imagine subclassing LineEdit will work. Or, if it leads to clumsy code, then refactor a base class for both LineEdit and the MultiLineEdit. I don't recommend linking several LineEdits, because they would each have their own Text element, in which case things like wordwrap wouldn't work properly.

-------------------------

Canardian | 2017-01-02 00:58:59 UTC | #3

I played around with inheriting LineEdit, but it seems it needs a lot of almost identical definitions in several other classes (UI.cpp at least), including xml style files.

Since the only difference between single line and multi line editing is actually how the Shift-Enter key is handled (to insert a line feed), maybe LineEdit could be simply expanded with an optional parameter to tell if it's single or multi line?

However, since more features will be needed too, like full-line-cursor, page-width-marker, foldable paragraphs, line numbers, vertical select, etc..., then it would make more sense again to inherit both LineEdit and MultiLineEdit (probably TextEdit sounds better) from a common core class.

-------------------------

cadaver | 2017-01-02 00:58:59 UTC | #4

UI.cpp shouldn't contain references to LineEdit except registering the object? Using style inheritance I'd believe the MultiLineEdit would need minimal additions to the style xml file, like <element type="MultiLineEdit" style="LineEdit" auto="false">

Thinking a bit more, the common base class (like TextEditBase or something) is very likely the best solution.

-------------------------

