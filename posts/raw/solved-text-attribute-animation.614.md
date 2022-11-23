Bluemoon | 2017-01-02 01:01:40 UTC | #1

Having learned how to use Urho3D's attribute animation, I tried to animated the text attribute of a Text UI element to obtain the effect of the text changing based on keyframe like the code below but it didn't work out and no errors were thrown or logged
[code]
ValueAnimation@ textAnimation = ValueAnimation();
		
textAnimation.SetKeyFrame(0.0f, Variant(String("1")));
textAnimation.SetKeyFrame(1.0f, Variant(String("2")));
textAnimation.SetKeyFrame(2.0f, Variant(String("3")));

Text@ text = ui.root.CreateChild("Text");
//Other initialization procedures here...

text.SetAttributeAnimation("Text", textAnimation, WM_ONCE);
[/code]  

I tried animating the color attribute and it worked out well

can the text attribute of a Text UI be animated, since it is an attribute I thought all attributes of Animatables can be animated

-------------------------

hdunderscore | 2017-01-02 01:01:41 UTC | #2

Looks like this is caused by the text attribute being set up like this:
[code]ATTRIBUTE("Text", String, text_, String::EMPTY, AM_FILE);[/code]

Because it's setting to the variable directly, instead of calling through SetText/GetText, it doesn't call the UpdateText method. Eg, if you do this in an update event:
[code]text.text = text.text;[/code]

You'll see the animation is working, just not updating automatically.

-------------------------

weitjong | 2017-01-02 01:01:41 UTC | #3

I believe this can be considered as a bug. Some of the attributes, such as Text's text attribute, need the ApplyAttributes() method to be called on the instance being changed in order to make it effective. Current attribute animation implementation may have forgotten to do so. When changing the Text's text attribute in the attribute inspector window in the editor, the changed text is reflected immediately correctly because it calls the ApplyAttributes() method somewhere in the inspector's edit function.

-------------------------

weitjong | 2017-01-02 01:01:43 UTC | #4

I have fixed this bug in the master branch. I have also modified the 30_LightAnimation samples to test out the text attribute animation.

-------------------------

Bluemoon | 2017-01-02 01:01:43 UTC | #5

[quote="weitjong"]I have fixed this bug in the master branch. I have also modified the 30_LightAnimation samples to test out the text attribute animation.[/quote]

Thats great, I'll grab the master branch later during the day and test it out. Thanks a million

-------------------------

Bluemoon | 2017-01-02 01:01:56 UTC | #6

Sorry for the late reply... it works well now. Thanks once more  :smiley:

-------------------------

