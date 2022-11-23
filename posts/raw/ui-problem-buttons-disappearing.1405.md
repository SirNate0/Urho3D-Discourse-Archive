Enhex | 2017-01-02 01:07:31 UTC | #1

I have a level selection menu that contains buttons for selecting a level.
The buttons are programmically created.
If there are more than 13 levels, the buttons disappear:
13: [i.imgur.com/6O9OZuq.png](http://i.imgur.com/6O9OZuq.png)
14: [i.imgur.com/s1pvnCg.png](http://i.imgur.com/s1pvnCg.png)

Even if I simplify the Button creation code to bare minimum it still happens:
[code]
auto levelButton = levels_container->CreateChild<Button>();
levelButton->SetStyleAuto();
[/code]

The container of the buttons is a ScrollView.

Anyone knows why it might happen?

-------------------------

