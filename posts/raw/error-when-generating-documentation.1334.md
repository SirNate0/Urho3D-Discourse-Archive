theak472009 | 2017-01-02 01:06:55 UTC | #1

Hello,
I am trying to build the docs for Urho3D on Windows and I get an error saying it failed to run hhc on index.hhp. The path is correctly configured in the doxyfile.

This is the error I get. Also I have no idea why it doesn't include a slash after the folder names
[spoiler]1>  sh: C:ProgramFilesHTMLHelpWorkshophhc.exe: command not found
1>CUSTOMBUILD : error : failed to run html help compiler on index.hhp[/spoiler]

Any idea how to fix this?

Thanks.

-------------------------

rasteron | 2017-01-02 01:06:55 UTC | #2

Generating docs seems to be working. Can you post your build process?

I'm using MinGW btw and after I created engine binaries..

[code]cd Docs
cmake -G "MinGW Makefiles" ./
mingw32-make doc
[/code]

[img]http://i.imgur.com/H7KXtnG.png[/img]

-------------------------

bvanevery | 2017-01-02 01:07:03 UTC | #3

I am also getting warnings and a fatal error trying to generate documentation.  Using Visual Studio 2015 Community Edition 64-bit, on Windows 7 64-bit.  Doxygen 1.8.10, GraphViz 2.38.  CMake 3.3.1.
[code]
3>CUSTOMBUILD : warning : Tag `SYMBOL_CACHE_SIZE' at line 346 of file `Doxyfile' has become obsolete.
3>           To avoid this warning please remove this line from your configuration file or upgrade it using "doxygen -u"
3>CUSTOMBUILD : warning : Tag `XML_SCHEMA' at line 1412 of file `Doxyfile' has become obsolete.
3>           To avoid this warning please remove this line from your configuration file or upgrade it using "doxygen -u"
3>CUSTOMBUILD : warning : Tag `XML_DTD' at line 1418 of file `Doxyfile' has become obsolete.
3>           To avoid this warning please remove this line from your configuration file or upgrade it using "doxygen -u"
3>CUSTOMBUILD : warning : doxygen no longer ships with the FreeSans font.
3>  You may want to clear or change DOT_FONTNAME.
3>  Otherwise you run the risk that the wrong font is being used for dot generated graphs.
3>CUSTOMBUILD : warning : the dot tool could not be found at C:/ProgramFiles(x86)/Graphviz2.38/bin
3>CUSTOMBUILD : warning : the mscgen tool could not be found at C:/ProgramFiles(x86)/Graphviz2.38/bin
3>  C:/Users/BVANEVRY/devel/Urho3D/Docs/Reference.dox:3036: warning: multiple use of section label 'FileFormats_Shader' while adding section, (first occurrence: C:/Users/BVANEVRY/devel/Urho3D/Docs/Reference.dox, line 3011)
3>CUSTOMBUILD : warning : Call graph for 'Urho3D::Connection::ProcessExistingNode' not generated, too many nodes. Consider increasing DOT_GRAPH_MAX_NODES.
3>CUSTOMBUILD : error : failed to run html help compiler on index.hhp
[/code]

dot.exe does exist at the path expected.  However I'm noticing that path is spelled "ProgramFiles(x86)" in the error and it should be "Program Files (x86)".

No tool named mscgen appears in that directory.  Maybe Graphviz 2.38 doesn't have such a thing.  And like before, the directory is misspelled.

Doxyfile has "HHC_LOCATION=C:\Program Files\HTML Help Workshop\hhc.exe".  No such directory or tool exists.  I tried downloading Microsoft HTML Help and installing it just now.  It said I already had a newer version installed.  That one seems to live at "C:\Program Files (x86)\HTML Help Workshop".  Note the (x86).  That could indicate something is fouling the path to locate html help on Windows.

I am thinking, perhaps I have some missing components, and one of the CMakeLists.txt could do more to detect them?  For instance, CMake never said anything about graphviz, but some earlier errors prompted me to add it.

My CMakeCache.txt has the correct dot.exe path in it.  
[code]//Graphviz Dot tool for using Doxygen
DOXYGEN_DOT_EXECUTABLE:FILEPATH=C:/Program Files (x86)/Graphviz2.38/bin/dot.exe[/code]
This makes me think that CMake is finding doxygen and graphviz correctly, but the information may not be being used correctly farther down the pipeline.  I do not see anything in CMake's FindDoxygen.cmake module about looking for mscgen, so I have no idea why Doxygen would think it would live in the graphviz directory.  Maybe it is a naive default, but it smells like an error.

-------------------------

weitjong | 2017-01-02 01:07:04 UTC | #4

I think I have said before in other thread. That's what you get when a Linux guy is doing a Windows work. Deep down (see my signature below), we have a hidden agenda to make all windows broken. But seriously now, I think it is a bug then when it is not working. If I recall correctly I could not verify the changes for hhc and mscgen because I don't have them preinstalled on my Windows 7 and I don't want to install the any extra tools from any 3rd party sources that I could not verify into my system. If you can make it work then please help to contribute back your changes. Thanks.

-------------------------

rasteron | 2017-01-02 01:07:05 UTC | #5

[b]@bvanevery[/b]

I think I know now your current issue here and I somehow replicated that problem and did a workaround. The generated files that I posted before was incomplete but I think I have managed to update it by setting up the path using environment variables. Just add another path pointing to your graphviz bin folder and your good to go:

[img]http://i.imgur.com/s65KUJq.jpg[/img]

[img]http://i.imgur.com/ZDA2F4V.jpg[/img]

Generated files inside the html folder is now ~500mb in size and ~30k items. 

The lack of space on that make/cmake path needs to be addressed though.

Hope this helps.

-------------------------

bvanevery | 2017-01-02 01:07:05 UTC | #6

Graphviz was already in my system path, so that alone is not the magic.  Historically, a problem with CMake project generation for Visual Studio is the latter does [b]not[/b] execute scripts in a command line environment.  Things like Graphviz needed to be obtained explicitly, you couldn't just expect them to show up in a PATH.  I don't know about CMake or Visual Studio nowadays though.

Sometimes starting CMake from a command line could also result in different behavior from just starting it from, say, the Start Menu, as I don't think an environment is automatically available.  However it's been awhile since I've dealt with that level of CMake gore on Windows.  Nevermind differences again for MinGW or Cygwin.  Tried from command line, made no difference.

My current workaround is I downloaded an already built copy of the docs.

Installing mscgen, more stuff seems to get done.  I do seem to have docs at build\Urho3D\docs\html  However there is still
[code]1>CUSTOMBUILD : error : failed to run html help compiler on index.hhp[/code]
and other warnings.  I wonder if some of them are dumb warnings that don't actually mean anything.  Weird.

-------------------------

weitjong | 2017-01-02 01:07:05 UTC | #7

The doxygen path is not hardcoded (see here [urho3d.github.io/documentation/H ... lding_Docs](http://urho3d.github.io/documentation/HEAD/_building.html#Building_Docs)).

To further troubleshoot your document generation problem on Windows host, you may wan to check these lines in the Doxyfile.in.
[github.com/urho3d/Urho3D/blob/m ... e.in#L1029](https://github.com/urho3d/Urho3D/blob/master/Docs/Doxyfile.in#L1029)
[github.com/urho3d/Urho3D/blob/m ... e.in#L1596](https://github.com/urho3d/Urho3D/blob/master/Docs/Doxyfile.in#L1596)
[github.com/urho3d/Urho3D/blob/m ... e.in#L1740](https://github.com/urho3d/Urho3D/blob/master/Docs/Doxyfile.in#L1740)
Especially the first one which has a hard-coded reference to where the hhc.exe. As I have explained before, when these entries were made, the testing was only done thoroughly on Linux host for Eclipse IDE's help (the one being used by its tester, me). Those entries were not filled previously, i.e. we didn't generate help files for specific IDE previously. It looks like the path should be "C:\Program Files (x86)\HTML Help Workshop" as you pointed out earlier. Not sure. You have to test that out yourself whether it works by making the change to the Doxyfile.in file. This is as explicit as I would like to go now to help you.

Beware that the generated online documentation and those that shipped by our binary packages are all generated using Linux host CI servers. It uses OpenGL as its graphics backend instead of Direct3D9 or Direct3D11. So, that documentation probably is sub-optimal to you.

EDIT: I made a mistake in my last statement. I totally forgot that we do have MinGW CI build with D3D9! So, if you use the doc generated from that build then you should be good.

-------------------------

bvanevery | 2017-01-02 01:07:06 UTC | #8

Thanks for the input!  The CMake configuration for some of these things is nominally incorrect.  For instance, detecting Doxygen shouldn't be QUIET when the user has explicitly checked that they want docs generated via URHO3D_DOCS.  

The standard CMake module for detecting Doxygen will detect dot.exe in a Graphviz directory, although I haven't tested how good it is at figuring out a Graphviz directory with a version number in it, i.e. C:\Program Files (x86)\Graphviz2.38\bin\dot.exe .  I remember it having a wildcard in there though.  Anyways, that would be an upstream CMake problem if there is one.

There is no standard CMake module for detecting mscgen and it would be wise to have some CMake code for this.  My docs build failed because I hadn't installed mscgen, and with all the other warnings and an error generated, that was not obviously the problem.  For instance, the last error before death was regarding hhc.  I think this gets back to the decision to do all this stuff QUIET when the user has explicitly requested to build the docs.

Also in Doxyfile.in, choosing the Graphviz directory as the default to look for mscgen, isn't reasonable for the mscgen I just downloaded.  It has its own directory, C:\Program Files (x86)\Mscgen .  I don't know where any previous release was kept or whether it was bundled with other things like Graphviz or Doxygen.  In CMake that would ideally be a Find* with several different paths listed to try.  Maybe someone somewhere already has a good modern FindMscgen.cmake module that could be borrowed.

Hardwiring hhc as "C:\Program Files (x86)\HTML Help Workshop" would work on most systems nowadays, but strictly speaking, old systems don't have the " (x86)" convention.  Hopefully such systems are too old to be real world problems now.  Microsoft does tend to ship most of their developer stuff in the " (x86)" directory; for instance, their SDKs.  I am seeing that CMake does ship with a FindHTMLHelp.cmake module; haven't looked at whether Urho3D uses it, or if the module is bug free.

As new users must have accurate docs for the system they're actually working on, it would be best from an adoption standpoint, if the doc build actually works within their installed IDE, and doesn't require installing a mingw environment just to get docs.  I think most people don't have my level of erstwhile CMake expertise and wouldn't be at all willing to track this stuff down.  They might ask here, but likely they'd give up.  Shipping prebuilt docs that do include D3D11 stuff would also be a solution, so long as they are easily found.  I haven't actually looked at those docs I downloaded yet to see what they have in them, to verify that D3D9 and D3D11 are not there, as you say.  Typically my 1st interaction with any potential 3d engine is "does it build?"

Found another problem, hearkening back to that "doc generation pollutes the source tree" bug I filed.  I don't think there's any explicitly correct CMake logic for what doc building depends on.  I tried creating a clean new set of Visual Studio .sln files and then building only the docs.  It should have done what it could, or have told me what it couldn't do and what I needed to do, but instead I got:
[code]1>------ Build started: Project: doc, Configuration: Release x64 ------
1>  Building Custom Rule C:/Users/BVANEVRY/devel/Urho3D/Docs/CMakeLists.txt
1>  CMake does not need to re-run because C:\Users\BVANEVRY\devel\build\Urho3Ddoc\Docs\CMakeFiles\generate.stamp is up-to-date.
1>  Dumping AngelScript API to ScriptAPI.dox
1>  'C:\Users\BVANEVRY\devel\build\Urho3Ddoc\bin\tool\ScriptCompiler' is not recognized as an internal or external command,
1>  operable program or batch file.
1>C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(171,5): error MSB6006: "cmd.exe" exited with code 9009.
========== Build: 0 succeeded, 1 failed, 0 up-to-date, 0 skipped ==========[/code]
If I build the entire solution, code, docs, and all though, I do get lots of doc stuff generated in build\Urho3D\docs\html .

-------------------------

weitjong | 2017-01-02 01:07:06 UTC | #9

I agree with all your points. There are for sure still rooms for improvement in our build system, especially on Windows side as it is not being continuously tested by our CI build. It is not everyday we have Windows/CMake savvy user joins our community. Please help us fix it or make it better.

-------------------------

weitjong | 2017-01-02 01:07:07 UTC | #10

Since I need to fix the documentation build to make it support spaces in the source tree, I have incorporated most of the points you have made with a little adjustment. The mscgen is not being setup now. As for your last issue, I cannot reproduce it using Makefile project file. Even in a newly configured project, the dependency on the 'doc' target should instructs 'make' to build all its dependencies correctly.

doc -> ScriptAPI.dox -> Urho3D & ScriptCompiler

So, 'make doc' alone would force the 'Urho3D' and 'ScripCompiler' targets to be built first. If you indeed having this dependency problem then perhaps you should file a bug report to either VS or CMake (in case the bug is in CMake/VS generator).

As before I have not tested any of the changes on the Windows host. So, please help to test it.

-------------------------

bvanevery | 2017-01-02 01:07:26 UTC | #11

Sorry, had some serious car trouble around when you posted, and GMail de-prioritized the forum notifications.  Both have been fixed.

In VS 2015 if I select "Project only... build only doc" before anything else is built, it fails because build\Urho3D\bin\tool\ScriptCompiler doesn't exist yet.  So that dependency issue remains.  I will consider delving into that after I get something more important working in Urho3D.  My current interest is dynamic lighting.  Meanwhile I've filed a bug so it's not forgotten.

When I build the entire solution including the docs, I get lots of "dot" errors.  Many "dot" status messages are issued where it seems to be doing productive work, but then followed by large sections where it just barfs.  Example:
[code]3>  Running dot for graph 515/957
3>  Running dot for graph 516/957
3>  Running dot for graph 517/957
3>  Running dot for graph 518/957
3>  Running dot for graph 519/957
3>  Running dot for graph 520/957
3>  Running dot for graph 521/957
3>  Running dot for graph 522/957
3>  Running dot for graph 523/957
3>  Running dot for graph 524/957
3>  Running dot for graph 525/957
3>  Running dot for graph 526/957
3>  Running dot for graph 527/957
3>  Running dot for graph 528/957
3>  Running dot for graph 529/957
3>  Running dot for graph 530/957
3>  Running dot for graph 531/957
3>  Running dot for graph 532/957
3>  Running dot for graph 533/957
3>  Running dot for graph 534/957
3>  Running dot for graph 535/957
3>  Running dot for graph 536/957
3>  Running dot for graph 537/957
3>  Running dot for graph 538/957
3>  Running dot for graph 539/957
3>  Running dot for graph 540/957
3>  Running dot for graph 541/957
3>  Running dot for graph 542/957
3>  Running dot for graph 543/957
3>  Running dot for graph 544/957
3>  Running dot for graph 545/957
3>  Running dot for graph 546/957
3>  Running dot for graph 547/957
3>  Running dot for graph 548/957
3>  Running dot for graph 549/957
3>  Running dot for graph 550/957
3>  Running dot for graph 551/957
3>  Running dot for graph 552/957
3>  Running dot for graph 553/957
3>  Running dot for graph 554/957
3>  Running dot for graph 555/957
3>  Running dot for graph 556/957
3>  Running dot for graph 557/957
3>  Running dot for graph 558/957
3>  Running dot for graph 559/957
3>  Running dot for graph 560/957
3>  Running dot for graph 561/957
3>  Running dot for graph 562/957
3>  Running dot for graph 563/957
3>  Running dot for graph 564/957
3>  Running dot for graph 565/957
3>  Running dot for graph 566/957
3>  Running dot for graph 567/957
3>  Running dot for graph 568/957
3>  Running dot for graph 569/957
3>  Running dot for graph 570/957
3>  Running dot for graph 571/957
3>  Running dot for graph 572/957
3>  Running dot for graph 573/957
3>  Running dot for graph 574/957
3>  Running dot for graph 575/957
3>  Running dot for graph 576/957
3>  Running dot for graph 577/957
3>  Running dot for graph 578/957
3>  Running dot for graph 579/957
3>  Running dot for graph 580/957
3>  Running dot for graph 581/957
3>  Running dot for graph 582/957
3>  Running dot for graph 583/957
3>  Running dot for graph 584/957
3>  Running dot for graph 585/957
3>  Running dot for graph 586/957
3>  Running dot for graph 587/957
3>  Running dot for graph 588/957
3>  Running dot for graph 589/957
3>  Running dot for graph 590/957
3>  Running dot for graph 591/957
3>  Running dot for graph 592/957
3>  Running dot for graph 593/957
3>  Running dot for graph 594/957
3>  Running dot for graph 595/957
3>  Running dot for graph 596/957
3>  Running dot for graph 597/957
3>  Running dot for graph 598/957
3>  Running dot for graph 599/957
3>  Running dot for graph 600/957
3>  Running dot for graph 601/957
3>  Running dot for graph 602/957
3>  Running dot for graph 603/957
3>  Running dot for graph 604/957
3>  Running dot for graph 605/957
3>  Running dot for graph 606/957
3>  Running dot for graph 607/957
3>  Running dot for graph 608/957
3>  Running dot for graph 609/957
3>  Running dot for graph 610/957
3>  Running dot for graph 611/957
3>  Running dot for graph 612/957
3>  Running dot for graph 613/957
3>  Running dot for graph 614/957
3>  Running dot for graph 615/957
3>  Running dot for graph 616/957
3>  Running dot for graph 617/957
3>  Running dot for graph 618/957
3>  Running dot for graph 619/957
3>  Running dot for graph 620/957
3>  Running dot for graph 621/957
3>  Running dot for graph 622/957
3>  Running dot for graph 623/957
3>  Running dot for graph 624/957
3>  Running dot for graph 625/957
3>  Running dot for graph 626/957
3>  Running dot for graph 627/957
3>  Running dot for graph 628/957
3>  Running dot for graph 629/957
3>  Running dot for graph 630/957
3>  Running dot for graph 631/957
3>  Running dot for graph 632/957
3>  Running dot for graph 633/957
3>  Running dot for graph 634/957
3>  Running dot for graph 635/957
3>  Running dot for graph 636/957
3>  Running dot for graph 637/957
3>  Running dot for graph 638/957
3>  Running dot for graph 639/957
3>  Running dot for graph 640/957
3>  Running dot for graph 641/957
3>  Running dot for graph 642/957
3>  Running dot for graph 643/957
3>  Running dot for graph 644/957
3>  Running dot for graph 645/957
3>  Running dot for graph 646/957
3>  Running dot for graph 647/957
3>  Running dot for graph 648/957
3>  Running dot for graph 649/957
3>  Running dot for graph 650/957
3>  Running dot for graph 651/957
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/struct_urho3_d_1_1_spriter_1_1_timeline_key__inherit__graph.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/struct_urho3_d_1_1_spriter_1_1_timeline_key__inherit__graph.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/struct_urho3_d_1_1_spriter_1_1_timeline_key__coll__graph.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/struct_urho3_d_1_1_spriter_1_1_timeline_key__coll__graph.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/graph_legend.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/graph_legend.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_b699b372bb605cdb8f888c3e34c55d43_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_b699b372bb605cdb8f888c3e34c55d43_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_05a93b0d590069529c9abbb2618b5314_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_05a93b0d590069529c9abbb2618b5314_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_b026fe03c823aa087622e4b3f5dcaf56_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_b026fe03c823aa087622e4b3f5dcaf56_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_2d49b02b069843969c3bd42257a6be0b_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_2d49b02b069843969c3bd42257a6be0b_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_72391119ae765017691725943a2be174_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_72391119ae765017691725943a2be174_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_b26daf59e986bd6bef100c69b6a66013_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_b26daf59e986bd6bef100c69b6a66013_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_a2c6f5d7b85d0cbaef28c13a9ed20e7e_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_a2c6f5d7b85d0cbaef28c13a9ed20e7e_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_b4d38ab8f82c0986d3c3cd0671c2d5e4_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_b4d38ab8f82c0986d3c3cd0671c2d5e4_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_03ce35b83061964b44d2890d4006219c_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_03ce35b83061964b44d2890d4006219c_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_ead020982771029195c1fb87f9c9aedf_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_ead020982771029195c1fb87f9c9aedf_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_a6fdf3b6d55867cc96a4933dcf7d26ad_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_a6fdf3b6d55867cc96a4933dcf7d26ad_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_9996dc4c638583205b1b54a32312e7c0_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_9996dc4c638583205b1b54a32312e7c0_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_c216154b89254b27ede7a5d19b2a3e24_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_c216154b89254b27ede7a5d19b2a3e24_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_571c3e3214e26be586fb16597065e3bd_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_571c3e3214e26be586fb16597065e3bd_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_0b8401b8dc2cd5c9dc3d99fabe063dea_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_0b8401b8dc2cd5c9dc3d99fabe063dea_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_4edeaea50fe93a7e911039e3e4232927_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_4edeaea50fe93a7e911039e3e4232927_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_28cc4b34cbfda88cf8a53154daca3084_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_28cc4b34cbfda88cf8a53154daca3084_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_7cc51c4a4cac7725d53127195384b49a_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_7cc51c4a4cac7725d53127195384b49a_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_af974a64c4bc25cda6649bbf563587a6_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_af974a64c4bc25cda6649bbf563587a6_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_59b35fdd3ee2b5924e95e8a23dd4e683_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_59b35fdd3ee2b5924e95e8a23dd4e683_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_67c414cc200fa99a3940fbf10515a41d_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_67c414cc200fa99a3940fbf10515a41d_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_aa8ef9e5b7a4abc67c852e1face73ece_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_aa8ef9e5b7a4abc67c852e1face73ece_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_99a52efcd07c715d77cd2718395b8285_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_99a52efcd07c715d77cd2718395b8285_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_3c3167ba88debea9485b94cde5ab455b_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_3c3167ba88debea9485b94cde5ab455b_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_70b43e9811a1f0624141fa6b3306995e_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_70b43e9811a1f0624141fa6b3306995e_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_582ed0a52e40fbc08c918a799744eb20_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_582ed0a52e40fbc08c918a799744eb20_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_8ceffd4ee35c3518d4e8bdc7e638efe8_dep.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/dir_8ceffd4ee35c3518d4e8bdc7e638efe8_dep.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_1.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_1.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_0.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_0.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_2.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_2.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_3.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_3.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_4.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_4.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_5.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_5.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_6.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_6.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_7.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_7.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_8.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_8.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_9.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_9.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_10.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_10.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_11.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_11.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_12.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_12.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_13.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_13.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_14.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_14.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_15.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_15.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_17.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_17.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_18.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_18.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_16.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_16.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_19.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_19.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_20.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_20.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_21.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_21.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_24.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_24.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_23.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_23.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_22.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_22.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_25.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_25.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_26.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_26.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_27.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_27.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_28.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_28.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_29.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_29.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_30.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_30.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_31.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_31.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_33.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_33.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_32.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_32.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_34.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_34.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_35.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_35.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_36.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_36.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_37.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_37.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_38.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_38.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_39.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_39.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_40.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_40.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_41.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_41.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_42.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_42.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_43.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_43.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_44.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_44.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_45.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_45.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_46.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_46.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_47.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_47.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_49.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_49.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_48.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_48.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_50.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_50.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_52.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_52.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_51.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_51.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_53.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_53.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_54.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_54.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_55.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_55.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_56.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_56.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_57.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_57.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_58.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_58.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_59.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_59.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_60.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_60.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_61.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_61.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_62.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_62.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_63.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_63.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_64.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_64.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_65.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_65.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_66.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_66.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_67.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_67.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_69.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_69.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_68.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_68.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_70.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_70.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_71.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_71.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_72.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_72.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_73.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_73.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_74.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_74.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_75.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_75.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_76.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_76.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_77.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_77.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_78.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_78.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_79.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_79.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_80.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_80.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_81.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_81.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_82.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_82.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_83.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_83.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_84.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_84.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_85.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_85.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_86.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_86.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_87.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_87.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_88.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_88.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_89.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_89.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_90.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_90.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_91.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_91.png"'
3>CUSTOMBUILD : error : Problems running dot: exit code=-1, command='dot', arguments='"C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_92.dot" -Tpng -o "C:/Users/bvanevery/devel/build/Urho3D/Docs/html/inherit_graph_92.png"'
[/code]

Looking in the CMake Advanced variables, I've got DOXYGEN_DOT_EXECUTABLE-NOTFOUND.  Doxygen doesn't ship with dot nowadays.  Dot is being tested for, that's good, but the result isn't being used informatively.  CMake users should find out about this sort of thing earlier somehow, it shouldn't get this late in the configuration, generation, and building.  Especially since the output looks like it works for 150 lines.  I will be filing an appropriate bug on that, once I figure out if it has to do with doc stuff being made QUIET.  Probably what should happen, is during CMake configuration it should say, "You probably need to install Graphviz".

-------------------------

bvanevery | 2017-01-02 01:07:28 UTC | #12

I've now filed all the bugs that came up in this thread, and a couple more I found along the way.  Some are simple, others are head scratchers.  I can't promise I'll come up with patches for them.  I need to move on with actually getting 3d graphics done with Urho3D, to prove viability, rather than worrying about docs and CMake builds.  But at least they are filed, and some of them reproduced by other devs.  Hopefully in time they'll get ironed out.

-------------------------

