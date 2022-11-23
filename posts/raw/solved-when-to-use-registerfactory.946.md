scorvi | 2017-01-02 01:04:20 UTC | #1

hey,

when do i use context->RegisterFactory<SomeNewClass>() to register my new class ? 
And when do i specify a category ?

-------------------------

cadaver | 2017-01-02 01:04:20 UTC | #2

If your class is a Component, Resource or UIElement subclass. Also, if you for some other reason want to instantiate your object by type with the CreateObject function.

Categories are for showing the component in the correct submenu in the editor.

-------------------------

scorvi | 2017-01-02 01:04:20 UTC | #3

ok thx

-------------------------

