Lumak | 2017-01-02 01:09:47 UTC | #1

I'm not sure if VPS is something that most developers setup, but I repeated this setup again today for the second time in months and forgotten what steps I took to do it, so I thought I can share this.

[b]Setting it up[/b]
For starters, I use DigitalOcean's VPS service. It's cheap and you can setup multiple Droplets, which is really a nice feature.

Here's a reference video [url]https://www.youtube.com/watch?v=c8PNJfDjFQg[/url] for those not familiar with setting up VPS.  
Unlike the video, I didn't setup ZPanel but do use Putty and WinSCP.
I chose Ubuntu 14.04.3 64-bit for my Droplet.
You do need to install camke, gcc and g++ before you get started.

[b]Standalone kNet library[/b]
The kNet library found here [url]https://bitbucket.org/clb/knet/downloads[/url] is not up to date and didn't build.
I've made a few corrections [url=http://wikisend.com/download/276566/clb-knet-2441ea01b46a.zip]clb-knet-2441ea01b46a.zip[/url], and it builds HelloServer that uses port 2345 that can be tested with 16_Chat demo.

-------------------------

Lumak | 2017-01-02 01:09:48 UTC | #2

My plan was to write a master server next, but I just discovered Unity's master server API here [url]http://unity3d.com/master-server[/url].
It might be easier to adopt their strategy.

-------------------------

rasteron | 2017-01-02 01:09:50 UTC | #3

Hey Lumak, this is quite interesting. :slight_smile: You can also have a look at Torque3D's masterserver implementation. The popular version that I know of just uses PHP and already tested to be still working. The code is also short and simple enough (~300 lines of code) but there's some work to be done on the urho client side.

Here's the link of the source for reference:

[garagegames.com/community/re ... view/14857](http://www.garagegames.com/community/resources/view/14857)

-------------------------

Lumak | 2017-01-02 01:09:52 UTC | #4

Oh wow, that is really short.  Thank you for this.

I did end up writing up my own master server using kNet for the sake of writing one, even after seeing Unity and RakNet master server samples. I'll probably use what I got for now, but it's good to know that there's something that I can fall back on.

-------------------------

rasteron | 2017-01-02 01:09:52 UTC | #5

[quote="Lumak"]Oh wow, that is really short.  Thank you for this.

I did end up writing up my own master server using kNet for the sake of writing one, even after seeing Unity and RakNet master server samples. I'll probably use what I got for now, but it's good to know that there's something that I can fall back on.[/quote]

Sure thing and sounds great! :slight_smile:

-------------------------

