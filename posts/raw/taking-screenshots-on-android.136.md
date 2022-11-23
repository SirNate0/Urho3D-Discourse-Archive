Mike | 2017-01-02 00:58:18 UTC | #1

Is it possible to take screenshots on Android?

What I want to achieve is:
    - take a screenshot and save it (using the same code as in Sample.lua, but saving to user documents dir)
    - then load/display it on demand

Everything seems to work fine, but I get a black picture when trying to display the saved screenshot.

-------------------------

cadaver | 2017-01-02 00:58:18 UTC | #2

Can you download the image back to your computer and verify whether it has proper content? If it has, then possible problem may be lack of support for non-power-of-two textures.

-------------------------

Mike | 2017-01-02 00:58:19 UTC | #3

I know that non-power-of-two textures are not supported on my device.

EDIT: you're right, this might be a non-power-of-two issue (image size is 1024x564 for a 1024x600 device, I think that bottom black bar is cropped from screenshot).

-------------------------

Mike | 2017-01-02 00:58:20 UTC | #4

Is there a way to 'convert' the screenshot to power-of-two?

-------------------------

cadaver | 2017-01-02 00:58:20 UTC | #5

There is the Image::Resize() function which can be used.

-------------------------

Mike | 2017-01-02 00:58:20 UTC | #6

Resizing performed successfully, thanks for exposing PowerOfTwo functions to lua.
Unfortunately still black picture on Android.

Here is the code used:

[code]
		local screenshot = Image()
		graphics:TakeScreenShot(screenshot)
		screenshot:Resize(NextPowerOfTwo(screenshot.width), NextPowerOfTwo(screenshot.height)) -- 'Convert' to power-of-two
		screenshot:SavePNG(fileSystem:GetUserDocumentsDir() .. "Screenshot.png")
[/code]

-------------------------

