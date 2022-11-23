TikariSakari | 2017-01-02 01:07:39 UTC | #1

I have been trying to make some ui-windows with urho, and there is one feature with editor I feel like is either missing, or I have just completely missed. Since I have tried to make UI scale according to window size and the game is resizable, I haven't found a way to set the UIElement size as size of the window. So when I am creating the ui-layouts with the editor, I have to manually always set the uielements size, so that I can actually use the horizontal/vertical alignment to correct side/corner of the screen.

If I resize the window size, I actually have to go through all the root elements to set the size of the elements according to the screen size. Now if there was a checkbox for use window screen width/height for uielement, this would actually make a lot of things easier for me, and hopefully for others too who are building UIs with urhos editor.

-------------------------

cadaver | 2017-01-02 01:07:39 UTC | #2

Typically this is something you'd do in code when the game is running. While editing, you should be able to manually resize your layout's root element to test for various sizes, and use the horizontal & vertical alignment on its children (which should be the actual elements with content)

Since there's the menu bar and inspectors etc. I'm not sure if resizing an element to the whole window size is useful while running in the editor.

-------------------------

TikariSakari | 2017-01-02 01:07:39 UTC | #3

[quote="cadaver"]Typically this is something you'd do in code when the game is running. While editing, you should be able to manually resize your layout's root element to test for various sizes, and use the horizontal & vertical alignment on its children (which should be the actual elements with content)

Since there's the menu bar and inspectors etc. I'm not sure if resizing an element to the whole window size is useful while running in the editor.[/quote]

I think you're right, and I think my own problem is mostly due to having too complex hierarchy, and depending too much on the setvisible and thus hiding some uielements depending on the state of the game. For example my ui might look as following during the game play: uiroot->gameplayui->dialogbox->......

I guess the only thing where this might be useful is things like dialogbox, where I would prefer to have full width sized dialogbox, and kinda trust on the automatic layout-engine to do its magic. Although even then I have to manually adjust some of the components.

This is kind of same as with something that I have been cursing on the automatic layout-engine, which is automatically keep things as minimized size. Like for example lets say that I add some stuff on the ui, and the ui grows bigger (during game play), and after deleting something I have to manually set that uielements parent uielement size to 0,0 so that it would automatically resize its size to the minimum size. Maybe it could also be used with horizontal/vertical layoutmode to keep one component at its minimum size, instead of like dividing the whole element size / number of child elements. The minimum size on the other hand might be even more problematic with the use full window width as uielement width option.

-------------------------

cadaver | 2017-01-02 01:07:40 UTC | #4

The layouting does somewhat evil things, as there are cases where it doesn't actually respect the min/max size, unless the element is set to completely fixed size. This should be reviewed / fixed, though the problem may be that in the process a ton of layout related things get broken :slight_smile:

-------------------------

