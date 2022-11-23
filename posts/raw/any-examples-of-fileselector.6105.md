evolgames | 2020-04-20 13:27:24 UTC | #1

Hey guys, it's been a while. I hope everyone is doing well. I'm working on something cool in U3d.
Are there any examples of fileselector implementation? I haven't found any in the Samples. I have a couple questions:

1. Does FileSelector do any native file selecting, like a browser does when you do "Choose File"? Or, is it merely a way to get information on files in a directory, to which an Urho UI needs to be built around? (I'm assuming the latter)
2. How do I approach files in the GetList?

I'm assuming I get the list of files from the directory and then I will be able to perform my operations with them. In my case, it's very simple. I just am reading and writing one-line string text files. I've already implemented that, though that's a hardcoded filename. What I'm aiming for is the user goes to save/load and then they can see the contents of the folder. This could help especially if they did their own backups and the filenames were not just the game's preset slots.

So far I have the following:

```
local fsel = FileSelector:new()
fsel:SetPath(fileSystem:GetProgramDir().."Data/Scenes/")
local list = fsel:GetFileList()
```

So now I have list, which is a userdata value. I took a look here, https://urho3d.github.io/documentation/1.7/class_urho3_d_1_1_list_view.html
but I'm not sure I understand how this list works.

I could easily make a little UI with a scrollbar and display this list contents. And once I have the filename, since I'm only doing simple text file read/write, that's all I need. Just not sure how it's getting the filenames. Is there a way to get a string/table of these filenames?

I notice there are SetSelection and SetHighlight, which I assume I would use to build this interface...


EDIT: got it. The relevant code was in EditorUI.as, and it wasn't hard to track down some of the other functions. Looking at this in practice makes much more sense than the documentation. I think all examples do. It wasn't hard to translate to lua. There are a few instances that use the fileselector in the editor, like saving scenes and picking models. Lastly, the reason my above code did nothing is because the style must be set. Using the below example, if you remove everything except the first two lines in the function, it will still create a fileselector window. Otherwise, if you don't set the style nothing will show up.
Found on line 1071:
```
void CreateFileSelector(const String&in title, const String&in ok, const String&in cancel, const String&in initialPath, Array<String>@ filters,
    uint initialFilter, bool autoLocalizeTitle = true)
{
    // Within the editor UI, the file selector is a kind of a "singleton". When the previous one is overwritten, also
    // the events subscribed from it are disconnected, so new ones are safe to subscribe.
    uiFileSelector = FileSelector();
    uiFileSelector.defaultStyle = uiStyle;
    uiFileSelector.title = title;
    uiFileSelector.titleText.autoLocalizable = autoLocalizeTitle;
    uiFileSelector.path = initialPath;
    uiFileSelector.SetButtonTexts(ok, cancel);
    Text@ okText = cast<Text>(uiFileSelector.okButton.children[0]);
    okText.autoLocalizable = true;
    Text@ cancelText = cast<Text>(uiFileSelector.cancelButton.children[0]);
    cancelText.autoLocalizable = true;
    uiFileSelector.SetFilters(filters, initialFilter);
    CenterDialog(uiFileSelector.window);
}
```

-------------------------

SirNate0 | 2020-04-20 12:33:00 UTC | #2

I think the Editor uses the file selector. It's written in AngelScript, but if you understand c++ you should be able to read it easily enough.

-------------------------

evolgames | 2020-04-20 11:54:16 UTC | #3

oh man I can't believe I didn't think about that. of course the editor uses it. Thanks, I'm taking a look!

-------------------------

