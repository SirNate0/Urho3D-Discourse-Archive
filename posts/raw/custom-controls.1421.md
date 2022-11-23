sabotage3d | 2017-01-02 01:07:38 UTC | #1

Hi guys,
I have some custom gesture events already setuped. What would be the best way to hook them into a custom control method. 
Currently I have to use: 
[code]void gestureStart(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
void gestureEnd(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);[/code]
I am looking for something similar the way input and controls are working like input->gesture(int action) a combination of both start and end events . I noticed VariantMap extraData_ inside the controls class but I am not sure how to use it properly. Thanks in advance.

-------------------------

cadaver | 2017-01-02 01:07:38 UTC | #2

extraData_ is primarily intended to allow easily transmitting custom controls data for network players. For example it could contain the last selected weapon.

-------------------------

sabotage3d | 2017-01-02 01:07:39 UTC | #3

Thanks cadaver, but how to combine two custom events like getstureStart and gestureEnd into a single function callback like:
[code]if(_inputManager->gesture(SWIPE_LEFT)) jump(); //called inside the player class[/code] At the moment I have to create the event method inside the player class rather than just calling the function directly.

-------------------------

cadaver | 2017-01-02 01:07:39 UTC | #4

You could make your inputmanager class listen to the gesture events, and keep track of which gestures are active in some data structure, for example a map, so that you can implement that gesture() function like you describe.

-------------------------

sabotage3d | 2017-01-02 01:07:39 UTC | #5

Is that what you mean? To create a HashMap like in the Urho3d Input class and send events containing actions as ints to the HashMap and in the player class just to check if the HashMap contains the action int?

-------------------------

cadaver | 2017-01-02 01:07:39 UTC | #6

That could work. You probably have to distinguish between new gestures and ongoing gestures to be able to detect the transition in the player code. Or if the player already knows to e.g. not jump if already jumping, then that isn't necessary.

-------------------------

sabotage3d | 2017-01-02 01:07:40 UTC | #7

One thing though how should I clear the map should I create a third event or I have to keep track of previous event?

-------------------------

