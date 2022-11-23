alexrass | 2017-01-02 00:57:44 UTC | #1

[img]http://s18.postimg.org/aznnhia6x/Codelite_script_editor.png[/img]

Add *.as in tags and syntax highlight (c++) options:

[img]http://s18.postimg.org/e6d540obd/sh_as.png[/img]
[img]http://s18.postimg.org/n041l4ba1/sh_as2.png[/img]

Create ptoject (Custom makefile).
add AngelScriptAPI.h and *.as files to project

-------------------------

lexx | 2017-01-02 00:59:34 UTC | #2

Thanks for this.

Does anyone know can I somehow start urho3dPlayer with current .as file when pressing F5, so testing scripts would be easy?


[EDIT]
Ok, did some kind of hack and it runs urho3dplayer with CTRL+F5. Uses .as name as program argument, not active .as tab name, but maybe this is fine.

[img]http://i60.tinypic.com/6sw7pc.png[/img]

-------------------------

gasp | 2017-01-02 00:59:36 UTC | #3

You can set an external tools like that :

Menu Plugins -> External Tools

[img]http://i60.tinypic.com/2crm6mw.jpg[/img]


now set the shortcut :
Settings -> keyboard Shortcut

[img]http://i62.tinypic.com/6f8h8h.jpg[/img]

-------------------------

lexx | 2017-01-02 00:59:36 UTC | #4

Awesome, thanks!

-------------------------

Enhex | 2017-02-11 08:59:08 UTC | #5

With CodeLite 10 I couldn't find `File Types` in CTag -> advanced.
Had to open code-completion.conf and add `;*.as` to `m_fileSpec` manually.

Also need to include `Urho3D/Docs` where `AngelScriptAPI.h` is located, and don't have to add it by itself to the project.

-------------------------

lexx | 2017-06-10 03:02:48 UTC | #6

[quote="Enhex, post:5, topic:68, full:true"]
With CodeLite 10 I couldn't find `File Types` in CTag -> advanced.
Had to open code-completion.conf and add `;*.as` to `m_fileSpec` manually.
[/quote]

In CodeLite 10.0.4,  there is  Setting -> Code Completion... where one can add ;*.as

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/9a35bd098ea97ffd7b7392bdb9753781de301282.png[/img]

-------------------------

