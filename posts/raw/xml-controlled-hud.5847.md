Chimareon | 2020-01-29 13:19:27 UTC | #1

Hi All,
thanks for amazing help with my last issue.
I am few stepd further in my work, but I have encountered another Problem:

I want to create a sort of Splashscreen for my app in form of Floating Panel connected to the camera (so that it does not move in respect to camera).

I am trying to use UI.root element with to which I set .XML file as DefaultStyle.
I get a White rectangle behaving the way I want, but cannot Control what happens within it.

Would someone be so kind to post sample .XML with Explanation how to make it work?

my XML:
   
    <?xml version="1.0"?>
    <!-- element type="Window">
      <attribute name="Position"     value="100 100" />
      <attribute name="Size"         value="380 120" />
    < element type="Button">
      <attribute name="Name"       value="ToggleLight1" />
      <attribute name="Position"   value="20 20" />
      <attribute name="Size"       value="140 30" />
    <element type="Text">
      <attribute name="Horiz Alignment"    value="Center" />
      <attribute name="Vert Alignment"     value="Center" />
      <attribute name="Top Left Color"     value="1 1 1 1" />
      <attribute name="Top Right Color"    value="1 1 1 1" />
      <attribute name="Bottom Left Color"  value="1 1 1 1" />
      <attribute name="Bottom Right Color" value="1 1 1 1" />
      <attribute name="Text"               value="Toggle light 1" />
    </element >
    </element >
    <element type="BorderImage">
      <attribute name="Name"       value="Texture" />
      <attribute name="Position"   value="20 20" />
      <attribute name="Size"       value="140 30" />
      <attribute name="Blend Mode" value="alpha" />
      <attribute name="Border"     value="4 4 4 4" />  
      <attribute name="Image Rect" value="0 0 16 16" />  
      <attribute name="Texture"    value="Texture2D;Textures/Earth.jpg" />    
    </element>
    </element >

I know that indentations are off, but they are fine in my Version :slight_smile: 

The BorderImage does is not shown at all :frowning:

-------------------------

Modanung | 2020-01-29 13:20:22 UTC | #2

Could this unterminated comment have something to do with it? :slightly_smiling_face: 

[quote="Chimareon, post:1, topic:5847"]
`<!-- element type="Window">`
[/quote]

Some code showing how you're trying to use the UI might also help to find a solution.

-------------------------

Chimareon | 2020-01-29 14:00:04 UTC | #3

comment is leftover after trying to persuade Forum to Show XML Code, it is not one of the Problems.


            base.Start();

            uiRoot = UI.Root;
            XmlFile style = ResourceCache.GetXmlFile("UI/WelcomeHUD.xml");

            uiRoot.SetDefaultStyle(style);

            InitWindow();

here is the Code where I try to call the .xml

-------------------------

Modanung | 2020-01-29 14:07:58 UTC | #4

Try `UI/DefaultStyle.xml` for the style and `uiRoot.LoadXML(...)` to load your layout.

-------------------------

Chimareon | 2020-01-31 09:00:48 UTC | #5

thanks for Your suggestions, it works now. 
I have however one interesting bug I encountered. 
I am running my Code on HoloLens gen1.
I am using the builtin camera to look for QR codes with Zxing.
When the Camera indicator (the orange icon in top left corner) is active, the splashscreen (the XML controled one) gets ~2 times bigger. When camera is turned off, the ui goes back to original size. Back and forth.
any idea what could be the Ground for this behaviour?

-------------------------

SirNate0 | 2020-01-31 15:25:14 UTC | #7

Does the resolution of the Hololens display change when the camera is on, perhaps?

-------------------------

Chimareon | 2020-02-03 07:15:38 UTC | #8

I have searched for it, there is one thread on Unity-related forum. 
https://forums.hololens.com/discussion/6508/hololens-in-camera-resolution-differences-when-taking-a-photo-and-using-unitys-camera-gameobject
but I cannot seem to find a way to translate it into urho.

-------------------------

SirNate0 | 2020-02-03 18:32:37 UTC | #9

Try looking at the log for window resized events when the camera is enabled/disabled. Lines like
`[Mon Feb  3 13:21:41 2020] DEBUG: Window was resized to 725x480`
That should at least confirm that it is the hololens changing the resolution based on the camera (I believe I read they reduce the framerate to 30fps when recording video, so a resolution drop may also be a thing). Other than that suggestion, I don't think I can help you much, since I don't have a hololens to try debugging it myself. Perhaps someone else with one has some suggestions...

[ Of course, if you wanted to get me a hololens, I'd be more than happy to help with trying to debug the issue ;) ]

-------------------------

