lezak | 2018-02-21 22:21:40 UTC | #1

Adding and tweaking post process may be a little pain in the ..., especially when You try to do it by tweaking default values in the xml files, so I've created little component to make it easier:
https://youtu.be/ZvmJGkKKXyI

Here's the code:
https://gist.github.com/lezak/433ec7253b7aba120349fcabd5e36e73

NOTE:
- as for now it supports only Gamma correction, Tonemap and Color correction;
- GetRenderPath function returns only render path from first viewport and this function should be replaced to better fit application specific needs;
- there can be more than 1 component of this type in the scene but only 1 will be active and it will override settings from others - this allows having different setup for different circumstances.

-------------------------

Don | 2018-02-22 05:40:33 UTC | #2

Excellent stuff here! I have always wanted a way to control tone mapping easily in editor.

Regarding your second point, maybe it could look for and cache any cameras it shares a Node with, and then use the first viewport of that camera to apply to. Otherwise, default to first viewport globally. That's just an idea I'm spitballing.

Regardless, great work, and do you have any intention of PRing?

-------------------------

lezak | 2018-02-22 16:58:19 UTC | #3

I don't think it's much of a PR material right now. 
In the next few days I'll try to find some time to add other processes and then try to find better solution for providing path (to be honest i didn't give much thought to this matter - just picked first and easiest option) and Your idea seems quite reasonable.

-------------------------

lezak | 2018-03-10 15:31:20 UTC | #4

I finally sat down to make this thing bit more complete. Right now:
- all effects that come with the engine are supported (and all paramters can be modified);
- order of applying effects can be changed;
- rather then directly modyfing render path, each instant of component stores its own effects  path. This path is appiled to speciefied viewports (multiple viewports are supported). Viewports can be set from code by calling AddViewport(Viewport*, bool) or by index in the renderer subsystem (AddViewportIndex(unsigned, bool)) - in latter case index is serialized and if viewport with given index exists when component is loaded, effects will be applied to it. Second param (bool) allows to remove other viewports (default false). In the editor viewports are assigned by index - this allows, for example, to compare different effects setups by setting split/quad view in editor and assigning different controllers to each viewport. 
Keep in mind that there is no event providing info that a viewport was removed or added to the renderer subsystem, so in this case viewports in component need to be updated manually;
- xml render path file can be provided as input 'base' path. If not provided component will use clonned default path. 
When viewport is removed from the controller (RemoveViewport, RemoveViewportIndex), applications default render path will be applied to it (when controller is removed from a scene path will be applied to all controlled viewports).

One more thing - component assumes that the renderer subsystem exists, so don't create it when application is in headless mode.

(updated code can be found in the first post)

-------------------------

