codefive | 2019-05-30 21:12:32 UTC | #1

I have been using the First Project template for my porpuses, great one, but now i want to create more classes, but i dont know which should be its inheritance, the model class?

I want this class to do the following.-

1.- Create a parent node
2.- Based on that parent node create several subnodes, all based in little 3D models, (i dont care if they are only Boxes)
3.- That way i will have a more complex 3D Model but attached to the parent node (and its sub nodes)
4.- Alter the model position (i think a simple function will do that or constructor)
5.- Place later the model in my main Application class (yep other story)

Could someone give me a hint to create such a class? Basically i dont know which its inheritance should be. Or this is too much for me a beginner ? I been reading a lot, thank you in advance

-------------------------

Modanung | 2019-05-30 21:38:04 UTC | #2

I'd inherit from `LogicComponent` and in its `OnNodeSet(Node* node)` create the sub-nodes and their models. During the `Update(float timeStep)` it would modify the position of it's child nodes.

-------------------------

codefive | 2019-05-30 21:40:42 UTC | #3

Oh such a precious information, thank you @Modanung now i can just begin LOL :slight_smile:

-------------------------

Modanung | 2019-05-30 21:45:15 UTC | #4

Furthermore you will have to register your component - before instantiation - by calling `RegisterFactory<MyComponent>()` on the `Context`. Hereafter you can call `CreateComponent<MyComponent>()` on a node to conjure your component.

-------------------------

codefive | 2019-05-30 21:47:16 UTC | #5

Thank you again, in that i will need more reading, but with this kind of help from your part i will stop being a noob soon Thank you !!!

-------------------------

Modanung | 2019-05-30 22:17:17 UTC | #6

I made a simple component a year and a half ago for [demonstration purposes](https://discourse.urho3d.io/t/rotating-a-model-around-an-axis/3531) that may be of use to fill some more gaps in your understanding as well: ;)

https://github.com/Modanung/WindmillComponent/blob/master/windmill.h

https://github.com/Modanung/WindmillComponent/blob/master/windmill.cpp

-------------------------

codefive | 2019-05-30 22:22:33 UTC | #7

Great !! yes it helps a lot !!

-------------------------

