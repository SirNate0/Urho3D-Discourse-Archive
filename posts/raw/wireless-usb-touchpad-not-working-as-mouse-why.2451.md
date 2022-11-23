OMID-313 | 2017-01-02 01:15:28 UTC | #1

Hi everyone,

I've been using a regular mouse (both wired and wireless) for my Urho3D game as the input, and it has worked fine. (Raspberry Pi)

I just bought a wireless USB touch pad (Logitech T650).
[amazon.com/Logitech-Recharg ... B0093H4WT6](https://www.amazon.com/Logitech-Rechargeable-Touchpad-Multi-Touch-Navigation/dp/B0093H4WT6)
[support.logitech.com/en_us/product/touchpad-t650](http://support.logitech.com/en_us/product/touchpad-t650)
But the problem is that when running the game, it doesn't recognize the mouse events (scroll, mouse move, click, ...).
In raspberry pi's desktop, the mouse works fine. But when I start the game, the mouse doesn't work.

What could be the problem !?

-------------------------

OMID-313 | 2017-01-02 01:15:28 UTC | #2

This is my code:

[code]

#include "Scripts/Utilities/Sample.as"

Node@ mushroomNode;
StaticModel@ mushroomObject;
Material@ My_Mat;
ValueAnimation@ My_Color;

bool My_Click = false;
bool My_Click2 = false;
int Clk = 1;
int C1 = 1;

void Start()
{

    SampleStart();
    CreateScene();
    SetupViewport();
    SubscribeToEvents();
}

void CreateScene()
{
    scene_ = Scene();
    scene_.CreateComponent("Octree");

    Node@ lightNode = scene_.CreateChild("DirectionalLight");
    lightNode.direction = Vector3(0.6f, -1.0f, 0.8f); // The direction vector does not need to be normalized
    Light@ light = lightNode.CreateComponent("Light");
    light.lightType = LIGHT_DIRECTIONAL;
    light.brightness = 2.1f;

	My_Mat = cache.GetResource("Material", "Materials/wire_255013019.xml");
	My_Color = ValueAnimation();
		
	        mushroomNode = scene_.CreateChild("Mushroom");
		        mushroomNode.position = Vector3(0.0f, 0.0f, 300.0f);
	        mushroomNode.rotation = Quaternion(0.0f, 0.0f, 0.0f);
	        mushroomNode.SetScale(0.6f);
	        mushroomObject = mushroomNode.CreateComponent("StaticModel");
		mushroomObject.model = cache.GetResource("Model", "3D_Models/Shoe_3.mdl");
		mushroomObject.ApplyMaterialList();		
		
	ScriptInstance@ instance = mushroomNode.CreateComponent("ScriptInstance");
	instance.CreateObject(scriptFile, "Rotator");
	Rotator@ rotator = cast<Rotator>(instance.scriptObject);
	rotator.rotationSpeed = Vector3(10.0f, 10.0f, 10.0f);

    cameraNode = scene_.CreateChild("Camera");
    cameraNode.CreateComponent("Camera");

    cameraNode.position = Vector3(0.0f, 5.0f, 0.0f);
}

void CreateInstructions()
{
    Text@ instructionText = ui.root.CreateChild("Text");
    instructionText.text = "SAPNA-CO :  Use WASD keys to move!";
    instructionText.SetFont(cache.GetResource("Font", "Fonts/Anonymous Pro.ttf"), 15);

    instructionText.horizontalAlignment = HA_CENTER;
    instructionText.verticalAlignment = VA_CENTER;
    instructionText.SetPosition(0, ui.root.height / 3);
}

void SetupViewport()
{
    Viewport@ viewport = Viewport(scene_, cameraNode.GetComponent("Camera"));
    renderer.viewports[0] = viewport;
}

void MoveCamera(float timeStep)
{
    const float MOVE_SPEED = 10.0f;
    const float MOUSE_SENSITIVITY = -0.05f;

    IntVector2 mouseMove = input.mouseMove;
    yaw += MOUSE_SENSITIVITY * mouseMove.x;
    pitch += MOUSE_SENSITIVITY * mouseMove.y;
    pitch = Clamp(pitch, -90.0f, 90.0f);

	mushroomNode.Rotate(Quaternion(MOUSE_SENSITIVITY * mouseMove.y, MOUSE_SENSITIVITY * mouseMove.x, 0.0f));

    if (input.keyDown['W'])
        cameraNode.Translate(Vector3(0.0f, -5.0f, 0.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['S'])
        cameraNode.Translate(Vector3(0.0f, 5.0f, 0.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['A'])
        cameraNode.Translate(Vector3(5.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['D'])
        cameraNode.Translate(Vector3(-5.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['Q'])
        cameraNode.Translate(Vector3(0.0f, 0.0f, -5.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['E'])
        cameraNode.Translate(Vector3(0.0f, 0.0f, 5.0f) * MOVE_SPEED * timeStep);

    if (input.keyDown['Z'])
        mushroomNode.position = Vector3(0.0f, 0.0f, 400.0f);
    if (input.keyDown['X'])
        mushroomNode.position = Vector3(0.0f, 0.0f, 500.0f);

        if (input.mouseButtonPress[MOUSEB_LEFT])
        {
                My_Click = !My_Click;
                if (My_Click)
                        Clk = 0;
                else
                        Clk = 1;
        }


        if (input.mouseButtonPress[MOUSEB_RIGHT])
        {         
		switch (C1)
		{
			case 1:
				My_Mat.shaderParameters["MatDiffColor"] = Variant(Color(0.0f, 0.0f, 1.0f, 1.0f));
				C1 = 2;
				break;
			case 2:
				My_Mat.shaderParameters["MatDiffColor"] = Variant(Color(0.0f, 1.0f, 0.0f, 1.0f));
				C1 = 3;
				break;
			case 3:
				My_Mat.shaderParameters["MatDiffColor"] = Variant(Color(1.0f, 0.0f, 1.0f, 1.0f));
				C1 = 4;
				break;
			case 4:
				My_Mat.shaderParameters["MatDiffColor"] = Variant(Color(1.0f, 1.0f, 0.0f, 1.0f));
				C1 = 5;
				break;
			case 5:
				My_Mat.shaderParameters["MatDiffColor"] = Variant(Color(0.0f, 1.0f, 1.0f, 1.0f));
				C1 = 6;
				break;
			case 6:
				My_Mat.shaderParameters["MatDiffColor"] = Variant(Color(1.0f, 1.0f, 1.0f, 1.0f));
				C1 = 7;
				break;
			case 7:
				My_Mat.shaderParameters["MatDiffColor"] = Variant(Color(1.0f, 0.0f, 0.0f, 1.0f));
				C1 = 1;
				break;
		}		
        }
}

void SubscribeToEvents()
{
    SubscribeToEvent("Update", "HandleUpdate");
}

void HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    float timeStep = eventData["TimeStep"].GetFloat();
    MoveCamera(timeStep);
}


class Rotator : ScriptObject
{
	Vector3 rotationSpeed;
	
	void Update(float timeStep)
	{
		node.Rotate(Quaternion(rotationSpeed.x * timeStep * Clk, rotationSpeed.y * timeStep * Clk, rotationSpeed.z * timeStep * Clk));
	}
}

String patchInstructions = "";

[/code]

-------------------------

rasteron | 2017-01-02 01:15:29 UTC | #3

Hey there,

Afaik Raspberry is still a desktop and a touch pad is not a mouse so maybe Urho3D is detecting it as touch input and you could try and test using Urho3D player and enable touch emulation via command line switch.

[b]-touch [/b]                Touch emulation on desktop platform

see if it works.

Command line switches here..
[urho3d.github.io/documentation/ ... nning.html](https://urho3d.github.io/documentation/1.6/_running.html)
Input Docs
[urho3d.github.io/documentation/ ... input.html](https://urho3d.github.io/documentation/1.6/class_urho3_d_1_1_input.html)

NJSW is also a good example where you can get started using touch input. Hope that helps.

-------------------------

OMID-313 | 2017-01-02 01:15:29 UTC | #4

[quote="rasteron"]Hey there,

Afaik Raspberry is still a desktop and a touch pad is not a mouse so maybe Urho3D is detecting it as touch input and you could try and test using Urho3D player and enable touch emulation via command line switch.

[b]-touch [/b]                Touch emulation on desktop platform

see if it works.

Command line switches here..
[urho3d.github.io/documentation/ ... nning.html](https://urho3d.github.io/documentation/1.6/_running.html)
Input Docs
[urho3d.github.io/documentation/ ... input.html](https://urho3d.github.io/documentation/1.6/class_urho3_d_1_1_input.html)

NJSW is also a good example where you can get started using touch input. Hope that helps.[/quote]

Thanks @rasteron for your reply.

I tried running the game with [b][i]-touch[/i][/b] as the following, but it didn't help.
[code]pi@raspberrypi:~/Urho3D-1.5/build/bin $ ./Urho3DPlayer Data/Scripts/My_Script.as -touch[/code]
Even in touch mode, only the regular mouse emulates as touch input. The T650 touch pad doesn't work.

Any suggestions !?

-------------------------

OMID-313 | 2017-01-02 01:15:29 UTC | #5

[quote="rasteron"]Hey there,

Afaik Raspberry is still a desktop and a touch pad is not a mouse so maybe Urho3D is detecting it as touch input and you could try and test using Urho3D player and enable touch emulation via command line switch.

[b]-touch [/b]                Touch emulation on desktop platform

see if it works.

Command line switches here..
[urho3d.github.io/documentation/ ... nning.html](https://urho3d.github.io/documentation/1.6/_running.html)
Input Docs
[urho3d.github.io/documentation/ ... input.html](https://urho3d.github.io/documentation/1.6/class_urho3_d_1_1_input.html)

NJSW is also a good example where you can get started using touch input. Hope that helps.[/quote]

I tried running the NinjaSnowBar.as both with and without -touch, but no help again.
[code]pi@raspberrypi:~/Urho3D-1.5/build/bin $ ./Urho3DPlayer Data/Scripts/NinjaSnowBar.as[/code]
[code]pi@raspberrypi:~/Urho3D-1.5/build/bin $ ./Urho3DPlayer Data/Scripts/NinjaSnowBar.as -touch[/code]
Again the regular mouse is detected as touch, but the T650 doesn't do anything.

-------------------------

OMID-313 | 2017-01-02 01:15:29 UTC | #6

Some strange mouse-related thing happens too, which might help diagnose the problem!

When I want to run the game, I open a terminal, try to maximize its window, then type the commands, then play the game.
But sometimes during the game, some clicks cause the game to close suddenly and desktop to appear, and then sometimes I see that many terminal windows has been opened while gaming.
Sometimes the game closes and I see absolutely no terminal, even the native terminal that I had typed the commands!!

How can I prevent mouse clicks to happen outside the game environment !?
Is this related to this problem !?

-------------------------

rasteron | 2017-01-02 01:15:29 UTC | #7

I see. Maybe you can check your touchpad if it is completely enabled or supported by running a browser game that supports touch input or any other games or apps that requires it. This way you can isolate your touch pad issue with your rasp pi and Urho3D.

-------------------------

OMID-313 | 2017-01-02 01:15:29 UTC | #8

[quote="rasteron"]I see. Maybe you can check your touchpad if it is completely enabled or supported by running a browser game that supports touch input or any other games or apps that requires it. This way you can isolate your touch pad issue with your rasp pi and Urho3D.[/quote]

Thanks again @rasteron for your reply.

I'm not sure I can find the correct game!
I tested this game: [touchpianist.com/](http://touchpianist.com/) and it works fine.

Would you please recommend a browser game to test this touch pad ?

-------------------------

rasteron | 2017-01-02 01:15:29 UTC | #9

[quote="OMID-313"][quote="rasteron"]I see. Maybe you can check your touchpad if it is completely enabled or supported by running a browser game that supports touch input or any other games or apps that requires it. This way you can isolate your touch pad issue with your rasp pi and Urho3D.[/quote]

Thanks again @rasteron for your reply.

I'm not sure I can find the correct game!
I tested this game: [touchpianist.com/](http://touchpianist.com/) and it works fine.

Would you please recommend a browser game to test this touch pad ?[/quote]

Of course, that would be the Urho3D emscripten demos. :slight_smile:

[urho3d.github.io/web-samples.html](https://urho3d.github.io/web-samples.html)

And here for native apps..
[itch.io/games/free/genre-platfo ... spberry-pi](https://itch.io/games/free/genre-platformer/tag-raspberry-pi)


You could file a github issue if your device really works except Urho3D. Maybe they can look into that and might have some related issue already posted.

-------------------------

OMID-313 | 2017-01-02 01:15:29 UTC | #10

[quote="rasteron"]
Of course, that would be the Urho3D emscripten demos. :slight_smile:

[urho3d.github.io/web-samples.html](https://urho3d.github.io/web-samples.html)

And here for native apps..
[itch.io/games/free/genre-platfo ... spberry-pi](https://itch.io/games/free/genre-platformer/tag-raspberry-pi)


You could file a github issue if your device really works except Urho3D. Maybe they can look into that and might have some related issue already posted.[/quote]

Thanks for the links @rasteron.

I tried these games:

- Minecraft Pi (installed on Raspbian by default) -> Touchpad worked as mouse perfectly.
- Python Games (installed on Raspbian by default) -> Touchpad worked as mouse perfectly.
- Urho3D emscripten web samples -> Couldn't load the game! "[i]Exception thrown. See Javascript console[/i]"
- 3D Frog for RPi -> The touchpad didn't work :frowning:

I think the usb touchpad mouse remains at the background, and doesn't come to the game.

-------------------------

rasteron | 2017-01-02 01:15:29 UTC | #11

[quote]
- 3D Frog for RPi -> The touchpad didn't work :frowning:[/quote]

hmm so it's not Urho3D specific.. Try more native apps that you can find, if this is the case then you should also post the issue to pi forums, as it's looking more device or OS related.

-------------------------

slapin | 2017-01-02 01:15:29 UTC | #12

I think this problem happens because Urho3D directly uses /dev/input devices instead of using X11 input on Pi
which leads to events being processed both by X11 and by Urho itself. Please try running without X11.
If that won't help thet it is probably SDL issue or some problem with handling SDL events on Pi.
Additionally the problem might be because touchpad uses absolute events instead of relateive,
but most tablets can be configured to behave like mouse and use relative events.

-------------------------

OMID-313 | 2017-01-02 01:15:31 UTC | #13

[quote="slapin"]I think this problem happens because Urho3D directly uses /dev/input devices instead of using X11 input on Pi
which leads to events being processed both by X11 and by Urho itself. Please try running without X11.
If that won't help thet it is probably SDL issue or some problem with handling SDL events on Pi.
Additionally the problem might be because touchpad uses absolute events instead of relateive,
but most tablets can be configured to behave like mouse and use relative events.[/quote]

Thanks @slapin for your reply.
I tried booting into CLI (text mdoe) which is without X.
But still the touchpad mouse doesn't work during the game.

-------------------------

OMID-313 | 2017-01-02 01:15:31 UTC | #14

One more thing:

I checked /dev/input , and the logitech USB receiver is listed here.

[code]pi@raspberrypi:/dev/input/by-id $ ls

usb-2188_USB_OPTICAL_MOUSE-event-mouse
usb-2188_USB_OPTICAL_MOUSE-mouse
usb-Logitech_USB_Receiver-if02-event-mouse
usb-Logitech_USB_Receiver-if02-mouse
usb-USB_USB_Keyboard-if01-mouse
usb-USB_USB_Keyboard-event-kbd
usb-USB_USB_Keyboard-if01-event-mouse[/code]

-------------------------

OMID-313 | 2017-01-02 01:15:32 UTC | #15

Any suggestions !?

-------------------------

OMID-313 | 2017-01-02 01:15:38 UTC | #16

I found the answer to this problem in the following topic:

[url]http://unix.stackexchange.com/questions/231139/libinput-touchpad-is-dead-around-the-perimter[/url]

[b][i]Summary:[/i][/b]

    1. Create a new file [b]/etc/modprobe.d/hid_logitech_hidpp.conf[/b] and add [b]options hid_logitech_hidpp disable_raw_mode=1[/b] to it.
    2. Power off the host, remove the "unifying receiver" (the little USB dongle) and turn off the T650 (set the switch on the left so that it shows red).
    3. Power on the host and go through the Linux boot process.
    4. Re-insert the receiver and turn the T650 back on.

-------------------------

