rbnpontes | 2017-01-02 01:13:36 UTC | #1

Hello Guys, i have a problem with ScrollView.
everytime that i try to Add Element using AddChild, the list won't work, the list won't rezise and not showing the bars
example:
[code]
ScrollView* scroll = new ScrollView(context);
scroll->SetSize(100,50);
for(int i=0;i<100;i++){
UIElement* element = new UIElement*(context);
Text* text = new Text(context);
text->SetText("TEST");
element->AddChild(text);
scroll->AddChild(element);
}
[/code]
here is Screenshot of  problem
[img]http://imgur.com/a/iOiYj[/img]

-------------------------

cadaver | 2017-01-02 01:13:36 UTC | #2

ScrollView doesn't automatically accept several children to be added as the scrollable content. Rather you must assign a "content element" which could be for example a large image, or a bare UIElement containing children.

Try creating an UIElement (it can have layouting if you wish), assign it as the content element using ScrollView::SetContentElement() (it's automatically added as child of the scrollview at that point) then add the individual elements to the content element. If you have set it to layout and resize, you should see the scrollbars appear when the content is too large to show at once.

If you just want to add list items vertically, I recommend the ListView class for convenience. In that case you don't call AddChild() either, but AddItem().

-------------------------

rbnpontes | 2017-01-02 01:13:36 UTC | #3

Thank's for the help, the problem has solved

-------------------------

