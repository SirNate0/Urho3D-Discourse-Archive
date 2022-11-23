johnnycable | 2018-01-08 15:38:41 UTC | #1

I'd like to manage multigestures, as described [here](http://lazyfoo.net/tutorials/SDL/55_multitouch/index.php). 
Event is: 
> /// Pinch/rotate multi-finger touch gesture motion update.
> URHO3D_EVENT(E_MULTIGESTURE, MultiGesture)
> {
>     URHO3D_PARAM(P_CENTERX, CenterX);              // int
>     URHO3D_PARAM(P_CENTERY, CenterY);              // int
>     URHO3D_PARAM(P_NUMFINGERS, NumFingers);        // int
>     URHO3D_PARAM(P_DTHETA, DTheta);                // float (degrees)
>     URHO3D_PARAM(P_DDIST, DDist);                  // float
> }

so I suppose it's the usual:

> void AnimatingScene::SubscribeToEvents()
> {
> SubscribeToEvent(E_GESTURERECORDED, URHO3D_HANDLER(AnimatingScene, HandleGesture));
> }

and finally:

> void AnimatingScene::HandleGesture(StringHash eventType, VariantMap& eventData)
> {
>     using namespace MultiGesture;
>     
> MultiGesture::P_DDIST pdist = (MultiGesture)eventData[MultiGesture::?????.getSomekindofdata???WTF 
opaquetypes???;
> }

I cannot figure what is the cast exactly and how to relate it to the event data...:crazy_face:
Thank you

-------------------------

Dave82 | 2018-01-08 18:18:18 UTC | #2

[code]
void AnimatingScene::HandleGesture(StringHash eventType, VariantMap& eventData)
{
       int centerX = eventData[P_CENTERX].GetInt();
       int centerY =  eventData[P_CENTERY].GetInt();
       float numFingers =  eventData[P_NUMFINGERS].GetFloat();
       // And so on...
}
[/code]

-------------------------

