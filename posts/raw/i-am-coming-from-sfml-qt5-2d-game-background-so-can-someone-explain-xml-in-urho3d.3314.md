Kishy-nivas | 2017-07-03 06:54:25 UTC | #1

I find the samples having reference to some XML files (like default.xml) .... why do we use them ? why should I use them ?  is that necessary for 2d games too ? There are plenty of XML files for models , so are they self generated ones, or we should write ourself , sorry if this is so noob question. I couldn't find any help .

-------------------------

hdunderscore | 2017-07-03 10:17:09 UTC | #2

The xml files are serialized resources, they make it easier to reuse and edit resources without re-compiling the app. You don't have to use them, everything can be done via code. For some resources, you can generate the xml's in the editor, and the ones that aren't covered such as texture settings are documented:

https://urho3d.github.io/documentation/HEAD/_materials.html
https://urho3d.github.io/documentation/HEAD/_render_paths.html

-------------------------

