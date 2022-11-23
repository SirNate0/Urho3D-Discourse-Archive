ksmit799 | 2020-03-28 15:07:38 UTC | #1

Hey everyone,

I've looked through a couple of old threads and I'm not entirely sure if the advice in them still stands. I'm wondering if there's a hassle-free way to scale the UI to whatever the window size is in a dynamic way (e.g. someone resizes the resizable window, or goes full-screen). Am I missing a simple setting that I need to enable or is it more complex then that? I know that Unity has the canvas scaler component which uses a reference resolution to automatically scale, but I've messed around with ui.SetScale and I wasn't able to find much success.

Any help would be greatly appreciated!

-------------------------

Modanung | 2020-03-28 15:08:05 UTC | #2

Seems like a duplicate of:
https://discourse.urho3d.io/t/xml-ui-element-relative-sizing/6019

-------------------------

ksmit799 | 2020-04-01 11:30:41 UTC | #3

Thanks for the response, I didn't see that post before I created this one sorry. I was able to achieve what I wanted to do with the following Lua code:

    function ResizeUI()
      local scale = GetScaleFactor(graphics:GetWidth(),
                                   graphics:GetHeight(),
                                   1920, 1080, 0.5)
      ui:SetScale(scale)
    end

    SubscribeToEvent("ScreenMode", "ResizeUI")

Where the GetScaleFactor function is the following (mimicks unity's method of scaling):

    local function GetScaleFactor(width, height, refWidth, refHeight, scaleFactor)
      return math.pow(width / refWidth, 1.0 - scaleFactor) *
             math.pow(height / refHeight, scaleFactor)
    end

However, I'm running into issues when attempting to scale a BorderImage object to match the screen size. The BorderImage is used as a background, and has the same width/height of the UI (ui.root.[width/height]). Is there any way to make an image 'stretch' to always fill the window? I know this behaviour is possible in other engines but I wasn't able to find a function to do it here. Attached is the problem I'm facing, the white area (a BorderImage) should always stretch to fill the screen. Any help would be greatly appreciated.
![UrhoScaleIssue|341x500](upload://3LSdRNtp4fsisQVVuhAM0vO6ZxM.png)

-------------------------

