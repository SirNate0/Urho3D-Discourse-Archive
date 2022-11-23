itisscan | 2017-01-02 01:14:32 UTC | #1

I need to use base-e exponential function of x, which is e raised to the power x: e^x.
In c++ case, i will include <cmath> and will use exp(x) function. 

I have found out that there is sdk addon [url]ftp://home.oppserver.net/mirror/debian.oppserver.net/incoming/pbody_tmp/squeeze/src/xbmc-pre11.0+pvr-testing/xbmc/visualizations/Vortex/angelscript/docs/manual/doc_addon_math.html[/url] , which can register the math functions from the standard C runtime library, but how it can be done with urho3d, i have no ideas.

[b]question.[/b]
How i can bound exp() function to AS ? 

Thanks.

-------------------------

1vanK | 2017-01-02 01:14:33 UTC | #2

Pow(e, x) ?

-------------------------

itisscan | 2017-01-02 01:14:33 UTC | #3

Yes, exactly. it was so simply, that did not notice it. :slight_smile:

-------------------------

