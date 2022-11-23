Enhex | 2017-01-02 01:04:40 UTC | #1

[img]https://pbs.twimg.com/media/CCYraj7UMAEaG7t.jpg:large[/img]

Repo dump:
[github.com/Enhex/Urho3D-CEF3](https://github.com/Enhex/Urho3D-CEF3)

Two problems:
1. CEF3 crashes on shutdown.
2. CEF3 provides BGRA pixel format, Urho3D's Texture2D is RGBA by default and I couldn't find an Urho3D BGRA. Manual conversion should be possible.
Tried to ask about it here: [topic1019.html](http://discourse.urho3d.io/t/solved-texture2d-bgra-format/991/1)

-------------------------

GoogleBot42 | 2017-01-02 01:04:40 UTC | #2

Nice!   :wink:   How difficult was it to do out of curiosity?

-------------------------

Enhex | 2017-01-02 01:04:41 UTC | #3

[quote="GoogleBot42"]Nice!   :wink:   How difficult was it to do out of curiosity?[/quote]
Getting it to render wasn't difficult. I followed this example: [github.com/qwertzui11/cef_osr](https://github.com/qwertzui11/cef_osr)
CEF3 does everything internally, you just set it up, run it, and shut it down.
I spent most of the time trying to find a way to make CEF3 shut down without crashing.

-------------------------

gunnar.kriik | 2017-01-02 01:04:43 UTC | #4

That's pretty cool! 

By the way, the reason CEF is crashing on you on exit may be because you're not initializing it correctly. I quickly tested out your code on Linux (which didn't work out of the box), and realised that you need to setup your main function differently. CEF spawns multiple processes since it does JS + rendering in a separate process, so it invokes the "parent" process multiple times. You need to take this into account, or define a separate subprocess for CEF to spawn (CefSettings.browser_subprocess_path). 

I have not tested this on Windows, but I did my best to "blind code" to make this work. Have a go and see how it works for you.

First, remove everything CEF related from the MyApp constructor (MyApp.cpp):
[code]
//
// Constructor
//
MyApp::MyApp(Context* context) :
Application(context)
{
}
[/code]

You need more control over the main function when dealing with CEF3 (unless you define a separate subprocess), so skip the Urho3D DEFINE_APPLICATION_MAIN() macro for now (main.cpp):
[code]
#include "MyApp.hpp"
#include "include/cef_app.h"

#include <iostream>

#if !defined(WIN32)
#include <unistd.h>
#endif

using std::cout;
using std::endl;

//DEFINE_APPLICATION_MAIN(MyApp)

int RunApplication()
{
  Urho3D::Context* context = new Urho3D::Context();
  MyApp* application = new MyApp(context);
  return application->Run();
}

#if defined(WIN32)
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE prevInstance, PSTR cmdLine, int showCmd)
#else
int main(int argc, char** argv)
#endif
{

  #if !defined(WIN32)
  pid_t t_pidid = getpid();
  cout << "Spawning process [" << t_pidid << "] int main(argc, argv);" << endl;
  #endif

  #if defined(WIN32)
  CefMainArgs args(hInstance);
  #else
  CefMainArgs args(argc, argv);
  #endif
  {
    // https://bitbucket.org/chromiumembedded/cef/wiki/GeneralUsage
    // By default the main application executable will be spawned multiple times to represent separate processes.
    // This is handled via command-line flags that are passed into the CefExecuteProcess function.
    // If the main application executable is large, takes a long time to load, or is otherwise unsuitable for non-browser processes the host can use a
    // separate executable for those other processes. This can be configured via the CefSettings.browser_subprocess_path variable.
    // See the ?Application Structure? section for more information.
    int result = CefExecuteProcess(args, nullptr, nullptr);
    // checkout CefApp, derive it and set it as second parameter, for more control on
    // command args and resources.
    if (result >= 0) // child proccess has endend, so exit.
    {
      return result;
    }
    if (result == -1)
    {
        // we are here in the father proccess.
    }
  }

  CefSettings settings;

  // checkout detailed settings options http://magpcss.org/ceforum/apidocs/projects/%28default%29/_cef_settings_t.html
  settings.windowless_rendering_enabled = true;
  //settings.no_sandbox = 1; // Use this to run without sandbox
  //settings.single_process = true;
  //settings.multi_threaded_message_loop = true;

  bool result = CefInitialize(args, settings, nullptr, nullptr);
  // CefInitialize creates a sub-proccess and executes the same executeable, as calling CefInitialize, if not set different in settings.browser_subprocess_path
  // if you create an extra program just for the childproccess you only have to call CefExecuteProcess(...) in it.
  if (!result)
  {
    // handle error
    return 0;
  }

  Urho3D::ParseArguments(argc, argv);
  return RunApplication();
}
[/code]

Added some Linux specific process debug output here, so don't worry about that, just wanted to demonstrate what is going on. Output of process:
[code]
[gunnar@G750JX Bin_Release]$ ./cef3_test -x 1280 -y 800
Spawning process [6477] int main(argc, argv);
Spawning process [1] int main(argc, argv);
[Wed Apr 15 22:04:27 2015] INFO: Opened log file Urho3D.log
[Wed Apr 15 22:04:27 2015] INFO: Created 3 worker threads
[Wed Apr 15 22:04:27 2015] INFO: Added resource path /home/gunnar/code/Urho3D-CEF3/Bin_Release/Data/
[Wed Apr 15 22:04:27 2015] INFO: Added resource path /home/gunnar/code/Urho3D-CEF3/Bin_Release/CoreData/
Spawning process [6497] int main(argc, argv);
[0415/220427:FATAL:scoped_file.cc(29)] Check failed: 0 == IGNORE_EINTR(close(fd)). : Bad file descriptor
[Wed Apr 15 22:04:27 2015] INFO: Set screen mode 1920x1080 fullscreen
[Wed Apr 15 22:04:27 2015] INFO: Initialized input
[Wed Apr 15 22:04:27 2015] INFO: Initialized user interface
[Wed Apr 15 22:04:27 2015] INFO: Initialized renderer
[Wed Apr 15 22:04:27 2015] INFO: Set audio mode 44100 Hz stereo interpolated
[Wed Apr 15 22:04:27 2015] INFO: Initialized engine
[0415/220429:WARNING:channel.cc(547)] Failed to send message to ack remove remote endpoint (local ID 1, remote ID 1)
[0415/220429:WARNING:channel.cc(547)] Failed to send message to ack remove remote endpoint (local ID 2147483648, remote ID 2)
[/code]

As you can see, the process is invoked three times (not sure about what the process with ID=1 is), but what you get is the "main" process that contains your application logic (Urho3D in this case), and a separate process that does the V8 JS processing and Blink rendering.
[code]
Spawning process [6477] int main(argc, argv);
Spawning process [1] int main(argc, argv);
Spawning process [6497] int main(argc, argv);
[/code]

I'm actually surprised it worked on Windows at all..

-------------------------

grumbly | 2017-01-02 01:04:44 UTC | #5

Great job getting this working!

I ran into a similar problem with the color channel reading incorrectly while getting Awesomium working with Urho3D a while ago (it displayed all red as blue). It turned out I was reading the Awesomium texture buffer incorrectly when copying to a texture Urho could display. Maybe seeing what I did will help? Or not :slight_smile:

[code]
if (bmsurface->is_dirty()) {
 bmsurface->CopyTo(buff, txtwidth*4, 4, true, false);
 renderTexture->SetData(0, 0, 0, txtwidth, txtheight, buff);
}
[/code]

-------------------------

gunnar.kriik | 2017-01-02 01:04:44 UTC | #6

[quote]it displayed all red as blue[/quote]

Right, Urho3D assumes the buffer is in RGBA, while CEF outputs BGRA. While swapping the buffer like you suggest would work fine, it would mean iterating through the entire buffer yet once more which would add an additional performance hit. It would be faster to swap the channels in the shader that displays the buffer. Or, BGRA texture format support could be added to Urho3D. I know OpenGL supports BGRA textures, and probably Direct3D aswell.

-------------------------

rasteron | 2017-01-02 01:07:17 UTC | #7

Clearly I have missed this one a few months ago when I was inactive here. Anyway, this is a cool integration Enhex! Great work and share, thanks!  :slight_smile:

-------------------------

Bananaft | 2017-01-02 01:07:17 UTC | #8

Hmmm, interesting. But can you run Urho HTML5 samples on it?

-------------------------

Enhex | 2017-01-02 01:07:17 UTC | #9

[quote="Bananaft"]Hmmm, interesting. But can you run Urho HTML5 samples on it?[/quote]
hehe, nice one.
Or even more interesting - run Urho HTML5 sample of CEF3 integration in the CEF3 integration sample.

-------------------------

Lumak | 2017-01-02 01:13:57 UTC | #10

This is exactly what I've been looking for.  Thank you for this!

-------------------------

rku | 2017-01-02 01:13:58 UTC | #11

This must be pretty slow right? I mean once you get into things like css animations etc.. Last time i checked it had no gpu acceleration whatsoever.

-------------------------

Lumak | 2017-01-02 01:14:02 UTC | #12

Yay, got it done.

[video]https://youtu.be/vnZ_7toWA0A[/video]

Forgot to capture the frame rate: that's the low end, averages about 185.

[img]http://i.imgur.com/ON04L8c.jpg[/img]

-------------------------

Mike | 2017-01-02 01:14:02 UTC | #13

Awesome  :stuck_out_tongue:

-------------------------

Miegamicis | 2017-01-02 01:14:04 UTC | #14

Awesome work! Thank you for sharing!  :slight_smile:

-------------------------

Lumak | 2017-01-02 01:14:13 UTC | #15

I have added my CEF integration derived from Enhex's code - [url]https://github.com/Lumak/CefIntegration[/url]

-------------------------

Lumak | 2017-01-02 01:14:13 UTC | #16

Added color correction and perhaps, a better shutdown sequence.

-------------------------

Lumak | 2017-01-02 01:14:13 UTC | #17

added a few mouse events.

-------------------------

Enhex | 2017-01-02 01:14:17 UTC | #18

Nice to see it being picked up and fixed, ty Lumak :slight_smile:

-------------------------

Lumak | 2017-01-02 01:14:18 UTC | #19

The benefits of open source, you get to build on others work :slight_smile:

[img]http://i.imgur.com/2lgz1Vu.jpg[/img]

-------------------------

sabotage3d | 2017-01-02 01:15:03 UTC | #20

Is it possible to get callbacks to C++ with HTML5 based UI for example?

-------------------------

TheSHEEEP | 2017-01-02 01:15:06 UTC | #21

Sure.
That's one of the main points of CEF, I'd say :slight_smile:

It's samples are actually pretty good to get started, especially combined with the wiki.
Not that all questions would be answered, but when do they ever?

-------------------------

sabotage3d | 2017-01-02 01:15:06 UTC | #22

Have anyone tried this one mobile? Would be interested to see what is the frame-rate?

-------------------------

Lumak | 2017-01-02 01:15:06 UTC | #23

Here is a list of CEF prebuild libs: [url]http://opensource.spotify.com/cefbuilds/index.html[/url]

I don't know if it's even possible to build CEF lib for Android.  I haven't been to their wiki since I've completed the port sometime ago, maybe that's changed.

-------------------------

sabotage3d | 2017-01-02 01:15:08 UTC | #24

There is an experimental branch that might compile for arm. Is there any alternatives to this that would work for mobile out of the box?

-------------------------

