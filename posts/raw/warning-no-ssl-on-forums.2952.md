Modanung | 2017-06-28 14:11:49 UTC | #1

https://discourse.urho3d.io is inaccessible, so every time I log in (without using Github) I get a warning. Could this be fixed?
Or is it me?

-------------------------

TheComet | 2017-03-27 17:07:06 UTC | #2

It's not just you. It says my connection is unsecured

-------------------------

hdunderscore | 2017-03-27 18:36:52 UTC | #3

I will look into it, I'm not sure what the options are for it yet.

-------------------------

rbyte | 2017-04-06 00:36:30 UTC | #4

I would like to have https as well please.

-------------------------

rasteron | 2017-04-06 10:05:06 UTC | #5

@hdunderscore Not sure if they include SSL with this sponsored plan, but maybe coordinate with the Discourse team and for a free SSL option, you can refer to this How-To post:

https://meta.discourse.org/t/setting-up-lets-encrypt/40709 

Hope that helps.

-------------------------

hdunderscore | 2017-04-27 06:50:53 UTC | #6

I've not been able to get to this sooner, but I believe the SSL is now enabled.

Thanks goes to the discourse staff -- the free hosting for the open source projects did include SSL so all that was required was to ask :)

-------------------------

rasteron | 2017-04-27 07:57:06 UTC | #7

nice! I was able to load the site with SSL but getting some mixed content, maybe change one of the logo address to `https://` or just `//` under site settings and maybe get a full display of that green lock SSL icon at least on the homepage?

I think this particular image:
http://discourse.urho3d.io/uploads/urho3d/original/1X/f0c81f2a309de88bf6196cd6179960dcbabe8d62.png

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/864d3afd34c0e8097aeada90f49510271da3a442.png" width="690" height="439">

-------------------------

rasteron | 2017-04-27 08:05:49 UTC | #8

awesome, works great now hd :)

-------------------------

hdunderscore | 2017-04-27 08:11:49 UTC | #9

If anyone has issues logging in via http://discourse.urho3d.io, try https://discourse.urho3d.io .

-------------------------

rasteron | 2017-04-27 08:25:30 UTC | #10

..also maybe do a sticky for a bit re: this change or setup a force redirect

https://meta.discourse.org/t/force-redirect-http-to-https/57393

-------------------------

weitjong | 2017-04-27 13:57:48 UTC | #11

I have updated the forum URL in the Urho3D main website to use the https protocol.

-------------------------

hdunderscore | 2017-04-28 10:28:43 UTC | #12

Just received an update from discourse staff, all traffic is now forced to https.

-------------------------

