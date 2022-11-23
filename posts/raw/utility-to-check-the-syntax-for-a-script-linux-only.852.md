setzer22 | 2017-01-02 01:03:30 UTC | #1

I have made this simple Urho3D application that just gets an Script name as a parameter, compiles it and then exits. All is done in headless mode.

The goal is having a tool that just checks the syntax for a given Script. Having this, combined with a simple Unix script to filter the output and just show compiler errors I've been able to check for compiler errors just by pressing F6 on vim :smiley:

Here's the Urho3D application code:

SyntaxChecker.h:
[code]
#pragma once

#include <Urho3D/Urho3D.h>
#include <Urho3D/Engine/Application.h>

using namespace Urho3D;

class SyntaxChecker : public Urho3D::Application {
   OBJECT(SyntaxChecker);

public:
   SyntaxChecker(Urho3D::Context*);

   virtual void Setup();
   virtual void Start();
   virtual void Stop() {}

private:
   
   SharedPtr<Context> context;
   String scriptName;
};
[/code]

SyntaxChecker.cpp
[code]
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Script/ScriptFile.h>
#include <Urho3D/Script/Script.h>
#include "CustomComponents.h"

using namespace Urho3D;

DEFINE_APPLICATION_MAIN(SyntaxChecker)

SyntaxChecker::SyntaxChecker(Urho3D::Context* context) : Application(context){
    this->context = context;
}

void SyntaxChecker::Setup(){
    engineParameters_["Headless"] = true;
    
    context_->RegisterSubsystem(new Script(context_));
    asIScriptEngine* engine = GetSubsystem<Script>()->GetScriptEngine();
    
    //Register here your custom script and object methods
    //if you happen to have them
    
    const Vector<String>& arguments = GetArguments();
    scriptName = arguments[0];
}

void SyntaxChecker::Start(){
    
    ScriptFile* e = context->GetSubsystem<ResourceCache>()->
        GetResource<ScriptFile>("Scripts/"+scriptName);
    engine_->Exit();
}
[/code]

This should build fine as of 1.32 (and the most recent commit I have, actually).

This will basically load the engine and then exit. If there was a compiler error, it should've been logged. The executable receives the Script path as its first paramer. Now to filter the output I use the following bash script (this is placed next to the executable):

syncheck.sh:
[code]
#!/bin/bash

s=$(echo $1 | sed s/'.*\/Scripts\/\(.*\)'/'\1'/g)
echo Checking syntax for $s
./SyntaxChecker $s 2>&1 | awk '/ERROR/{print;}' | sed s/'\[.*\]\s'/''/g
[/code]

This script does two things, first it takes a full (or relative) path as an argument and passes it to the Urho application I just posted and then it runs the application with the correct path. It's assumed that all the scripts are under the "Scripts" directory, note that if there are multiple "Scripts" folders in the path this will fail (I'm not that good with regex, but this can be fixed).

Lastly, I added this to my .vimrc in order to bind F6 to check the syntax for the current script:

[code]map <F6> :! cd $MY_PROJECT_BIN_PATH && sh syncheck.sh '%:p' <Return>[/code]

And that's all folks! When I have time I'll just get rid of all the bash and do everything with Urho to ensure compatibility in all platforms.

This can be basically used as an application that returns all the errors in a file, so it can be the base of a sublime, vim or similar editors' plugin to highlight errors and things like that, and that was my idea on the first place. If anyone does something similar please share it!

-------------------------

