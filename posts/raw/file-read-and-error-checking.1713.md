TheComet | 2017-01-02 01:09:39 UTC | #1

Hey!

I think this is a great project and I want to help contribute. Is there a style/concept guideline anywhere? More specifically I want to know more about the way you handle errors (i.e. why did you choose not to use exceptions).

Take this snippet for example:

(Source: [url]https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/IO/File.cpp#L251[/url])
[code]unsigned File::Read(void* dest, unsigned size)
{
    // SNIP

    if (compressed_)
    {
        unsigned sizeLeft = size;
        unsigned char* destPtr = (unsigned char*)dest;


        while (sizeLeft)
        {
            if (!readBuffer_ || readBufferOffset_ >= readBufferSize_)
            {
                unsigned char blockHeaderBytes[4];
                fread(blockHeaderBytes, sizeof blockHeaderBytes, 1, (FILE*)handle_);


                MemoryBuffer blockHeader(&blockHeaderBytes[0], sizeof blockHeaderBytes);
                unsigned unpackedSize = blockHeader.ReadUShort();
                unsigned packedSize = blockHeader.ReadUShort();


                if (!readBuffer_)
                {
                    readBuffer_ = new unsigned char[unpackedSize];
                    inputBuffer_ = new unsigned char[LZ4_compressBound(unpackedSize)];
                }


                /// \todo Handle errors
                fread(inputBuffer_.Get(), packedSize, 1, (FILE*)handle_);
                LZ4_decompress_fast((const char*)inputBuffer_.Get(), (char*)readBuffer_.Get(), unpackedSize);


                readBufferSize_ = unpackedSize;
                readBufferOffset_ = 0;
            }


            unsigned copySize = (unsigned)Min((int)(readBufferSize_ - readBufferOffset_), (int)sizeLeft);
            memcpy(destPtr, readBuffer_.Get() + readBufferOffset_, copySize);
            destPtr += copySize;
            sizeLeft -= copySize;
            readBufferOffset_ += copySize;
            position_ += copySize;
        }


        return size;
    }

    // SNIP
}[/code]

My questions are these.
[ul][li]Is it normal not to check the return value of fread() or read()? If the return values shouldn't be checked, what's your rationale for that decision?[/li]
[li]Is it normal not to check if memory allocations succeeded? Again, rationale?[/li]
[li]I see a [b]\todo Handle errors[/b] there, which I assume is referring to the decompression of the data. Seeing as all callers of File::Read never check the return value either -- and the use of exceptions is discouraged -- there seems to be little reason to implement error checking unless everyone in the call stack starts checking the return value of File::Read too. Is this something that needs implementing?[/li][/ul]

Thanks!

-------------------------

valera_rozuvan | 2017-01-02 01:09:39 UTC | #2

Hello [b]TheComet[/b]. I was also wondering just today why there are no exceptions...

Maybe better to move this topic to [b]Developer Talk[/b] [url]http://urho3d.prophpbb.com/forum7.html[/url]?

-------------------------

valera_rozuvan | 2017-01-02 01:09:39 UTC | #3

By the way, take a look at the code conventions that are at [url]http://urho3d.github.io/documentation/1.5/_conventions.html[/url]. It does mention that:

[quote]No C++ exceptions. Error return values (false / null pointer / dummy reference) are used instead. Script exceptions are used when there is no other sensible way, such as with out of bounds array access.[/quote]

-------------------------

cadaver | 2017-01-02 01:09:39 UTC | #4

The primary reason to avoid exceptions was that they wreak havoc with script bindings, as script VM's usually can't handle it when an exposed C++ function throws an exception within the VM run loop.

There is fread() error checking in the normal (non-compressed) execution path. For the compressed path there's a todo marked. Overall I know that Urho could use some more error checking.

Out-of-memory situations are not really handled, because it's unsure how well the program could recover at that point (even allocating an error message string could also fail.) We use new and new[] instead of malloc, so this should throw a bad alloc, which is typically caught in the Urho application top level.

-------------------------

