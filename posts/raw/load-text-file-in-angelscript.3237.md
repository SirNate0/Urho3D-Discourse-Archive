lexx | 2017-06-10 13:58:56 UTC | #1

Can I load .txt file in AngelScript (to string) ?
Somehow using resource cache (there are xml and json but I need .txt loader) ?

-------------------------

lezak | 2017-06-10 11:15:13 UTC | #2

1. Create and open file:
    File@ file = File();
    file.Open("full path to Your txt file", FILE_READ);
or just:
    File@ file = File("full path to Your txt file, FILE_READ);

2. Read String:
    String s = file.ReadString();
or:
    String s = file.ReadLine();

-------------------------

