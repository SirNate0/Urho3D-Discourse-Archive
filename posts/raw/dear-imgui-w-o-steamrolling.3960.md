Sinoid | 2018-01-24 02:47:18 UTC | #1

While there's been a ton of Dear ImGui implementations created by many, all of those I've seen have employed some degree of steamrolling over the existing UI (ie. new subsystem that doesn't play nice, directly hooking ImGui samples code, etc).

[ImGuiElement Github gist](https://gist.github.com/JSandusky/54b85068aa30390c91a0b377703f042e)

This implementation is as a UIElement that largely plays nice with the existing Urho3D UI, respecting z-order, mouse-mode, touch as left-button, renders through UIBatch, etc. *Cludge hacks* are always demanding fullscreen size (which is pretty much the dear imgui way) and cheating with screen->element coordinates. While multiple instances sort of work (font issues ... debatable), it's not really intended for that or for being a child of anything but the root ... seems to work though. (all the cludge has notes in the sources)

Playing nice with the main UI keeps it handy as a debug tool rather than an outright UI replacement, doesn't mangle the usability of a HUD, legible dev interface without juggling multiple UI skins, etc.

Takes a function pointer or overload to render the UI as well as sends an event. Use from Angelscript is via subscribing to the event and then pumping out stuff.

    // Angelscript code
    ...
    SubscribeToEvent("IMGUIDraw", "HandleIMGUIDraw");
    ...
    void HandleIMGUIDraw(StringHash eventType, VariantMap& eventData)
    {
        // superficially retains the dear imgui API, &inout instead of *s
        // because a window isn't being made it's goes to the automatic "Debug" window
        ImGui::Button("This button added by Angelscript!");
        ImGui::Text("This text came from angelscript too!");
        ImGui::ColorEdit3("Color Editor", imButtonColor);
        ImGui::ColorButton("Colors", imButtonColor);
        
        if (testStrArray.length == 0)
        {
            testStrArray.Push("Roger");
            testStrArray.Push("Moore");
            testStrArray.Push("Timothy");
            testStrArray.Push("Dalton");
        }
        ImGui::Combo("Testing this out", comboIdx, testStrArray);
    }


<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/9/9adbeea203c39988262930cb3fd19d3252ce68ca.png'>

Angelscript bindings are ~90%, most of what's missing are flags in the `Begin__XXX__` functions and varargs *fun*, note the use of a namespace so it's still `ImGui::Text()` in Angelscript. C++11 required for the bindings as that's how I had the robot spit everything out from the imgui headers.

No lua-bindings as the amount of pass by pointer/ref involved isn't something Lua's type-system can cope with - without pumping a ton of multi-valued returns or tables+keys (messy either way).

-------------------------

slapin | 2018-05-05 12:14:09 UTC | #2

Hi all!

As this implementation is nice, a problem with it is that it is not possible to SetCullMode(CULL_NONE) per batch, so it is hard wired to CULL_CCW in UI.cpp, which prevents some ImGUI parts (like text cursor) from drawing. Is it possible to avoid Urho modification in this  case and set culling somewhere within UIElement? I wonder...

-------------------------

slapin | 2018-05-05 14:35:30 UTC | #3

I wonder what is easier - to convert ImGui vertex buffer to some proper winding or to disable culling
in Urho3D for UI. I tould be much easier if Urho supported culing control from user code... I don't want to support local Urho patches...

-------------------------

slapin | 2018-05-06 03:31:53 UTC | #4

Resolved this temporarily by applying vertices in both winding orders, which is big overhead, but makes GUI look good.

-------------------------

Lumak | 2018-05-06 04:17:50 UTC | #5

I thought you can just change the UI technique -- **CoreData/Techniques/BasicVColUnlitAlpha.xml** and add no cull there. UI elements are all quads so you shouldn't get any performance loss.

edit: oh wait, UI fetches shaders, not technique, then maybe you can change this line to CULL_NONE:
[code]
    graphics_->SetCullMode(CULL_CCW);
[/code]

-------------------------

slapin | 2018-05-06 04:36:56 UTC | #6

Well, it is what I call "hardwired", I work using separate tree to avoid patching Urho,
so it is easier for me to do updates and avoid sending PRs completely.
With change like this I will have to support patch which will never end-up upstream,
which is not good... So I look for some alternative solution...

-------------------------

Lumak | 2018-05-06 06:34:23 UTC | #7

Ah, Ok. I thought you had made changes to the UI already, but I get that you made changes to the imgui code. But I wonder if setting *graphics_->SetCullMode(CULL_CCW)* is even necessary. I guess it'd make sense if you're rendering 3D models.

-------------------------

slapin | 2018-05-06 06:01:20 UTC | #8

Well, with such things I will not be happy changing one hard wired value to another - who knows what will break?
If I pass uibatch data twice, it is ovehead, but not actually much, I get serious frame drop,
but nothing too hard for the application I do now. I use ImGui for tools and stock widets for end-user interfaces, so unless I end up with 1-2 fps I can manage with current solution.

However if there is some better way I willbe more than happy to go that way as I have uneasy feeling of CPU cycles being wasted for nothing.

-------------------------

Lumak | 2018-05-06 12:39:25 UTC | #9

You can check the crossproduct of the 3 verts of the 1st triangle of the quad to determine whether z term points in or out. Form a Vector3 from the x,y term with z=0 and (v1-v0)).CrossProduct(v2-v0) should give you the z result.

-------------------------

