Mike | 2017-11-09 18:25:46 UTC | #1

Enable a simple splash screen displayed during loading time.

[details="LUA"]
In LuaScripts/Utilities/Sample.lua:

Add this line at the beginning of SampleStart() function:
[code]
    SplashScreen() -- Display splash screen
[/code]

Then create new functions:
[code]
function SplashScreen()
    local splashUI = ui.root:CreateChild("BorderImage", "Splash")
    local texture = cache:GetResource("Texture2D", "Textures/LogoLarge.png") -- Get texture
    splashUI.texture = texture -- Set texture
    splashUI:SetSize(texture.width, texture.height)
    splashUI:SetAlignment(HA_CENTER, VA_CENTER)
    engine:RunFrame() -- Render Splash immediately
    SubscribeToEvent("EndRendering", "HandleSplash") -- Keep visible until rendering of the scene
end

function HandleSplash(eventType, eventData)
    -- Remove splash screen when the scene gets rendered
    if ui.root:GetChild("Splash") ~= nil then ui.root:GetChild("Splash"):Remove() end
    UnsubscribeFromEvent("EndRendering")
end
[/code]
[/details]

[details="ANGEL SCRIPT"]
In Scripts/Utilities/Sample.as:

Add this line at the beginning of SampleStart() function:
[code]
SplashScreen();
[/code]

Then create new functions:
[code]
void SplashScreen()
{
    BorderImage@ splashUI = ui.root.CreateChild("BorderImage", "Splash");
    Texture2D@ texture = cache.GetResource("Texture2D", "Textures/LogoLarge.png"); // Get texture
    splashUI.texture = texture; // Set texture
    splashUI.SetSize(texture.width, texture.height);
    splashUI.SetAlignment(HA_CENTER, VA_CENTER);
    engine.RunFrame(); // Render Splash immediately
    SubscribeToEvent("EndRendering", "HandleSplash"); // Keep visible until rendering of the scene
}

void HandleSplash(StringHash eventType, VariantMap& eventData)
{
    // Remove splash screen when the scene gets rendered
    if (ui.root.GetChild("Splash") !is null)
        ui.root.GetChild("Splash").Remove();
    UnsubscribeFromEvent("EndRendering");
}
[/code]
[/details]

[details="C++"]
In Source/Samples/Sample.h

In namespace Urho3D, add:
[code]
class BorderImage;
[/code]
Add to private:
[code]
    void SplashScreen();
    void HandleSplash(StringHash eventType, VariantMap& eventData);
[/code]

In  Source/Samples/Sample.inl:
Includes:
[code]
#include "BorderImage.h"
#include "GraphicsEvents.h"
[/code]

Add this line at the beginning of void Sample::Start()
[code]
SplashScreen();
[/code]

Then create new functions:
[code]
void Sample::SplashScreen()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    UI* ui = GetSubsystem<UI>();
    BorderImage* splashUI = new BorderImage(context_);
    splashUI->SetName("Splash");
    Texture2D* texture = cache->GetResource<Texture2D>("Textures/LogoLarge.png");
    splashUI->SetTexture(texture); // Set texture
    splashUI->SetSize(texture->GetWidth(), texture->GetHeight());
    splashUI->SetAlignment(HA_CENTER, VA_CENTER);
    ui->GetRoot()->AddChild(splashUI);
    GetSubsystem<Engine>()->RunFrame(); // Render Splash immediately
    SubscribeToEvent(E_ENDRENDERING, HANDLER(Sample, HandleSplash)); // Keep visible until rendering of the scene
}

void Sample::HandleSplash(StringHash eventType, VariantMap& eventData)
{
    // Remove splash screen when scene fully rendered
    UIElement* splashUI = GetSubsystem<UI>()->GetRoot()->GetChild("Splash", true);
    if (splashUI)
    splashUI->Remove();
    UnsubscribeFromEvent(E_ENDRENDERING);
}
[/code]
[/details]

-------------------------

weitjong | 2017-01-02 00:58:15 UTC | #2

Thanks for sharing. I just want to point out that the EndRendering event will keep triggering the HandleSplash() event handler unnecessarily after the splash has been removed. It would be better to unsubscribe the event handler afterwards. Also, I would like to point out that the splash will only be rendered [i]after[/i] the Urho3D engine is instantiated and initialized. From the time the app is launched and the engine is initialized, user still sees nothing. In mobile environment, I think using the native GUI for this case is more beneficial. For example, one could use a splash screen activity as the launcher before passing the control to the actual application main activity.

-------------------------

Mike | 2017-01-02 00:58:15 UTC | #3

Thanks for suggestions and insights.

For event handler, is it OK if I unsubscribe at the end of HandleSplash() ?

Can you please elaborate more on the way to switch between activities. Can it be done in lua only or do I need to mix C++ and lua?
Currently I'm using this kind of splash screen in lua to transition between levels, passing the image file to use and a few text lines to SplashScreen().

-------------------------

weitjong | 2017-01-02 00:58:16 UTC | #4

[quote="Mike"]For event handler, is it OK if I unsubscribe at the end of HandleSplash() ?[/quote]

Yes, you can.

[quote="Mike"]Can you please elaborate more on the way to switch between activities. Can it be done in lua only or do I need to mix C++ and lua?
Currently I'm using this kind of splash screen in lua to transition between levels, passing the image file to use and a few text lines to SplashScreen().[/quote]

I think you misunderstood me. Somehow I have forgotten to type that my example in my last post is for Android development environment and so I was referring to the "android.app.Activity" java class. Please see AndroidManifest.xml for more detail. Instead of launching the main activity, one can easily change it to first launch a simple activity that shows a splash for, say, 5 seconds delay or while performing initialization in the background before switching to the actual main activity when it is ready.

For the levels transition, I am ambivalent on either ways since at that point the engine should be anyway ready to render game level loading sequence.

-------------------------

Mike | 2017-01-02 00:58:16 UTC | #5

Ok, thanks, it's good to know of this possibility.

-------------------------

v0van1981 | 2017-01-02 01:02:20 UTC | #6

in C++ sample missing unsubscribe from event

[code]
void Sample::HandleSplash(StringHash eventType, VariantMap& eventData)
{
	UnsubscribeFromEvent(E_ENDRENDERING);
	UIElement* splashUI = GetSubsystem<UI>()->GetRoot()->GetChild("Splash", true);
	if (splashUI)
		splashUI->Remove();
}
[/code]

-------------------------

rasteron | 2017-01-02 01:06:08 UTC | #7

This looks interesting. I'm still a bit rusty with some engine/script code being away for awhile and I'm curious how do you delay the splash screen so it shows up properly with enough time before the game starts. Any ideas?

-------------------------

codingmonkey | 2017-01-02 01:06:10 UTC | #8

>Any ideas?

Somewhere in Application start 
timeToShowScene = time.systemTime+(1000 * secCount)

load and setup splash scene(Scene with orho camera + plane with splash texture) and show it

SplashScreen:: FixedUpdate(time) {
if (timeToShowScene < time.systemTime) 
{
 ShowGameWolrdScene();
}
}

:slight_smile:

-------------------------

rasteron | 2017-01-02 01:06:10 UTC | #9

Thanks codingmonkey for this but I was hoping for an Angel script version..

-------------------------

Miegamicis | 2017-11-08 15:12:27 UTC | #10

Just did the splash screen in Angel script, my code is as following
```
namespace SplashScreen {

    Sprite@ logoSprite;
    Text@ loadingText;
    float opacity; //current opacity
    bool show;
    const float FADE_SPEED = 1.0f; //How fast the logo should fade in and fade out
    bool ended = false;

    Array<String> textures;

    uint currentIndex = 0;

    /**
     * List of all the logos which we need to show in the splash screen
     */
    void InitList()
    {
        textures.Push("Textures/FishBoneLogo.png");
        textures.Push("Textures/UrhoIcon.png");
    }

    void SetTexture()
    {
        Destroy();
        logoSprite = ui.root.CreateChild("Sprite");
        Texture2D@ logoTexture = cache.GetResource("Texture2D", textures[currentIndex]);
        //if (logoTexture is null)
          //  return;

        // Set logo sprite texture
        logoSprite.texture = logoTexture;

        int textureWidth = logoTexture.width;
        int textureHeight = logoTexture.height;

        // Set logo sprite scale
        //logoSprite.SetScale(256.0f / textureWidth);

        // Set logo sprite size
        logoSprite.SetSize(textureWidth, textureHeight);

        logoSprite.position = Vector2(-textureWidth/2, -textureHeight/2);

        // Set logo sprite hot spot
        //logoSprite.SetHotSpot(textureWidth, textureHeight);

        // Set logo sprite alignment
        logoSprite.SetAlignment(HA_CENTER, VA_CENTER);
        //logoSprite.position = Vector2(-textureWidth/2, -textureHeight/2);

        // Make logo not fully opaque to show the scene underneath
        logoSprite.opacity = opacity;

        // Set a low priority for the logo so that other UI elements can be drawn on top
        logoSprite.priority = -100;
        //DelayedExecute(10.0, false, "void SplashScreen::HandleSplashEnd()");

    }

    void SetLoadingText()
    {
        loadingText = ui.root.CreateChild("Text");
        loadingText.text = "LOADING...";
        loadingText.SetFont(cache.GetResource("Font", "Fonts/Anonymous Pro.ttf"), 20);
        loadingText.textAlignment = HA_CENTER; // Center rows in relation to each other

        // Position the text relative to the screen center
        loadingText.horizontalAlignment = HA_RIGHT;
        loadingText.verticalAlignment = VA_BOTTOM;
        loadingText.SetPosition(-20, -20);
    }

    void CreateSplashScreen()
    {
        InitList();
        opacity = 0.f;
        show = true;

        SubscribeToEvent("Update", "SplashScreen::HandleUpdate");

        SetTexture();
    }

    void Destroy()
    {
        if (logoSprite !is null) {
            logoSprite.Remove();
        }
        if (loadingText !is null) {
            loadingText.Remove();
        }
    }

    void HandleSplashEnd()
    {
        Destroy();
        SendEvent("SplashScreenEnd");
    }

    void HandleUpdate(StringHash eventType, VariantMap& eventData)
    {
        float timeStep = eventData["TimeStep"].GetFloat();
        if (show) {
            opacity += timeStep * FADE_SPEED;
            if (opacity > 1.0f) {
                opacity = 1.0f;
                show = false;
            }
        } else if (!ended) {
            opacity -= timeStep * FADE_SPEED;
            if (opacity < 0.0f) {
                opacity = 0.0f;
                currentIndex++;
                if (currentIndex >= textures.length) {
                    ended = true;
                    DelayedExecute(1.0, false, "void SplashScreen::HandleSplashEnd()");
                    SetLoadingText();
                } else {
                    show = true;
                    SetTexture();
                }
            }
        }
        logoSprite.opacity = opacity;
    }
}

```

In your main script call
```
    void Start()
    {
        SubscribeToEvent("SplashScreenEnd", "HandleSplashScreenEnd");
        SplashScreen::CreateSplashScreen();
     }

      ...
      
     void HandleSplashScreenEnd(StringHash eventType, VariantMap& eventData)
    {
         SubscribeToEvent("Update", "HandleUpdate"); //This is important to override SplashScreen subscribed event
         CreateScene();
    }
```

Code is still messy and there's still room for improvements. Basically the splash screen will show all the logos in  the texture array (with fade in and fade out animations) and after that "HandleSplashEnd" event will be called

-------------------------

Modanung | 2017-11-09 18:35:17 UTC | #11

If anyone would like a bigger fishbone logo for this purpose, there's an SVG version available through [LibreGameWiki](https://libregamewiki.org/Urho3D):
[[img]https://libregamewiki.org/images/f/fa/Urho3D.svg[/img]](https://libregamewiki.org/images/f/fa/Urho3D.svg)

-------------------------

