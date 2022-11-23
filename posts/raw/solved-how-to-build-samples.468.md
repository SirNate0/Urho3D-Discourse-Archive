rogerdv | 2017-01-02 01:00:40 UTC | #1

Do I need any specific directive to compile c++ samples? Im trying to foind them after compiling the engine and cant find any.

[b]Found it in the docs![/b]

-------------------------

thebluefish | 2017-01-02 01:00:40 UTC | #2

By default, CMAKE won't generate the samples. Here's how I would generate a VS2013 solution (just a manual edit to cmake_vs2013.bat):

[code]
@%~dp0\cmake_vs2008.bat VERSION=12 -DURHO3D_SAMPLES=1 %*
[/code]

-------------------------

rogerdv | 2017-01-02 01:00:41 UTC | #3

Thanks, I will use that to compile the Win version.

-------------------------

