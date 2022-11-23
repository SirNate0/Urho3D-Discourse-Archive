slapin | 2017-05-01 05:15:40 UTC | #1

1. Setting-up layout out of 2 parts using UIElements.
i.e. window - LM_HORIZONTAL,
UIElement_a - LM_VERTICAL
UIElement_b - LM_VERTICAL
window.AddChild(UIElement_a)
window.AddChild(UIElement_b)
UiElement_b.maxWidth = graphics.width * 0.25f;

Adding View3D to UIElement_a
Adding a few buttons as children to
UiElement_b - everything works as expected.

We see a screen with view3d on left, buttons on right, buttons use 1/4 of width.
Now we delete all children from left and right layouts.
Then we add UIElement_c (LM_FREE) to left and
a few other buttons to right. This goes absolutely haywire.

1. Buttons occupy 50% of width.
2. Everything is offset down like it was centered vertically.

If I delete all GUI and reconstruct from scratch, everything works as expected.
Any ideas? Why layout is messed-up?

-------------------------

slapin | 2017-05-01 05:46:25 UTC | #2

I was wrong, the problem is not resoleable by just recreating GUI, everything gets messed-up
after re-creation. Looks like behavior of all containers changes, they stop filling parent area.
i.e. root window starts filling smallest area possible, while at start everything seems to fill as much as possible,
Looks like something triggers unpredictable behavior change globally.

-------------------------

lezak | 2017-05-01 09:59:30 UTC | #3

For this kind of setup You should rather use anchors then layout modes.
Try this:
1. Window, layout mode: free, set anchor to cover as much of a screen as You want;
    2. UIElemenet a: layout mode free, anchor: xmin: 0, y min:0, xmax: 0.75, ymax: 1;
       2a. View3D, anchor: xmin 0, ymin 0. xmax 1, ymax 1 (will fill the whole left side - 75% of the window)
    3. UIElement b : layout mode: vertical, anchor: xmin 0.75, ymin: 0, xmax 1, ymax 1
        3a - add buttons - they will fill the left side

with this anchor pivot on all elements: 0,0. 

As for Your problems:
- offset is propably caused by pivot point location (horizontal and vertical aligment)
- resizing because You don't have min/max size specified

-------------------------

slapin | 2017-05-01 10:58:16 UTC | #4

Thanks.

I fixed this by hardcoding min values on all containers. I wonder why GUI behaves like this.
And why it works first time but never again?

-------------------------

lezak | 2017-05-01 11:23:57 UTC | #5

As You can find in documentation (about layouting child elements):
> They will be preferably resized to fit the parent element, taking into account their minimum and maximum sizes, but failing to do that, the parent element will be resized.

So if size of the child element doesn't fit container it will resize it and it may mess up the whole setup.

[quote="slapin, post:4, topic:3085"]
And why it works first time but never again?
[/quote]

That I don't know, I never had this problem. Are You making ui in editor and then loading it or each time you create it from code?

-------------------------

slapin | 2017-05-01 11:34:05 UTC | #6

I create it from code, UI editor in editor is too unstable for me
It looks like this behavior is triggered by deleting of child elements.
Then UI behavior changes. The only way to recover id elete all GUI elements and reconstruct all GUI.
If all min values are hardcoded from start the GUI is still slightly different from before deletion,
but as it is internal tool, I can live with that.
The sequence is -
Create all GUI - delete buttons - catastrophe (layout is messed-up) - delete all UI elements (nothing helps to recover,
even saving/loading) - create all previous layout except buttons - add different buttons.
This case produces working GUI (but it is a bit different - main window is bigger, buttons area is smaller, standalone text labels are larger). I'd say I would not recommend such GUI for real production, but it works for internal tools.
but real game GUIS are ususlly very simple, so probably they don't have such problems.

-------------------------

lezak | 2017-05-01 11:48:42 UTC | #7

It looks like Your problem is that Your container is being resized when You add child elements and then after deleting them it returns to minimal size. To keep fixed size whole time You should also specify the maximal size of the container. You can set min and max to be the same and then it won't resize in any case. 
[quote="slapin, post:6, topic:3085"]
I'd say I would not recommend such GUI for real production, but it works for internal tools.
[/quote]

You just must get used to it. In my project I'm using quite complex ui layouts and everything works as it's supposed to.

-------------------------

slapin | 2017-05-01 12:03:23 UTC | #8

Well, the UIs should be flexible, not nailed to the specific values. It is probably acceptable for game UI
though, but in this calse the UI could be much simpler. Now it is both complex and unpredictable if not nailed to the wall.
This is what I'm not happy about. I have huge experence with Gtk+ and Qt GUIs and can compare....
I used tiny embedded GUIs. They can't do many things and everything is manual, but they are tansparent in their workings and very simple. I used complex GUI systems in which you just put a set of widgets and layout containers do
their job, so you don't need to worry if your window gets resized. But in Urho it is complex - there are many handles you can mess-up, and many handles you have to tune to make things work. Also it is very hard to predict the consequences of changes. It is like driving combution engine manually switching sparks. You can do it, but it requires a lot of effort and experience. And the results are not very rewarding. So Urho GUI is not simple and transparent, also it will not help you like complex GUIs like Qt do. So it should be either simplified (dropping complex widgets
nobody knows how to make work, cleaning up, documenting remaining things) or some predictability should be added
(some sane defaults are needed, so there should be no need to nail everything to the wall). One can't sit on 2 chairs at the same time. Trying to do so will produce painful results.

-------------------------

slapin | 2017-05-01 12:06:00 UTC | #9

For example drop down list widget still doesn't work for me after years. Very high level magic is required to make it run.
i see it works in Editor, but each time I try to make it work it is complete failure. It should not be like this.

-------------------------

lezak | 2017-05-01 12:38:52 UTC | #10

Just use anchors and You won't need to worry about window being resized. 
Using dropdown list is as simple as using "AddItem" function and subscribing to "E_ITEMSELECTED"

-------------------------

slapin | 2017-05-01 12:13:57 UTC | #11

A problem is that in my case the list appears as a button, and its popup is empty. And I get no errors or warnings.
And it was like this since the beginning.

-------------------------

lezak | 2017-05-01 12:28:05 UTC | #12

Take this as reference. This is part of launcher in my project. "ModuleHandler" is object that scans resource dir for "ModInfo" objects (containing some info required for setup of different modules) and adds them to the map (You don't need this part) next, for each found mod there is Text added to the dropdown list (named modSelection_) (You need this part). 
>     void Launcher::SetMouduleHandler()
>     {
>         modHndlr_ = SharedPtr<ModuleHandler>(new ModuleHandler(context_));
>         for (auto m : modHndlr_->GetMods())
>         {
>             SharedPtr<Text> txt(new Text(context_));
>             txt->SetStyleAuto(defStyle_);
>             txt->SetText(m->GetName());
>             txtModMap_.Insert(Pair<SharedPtr<Text>, SharedPtr<ModuleInfo>>(txt, m));

>             modsSelection_->AddItem(txt);
>         }
>         SubscribeToEvent(modsSelection_, E_ITEMSELECTED, URHO3D_HANDLER(Launcher, HandleModChange));
>     }

>     void Launcher::HandleModChange(StringHash eventType, VariantMap & eventData)
>     {
>         Text* txt = static_cast<Text*>(modsSelection_->GetSelectedItem());
>         if (txt)
>         {
>             if (txtModMap_.Contains(SharedPtr<Text>(txt)))
>             {
>                 selectedMod_ = txtModMap_[SharedPtr<Text>(txt)];
>                 URHO3D_LOGDEBUG("Selected mod: " + selectedMod_->GetName() + "\n" + " Version: " + String(selectedMod_->GetVersion()) + " res path: " + selectedMod_->GetResPath());
>             }
>         }
>     }

-------------------------

Victor | 2017-05-01 13:04:59 UTC | #13

I've seen this issue, however for me it's usually because I didn't set the default style somewhere (or size in the case below). This has been tackled on the forums at some point as well. Maybe your issue is similar?

Google Search: **urho3d dropdown empty**
https://urho3d.prophpbb.com/topic1450.html

https://urho3d.prophpbb.com/topic790.html

I hope that helps man :)

-------------------------

