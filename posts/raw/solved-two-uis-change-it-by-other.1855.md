Kanfor | 2017-01-02 01:10:45 UTC | #1

Hi, urhofriends.

I have two UIs and I would like change one by the other.
What is the better way to do it? Do I delete one of them?
Now, If I CLEAR one, I yet see his elements in the other UI.

Thank you!

-------------------------

hdunderscore | 2017-01-02 01:10:45 UTC | #2

You can just hide (SetEnable(false)) the one you don't need, that way you don't need to reallocate memory etc when you need it again if you are using it often.

-------------------------

Kanfor | 2017-01-02 01:10:45 UTC | #3

SetEnable not works, only SetVisible. Is it the same?

By the way, how can I destroy on the them?

-------------------------

cadaver | 2017-01-02 01:10:45 UTC | #4

SetEnabled() is for input/interactability, SetVisible() is for visibility. When you RemoveChild() a UI element, it will get destroyed if it's not held alive by a SharedPtr in your own code.

-------------------------

Kanfor | 2017-01-02 01:10:45 UTC | #5

Oh, great. Now I see the difference  :wink: 

Thank you!

-------------------------

