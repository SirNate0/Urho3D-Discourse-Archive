Sunc | 2022-02-21 08:25:49 UTC | #1

For example, common techniques support this feature by creating another thread to do rendering commands execution, one or two command queue is maintained.

-------------------------

Eugene | 2022-02-21 08:42:15 UTC | #2

While *some* rendering-related work is outsourced to worker threads, Urho uses single draw command queue executed in the main thread.

-------------------------

