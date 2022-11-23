capelenglish | 2018-06-01 17:22:38 UTC | #1

I am trying to create a countdown timer using Text. When the user presses a certain key, I want the seconds value to update on the screen as it counts down from 5. The code below uses a Urho3D::Timer, but it doesn't display the text on the screen until after the timer has counted all the way down. Any suggestions would be appreciated.

    ResourceCache* cache = GetSubsystem<ResourceCache>();
		UI* ui = GetSubsystem<UI>();
		// Construct new Text object, set string to display and font to use
		Text* instructionText = ui->GetRoot()->CreateChild<Text>();
		instructionText->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"), 48);
		instructionText->SetColor(Color(0.0f, 1.0f, 0.0f));
		instructionText->SetTextAlignment(HA_CENTER);
		instructionText->SetHorizontalAlignment(HA_CENTER);
		instructionText->SetVerticalAlignment(VA_CENTER);
		instructionText->SetPosition(0, ui->GetRoot()->GetHeight() / 4);
		instructionText->SetText("Countdown");
		// Add Text instance to the UI root element
		GetSubsystem<UI>()->GetRoot()->AddChild(instructionText);

		for (int i = 5; i >= 1; i--)
		{
			instructionText->SetText("Countdown " + String(i));
			Timer tmr = Timer();
			do {} 
			while (tmr.GetMSec(false) < 1000);
			// reset the timer
			tmr.Reset();

			if (DEBUG) URHO3D_LOGINFOF("Tick %d", i);
		}

-------------------------

Eugene | 2018-05-31 20:41:58 UTC | #2

The program cannot draw countdown because Engine doesn’t draw anything until you exit all your functions and let internal rendering routines go.

-------------------------

Lumak | 2018-06-01 17:23:07 UTC | #3

Understanding a bit about Urho3D's game loop might help - I'll keep it short.
Like many game engines, Urho3D's game loop consists of (listing from Urho3D/Core/CoreEvents.h):
[code]
1 - E_BEGINFRAME, BeginFrame
2 - E_UPDATE, Update
3 - E_POSTUPDATE, PostUpdate
4 - E_RENDERUPDATE, RenderUpdate
5 - E_POSTRENDERUPDATE, PostRenderUpdate
6 - E_ENDFRAME, EndFrame
[/code]

For simplicity, treat these as **sequential stages** that *gets processed every frame*, and in each stage processes some subsystem required for that stage, e.g graphics and UI needs to render in **stage 4**.
Most of the user's game logic ends up in stage 2, in Update().  However, if your Update stage looks like:
[code]
Update-Stage()
{
  for-loop(...)
  {
    do{} while (somevalue == valid);
  }
}
[/code]
rest of the stages are waiting their turn to process but cannot get there until update() completes.

Better method for your countdown in Update()
[code]
if (countDownTimer_.GetMSec(false) > 1000 && countDown_ > 0)
{
  instructionText->SetText("Countdown " + String(--countDown_));
  countDownTimer_.Reset();
}
[/code]

-------------------------

capelenglish | 2018-06-01 11:01:30 UTC | #4

@Lumak, Thanks for this answer, it is very helpful. This is my first gaming engine and I'm still trying to get my head wrapped around how everything works.

-------------------------

capelenglish | 2018-06-01 12:01:31 UTC | #5

@Lumak, using your suggested approach, I was able to implement my countdown timer exactly as I wanted to. Thanks again!

I would mark this issue [SOLVED] but I don't see any buttons or links to do so.

-------------------------

Eugene | 2018-06-01 12:18:01 UTC | #6

Here should be one more button:
But maybe topics in this forum category doesn't have such feature, I'm not 100% sure.
![image|690x311](upload://l4cof8fZlhYQg3tX3G9oNXJ7Y0g.png)

-------------------------

Modanung | 2018-06-01 17:24:04 UTC | #7

[quote="Eugene, post:6, topic:4274"]
But maybe topics in this forum category doesn’t have such feature, I’m not 100% sure.
[/quote]

Indeed only topics in the Support category can be marked _solved_.

-------------------------

capelenglish | 2018-06-01 20:00:29 UTC | #8

It appears that only certain users have the checkbox to mark a reply as solving the problem. For example, neither @Lumak nor I have this checkbox but @Eugene and @Modanung do. Not sure what's up with that...

-------------------------

Modanung | 2018-06-01 20:03:15 UTC | #9

I did have to change the topic's category (allowed at trust level 4) first and refresh the page for the button to appear. :slight_smile:

-------------------------

