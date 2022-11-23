rogerdv | 2017-01-02 01:02:01 UTC | #1

I need  to programatically add several children to an existing UIElement, through this code:

[code]
for (i=0;i<numChoices;i++){
  Text@ t =Text();
  t.text = choices[i];
  dlgWindow.AddChild(t);
}
[/code]

But the children arent displayed. I tried creating an array of Text@, but that didnt worked neither.

-------------------------

hdunderscore | 2017-01-02 01:02:01 UTC | #2

Try like this:
[code]for (i=0;i<numChoices;i++){
  Text@ t =Text();
  dlgWindow.AddChild(t);
  t.text = choices[i];
  t.style = "Text";
}[/code]

-------------------------

Azalrion | 2017-01-02 01:02:01 UTC | #3

Which is a problem, the parent layout should be updated when a child is added to it that is already styled. I did look into it at one point and it's something to do with how it works out the minimum size.

-------------------------

rogerdv | 2017-01-02 01:02:02 UTC | #4

Damn, the same problem hit me when using a listview and I forgot I have to set the style.

-------------------------

rogerdv | 2017-01-02 01:02:03 UTC | #5

Ok, solved the text problem, but seems that Text doesnt handles click events. Tried to put the texts inside buttons, but I just get an empty button.

[code]for (int i = 0; i < d.answers.length; i++)	{
      Button@ buttons = Button();
      buttons.SetPosition(10,40+i*25);
      Text@ answers = Text();
      answers.text = d.answers[i];
      buttons.name = d.ids[i];      
      buttons.AddChild(answers);
      answers.style = "Text";
      dlgwin.AddChild(buttons);
      buttons.SetStyleAuto();
      buttons.SetMinSize(500, 22);
      SubscribeToEvent("UIMouseClick", "HandleControlClicked");
		
}[/code]

Whats missing now?

-------------------------

hdunderscore | 2017-01-02 01:02:03 UTC | #6

You need to actually enable text for input-- by default it's disabled (if that wasn't the case, a text in a button would receive events instead of the button, which is usually not what you want):
[code]answers.enabled = true;[/code]

-------------------------

