Lichi | 2017-01-02 01:01:40 UTC | #1

Hi, i want to add aa to my project, but i dont know who, someone help me?
Thanks. :slight_smile:

-------------------------

hdunderscore | 2017-01-02 01:01:40 UTC | #2

You could use SetMode() in Graphics ([url=http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_graphics.html#adc16c8a19af1584c902fe29e3d21d6eb]doc link[/url]) to enable MSAA, or if you want to use FXAA (or one of your own) post process you can look at the sample: 09_MultipleViewports which demonstrates both FXAA and bloom post process effects.

-------------------------

weitjong | 2017-01-02 01:01:40 UTC | #3

Are you referring to FXAA post-processing? If yes then you may want to check 09_MultipleViewports sample app. There are also a few paragraphs regarding post-processing in our documentation. This page is one of them. [urho3d.github.io/documentation/1 ... paths.html](http://urho3d.github.io/documentation/1.32/_render_paths.html)

-------------------------

