UrOhNo3D | 2017-01-02 01:08:09 UTC | #1

Hi all!

I am currently trying to implement basic networking into a project that I am working on, and whilst some code samples (NinjaSnowWar, 16_Chat and 17_SceneReplication) are useful, they make no usage of the HttpRequest as far as I can tell.

I am interested in making my own custom API calls to a server that hosts player information which is retrieved upon logging in, only I cannot seem to find the appropriate syntax for doing so.

Here is some code to show where I am at:
[code]SharedPtr< HttpRequest > response = network->MakeHttpRequest(String("http://httpbin.org/ip"));
Log *log = new Log(context_);
if (response->GetError() == "") {
    log->WriteRaw("No error in response");

    std::string dest;
    response->Read(&dest, response->GetAvailableSize());
    log->WriteRaw("RESP: BEGIN");
    log->WriteRaw(String(dest));
    log->WriteRaw("RESP: END");
}[/code]

I am basing this code off of the documentation here: [url]http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_http_request.html[/url]

Can anybody help me extract the response from this GET request so that I can use it to access my own custom API?
Currently, I am getting:
[code]No error in response
RESP: BEGIN
RESP: END[/code]
Am I perhaps not handling the void pointer correctly?
Thanks!

-------------------------

UrOhNo3D | 2017-01-02 01:08:10 UTC | #2

Thanks for your quick response!

[quote]VectorBuffer is also a much better candidate in general given all the whacky stuff you can get from a GET request.
[/quote]
Could you elaborate on this? A much better candidate for what, and how would it be used? I'm unsure where in the documentation this is, and how I would go about using it.

At any rate, I will play around with the code snippet that you provided shortly and see whether I can get it working.

-------------------------

UrOhNo3D | 2017-01-02 01:08:10 UTC | #3

Hey, so I have managed to get this working now!

[code]void NetworkHandler::StartHTTPRequest() {
    response = network->MakeHttpRequest(String("http://httpbin.org/ip"));
    log = new Log(context_);
}

void NetworkHandler::HandleUpdate(StringHash eventType, VariantMap& eventData) {
    HttpRequestState state = response->GetState();
    if (state == HTTP_CLOSED && !stop) {
        dest.Resize(response->GetAvailableSize());
        const unsigned bytesRead = response->Read((void*)dest.CString(), response->GetAvailableSize());
        log->WriteRaw(dest);
        stop = true;
    }
}[/code]
where HandleUpdate is run every game loop.

Thanks again for the help! Really appreciated!

-------------------------

