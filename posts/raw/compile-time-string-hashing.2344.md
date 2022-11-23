S.L.C | 2017-01-02 01:14:52 UTC | #1

Had some fun tonight trying to implement a [url=https://godbolt.org/g/4hdnjz]constexpr version of the StringHash[/url] type ([i]not an actual implementation. just a proof of concept[/i]). Anyway, I thought I'd share it hoping that it could be integrated into the engine since C++11 can now be optionally enabled. If necessary I'll make a pull request myself.

-------------------------

yushli | 2017-01-02 01:14:52 UTC | #2

That sounds quite interesting. However I cann't access the link. Can you put it on github?

-------------------------

S.L.C | 2017-01-02 01:14:52 UTC | #3

Sure, here's a [url=https://gist.github.com/iSLC/ef8cee39a16661b953fc0ef61fb10b54]gist[/url]. To actually see the difference in the generated assembly code I'd suggest something like [gcc.godbolt.org/](http://gcc.godbolt.org/) with "-O3 -std=c++11" as command line. Uncommenting each example individually.

I've actually wen't ahead and integrated it with the engine and I'm trying it right now to see if it compiles (MinGW) and works. MSVC sure made it annoying considering they've introduced constexpr in the November CTP for 2013 and user defined literals again in the CTP 14 which eventually became 2015. So right now it looks a bit weird with some macros.

EDIT: Well, one thing it did so far is to shave  about +250kb from the dll size ([i]with some components disabled. like 2d, lua, database[/i]) and even from the samples as well. Considering only the StringHash type was specialized to take advantage of that, I'd say it's decent. I wonder how far I can take it. A huge opportunity is in the URHO3D_OBJECT macro. But I need to be sure not to affect exports.

-------------------------

yushli | 2017-01-02 01:15:02 UTC | #4

Can you post the code here? I cannot access gist

-------------------------

S.L.C | 2019-08-18 00:02:00 UTC | #5

```cpp
#include <cstdio>
#include <cctype>

// ------------------------------------------------------------------------------------------------

/// Retrieve the lowercase version of an ASCII character.
constexpr int tolower_c(int c)
{
    return (c > 64 && c < 91) ? (c + 32) : c;
}

/// Retrieve the uppercase version of an ASCII character.
constexpr int toupper_c(int c)
{
    return (c > 96 && c < 123) ? (c - 32) : c;
}

// ------------------------------------------------------------------------------------------------

//// Calculate the hash of the given ASCII string using the SDBM algorithm at compile time.
constexpr unsigned SDBMHash_C(const char* s, unsigned i, unsigned n, unsigned h)
{
	return i < n ? SDBMHash_C(s, i + 1, n, tolower_c(s[i]) + (h << 6) + (h << 16) - h) : h;
}

//// Update a hash with the given 8-bit value using the SDBM algorithm.
inline unsigned SDBMHash(unsigned hash, unsigned char c)
{
    return c + (hash << 6) + (hash << 16) - hash;
}

// ------------------------------------------------------------------------------------------------

// used as a workaround for overloading string literals
struct IsCharPtrDummy
{
};
template< typename T > struct IsCharPtr
{
};
template<> struct IsCharPtr< const char * >
{
    typedef IsCharPtrDummy* Type;
};
template<> struct IsCharPtr< char * >
{
    typedef IsCharPtrDummy* Type;
};

// ------------------------------------------------------------------------------------------------

// dummy hash class with optional compile time evaluation
struct shash
{
  	unsigned value;

  	// pre-compiled hash
    explicit constexpr shash(unsigned hash)
  		: value(hash)
  	{
  	}

  	// compile time hash
	template< unsigned N > constexpr shash(const char(&a)[N])
  		: value(SDBMHash_C(a, 0, N-1, 0))
  	{
  	}

  	// run-time non-const buffer hash
	template< unsigned N > shash(char(&a)[N])
  		: value(calculate(a))
  	{
  	}

  	// regular hash
  	template< typename T > shash(T str, typename IsCharPtr<T>::Type=0)
      	: value(calculate(str))
  	{
  	}

  	// compile time hash of explicit length string
    constexpr shash(const char* str, size_t len)
  		: value(SDBMHash_C(str, 0, len, 0))
  	{
  	}

  	unsigned calculate(const char* str)
	{
    	unsigned hash = 0;

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
};

// ------------------------------------------------------------------------------------------------

constexpr shash operator "" _hash(const char* str, size_t len)
{
    return shash(str, len);
}

constexpr unsigned operator "" _h(const char* str, size_t len)
{
    return SDBMHash_C(str, 0, len, 0);
}

// ------------------------------------------------------------------------------------------------

void test(const shash hash)
{
	printf("%u\n", hash.value);
}

// ------------------------------------------------------------------------------------------------

int main()
{
 	const char * cstr = "abc";
  	char sbuf[] = "abc";

  	// compile time evaluation
	test("abc");
 	//test(shash("abc")); // same thing
  
 	// compile time evaluation with user defined literal
	//test("abc"_hash);
 
  	// compile time evaluation with user defined literal
  	// ugly because that constructor is explicit :(
	//test(shash("abc"_h));
 
  	// run-time evaluation
  	//test(cstr);
 
  	// run-time evaluation on non-const buffers (preferably?)
  	//test(sbuf);
 
  	return 0;
}
```

-------------------------

yushli | 2017-01-02 01:15:03 UTC | #6

Thank you for sharing this! Hope this can be merged into main branch.

-------------------------

smellymumbler | 2017-11-08 20:02:38 UTC | #8

What's the benefit of using this? Much faster? Sorry about the ignorance. :(

-------------------------

Eugene | 2017-11-08 22:28:00 UTC | #9

It mostly about `switch` with string hash keys and templates and such compile-time places.

-------------------------

