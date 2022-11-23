BananaIguana | 2017-01-02 01:09:45 UTC | #1

I'm using the 2D features of Urho3D and I have a question about StaticSprite2D.

I would like to set the colour of each vertex which makes up the sprite. I understand StaticSprite2D only has one method which sets the colour for all 4 verticies. To achieve this, is it best to subclass StaticSprite2D and modify it to deal with this one-off case or is there perhaps a better approach?

-------------------------

Bananaft | 2017-01-02 01:09:47 UTC | #2

Custom geometry might be a better approach.

-------------------------

