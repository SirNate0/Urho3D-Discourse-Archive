jjy | 2017-01-16 11:54:02 UTC | #1

After upgraded to 1.6, the UI texts in the editor becomes very small. Is there any settings for this?

If I start it with fullscreen mode, the screen turn black and shows nothing. 

Urho3d 1.6 master + macbook pro retina + macOS 10.12.2

Thanks

-------------------------

hdunderscore | 2017-01-16 12:49:24 UTC | #2

Just to clarify, are you using the latest github version?

-------------------------

jjy | 2017-01-16 13:43:37 UTC | #3

Yes, I cloned the master branch yesterday.

-------------------------

cadaver | 2017-01-17 09:29:19 UTC | #4

UI subsystem has SetScale() / scale property, which can be used to globally scale the UI size. However I wouldn't be surprised if there's editor code that can't tolerate it being anything than 1 (due to direct calculations from graphics width/height)

For general usability, if we don't have active developers with Retina displays who could fix Retina-related things, it might be better to revert the engine to not use high DPI mode by default.

-------------------------

weitjong | 2017-01-17 14:21:18 UTC | #5

I may have way to simulate Retina display using AppleTV simulator. But I agree with your point. Will revert back if we cannot fix it soon. 

I have actually hinted quite a few number of times that we need hardware donation to test some of the platforms, but it looks like I have to say it out loud. :grin:

-------------------------

godan | 2017-01-17 15:59:35 UTC | #6

Not sure how this works with the latest code, but this what we use to find a decent UI scale in HDPI mode:

    void BasicApp::SetUIScale()
    {
    	float a, b, c;
    	SDL_GetDisplayDPI(0, &a, &b, &c);

    	//get current window size
    	Graphics* g = GetSubsystem<Graphics>();

    	// check to see if we should scale based on windowsize : drawable size ratio
    	// only relevant for OSX Retina displays?
    	SDL_Window* curwindow = g->GetWindow();

    	int gl_w, gl_h;
    	SDL_GL_GetDrawableSize(curwindow, &gl_w, &gl_h);

    	int sdl_w, sdl_h;
    	SDL_GetWindowSize(curwindow, &sdl_w, &sdl_h);
    	float multiplier = 1.0f;
    	if (sdl_w != 0)
    		multiplier = gl_w / sdl_w;

    	int realDPI = multiplier * a;
    	float scale = Max(0.33f * (realDPI / 48.0f), 1.0f); //0.33f and 48 are magic numbers here..

    	UI* ui = GetSubsystem<UI>();
    	float curScale = ui->GetScale();
    	if (Abs(scale - curScale) > 0.001f)
    		ui->SetScale(scale);
    }

-------------------------

jjy | 2017-01-18 00:15:57 UTC | #7

I tried to set ui.scale larger than 1. The UI is scaled globally. But text boxes and buttons can not respond accurately on clicking.

-------------------------

weitjong | 2017-04-14 10:57:35 UTC | #8

I suppose you were using 1.6 still when trying this. Lasse has made changes in the master branch around the same time you reported your issue in January. So, you might want to pull the latest code from the master branch and retest on that. And the reason I resurrect this discussion because I need your help to test whether it is better to just 2x the UI or use the input scale itself as the multiplier. Of course other who has Retina display or 4K display can report your test result. Thanks in advance.

-------------------------

johnnycable | 2017-04-14 12:12:25 UTC | #9

Hello, I have Mac and can do some testing, but I don't know Urho very well and I need directions.
What is the procedure for scale UI * (some magnifying factor) in the editor?
What piece of code to modify for auto calculate (like in godan example?)
Thanks

-------------------------

weitjong | 2017-04-14 14:17:12 UTC | #10

Just build from source using the latest master branch. Editor will auto scale up the UI on Retina display. See the change in the Editor.as. If need to, you can try to use the "Ceil(input.inputScale.x)" or "Ceil(input.inputScale.y)" instead of constant 2 multiplier on line 66, and see which works the best.

-------------------------

johnnycable | 2017-04-14 16:00:38 UTC | #11

Ok. Forgot to mention an obvious problem: on retina displays, resources needs to be scaled by 2x, 3x, to account for more density. That means, 2d raster resources in Data/CoreData used by the editor.

-------------------------

weitjong | 2017-04-14 16:40:50 UTC | #12

Although I would agree that we should probably have UI@x2.png or something like that, but I don't think it is that important in this test. And I am not an artist nor UX designer. Contribution is welcome.

-------------------------

johnnycable | 2017-04-14 19:08:40 UTC | #13

Ok. First things first. git clone --recursive https://github.com/urho3d/Urho3D.git. Created a build dir into the dir, cmake_xcode.sh build, opened xcode project file, cmd-B build, cd build/bin, ./Editor.sh:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/ec1cd4751bfacc093d11aa103419d18e4abaa885.png" width="690" height="431">
everything looks normal.
While other examples show tiny resources:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/9938c76b543a128db6ee0be3ab0c5a9c96148bce.png" width="690" height="419">
I have build without particular options, so this should be release mode, right?
I'm gonna try debug next.

-------------------------

weitjong | 2017-04-15 02:20:28 UTC | #14

Thanks for testing. This discussion is about "Editor on retina display". We still need a lot more work for other areas.

-------------------------

johnnycable | 2017-04-17 09:18:40 UTC | #15

Here's example 24 with 2x (128x128) magnified asset (star) and normal coin.
@2 assets appear to look ok on os x, at least at first sight...
Used imagemagick with: convert <resourcename> -resize 128x128 <resourcename>

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/6021f87b5f41caf8ae465bb3906f2a4ebfc55c3a.png" width="666" height="500">
 
I tried to add a sprite to the editor to double check, but when I point and click the attribute inspector, it loses focus and no input is possible. Checked on 2d + sprite and UI element, nothing is editable.That is editor in Head on os x is not usable atm...

-------------------------

weitjong | 2017-04-17 10:27:22 UTC | #16

You are confusing me. Is the mouse clicking issue exist on Retina display as it is?

-------------------------

johnnycable | 2017-04-17 12:39:22 UTC | #17

I don't know. In 1.6 stable version, editor works fine, no clicking issues; examples show resources in correct density/resolution. 
Head version, which I downloaded for this test, shows the aforementioned problems with density regarding examples; but I wasn't able to try in editor, because I cannot create a sprite or an UI element, for instance, because of clicking issue.
Hope it is clear. I cannot tell you if the clicking issue is tied to retina display in particular, but I guess not, because every other part of the editor appears to be ok...

-------------------------

weitjong | 2017-04-17 13:32:23 UTC | #18

Again, thanks for your time. It is sad to hear that. It means we still have hit test issue on retina display when the UI is scaled. Please note that none of the core devs have retina display to actually test our work. The best I could do was just try to simulate a condition in a simulator where the back-buffer and the screen size differed and the input scale start to kick in and the UI in the editor doubled up its size. In my simulated test, I didn't have any hit test issue with my mouse. Probably I was testing in a region closer to the top left corner of the UI, and possibly the hit test issue only manifested itself on the far right region (like where the inspector window located).

Here is the thing. We actually need developer(s) who has the time and the capability to test and fix whatever the remaining problem(s) we may have in order to make our Editor usable on Retina display. If we don't have this fix in time, Lasse may advocate to have the Retina display support disabled by default on the engine side before releasing 1.7. This means the engine would treat your expensive retina display like the yesteryear display and render everything using lower resolution than it capable of (like the way in 1.6 was). I don't want to see that happens but it is not my choice. I already tried to buy the time.

-------------------------

johnnycable | 2017-04-17 16:49:44 UTC | #19

Let me know if you still need help.

-------------------------

