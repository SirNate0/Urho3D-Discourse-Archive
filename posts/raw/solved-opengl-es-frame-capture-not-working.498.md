sabotage3d | 2017-01-02 01:00:53 UTC | #1

Hello ,

I am new to Urho3d I am coming from Ogre3d background. When I run my app on the device with Ogre3d I can see the FPS and I can run the OpenGL ES Frame Capture to Debug any OpenGL calls. I tried the Urho3DPlayer example NinjaSnowWar on the IOS Device but I cannot get OpenGL ES Frame Capture activated nor I can get the FPS showing in Xcode.  

Thanks in advance,

Alex

-------------------------

weitjong | 2017-01-02 01:00:54 UTC | #2

This question has been asked before here: [topic387.html](http://discourse.urho3d.io/t/cant-capure-opengl-es-frame-on-iphone5s/395/1).
I haven't looked at the code, but I guess Urho3D/SDL does not use CADisplayLink or GLKViewController for the OpenGL ES rendering loop as expected by the Xcode instrumentation tool. See the note in here ([developer.apple.com/library/ios ... rview.html](https://developer.apple.com/library/ios/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/ToolsOverview/ToolsOverview.html)) for the feature to work.

-------------------------

sabotage3d | 2017-01-02 01:00:54 UTC | #3

Thanks a lot.
Is there a way to create my own SDL context and pipe it through Urho3D ?
Is there anything similar in Urho3d or it has to be requested ?
With Ogre3D I can do this:

[code]SDL_SysWMinfo systemWindowInfo;
SDL_VERSION(&systemWindowInfo.version);
UIWindow * uiWindow = systemWindowInfo.info.uikit.window;

Ogre::NameValuePairList params;
params["externalWindowHandle"] = Ogre::StringConverter::toString((unsigned long)uiWindow);
params["externalViewHandle"] = Ogre::StringConverter::toString((unsigned long)uiView);[/code]

And then I just create my SDL context.

Thanks,

Alex

-------------------------

weitjong | 2017-01-02 01:00:54 UTC | #4

Urho3D engine also supports external window. Although to my knowledge that option is usually only used when the application uses other windowing toolkit such as Qt. The full list of engine supported initialization parameters can be found here. [urho3d.github.io/documentation/H ... _loop.html](http://urho3d.github.io/documentation/HEAD/_main_loop.html). Still, I don't see how by creating SDL window yourself externally would help. I could be wrong though.

I spent some time to peek into SDL code briefly this morning and interestingly I do see that SDL uses the CADisplayLink for the OpenGL ES rendering loop, so there could be something else or SDL does not do it in a way expected by the tool. Perhaps you can compare how Ogre and Urho/SDL setup the rendering loop for the iOS and see if there are any differences.

-------------------------

sabotage3d | 2017-01-02 01:01:04 UTC | #5

I will be good it is it in the engine itself as I have to do some hacks to make it work.

-------------------------

sabotage3d | 2017-01-02 01:01:10 UTC | #6

Suddenly this work now in the latest Urho3d build not sure if someone changed something .

-------------------------

weitjong | 2017-01-02 01:01:10 UTC | #7

I am not aware of anyone that has made commit specifically to address this issue. But I like those issues that come and go away by themselves  :smiley: .

-------------------------

