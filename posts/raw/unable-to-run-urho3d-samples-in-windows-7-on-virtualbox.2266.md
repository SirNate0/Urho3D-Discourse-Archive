djmig | 2017-01-02 01:14:23 UTC | #1

Hi,
Been trying to run samples from Urho3D-1.6-Windows-STATIC-3D11, which was downloaded from SourceForge, with no success.
I am running Windows 7 32-bit (with Direct3D11 enabled) on top of VitualBox hosted on Mac.
Below is a screenshot of error log and Direct3D status on dxdiag.

[img]https://i.imgsafe.org/706e2e4a0e.png[/img]

Your help to resolve this problem is very much appreciated.

Regards,
Don.

-------------------------

jmiller | 2017-01-02 01:14:23 UTC | #2

Only to shed some light,
[url=https://msdn.microsoft.com/en-us/library/windows/desktop/bb509553(v=vs.85).aspx]DXGI_ERROR_UNSUPPORTED = 0x887A0004[/url]
"The requested functionality is not supported by the device or the driver."

-------------------------

djmig | 2017-01-02 01:14:24 UTC | #3

Thank you carnalis. Yes, somehow Direct3D11 was not supported. I was able to run examples in Urho3D-1.6-Windows-STATIC.
Is Urho3D-1.6-Windows-STATIC compiled with OpenGL support?

Thank you again for the pointer,
Don.

-------------------------

jmiller | 2017-01-02 01:14:24 UTC | #4

I am not sure if that version is for GL... Maybe it corresponds to one here?
[urho3d.github.io/latest-news.html](https://urho3d.github.io/latest-news.html)

Apologies if I miss something; I usually [url=https://urho3d.github.io/documentation/HEAD/_building.html]build from source[/url].

-------------------------

djmig | 2017-01-02 01:14:25 UTC | #5

Yes, those Windows binaries corresponds to [urho3d.github.io/latest-news.html](https://urho3d.github.io/latest-news.html)
Later I may build Urho3d from source for the hosted Windows 7, as I did for the Mac. I was testing out the possibilities of developing a smallish game for Windows within VirtualBox.

Thanks again for your help.
Don.

-------------------------

