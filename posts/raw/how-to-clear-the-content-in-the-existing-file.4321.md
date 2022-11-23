chenjie199234 | 2018-06-15 11:19:38 UTC | #1

just like the title.
now i have a file filled with old data and i want to use new data to cover it.
the problem is that,how to clear the file.
i can delete the file through enhine's subsystem,but i cant create a new one.there is no such api.
there is also no function to clear the file's content
there is also no more mode flags when we open the file,only read write.
so how to clear one file's content

-------------------------

Modanung | 2018-06-15 17:36:59 UTC | #2

Simply create a new file - instead of opening one - and save it over the other one.

Could you share some code if this doesn't clarify things?

-------------------------

SirNate0 | 2018-06-16 03:31:52 UTC | #3

Open the file as write only and I'm pretty sure it will create it if it doesn't exist and overwrite the contents if it does.

-------------------------

