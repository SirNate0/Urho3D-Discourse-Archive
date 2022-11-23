rku | 2017-01-02 01:11:41 UTC | #1

I am implementing attribute inspector based on editor UI layout. I want AttributeList and AttributeContainer to be of max size possible and have scrollbar in ParentContainer. However no matter what i try AttributeList and AttributeContainer are of fixed size. Resizing them just resets size to what already is there. I am attaching xml dump that can be loaded in editor for inspection. Any hints what i should change in layout to make said elements resize would be greatly appreciated.

xml: [gist.github.com/anonymous/5e126 ... 7ca0a566c2](https://gist.github.com/anonymous/5e1268ef5efc0fe96bdc357ca0a566c2)

-------------------------

Enhex | 2017-01-02 01:11:41 UTC | #2

You can use non-free Layout mode so the children of the element  are automatically sized and positioned.

If you want to resize an element to window size,  the UI's root element is automatically resized to the window size, and you can subscribe to it's E_RESIZED event and use the Graphics subsystem to get the window size.

-------------------------

rku | 2017-01-02 01:11:42 UTC | #3

If you looked at xml you would notice i nowhere used LM_FREE. Looks like only way to achieve this is positioning everything manually.

-------------------------

