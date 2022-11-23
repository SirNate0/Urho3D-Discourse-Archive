Mike | 2017-01-02 01:01:50 UTC | #1

When using a Slider from a ScrollView with SetAutoDisableChildren enabled, moving the Slider becomes tedious as we are limited by the value set for SetAutoDisableThreshold (when the threshold is reached, sliding ends and we have to grab the knob again and slide in multiple small steps).
Maybe we could for example make an exception for the Slider's knob to not be impacted by SetAutoDisableChildren.

-------------------------

hdunderscore | 2017-01-02 01:01:50 UTC | #2

Which platform are you testing on? Are you using auto-disable on non-touch? On a touch situation? Horizontal slider? Touch emulation? I'm trying to reproduce the error.

There is already a check for the scrollbars (the children won't be disabled with scroll bar scrolling).

-------------------------

Mike | 2017-01-02 01:01:51 UTC | #3

Thanks hd_. I'm testing on Android and Touch emulation, without scrollbars, auto-disable off, horizontal slider.
I'll add a simple example to illustrate the 'issue'.

-------------------------

Mike | 2017-01-02 01:01:51 UTC | #4

Here is sample to reproduce on mobile or in Touch emulation:
[code]
void Start()
{
    input.mouseVisible = true;
    ui.root.defaultStyle = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
    InitWindow();
}

void InitWindow()
{
	Slider@ slider = Slider();
	slider.SetStyleAuto();
	slider.SetFixedSize(250, 40);
	slider.range = 50;
	slider.value = 25;

	ScrollView@ newScrollView = ui.root.CreateChild("ScrollView");
	newScrollView.SetStyleAuto();
	newScrollView.SetAlignment(HA_CENTER, VA_CENTER);
	newScrollView.SetFixedSize(250, 40);
	newScrollView.autoDisableChildren = true;
	newScrollView.SetScrollBarsVisible(false, false);
	newScrollView.contentElement = slider;
}
[/code]

-------------------------

hdunderscore | 2017-01-02 01:01:51 UTC | #5

Thanks for the sample code, error is reproduced. I'll look into it.

-------------------------

Mike | 2017-01-02 01:01:52 UTC | #6

Thanks hd_.

-------------------------

hdunderscore | 2017-01-02 01:01:53 UTC | #7

After looking at this, I'm not sure an in-engine solution is the best way, as it could get out of hand with micro-options. This is something that can be done on application side without too much effort:

[code]void Start()
{
    log.Open("./log.log");
    input.mouseVisible = true;
    ui.root.defaultStyle = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
    InitWindow();
    input.touchEmulation = true;
}

void InitWindow()
{
   Slider@ slider = Slider();
   slider.SetStyleAuto();
   slider.SetFixedSize(250, 20);
   slider.range = 10;
   slider.value = 50;

   ScrollView@ newScrollView = ui.root.CreateChild("ScrollView");
   newScrollView.SetStyleAuto();
   newScrollView.SetAlignment(HA_CENTER, VA_CENTER);
   newScrollView.SetFixedSize(250, 40);
   newScrollView.autoDisableChildren = true;
   newScrollView.SetScrollBarsVisible(false, false);
   newScrollView.contentElement = slider;

   SubscribeToEvent(slider, "SliderChanged", "HandleDrag");
   SubscribeToEvent(slider, "DragEnd", "HandleDrag");
}

void HandleDrag(StringHash eventType, VariantMap& eventData)
{
    UIElement@ element = eventData["Element"].GetPtr();
    UIElement@ parent = element.parent;

    if (parent is null)
        return;
	
    ScrollView@ scrollView = parent.parent;
    if (scrollView is null)
        return;
    
    if (eventType == StringHash("SliderChanged"))
        scrollView.autoDisableChildren = false;
    else if (eventType == StringHash("DragEnd"))
        scrollView.autoDisableChildren = true;
}[/code]

-------------------------

Mike | 2017-01-02 01:01:54 UTC | #8

Thanks hd_ for investing this possibility  :wink: 
Since latest commit for ScrollView.cpp it seems that I can't disable autoDisableChildren anymore, I'll try from a clean build later and report if necessary.

-------------------------

