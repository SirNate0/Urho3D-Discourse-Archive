godan | 2017-01-02 01:13:32 UTC | #1

So, this isn't directly an Urho question, but since I'm trying to figure out of I should use Urho for this project, it's kind of related....anyway....

Here's what I need to do:

- Have a fullscreen app doing something like uv painting a 3d model (I know how to do this, no issues here)
- Write the painted 3d model's texture to a file or append it to a video (appending it as a video is a little tricky)
- Say all this is happening on a laptop. I want to be able to plug in an HDMI or DVI cable and have ONLY the texture video come through as a live feed.

In other words, normally if I plugged in a HDMI cable and connected it to, say, a projector, the whole desktop screen would come through. How can I stream just the texture part? How can I say: "only this video/texture/frame buffer should be output through the hdmi cable? Tricky right? 

I would not be surprised if it's not possible. In fact, my plan B is to create a little webpage/js script that reloads the texture on disk every time I write it. Then, via localhost or whatever, someone else can see it. No cords necessary. HOWEVER, it would be "nicer" if I could do the HDMI/DVI thing. 

Any thoughts?

-------------------------

hdunderscore | 2017-01-02 01:13:33 UTC | #2

Normally when you plug in a hdmi cable, the new screen can be set up as a separate desktop ? In that case the problem is simplified.

Which OS do you run ?

-------------------------

godan | 2017-01-02 01:13:34 UTC | #3

Yes, that is absolutely true. I guess the thing is, for this particular project, we would be connecting to another computer (in this  case, the computer running a bunch of projectors via D3 - [d3technologies.com](http://www.d3technologies.com)). As it turns out, D3 knows about HDMI cables and registers itself as an external monitor with the laptop (or so I'm told). So, as you say, we can just extend the desktop, maximize the window, et voila.

However, I feel like I don't understand something about this whole setup. How does D3 register itself as an external monitor? Is the whole HDMI port thing purely at the mercy of the OS? Anyway, at this point, the question is academic, but I am still curious.

-------------------------

