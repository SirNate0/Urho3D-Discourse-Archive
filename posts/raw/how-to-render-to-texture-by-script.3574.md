WangKai | 2017-09-17 13:12:01 UTC | #1

I've been trying to create preview image for every reource in the editor: 
https://discourse.urho3d.io/t/quick-expriment-on-editor/3571

Rendertarget is needed to generate the preview image for model/material... However, it seems that I need to wait for the next frame to get the texture ready. Is there a way to get the render result immediately? (Maybe engine->Update/engine->Render will work, which I haven't tryied. But they cannot be called from script) If so, we could add such a function to the View3D.

Edit: BTW, Constructing a `Scene` object in `ResourceBackgroundLoaded` event handler will result addref related crash which is very strange..

Thanks.

-------------------------

Eugene | 2017-09-17 14:41:38 UTC | #2

[quote="WangKai, post:1, topic:3574"]
Maybe engine-&gt;Update/engine-&gt;Render will work
[/quote]

I used View::Render.

[quote="WangKai, post:1, topic:3574"]
Edit: BTW, Constructing a Scene object in ResourceBackgroundLoaded event handler will result addref related crash which is very strange…
[/quote]

Stack and/or STR?

-------------------------

WangKai | 2017-09-19 02:08:15 UTC | #3

Call Stack:

![crash|681x438](upload://9GTUhi4nYtGCM2yMZLvR8gO0Q31.png)

----------
Script code:

    // called from HandleResourceBackgroundLoaded
    Texture@ TakePhoto(Model@ model)
    {
        Scene@ previewScene = Scene("previewScene"); // crash happens, I cannot create Scene here
        
        // this can work, previewScenes are pre-created in initialization phase
        //Scene@ previewScene = previewScenes[scene_index++];
        
        // ...
    }

-------------------------

Eugene | 2017-09-19 07:26:03 UTC | #4

Well, scene doesn't have constructor from string.

-------------------------

WangKai | 2017-09-19 07:40:01 UTC | #5

Yes, it has.

    
    RegisterNamedObjectConstructor<Scene>(engine, "Scene");



----------

    /// Template function for registering a named constructor for a class derived from Object.
    template <class T> void RegisterNamedObjectConstructor(asIScriptEngine* engine, const char* className)
    {
        String declFactoryWithName(String(className) + "@+ f(const String&in)");
        engine->RegisterObjectBehaviour(className, asBEHAVE_FACTORY, declFactoryWithName.CString(), asFUNCTION(ConstructNamedObject<T>), asCALL_CDECL);
    }

-------------------------

Eugene | 2017-09-19 07:52:36 UTC | #6

Yeah, I missed it... I mean, try not to use it.
I have no idea why it crashes, however.

-------------------------

WangKai | 2017-09-19 08:05:42 UTC | #7

Yes, it's annoying. I have no idea till now. So I have to work around, dirty...:sweat_smile:
        
    PreviewRenderer@ GetFreePreviewRenderer()
    {
	    for (uint i = 0; i < previewRenderers.length; ++i)
	    {
            PreviewRenderer@ renderer = previewRenderers[i]; 
            if (renderer.state == PREVIEW_FREE)
                return renderer;
	    }

	    return null;
    }

-------------------------

Eugene | 2017-09-19 08:15:31 UTC | #8

Scene has default ctor that works perfercty. Also, you may just wait until I merge the fix.

-------------------------

Eugene | 2017-09-20 16:44:23 UTC | #9

[quote="WangKai, post:1, topic:3574"]
Edit: BTW, Constructing a Scene object in ResourceBackgroundLoaded event handler will result addref related crash which is very strange…
[/quote]

Shall be fixed now..

-------------------------

WangKai | 2017-09-21 02:18:11 UTC | #10

Thank you Eugene. That's nice :)

-------------------------

