rku | 2017-10-16 14:52:20 UTC | #1

I implemented cooperative multitasking for Urho3D. Simply put you can now write code like this:

```cpp

void TasksSample::MushroomAI()
{
    // Implement mushroom logic.
    const char* mushroomText[] = {
        "Q: Mummy, why do all the other kids call me a hairy werewolf?",
        "A: Now stop talking about that and brush your face!",
        "Q: What did one thirsty vampire say to the other as they were passing the morgue?",
        "A: Let’s stop in for a cool one!",
        "Q: How can you tell if a vampire has a horrible cold?",
        "A: By his deep loud coffin!",
        "Q: What do skeletons say before eating?",
        "A: Bone Appetit!",
        "Q: Why did the vampire get fired from the blood bank?",
        "A: He was caught drinking on the job!",
        "Q: What is a vampire’s pet peeve?",
        "A: A Tourniquet!",
    };

    // This task runs as long as title node exists in a scene.
    WeakPtr<Node> titleNode(scene_->GetChild("MushroomTitle", true));
    for (;!titleNode.Expired();)
    {
        auto index = Random(0, SDL_arraysize(mushroomText) / 2);
        auto text3D = titleNode->GetComponent<Text3D>();

        // Mushroom says a joke question
        text3D->SetText(mushroomText[index * 2]);
        // And waits for 5 seconds. This does not block rendering.
        SuspendTask(5.f);

        // After 5 seconds mushroom tells an answer.
        text3D->SetText(mushroomText[index * 2 + 1]);
        SuspendTask(3.f);

        // And after 3 more seconds laughs.
        text3D->SetText("Hahahahaha!!!");
        // Next joke comes after 3 seconds.
        SuspendTask(3.f);

        // SuspendTask() may be called without arguments. Execution will be resumed on the next frame.
        SuspendTask();
    }
}

void TasksSample::SubscribeToEvents()
{
    // Create a task that will be scheduled each time E_UPDATE event is fired.
    GetTasks()->Create(E_UPDATE, std::bind(&TasksSample::MushroomAI, this));
}
```

`MushroomAI()` code is written as if it executed sequentially and yet `SuspendTask()` calls do not block rendering even though code runs on the main thread. If you wish you may implement task scheduling on other threads as well. It is implemented in a cross-platform and efficient way. On windows it uses fiber API. On unixes it uses ucontext for first context switch and _setjmp/_longjmp for following context switches. No assembly code used.

Code:
* [Tasks.h](https://github.com/rokups/Urho3D/blob/master/Source/Urho3D/Core/Tasks.h)
* [Tasks.cpp](https://github.com/rokups/Urho3D/blob/master/Source/Urho3D/Core/Tasks.cpp)
* [Full sample code](https://github.com/rokups/Urho3D/blob/master/Source/Samples/101_Tasks/Tasks.cpp)

Joke-telling npc mushroom from the sample:
![2|640x351](upload://1EYGlAD9S77pP609A8DRE7d3d0g.gif)

-------------------------

TrevorCash | 2017-10-16 18:30:59 UTC | #2

This looks awesome - can you start tasks with function arguments?

-------------------------

Eugene | 2017-10-16 18:32:01 UTC | #3

It looks great, but I am afraid that it has bad portability among platforms.

-------------------------

George1 | 2017-10-17 02:58:22 UTC | #4

Great work.

Instead of time out, how can we use this coroutine to wait for a signal or a returned object before continue with the next or subsequence or parallel tasks?

These has lots of application. E.g. parallel path findings, state machines, discrete event etc.

-------------------------

rku | 2017-10-17 07:18:29 UTC | #5

[quote="TrevorCash, post:2, topic:3665, full:true"]
This looks awesome - can you start tasks with function arguments?
[/quote]

Sure, use `std::bind`:

```cpp
void MyClass::MyMethod(int val)
{
    assert(val == 2);
}
GetTasks()->Create(std::bind(&MyClass::MyMethod, this, 2));
```

[quote="Eugene, post:3, topic:3665, full:true"]
It looks great, but I am afraid that it has bad portability among platforms.
[/quote]

What do you mean? It would run perfectly on platforms that support ucontext and some version of c standard, which is just about any platform supported by urho. Including MacOS (although it is true that they deprecated ucontext), iOS, Android, raspberry pi, arm/arm64/x86/x64. I am not so sure how it would fare on consoles. One thing that i am sure of - if this does not work on certain platforms then it is not too hard to make it work ;)

[quote="George1, post:4, topic:3665"]
Instead of time out, how can we use this coroutine to wait for a signal or a returned object before continue with the next or subsequence or parallel tasks?

These has lots of application. E.g. parallel path findings, state machines, discrete event etc.
[/quote]

Sure you can. What you would do is:
```cpp
if (isConditionSet)
{
    // signal was received, do things
}
SuspendTask();    // Schedule other tasks, resume on next frame.
```

Or you can manually switch to tasks. API still needs a bit of work to allow sidestepping scheduler completely, but in theory you can totally do `task->SwitchTo()`, task is scheduled and execution resumes after this method call as soon as task calls `SuspendTask()`.

-------------------------

George1 | 2017-10-17 07:52:25 UTC | #6

Look great.
Where would you put that signal condition check inside the tasks code so that it execute immediately on signal.
Could you make a small sample for this?

How would you do to suspend or interrupt other tasks from a different task?
Or could you possible sending object or signal immediately between tasks? For example sending to interrupt and changing task at the current frame.

-------------------------

rku | 2017-10-17 07:59:38 UTC | #7

[quote="George1, post:6, topic:3665"]
Where would you put that signal condition check inside the tasks code so that it execute immediately on signal.

Could you make a small sample for this?
[/quote]

That is not how tasks work. Tasks are like micro-threads. If you want task to resume when some signal is sent you probably want to do it manually - receive signal and call `task->SwitchTo()` which will schedule task.

[quote="George1, post:6, topic:3665"]
How would you do to suspend or interrupt other tasks from a different task?
[/quote]
Same way as you would do it with threads: set condition variable somewhere and have task check it constantly. You do not want to have and use `task->Terminate()` for example, because it would free task stack without unwinding it and possibly cause memory leaks.

[quote="George1, post:6, topic:3665"]
Or could you possible sending object or signal immediately between tasks? For example sending to interrupt and changing task at the current frame.
[/quote]
You would have to implement that part. Maybe like some kind of queue that task is constantly checking, getting items from it and processing once you put something in there?

-------------------------

George1 | 2017-10-17 08:09:31 UTC | #8

Thanks,
I'm just raising a few questions to understand the capability of the implementation.

The reason I'm asking about interrupt and signal is when you would use it for ai character, where the ai could do multiple tasks concurrently.

Best regards

-------------------------

rku | 2017-10-17 08:21:19 UTC | #9

Yes, that is exactly the point of task system - doing multiple things at one (but not in parallel).

For example you could have `AttackTask()` which actively looks for enemies around and attacks them.

Then you could have `HealTask()` which checks HP every X seconds and consumes healing potions.

Then you could have `ReactTask()` which would check HP every X seconds and once it reaches 10% or less it would make NPC scream "AHHHH!!!" and flee.

Now logical thing would be to terminate `AttackTask()` when `ReactTask()` initiates fleeing. NPC could have `state_` member variable which could be `AGGRESSIVE` or `FRIGHTENED`, and `AttackTask()` then would only make NPC attack if it is in `AGGRESSIVE` state.


Not the best AI design but i hope it illustrates how to do things concurrently.

-------------------------

rku | 2017-10-17 11:45:32 UTC | #10

@George1 i worked on it a bit more and added `task->Terminate()` method to request task termination. `SuspendTask()` throws exception in the task, this unwinds the stack properly and prevents any memory leaks i mentioned earlier. If exception cost is too high you may manually keep checking `task->IsTerminating()` before every `SuspendTask()` call and return from the task, avoiding throwing exception.

Updated sample, adding multiple examples to that worker thread function demonstrating how various things work. Also added example on how to manually schedule tasks without using task scheduler.

Hope you find it useful

-------------------------

