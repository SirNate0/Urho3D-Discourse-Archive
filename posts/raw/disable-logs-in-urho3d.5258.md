lahiruzz | 2019-07-01 13:01:29 UTC | #1

Is there any way to disable the logs in Urho3D ?

-------------------------

Pencheff | 2019-06-27 12:04:36 UTC | #2

[code]
void MyApplication::Setup()
{
    engineParameters_[EP_LOG_NAME] = "";
    ....
[/code]

-------------------------

weitjong | 2019-06-27 14:18:53 UTC | #3

You can also build the engine without logging support at all.

-------------------------

Modanung | 2019-06-28 09:21:52 UTC | #4

Another option seems to be `Log::SetLevel(LOG_NONE)`.

-------------------------

