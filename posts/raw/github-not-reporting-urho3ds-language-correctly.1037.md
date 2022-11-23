GoogleBot42 | 2017-01-02 01:04:58 UTC | #1

Github reports Urho3D's main language as "C".  This is obviously do to the third party code that it uses.  Of course this is something that won't be changing but apparently there are some ways to make github skip the third party code.  This might mean renaming some directories which it not the best solution because that could add even more confusion over the Urho3D build process.  Although it seems that a .gitattributes file can be added which lets github know what code is third party.
[url]https://github.com/github/linguist[/url]

Changing this is particularly useful because it may make scans such as this one [url]http://discourse.urho3d.io/t/coverity-scan/1018/1[/url] more accurate if it iteracts directly with github.

What do you guys think?  :slight_smile:

-------------------------

weitjong | 2017-01-02 01:04:59 UTC | #2

Thanks for pointing this out. The .gitattributes file has been added into our master branch to correct the language breakdown. I don't think, however, that it will influence coverity scan result in any way.

-------------------------

GoogleBot42 | 2017-01-02 01:04:59 UTC | #3

[quote="weitjong"]Thanks for pointing this out. The .gitattributes file has been added into our master branch to correct the language breakdown.[/quote]
Nice!  It works!  Urho3D now reports as mainly C++.  :smiley: 

[quote="weitjong"]I don't think, however, that it will influence coverity scan result in any way.[/quote]
 :frowning:  Oh well...

-------------------------

