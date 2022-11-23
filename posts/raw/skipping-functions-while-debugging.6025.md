SirNate0 | 2020-03-28 16:28:24 UTC | #1

When stepping through my programs while debugging I've often been annoyed by the extra steps through SharedPtr's operator ->. I've found the solution to it, though:
* For GDB https://sourceware.org/gdb/onlinedocs/gdb/Skipping-Over-Functions-and-Files.html
* For VS there are some links under tip 4 here (along with some other useful tips) https://dev.to/fenbf/11-visual-c-debugging-tips-that-will-save-your-time-2bam

-------------------------

