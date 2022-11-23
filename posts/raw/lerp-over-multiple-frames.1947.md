godan | 2017-01-02 01:11:44 UTC | #1

I'm wondering what the "Urho" way would be to implement the following behavior:

Say I have an Object at Position A. I would like to move it to Position B. But, I would like this move to happen smoothly over, say, 100 frames. 

So here are some thoughts:

[ul]
1. Ideally, I would like to emulate Unity's Coroutine architecture.
2. I'm familiar with the WorkQueue. However, my understanding is that it is not safe to modify scene too much from a threaded function, so while the above example might work, in general, this is not the way. And in fact, as I write this, I'm pretty sure that using a WorkItem wouldn't help anyway...
3. There is most likely a way to do this by implementing some behavior in the Update loop. But this is a bit ugly IMO, since you end up with a bunch of code in your Update loop that is only rarely used. For instance, you would write something like:

[code]
if(shouldMove)
{
 if(!IsAtTarget())
 {
  StepTowardsTarget(target, stepSize);
 }
}
[/code]
But this check needs to happen every frame, regardless of whether or not you want to move. Better would be to have a function that can yield control back to the main thread...
[/ul]
Unless I'm missing something (which is likely :slight_smile:) it seems that such behavior is a bit of a hassle to implement. I've done a bit of reading on how to implement coroutines in C++, but I'm no expert, so all input is welcome. I know that Boost has a coroutine module, but, well...I'm not sure if I want to include Boost in my projects.

-------------------------

cadaver | 2017-01-02 01:11:44 UTC | #2

Like you observed, using the WorkQueue is certainly wrong for this kind of task.

Some things that come to mind is using ValueAnimation, or writing your own manager to which you can submit objects/attributes to be modified over time, or object methods to be called periodically. The manager would listen to frame events, freeing your per-object update code from having to do that. The ScriptInstance (AngelScript) already provides a delayed or delayed repeating method call mechanism.

Actual coroutines go against pure C++ which cannot readily manipulate the actual CPU stack (you could use assembly, or setjmp/longjmp, but that goes easily into nonportable or crashprone territory.)

-------------------------

godan | 2017-01-02 01:11:45 UTC | #3

K, thanks!

I think the manager idea is probably the way forward in my case. It seems like it should be possible to make this reasonably general. Maybe something like the WorkQueue/WorkItem, but on the main thread. The WorkItems have a function pointer and some configuration data, like a stopping condition, etc....

-------------------------

