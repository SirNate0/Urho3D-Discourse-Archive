miz | 2017-01-02 01:15:19 UTC | #1

I set a UIElement as the content element of a ScrollView and then add children to that content element. Only one of these children (the one added first placed highest vertically) responds to clicks (i.e. OnClickBegin is called) for the ones vertically below the clicked UIElement is always the SV_ScrollPanel from the ScrollView.  So I assume that the GetElementAt() function in UI isn't quite returning the desired element.  Setting higher priorities doesn't seem to help.

Has anyone had a similar issue? Is there a way to force a UIElement to be picked up by GetElementAt provided the mouse click is in the right place?

Thanks :slight_smile:

-------------------------

miz | 2017-01-02 01:15:31 UTC | #2

Anyone?

-------------------------

tarzeron | 2021-12-11 09:23:39 UTC | #3

If someone still needs it, you can do it

```
scrollView->GetChild("SV_ScrollPanel", true)->SetEnabled(false);
```

-------------------------

