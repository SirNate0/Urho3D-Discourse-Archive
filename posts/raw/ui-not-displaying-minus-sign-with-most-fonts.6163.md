Lys0gen | 2020-05-18 20:53:48 UTC | #1

Hello, I have encountered a weird issue.
I tried 3 fonts - Arial, Times New Roman and Tahoma - and with all of them the UI fails to display a simple minus sign. Perhaps there is an issue with other characters as well, but this was most glaring as I can't display negative numbers. There is no whitespace or anything, the text is just shown as if there is nothing there. Escaping it did not do anything either.
Note that **it does work with the default UI's "Anonymous Pro" font** but that is not really a solution for me.

Anyone have an idea why this happens?

-------------------------

SirNate0 | 2020-05-19 01:44:56 UTC | #2

Which minus sign? If it's an en or em dash I could see it being that the font doesn't allo the non-ASCII character by default. I have no idea if that's the actual cause, I just think it might be a possibility.

Edit: I tried it myself with Arial and I couldn't get the "-" to display without using font size 64. Hopefully someone more knowlegable can help, as that seems to be a serious problem.

-------------------------

weitjong | 2020-05-19 02:24:59 UTC | #3

Could you log it as a bug in the issue tracker. Hopefully GitHub will suggest the person who last contributed the code for TTF rendering and you can ping him. I can’t recall his name off hand now.

-------------------------

Lumak | 2020-06-02 00:23:55 UTC | #4

I was surprised about the '-' char code missing in arial.ttf and I looked into this bug. The bug lies in FreeType lib. 
code that Urho3D calls are:
```
 FT_Get_First_Char(face, &glyphIndex);
and 
charCode = FT_Get_Next_Char(face, charCode, &glyphIndex);
```
and no where from the 1st call to the last is '-' returned, eventhough, that charcode exists. FreeType is now 2.10 something and might have that fix.

Temporary fix would be to add at
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/UI/FontFaceFreeType.cpp#L219

at L 219
```
	if (!LoadCharGlyph('-', image))
	{
		hasMutableGlyph_ = true;
	}
```
Pic or it didn't happen?
[img]https://i.imgur.com/xfINWNf.png[/img]

-------------------------

1vanK | 2020-10-30 05:46:39 UTC | #5

When font Arial is used 
```charCode = FT_Get_Next_Char(face, charCode, &glyphIndex);```

sometimes return identical `glyphIndex` for different char codes.

This cause overriding in ```charCodes[glyphIndex + 1] = (unsigned)charCode;```
so array `charCodes` loses some values (including `-`)

EDIT:
This also source of the problem with space:
```
    // Attempt to load space glyph first regardless if it's listed or not
    // In some fonts (Consola) it is missing
    charCodes[0] = 32;
```

-------------------------

