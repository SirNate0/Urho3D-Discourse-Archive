codingmonkey | 2017-01-02 01:03:38 UTC | #1

Hi folks! Today I tried to deal with multithreading.
I have something has been done and it works.
for the test, I concluded numbers to the console from another thread.
Here are the basic pieces of code.

[pastebin]fidfpQKQ[/pastebin]

But I have some questions.

for what purpose is WorkItem-> aux_ ?
and what is the difference of aux from item-> start_ or item-> end_?  
is they can not be assigned the same thing ?

-------------------------

cadaver | 2017-01-02 01:03:38 UTC | #2

You can use the variables like you want, they're only for the worker function and are not touched by anything else. Typically a worker function would process a range of items from start_ to end_ and maybe use some auxiliary data structure (aux_). A future improvement would perhaps be to simply subclass the worker task and remove those hardcoded variables.

-------------------------

codingmonkey | 2017-01-02 01:03:39 UTC | #3

And how many of these work items user can create ?

Let's say if I write a component that prepares the dynamic geometry in a work item (thread) on the current frame and on the next frame if the data is ready, they are copied into the main thread into the vertex buffer.

And if such components in the scene will be 100, it will create 100 threads at same time or still have 1 - 4 threads ? 
I mean these workers are create really new thread or they push all new-incoming works into some already existed threads ?

-------------------------

cadaver | 2017-01-02 01:03:39 UTC | #4

They are pushed into a queue from which the worker threads take work to execute. New threads will not be spawned per item, so you can use as many work items as you want. By default the engine creates as many worker threads as there are physical CPU cores. 

One thing you want to note is the work item priority. The rendering system uses work items of priority 0xffffffff (maximum) to execute work it needs to complete immediately, but split onto several cores. For example culling. So if you want to make tasks that can take several frames to update, use lower priority.

One more thing, that is easy to trip over: Urho's shared pointers (or more accurately, the reference counter inside) are not thread-safe, so make sure you're not manipulating them from the work functions and main thread simultaneously. Copying a shared pointer changes the ref count and counts as manipulation as well.

-------------------------

1vanK | 2017-01-02 01:13:57 UTC | #5

[urho3d.github.io/documentation/ ... ading.html](https://urho3d.github.io/documentation/1.6/_multithreading.html)
[quote]
When making your own work functions or threads, observe that the following things are unsafe and will result in undefined behavior and crashes, if done outside the main thread:

Modifying scene or UI content[/quote]

As far as I understand, this means a depreciation of creating and deleting of nodes. But it is allowed nodes transformation in a background thread?

EDIT: Is the event system thread-safe? If I add tag to Node in bacground thread it call SendEvent. Does it problems?

-------------------------

