lexx | 2017-01-02 00:59:48 UTC | #1

How to draw a line   (x1,y1 to  x2,y2)  ?

-------------------------

jmiller | 2017-01-02 00:59:49 UTC | #2

Hi lexx,

So far, I see this but have not used it:
[code]PhysicsWorld2D::DrawSegment(const b2Vec2 &p1, const b2Vec2 &p2, const b2Color &color)[/code]
[urho3d.github.io/documentation/a00270.html](http://urho3d.github.io/documentation/a00270.html)

-------------------------

Mike | 2017-01-02 00:59:49 UTC | #3

You can draw lines using DebugRenderer, check example 15_Navigation, some lines and boxes are drawn for the path (see HandlePostRenderUpdate() function).

-------------------------

lexx | 2017-01-02 00:59:49 UTC | #4

Thanks guys, will check these asap. Not for debugging purposes but lines are lines


[edit]
Ok, checked those and these uses DebugRenderer, and so do I.
[code]
init:
	scene_->CreateComponent<DebugRenderer>();

update():
   ...
	DebugRenderer* debug = scene_->GetComponent<DebugRenderer>();
	debug->AddLine(Vector3(0, 0, 0), Vector3(mx, my, 0), Color(1, 1, 1, 1), false);
[/code]

-------------------------

