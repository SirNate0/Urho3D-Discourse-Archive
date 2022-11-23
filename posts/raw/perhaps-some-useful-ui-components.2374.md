Lumak | 2017-01-02 01:15:02 UTC | #1

Here [url]https://github.com/Lumak/Urho3D-UI-Components[/url]

[img]http://i.imgur.com/lfSX00F.jpg[/img]

[img]http://i.imgur.com/DerpP2p.jpg[/img]




Edit: changed screenshot, again.

-------------------------

yushli | 2017-01-02 01:15:02 UTC | #2

That is really great! I will check it out.
Can I adjust the background images for these components?

-------------------------

Lumak | 2017-01-02 01:15:03 UTC | #3

Changed code and UI.png to be able to change tab color. Pull the repo you will seen green tab/body now.

Edit: and with that, you should be able to change every component's background color now.

-------------------------

Victor | 2017-01-02 01:15:03 UTC | #4

Nice work! Thanks!

-------------------------

Lumak | 2017-01-02 01:15:03 UTC | #5

@Victor, I hope you can make a good use of them:)

Repo update: edited UI.png to add colorable checkbox.

I suppose I can rename the checkboxGroup class to Radial something.

-------------------------

sabotage3d | 2017-01-02 01:15:04 UTC | #6

Thanks for these.

-------------------------

Lumak | 2017-01-02 01:15:05 UTC | #7

@sabotage3d, there's more to come :slight_smile: 

@yushil, I added a UI-NoColor.png and DefaultNoColorStyle.xml in the repo for you.  Be warned, you'll have to manually change the color for everything that you create.

-------------------------

yushli | 2017-01-02 01:15:05 UTC | #8

Thank you for sharing all these. I will try it out. Keep up the good work.  :slight_smile:

-------------------------

Lumak | 2017-01-02 01:15:06 UTC | #9

preview of what I'm working on, inspired by godan's Iogram:

[img]http://i.imgur.com/gPF0MGw.jpg[/img]

-------------------------

Lumak | 2017-01-02 01:15:08 UTC | #10

progress: this is coming along nicely, see pic below.

Currently, my interfaces to access data look like this:

[code]
Variant var = outputNode_->GetCurrentValue("Ni");

float x = outputNode_->GetValueAt("Xi", ballList_[i].time);
float y = outputNode_->GetValueAt("Yi", ballList_[i].time);
[/code]

I think that's simple... not sure if it can be simplified more.

[img]http://i.imgur.com/68rnBUC.jpg[/img]

-------------------------

sabotage3d | 2017-01-02 01:15:09 UTC | #11

Nice! Is it currently possible to antialias the lines?

-------------------------

Lumak | 2017-01-02 01:15:09 UTC | #12

No, I haven't added anything.  But I think 1vank or someone added AA on debug lines about a month ago.  I think same could be applied to the linebatcher.

Anyway, checked in my latest code that includes node graph.

-------------------------

yushli | 2017-01-02 01:15:09 UTC | #13

Woo, you are making great progress! Nice to see node graph built solely on Urho3D, not depending on other UI libraries. Looking forward to other exciting components...

-------------------------

Miegamicis | 2017-01-02 01:15:09 UTC | #14

Awesome work! Looks great, will check this out.  :slight_smile:

-------------------------

godan | 2017-01-02 01:15:09 UTC | #15

Nicely done! Node graphs FTW!

-------------------------

Lumak | 2017-01-02 01:15:09 UTC | #16

Thanks.  I hope I've written enough to be a good foundation for others to build on.

-------------------------

namic | 2017-01-02 01:15:10 UTC | #17

The node graph is amazing. Thank you.

-------------------------

Lumak | 2017-01-02 01:15:15 UTC | #18

[quote="sabotage3d"]Nice! Is it currently possible to antialias the lines?[/quote]

I looked into this and this doesn't work like the debug lines as I previously thought. All batches are rendered by UI class, and I'm not sure how to specify anti aliasing for a specific batch.  Maybe someone in the community has a clear idea on how to fix it.

-------------------------

sabotage3d | 2017-01-02 01:15:15 UTC | #19

I am getting some errors on OSX. This is the log:
[url]http://codepad.org/qtKWPhbK[/url]

-------------------------

Lumak | 2017-01-02 01:15:15 UTC | #20

The 
[code]
void SetCheckedInternal(bool enable);
[/code]
is defined in: Urho3D-UI-Components/Source/Urho3D/UI/CheckBox.h

Try changing the two fn params in the .cpp/.h files to:
[code]
    void SetRange(const Variant &vmin, const Variant &vmax);
    void SetCurrentValue(const Variant &val);

[/code]

I appreciate the PR once you verified it's fixed.

edit: and I'm not sure what this error means:
[code]
/DEV/Urho3D-UI-Components/Source/Samples/61_UITest/TabGroup.h:59:27: error:
      extra qualification on member 'GetTabElement'
    TabElement* TabGroup::GetTabElement(unsigned idx);
[/code]

-------------------------

sabotage3d | 2017-01-02 01:15:15 UTC | #21

It works now. Clang is more strict it needs to be GetTabElement only without TabGroup. I made a quick PR with the working changes for OSX.

-------------------------

Lumak | 2017-01-02 01:15:15 UTC | #22

OK, thanks.

-------------------------

ghidra | 2017-01-02 01:15:15 UTC | #23

How did i miss this!?
Really cool!

-------------------------

miz | 2017-01-02 01:15:19 UTC | #24

these are great thanks!

-------------------------

