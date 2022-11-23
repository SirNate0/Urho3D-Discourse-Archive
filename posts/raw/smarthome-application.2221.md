LotusV | 2017-01-02 01:14:01 UTC | #1

Hi guys. I'm novice in the game developing and also graphics inspite of I have 15 years experience in the .net developing. I would like to create some hobby cross platform application for smarthome. The ToDo list is below:
1. Create interface (Design mode) for loading image as background and construct walls of plan room based on the image plan. This interface should allow to create lines and the vertex, join two vertexes and allow to move them. 
2. Allow in Design mode create and place objects likes light and allow to bind On status URL and Off status Url. The Lights can be simple light which allow On and Off and can be dimmable which also allow Dim and bright commands urls.
3.  Design mode should allow several floors creation.
4. After finishing Design mode should allow serialize plan(s).
5. Runtime mode should deserialize floors from XML 
6. The design of floor should be in 3d mode and allow set the high of walls.
7. The runtime mode should provide interactive scene which should allow select floor, change Viewport of selected scene, allow On, Off, Dim, Bright by the click on the light object and light object should react based on response from Url (that mean if response ok light object should light on, off, dim or bright)

Can someone describe which object can I use in design mode and in the runtime mode? Thanks in advance.
P.S. I'm interesting only in the design objects architecture. The subreoutine procedures like serialize, deserialize, Web request and web response can be ommited. And also I'm plannig to use xamarin platform for developing.

-------------------------

codingmonkey | 2017-01-02 01:14:01 UTC | #2

[quote]which object can I use in design mode and in the runtime mode?
[/quote]
Hi!
I think you may use this in runtime:
[urho3d.github.io/documentation/ ... metry.html](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_custom_geometry.html)

Or even, you may feed the batches in own component based on Drawable, of course only if UrhoSharp allow this

-------------------------

