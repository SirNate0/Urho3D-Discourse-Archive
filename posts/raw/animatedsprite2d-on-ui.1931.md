Kanfor | 2017-01-02 01:11:38 UTC | #1

Hi, urhofans. It's me again  :smiley: 

Can I add an AnimatedSprite2D to UI?

And other type of animated sprite made with Spriter?

Thank you very much! :wink:

-------------------------

miz | 2017-01-02 01:11:58 UTC | #2

Hi Kanfor, did you figure out how to do this? I'm trying to do the same now...

-------------------------

weitjong | 2017-01-02 01:11:58 UTC | #3

I don't think this is possible if by "UI" here you meant the UI subsystem. The UI subsystem uses it own batches to draw those UI elements last, so they always stay on top of your scene. While 2D and 3D drawables are part of your scene component objects.

-------------------------

cadaver | 2017-01-02 01:11:58 UTC | #4

You could possibly (mis)use the "renderui" renderpath command, meaning you would render the UI in the middle of scene rendering, then continue with more scene passes to draw a sprite on top. Another (if applicable) is to use the View3D UI element which allows to render a scene into a texture and display it in the UI. May not be good for performance though.

-------------------------

miz | 2017-01-02 01:11:58 UTC | #5

Is there a way to grab the texture from the AnimatedSprite2D then render it to a UIElement?

Something like UISprite->SetTexture(animatedsprite2d->GetSprite()->GetTexture());

-------------------------

cadaver | 2017-01-02 01:11:58 UTC | #6

Not directly. Having your AnimatedSprite2D in a separate scene, which View3D displays, is the closest to this. Note that you can queue the rendering of a View3D's texture on-demand, it doesn't have to update every frame.

-------------------------

