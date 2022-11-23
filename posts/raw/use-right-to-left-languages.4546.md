hassanrahimi | 2018-09-17 20:19:05 UTC | #1

hi all 
I want to use right to left language in text in the urho3d, I try this but don't work. 
please help me. 
thanks

-------------------------

hassanrahimi | 2018-09-19 08:11:40 UTC | #2

hi all i try to make a font , but dont work correct, in persian(farsi) language, word must stick to other
it is result of make new font that is incorrect

![Capture|690x432](upload://a5lhrQMc5e7yHE2qKLGdPlEKsTi.png) 



please anyone answer to me!

-------------------------

Modanung | 2018-09-19 14:50:28 UTC | #3

I wish I could help you. But apart from changing the [alignment](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_text.html#a1582bfb8d06d3c7675681ed2475b8756) of `Text` I _don't know_ if Urho (already) has full support for right-to-left languages.
Would it be enough to reverse the order of each string/line as a work-around? Adding this as a parameter shouldn't be too hard. Maybe you could create a pull request for this?

Welcome to the forums, btw! :confetti_ball: :)

-------------------------

hassanrahimi | 2018-09-20 03:42:15 UTC | #4

Thanks for your sympathy.thanks,I Changed text alignment but dont work.
in editor i cant insert farsi language in text3d.
i think in core editor dose not ready for enter right to left language.
i dont know how to develop urho3d editor to possibility use right to left language.

-------------------------

Modanung | 2018-09-20 21:49:34 UTC | #5

But would reversing the string before use solve your problem?

-------------------------

hassanrahimi | 2018-09-21 06:29:17 UTC | #6

hi ,thank you.
don't work.😧

-------------------------

Modanung | 2018-09-21 06:35:55 UTC | #7

Isn't the order of the characters all that needs to change?

-------------------------

Omid | 2018-09-21 10:39:20 UTC | #8

@hassanrahimi I think you need Persian Reshaper.
I search and i found one for C#
https://github.com/yeganehaym/PersianReshaper 
I don't know which platform do you using now.

-------------------------

Omid | 2018-09-21 10:44:00 UTC | #9

btw write your word in `Character map` and paste it to your code for test.
![image|485x410](upload://yGT1LMvJfS2nGLlpNIcvNAGFnxU.png)

-------------------------

hassanrahimi | 2018-09-21 13:40:21 UTC | #10

thanks mr Omid and thanks Mr Modanung 
it's Solved.

for todays, before support RTL languages in Urho3d , Combine two methods 
1: Write your text in Character Map and copy text to string in c#(click start menu and write Charactor Map)
2: reverse your string
3: show in value in text.
![Capture|344x192](upload://qEtY1yRd2K3oy63mUPitlY5gnjA.png) 
```
    protected override void Start()
		{

                     string str = "ﺳﻠﺎﻡ ﺑﻪ ﻫﻤﻪ";   
                    var cache = ResourceCache;
                    var helloText = new Text()
              {
                
                Value = Reverse(str),
             
					HorizontalAlignment = HorizontalAlignment.Center,
					VerticalAlignment = VerticalAlignment.Center,                    
                    
				};
			helloText.SetColor(new Color(0f, 1f, 0f));
			helloText.SetFont(font: cache.GetFont("Fonts/BYekan1.sdf"), size: 30);
            
            UI.Root.AddChild(helloText);
            
			
			Graphics.SetWindowIcon(cache.GetImage("Textures/UrhoIcon.png"));
			Graphics.WindowTitle = "UrhoSharp Sample";

			// Subscribe to Esc key:
			Input.SubscribeToKeyDown(args => { if (args.Key == Key.Esc) Exit(); });
		}


//Reverse method
 private static string Reverse(string str)
        {
            string revStr = string.Empty;
            for (int i = str.Length - 1; i >= 0; i--)
            {
                revStr += str[i].ToString();
            }
            return revStr;
        }
```
thnaks again.:sunflower::sunflower::sunflower::sunflower::confetti_ball::tada::confetti_ball:

-------------------------

