TikariSakari | 2017-01-02 01:05:36 UTC | #1

Hello, I was wondering if there would be a Text3D object (not ui), that would always point itself towards camera? By this I mean something like if I want to put a name on top of a character or making floating damage numbers from a hit, the text is kind of unreadable from bad angle.

I suppose I could adjust the nodes angle on every single update, but I was wondering if there is a way to combine billboards with Text3D.

edit: This at least works when called on every update, but maybe there are better ones:

[code]
    Quaternion camRot = cameraNode_->GetWorldRotation();
    for(Urho3D::Node* node : textNodes_)
    {
        node->SetWorldRotation( camRot );
    }
[/code]

-------------------------

thebluefish | 2017-01-02 01:05:36 UTC | #2

I would just make a component for that. For example, that's exactly what's being done in my [url=https://github.com/thebluefish/Idler/blob/master/Idler/GameClient/src/Game/UpgradeMachine.cpp]UpgradeMachine component[/url].

-------------------------

TikariSakari | 2017-01-02 01:05:36 UTC | #3

Using components definitely seems smarter way to accomplish this than having to keep a list of nodes which may or may not exist anymore in next update.

-------------------------

JTippetts | 2017-01-02 01:05:36 UTC | #4

Is [url=https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/UI/Text3D.h#L92]Text3D::SetFaceCameraMode()[/url] not sufficient? Options are enumerated in the [url=https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/GraphicsDefs.h#L268]FaceCameraMode[/url] enum, with default of FC_NONE.

-------------------------

TikariSakari | 2017-01-02 01:05:37 UTC | #5

[quote="JTippetts"]Is [url=https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/UI/Text3D.h#L92]Text3D::SetFaceCameraMode()[/url] not sufficient? Options are enumerated in the [url=https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/GraphicsDefs.h#L268]FaceCameraMode[/url] enum, with default of FC_NONE.[/quote]

This definitely seems like what I was looking for. I figured there would be some very simple way to set the rotation according to camera. Thank you for pointing the function out.

-------------------------

