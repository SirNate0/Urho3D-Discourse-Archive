nattydread | 2019-10-03 13:14:55 UTC | #1

I'm trying to apply the Jack textures to the Jack models in the 13_Ragdolls demo. 
I have followed I3DB's instructions above but I cannot get any of Jacks textures to display. In fact whatever texture I have loaded for the floor gets used either on Jack's head or body. Any tips?  Am I missing something obvious?

-------------------------

Modanung | 2019-10-03 13:14:55 UTC | #2

Are there any error messages in the log about unfound resources?

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

Modanung | 2019-10-03 13:15:58 UTC | #3

Could you share the code used to apply the textures, btw?

-------------------------

nattydread | 2019-10-04 13:14:20 UTC | #4

Yes from the Ragdoll demo I add the lines at line 146:

modelObject->SetMaterial(0, cache->GetResource<Material>("Materials/JackBody.xml"));
modelObject->SetMaterial(1, cache->GetResource<Material>("Materials/JackHead.xml"));

where the xml files are identical to the ones above.

Jack assumes the stone texture from the ground plane.

Now you mention it there are ERROR messages. 
I'll see if I can resolve that.

-------------------------

nattydread | 2019-10-04 13:19:33 UTC | #5

OK Its working! I needed the Textures path in the xml files for the body parts:

name="Textures/Jack_face.jpg"

Thanks for the tip. :slight_smile:

-------------------------

nattydread | 2019-10-04 13:40:51 UTC | #6

Now its working shall we improve the 13_Ragdoll demo?

-------------------------

Modanung | 2019-10-04 15:59:20 UTC | #7

Could you share a screenshot of that?

-------------------------

nattydread | 2019-10-04 19:11:53 UTC | #8

Sure!

![Ragdolls1|672x500](upload://jhQLqRPzPOseJg8QgWUe5QSB8HS.png)

-------------------------

Modanung | 2019-10-08 09:45:50 UTC | #9

Hm, I can see why (probably) @cadaver left him untextured in the samples.

What does the community think? 

[poll type=regular results=always]
* I like Jack better with these textures
* I'd prefer leaving Jack untextured
* Opinion void
[/poll]

-------------------------

