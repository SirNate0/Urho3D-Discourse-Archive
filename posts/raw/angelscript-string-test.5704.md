diskette | 2019-11-03 16:15:19 UTC | #1

I think AngelScript Urho3D Strings need more descriptions or samples.<br>What about **single-double quotes** for Strings?<br><br>**====== Strings ======**:<br><pre>String[] string1 = { "1", "2", "3", "a", "b", "c"};
    String[] string2 = { '1', '2', '3', 'a', 'b', 'c'};
    String string3 = "123abc";
    String string4 = '123abc';</pre>**====== Test 1 ======**:<br><pre>for(uint x = 0; x < string1.length; x++)
    {
        Print("STR1: " + string1[x]);
    }
    for(uint y = 0; y < string2.length; y++)
    {
        Print("STR2: " + string2[y]);
    }
    for(uint z = 0; z < string3.length; z++)
    {
        Print("STR3: " + string3[z]);
    }
    for(uint w = 0; w < string4.length; w++)
    {
        Print("STR4: " + string4[w]);
    }</pre>**Output**:<br>STR1: 1 2 3 a b c
STR2: 49 50 51 97 98 99
STR3: 49 50 51 97 98 99
STR4: 52 57<br><br>**====== Test2 ======**:<pre>uint ret_pos = NPOS;
ret_pos = string1.Find("3"); // '' OR ""
Print("STR1_POS: " + String(ret_pos));
ret_pos = NPOS;
ret_pos = string2.Find("3"); // '' OR ""
Print("STR2_POS: " + String(ret_pos));
ret_pos = NPOS;
ret_pos = string3.Find("3"); // '' OR ""
Print("STR3_POS: " + String(ret_pos));
ret_pos = NPOS;
ret_pos = string4.Find("3"); // '' OR ""
Print("STR4_POS: " + String(ret_pos));
ret_pos = NPOS;</pre>**Output**:<br>--- Single quotes ('')
STR1_POS: 4294967295
STR2_POS: 2
STR3_POS: 2
STR4_POS: 4294967295

--- Double quotes ("")
STR1_POS: 2
STR2_POS: 4294967295
STR3_POS: 2
STR4_POS: 4294967295<br><br>**====== Test3 ======**:<pre>String ltr1, ltr2, ltr3, ltr4; // single letter
ltr1 = string1[0];
ltr2 = string2[0];
ltr3 = string3[0];
ltr4 = string4[0];
Print("ltr1: "+ ltr1 +" ltr2: "+ ltr2 +" ltr3: "+ ltr3 +" ltr4: "+ ltr4);</pre>**Output**:<br>ltr1: 1 <br>ltr2: 49 <br>ltr3: 49 <br>ltr4: 52

-------------------------

S.L.C | 2019-11-03 20:37:04 UTC | #2

single quote strings can be enabled by a engine option. i think by default they're used for characters.

https://www.angelcode.com/angelscript/sdk/docs/manual/angelscript_8h.html#a53c2e8a74ade77c928316396394ebe0fa6dc1c33f9227c66f18fc0f95a0c798b2

-------------------------

