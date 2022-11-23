Sir_Nate | 2017-01-02 01:09:22 UTC | #1

It seems that SDL does not generate a TextInput event when return is pressed (i.e. the character '\n' or '\r' does not seem to be added to the TextInput string). It also seems not to send one when you press control+[a letter], though it does for Ctrl+[a number/symbol]. I thought I'd let you guys know, as I don't think it is actually documented anywhere, but it becomes relevant with multi-line text editors.

I don't think I'd call it a bug, especially since the user could just send their own TextInput event when return is pressed, but it can be important to be aware of it.

-------------------------

