johnnycable | 2017-05-11 16:59:58 UTC | #1

I want to make a node into a group of StaticSprite2D, that is a node with a group of sprites within. How do I know / calculate their total size? 
The only way I found for checking size is:
>         auto nodePosition = child->GetNode()->GetPosition2D();
>         auto nodeWidth = child->GetSprite()->GetRectangle().Width() * PIXEL_SIZE;
>         auto nodeHeight = child->GetSprite()->GetRectangle().Height()  * PIXEL_SIZE;
by getting the resource size.
Or that is not possible, I can only have a 1:1 relationship node<->StaticSprite2D component?
It doesn't look that way, because in the editor i can create a node and multiple StaticSprite2D within it.
Or I need to have a group node alone with n nodes each one set with a single StaticSprite2D?
And for 3D? I'd be able to use AABB min & max for a compound node total size, and even for 2d, but how?

-------------------------

slapin | 2017-05-11 19:55:08 UTC | #2

I'd use Rect and fill it with Rects... or BoundingBox for 3d.

-------------------------

johnnycable | 2017-05-11 20:55:50 UTC | #3

Yes, I know about Rects, but what I really need to know is big a sprite is.
Now, only nodes have position; components don't. So if I have multiple sprites(comps) on a node, only one must be "active"... the others can be switched for I think...

-------------------------

