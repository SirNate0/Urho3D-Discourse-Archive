imxqliu | 2017-01-02 01:10:14 UTC | #1

Hi, gus
   while I run sample NO.1 on a destop(i7-4790, windows7 64bit), I find it create 3 threads in helloworld.log, but on my laptop(Intel i5-3210m, windows10 64bit) only one thread. this problem confused me a lot , will you have  any opinions?
    thanks.

-------------------------

weitjong | 2017-01-02 01:10:14 UTC | #2

As I understood how the engine works, it only counts physical CPU and use that number minus 1 as one of the core is reserved for main thread. Your desktop CPU has 4 cores, so 3 worker threads looks correct to me. Your mobile CPU has 2 cores, so only 1 worker thread being used is also correct. The main thread is not being mentioned in the log but of course it is there.

-------------------------

imxqliu | 2017-01-02 01:10:18 UTC | #3

weitjong,thanks.

-------------------------

