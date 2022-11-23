WangKai | 2018-08-25 15:49:06 UTC | #1

It seems that we don't take hash collsion into account when we use StringHash. It's a dummy quesion but StringHash is not 100% collision safe, right?
```c++
unsigned StringHash::Calculate(const char* str, unsigned hash)
{
    if (!str)
        return hash;

    while (*str)
    {
        // Perform the actual hashing as case-insensitive
        char c = *str;
        hash = SDBMHash(hash, (unsigned char)tolower(c));
        ++str;
    }

    return hash;
}
```

I'm not sure how many places there are having the risk of hash collision of other data types besides String.

-------------------------

weitjong | 2018-08-26 04:20:39 UTC | #2

The latest master branch version has made this calculation case-sensitive exactly in order to reduce the hash collision. But you are right, the chance is still non-zero.

-------------------------

WangKai | 2018-08-28 02:22:50 UTC | #3

For explicit cases, e.g. we use const StringHash to represent constant String values which is fast, and if collision is there, we can find out when coding. However, if we use `HashMap<StringHash, XXX>` which is dangerous since we cannot estimate that different Strings will always have different StringHash value. Instead, we should use `HashMap<String, XXX>` as HashMap will take care of hash collision.

-------------------------

weitjong | 2018-08-28 10:46:01 UTC | #4

You are absolutely right! Provided you have Urho3D::String and not C-string as your key.

-------------------------

Eugene | 2018-08-28 09:26:08 UTC | #5

FYI, there's realtime hash collision detection guarded via `URHO3D_HASH_DEBUG`. It'd slow code down, of course.

-------------------------

WangKai | 2018-08-31 07:42:10 UTC | #6

Yes, Eugene, I've seen them. Sweet implementation :wink:

-------------------------

