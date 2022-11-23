vivienneanthony | 2017-01-02 01:06:04 UTC | #1

Hi

Does anyone have any idea how to setup multithreading in Urho?

I have a application class(like the samples) that has a subclass(which is the application.). In the subclass I run a logiccomponent that gets a getline. It calls a event. Custom event that a handler in the application subclass has. It runs functions and code there.

I probably subclass  in  a derived class to keep everything neat.

There needs to be two threads. The main code and then the component-serverconsoleinterface needs to be in a separate thread. So, there is no conflicts.

Do anyone have any suggestion? The documentation on threads seems vague to me. Later on I want to add Telnet access to.

Vivienne

-------------------------

rasteron | 2017-01-02 01:06:05 UTC | #2

multithreading [topic885.html](http://discourse.urho3d.io/t/multithreading/864/1)

-------------------------

vivienneanthony | 2017-01-02 01:06:05 UTC | #3

[quote="rasteron"]multithreading [topic885.html](http://discourse.urho3d.io/t/multithreading/864/1)[/quote]

Yea. I'm looking at this code.


[code]    void AddSomeWork()
        {
                WorkQueue* queue = GetSubsystem<WorkQueue>();
                SharedPtr<WorkItem> item = SharedPtr<WorkItem>(new WorkItem);
                Log* log = GetSubsystem<Log>();
                item->aux_ = (void*)&log;
                item->workFunction_ = &DoingSomeMonkeyWork;
                item->sendEvent_ = true;
               
                queue->AddWorkItem(item);
        }[/code]

Specifically

[code]                item->workFunction_ = &DoingSomeMonkeyWork;[/code]

I am assuming thats where the bulk the thread creation. Baasically adding a Start function and starting the logiccomponent there.  

something like 

[code]item->workFunction= &ServerConsoleInterface -> Start();[/code]

-------------------------

cadaver | 2017-01-02 01:06:05 UTC | #4

I recommend using the WorkQueue & tasks only for short tasks that need to repeat from frame to frame and benefit from multicore scaling. Something like reading console input sounds like a job for the Thread class, which represents a long-lived thread and is fairly simple to use. Search "public Thread" from Urho code to see where it's being subclassed & used.

However, for this exact task the ProcessUtils.h also includes a non-blocking console read function, GetConsoleInput(), which you should be able to use in the main thread, so if it works well for you you shouldn't need to even create a thread.

-------------------------

vivienneanthony | 2017-01-02 01:06:05 UTC | #5

[quote="cadaver"]I recommend using the WorkQueue & tasks only for short tasks that need to repeat from frame to frame and benefit from multicore scaling. Something like reading console input sounds like a job for the Thread class, which represents a long-lived thread and is fairly simple to use. Search "public Thread" from Urho code to see where it's being subclassed & used.

However, for this exact task the ProcessUtils.h also includes a non-blocking console read function, GetConsoleInput(), which you should be able to use in the main thread, so if it works well for you you shouldn't need to even create a thread.[/quote]


Yea. I found the code.

[code]String GetConsoleInput()
{
    String ret;
    #ifdef URHO3D_TESTING
    // When we are running automated tests, reading the console may block. Just return empty in that case
    return ret;
    #endif

    #ifdef WIN32
    HANDLE input = GetStdHandle(STD_INPUT_HANDLE);
    HANDLE output = GetStdHandle(STD_OUTPUT_HANDLE);
    if (input == INVALID_HANDLE_VALUE || output == INVALID_HANDLE_VALUE)
        return ret;

    // Use char-based input
    SetConsoleMode(input, ENABLE_PROCESSED_INPUT);

    INPUT_RECORD record;
    DWORD events = 0;
    DWORD readEvents = 0;

    if (!GetNumberOfConsoleInputEvents(input, &events))
        return ret;

    while (events--)
    {
        ReadConsoleInputW(input, &record, 1, &readEvents);
        if (record.EventType == KEY_EVENT && record.Event.KeyEvent.bKeyDown)
        {
            unsigned c = record.Event.KeyEvent.uChar.UnicodeChar;
            if (c)
            {
                if (c == '\b')
                {
                    PrintUnicode("\b \b");
                    int length = currentLine.LengthUTF8();
                    if (length)
                        currentLine = currentLine.SubstringUTF8(0, length - 1);
                }
                else if (c == '\r')
                {
                    PrintUnicode("\n");
                    ret = currentLine;
                    currentLine.Clear();
                    return ret;
                }
                else
                {
                    // We have disabled echo, so echo manually
                    wchar_t out = c;
                    DWORD charsWritten;
                    WriteConsoleW(output, &out, 1, &charsWritten, 0);
                    currentLine.AppendUTF8(c);
                }
            }
        }
    }
    #elif !defined(ANDROID) && !defined(IOS)
    int flags = fcntl(STDIN_FILENO, F_GETFL);
    fcntl(STDIN_FILENO, F_SETFL, flags | O_NONBLOCK);
    for (;;)
    {
        int ch = fgetc(stdin);
        if (ch >= 0 && ch != '\n')
            ret += (char)ch;
        else
            break;
    }
    #endif

    return ret;
}[/code]

-------------------------

vivienneanthony | 2017-01-02 01:06:07 UTC | #6

[quote="cadaver"]I recommend using the WorkQueue & tasks only for short tasks that need to repeat from frame to frame and benefit from multicore scaling. Something like reading console input sounds like a job for the Thread class, which represents a long-lived thread and is fairly simple to use. Search "public Thread" from Urho code to see where it's being subclassed & used.

However, for this exact task the ProcessUtils.h also includes a non-blocking console read function, GetConsoleInput(), which you should be able to use in the main thread, so if it works well for you you shouldn't need to even create a thread.[/quote]

I have to look at the class. I'm trying to figure it out. It should be something simple.  Although to me it looks extremely vague.

-------------------------

vivienneanthony | 2017-01-02 01:06:07 UTC | #7

Is there any other example? All I want to do is run a component->Start() / class in another thread?

-------------------------

weitjong | 2017-01-02 01:06:07 UTC | #8

[quote="vivienneanthony"]All I want to do is run a component->Start() / class in another thread?[/quote]
Sounds like you need another "process" instead of "thread".

-------------------------

vivienneanthony | 2017-01-02 01:06:07 UTC | #9

[quote="weitjong"][quote="vivienneanthony"]All I want to do is run a component->Start() / class in another thread?[/quote]
Sounds like you need another "process" instead of "thread".[/quote]

Someone said to just focus on the Thread class.

I'm looking at [github.com/urho3d/Urho3D/blob/m ... orkQueue.h](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Core/WorkQueue.h) also.

Just not certain which method nor how. I know what I want to do just the method to do it I'm not clear about.

-------------------------

weitjong | 2017-01-02 01:06:08 UTC | #10

I am sorry if I have confused you further. Note that I was referring to "process" and "thread" in their general context. I was not referring to Urho3D::Thread class in particular. And I said "sounds like" only because I don't know for sure your actual use case. A process can have many threads, it can run an instance of your app separate from the other. On the server side programming, you usually hear people fork a process from the main process. All I want to say is, determine first what you need.

-------------------------

vivienneanthony | 2017-01-02 01:06:08 UTC | #11

[quote="weitjong"]I am sorry if I have confused you further. Note that I was referring to "process" and "thread" in their general context. I was not referring to Urho3D::Thread class in particular. And I said "sounds like" only because I don't know for sure your actual use case. A process can have many threads, it can run an instance of your app separate from the other. On the server side programming, you usually hear people fork a process from the main process. All I want to say is, determine first what you need.[/quote]

I was thinking the method would be start the program application class as normal and assign it as the main thread. Then start the servercontrolcomponent in another thread or child.

I am looking at Thread.h and Thread.cpp which I think I would have to use but I'm not certain how.

-------------------------

vivienneanthony | 2017-01-02 01:06:08 UTC | #12

After fooling around looking at some Urho source. I got this.

[code]vivienne@vivienne-System-Product-Name:~$ cd /media/home2/vivienne/GameEconomicUrho
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/GameEconomicUrho$ cd bin
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/GameEconomicUrho/bin$ ./GameEconomicServer
[Tue Jul 28 00:41:58 2015] INFO: Opened log file /home/vivienne/.local/share/urho3d/logs/GameEconomicServer.log
[Tue Jul 28 00:41:58 2015] INFO: Created 3 worker threads
[Tue Jul 28 00:41:58 2015] INFO: Added resource path /media/home2/vivienne/GameEconomicUrho/bin/Data/
[Tue Jul 28 00:41:58 2015] INFO: Added resource path /media/home2/vivienne/GameEconomicUrho/bin/CoreData/
[Tue Jul 28 00:41:58 2015] INFO: Initialized engine
Info: Loading database configuration .
Info: Loading database configuration successful.
Info: Database connection succesful. 
Info: Database Markets table found.
Info: Database MarketTransactions table found.
Info: Database Traders table found.
Info: Database CargoBays table found.
Info: Database CargoBayCatalog table found.
Info: Database Players table found.
Info: Database Accounts table found.
Headless Server Model 
Programmer Vivienne Anthony
 
Enter Command >> quit
Enter Command >> [Tue Jul 28 00:41:59 2015] ERROR: Sending events is only supported from the main thread
quit
Enter Command >> [Tue Jul 28 00:42:01 2015] ERROR: Sending events is only supported from the main thread
t
Enter Command >> [Tue Jul 28 00:42:03 2015] ERROR: Sending events is only supported from the main thread

Error. Invalid  command
Enter Command >> 
Error. Invalid  command
Enter Command >> 
[/code]

Why can't sub threads can't send events? Or can I force it to.

-------------------------

vivienneanthony | 2017-01-02 01:06:10 UTC | #13

[quote="weitjong"]I am sorry if I have confused you further. Note that I was referring to "process" and "thread" in their general context. I was not referring to Urho3D::Thread class in particular. And I said "sounds like" only because I don't know for sure your actual use case. A process can have many threads, it can run an instance of your app separate from the other. On the server side programming, you usually hear people fork a process from the main process. All I want to say is, determine first what you need.[/quote]

I think it's working now.

-------------------------

vivienneanthony | 2017-01-02 01:06:10 UTC | #14

[quote="cadaver"]I recommend using the WorkQueue & tasks only for short tasks that need to repeat from frame to frame and benefit from multicore scaling. Something like reading console input sounds like a job for the Thread class, which represents a long-lived thread and is fairly simple to use. Search "public Thread" from Urho code to see where it's being subclassed & used.

However, for this exact task the ProcessUtils.h also includes a non-blocking console read function, GetConsoleInput(), which you should be able to use in the main thread, so if it works well for you you shouldn't need to even create a thread.[/quote]

I used that code and it seems to work the only problem I have is when nothing is entered just "return". it returns 0 basically a empty string.

So, with the function itself I can't determine when a line is entered with just a return key. It's not a breaking thing. Just would be a nuisance.

I had to create a thread but it's minor.

-------------------------

cadaver | 2017-01-02 01:06:13 UTC | #15

Hm yes, that would be good to differentiate. Maybe return a string with just a CR or LF in that case, though they're normally stripped.

-------------------------

