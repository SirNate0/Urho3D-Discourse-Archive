ucupumar | 2017-01-02 01:00:22 UTC | #1

Do anyone know how to get/calculate current FPS on Urho?  :confused:

-------------------------

hdunderscore | 2017-01-02 01:00:22 UTC | #2

As far as I know, there's no built in for it. Two ways come to mind:

Quick and dirty:
[code]FrameInfo frameInfo = GetSubsystem<Renderer>()->GetFrameInfo();
text->SetText("FPS: " + String(1.0 / frameInfo.timeStep_));[/code]

Or more standard:
[code]void FPSCounter::Update(float deltaTime)
{
    counter += 1;
    timer += deltaTime;
    if (timer >= 0.5f)
    {
        text->SetText("FPS: " + String(counter/timer));
        timer = 0.0f;
        counter = 0;
    }
}[/code]

You would need to set up a 'Text* text' object in the above examples, and an object or event to do the update event in.

-------------------------

weitjong | 2017-01-02 01:00:22 UTC | #3

Urho3D has a Profiler class that does just that and more. In the samples, you can press F2 to see it in action.

-------------------------

ucupumar | 2017-01-02 01:00:23 UTC | #4

Thanks for all the answer. It works now! 
I never thought it was so simple.  :smiley:

@weitjong I haven't tried profiler class, but terima kasih buat tipsnya!  :smiley:

-------------------------

cirosantilli | 2017-12-10 00:12:34 UTC | #5

I can't find the FPS information on the current Profiler :frowning: lots of data! But the data it shows looks pretty cool.

-------------------------

weitjong | 2017-12-10 01:18:41 UTC | #6

It is the "Cnt" at the outer block.

-------------------------

