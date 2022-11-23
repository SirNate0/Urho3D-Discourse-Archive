codingmonkey | 2017-01-02 01:01:03 UTC | #1

I try bring to life palm trees on lands and i use VegetationDiff technique for it.
And here is what I got 
[video]http://www.youtube.com/watch?v=SBVBfw3GbeE[/video]
What is this strange movement? it's like micro-shifts then camera move
Why can this be?

-------------------------

codingmonkey | 2017-01-02 01:01:08 UTC | #2

There are even no guesses why this happens?

-------------------------

cadaver | 2017-01-02 01:01:08 UTC | #3

That actually looks quite like it should. The example vegetation shader is very simple, it moves the XZ coordinates of the model depending on the height (Y). It doesn't properly rotate so that you may get a strange kind of shearing. The shader is provided only as an example (like every asset that comes with the Urho repository) and for real-world use cases you probably need to write your own, more sophisticated one.

-------------------------

codingmonkey | 2017-01-02 01:01:08 UTC | #4

okay, probably better in this situation to make animation for wood

-------------------------

