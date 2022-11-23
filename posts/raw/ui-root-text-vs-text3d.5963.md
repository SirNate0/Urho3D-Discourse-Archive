pldeschamps | 2020-03-02 17:00:59 UTC | #1

Hello,

In a Urho3D 3D game, if you need to write over a game character its name, I guess there are two solutions:
- use Text3D to write the name of the character and manage to get the text facing the camera
- get the 2D coordinates of the character in the UI and write the name over the character.

I don't do a game but I need to write the name of the stars over each star.
What would be the easiest solution?
What is the easiest way to get the 2D coordinates of the star in the UI rectangle (and to know if the star is in the field of the camera)?

Regards,

-------------------------

Modanung | 2020-03-21 15:12:06 UTC | #2

For the UI approach you can use the following function of the camera:
```
/// Convert a world space point to normalized screen coordinates (0 - 1).
Vector2 WorldToScreenPoint(const Vector3& worldPos) const;
```
If you multiply this by `GetSubsystem<Graphics>()->GetSize()` you should have the required position for placing your UI element.

-------------------------

WangKai | 2020-03-03 02:20:47 UTC | #3

And also, I guess we also need to sort the UI "billboard" according to their distance to the main camera.

-------------------------

Modanung | 2020-03-03 09:38:36 UTC | #4

...which `Text3D` would take care of for you, I guess. You'll probably want to `SetFixedScreenSize(true)` if you use that component.

-------------------------

pldeschamps | 2020-03-20 21:44:21 UTC | #5

Hi @Modanung

I can get the Vector2D in C#:
```
IntVector2 v2 = viewPort.WorldToScreenPoint(bbi.Position);
```
But do you have any idea how to GetSubsystem<Graphics>()->GetSize() in C#?

I tried that:
```
            var graphics = GetSubsystem<Graphics>();
```
But GetSubsystem is non generic in urhosharp :-( 

I hope you are not in trouble with COVID-19.

Regards,

-------------------------

pldeschamps | 2020-03-20 21:52:59 UTC | #6

Sorry for this question.
I think the solution is that one:
```
Urho.BillboardWrapper bbi;
                bbi = StarsBbs.GetBillboardSafe(i);
                IntVector2 v2 = viewPort.WorldToScreenPoint(bbi.Position);
                IntVector2 v2TextPosition = new IntVector2(v2.X * graphics.Width, v2.Y * graphics.Height);
```
Is this what you mean by "multiply this by  `GetSubsystem<Graphics>()->GetSize()`"?

-------------------------

Modanung | 2020-03-20 22:37:47 UTC | #7

[quote="pldeschamps, post:5, topic:5963"]
I hope you are not in trouble with COVID-19.
[/quote]

Yesterday was the worst it seems. I'm feeling a lot better already, but thanks for your concern. :slightly_smiling_face:

[quote="pldeschamps, post:6, topic:5963"]
Is this what you mean by "multiply this by `GetSubsystem<Graphics>()->GetSize()` "?
[/quote]
This is only required when using `Camera::WorldToScreenPoint` (which should be named `Pos`, and not `Point`, in my opinion), `Viewport::WorldToScreenPoint` already does this multiplication.

-------------------------

pldeschamps | 2020-03-20 22:01:15 UTC | #8

[quote="Modanung, post:7, topic:5963"]
`Viewport::WorldToScreenPoint` already does this multiplication
[/quote]

Well, the text seems not to be at the right position on the attached png
![names|690x388](upload://hfVvKIV7YXO6kdcExikBieXmFia.png)

-------------------------

pldeschamps | 2020-03-20 22:02:40 UTC | #9

Where I don't multiply:
```
{
            var graphics = Graphics;
            Urho.BillboardWrapper bbi;
            for(uint i=0; i< (uint)App.StarsData.Count; i++)
            {
                bbi = StarsBbs.GetBillboardSafe(i);
                IntVector2 v2 = viewPort.WorldToScreenPoint(bbi.Position);

                WriteStarName(v2);
            }
        }
        private void WriteStarName(IntVector2 v2)
        {
            var text = new Text()
            {
                Value = "star",
                Position = v2
            };
            text.SetColor(Color.Cyan);
            text.SetFont(font: ResourceCache.GetFont("Fonts/Anonymous Pro.ttf"), size: 10);
            UI.Root.AddChild(text);
        }
```

-------------------------

Modanung | 2020-03-20 22:04:29 UTC | #10

Try getting it right with a single star first.

-------------------------

pldeschamps | 2020-03-20 22:07:03 UTC | #11

You are right.
And moreover, the positions of the names are the same whatever the size of the window. So I have to update the positions after the window is set...
I will find out that tomorrow.
Thanks for your help.

-------------------------

Modanung | 2020-03-20 22:10:34 UTC | #12

When using `Text3D` you would not have to update their position separately. With `UIElement`s you'll probably want your stars to keep a reference to their label.

-------------------------

pldeschamps | 2020-03-20 22:10:25 UTC | #13

I am trying that for the cardinal points but it is very difficult to keep the text facing the camera. I still not have succeded. But if I succeed, I could do the same for the stars.

-------------------------

pldeschamps | 2020-03-21 15:11:49 UTC | #14

I did it. It seems a little bit slow though. I will try to optimize that.
I have to find a font compatible with greek characters.
![names_ok|460x500](upload://hD8jDoaxJLxkzXiQzM2kDogDKpy.png)

-------------------------

SirNate0 | 2020-03-21 21:04:25 UTC | #15

I think some of the libre office fonts would include them, though I'm not sure what their licenses are (fonts like liberation serif)

-------------------------

pldeschamps | 2020-03-21 21:57:36 UTC | #16

Hi @SirNate0,
The first issue was that I was using UTF-16. First I converted my strings to UTF-8. But there are still some greek characters that don't print. Unfortunately, no chinese characters printed.
I go on with the english names...

-------------------------

