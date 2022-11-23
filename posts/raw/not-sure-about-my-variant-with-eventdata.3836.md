sirop | 2017-12-12 08:43:01 UTC | #1

Hello.

Suppose I send eventData like:

    void SplineEditor::SendEventIndexSelected(int index)
    {
    using namespace IndexSelected;

    VariantMap& eventData = GetEventDataMap();

    float data[6];

    data[0] = splineVector_[index].x_;
    data[1] = splineVector_[index].y_;
    data[2] = splineVector_[index].z_;

    data[3] = splineOrientVector_[index].x_; // Pan
    data[4] = splineOrientVector_[index].y_;  // Tilt
    data[5] = splineOrientVector_[index].z_;  // Roll

    eventData[P_DATA]= Variant(data);
    SendEvent(E_ITEMSELECTED, eventData);
    }

and process/receive eventData by:

    void Navigation::HandleSplineItemSelected(StringHash eventType, VariantMap &eventData)
    {
    
    uint8_t* data;
    data = (uint8_t*)eventData[IndexSelected::P_DATA].GetVoidPtr();
    float x = *(float*)&data[0];
    float y = *(float*)&data[4];
    float z = *(float*)&data[8];
    float pa = *(float*)&data[12];
    float ta = *(float*)&data[16];
    float ra = *(float*)&data[20];
    
    cameraNode_->SetPosition(Vector3(x,y,z));
    cameraNode_->SetRotation(Quaternion(ta, pa, ra));
    }
    
Especially the lines: 

     eventData[P_DATA]= Variant(data);   

and 

     data = (uint8_t*)eventData[IndexSelected::P_DATA].GetVoidPtr();
are somewhat doubtful for me. May it be that simple?

Thanks.

-------------------------

Dave82 | 2017-12-12 09:54:21 UTC | #2

If you want to send two vectors why not just send two vectors ?

[CODE]eventData["splineVector"] = splineVector;
eventData["splineOrientVector"] = splineOrientVector;
SendEvent(E_ITEMSELECTED, eventData);[/CODE]

and process like this : 
[CODE]
cameraNode_->SetPosition(eventData["splineVector"].GetVector3());
cameraNode_->SetRotation(QUaternion(eventData["splineOrientVector"].GetVector3()));
[/CODE]

-------------------------

sirop | 2017-12-12 10:28:57 UTC | #4

Good. But I am still curious if my approach as in the first post is valid.
We'll check it then with debug statements.

-------------------------

kostik1337 | 2017-12-12 10:38:58 UTC | #5

[quote="sirop, post:1, topic:3836"]
float data[6];
[/quote]

Your data is located on stack and it is "freed" when SendEventIndexSelected method exits. So, if you need to pass it to another method, allocate it on heap with new: float* data = new float[6] and delete[] it when you need.

-------------------------

Eugene | 2017-12-12 10:50:14 UTC | #6

[quote="kostik1337, post:5, topic:3836"]
Your data is located on stack and it is “freed” when SendEventIndexSelected method exits.
[/quote]

`SendEventIndexSelected` is exited after `HandleSplineItemSelected` call, so why not?

-------------------------

kostik1337 | 2017-12-12 11:15:05 UTC | #7

Ah, right, I forgot that method subscribers are called immediately, that should work

-------------------------

sirop | 2017-12-13 15:25:30 UTC | #8

I incline to use your approach as it is more ellegant.

But how does such an event have to be declared?
    
    // if element selection changed:
    URHO3D_EVENT(E_INDEXSELECTED, IndexSelected)
    {
      URHO3D_PARAM(P_DATA, Data);                  
    }
or schould it be smth. like

     URHO3D_EVENT(E_INDEXSELECTED, IndexSelected)
     {
        URHO3D_PARAM("splineVector", Data); 
        URHO3D_PARAM("splineOrientVector", Data);              
     } 
?

Thanks.

-------------------------

Dave82 | 2017-12-13 17:37:42 UTC | #9

Just declare a variant map and add your params to it and finally send it.

void SplineEditor::SendEventIndexSelected(int index)
{
      VariantMap eventData;
      eventData["splineVector"] = splineVector[index];
      eventData["splineOrientVector"] = splineOrientVector[index];
      SendEvent(E_ITEMSELECTED , eventData);
}


and process it in your handler

void Navigation::HandleSplineItemSelected(StringHash eventType, VariantMap &eventData)
{
       cameraNode_->SetPosition(eventData["splineVector].GetVector3());
       Vector3 rotation = eventData["splineOrientVector"];
       cameraNode_->SetRotation(Quaternion(rotation.x_ , rotation.y_ , rotation.z_));
}

-------------------------

