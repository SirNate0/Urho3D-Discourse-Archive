BananaIguana | 2017-01-02 01:10:37 UTC | #1

Hello all,

So I'm fairly new to Urho3D and I'm in the process of porting a game across to this engine. My game is 2D and doesn't use the depth buffer, the order I add the sprites is the order they are drawn. I'm trying to fix this bit in the Urho3D version but I'm getting some strange behaviour. I've no doubt this is a simple misunderstanding on my part but any advice would be appreciated.

So, I add a bottom layer of sprites and they render fine. I then add a second upper layer of sprites and they seem to draw sporadically. Some are visible, some are not (different with each run). At this point it's obvious they are using the same Z space and the render order is just different each time I run as it shows a different mix of visible sprites. From this point, I draw the bottom layer with Z values fixed behind the upper layer. Confusingly, this doesn't seem to solve this issue. If I turn off the bottom layer completely, I can see the upper layer rendering perfectly but as soon as I add both layers, they suffer form Z order issues, even though I specify different Z values.

Obviously I'm missing something, do doubt fairly trivial but if anyone could suggest things to check, I would be grateful.

-------------------------

gawag | 2017-01-02 01:10:38 UTC | #2

I'm not really familiar with 2D in Urho but UIElement (like Sprite) has a SetPriority function: [urho3d.github.io/documentation/1 ... 513726de7c](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_u_i_element.html#a5a2f548ac25ff0b8dbcd51513726de7c)
And Drawable2D (base class of all 2D things I suppose) has a SetLayer function: [urho3d.github.io/documentation/1 ... 0124a9d17b](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_drawable2_d.html#ac9f626566fe697b52a9a480124a9d17b)
Drawable2D has also a SetOrderInLayer(int orderInLayer).

Does setting the priority/layer/order work as expected?
Or did you already try that and mean that by setting Z values?

-------------------------

BananaIguana | 2017-01-02 01:10:40 UTC | #3

Thank-you gawag. You're suggestions worked perfectly!  :smiley:

-------------------------

