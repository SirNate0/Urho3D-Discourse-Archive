christianclavet | 2017-01-02 01:06:23 UTC | #1

[b]COLLAPSABLE WINDOWS:[/b]
This is one thing the Inspector really need.
Here an example from the web:
[img]http://designingwebinterfaces.com/blog/wp-content/uploads/2009/04/collapsible_panels.png[/img]

When we add a component to a node, the parameter window should be collapsed, and when we want to edit we click on the triangle (other standard behavior is to double click on the title), that will "open" the window full size to change the parameters.

I think it would be possible to add this directly in the editor in .AS (Angelscript), as it could be a button that set the size of the window. But would be time consuming (Not totally sure). If it was a window (option or variant) directly from the engine would be instanced directly with this ability and with no coding. (Min size would be collapsed, and max size would be expanded)

[b]TABBED WINDOWS:[/b]
I think it's the perfect tool to isolate/show specific icons/element of an interface depending of the work we do.
[img]http://www.codeproject.com/KB/dialog/AndLawtabsetdlg/tabsetdlg1.png[/img]
This could be used in the EDITOR to define SUB-MODES of editing: (Here is some examples I'm thinking of)
1- Terrain editor with only the icons tools used in the terrain editing
2- Material Editor, have sections of stuff of shader types, shaders, and post-fx, etc.
3- Particle editing.
4- Cutscene editing, would reveal a timeline and spline controls 
5- Could be used to edit multiple scenes as ATOMIC EDITOR is doing...

[size=150]Editor design suggestions[/size]:
[ul][li]Can the inspector window could be "docked" on the right and not moving? With the current font size of the input text, we have also to expand the window a little as we can't read the data correctly. (Expand the window a little or reduce a little the font size)[/li]
[li]Is there a way to have the background of the editor[u] not being full black[/u] while editing? (Only aesthetic, but I think would make the editor look better)
Here is some example from other software their background is grey while they edit:[/li][/ul]
[b]Unity 3D:[/b]
[img]http://i.ytimg.com/vi/tCic7cp3ghE/maxresdefault.jpg[/img]
[b]Blender:[/b]
[img]http://linux4vjs.net/wp-content/uploads/2013/12/blender.jpg[/img]
[b]Maya:[/b]
[img]http://www.3dtotal.com/admin/new_cropper/tutorial_content_images/1734_tid_mainimage.jpg[/img]

-------------------------

rasteron | 2017-01-02 01:06:23 UTC | #2

Hey Christian,

I did manage to update my old tabbed menu code to work with the latest 1.4 and would be able to submit a pull request if there's some interest with this version. I posted some details and now a video demo here on my [b][url=http://blog.rastercode.com/post/adding-tabbed-menus-in-urho3d-ui-and-editor/]tech blog[/url].[/b]

cheers.  :slight_smile:

-------------------------

weitjong | 2017-01-02 01:06:23 UTC | #3

When we renamed our editor's attribute inspector window as "Inspector", it is easy to see from where we get the inspiration from. The attribute fields are enabled, disabled, or striked-out in the same fashion as Unity3D when multiple items are being selected. Personally I have always wanted to emulate the collapsible "panels" too. It should not be difficult to do as we could reuse the collapse/expand logic available in the ListView class. Having said that, for some reasons I just keep thinking about it instead of doing it.  :wink:  Perhaps, it is because I have made a promise myself not to touch the UI subystem anymore as I have spent too much time on it and there are plenty more other things to learn from Lasse and his engine. If anyone interested in picking this up, I would recommend to study the ListView class closely.

-------------------------

christianclavet | 2017-01-02 01:06:23 UTC | #4

Hi! 

@rasteron: URHO seem quite flexible! I've checked your patch and all is done directly in the editor .as (Angelscript) files! I would perhaps not use tabbed windows with inspector window (perhaps withing but not the whole window), but it show a good example that TAB can be created from scripts without patching the engine.

A good use for your tab, would be to merge the hierarchy and the content browser. The content browser is really nice, but the current layout for me seem a little out of place. I feel it take too much space, a tabbed window with the hierarchy and this browser would perhaps resolve it.  

For the collapsible windows, the layout would need a "signal" that it must be refreshed (When one of the element is being collapsed/expanded as the other elements in the layout will need to be repositionned. I'm still studying how the editor is made and checking the examples...

@weitjong: Thanks for the tip!

-------------------------

rasteron | 2017-01-02 01:06:24 UTC | #5

[quote="christianclavet"]Hi! 

@rasteron: URHO seem quite flexible! I've checked your patch and all is done directly in the editor .as (Angelscript) files! I would perhaps not use tabbed windows with inspector window (perhaps withing but not the whole window), but it show a good example that TAB can be created from scripts without patching the engine.

A good use for your tab, would be to merge the hierarchy and the content browser. The content browser is really nice, but the current layout for me seem a little out of place. I feel it take too much space, a tabbed window with the hierarchy and this browser would perhaps resolve it.  

For the collapsible windows, the layout would need a "signal" that it must be refreshed (When one of the element is being collapsed/expanded as the other elements in the layout will need to be repositionned. I'm still studying how the editor is made and checking the examples...

[/quote]

Yep, it just so happens that the 3 windows have the same width that is why it is perfect for the demo. :wink: 

I always do my prototypes through scripting as much as possible to save time and just convert it to c++ when it is really needed.

As for the "signal" thing, it could be the same as saving editor settings like what I did or if you prefer to create sessions so it will just be a per scene basis.

-------------------------

