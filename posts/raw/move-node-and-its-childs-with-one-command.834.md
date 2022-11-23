syjgin | 2017-01-02 01:03:19 UTC | #1

There are something wrong, when I try to animate my camera: it moves in wrong way. Maybe this takes place because on my move functions I have to move both camera node and separate center node:
[code]
void LevelCamera::VerticalTranslate(float amount)
{
    float currentRot = _cameraNode->GetRotation().YawAngle();
    Quaternion distilledRot;
    distilledRot.FromAngleAxis(currentRot, Vector3(0,1,0));
    Vector3 rotated = distilledRot.RotationMatrix() * Vector3(0,0,amount);
    _cameraNode->Translate(rotated, TS_WORLD);
    _centerPosition->Translate(rotated);
}

void LevelCamera::HorizontalTranslate(float amount)
{
    float currentRot = _cameraNode->GetRotation().YawAngle();
    Quaternion distilledRot;
    distilledRot.FromAngleAxis(currentRot, Vector3(0,1,0));
    Vector3 rotated = distilledRot.RotationMatrix() * Vector3(amount,0,0);
    _cameraNode->Translate(rotated, TS_WORLD);
    _centerPosition->Translate(rotated);
}
[/code]
Maybe I made something wrong in camera moving? I have to remove all angles, except yaw, from camera rotation, because without this camera was moving by local axes, not rotated global: [url=http://rghost.net/8wJ6DDbCf.view][img]http://rghost.net/8wJ6DDbCf/image.png[/img][/url]

-------------------------

Bluemoon | 2017-01-02 01:03:23 UTC | #2

is _cameraNode parented to _centerPosition ?

-------------------------

thebluefish | 2017-01-02 01:03:24 UTC | #3

Moving/Rotating/Scaling a parent node will apply to all of its children. If you are running into problems with it, you're probably using bad hierarchy.

-------------------------

