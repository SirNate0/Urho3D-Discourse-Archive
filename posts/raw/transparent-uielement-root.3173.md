redmouth | 2017-05-29 13:59:26 UTC | #1

UIElement* root = GetSubsystem<UI>()->GetRoot();
parent = root->CreateChild<UIElement>();
parent->CreateChild<Button>();
...


Sometimes the background is black, sometimes it turns fully transparent, randomly.   Any suggestion to make the parent always transparent?

-------------------------

Modanung | 2017-05-29 13:25:13 UTC | #2

Maybe try `SetDefaultStyle` on the `root`?

-------------------------

redmouth | 2017-05-30 00:47:49 UTC | #3

the ui root has been set with DefaultStyle

-------------------------

