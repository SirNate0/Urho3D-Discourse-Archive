TikariSakari | 2017-01-02 01:06:50 UTC | #1

Hello, I've tried to create few UI-windows for now, and there is one thing that I haven't really been able to find in the editor. What I think it is truly missing is the ability to move uielements up/down. Basically lets say that you make element and set the layoutmode to vertical. Now you create several elements inside the element that has layoutmode. Then you realise that one of the elements should actually contain 2 elements, so you add another uielement, but this element gets set to last one on the list. Now to actually get this into correct position, you have to move every single element that is shown before the new element to some other node, and then back to be able to set it to last one on the list.

For creating uis, the editor definitely makes things a lot easier, so I would be grateful for this. 

Something else I've noticed missing from the editor is the ability to hide UI-components. I was thinking that having a checkbox next to the ui-element in the hierarchy window could work. But if I've needed to temporarily move something out the way, I've been changing the position to something out of the screen, so this is workable.

-------------------------

weitjong | 2017-01-02 01:06:50 UTC | #2

For the first question. Is your problem due to the correct parent UI-element is not being selected? If yes then you can first select the correct element by using UI-element picker tool. You can also select the UI-element by highlighting it in the hierarchy window. If, however,  what you want is to change siblings order then you can't do it with drag and drop in the hierarchy window at the moment. What you can do is using cut and paste operations, performing an insertion sort algorithm manually. Easier still, save the layout temporarily and whip out a text editor of your choice to reorder. :wink:

For the second question, hiding the UI. Don't we already have an F12 shortcut for that? Or I have understood you wrongly.

-------------------------

TikariSakari | 2017-01-02 01:06:50 UTC | #3

[quote="weitjong"]For the first question. Is your problem due to the correct parent UI-element is not being selected? If yes then you can first select the correct element by using UI-element picker tool. You can also select the UI-element by highlighting it in the hierarchy window. If, however,  what you want is to change siblings order then you can't do it with drag and drop in the hierarchy window at the moment. What you can do is using cut and paste operations, performing an insertion sort algorithm manually. Easier still, save the layout temporarily and whip out a text editor of your choice to reorder. :wink:

For the second question, hiding the UI. Don't we already have an F12 shortcut for that? Or I have understood you wrongly.[/quote]

Yep the insertion sort algorithm manually thing is exactly what I mean. I was looking for a button that would change the order of siblings without having to either save and manually edit xml-file or drag and drop the objects around to do the "sorting".

[quote="Sinoid"][quote]Something else I've noticed missing from the editor is the ability to hide UI-components. I was thinking that having a checkbox next to the ui-element in the hierarchy window could work. But if I've needed to temporarily move something out the way, I've been changing the position to something out of the screen, so this is workable.
[/quote]

Why don't you just use the existing checkbox for Enable/Disable component on the UI elements you want to hide? Does that not do what's desired?[/quote]
The enable/disable doesn't actually work that way in the engine. Unless you go through the whole hierarchy and disable everything, under the node/uielement, those nodes/uielements that are child to the node, will still be visible/enabled (this also includes 3d-objects/components). There is a function called setdeepenabled that doesn't touch the remembered enable state, so it is less permanently changing the enabled states and then i can reset it with resetenabled.

On the other hand UIElements do have setvisible-function that actually hides the element + all the children of the element. I am not actually sure though if I make 1000 elements, and 999 of the elements are under one UIElement, would this cause performance issues even if those 999 elements are invisible, this is something I probably should test, since I noticed that currently according to the Urhos profiling my RenderUI is actually taking 4-5 ms on 60fps, so it is spending 25% of the frame time for the UI only. It is bit hard to figure out the exact numbers of UI-rendering since the profilers UI takes some time, so unless I actually use the logging to pump some numbers out I cannot really get the correct render time for the UI.

edit: For trying to visualize the enable:
[code]
<Node 1>
    <Node 2>
         <AnimatedMesh>
[/code]
disabling/enabling Node 1 doesn't affect Node 2 at all, so the Animated mesh under Node 2, that is under Node 1 will still be visible / updating animations until you actually disable Node 2. Also on a quick test on the UIElement enabling/disabling single object such as Text doesn't actually affect the visibility at all.

-------------------------

TikariSakari | 2017-01-02 01:06:53 UTC | #4

[quote="Sinoid"]That checkbox (the one to the right of the title ie. "UIELement [ID 13]      [Reset Button][Enable/Disable button]" is bound to "Is Visible" for UIElements, which can be found in AttributeEditor.as - because "Is Enabled" means something entirely else in regards to UIElements. Which is why even though "Is Visible" is an attribute it isn't displayed in the list of attributes, because that checkbox takes over.
[/quote]

Seems that this button works like a charm, and I've completely missed its purpose on the interface. Thank you for this info, it does help me a lot in the future, when I have to dive into doing all those UI-parts for the game (I will need tons of different menus)

-------------------------

