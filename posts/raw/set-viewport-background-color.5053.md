capelenglish | 2019-03-29 15:28:18 UTC | #1

I resizie my graphics window after the game starts as follows:

> scene_ = new Scene(context_);
> Graphics* graph = GetSubsystem&lt;Graphics&gt;();
> graph-&gt;SetMode(1280, 800, false, true, false, false, false, false, 1, 1, 1);
> // set the viewport dimensions and position
> graph-&gt;SetMode(width, height);
> graph-&gt;SetWindowPosition(left,0);
> scene_ = new Scene(context_);

My problem is that this "padding" has a light gray color. How do I change this color to black?

-------------------------

Pencheff | 2019-03-29 19:44:37 UTC | #2

You are calling Graphics::SetMode twice, the second call is not necessary.
Also, check the log for a line that says something like:
`Set screen mode 1280x720 windowed monitor 0 resizable`

-------------------------

WangKai | 2019-03-30 02:30:04 UTC | #3

Hi, capelenglish,

You can use following code to set the background color (clear color) 

`GetSubsystem<Renderer>()->GetDefaultZone()->SetFogColor(Color(0.0f, 0.0f, 0.0f));`

and you can also add an extra `Zone` and set the colors.

-------------------------

Leith | 2019-03-30 03:40:36 UTC | #4

When setting fog colour on a zone, don't forget to also set the ambient colour, which basically provides a minimum colour (and intensity) for ambient lighting, ie, how rendered surfaces will appear, in the absence of any lighting.
[code]
            zone->SetAmbientColor(Color(0.25f, 0.25f, 0.25f));
            zone->SetFogColor(Color(0.5f, 0.5f, 0.7f));
[/code]

-------------------------

capelenglish | 2019-04-01 18:53:31 UTC | #5

I guess my question wasn't very clear. By background, I meant the viewport background. I'm displaying my game using a projector with a resolution of 1280x800, but I only wanted to use 800x780 of the display. I was able to solve my problem by setting the enigne parameters:

    engineParameters_[EP_WINDOW_WIDTH] = width;
    engineParameters_[EP_WINDOW_HEIGHT]= height;    
    engineParameters_[EP_WINDOW_POSITION_X]= left;
    engineParameters_[EP_WINDOW_POSITION_Y]= top;

Thanks for responding. If you are wondering why I would want to do this, it's a long and convoluted story related to a work project.

-------------------------

Modanung | 2019-04-01 20:05:35 UTC | #6

https://discourse.urho3d.io/t/background-color/1510/2

-------------------------

