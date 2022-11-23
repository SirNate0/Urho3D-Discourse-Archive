vivienneanthony | 2017-01-02 01:15:07 UTC | #1

Hey,

Someone recommended to use PODVector to use a raw Int64. Which I will look at.

Basically, on the server I want to use long int on the server side. Send that info to a quiet. Then convert the XMLElement into something similiar to GetInt64() or GetLongInt(). The reason way, time and date can be converted to long int. In during so, I can do time+date for example plus 16 hours. Save that long int and send that to the server.

I hope that makes sense. Comparing the retrieved long int  to the time date long int. I can come up with progress time or duration.

Anybody has a quick solution to the problem. Or a quick way I can mod Urho to have that additional Get types.

Vivienne

-------------------------

Sir_Nate | 2017-01-02 01:15:09 UTC | #2

You could also cast to IntVector2, which should have 64 bits of data, and would make it easier to get the high and low 32 bits if you need to do that.

-------------------------

