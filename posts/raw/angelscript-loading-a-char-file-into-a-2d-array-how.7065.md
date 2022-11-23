xlat | 2021-11-27 13:11:00 UTC | #1

All is well - documentation on urho is sea.
Hmm, and I'm drowning in it ...

The task seems to be simple and it is like this:
You need to stupidly load your format (albeit text) the ENTIRE file into a string.

The task is a little more difficult:
Something like this:

```
File file("my.txt");
String mystr[file.size()];
file.Read(mystr.data(), file.size());
Vector< String > map = mystr.Split('\n');
```

**How to write this in Angelscript correctly to make it work?**

-------------------------

tarzeron | 2021-11-24 09:36:45 UTC | #2

```
#include "Scripts/Utilities/Sample.as"
void Start()
{
    Print("//////////////////");
    File@ f = File("/home/s/test.txt", FILE_READ);
    Print("file size: " + String(f.get_size()));
    //Print(String(ReadInt));
    Print(f.ReadLine());
    Print("current position: " + String(f.get_position()));
    Print(f.ReadString());
    f.Close();
    engine.Exit();
}
String patchInstructions = "";
```

-------------------------

Modanung | 2021-11-25 10:34:31 UTC | #3

Welcome to the forums! :confetti_ball: :slightly_smiling_face:

Threads in the _Support_ section can be marked as solved. You could move this one there and mark @tarzeron's post as the solution (after refreshing) to increase his _solutions_ count to 2. It also adds a check mark to the thread's title.

-------------------------

xlat | 2021-11-27 11:35:21 UTC | #4

Thanks a lot,
I made such a test class,
Thanks to your hint:
```
class Gamemap
{   String name = "test.txt";
    Array<String> m;
    
    uint r = 0;
    uint c = 0;
    
    String load()
    {   m = from_file("data/!my-files/map_test.txt");
    
        if(m.length == 0) return "ERROR: \"map_test.txt\" FILE!";
        
        r = m   .length;
        c = m[0].length;
        
        return String("Стенд - 001: map[") + String(r) + "][" + String(c) + "]";
    }
    
    Array<String> from_file(String name)
    {   
        File@ f = File(name, FILE_READ);
        if(f.open)
        {   String str = f.ReadString();
                         f.Close     ();
            return str.Split('\n');
        }
        return Array<String>();
    }
}
```

-------------------------

xlat | 2021-11-28 10:01:43 UTC | #5

This does not work in the Urho 1.8 Alfa version:
[quote="xlat, post:4, topic:7065"]
`return String("Стенд - 001: map[") + String(r) + "][" + String(c) + "]";`
[/quote]

To make it work again, I did this:
```
    String s = String("Stend - 001: map[");
return     s + String(r) + "][" + String(c) + "]";
```

-------------------------

Modanung | 2021-11-28 10:23:42 UTC | #6

How about with the latest from the [master branch](https://github.com/urho3d/Urho3D)?

-------------------------

xlat | 2021-11-28 11:27:07 UTC | #7

[quote="Modanung, post:6, topic:7065"]
from the [master branch](https://github.com/urho3d/Urho3D)?
[/quote]
From here I took the file download **Urho3D-master.zip**
And everything worked well here.

[I have corrected for this.](https://github.com/urho3d/Urho3D/releases)
here I took the file download **Urho3D-1.8-ALPHA.zip**

Build by C::B MSYS GCC 10.3:
Urho3D-master.zip -> Size Urho3DPlayer.exe == 23 Mb
Urho3D-1.8-ALPHA.zip -> Size Urho3DPlayer.exe ==  17Mb

-------------------------

