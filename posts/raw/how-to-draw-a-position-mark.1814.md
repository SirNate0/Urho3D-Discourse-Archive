victorfence | 2017-01-02 01:10:24 UTC | #1

Hello everyone,

I want to draw the position mark as three different colored lines.

I noticed there's a mark inside urho3d editor's viewport:
[img]https://i.imgsafe.org/faca52a.png[/img]

I comment out this line 
CreateGizmo();

The handles removed and this is what I want.
[img]https://i.imgsafe.org/faa40dc.png[/img]

after digging into the codes, I still can't figure out how the lines are drawed. Can you explain a little bit about this?

Thank!!!

-------------------------

victorfence | 2017-01-02 01:10:24 UTC | #2

Ok, I'v got this done, after doing more researching

void HandleUpdate(StringHash eventType, VariantMap& eventData) {
  DebugRenderer@ debug=scene_.GetComponent("DebugRenderer");
  debug.AddNode(scene_.GetChild("cameraNode"),1.0, false);
...

Thanks.

-------------------------

