Dave82 | 2019-12-14 20:22:22 UTC | #1

Hi ! I have added extra commands to the default renderpath like this :
[code]
<renderpath>
    <command type="renderui"/>
    <command type="clear" depth="1.0" />
    <command type="scenepass" pass="ontop"/>
</renderpath>
[/code]
This way i can render certain models on top of UI elements (showing 3d models inside inventory) So every model which technique has a "ontop" pass defined will be rendere after the ui. The only problem with this is only renders the models bland , (diffuse only ,since it is a scenepass). How could i expand to have specular , normal and light pass after "renderui" ? I could just copy the whole  Forward renderpath after this command but that would render again everything twice. 

Is there a way to have a post UI render path but to filter which models to render ?

-------------------------

SirNate0 | 2019-12-15 00:44:33 UTC | #2

I don't have a solution to your problem, that will have to come from others, as I have very little experience with the render path. I can suggest an alternate way to accomplish (likely) what you are trying to do, though: render the models to a texture and then display those images in the UI.

-------------------------

dev4fun | 2019-12-15 03:07:58 UTC | #3

Why not Render to Texture?

-------------------------

Dave82 | 2019-12-15 10:23:45 UTC | #4

In case theres no other solution i will use rtt. Thinking about this problem and reading the documentation i had an idea : Maybe i could do the opposite ? Render the ui on top as usual and when i show the inventory just render the UI before the 3d models. So let me rephrase the question :
Is there a way to turn on and off various commands in the renderpath ?

EDIT : 
OK i have some progress : tagging "rederui" commands in the renderpath as "postUI" and "preUI" and then enable/disable them to achive the desired effect solves the problem. I wonder are there any drawbacks or price to pay for this extremely easy and trivial solution...

-------------------------

tarzeron | 2019-12-15 11:38:51 UTC | #5

`Not
sure, but maybe you can try rendering scene to View3D and adjust the
transparent background.`

`In` `RenderPath ToggleEnabled ` `for` enabled state of commands and rendertargets by tag.

https://urho3d.github.io/documentation/1.7.1/class_urho3_d_1_1_render_path.html#a3ba2427a6feed595ac675e060be2f55e

`And
check this demo`

https://github.com/urho3d/Urho3D/blob/master/Source/Samples/48_Hello3DUI/Hello3DUI.cpp

-------------------------

Dave82 | 2019-12-15 13:57:06 UTC | #6

Wow. i wasn't aware of the 3d UI component. I didn't tried the latest master in a long long time (i was happy with the 1.7) 
Definitely trying this out.

-------------------------

