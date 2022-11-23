evolarium | 2017-01-02 01:07:40 UTC | #1

I've been trying to create a UI with the built-in UI system, but I'm getting some behaviour that seems weird to me.

[code]
  UI* ui = GetSubsystem<UI>();
  Graphics* graphics = GetSubsystem<Graphics>();

  UIElement* root = ui->GetRoot();
  // Load the style sheet from xml
  root->SetDefaultStyle(cache_->GetResource<XMLFile>("UI/DefaultStyle.xml"));

  UIElement* window = root->CreateChild<UIElement>();
  window->SetLayout(LM_VERTICAL);

  UIElement* topMenu = window->CreateChild<UIElement>();
  topMenu->SetLayout(LM_HORIZONTAL);

  BorderImage* columnOne = topMenu->CreateChild<BorderImage>();
  columnOne->SetLayout(LM_VERTICAL, 6, IntRect(6,6,6,6));
  columnOne->SetColor(Color(1.0f, 0.0f, 0.0f));
  columnOne->SetMinWidth(graphics->GetWidth()/2);

  BorderImage* columnTwo = topMenu->CreateChild<BorderImage>();
  columnTwo->SetLayout(LM_VERTICAL, 6, IntRect(6,6,6,6));
  columnTwo->SetColor(Color(0.0f, 0.0f, 1.0f));
  columnTwo->SetMinWidth(graphics->GetWidth()/2);

  CheckBox* checkBox = columnOne->CreateChild<CheckBox>();
  checkBox->SetStyleAuto();

  CheckBox* checkBox2 = columnTwo->CreateChild<CheckBox>();
  checkBox2->SetStyleAuto();
[/code]

My expected layout versus what I get:
imgur.com/gallery/YSLpJ

Shouldn't each column be half the screen width?

-------------------------

TikariSakari | 2017-01-02 01:07:40 UTC | #2

If I understand correctly the min widths are usually calculated values, so that it counts the minimum size that the sub elements use. Like lets say that you have text there, then usually the element that contains the text has minimum size of what the text size would be if it uses either horizontal or vertical layout.

You could also try using fixed width which from my understanding kind of ignores the automatic sizing that comes from layout modes. But from my experience trying to set minimum size quite rarely actually works the way you might thing it would do, especially with layout modes.

Also if you are trying to make full screen width ui, you could just set the topmenu width to full screen width. This should? then split the given width to the child elements evenly since it is using horizontal layout, but I am not sure if you also need to set all of topmenus parent elements to this same size as well including the root. Then you can remove the minimum width from the columns I think.

Edit: Also you might want to try to create your ui-layout with the editor that comes with Urho or at least some basic layouts with it.

-------------------------

cadaver | 2017-01-02 01:07:40 UTC | #3

Will have to check this in detail, but the current layout code can force the parent element beyond its min or max size, unless it's set to completely fixed size, in the case that the child element sizing can't be satisfied by other means. This would certainly be preferable to fix.

-------------------------

