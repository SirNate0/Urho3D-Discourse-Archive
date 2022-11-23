Jillinger | 2017-03-28 01:58:22 UTC | #1

Hi
I've been playing around with the editor for a while, and I am ready to do scripting on a new project. I have three queries.
1) I don't see a script button in the editor. How can I add a script, and edit it in Visual Studio? Can I use the editor in this way to start a project from scratch?

2) I was following the docs on creating a new product, but somehow my include files are missing. How can I ensure they are included when I generate a project?
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/df95d40128be8230b0a84586d8b8e8954353a1bb.jpg" width="500" height="300">

3) Can I use an main.as file instead of, or along with the main.cpp file?

Thanks

-------------------------

Jillinger | 2017-03-28 22:58:07 UTC | #2

Okay. So I found out how to add a script, which answers my number 1 question.
So I can use the editor to develop my project, only it appears, I need to use an IDE to publish.
That's not bad at all. Other than the lack of that feature, the editor in my opinion has some great advantages, like allowing me to customize it to my likings It updates in realtime superbly, and it's beautiful. :sweat_smile:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/f4e6859408ff1e8166ef2cacc57430f8a6d12a56.jpg" width="690" height="387">

It still would be nice to get questions 2 and 3 covered.

-------------------------

lezak | 2017-03-29 00:51:04 UTC | #3

As for 3. You can use player application, <a href="https://urho3d.github.io/documentation/1.6/_running.html"> here is documentation </a>, also check out scripted samples and how are they started (in "Data/CommandLine.txt place path to Your Main.as and run player). If You want to use scripting alongside C++ <a href="https://urho3d.github.io/documentation/1.6/_scripting.html"> check this page </a> for some instructions.

-------------------------

Jillinger | 2017-03-29 01:57:39 UTC | #4

[quote="lezak, post:3, topic:2960"]
As for 3. You can use player application,  here is documentation , also check out scripted samples and how are they started (in "Data/CommandLine.txt place path to Your Main.as and run player)
[/quote]

Thanks lezak.
Now I just need to get number 2, and I can use this.:smile: Thanks

-------------------------

Jillinger | 2017-03-29 20:37:49 UTC | #5

Alright! Number 2 is covered.
It seems cmakeLists was missing this piece of code:

    # Find Urho3D library
    find_package (Urho3D)
    include_directories (${URHO3D_INCLUDE_DIRS})

Done.:smiley:

-------------------------

