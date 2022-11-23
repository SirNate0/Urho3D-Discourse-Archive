najak3d | 2020-09-03 17:05:06 UTC | #1

We want to set up a new scene for a pop-up form, which needs to render it's own scene, separate from the main form.  What is the best way to go about this?

Currently, we are considering creating a whole new Urho Application to do this, but I'm not a fan of having multiple "Contexts" for graphics resources/etc.   Is there a way to use the same Urho App (and Resources/Context) to render to multiple Surfaces? (in Windows, I'm talking about multiple Windows Controls)

-------------------------

Modanung | 2020-09-03 18:19:58 UTC | #2

Maybe [QUrho](https://discourse.urho3d.io/t/the-legendary-fish-on-your-desktop/5455) can help?

-------------------------

Eugene | 2020-09-03 18:36:02 UTC | #3

I know that ImGUI backend in rbfx can somehow render multiple "surfaces" (i.e. multiple system windows) on Desktop platforms.
Therefore, it should be possible to do with some tweaking on C++ side.
I admit that I have no clue what exactly has to be done.

-------------------------

Modanung | 2020-09-03 20:55:07 UTC | #4

If you render to texture you can draw it wherever you like.
```
static QPixmap toPixmap(Image* image) {
     return QPixmap::fromImage(QImage{
                   image->GetData(),
                   image->GetWidth(),
                   image->GetHeight(),
                   QImage::Format_RGBA8888 });
}
```

-------------------------

najak3d | 2020-09-03 20:56:34 UTC | #5

Modanung - RTT might be what we end up doing, to keep this lightweight.  Thanks for the suggestion and code example.

-------------------------

