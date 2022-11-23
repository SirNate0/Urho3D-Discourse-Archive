alessandro | 2017-05-26 14:41:38 UTC | #1

Does screen joystick have a predefined set of buttons?
i ask so because i have deleted all the buttons and i see them on te screen.
i dont't understand why

> void InitTouchInput()
> {
> TouchEnabled = true;
> var layout = ResourceCache.GetXmlFile("UA/ScreenJoystick.xml");
> if (!string.IsNullOrEmpty(JoystickLayoutPatch))
> {
> XmlFile patchXmlFile = new XmlFile();
> patchXmlFile.FromString(JoystickLayoutPatch);
> layout.Patch(patchXmlFile);
> }
> var screenJoystickIndex = Input.AddScreenJoystick(layout, ResourceCache.GetXmlFile("UI/DefaultStyle.xml"));
> Input.SetScreenJoystickVisible(screenJoystickIndex, true);
> }


WIth this configuration i see three buttons on the screen but if i substitute 
var screenJoystickIndex = Input.AddScreenJoystick(layout, ResourceCache.GetXmlFile("UI/DefaultStyle.xml"));


with

var screenJoystickIndex = Input.AddScreenJoystick(null, null); NOTHING changes.


CAN I PUT two buttons over the screen without using screenjoistick?
i am frustrated :frowning:

-------------------------

rasteron | 2017-05-26 12:59:35 UTC | #2

[quote="alessandro, post:1, topic:3166"]
CAN I PUT two buttons over the screen without using screenjoistick?
i am frustrated :frowning:
[/quote]

In NSW, there's a single fire/attack button, also a few buttons with debug, console etc on top.

-------------------------

weitjong | 2017-05-26 13:45:19 UTC | #3

It does not have any predefined. Despite its name, it is really just UI-element(s) overlayed on the scene with customizable bindings to the input events. In the sample apps, we use the default UI "skin" texture, but it does not have to be, i.e. you can go crazy on how the hats or the buttons should look like. The elements are layout using UI layout file which is an XML file. There is an undocumented or not well documented feature in Urho where any XML resources can be patched on the fly. In the code snippet above it is evidently visible that the buttons or what have you are actually came from another base XML resource file.

-------------------------

alessandro | 2017-05-26 18:28:47 UTC | #4

many thanks, i will dig on samples to get it woroking.

Alessandro

-------------------------

