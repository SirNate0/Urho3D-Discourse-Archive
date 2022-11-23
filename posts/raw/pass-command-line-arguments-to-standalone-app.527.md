godan | 2017-01-02 01:01:08 UTC | #1

I'm using Urho as a static lib and I would like to pass some command line arguments to the app. I'm fairly new to this library, so for now, I've just used the sample code (Physics) to compile a standalone app. In that sample code, the application entry point is defined:

[code]DEFINE_APPLICATION_MAIN(Physics)

Physics::Physics(Context* context) :
    Sample(context),
    drawDebug_(false)
{
}[/code]

Is it possible to modify this macro so that command line arguments can be passed?

-------------------------

cadaver | 2017-01-02 01:01:08 UTC | #2

DEFINE_MAIN and DEFINE_APPLICATION_MAIN always call the static function ParseArguments() in ProcessUtils.h to capture the command line. You can retrieve the arguments later with the similarly static function GetArguments().

-------------------------

godan | 2017-01-02 01:01:21 UTC | #3

Thanks! That works great.

-------------------------

