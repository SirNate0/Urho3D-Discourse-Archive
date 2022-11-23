devrich | 2017-01-02 01:02:39 UTC | #1

Hi guys,

When i extracted the Urho3D linux 64-bit static on my offline pc; all the docs cam eout with no CSS stylesheet.  I can't find the doxygen file and was wondering how to re-run doxygen to get an offline copy of the documentation for this offline pc ?

-------------------------

weitjong | 2017-01-02 01:02:39 UTC | #2

I am sorry to say that you will never get the same look and feel of the documentation pages when generated using Doxygen or by running 'make doc' locally. The online documentation pages on our main website looks nicer because they are "themed" (or have custom CSS, using your own words). If you want to get similar look and feel offline then there is one way I can think of. Host the website locally. However, that alone would require a different set of software component requirement and also different skill set on your part. If you are still interested then you can have a look on this repo. [github.com/urho3d/urho3d.github.io](https://github.com/urho3d/urho3d.github.io).

I think it is much quicker just save our online pages from a PC with internet connection. No?

-------------------------

rogerdv | 2017-01-02 01:02:40 UTC | #3

The doxygen file is at Docs directory. I ahve had no troubles generating the documentaiton at home, without internet. Yes, it looks weird, and the class list doesnt list classes at all, but it works.

-------------------------

weitjong | 2017-01-02 01:02:40 UTC | #4

[quote="rogerdv"]The doxygen file is at Docs directory. I ahve had no troubles generating the documentaiton at home, without internet. Yes, it looks weird, and the class list doesnt list classes at all, but it works.[/quote]
I only agree on that the locally generated documentation looks different than the online one. But content wise, they should be the same. Both online and local doc are derived from Doxygen files which are generated from a same "doc" built-in target. You should run "make doc" or its equivalent in the IDE instead of double clicking on the *.dox files.

-------------------------

devrich | 2017-01-02 01:02:40 UTC | #5

[quote="weitjong"]I am sorry to say that you will never get the same look and feel of the documentation pages when generated using Doxygen or by running 'make doc' locally. The online documentation pages on our main website looks nicer because they are "themed" (or have custom CSS, using your own words). If you want to get similar look and feel offline then there is one way I can think of. Host the website locally. However, that alone would require a different set of software component requirement and also different skill set on your part. If you are still interested then you can have a look on this repo. [github.com/urho3d/urho3d.github.io](https://github.com/urho3d/urho3d.github.io).

I think it is much quicker just save our online pages from a PC with internet connection. No?[/quote]

I tried some of the documentation pages but then when i click on a link they try to goto the site xD

I suppose I could download all the documentation pages then write a program to change the base url of all the links to look a local path and subfolder...  atm, i have a super slow old ( ooold ) pc connected to the internet next to my offline pc ( powerhouse pc ) but sharing a monitor has been quite annoying lol  :laughing:


Thanks for the hints for re-running the doxygen guys, i'll give that a try and see if maybe there are some options there for including style sheets.  i checked the source of the offline docs and see that they are using css class=" " attributes in the html tags so maybe there is somehting in the doxygen program that could use a specific css sheet and if so then i'll post how to do it here  :slight_smile:

-------------------------

devrich | 2017-01-02 01:02:41 UTC | #6

[size=150][b][color=#0040FF]GOT IT!!![/color][/b][/size]   :nerd: 

Here's how to do it!

1: Download the source for Urho3D and extract it.  In my case iI get the directory "Urho3D-1.32"...
2: navigate to "Urho3D-1.32/Docs" and you will see a file "Doxyfile.in" -- Open this file in a text editor ( Gedit for me partially beacuse it allows you to enable displaying line numbers )
3: goto line #914 HTML_STYLESHEET =
4: Type "main-min.css" next to it ( no quotes or semi-colons or anything afterwards ) to get this:
[code]| 913 |
| 914 | HTML_STYLESHEET = main-min.css
| 915 |[/code]
** SAVE IT **

5: To make sure Doxygen can find the "main-min.css" stylesheet, we need to download it and here's how:
6-A: Goto the Urho3D "About" page: [url]http://urho3d.github.io/about.html[/url] and then save it as COMPLETE HTML... in FireFox I used "[u]F[/u]ile > Save Page [u]A[/u]s" ( note: <CTRL>+<s> works too ) and make sure that you are saving as "Webpage, Complete" which will save all the files that the webpage links to including "main-min.css
6-B: or i suppose you could just download the stylesheet directly [url]http://urho3d.github.io/main-min.css[/url]   :unamused: 
7: Be sure to copy that "main-min.css" page into the same folder as the "Doxygen.in" file --> "Urho3D-1.32/Docs"
8: open a terminal window and navigate to the directory where the Doxygen.in and the main-min.css files are "Urho3D-1.32/Docs"

9: type: 
[code]Doxygen Doxygen.in[/code]
 and when it gets done then it will generate a folder "html" right there in that "Urho3D-1.32/Docs" folder and then everything works beautifully including classes

10: Enjoy :slight_smile:

NOTE:   I looked at the main-min.css file and there are URL imports in there to import files from the web such as google and github.  I didn't look too deeply as my text editor kept getting overloaded ( cpu-wise ) by the file.  I did all of this on my offline PC after transfering the main-min.css file and the Urho3D source over there so there was no internet to connect to.  Your results may vary ( or look nicer than mine ) but still  :smiley:

Many thanks for your hints at where to look guys!

-------------------------

weitjong | 2017-01-02 01:02:41 UTC | #7

Interesting you can get it work that way. Firstly, the "Docs/Doxyfile.in" is not the correct input file for Doxygen, the generated "Docs/Doxyfile" in the build tree is. Secondly, the "main-min.css" is designed to look best on our main website which uses "Minimal" theme originally created by orderedlist ([orderedlist.com/minimal/](http://orderedlist.com/minimal/)). We will not support its usage in the manner you described. However, if the CSS works for you that way then by all mean use it  :wink: .

-------------------------

