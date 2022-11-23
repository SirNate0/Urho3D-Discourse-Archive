George1 | 2018-01-12 06:14:56 UTC | #1

Dear all,
Does anyone aware if there is such a flag to disable rendering update or 
flag to disable different update?

Thanks

-------------------------

Modanung | 2018-01-12 09:31:01 UTC | #2

`Object::SetBlockEvents()` and `Engine::SetPauseMinimized()` might meet your criteria.

-------------------------

George1 | 2018-01-12 10:39:00 UTC | #3

Is SetPauseMinimized() pause everything?

I need to have the update event (e.g. position and transformation update), but not the graphic rendering update.

Regards

-------------------------

Modanung | 2018-01-12 10:42:21 UTC | #4

Maybe `engineParameters_[EP_HEADLESS] = true;` would do the trick in your case?

-------------------------

George1 | 2018-01-12 11:43:35 UTC | #5

Not sure that's what I need. But I want to turn rendering on and off at run time.

-------------------------

lezak | 2018-01-12 13:50:56 UTC | #6

I don't think You can do that without modyfing the engine, since Render() is called directly from RunFrame().
What You can do is set number of viewports to 0, this way everything will be updated, but only clear color will be rendered.

-------------------------

Eugene | 2018-01-12 14:01:17 UTC | #7

XY problem, I guess.

-------------------------

George1 | 2018-01-12 14:08:46 UTC | #8

Thanks lezak, I have tried this method. My event update speed ( discrete event counter) looks like its still the same. 

So I'm not sure this help increase the loop speed.

-------------------------

