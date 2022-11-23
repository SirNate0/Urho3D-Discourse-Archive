ppsychrite | 2017-07-07 22:19:14 UTC | #1

Hello!
I recently have taken to httprequest .pngs.
The httprequesting part is fine and dandy but when I write the image into a .png and try to open it it complains about being unable to open it. I tried opening the file in notepad and it seems to be correct-ish (starts with "‰PNG" and has a bunch of gibberish)

Although from looking at it it does miss a few "gibberish blocks"
So I've pastebin'd the working .png I downloaded and the one wrote to file by urho3d:
Working: https://pastebin.com/VxNHKVfq
Non-Working: https://pastebin.com/ge97122J

If it helps, this is how I get the .png data

    request = network->MakeHttpRequest("www.gamefromscratch.com/image.axd?picture=logo_thumb_2.png");
    bool mtlDone = false;

    ur::String mtl;
    while (!mtlDone) {
    if (request->GetState() == ur::HTTP_INITIALIZING) continue;
    else if (request->GetState() == ur::HTTP_ERROR) objDone = true;
    else {
	while (request->GetAvailableSize() > 0) {
	mtl += request->ReadString();
	}
	if (request->GetState() == ur::HTTP_CLOSED) {
	mtlDone = true;
	}					
	}
	}

(In other questions, is there a way to set a material's texture using just a raw image instead of making a file manually and writing all .png data in it?)

-------------------------

jmiller | 2017-07-10 03:32:52 UTC | #2

Hello,

Here is some posted code for reading response data. Maybe it will help?
https://discourse.urho3d.io/t/solved-reading-response-data-from-http-request/1501/3

For the last question, the answer is 'yes'. Victor may have posted a working example here
https://discourse.urho3d.io/t/manually-setting-pixels-in-texture/370/4
but there are [url=https://discourse.urho3d.io/search?q=Texture2D%20SetData%20Image]some others posted[/url].

Hope that is some help. Let us know how it's coming along :)

-------------------------

ppsychrite | 2017-07-16 14:31:09 UTC | #3

The way he did does not seem to be working.
I'm going to be trying curlpp and see if that brings any results.
Thanks though! :)

-------------------------

