Lumak | 2017-12-15 08:22:17 UTC | #1

I had another thread posted in "dev talk" section because there were some issues that I needed to resolve, but it's all fixed now.

edit final: new repository created [url]https://github.com/Lumak/Urho3D-1.4-TurboBadger[/url]

--------------------------------------------------------------------------------------------
## Features

- no unique shader required
- no unique render path required
- no unique graphics settings required
- uses Urho3D's default UIBatch render process
- delivers TurboBadger's batch data in its format, so it pumps data as fast as Turbo Badger can send them

--------------------------------------------------------------------------------------------

Image (Turbo Badger demo shown in Urho3D):
[img]http://i.imgur.com/gA2z5qi.jpg?1[/img]

-------------------------

Lumak | 2017-01-02 01:07:51 UTC | #2

I just been informed that this code is not compatible with the latest Urhod3D master branch, as reported by Hevedy:

[quote]
Added the line 65 add_sample_subdirectory (54_TurboBadger) in Source/Samples/CMakeLists.txt to include the sample.
*Added the line 108 add_subdirectory (ThirdParty/TurboBadger) in Source/CMakeLists.txt to include the TurboBadger lib.

This are errors: ?
The line UIDrag.h 40 should be URHO3D_OBJECT( UIDrag ); and no OBJECT( UIDrag ); ?
The line TBWrapper.h 51 should be URHO3D_OBJECT( TUIRendererBatcher ); and no OBJECT( TUIRendererBatcher ) ?
HANDLER to URHO3D_HANDLER

Anyway after change that i got 6 errors
Error 8 error C2208: 'Urho3D::Application' : no members defined using this type 54_turbobadger\UIDrag.h 40 1 54_TurboBadger
Error 3 error C1903: unable to recover from previous error(s); stopping compilation 54_turbobadger\TBWrapper.h 51 1 54_TurboBadger

*I using the master version but with the 1.4 adding only that changes to the CMakeList.txt give me too errors with the generated files.

41>Urho3D-1.4\Build\bin\54_TurboBadger.exe : fatal error LNK1120: 195 unresolved externals
[/quote]

I'm still on 1.4 and will not be merging with the master branch anytime soon. I hope there are others who can help him with his build errors. I'll try to help him with 1.4 linking problem.

-------------------------

Enhex | 2017-01-02 01:07:52 UTC | #3

I think it might be a good idea to wait for the 1.5 release before adopting to the changes.

-------------------------

Lumak | 2017-01-02 01:09:53 UTC | #4

added a download link to the integration, including tb and its data.

-------------------------

Enhex | 2017-01-02 01:09:53 UTC | #5

Why not make a public repository?

-------------------------

Lumak | 2017-01-02 01:09:53 UTC | #6

I don't see any reason why I should create a repository for this.  I don't see anyone interest in this judging by the number of comments on this thread (only you commented about waiting), so I'm just going to provide a public downloadable link.

-------------------------

thebluefish | 2017-01-02 01:09:53 UTC | #7

A repo takes a minute to setup and makes it so much easier to look at the code. Even if there aren't any comments to "show interest", it doesn't mean that people will be any less interested in your work. For example, a libGDX demo that I created and posted on the site only got a few comments, but has racked up well over 20k downloads.

Github (or really any public source control host) is a great place to keep a portfolio of your work if you plan on applying to developer positions.

-------------------------

Dave82 | 2017-01-02 01:09:53 UTC | #8

[quote="Lumak"]I don't see any reason why I should create a repository for this.  I don't see anyone interest in this judging by the number of comments on this thread (only you commented about waiting), so I'm just going to provide a public downloadable link.[/quote]

I'll comment :smiley: You did an awesome work ! I can't see the reason why devs won't implement this as an official subsystem ? Looks professional , there are way more widgets , and could boost the editor's appereance and it would attract more users.

-------------------------

rasteron | 2017-01-02 01:09:53 UTC | #9

Count me in! I would agree on this as well. :slight_smile: It is another good UI framework option and setting up a repo where you can improve and fully integrate it is a big plus! I'm also thinking of using this as an alternative to Qt, due to its hefty payload.

Btw, thanks again for the download links and assistance Lumak! :smiley:

-------------------------

jenge | 2017-01-02 01:09:53 UTC | #10

In terms of "higher end" editor, one thing TurboBadger needs is support for multiple top level windows.  Being able to drag windows in and out of tabs would also be huge.  Urho would also have to support multiple top level windows (probably with styling, as default style isn't good for a an editor window like this)

- Josh

-------------------------

Bluemoon | 2017-01-02 01:09:54 UTC | #11

[quote="Lumak"]I don't see any reason why I should create a repository for this.  I don't see anyone interest in this judging by the number of comments on this thread (only you commented about waiting), so I'm just going to provide a public downloadable link.[/quote]

Trying to figure out the interest of people through the comments here might be really misleading... Believe me, I spent a considerable amount of my time last month (January 2016) trying to implement Turbo Badger as a stand alone library to Urho3D and guess what? I achieved it using your Urho3D_TurboBadger implementation, the exact same one you pulled from github. I had a local copy of the last snapshot and was looking for the best time to tinker with it.
When I realized that jenge and the folks at Atomic Game Engine (which bred from Urho3D) had Turbo Badger Integrated, I was more than motivated to give it a shot. 

I've only tested this on Windows Machine, OpenGL build was great, D3D9 was good but D3D11 had a bit of rendering issues (and I'm not really good at all those graphic pipeline stuffs :unamused:  ) What consumed a vast portion of my time and mental energy was how to integrate TB as part of other Third Party library and how its interface would be wrapped and exposed for use in Urho3D. Is it going to replace the existing UI system or will it be part of custom UI structure that would be implemented in Urho3D?

So... Quite a lot of people are interested in this project, even though some of us are yet to comment :wink:

-------------------------

Enhex | 2017-01-02 01:09:54 UTC | #12

I definitely want an external TurboBadger integration that doesn't modify Urho3D, so there's no need for a fork to maintain.

-------------------------

Lumak | 2017-01-02 01:09:54 UTC | #13

[quote="thebluefish"]
A repo takes a minute to setup and makes it so much easier to look at the code. Even if there aren't any comments to "show interest", it doesn't mean that people will be any less interested in your work. For example, a libGDX demo that I created and posted on the site only got a few comments, but has racked up well over 20k downloads.
[/quote]
Nice, if only we can do so well with games that we create.

[quote="Dave82"]
I'll comment :smiley: You did an awesome work ! I can't see the reason why devs won't implement this as an official subsystem ? Looks professional , there are way more widgets , and could boost the editor's appereance and it would attract more users.
[/quote]
Thank you. TurboBadger does have nice UI graphics.

[quote="rasteron"]
Count me in! I would agree on this as well. :slight_smile: It is another good UI framework option and setting up a repo where you can improve and fully integrate it is a big plus! I'm also thinking of using this as an alternative to Qt, due to its hefty payload.
Btw, thanks again for the download links and assistance Lumak! :smiley:
[/quote]
Yeah Qt is also LGPL, and you're welcome.

[quote="jenge"]
In terms of "higher end" editor, one thing TurboBadger needs is support for multiple top level windows. Being able to drag windows in and out of tabs would also be huge. Urho would also have to support multiple top level windows (probably with styling, as default style isn't good for a an editor window like this)
[/quote]
I haven't look into creating an editor, but I agree that having multiple top level windows in any editor would be beneficial.

[quote="Bluemoon"]
Trying to figure out the interest of people through the comments here might be really misleading... Believe me, I spent a considerable amount of my time last month (January 2016) trying to implement Turbo Badger as a stand alone library to Urho3D and guess what? I achieved it using your Urho3D_TurboBadger implementation, the exact same one you pulled from github. I had a local copy of the last snapshot and was looking for the best time to tinker with it.
When I realized that jenge and the folks at Atomic Game Engine (which bred from Urho3D) had Turbo Badger Integrated, I was more than motivated to give it a shot.

I've only tested this on Windows Machine, OpenGL build was great, D3D9 was good but D3D11 had a bit of rendering issues (and I'm not really good at all those graphic pipeline stuffs :unamused: ) What consumed a vast portion of my time and mental energy was how to integrate TB as part of other Third Party library and how its interface would be wrapped and exposed for use in Urho3D. Is it going to replace the existing UI system or will it be part of custom UI structure that would be implemented in Urho3D?

So... Quite a lot of people are interested in this project, even though some of us are yet to comment :wink:
[/quote]
It's great to hear that someone is making use of my repository from last year. I haven't built D3D11 yet to see what's going on with that, but I'll attempt to build it and see sometime this week.

[quote="Enhex"]
I definitely want an external TurboBadger integration that doesn't modify Urho3D, so there's no need for a fork to maintain.
[/quote]
The Urho3D-1.4-TurboBadger repository will be a standalone integration to an app, and not integrated with Urho3D lib.  It's good to hear comments like this so I can save myself the work trying to do the opposite.

[b][size=150]New Repository Created[/size][/b]
Just because you asked - link [url]https://github.com/Lumak/Urho3D-1.4-TurboBadger[/url]

-------------------------

jmiller | 2017-01-02 01:09:54 UTC | #14

Nice work on the implementation. :slight_smile:

[quote="Enhex"]I definitely want an external TurboBadger integration that doesn't modify Urho3D, so there's no need for a fork to maintain.[/quote]

I think the Urho-TurboBadger integration posted by [b]thebluefish[/b] also fits this bill.
[topic1413.html](http://discourse.urho3d.io/t/turbo-badger-implementation/1364/1)
I migrated over half a year ago and only looked forward, aside from some work in the shared linking department.  :mrgreen: 

Re. multi-windows.. others are more knowledgeable on this, but TB does have multiple internal windows (enough for me, in an editor), drop support, and is rather flexible in general.

-------------------------

George | 2017-01-02 01:09:56 UTC | #15

Hi,
This is great stuff.
I hope you have time to port this to the Urho trunk  version.

Best regards,

-------------------------

George | 2017-01-02 01:09:56 UTC | #16

Ignore my previous message.
I got it to work in 1.5.

Just change these to new Urho3d name convention. 

[code]
class UTBRendererBatcher : public UIElement, public TBRendererBatcher
{
	URHO3D_OBJECT( UTBRendererBatcher, UIElement)
...}



URHO3D_EVENT(E_TBMSG, TBMessageNamespace)
{
	URHO3D_PARAM(P_TBWIDGET, Widget);  // TBWidget pointer
}


//=============================================================================
//=============================================================================
class UTBListener : public Object, public TBWidgetListener
{
	URHO3D_OBJECT(UTBListener, Object);
public:
	UTBListener(Context *context);

	~UTBListener();

	void CreateMsgWindow();
	virtual void OnWidgetRemove(TBWidget *parent, TBWidget *child);
	virtual bool OnWidgetInvokeEvent(TBWidget *widget, const TBWidgetEvent &ev);

	TBWidget* GetTBMessageWidget()
	{
		return (TBWidget*)pTBMessageWindow_;
	}
protected:
	void SendEventMsg();

protected:
	TBMessageWindow     *pTBMessageWindow_;

};



	// create TB render batcher
	Graphics *graphics = GetSubsystem<Graphics>();
	UTBRendererBatcher::Create(GetContext(), graphics->GetWidth(), graphics->GetHeight());
	UTBRendererBatcher::Singleton().Init("Data/TB/");

	// create a msg win
	pTBListener_ = new UTBListener(GetContext());
	pTBListener_->CreateMsgWindow();

	SubscribeToEvent(E_TBMSG, URHO3D_HANDLER(NVuDuMain, HandleTBMessage));


[/code]

How to make it interact with Urho object?

-------------------------

Enhex | 2017-01-02 01:09:56 UTC | #17

Pull request or let lumark add it to the repository, which should also remove the urho version number from the name, from "Urho3D-1.4-TurboBadger", to "Urho3D-TurboBadger".

-------------------------

George | 2017-01-02 01:09:56 UTC | #18

I think Lumak can update it. As it is easy for him to add changes to the code.

One more thing for those who want to see their game object. Just comment out the below line inside the UTBRendererBatcher.cpp
  
//  root_.SetSkinBg(TBIDC("background"));

Cheers

-------------------------

christianclavet | 2017-01-02 01:11:19 UTC | #19

Hi. I've tried to build it using cmake, but got some error (I'm not familiar with CMAKE, only used it to build URHO so far).

[quote]New Repository Created
Just because you asked - link [github.com/Lumak/Urho3D-1.4-TurboBadger](https://github.com/Lumak/Urho3D-1.4-TurboBadger)[/quote]
I extracted the archive then tried to build it with cmake... Here the result:
[code]C:\Users\Christian\Desktop\Urho3D-1.4-TurboBadger-master\Source\ThirdParty\TurboBadger>cmake_codelite ../turbo
-- The C compiler identification is GNU 5.1.0
-- The CXX compiler identification is GNU 5.1.0
-- Check for working C compiler: C:/TDM-GCC-64/bin/gcc.exe
-- Check for working C compiler: C:/TDM-GCC-64/bin/gcc.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: C:/TDM-GCC-64/bin/g++.exe
-- Check for working CXX compiler: C:/TDM-GCC-64/bin/g++.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Error at CMakeLists.txt:36 (setup_library):
  Unknown CMake command "setup_library".


CMake Warning (dev) in CMakeLists.txt:
  No cmake_minimum_required command is present.  A line of code such as

    cmake_minimum_required(VERSION 3.4)

  should be added at the top of the file.  The version specified may be lower
  if you wish to support older CMake versions for this project.  For more
  information run "cmake --help-policy CMP0000".
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Configuring incomplete, errors occurred!
See also "C:/Users/Christian/Desktop/Urho3D-1.4-TurboBadger-master/Source/ThirdParty/turbo/CMakeFiles/CMakeOutput.log".[/code]

[b]EDIT:[/b] Ok seen more of the structure of your files. This need to be added to the files of URHO and modify the makefiles so URHO add the new sub-directories to the build. I will have to download 1.4 to really test this, but understand more a little about CMAKE now. I would really like to have this in URHO3D as an option that could be activated. (Same for IMGUI), both GUI have their use and your worked to integrate them in URHO. Having a way to activate them in the build via cmake flag would be really nice.

-------------------------

Lumak | 2017-01-02 01:11:20 UTC | #20

[quote]EDIT: Ok seen more of the structure of your files. This need to be added to the files of URHO and modify the makefiles so URHO add the new sub-directories to the build. I will have to download 1.4 to really test this, but understand more a little about CMAKE now. I would really like to have this in URHO3D as an option that could be activated. (Same for IMGUI), both GUI have their use and your worked to integrate them in URHO. Having a way to activate them in the build via cmake flag would be really nice.[/quote]

Yes, all of my code exchanges are built as a sample in the sample folder.  Good to see that you figured it out.

-------------------------

christianclavet | 2017-01-02 01:11:21 UTC | #21

Hi, Downloaded 1.4 and added your files, it compile but fail at turbobadger because I think it require c++11 support and I don't think the compiler I'm using (Windows 10, TDM-GCC5.1 64bit, Codelite) support it.
TDM-GCC should be the latest build for GNU GCC available for windows. (I think it's based on MINGW64)

It all seem to fail when compiling theses directives (nullptr): From google, this seem that my toolchain doesnt support c++11 (If the C++11 is active in CMAKE for Urho1.5 it fail the generation). Is there a way to make it work, like replacing with NULL instead? All the errors seem to point at this nullptr use.
[code]In file included from C:\Users\Public\Projets\URHO\Urho3D-1.4\Source\ThirdParty\TurboBadger\tb_addon.h:10:0,
                 from C:\Users\Public\Projets\URHO\Urho3D-1.4\Source\ThirdParty\TurboBadger\tb_addon.cpp:7:
C:\Users\Public\Projets\URHO\Urho3D-1.4\Source\ThirdParty\TurboBadger\tb_widgets.h: At global scope:
C:\Users\Public\Projets\URHO\Urho3D-1.4\Source\ThirdParty\TurboBadger\tb_widgets.h:583:60: error: 'nullptr' was not declared in this scope
  TBWidget *GetNextDeep(const TBWidget *bounding_ancestor = nullptr) const;[/code]
[b]EDIT: [/b]Done replacement of "nullptr" to "NULL" all over the files of turbobadger and it now compile and build. But the example 54_Turbobadger.exe doesnt show any GUI exept the URHO ones.
EDIT2: Put back the source as they were. Then set the CMAKELIST.TXT of the source to specifically set the compiler to use the c++11 features (Mingw64 support it but need to be specified). No errors in compilation, linking. But still only a black window with the URHO3D logo.

Here is the code I added to the CMAKELIST to specifically set the compiler to use c++11 feature (from google)
[code]include(CheckCXXCompilerFlag)
CHECK_CXX_COMPILER_FLAG("-std=c++11" COMPILER_SUPPORTS_CXX11)
CHECK_CXX_COMPILER_FLAG("-std=c++0x" COMPILER_SUPPORTS_CXX0X)
if(COMPILER_SUPPORTS_CXX11)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
elseif(COMPILER_SUPPORTS_CXX0X)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
else()
        message(STATUS "The compiler ${CMAKE_CXX_COMPILER} has no C++11 support. Please use a different C++ compiler.")
endif()[/code]

-------------------------

Lumak | 2017-01-02 01:11:21 UTC | #22

[quote="christianclavet"]
[b]EDIT: [/b]Done replacement of "nullptr" to "NULL" all over the files of turbobadger and it now compile and build. But the example 54_Turbobadger.exe doesnt show any GUI exept the URHO ones.[/quote]

You don't see any gui except for the urho ones? That's odd because there is no urho gui in that example.  They're all TB gui.

Perhaps you can try skipping the "hello world" intro in the Start() func. and jump right into the TB demo:
[code]
void UIDrag::Start()
{
    // Execute base class startup
    Sample::Start();

    // Set mouse visible
    //String platform = GetPlatform();
    //if (platform != "Android" && platform != "iOS")
    GetSubsystem<Input>()->SetMouseVisible(true);

    // create TB render batcher
    Graphics *graphics = GetSubsystem<Graphics>();
    UTBRendererBatcher::Create( GetContext(), graphics->GetWidth(), graphics->GetHeight() );
    UTBRendererBatcher::Singleton().Init( "Data/TB/" );
    
    // create a msg win
    //pTBListener_ = new UTBListener( GetContext() );
    //pTBListener_->CreateMsgWindow();

    //SubscribeToEvent(E_TBMSG, HANDLER(UIDrag, HandleTBMessage));

    // skip to tb demo
    TBDemo::Init();
}

[/code]

-------------------------

Lumak | 2017-01-02 01:11:21 UTC | #23

You did copy "bin\Data\TB" folder to your build folder?

-------------------------

christianclavet | 2017-01-02 01:11:21 UTC | #24

Hi,

I had packed resources. I had put them in the source files. Removed the archives and copied the folders instead. I see everything now. Do I have to tell something in the makefile to put them in the pak files?
Thanks a lot for helping me! I see the gui now!

-------------------------

Lumak | 2017-01-02 01:11:21 UTC | #25

[quote="christianclavet"]Hi,

I had packed resources. I had put them in the source files. Removed the archives and copied the folders instead. I see everything now. Do I have to tell something in the makefile to put them in the pak files?
Thanks a lot for helping me! I see the gui now![/quote]

I don't usually work with pak files unless it's something that I create specifically to protect data content/save file.  I'm not sure how the pak files are auto generated on platforms other than Android -- auto built from Android Studio for me.  So, I'm no help.

It's good to hear you got it working!  And, I didn't do much, just watched your progress onto getting it working  :wink:

-------------------------

christianclavet | 2017-01-02 01:11:22 UTC | #26

Thanks Lumak!

I've done a search of all the makefiles that URHO uses to see how it creating the .PAK archives. It use a folder and put the files recursively into an archive. 
I've done it manually via the pakage tool and from the output of the console the resources were packed in the .pak files with the rest. So I checked the sources files of the demo and I think TurboBadger is using it's own file system to load the ressources.

[b]From TBDEMO.cpp[/b][code]void ResourceEditWindow::Load(const char *resource_file)
{
	m_resource_filename.Set(resource_file);
	SetText(resource_file);

	// Set the text of the source view
	m_source_edit->SetText("");

	if (TBFile *file = TBFile::Open(m_resource_filename, TBFile::MODE_READ))
	{
		TBTempBuffer buffer;
		if (buffer.Reserve(file->Size()))
		{
			uint32 size_read = file->Read(buffer.GetData(), 1, buffer.GetCapacity());
			m_source_edit->SetText(buffer.GetData(), size_read);
		}
		delete file;
	}
	else // Error, show message
	{
		TBStr text;
		text.SetFormatted("Could not load file %s", resource_file);
		if (TBMessageWindow *msg_win = new TBMessageWindow(GetParentRoot(), TBIDC("")))
			msg_win->Show("Error loading resource", text);
	}

	RefreshFromSource();
}[/code]

It is probably not using the file system mechanism from URHO. That explain why I had a black window with only the URHO logo. (This will happen if it fail to load the resources). I don't know if this could be fixed to use URHO to load the files and convert it in a TBFILE pointer...

If this would mean modifying the Turbobadger source files (not the demo), I don't think it would be worth it, since somebody would have to maintain it at each revision... Perhaps warn if URHO_PACKAGING is active that the UI resources need to be in a folder not into an archive (Would this create problems with other platforms like IOS, Android and Emscriptem?). I mean, if the resources can't be put in a pak file, would not work on these platforms?

Or there a way to make this completely external?

This seem to work fine here on Windows and Linux Mint (using codelite on both). And for me it's what I need.

-------------------------

George | 2017-01-02 01:11:22 UTC | #27

Hi christianclavet

Read my post on this thread to get it to run on Urho 1.5.

Regards

-------------------------

christianclavet | 2017-01-02 01:11:22 UTC | #28

HI, George. 

When I saw it first I was not understanding. I checked the source again and saw a difference:

[code]class UTBRendererBatcher : public UIElement, public TBRendererBatcher
{
    OBJECT( UTBRendererBatcher )[/code]

Would be something like this:
[code]class UTBRendererBatcher : public UIElement, public TBRendererBatcher
{
    URHO3D_OBJECT( UTBRendererBatcher )[/code]

I'll try it and report.

-------------------------

christianclavet | 2017-01-02 01:11:22 UTC | #29

Hi. Sorry to double post. You were right, it worked. I decided to load the last version of Urho directly from GITHUB (03/20/16) and try to build it with it. There are new keywords that have been changed since with the URHO3D_ prefix.

For using this with URHO 1.5 (last revision) you will have to replace 4 files from the example folder (54_Turbobadger folder)(this only affect the demo source, the source for TurboBadger I had is unchanged).

First file: [b]UIDRAG.H[/b]
[code]//
// Copyright (c) 2008-2015 the Urho3D project.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//

#pragma once

#include <Urho3D/Core/Object.h>
#include <TurboBadger/tb_widgets_listener.h>

#include "Sample.h"


namespace Urho3D
{
class Node;
class Scene;
}

namespace tb
{
class TBMessageWindow;
}

using namespace Urho3D;
using namespace tb;

//=====================================
URHO3D_EVENT(E_TBMSG, TBMessageNamespace)
{
    URHO3D_PARAM(P_TBWIDGET, Widget);  // TBWidget pointer
}

//=============================================================================
//=============================================================================
class UTBListener : public Object, public TBWidgetListener
{
    URHO3D_OBJECT(UTBListener, Object);
public:
    UTBListener(Context *context);

    ~UTBListener();

    void CreateMsgWindow();
	virtual void OnWidgetRemove(TBWidget *parent, TBWidget *child);
	virtual bool OnWidgetInvokeEvent(TBWidget *widget, const TBWidgetEvent &ev);

    TBWidget* GetTBMessageWidget()
    {
        return (TBWidget*)pTBMessageWindow_;
    }
protected:
    void SendEventMsg();

protected:
    TBMessageWindow     *pTBMessageWindow_;

};

//=============================================================================
//=============================================================================
/// GUI test example.
/// This sample demonstrates:
///     - Creating GUI elements from C++
///     - Loading GUI Style from xml
///     - Subscribing to GUI drag events and handling them.
class UIDrag : public Sample
{
    URHO3D_OBJECT(UIDrag,Sample);

public:
    /// Construct.
    UIDrag(Context* context);
    ~UIDrag();

    /// Setup after engine initialization and before running the main loop.
    virtual void Setup();
    virtual void Start();
    virtual void Stop();

protected:
    void HandleTBMessage(StringHash eventType, VariantMap& eventData);

    /// Return XML patch instructions for screen joystick layout for a specific sample app, if any.
    virtual String GetScreenJoystickPatchString() const { return
        "<patch>"
        "    <add sel=\"/element/element[./attribute[@name='Name' and @value='Hat0']]\">"
        "        <attribute name=\"Is Visible\" value=\"false\" />"
        "    </add>"
        "</patch>";
    }

    UTBListener     *pTBListener_;

};
 [/code]
[b]UIDRAG.CPP[/b]
[code]//
// Copyright (c) 2008-2015 the Urho3D project.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//

#include <Urho3D/Urho3D.h>

#include "UIDrag.h"
#include "UTBRendererBatcher.h"
#include "TBDemo.h"

#include <Urho3D/DebugNew.h>

//=============================================================================
//=============================================================================
URHO3D_DEFINE_APPLICATION_MAIN(UIDrag)


//=============================================================================
//=============================================================================

UIDrag::UIDrag(Context* context) :
    Sample(context), pTBListener_( NULL )
{
}

UIDrag::~UIDrag()
{
    if ( pTBListener_ )
    {
        delete pTBListener_;
        pTBListener_ = NULL;
    }
}

//=============================================================================
//=============================================================================
void UIDrag::Setup()
{
    // Modify engine startup parameters
    engineParameters_["WindowTitle"] = GetTypeName();
    engineParameters_["LogName"]     = GetSubsystem<FileSystem>()->GetAppPreferencesDir("urho3d", "logs") + GetTypeName() + ".log";
    engineParameters_["FullScreen"]  = false;
    engineParameters_["Headless"]    = false;
    engineParameters_["WindowWidth"] = 1280; 
    engineParameters_["WindowHeight"] = 720;
}

//=============================================================================
//=============================================================================
void UIDrag::Start()
{
    // Execute base class startup
    Sample::Start();

    // Set mouse visible
    String platform = GetPlatform();
    if (platform != "Android" && platform != "iOS")
        GetSubsystem<Input>()->SetMouseVisible(true);

    // create TB render batcher
    Graphics *graphics = GetSubsystem<Graphics>();
    UTBRendererBatcher::Create( GetContext(), graphics->GetWidth(), graphics->GetHeight() );
    UTBRendererBatcher::Singleton().Init( "Data/TB/" );
    
    // create a msg win
    pTBListener_ = new UTBListener( GetContext() );
    pTBListener_->CreateMsgWindow();

    SubscribeToEvent(E_TBMSG, URHO3D_HANDLER(UIDrag, HandleTBMessage));

}

void UIDrag::Stop()
{
    TBDemo::Destroy();
    UTBRendererBatcher::Destroy();
    Sample::Stop();
}

void UIDrag::HandleTBMessage(StringHash eventType, VariantMap& eventData)
{
    using namespace TBMessageNamespace;

    TBWidget *pTBWidget = (TBWidget*)eventData[P_TBWIDGET].GetVoidPtr();

    if ( pTBListener_->GetTBMessageWidget() == pTBWidget )
    {
        TBDemo::Init();
    }
}

//=============================================================================
//=============================================================================
UTBListener::UTBListener(Context *context)
    : Object(context)
    , pTBMessageWindow_( NULL )
{
}

UTBListener::~UTBListener()
{
    if ( pTBMessageWindow_ )
    {
        pTBMessageWindow_ = NULL;
    }
}

void UTBListener::CreateMsgWindow()
{
    TBStr text("\nHellow World from Turbo Badger.\n\nClick OK to get started.");
    pTBMessageWindow_ = new TBMessageWindow( &UTBRendererBatcher::Singleton().Root(), TBIDC("") );
    pTBMessageWindow_->Show("Start Message", text);

    TBWidgetListener::AddGlobalListener( this );
}

void UTBListener::OnWidgetRemove(TBWidget *parent, TBWidget *child)
{
    if ( pTBMessageWindow_ == child )
    {
        TBWidgetListener::RemoveGlobalListener( this );
    }
}

bool UTBListener::OnWidgetInvokeEvent(TBWidget *widget, const TBWidgetEvent &ev) 
{ 
    if ( pTBMessageWindow_ && pTBMessageWindow_ == ev.target )
    {
        if ( ev.type == EVENT_TYPE_CLICK )
        {
            TBWidgetListener::RemoveGlobalListener( this );

            SendEventMsg();
        }
    }

    return false; 
}

void UTBListener::SendEventMsg()
{
    using namespace TBMessageNamespace;

    VariantMap& eventData = GetEventDataMap();
    eventData[P_TBWIDGET] = GetTBMessageWidget();

    SendEvent( E_TBMSG, eventData );
}
[/code]
[b]UTBRendererBatcher.h[/b]
[code]//=============================================================================
// Copyright (c) 2015 LumakSoftware
//
//=============================================================================
#pragma once

#include <Urho3D/Urho3D.h>
#include <TurboBadger/tb_widgets.h>
#include <TurboBadger/tb_renderer.h>
#include <TurboBadger/renderers/tb_renderer_batcher.h>

namespace Urho3D
{
class Context;
class VertexBuffer;
class Texture2D;
}

//=============================================================================
//=============================================================================
using namespace Urho3D;
using namespace tb;

//=============================================================================
//=============================================================================
class UTBBitmap : public TBBitmap
{
public:
    UTBBitmap(Context *_pContext, int _width, int _height); 
    ~UTBBitmap();

    // =========== virtual methods required for TBBitmap subclass =========
	virtual void SetData(uint32 *_pdata)
    {
        texture_->SetData( 0, 0, 0, width_, height_, _pdata );
    }

    virtual int Width() { return width_; }
    virtual int Height(){ return height_; }

    SharedPtr<Context>      context_;
    SharedPtr<Texture2D>    texture_;
    int                     width_;
    int                     height_;
};

//=============================================================================
//=============================================================================
class UTBRendererBatcher : public UIElement, public TBRendererBatcher
{
    URHO3D_OBJECT( UTBRendererBatcher, UIElement );
public:
    // static funcs
    static void Create(Context *_pContext, int _iwidth, int _iheight)
    {
        if ( pSingleton_ == NULL )
        {
            pSingleton_ = new UTBRendererBatcher( _pContext, _iwidth, _iheight );
        }
    }

    static void Destroy()
    {
        if ( pSingleton_ )
        {
            pSingleton_->Remove();
            pSingleton_ = NULL;
        }
    }

    static UTBRendererBatcher& Singleton() { return *pSingleton_; }

    // methods
    void Init(const String &_strDataPath);
    void LoadDefaultResources();

    TBWidget& Root() { return root_; }
    const String& GetDataPath() { return strDataPath_; }

    // override funcs
    virtual void BeginPaint(int render_target_w, int render_target_h);
    virtual void EndPaint();

    // UIElement override method to add TB batches
    virtual void GetBatches(PODVector<UIBatch>& batches, PODVector<float>& vertexData, const IntRect& currentScissor);

	// ===== methods that need implementation in TBRendererBatcher subclasses =====
	virtual TBBitmap* CreateBitmap(int width, int height, uint32 *data);

    virtual void RenderBatch(Batch *batch);

	virtual void SetClipRect(const TBRect &rect)
    {
        m_clip_rect = rect;
    }

protected:
    // override methods
    virtual void AddQuadInternal(const TBRect &dst_rect, const TBRect &src_rect, uint32 color, TBBitmap *bitmap, TBBitmapFragment *fragment);

protected:
    UTBRendererBatcher(Context *_pContext, int _iwidth, int _iheight);
    virtual ~UTBRendererBatcher();

    void OnResizeWin(int _iwidth, int _iheight);
    void CreateKeyMap();
    void RegisterHandlers();

    void HandleUpdate(StringHash eventType, VariantMap& eventData);

    // renderer
    void HandleScreenMode(StringHash eventType, VariantMap& eventData);
    void HandleBeginFrame(StringHash eventType, VariantMap& eventData);
    void HandlePostUpdate(StringHash eventType, VariantMap& eventData);
    void HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData);

    // inputs
    void HandleMouseButtonDown(StringHash eventType, VariantMap& eventData);
    void HandleMouseButtonUp(StringHash eventType, VariantMap& eventData);
    void HandleMouseMove(StringHash eventType, VariantMap& eventData);
    void HandleMouseWheel(StringHash eventType, VariantMap& eventData);
    void HandleKeyDown(StringHash eventType, VariantMap& eventData);
    void HandleKeyUp(StringHash eventType, VariantMap& eventData);
    void HandleTextInput(StringHash eventType, VariantMap& eventData);

    // TB special and quality keys func
    int FindTBKey(int _ikey);

protected:
    static UTBRendererBatcher   *pSingleton_;

    TBWidget            root_;
    PODVector<float>    vertexData_;
    PODVector<UIBatch>  batches_;

    String              strDataPath_;

    HashMap<int, int>   uKeytoTBkeyMap;
    IntVector2          lastMousePos_;
};

[/code]
[b]UTBRendererBatcher.cpp[/b]
[code]//=============================================================================
// Copyright (c) 2015 LumakSoftware
//
//=============================================================================
#include <Urho3D/Urho3D.h>

#include <Urho3D/Core/Context.h>
#include <Urho3D/Core/Object.h>
#include <Urho3D/Core/CoreEvents.h>
#include <Urho3D/UI/UI.h>
#include <Urho3D/UI/UIElement.h>
#include <Urho3D/UI/UIEvents.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Graphics/GraphicsEvents.h>
#include <Urho3D/Graphics/VertexBuffer.h>
#include <Urho3D/Graphics/Texture2D.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/IO/FileSystem.h>
#include <Urho3D/Input/InputEvents.h>

#include <TurboBadger/tb_font_renderer.h>
#include <TurboBadger/tb_widgets.h>
#include <TurboBadger/tb_bitmap_fragment.h>
#include <TurboBadger/tb_system.h>
#include <TurboBadger/tb_msg.h>
#include <TurboBadger/tb_language.h>
#include <TurboBadger/animation/tb_animation.h>
#include <TurboBadger/animation/tb_widget_animation.h>

#include "UTBRendererBatcher.h"

#include <Urho3D/DebugNew.h>

//=============================================================================
//=============================================================================
#define QAL_VAL         0x60000000 // value to offset qualifier keys from all other keys in the same hash map

//=============================================================================
//=============================================================================
UTBRendererBatcher* UTBRendererBatcher::pSingleton_ = NULL;

//=============================================================================
//=============================================================================
UTBBitmap::UTBBitmap(Context *_pContext, int _width, int _height) 
    : context_( _pContext )
    , width_( _width ) 
    , height_( _height )
    , texture_( NULL )
{
    texture_ = new Texture2D( context_ );

    // set texture format
    texture_->SetMipsToSkip( QUALITY_LOW, 0 );
    texture_->SetNumLevels( 1 );
    texture_->SetSize( width_, height_, Graphics::GetRGBAFormat() );

    // set uv modes
    texture_->SetAddressMode( COORD_U, ADDRESS_WRAP );
    texture_->SetAddressMode( COORD_V, ADDRESS_WRAP );
}

//=============================================================================
//=============================================================================
UTBBitmap::~UTBBitmap()
{
    if ( texture_ )
    {
        texture_ = NULL;
    }
}

//=============================================================================
//=============================================================================
UTBRendererBatcher::UTBRendererBatcher(Context *_pContext, int _iwidth, int _iheight) 
    : UIElement( _pContext )
    , TBRendererBatcher() 
{
    SetPosition( 0, 0 );
    OnResizeWin( _iwidth, _iheight );
}

//=============================================================================
//=============================================================================
UTBRendererBatcher::~UTBRendererBatcher()
{
    vertexData_.Clear();
    batches_.Clear();
    uKeytoTBkeyMap.Clear();

    TBWidgetsAnimationManager::Shutdown();

    // shutdown
    tb_core_shutdown();
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::OnResizeWin(int _iwidth, int _iheight)
{
    m_screen_rect = TBRect( 0, 0, _iwidth, _iheight );

    SetSize( _iwidth, _iheight );

    root_.SetRect( m_screen_rect );
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::Init(const String &_strDataPath)
{
    // register with UI
    GetSubsystem<UI>()->GetRoot()->AddChild( this );

    // store data path
    strDataPath_ = GetSubsystem<FileSystem>()->GetProgramDir() + _strDataPath;

    // init tb core
    tb_core_init( this );

    // load resources
    LoadDefaultResources();

    // map keys
    CreateKeyMap();

    // register handlers
    RegisterHandlers();
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::LoadDefaultResources()
{
    g_tb_lng->Load("resources/language/lng_en.tb.txt");

    // Load the default skin, and override skin that contains the graphics specific to the demo.
    g_tb_skin->Load("resources/default_skin/skin.tb.txt", "demo01/skin/skin.tb.txt");

    // **README**
    // - define TB_FONT_RENDERER_FREETYPE in tb_config.h for non-demo
#ifdef TB_FONT_RENDERER_TBBF
    void register_tbbf_font_renderer();
    register_tbbf_font_renderer();
#endif
#ifdef TB_FONT_RENDERER_STB
    void register_stb_font_renderer();
    register_stb_font_renderer();
#endif
#ifdef TB_FONT_RENDERER_FREETYPE
    void register_freetype_font_renderer();
    register_freetype_font_renderer();
#endif

    // Add fonts we can use to the font manager.
#if defined(TB_FONT_RENDERER_STB) || defined(TB_FONT_RENDERER_FREETYPE)
    g_font_manager->AddFontInfo("resources/vera.ttf", "Vera");
#endif
#ifdef TB_FONT_RENDERER_TBBF
    g_font_manager->AddFontInfo("resources/default_font/segoe_white_with_shadow.tb.txt", "Segoe");
    g_font_manager->AddFontInfo("fonts/neon.tb.txt", "Neon");
    g_font_manager->AddFontInfo("fonts/orangutang.tb.txt", "Orangutang");
    g_font_manager->AddFontInfo("fonts/orange.tb.txt", "Orange");
#endif

    // Set the default font description for widgets to one of the fonts we just added
    TBFontDescription fd;
#ifdef TB_FONT_RENDERER_TBBF
    fd.SetID(TBIDC("Segoe"));
#else
    fd.SetID(TBIDC("Vera"));
#endif
    fd.SetSize(g_tb_skin->GetDimensionConverter()->DpToPx(14));
    g_font_manager->SetDefaultFontDescription(fd);

    // Create the font now.
    TBFontFace *font = g_font_manager->CreateFontFace(g_font_manager->GetDefaultFontDescription());

    // Render some glyphs in one go now since we know we are going to use them. It would work fine
    // without this since glyphs are rendered when needed, but with some extra updating of the glyph bitmap.
    if ( font )
    {
        font->RenderGlyphs(" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~????????");
    }

    root_.SetSkinBg(TBIDC("background"));

    TBWidgetsAnimationManager::Init();
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::CreateKeyMap()
{
    // special keys
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_UP       , TB_KEY_UP        ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_DOWN     , TB_KEY_DOWN      ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_LEFT     , TB_KEY_LEFT      ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_RIGHT    , TB_KEY_RIGHT     ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_PAGEUP   , TB_KEY_PAGE_UP   ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_PAGEDOWN , TB_KEY_PAGE_DOWN ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_HOME     , TB_KEY_HOME      ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_END      , TB_KEY_END       ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_TAB      , TB_KEY_TAB       ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_BACKSPACE, TB_KEY_BACKSPACE ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_INSERT   , TB_KEY_INSERT    ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_DELETE   , TB_KEY_DELETE    ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_RETURN   , TB_KEY_ENTER     ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_ESC      , TB_KEY_ESC       ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_F1       , TB_KEY_F1        ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_F2       , TB_KEY_F2        ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_F3       , TB_KEY_F3        ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_F4       , TB_KEY_F4        ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_F5       , TB_KEY_F5        ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_F6       , TB_KEY_F6        ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_F7       , TB_KEY_F7        ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_F8       , TB_KEY_F8        ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_F9       , TB_KEY_F9        ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_F10      , TB_KEY_F10       ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_F11      , TB_KEY_F11       ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( KEY_F12      , TB_KEY_F12       ) );

    // qualifiers: add QAL_VAL to qual keys to separate their range from rest of the keys
    uKeytoTBkeyMap.Insert( Pair<int,int>( QUAL_SHIFT + QAL_VAL, TB_SHIFT ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( QUAL_CTRL  + QAL_VAL, TB_CTRL  ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( QUAL_ALT   + QAL_VAL, TB_ALT   ) );
    uKeytoTBkeyMap.Insert( Pair<int,int>( QUAL_ANY   + QAL_VAL, TB_SUPER ) );
}

//=============================================================================
//=============================================================================
TBBitmap* UTBRendererBatcher::CreateBitmap(int width, int height, uint32 *data)
{
    UTBBitmap *pUTBBitmap = new UTBBitmap( GetContext(), width, height );

    FlushBitmap( (TBBitmap*)pUTBBitmap );

    pUTBBitmap->SetData( data );

    return (TBBitmap*)pUTBBitmap;
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::RenderBatch(Batch *_pb)
{
    if ( _pb )
    {
        UTBBitmap *pUTBBitmap = (UTBBitmap*)_pb->bitmap;
        SharedPtr<Texture2D> tdummy;
        SharedPtr<Texture2D> texture = pUTBBitmap?pUTBBitmap->texture_: tdummy;
        IntRect scissor( _pb->clipRect.x, _pb->clipRect.y, _pb->clipRect.x + _pb->clipRect.w, _pb->clipRect.y + _pb->clipRect.h );
        UIBatch batch( this, BLEND_ALPHA, scissor, texture, &vertexData_ );

        unsigned begin = batch.vertexData_->Size();
        batch.vertexData_->Resize(begin + _pb->vertex_count * UI_VERTEX_SIZE);
        float* dest = &(batch.vertexData_->At(begin));

        // set start/end
        batch.vertexStart_ = begin;
        batch.vertexEnd_   = batch.vertexData_->Size();

        for ( int i = 0; i < _pb->vertex_count; ++i )
        {
            dest[0+i*UI_VERTEX_SIZE]              = _pb->vertex[i].x; 
            dest[1+i*UI_VERTEX_SIZE]              = _pb->vertex[i].y; 
            dest[2+i*UI_VERTEX_SIZE]              = 0.0f;
            ((unsigned&)dest[3+i*UI_VERTEX_SIZE]) = _pb->vertex[i].col;
            dest[4+i*UI_VERTEX_SIZE]              = _pb->vertex[i].u; 
            dest[5+i*UI_VERTEX_SIZE]              = _pb->vertex[i].v;
        }

        // store
        UIBatch::AddOrMerge( batch, batches_ );
    }
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::GetBatches(PODVector<UIBatch>& batches, PODVector<float>& vertexData, const IntRect& currentScissor)
{
    for ( unsigned i = 0; i < batches_.Size(); ++i )
    {
        // get batch
        UIBatch &batch     = batches_[ i ];
        unsigned beg       = batch.vertexStart_;
        unsigned end       = batch.vertexEnd_;
        batch.vertexStart_ = vertexData.Size();
        batch.vertexEnd_   = vertexData.Size() + (end - beg);

        // resize and copy
        vertexData.Resize( batch.vertexEnd_ );
        memcpy( &vertexData[ batch.vertexStart_ ], &vertexData_[ beg ], (end - beg) * sizeof(float) );

        // store
        UIBatch::AddOrMerge( batch, batches );
    }

    // clear buffers
    vertexData_.Clear();
    batches_.Clear();
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::BeginPaint(int render_target_w, int render_target_h)
{
    TBRendererBatcher::BeginPaint( render_target_w, render_target_h );
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::EndPaint()
{
    TBRendererBatcher::EndPaint();
}

//=============================================================================
// TBRendererBatcher::AddQuadInternal function override
// ** move this to TurboBadger/renderers/tb_renderer_batcher.cpp once you understand the changes, as this function should be in the library
//=============================================================================
void UTBRendererBatcher::AddQuadInternal(const TBRect &dst_rect, const TBRect &src_rect, uint32 color, 
                                         TBBitmap *bitmap, TBBitmapFragment *fragment)
{
    if (batch.bitmap != bitmap)
    {
        batch.Flush(this);
        batch.bitmap = bitmap;
    }
    batch.fragment = fragment;

    // save clip rect
    // **note** the clipRect member var, as declared below, was added to the Batch class in tb_renderer_batcher.h
    // TBRect clipRect; 
    batch.clipRect = m_clip_rect;

    if ( bitmap )
    {
        // ** Urho3D adds UV offset when using DX, see:
        // https://github.com/urho3d/Urho3D/commit/0990fd72f239594fae113820233d1f858325f8dd
        #ifdef URHO3D_OPENGL
        float uvOffset = 0.0f;
        #else
        float uvOffset = 0.5f;
        #endif
        int bitmap_w = bitmap->Width();
        int bitmap_h = bitmap->Height();
        m_u  = (float)(src_rect.x + uvOffset)/ bitmap_w;
        m_v  = (float)(src_rect.y + uvOffset)/ bitmap_h;
        m_uu = (float)(src_rect.x + uvOffset + src_rect.w) / bitmap_w;
        m_vv = (float)(src_rect.y + uvOffset + src_rect.h) / bitmap_h;
    }

    // change triangle winding order to clock-wise
    Vertex *ver = batch.Reserve(this, 6);
    ver[0].x = (float) dst_rect.x;
    ver[0].y = (float) (dst_rect.y + dst_rect.h);
    ver[0].u = m_u;
    ver[0].v = m_vv;
    ver[0].col = color;
    ver[2].x = (float) (dst_rect.x + dst_rect.w);
    ver[2].y = (float) (dst_rect.y + dst_rect.h);
    ver[2].u = m_uu;
    ver[2].v = m_vv;
    ver[2].col = color;
    ver[1].x = (float) dst_rect.x;
    ver[1].y = (float) dst_rect.y;
    ver[1].u = m_u;
    ver[1].v = m_v;
    ver[1].col = color;

    ver[3].x = (float) dst_rect.x;
    ver[3].y = (float) dst_rect.y;
    ver[3].u = m_u;
    ver[3].v = m_v;
    ver[3].col = color;
    ver[5].x = (float) (dst_rect.x + dst_rect.w);
    ver[5].y = (float) (dst_rect.y + dst_rect.h);
    ver[5].u = m_uu;
    ver[5].v = m_vv;
    ver[5].col = color;
    ver[4].x = (float) (dst_rect.x + dst_rect.w);
    ver[4].y = (float) dst_rect.y;
    ver[4].u = m_uu;
    ver[4].v = m_v;
    ver[4].col = color;

    // Update fragments batch id (See FlushBitmapFragment)
    if (fragment)
        fragment->m_batch_id = batch.batch_id;
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::RegisterHandlers()
{
    // timer
    SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(UTBRendererBatcher, HandleUpdate));

    // screen resize and renderer
    SubscribeToEvent(E_SCREENMODE, URHO3D_HANDLER(UTBRendererBatcher, HandleScreenMode));
    SubscribeToEvent(E_BEGINFRAME, URHO3D_HANDLER(UTBRendererBatcher, HandleBeginFrame));
    SubscribeToEvent(E_POSTUPDATE, URHO3D_HANDLER(UTBRendererBatcher, HandlePostUpdate));
    SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(UTBRendererBatcher, HandlePostRenderUpdate));

    // inputs
    SubscribeToEvent(E_MOUSEBUTTONDOWN, URHO3D_HANDLER(UTBRendererBatcher, HandleMouseButtonDown));
    SubscribeToEvent(E_MOUSEBUTTONUP, URHO3D_HANDLER(UTBRendererBatcher, HandleMouseButtonUp));
    SubscribeToEvent(E_MOUSEMOVE, URHO3D_HANDLER(UTBRendererBatcher, HandleMouseMove));
    SubscribeToEvent(E_MOUSEWHEEL, URHO3D_HANDLER(UTBRendererBatcher, HandleMouseWheel));
    SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(UTBRendererBatcher, HandleKeyDown));
    SubscribeToEvent(E_KEYUP, URHO3D_HANDLER(UTBRendererBatcher, HandleKeyUp));
    SubscribeToEvent(E_TEXTINPUT, URHO3D_HANDLER(UTBRendererBatcher, HandleTextInput));
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    // msg timer
    double t = TBMessageHandler::GetNextMessageFireTime();

    if ( t != TB_NOT_SOON && t <= TBSystem::GetTimeMS() )
    {
        TBMessageHandler::ProcessMessages();
    }
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::HandleScreenMode(StringHash eventType, VariantMap& eventData)
{
    using namespace ScreenMode;

    OnResizeWin( eventData[P_WIDTH].GetInt(), eventData[P_HEIGHT].GetInt() );
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::HandleBeginFrame(StringHash eventType, VariantMap& eventData)
{
    TBAnimationManager::Update();
    root_.InvokeProcessStates();
    root_.InvokeProcess();
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::HandlePostUpdate(StringHash eventType, VariantMap& eventData)
{
    BeginPaint( root_.GetRect().w, root_.GetRect().h );

    root_.InvokePaint( TBWidget::PaintProps() );

    // If animations are running, reinvalidate immediately
    if ( TBAnimationManager::HasAnimationsRunning() )
    {
        root_.Invalidate();
    }
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
{
    EndPaint();
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::HandleMouseButtonDown(StringHash eventType, VariantMap& eventData)
{
    using namespace MouseButtonDown;

    int mouseButtons = eventData[P_BUTTONS].GetInt();
    int qualifiers = eventData[P_QUALIFIERS].GetInt();
    MODIFIER_KEYS modKey = (MODIFIER_KEYS)FindTBKey( qualifiers + QAL_VAL );

    // exit if not the left mb
    if ( mouseButtons != MOUSEB_LEFT )
    {
        return;
    }

    root_.InvokePointerDown( lastMousePos_.x_, lastMousePos_.y_, 1, modKey, false );
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::HandleMouseButtonUp(StringHash eventType, VariantMap& eventData)
{
    using namespace MouseButtonUp;

    int qualifiers = eventData[P_QUALIFIERS].GetInt();
    MODIFIER_KEYS modKey = (MODIFIER_KEYS)FindTBKey( qualifiers + QAL_VAL );

    root_.InvokePointerUp( lastMousePos_.x_, lastMousePos_.y_, modKey, false );
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::HandleMouseMove(StringHash eventType, VariantMap& eventData)
{
    using namespace MouseMove;

    int qualifiers = eventData[P_QUALIFIERS].GetInt();
    MODIFIER_KEYS modKey = (MODIFIER_KEYS)FindTBKey( qualifiers + QAL_VAL );
    lastMousePos_ = IntVector2( eventData[P_X].GetInt(), eventData[P_Y].GetInt() );

    root_.InvokePointerMove( lastMousePos_.x_, lastMousePos_.y_, modKey, false );
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::HandleMouseWheel(StringHash eventType, VariantMap& eventData)
{
    using namespace MouseWheel;

    int qualifiers = eventData[P_QUALIFIERS].GetInt();
    int delta = eventData[P_WHEEL].GetInt();
    MODIFIER_KEYS modKey = (MODIFIER_KEYS)FindTBKey( qualifiers + QAL_VAL );

    root_.InvokeWheel( lastMousePos_.x_, lastMousePos_.y_, 0, -delta, modKey );
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::HandleKeyDown(StringHash eventType, VariantMap& eventData)
{
    using namespace KeyDown;

    int qualifiers = eventData[P_QUALIFIERS].GetInt();
    int key = eventData[P_KEY].GetInt();
    MODIFIER_KEYS modKey = (MODIFIER_KEYS)FindTBKey( qualifiers + QAL_VAL );
    SPECIAL_KEY spKey = (SPECIAL_KEY)FindTBKey( key );

    // exit if not a special key
    if ( spKey == TB_KEY_UNDEFINED )
    {
        return;
    }

    root_.InvokeKey( key, spKey, modKey, true );
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::HandleKeyUp(StringHash eventType, VariantMap& eventData)
{
    using namespace KeyUp;

    int qualifiers = eventData[P_QUALIFIERS].GetInt();
    int key = eventData[P_KEY].GetInt();
    MODIFIER_KEYS modKey = (MODIFIER_KEYS)FindTBKey( qualifiers + QAL_VAL );
    SPECIAL_KEY spKey = (SPECIAL_KEY)FindTBKey( key );

    root_.InvokeKey( key, spKey, modKey, false );
}

//=============================================================================
//=============================================================================
void UTBRendererBatcher::HandleTextInput(StringHash eventType, VariantMap& eventData)
{
    using namespace TextInput;

    int qualifiers = eventData[P_QUALIFIERS].GetInt();
    int key = (int)eventData[ P_TEXT ].GetString().CString()[ 0 ];
    MODIFIER_KEYS modKey = (MODIFIER_KEYS)FindTBKey( qualifiers + QAL_VAL );

    root_.InvokeKey( key, TB_KEY_UNDEFINED, modKey, true );
}

//=============================================================================
// TB special and quality keys func
//=============================================================================
int UTBRendererBatcher::FindTBKey(int _ikey)
{
    HashMap<int, int>::Iterator itr = uKeytoTBkeyMap.Find( _ikey );
    int itbkey = 0;

    if ( itr != uKeytoTBkeyMap.End() )
    {
        itbkey = itr->second_;
    }

    return itbkey;
}

//=============================================================================
//=============================================================================
class UTBFile : public TBFile
{
public:
    UTBFile(Context *_pContext) 
        : ufileSize_( 0 )
    {
        pfile_ = new File( _pContext );
    }

    virtual ~UTBFile() 
    { 
        if ( pfile_ )
        {
            pfile_->Close();
            pfile_ = NULL;
        }
    }

    bool OpenFile(const char* fileName)
    {
        bool bopen = pfile_->Open( fileName );

        if ( bopen )
        {
            ufileSize_ = pfile_->Seek( (unsigned)-1 );
            pfile_->Seek( 0 );
        }

        return bopen;
    }

    virtual long Size()
    {
        return (long)ufileSize_;
    }

    virtual size_t Read(void *buf, size_t elemSize, size_t count)
    {
        return pfile_->Read( buf, elemSize * count );
    }

protected:
    SharedPtr<File> pfile_;
    unsigned ufileSize_;
};

//=============================================================================
// static
//=============================================================================
TBFile* TBFile::Open(const char *filename, TBFileMode )
{
    UTBFile *pFile = new UTBFile( UTBRendererBatcher::Singleton().GetContext() );
    String strFilename = UTBRendererBatcher::Singleton().GetDataPath() + String( filename );

    if ( !pFile->OpenFile( strFilename.CString() ) )
    {
        delete pFile;
        pFile = NULL;
    }

    return pFile;
}
[/code]
This worked with the latest of URHO3D (March 20 2016). I have the GUI displaying with this version (URHO 3D 1.5 GITHUB head revision 03/20/16).

-------------------------

Enhex | 2017-01-02 01:11:23 UTC | #30

BTW the licensing is messed up.
You got zlib license in the README.md, but all rights reserved in the source files.

-------------------------

Lumak | 2017-01-02 01:11:23 UTC | #31

My TB integration work is [url=https://opensource.org/licenses/MIT]MIT[/url], and that license has a precedence and covers everything that I have included in the repository (with exception to TB lib which is covered below) w/o having to recopy it in every file.
TB library has its own license - I've included the TB library link, the original author's link, and its license in the readme.md file.

Edit: should I remove TB lib license to avoid any confusion?

-------------------------

Enhex | 2017-01-02 01:11:23 UTC | #32

"Copyright (c) 2015 LumakSoftware" defaults to all rights reserved.
The safest option is to include the whole license in every file.
A shorter solution is to just say or add "look at file X for the license".
Or at least don't write anything so there are no conflicting statements.

You can put the TB license in a separate file (so when people scroll down and see "License" they don't confuse it to your license), but if you include TB in your repo then you can't remove it completely.

-------------------------

Lumak | 2017-01-02 01:11:23 UTC | #33

Added the license info in the repository. 
I already had the TB lib license in the Source/ThirdParty/TurboBadger/ section from day one, and I think it's more clear about my license having the TB license removed from the main readme page.  
Good call.

-------------------------

Enhex | 2017-01-02 01:11:23 UTC | #34

Thanks!

-------------------------

sabotage3d | 2017-01-02 01:13:56 UTC | #35

Anyone using TB for in-game UI or it is suitable only for debug editor?

-------------------------

jmiller | 2017-01-02 01:13:56 UTC | #36

[quote="sabotage3d"]Anyone using TB for in-game UI or it is suitable only for debug editor?[/quote]

Sure, have been using the other integration since it was posted: [topic1413.html](http://discourse.urho3d.io/t/turbo-badger-implementation/1364/1)
I've posted my Console widget there and I'm intending to post an animated+skinned radial menu widget soon. TB is fast, many-featured, and I like the retained mode.

[url=http://imgbox.com/SSproDGw][img]http://0.t.imgbox.com/SSproDGw.jpg[/img][/url]

-------------------------

sabotage3d | 2017-01-02 01:13:56 UTC | #37

Looks really nice. I think the other one is removed is there any public repo?

-------------------------

jmiller | 2017-01-02 01:13:57 UTC | #38

[quote="sabotage3d"]Looks really nice. I think the other one is removed is there any public repo?[/quote]

Just posted my working version in that thread.

-------------------------

