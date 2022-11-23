victorfence | 2017-01-02 01:06:21 UTC | #1

Hello Everyone,

I have write something to try to define a object type as object handel type:

c++
[code]
class URHO3D_API CurlWrapper {
...

static void ConstructCurl(CurlWrapper* ptr) {
    new(ptr) CurlWrapper();
}
...

engine->RegisterObjectType("Curl", sizeof(CurlWrapper), asOBJ_VALUE | asOBJ_POD | asOBJ_APP_CLASS_C);
engine->RegisterObjectBehaviour("Curl", asBEHAVE_CONSTRUCT, "void f()", asFUNCTION(ConstructCurl), asCALL_CDECL_OBJLAST);
engine->RegisterObjectMethod("Curl", "bool Download(const String&in,const String&in)", asMETHODPR(CurlWrapper, Download,(const String&,const String&), bool), asCALL_THISCALL);
engine->RegisterObjectMethod("Curl", "bool Get(const String&in)", asMETHODPR(CurlWrapper, Get,(const String&), bool), asCALL_THISCALL);
[/code]

angelscript:
[code]
Curl@ c=Curl();
[/code]

I got a error of: Object handle is not supported for this type, so is it possible or something necessary missed?

thanks.

-------------------------

cadaver | 2017-01-02 01:06:21 UTC | #2

You're registering it as a value type, which means you can't use handles on it, so leave the @ out.

If you want to use handles on your object, you need to register as a ref type instead and handle refcounting (with classes that derive from Urho's RefCounted this is rather easy)

-------------------------

victorfence | 2017-01-02 01:06:23 UTC | #3

Hi Cadaver, thanks a lot for your guid. My class definition is done by these codes now:

[code]
class URHO3D_API CurlWrapper : public Object {
  OBJECT(CurlWrapper);
  BASEOBJECT(CurlWrapper);
...

RegisterObjectConstructor<CurlWrapper>(engine, "Curl");
engine->RegisterObjectMethod("Curl", "bool Download(const String&in,const String&in)",
        asMETHODPR(CurlWrapper, Download,(const String&,const String&), bool), asCALL_THISCALL);
...
[/code]

And, may I ask another question?
Each of my "Curl" object always downloads file under a sub thread(pthread), I want to send "ProgressChanged" event to each angelscript "Curl" instances:
[code]
VariantMap eventData;
eventData["progress"] = progress;
SendEvent("ProgressChanged",eventData);
[/code]

When I try this, I got:
ERROR: Sending events is only supported from the main thread

I know this should not a defect of urho3d, but I'd like to hear any suggestion about this, thanks.

-------------------------

cadaver | 2017-01-02 01:06:23 UTC | #4

You need a "master" object that polls on the main thread, for example in the Application update event, for a queue that the subthreads post their progress reports to. The master object will actually send the events. 

See the FileWatcher class which does something very similar.

Urho doesn't implement this kind of mechanism automatically because it's not unambiguous, at what stage of frame processing these "other-thread" events should be handled.

-------------------------

victorfence | 2017-01-02 01:06:24 UTC | #5

[quote="cadaver"]You need a "master" object that polls on the main thread, for example in the Application update event, for a queue that the subthreads post their progress reports to. The master object will actually send the events. 

See the FileWatcher class which does something very similar.

Urho doesn't implement this kind of mechanism automatically because it's not unambiguous, at what stage of frame processing these "other-thread" events should be handled.[/quote]

Thank you Cadaver, It's good to know this can be done. I'll take a look!!

-------------------------

