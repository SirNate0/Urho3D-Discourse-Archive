elemusic | 2017-01-02 01:10:53 UTC | #1

i don't know if there is an offline document,didn't find it

sometime i need to check the document without internet.
dont' know if there a html,chm,pdf or something which can read offline

-------------------------

1vanK | 2017-01-02 01:10:53 UTC | #2

U can enable URHO3D_DOCS in CMake

-------------------------

elemusic | 2017-01-02 01:10:53 UTC | #3

thank you,never thought it works like this.amazing :smiley:

-------------------------

hdunderscore | 2017-01-02 01:10:53 UTC | #4

If you have the right tools installed, it will generate a chm too, which I think is pretty handy.

-------------------------

weitjong | 2017-01-02 01:10:53 UTC | #5

You also don't need to use that build option unless you really want to rebuild the doc each time you build Urho3D. The 'doc' built-in target is always available, except when you don't have Doxygen installed. For example, makefile user may just simply invoke 'make doc' to get it. And also, besides CHM for VS, the doc target also supports building the documentation for other supported IDEs. Check the dev comments in the doxyfile. Finders, keepers.

-------------------------

jamies | 2020-05-13 15:13:32 UTC | #6

I wonder if I can generate a PDF or html doc that is more easily browse-able and search-able on a smartphone.

Sometimes exploring the engine doc can be made while being at the park instead of in front of a computer :)

-------------------------

weitjong | 2020-05-13 15:55:37 UTC | #7

Our main website including the online documentation uses mobile-first responsive design. You should be able to read online documentation via smart device with screen size from iPhone 4S (I used to have that model and use that as first target to check) to iPad. It even supports the Reader-View mode. However, it still lacks the site search functionality, so you probably need Google help on that. Our website pages are being indexed pretty good by Google. Use the "site:urho3d.github.io" to limit the search on our main website. For example, to search on one of the shader, try: "site:urho3d.github.io LitSolid shader". HTH.

-------------------------

jamies | 2020-05-13 16:19:10 UTC | #8

That's nice, but I'd rather have an offline doc... I guess I'll try saving the pages I'm interested in. I was also wondering about finding a way to print the doc, in a 2 by 2 layout to save paper. That's fine, I will manage, thanks!

-------------------------

jmiller | 2020-05-13 21:05:14 UTC | #9

While not hyperlinked, I find the source reference quickly readable and searchable... ;)
  https://github.com/urho3d/Urho3D/blob/master/Docs/Reference.dox

Doxygen has various output formats (docbook, html, rtf) that could be used by changing your Urho cmake configuration.
  http://www.doxygen.nl/manual/starting.html
LaTeX > PDF and htmldoc may be known paths..
  https://stackoverflow.com/questions/374032/generate-single-file-html-code-documentation

-------------------------

Modanung | 2020-05-13 19:05:17 UTC | #10

...and ePubs are just ZIPs - with a different extension - containing a webpage.

-------------------------

