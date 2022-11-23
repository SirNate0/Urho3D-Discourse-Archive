Jillinger | 2017-04-01 02:11:42 UTC | #1

Hi
I was just looking over the docs, and on the "Editor Instructions" page, it says this:

`Hint: to get more content to look at, run the Physics sample application (bin/Data/Scripts/11_Physics.as), and press F5. This saves a scene file called Physics.xml into the Data/Scenes subdirectory, which can be loaded in the editor.` 

I followed those instructions (except I used the entire path of the Scripts directory) and nothing happened. At least there are no new .xml files in the Scenes folder. Can someone help me convert the examples to scenes please. Thanks.

Edit
...or did the instructions mean - run the script from the editor, not the Urho3D Player from the command line?
When I run script from the editor, I get all errors.

-------------------------

Mike | 2017-04-02 23:24:19 UTC | #2

When running the sample in the Player, after pressing F5 press F1 to check where the scene has been saved.

-------------------------

Jillinger | 2017-04-02 13:28:35 UTC | #3

Hey Mike.
Thanks for the response.
Only, I don't think any file was saved. At least not an .xml.

I did a search on my pc for the HelloGUI.xml file, and there was none.
I also uses a file system watcher when I pressed F5, and the only file that was created was a log file '02_HelloGUI.as.log' in the location 'C:\...\Roaming\urho3d\logs'. 

I pressed F1 after F5, and the console opened with the word FileSystem, and a prompt. So I took a try and typed in a loacation, and hit enter. It responded by giving me a message in red - 'C:\Urho3D\Urho3D-1.6\bin\Data\Scenes' is not recognized as an internal or external command, operatable program or batch file. So I figure that the prompt is for a command, not a location.

I think I followed the instructions correctly so far. Or did I miss something?

-------------------------

Modanung | 2017-04-02 23:24:19 UTC | #4

This is what I see:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/f974d5cc7fa8947d3ffd68adddd8422c5bac1bdd.jpg" width="652" height="499">

Not every sample supports scene saving, HelloGUI doesn't. The call to scene saving is built into the MoveCamera function of the Physics sample.

-------------------------

Jillinger | 2017-04-02 22:55:08 UTC | #5

You're right Modanung. I got that too.
I was sure I read _somewhere_ where someone said you can test the examples in the editor.
I probably inserted the word _'all'_ in my brain, if it wasn't mentioned. :grinning:
Thank you.

-------------------------

