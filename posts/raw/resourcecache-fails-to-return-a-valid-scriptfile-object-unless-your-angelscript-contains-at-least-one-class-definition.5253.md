Leith | 2019-06-26 07:05:48 UTC | #1

I wrote a small AngelScript containing a free function.
When I tried to load it via ResourceCache, I found it returned nullptr - even though the script compiled ok. I noticed that when I added a small dummy class to the script, all of a sudden I was getting a valid ScriptFile object from the ResourceCache, and I could call my free function.
I was wondering why ResourceCache is making the assumption that a script module bereft of object classes is somehow invalid?

-------------------------

SirNate0 | 2019-06-25 16:21:33 UTC | #2

Do you get a "Failed to compile script module" in the log when you try to load the class-less file?

-------------------------

Leith | 2019-06-26 01:42:49 UTC | #3

No! the script compiled perfectly - just ResourceCache refused to hand back the ScriptFile object unless I added the following unreferenced dummy class:

[code]
class dummy{
     int x;
     int y;
}

int MyFreeFunction( ... 
[/code]

Once I added the dummy class, ResourceCache was happy to give me access to the compiled module, and let me execute my free function... seems like ResourceCache has some requirement that a script must contain a class definition, even if it's never referenced...

-------------------------

SirNate0 | 2019-06-26 03:58:59 UTC | #4

Really strange. I don't see how that can happen if you're seeing the "Compiled script module [name]" message in the log. Unless someone else has some insight you might be left with just stepping through the GetResource call until you find where the loading fails.

-------------------------

Leith | 2019-06-26 06:53:09 UTC | #5

Looks that way :slight_smile:
To be honest, the workaround is not a deal-breaker, I just found it a little odd..
I can reproduce the issue in about 3 lines of code, it's repeatable.
So can you.

I wanted to clarify since the title of my post may be misleading...

- Register the scripting subsystem with urho3d.
        Script* script=new Script(context_);
        context_->RegisterSubsystem(script);
- Create an angelscript textfile, containing a dummy function.
void ThisDoesNothingButCompilesFine { } and save it in your resource folder.

- Try to  access the script file via resourcecache:
ScriptFile* file = GetSubsystem<ResourceCache>()->GetResource<ScriptFile>("Scripts/TestScript.as");

Without a dummy class in the script file, I am betting you get file==nullptr, while the log suggests that compile was successful.

I did tests with various forms of function declaration, the resourcecache lets us down every time, except if there is at least one class somewhere in the script, even if we never mention it anywhere else.

-------------------------

Leith | 2019-06-26 07:02:59 UTC | #6

Stepping through GetResource is not a great option for a couple of reasons.
- CodeBlocks on Linux is super slow when symbolic lookups are enabled
- I link to a static, release build of the lib in most cases
- I'm still new to using GDB outside of an IDE

It's actually faster for me to google the sourcecode to that class, and stare down the code for that method, in most cases anyway. It's even faster than digging around in the sourcecode itself, which I already have, obviously. But with less motions of my body, I can often deduce the answer using nothing more than google and searching the plaintext of the sourcecode for keywords.

Usually, if something crashes, I can just hop into the disassembler, see where I landed, examine my cpu registers, and deduce the issue, like a boss. But if I am returned a bad state with no errors generated, and it does not crash (hey maybe there is an exception handler chain?) then it gets harder to do that without, as you suggested, actually stepping through the code.

I hate silent errors - exception handling is often a culprit, but I really hate late error checking where no last moment error information was provided at all.

"Hey, everything is good" - here is your nullptr. Have a nice day.

-------------------------

guk_alex | 2019-06-26 07:57:10 UTC | #7

There are a bunch of places inside GetResource and down the Resource class where nullptr can be returned. It certainly will be faster to simply stepping through the code with debugger (or setting brakepoints in certain places) then guessing why that could happen.

-------------------------

Leith | 2019-06-26 11:04:56 UTC | #9

Why the (very rude expression in four letter terms) is no error information emitted in these cases? I mean - really? We are the point of error, we have error logging, and we did what? I find this dismal, useless and definitely not good enough. This is not how we grow, this is how we hide.

-------------------------

