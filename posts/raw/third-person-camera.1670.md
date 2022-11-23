bmcorser | 2017-01-02 01:09:24 UTC | #1

Hello everyone,

First post on the Urho3D forum!

I found a video on YouTube showing a third person camera controlled by the mouse (can't post the link in my first post). It looks like exactly the type of thing I'd like to start with, but couldn't find the source code anywhere. Anyone know where I can get hold of the source?

Greets,

Ben

-------------------------

bmcorser | 2017-01-02 01:09:24 UTC | #2

Second post might let me post a link?
[youtube.com/watch?v=iK2jCrGjabY](https://www.youtube.com/watch?v=iK2jCrGjabY)

-------------------------

1vanK | 2017-01-02 01:09:24 UTC | #3

[github.com/MonkeyFirst/FH/blob/ ... Camera.cpp](https://github.com/MonkeyFirst/FH/blob/master/Featheredhat/ThirdPersonCamera.cpp)

-------------------------

bmcorser | 2017-01-02 01:09:24 UTC | #4

Ah, awesome. Thanks 1vanK.

-------------------------

jmiller | 2017-01-02 01:09:25 UTC | #5

[b]JTippets' Demo and explanation of Third Person Camera[/b]

For Urho3D, written in Lua, but not hard to translate to C++ (I have done one based on this)

[gamedev.net/blog/33/entry-22 ... on-camera/](http://www.gamedev.net/blog/33/entry-2259326-demo-and-explanation-of-third-person-camera/)

-------------------------

bmcorser | 2017-01-02 01:09:29 UTC | #6

That looks really interesting, carnalis, thanks for pointing me there.

My intention is to be able to switch targets; it's mentioned in the post that some extra work would need to be done for that.

[quote]
 ... each controller [would] need to have an active flag, and some means for specifying which camera controller is active at any given time. It might also need additional functionality for handling hard camera position setting in the case of soft camera tracking 
[/quote]

The obvious way to achieve this would be using the events system; where an event such as "RequestCameraControl" would be fired by the object that wants to have camera "focus", then some logic in the camera would decide firstly whether to look at the thing requesting "focus" and secondly how to smoothly transition from current target to next target.

Am I on the right track?

-------------------------

jmiller | 2017-01-02 01:09:29 UTC | #7

Seems like you have a firm grip on the concepts, and that seems like a good track. Lot of ways to do something..

Note the controllers shared by JTippets and MonkeyFirst (much like mine :smiley: ) have a 'springtrack' setting (see SpringPosition()) that causes the camera to smoothly 'lerp' to new positions.

For camera focus, here's a simple component that uses the CameraController.
It's not necessarily the most efficient or flexible, but it is dead easy (just add/remove from nodes) and would fit neatly in the CameraController header.

[code]
class CameraFocus : public Urho3D::Component {
URHO3D_OBJECT(CameraFocus, Urho3D::Component);

public:
  CameraFocus(Urho3D::Context* context): Urho3D::Component(context) { }
  ~CameraFocus() { }
  static void RegisterObject(Urho3D::Context* context) {
    context->RegisterFactory<CameraFocus>();
  }

protected:
  void OnNodeSet(Urho3D::Node* node) {
    SubscribeToEvent(Urho3D::E_POSTUPDATE, URHO3D_HANDLER(CameraFocus, HandlePostUpdate));
  }

  void HandlePostUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData) {
    Urho3D::VariantMap& vm(GetEventDataMap());
    Urho3D::Vector3 pos(node_->GetPosition());
    vm[SetCameraPosition::P_POSITION] = pos;
    node_->SendEvent(E_SETCAMERAPOSITION, vm);
  }
};[/code]

edit: and just a reminder to register the Component, like in App constructor
  CameraFocus::RegisterObject(context);

-------------------------

bmcorser | 2017-01-02 01:09:30 UTC | #8

Sweet! I'm sure that will come in very useful.

I found a decent article (from 1998 -- it's practically prehistoric!) dealing with the basic mathematics of quaternions and actually discussing the implementation of a third-person camera ... good stuff.

[gamasutra.com/view/feature/1 ... rnions.php](http://www.gamasutra.com/view/feature/131686/rotating_objects_using_quaternions.php)

-------------------------

