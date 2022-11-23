ucupumar | 2017-01-02 01:09:21 UTC | #1

Continuing about [url=http://discourse.urho3d.io/t/particle-editor-3d/572/18]my last post[/url] on Particle Editor thread, I think it's better to create new thread specified about direction support of particles/billboard.
I'm experimenting about particle direction inspired by Unity stretched billboard particles. If you have tried that on Unity, stretched particle can create pseudo 3d effect despite still using billboard. It can be really useful for sparking effects and many other stuffs. Here are the screenshots:

[img]http://i.imgur.com/YfbxVsm.png[/img]

And this is what happens if using constant force and setting up direction min and max:
[img]http://i.imgur.com/IR0SQSE.png[/img]

You can see this feature in action on this video:
[video]https://www.youtube.com/watch?v=zR7KtF6qtaU[/video]

About the implementation, I modify the billboard object to store direction. This data only works if new face camera mode FC_DIRECTION is used. If this mode is used, billboard will rotate facing camera with direction as axis, so it will create pseudo 3D effect. Because every billboard has different rotation, Urho needs to calculate rotation for every billboard. For now, CPU is doing those calculation, but I have plan to move them to the GPU.
I have already create [url=https://github.com/ucupumar/Urho3D/tree/particle-editor]a branch on Github[/url] if you want to test it out. It's still only works on OpenGL though. I hope this branch can be merged to the master soon.  :smiley:

-------------------------

Enhex | 2017-01-02 01:09:21 UTC | #2

Nice work!

I was looking for such a feature a while ago. Do want.

-------------------------

1vanK | 2017-01-02 01:09:21 UTC | #3

The particles appear very sharply. Suppose that at the beginning of their size 0. After a while their size to normal. Thereafter, their size stable.

EDIT: Also can be done to length depend on the speed. When a particle is moving vertically upwards at the top it is compressed, and when it falls back down - stretched.

-------------------------

ucupumar | 2017-01-02 01:09:21 UTC | #4

[quote="Enhex"]Nice work!

I was looking for such a feature a while ago. Do want.[/quote]
Thanks dude!  :smiley: 

[quote="1vanK"]The particles appear very sharply. Suppose that at the beginning of their size 0. After a while their size to normal. Thereafter, their size stable.

EDIT: Also can be done to length depend on the speed. When a particle is moving vertically upwards at the top it is compressed, and when it falls back down - stretched.[/quote]
This implementation still haven't done anything related to size. To solve that problem, I think the size variation system of Urho particles need to be revamped. As for now, it can only do add and multiply. 
I actually have plan to do this, but let's see if this particle direction can be merged first.  :slight_smile:

-------------------------

codingmonkey | 2017-01-02 01:09:21 UTC | #5

thanks for sharing this! very interesting stuff)
but in addition I want to mention one common problem of urho's particles - the problem this is named - "Improving fillrate" 
you may look this topic for clarify [opengl-tutorial.org/intermed ... nstancing/](http://www.opengl-tutorial.org/intermediate-tutorials/billboards-particles/particles-instancing/)
[img]http://www.humus.name/Cool/ParticleTrimmer.jpg[/img]
I guess what urho's particle system need add ability to use custom flat model(selected by user) as billboard plane instead usual billboard with is very expensive in fill rate in some cases;

-------------------------

ucupumar | 2017-01-02 01:09:22 UTC | #6

[quote="codingmonkey"]thanks for sharing this! very interesting stuff)[/quote]
You're welcome! :slight_smile:
[quote="codingmonkey"]but in addition I want to mention one common problem of urho's particles - the problem this is named - "Improving fillrate" 

I guess what urho's particle system need add ability to use custom flat model(selected by user) as billboard plane instead usual billboard with is very expensive in fill rate in some cases;[/quote]
Interesting, I think it's possible to implement custom mesh for billboard, but if the submitted model are not flat, it will defy the original purpose of billboard itself. The solution of this would be some kind of automatic optimized flat mesh depending of the texture, like the link you tell us. But in the end, who want to implement this on Urho? :stuck_out_tongue:

-------------------------

ucupumar | 2017-01-02 01:09:22 UTC | #7

The support for DirectX9/11 is done! 
I also added particle example called Burst.xml

[img]http://i.imgur.com/Fk72jgN.png[/img]

You test it using [url=https://github.com/ucupumar/Urho3D/tree/particle-editor]this branch[/url]. 
EDIT: I already create a pull request [url=https://github.com/urho3d/Urho3D/pull/1144]here[/url]
 :slight_smile:

-------------------------

Modanung | 2017-01-02 01:09:22 UTC | #8

Awesome!  :mrgreen:

-------------------------

ucupumar | 2017-01-02 01:09:22 UTC | #9

[quote="Modanung"]Awesome!  :mrgreen:[/quote]
Thanks dude!  :mrgreen: 

I just pushed new commit that move rotation computation from CPU to GPU. Now particle with direction should be give faster performance. 
I tried to input 200k of particles, but I think Urho limit it's particles to only some thousands. Below is screenshot of them.

[img]https://cloud.githubusercontent.com/assets/5253453/12263495/1cbdca1c-b962-11e5-8433-66b8ff010653.png[/img]

Surprisingly, Radeon R9 270x can run it at only 450Mhz clock speed (max speed is 1050Mhz).  :mrgreen:

-------------------------

