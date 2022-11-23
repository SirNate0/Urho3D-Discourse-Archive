Mike | 2017-01-02 01:02:42 UTC | #1

Are the AngelScript bindings for writing/reading a VectorBuffer in Serializer and Deserializer classes missing? (or is it performed otherwise?)

-------------------------

cadaver | 2017-01-02 01:02:42 UTC | #2

You can write and read an array of uint8's, but it's not quite the same thing. Should be easy to add.

-------------------------

cadaver | 2017-01-02 01:02:42 UTC | #3

Has been added to master. It's the user's responsibility to know the size of the data, for example:

[code]
    VectorBuffer test;
    for (int i = 0; i < 10; ++i)
        test.WriteString("Test" + String(i));

    File outFile("Test.bin", FILE_WRITE);
    outFile.WriteUInt(test.size);
    outFile.WriteVectorBuffer(test);
    outFile.Close();

    File inFile("Test.bin");
    uint size = inFile.ReadUInt();
    VectorBuffer test2 = inFile.ReadVectorBuffer(size);
    inFile.Close();
    
    while(!test2.eof)
      Print(test2.ReadString());
[/code]

-------------------------

Mike | 2017-01-02 01:02:42 UTC | #4

Awesome! Works great, many thanks Cadaver  :stuck_out_tongue:

-------------------------

