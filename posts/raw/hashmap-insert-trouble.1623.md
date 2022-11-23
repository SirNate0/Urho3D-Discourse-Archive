ToxikCoder | 2017-01-02 01:09:02 UTC | #1

Hello,
I have a code 
[code]
HashMap<int, WString> rus;
rus.Insert(Pair<int, WString>(LocalStringIndex::mainMenuStartButtonText, WString("??????")));
[/code]
VS13 tells me, that code triggers breakpoint,  I can't understand why. It worked well with String.
Can you help me?
P.S. LocalStringIndex is enumeration

-------------------------

thebluefish | 2017-01-02 01:09:02 UTC | #2

I've had issues like that in the past specific to VS2013. [url=https://msdn.microsoft.com/en-us/library/ft4yk3a3(v=vs.90).aspx]Deleting all breakpoints[/url] should do the trick.

-------------------------

ToxikCoder | 2017-01-02 01:09:02 UTC | #3

[quote="thebluefish"]I've had issues like that in the past specific to VS2013. [url=https://msdn.microsoft.com/en-us/library/ft4yk3a3(v=vs.90).aspx]Deleting all breakpoints[/url] should do the trick.[/quote]
Didn't checked this. Actually, th whole problem was being unable to set russian text to Text, using code
[code]HashMap<int, WString> rus;
rus.Insert(Pair<int, WString>(LocalStringIndex::mainMenuStartButtonText, WString("??????")));
[/code]
I fixed it by changing code to 
[code]
HashMap<int, String> rus;
rus.Insert(Pair<int, String>(LocalStringIndex::mainMenuStartButtonText, String(L"??????")));
[/code]
But thanks for help anyway:)

-------------------------

