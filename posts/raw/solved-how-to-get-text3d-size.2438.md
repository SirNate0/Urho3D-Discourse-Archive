1vanK | 2017-01-02 01:15:24 UTC | #1

I need know size of Text3D component for manual positioning. I try to use BoundingBox for it, but
[img]http://savepic.ru/12415978.png[/img]
Any another way?

-------------------------

cadaver | 2017-01-02 01:15:24 UTC | #2

It looks odd that worldBoundingBox should be illegal, because in that case it shouldn't be able to render either.

You have a couple of other options. GetWidth() / GetRowHeight() / GetNumRows() should allow access to the underlying UI element's dimensions. GetHeight() seems to be missing but shouldn't be no reason why it shouldn't be added.

Since Text3D is a drawable you should also be able to access its local-space bounding box (GetBoundingBox()).

-------------------------

1vanK | 2017-01-02 01:15:24 UTC | #3

The first few times

[img]http://savepic.ru/12437266.png[/img]

-------------------------

1vanK | 2017-01-02 01:15:24 UTC | #4

[code]void Text3D::UpdateTextBatches()
{
    uiBatches_.Clear();
    uiVertexData_.Clear();

    text_.GetBatches(uiBatches_, uiVertexData_, IntRect::ZERO);
[/code]

uiVertexData_ is empty the first few times, but textDirty_ is setted to false

-------------------------

1vanK | 2017-01-02 01:15:24 UTC | #5

As far as I understand, at the beginning "text_.GetBatches" executes when font == null (before set font) and result is infinite bounding box.
And in my game I recieve infinite position of my node. After that any mathematical operation with this infinite pos lead to error. May be Text3D without font should be zero?

-------------------------

cadaver | 2017-01-02 01:15:24 UTC | #6

I pushed a change where the bounding box will be zeroed if there's no text content yet.

After setting both font & text the bounding boxes should have a valid size. At least when testing with the sample 35.

-------------------------

1vanK | 2017-01-02 01:15:25 UTC | #7

It helped me, big thanks!

-------------------------

