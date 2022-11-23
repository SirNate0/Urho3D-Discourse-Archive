Stymgade | 2017-01-02 01:01:38 UTC | #1

This is actually a two-parter: I made a test .exe that does nothing but do the 'Hello World' without using the Sample class - this works perfectly fine.

My existing design  (migrating from Ogre) has 3 binaries involved:
[ul]
[li]The main exe, which calls a GraphicsEngine::Run[/li]
[li]The Urho3D 'Interaction' dll, which contains the class inheriting from Urho3D::Application[/li]
[li]The dll where the bulk of the code resides, which contains the GraphicsEngine class, and which creates the Urho3D::Application subclass.[/li][/ul]

Using the exact code from the test exe, putting it into the aforementioned dll (and exporting it), and running the application, results in an endless loop due to it apparently not being the 'main thread' (I've created no threads in my own code at this stage). I can post code if this isn't clear, which I don't think it is  :smiley: 

Which results my main question: Why does it not register as a main thread, or how can I make it do so? I had a quick look over the documentation but could only see the multithreading reference.

This leads onto the problem in the actual code:

Line 252 in Log.cpp:
[code]void Log::HandleEndFrame(StringHash eventType, VariantMap& eventData)
{
    MutexLock lock(logMutex_);
    
    // Process messages accumulated from other threads (if any)
    while (!threadMessages_.Empty())	
    {
        const StoredLogMessage& stored = threadMessages_.Front();
        
        if (stored.level_ != LOG_RAW)
            Write(stored.level_, stored.message_);
        else
            WriteRaw(stored.message_, stored.error_);
        
        threadMessages_.PopFront();
    }
}[/code]
This obviously pops off one message each time, decrementing the total - fair enough. 

The problem is in the called Log::Write, line 132:
[code]void Log::Write(int level, const String& message)
{
    assert(level >= LOG_DEBUG && level < LOG_NONE);

    // If not in the main thread, store message for later processing
    if (!Thread::IsMainThread())
    {
        if (logInstance)
        {
            MutexLock lock(logInstance->logMutex_);
            logInstance->threadMessages_.Push(StoredLogMessage(message, level, false));
        }
        
        return;
    }
    ...[/code]

If it's not the main thread, and logInstance is valid, the log entry gets pushed back onto the list. This results in the endless loop I was encountering. I'm only getting this due to the incorrect main thread assignment (which I'd appreciate for how to fix!), but it's clearly possible to result in the endless loop in other situations.

-------------------------

Stymgade | 2017-01-02 01:01:39 UTC | #2

Ok, after much debugging I found the issue: crossing DLL boundaries.

It seems the second it entered any function within the DLL, the mainThreadID was 0, hence triggering the invalid main thread - despite the fact the same compiler was used for all projects, and to compile the engine itself. The answers here provide a decent explanation: [url]http://stackoverflow.com/questions/22797418/how-do-i-safely-pass-objects-especially-stl-objects-to-and-from-a-dll[/url].

Luckily, I have no real need to have it in a separate DLL, so I've just converted the project to a static library and am linking to it with the main exe as a workaround.

The potential for the endless loop still exists however, so I'll add it to the issue tracker separately.

-------------------------

