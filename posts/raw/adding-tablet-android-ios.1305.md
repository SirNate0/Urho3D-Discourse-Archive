vivienneanthony | 2017-01-02 01:06:42 UTC | #1

Hi,
So I converted Existence to a more compact version. I'm trying to get touch enabled and port some more so Android and IOS can be supported. Any suggestions?

The first problem:

Getting the UI to handle touch screen input. I'm not sure how and it is not clear. Do I have to assign any special events to UIElements??

[code]
void GameEconomicGameClient::Init(Context * context)
{

    /// Get the platform - Set global variable that determines the game
    CurrentPlatform = OSTool::GetOS(GetPlatform());

    /// Change touch enbabled based on platform
    if (CurrentPlatform==PlatformAndroid||CurrentPlatform==PlatformIOS)
    {
        /// touch enable for Android and iOS
        touchenabled_=true;
    }
    else if (GetPlatform() == "Android" || GetPlatform() == "iOS")
    {

        /// touch enable for Android and iOS
        touchenabled_=true;
    }
    else
    {
        /// diaable touch enabled
        touchenabled_=false;
    }

    return;
}
[/code]

The second problem:
How does the package system work? Considering I probably have to make a client load a package for all the needed resources from a server? So, How to add a directory to a package? THen get it sent over.

The third problem:
Is there any additional networking required

Fourth problem:
Making the executable and putting it somewhere so I can test it either locally on a simulator or live?

Vivienne

-------------------------

