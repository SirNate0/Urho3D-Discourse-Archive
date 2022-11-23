Kronix | 2018-09-23 14:49:48 UTC | #1

Edit: After switching from the C# UrhoSharp solution to the C++ master build, the implementation in question (2) is now accessible, but I have another compile problem (see my reply post below)

1) I downloaded the urho-samples-master.zip file from GitHub, extracted it to a directory, went to the FeaturedSamples directory, and opened FeatureSamples.sln.  When I try to run the WinForms Projekt, I get an error that it can't find CoreData.pak in \bin\Desktop.  This was on line 20 of SamplesForm.cs where the AssetsDirectory is set, so I'm assuming something in that folder is trying to reference the wrong path to CoreData.pak.  So I did a search and copied CoreData.pak from \packages\UrhoSharp.1.8.71\native\ into \bin\Desktop.

Tried to compile again, and I got another error that it can't find the mono-urho DLL file.  So I did a search, found 4 different mono-urho DLL files, and copied the one from \packages\UrhoSharp.1.8.71\native\Win64 into \bin\Desktop.  Compiled again and it works.

Why did I have to do this?  Why didn't it work out of the box?

2) I was trying to find more information on the Model.SetGeometry() function in the DynamicGeometry example, but I could only find the Class Definition in Model.cs and not much explanation in the online documentation.  Is there anywhere I can find the implementation code of SetGeometry() or more thorough explanations of what functions do, or do I have to ask here every time?

P.S. I'm not sure how to keep the numbered paragraphs in my post from indenting, or indent the other paragraphs that were part of number 1.

-------------------------

S.L.C | 2018-09-23 13:33:32 UTC | #2

You sure you're on the right forum? By the looks of you you're trying to use a C# variant of the engine. Which i don't recall being supported officially.

-------------------------

Kronix | 2018-09-23 14:33:59 UTC | #3

Sorry, I didn't know the DynamicGeometry sample as mentioned by lezak was also in the master C++ build.  Well, I installed the solution for the C++ version and the good news is, the implementations of the functions appear to visible (instead of hidden in DLLs).  The bad news is, I can't compile.  Here's the result:

![U3DMasterScreen1|690x388](upload://ftxPFiEpqqqucD4spPrhsJWjy70.png)

-------------------------

S.L.C | 2018-09-23 14:57:16 UTC | #4

What was the process that you've used to build the engine? I mean, walk us through the stales you took to build it.

-------------------------

Kronix | 2018-09-23 16:14:44 UTC | #5

I used the CMake GUI as described here: https://github.com/urho3d/Urho3D/wiki/Setting-up-Urho3D-on-Windows-with-Visual-Studio

I found that other people had the same problem here: https://github.com/urho3d/Urho3D/issues/2362

I just now fixed it by following lxq's post further down the problem page.  Namely, I disabled AngelScript in CMake.  Now the samples run.

But I don't know much about AngelScript.  Will I need that?

EDIT: I also got it working by modifying AngelScript\APITemplates.h as in orefkov's post further down the problem page, without disabling AngelScript.  However, the change must be made in the source folder before running CMake.

-------------------------

S.L.C | 2018-09-23 15:41:41 UTC | #6

Mostly if you plan on using the built int Editor. Otherwise, if you plan on doing everything yourself. You're likely to not depend on it.

-------------------------

