Sir_Nate | 2017-01-02 01:13:51 UTC | #1

I needed to use an Urho3D::File (for resource cache support) as an std::istream (for a 3rd party library). This seems to work (though I've not thoroughly tested it)
FileStream.hpp
[code]#pragma once

//based on http://www.mr-edd.co.uk/blog/beginners_guide_streambuf


#include <streambuf>
#include <vector>
#include <cstdlib>
#include <cstdio>

#include <IO/Deserializer.h>

class FileStream : public std::streambuf
{
    public:
        explicit FileStream(Urho3D::Deserializer &src, std::size_t buff_sz = 256, std::size_t put_back = 8);
        virtual ~FileStream() {};
    private:
        // overrides base class underflow()
        int_type underflow();

        // copy ctor and assignment not implemented;
        // copying not allowed
        FileStream(const FileStream &);
        FileStream &operator= (const FileStream &);

    private:
        Urho3D::Deserializer& src_;
        const std::size_t put_back_;
        std::vector<char> buffer_;
};
[/code]

FileStream.cpp
[code]#include "FileStream.hpp"

#include <algorithm>
#include <cstring>

using std::size_t;

FileStream::FileStream(Urho3D::Deserializer &src, size_t buff_sz, size_t put_back) :
    src_(src),
    put_back_(std::max(put_back, size_t(1))),
    buffer_(std::max(buff_sz, put_back_) + put_back_)
{
    char *end = &buffer_.front() + buffer_.size();
    setg(end, end, end);
}

std::streambuf::int_type FileStream::underflow()
{
    if (gptr() < egptr()) // buffer not exhausted
        return traits_type::to_int_type(*gptr());

    char *base = &buffer_.front();
    char *start = base;

    if (eback() == base) // true when this isn't the first fill
    {
        // Make arrangements for putback characters
        std::memmove(base, egptr() - put_back_, put_back_);
        start += put_back_;
    }

    // start is now the start of the buffer, proper.
    // Read from fptr_ in to the provided buffer
//    size_t n = std::fread(start, 1, buffer_.size() - (start - base), fptr_);
    unsigned n = src_.Read(start,buffer_.size() - (start - base));
    if (n == 0)
        return traits_type::eof();

    // Set buffer pointers
    setg(base, start, start + n);

    return traits_type::to_int_type(*gptr());
}
[/code].
You can then create an istream like:
[code]
    File f(context_,filename,FILE_READ);
    FileStream fs(f);
    std::istream is(&fs);[/code]

-------------------------

