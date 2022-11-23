practicing01 | 2017-01-02 01:04:39 UTC | #1

Edit: I used a VectorBuffer and called GetBuffer() on it to construct the MemoryBuffer.

Hello I've got some code like this:
[code]
MemoryBuffer* mechanicParams_;
PODVector<unsigned char> data_;

mechanicParams_ = new MemoryBuffer(data_);

data_.Clear();
mechanicParams_->Seek(0);
mechanicParams_->WriteString("Health");

mechanicParams_->ReadString();
/code]

but the string read is empty.  What's the proper way to use MemoryBuffer?  Thanks for any help.

-------------------------

