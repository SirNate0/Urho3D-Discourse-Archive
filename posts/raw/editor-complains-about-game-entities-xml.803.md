rogerdv | 2017-01-02 01:03:01 UTC | #1

I decide to place all game related content in a directory named Game in Data. Among other files, I have one named entities.xml, containing info related to game characters. Yesterday I loaded an scene to edit it and got a curious error: editor said it couldnt load Game/entities.xml. It was a sort of WTF?! for me, as I have no references to such file in the scene. So, I guess that the editor is trying to load the file for some reason unknown to me. Does anybody knows why? What is supposed to be in Game/entities.xml?

-------------------------

Mike | 2017-01-02 01:03:01 UTC | #2

The 'Resource Browser' is scanning your paths and will report files that it can't use. This is not an issue, you can safely ignore it.

-------------------------

