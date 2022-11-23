april_si | 2017-01-02 01:05:51 UTC | #1

Hello, I am artist and trying out Urho Editor.sh

Whenever I select the camera in Editor, a nice view pop in lower right corner and when detected it disappears.
How to do so that it always stays there?

Anyway to pop out the camera view and resize it.

-------------------------

setzer22 | 2017-01-02 01:05:51 UTC | #2

Welcome to Urho3D!  :smiley: 

I'm not able to reproduce that issue as I'm able to see the small camera view, even when manipulating the camera node (moving the camera) the viewport is still there and I'm able to see through the camera. Could you please clarify a bit more what are you doing when the problem occurs, and what exactly do you mean by "when detected"?

-------------------------

amit | 2017-01-02 01:05:51 UTC | #3

I think when camera is deselected the said view disappears. It happens.

-------------------------

april_si | 2017-01-02 01:05:51 UTC | #4

Thanks setzer22, :slight_smile: 

Oops, I meant when I [u]deselected[/u] camera, not detected :blush: 
Whenever I select some other node, the camera view disappears. Just want to keep it up while I set the scene.

-------------------------

setzer22 | 2017-01-02 01:05:52 UTC | #5

I'm afraid that's the intended behaviour of the Editor. Bear in mind that the editor is still far from production-ready, and you might not find all the desired features in it. Even though it's a great tool for most use cases IMO.

That being said, It wouldn't be difficult to come up with a quick hack in order to display a camera on the screen as a separate viewport without even touching the editor code, just by adding a component to the camera node. I'm also interested and I was working on something very similar just the other day, so I'm going to give it a try and post it here if I manage to do it.

Also, if you want, you can open a new thread in the Feature Request section, and ask for this feature to be included in the editor!

-------------------------

weitjong | 2017-01-02 01:05:52 UTC | #6

I agree with what setzer22 has said. But I want to add that currently the provided Editor is already capable to display multiple viewports. At the moment, the camera's properties have to be manually adjusted. It should not be difficult to script that the viewport can be 'stick' to or associate to another camera component and therefore render from its point of view.

-------------------------

april_si | 2017-01-02 01:05:52 UTC | #7

[quote="setzer22"]just by adding a component to the camera node[/quote]
What component is to be added to it and how.
But on the same thought train I was able to achieve some success. I just selected the camera and not the parent node, this displayed the viewport.
Then I "ctrl" selected the node of the mesh to be moved/rotate/scale, now node transformation only applies to selected nodes not the selected camera  :sunglasses: .
(Is that what you were saying setzer..)
... Thanks

I am able to do what i want but, would want some more non-hackish way.

I do not know much of coding, but can understand and do some changes  :neutral_face:  if I know where to do so. Ill try take some help.

The Editor a great tool, and my work tool in urho sphere, few stuff like applying standard materials could be more intuitive and of course sticky camera, but still given urho's team size it still well thought of, like pick light|geometries|... and fill point|wire|geometries options.

-------------------------

april_si | 2017-01-02 01:05:52 UTC | #8

Ok ....
in file EditorView.as added slashes at line 663
        //if (renderer.numViewports > viewports.length)
        //    renderer.numViewports = viewports.length;
it work for now
Hope this has no errors,
Any more would require more work i suppose.

-------------------------

setzer22 | 2017-01-02 01:05:52 UTC | #9

[quote="april si"][quote="setzer22"]just by adding a component to the camera node[/quote]
What component is to be added to it and how.[/quote]

The component I was talking about is not done. I was talking about doing it myself. It's still a bit hackish but way more functional than Ctrl-Clicking that way. The workflow would basically be adding a component to the camera node which then would display said camera in a region of the screen (and you'd be able to define that region through the Component's attributes). It's really quick to do, and in fact I was working on a very similar thing just yesterday, but somehow the editor was preventing me to add more viewports to the renderer.

[quote]
Ok ....
in file EditorView.as added slashes at line 663
//if (renderer.numViewports > viewports.length)
// renderer.numViewports = viewports.length;
it work for now
Hope this has no errors,
Any more would require more work i suppose.[/quote]

And it seems you just have found the line responsible for that! I'm going to have a look now and see if I can code something quick, brb.

-------------------------

setzer22 | 2017-01-02 01:05:52 UTC | #10

Just as I thought, the lines you commented out were responsible for hiding the camera once un-selected. By removing those, the viewport is never removed and you'll always see the last camera you clicked. 

That's a workaround and it works, but it's not a proper fix, because each time you select the camera (or a different one), a new viewport is created on top of the other one, so you'll end up with lots of viewports and that would eventually slow up the editor. 

Without removing those lines, the problem is the editor removes all the viewports the user might have created so my component won't work until this is fixed. 

For now having those lines removed allows for the functionality you needed so until there's a fix it should be ok to do that. It would take a while until you notice a substantial slowdown anyway, but bear in mind that performance might degrade.

Anyway, I've made a small script that draws a viewport with the camera it's attached to anywhere on the screen. That would allow for more functionality like dislpaying the contents of multiple cameras if needed, and allow the user to customize the size of the viewport as well. Once I find a fix for this I'll post it on the Code Exchange section of the forum! For now I guess the workaround is good enough?

-------------------------

april_si | 2017-01-02 01:05:53 UTC | #11

Thanks for all the help ...
I would not be able do anything more even if I want to.
This was lucky too ... I saw EditorView.as in editor.as, looked in to file, luckily found the function and removed the ones which were hiding the viewport.
I was thinking to change "selectedComponents" with allComponents, but did not know where allcomponents are .. I even don't know what language it is  :smiley: 
I think I should focus on art.

Should i request this feature from Urho team?

Thanks again for helping me out, this really helped my workflow.

-------------------------

setzer22 | 2017-01-02 01:05:53 UTC | #12

The problem with changing selectedComponents with all the components in the scene would be that if more than a camera is present in the scene, only the first would ever get drawn.

The editor is written in AngelScript, it's a scripting language with a C++-like syntax that's used in Urho.

You can make a feature request for this. Having a way to keep the last selected camera shouldn't be difficult to fix. Maybe a better (but also more difficult) way of implementing the feature could be something like: 
right click on camera -> View in window -> A UI window pops up with the camera view and you can move it and resize it.

-------------------------

april_si | 2017-01-02 01:05:54 UTC | #13

[quote="setzer22"]right click on camera -> View in window -> A UI window pops up with the camera view and you can move it and resize it.[/quote]
sounds nice.

Ill request a feature sometime soon, for the same. This is feature that would help a lot.

Thanks

-------------------------

