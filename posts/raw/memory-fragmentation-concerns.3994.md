QBkGames | 2018-02-07 03:55:50 UTC | #1

I started looking through the engine code in more detail, and I noticed a few possible issues that could cause unnecessary memory fragmentation (which PCs could live with but could affect performance on mobile and maybe even on consoles). 

1. RefCounted class contains an instance of RefCount struct which is allocated on the heap with new() in the constructor. I'm not an expert at reference counting, but is there a good reason for this and not having the struct as a plain member of the class?

   RefCounted::RefCounted() :
        refCount_(new RefCount())

Looks like the constructor always allocates a new RefCount struct, so I cannot see any reason why it couldn't be a plain member. Creating and deleting game entities based on RefCounted, would created extra (apparently unnecessary) memory fragmentation by always also allocating/deleting the RefCount struct separately.

2. Passing String as a parameter to ResourceCache functions, node creation functions, etc, again unnecessarily allocates, copies then deallocates temporary string of chars, just so that they get passed to a function. Passing "const char*" to all these functions would be much more efficient as it would not require allocating and copying buffers.
This is especially ridiculous for ResourceCache which all it really requires is actually a StringHash. 

A possible alternative (to passing "const char*") solution would be to modify the String class to support shared buffers.

Can someone enlighten me as to whether there is a good reason for the way things are? Thanks.

-------------------------

Sinoid | 2018-02-07 08:31:05 UTC | #2

The refcount has to be a pointer for the WeakPtr types to work sanely. Otherwise you'd need a list for every living WeakPtr instance to mark them invalid - instead they can just point at the RefCount and the last WeakPtr can delete it when it's time.

There is no better solution. It's basically the same as std::shared_ptr.

---

> Passing String as a parameter to ResourceCache functions, node creation functions, etc, again unnecessarily allocates, copies then deallocates temporary string of chars, just so that they get passed to a function.

No. They're almost always passed as `const&`, nothing is allocated. Every single function in `ResourceCache` that takes a string does so by reference - not copy.

That's fundamental C.

> Passing “const char*” to all these functions would be much more efficient as it would not require allocating and copying buffers.

No. The data-segment (where those `"My Explicitly typed string"` live is a cache minefield and strings in it are a cache-miss everytime. Unless you're actively in it It's likely to be the single furthest thing from any point in your program's lifecycle. It's only fast when all you care about is the address, dereference that pointer, `strlen` it, etc and the magic is gone.

That's also fundamental C and an eternal compiler development dilemma.

> This is especially ridiculous for ResourceCache which all it really requires is actually a StringHash

Again, every single String passed in as an alias, there is **no copy** until the ResourceCache needs to remap a path or store it for itself.

Also, they're **paths**, not names.

How would you remap paths or select appropriate loaders from a StringHash? You can't, the information required is lost - any structure based solution around it is just reinventing paths but worse.

-------------------------

QBkGames | 2018-02-09 12:19:01 UTC | #3

Thanks for the reply and clarifications.

-------------------------

TheComet | 2018-02-09 22:10:17 UTC | #4

[quote="Sinoid, post:2, topic:3994"]
Passing String as a parameter to ResourceCache functions, node creation functions, etc, agay unnecessarily allocates, copies then deallocates temporary string of chars, just so that they get passed to a function.

No. They’re almost always passed as const&, nothing is allocated. Every single function in ResourceCache that takes a string does so by reference - not copy.

That’s fundamental C.
[/quote]

Unless he means the cases where you pass in a c string to these functions (e.g. if you call the function ```void Foo(const String& s);``` with ```Foo("test");```) then this will definitely be a memory allocation, string copy, followed by a deallocation. ```std::string``` has a small size optimization which gets around that allocation for small strings, but I don't think Urho3D does this.

-------------------------

Eugene | 2018-02-09 22:16:52 UTC | #5

@QBkGames, I tried to use `const char*` in my pet engine, but it sux.
So unhandy to deal with any string ops and always do these nasty `std::string(my_arg)` and `foo(str.c_str())`.

-------------------------

Sinoid | 2018-02-09 23:05:13 UTC | #6

@TheComet, right that slipped my mind, and C++11 forbid copy-on-write strings so it's mandatory (which probably made GCC folks grumble at the time).

StringHash is used so extensively throughout Urho3D that when there's a string showing up it generally has a reason (came from data, is script / user facing, the string is meaningful like a path / text / shader #define / etc).

-------------------------

QBkGames | 2018-02-11 08:24:43 UTC | #7

Regarding Strings, the scenario that @TheComet refers to is exactly what I meant.

Although a lot of string data comes from external files which are read in as String, you still refer to a lot of constant strings throughout the game: when getting some resources, when referring to specific UI elements, when referring to specific objects in a XML or JSON file, when looking for specific Nodes or component, etc.
So there is quite a lot of scenarios where the String acts simply as a temporary wrapper around a const char* only because the function you are calling requires a const String reference instead of simply accepting a const char* (which is what you are really supplying). Most of these calls happen when the game initialises so your memory gets trashed even before the game begins.

I'm currently working on a potential solution that should have a minimal impact on existing code base (some changes to String to allow for a shared buffer, thus not requiring allocating and copying the source buffer).

-------------------------

Sinoid | 2018-02-11 10:57:05 UTC | #8

> I’m currently working on a potential solution that should have a minimal impact on existing code base (some changes to String to allow for a shared buffer, thus not requiring allocating and copying the source buffer).

I assume you're turning off threads then. Are you're going to add a refcount or mutex to string? COW plus threads doesn't mix.

Do you have histograms or anything that show fragmentation to be a problem?

-------------------------

SirNate0 | 2018-02-11 20:30:13 UTC | #9

Would it be possible to create a constexpr string literal operator (maybe _S or _US) to construct an Urho3D::String, and would that alleviate the fragmentation concerns raised? I have no idea -- I assume it should be possible to create it, but I really don't know if it would alleviate the concerns about fragmentation. My guess is that it might, provided all calls to the functions in question added the new suffix to the hard-coded string.

-------------------------

S.L.C | 2018-02-11 23:52:25 UTC | #10

Regarding the string issue. I see two options. Implement a `std::string_view` like the new c++17 standard. Which might be a little more difficult than expected with C++11. Having C++14 would be favorable since they've removed some `constexpr` limitations. But even with just C++11, where you're forced to have an immutable implementation. It would still work. I remember trying it a while ago.

Or, implement the small buffer optimization like many new libraries do these days. The local string implementation really is just a:

	struct String
	{
		String() : data(local_), size(0) { }
		~String() { if (data_ != local_) delete[] data_; }
	private:

		char * 			data_;
		unsigned		size_;
		union {
			unsigned 	capacity_;
			char 		local_[20];
		};
	};

And you have 32 byte (_regardless of architecture_) `String` implementation with room for 19 usable bytes. `std::string` uses `size_t` so they loose 4 bytes. but it only occupies 24 bytes on 32-bit.

Or even better, have them both :smiley: Gotta say it looks fun and I might even try it this week. Out of curiosity.

-------------------------

TheComet | 2018-02-12 01:56:05 UTC | #11

If you make the change, it would be beneficial if you could also *measure* the impact these changes have, to see if it matters or not.

-------------------------

weitjong | 2018-02-12 11:27:31 UTC | #12

Personally I like this idea more, although I am not sure yet whether it can be pulled off but using `constexpr` or user-defined suffix for the `String` literal looks promising.

-------------------------

S.L.C | 2018-02-12 02:14:42 UTC | #13

I did make a dummy implementation of a local string in my fork of the engine. Currently the Editor crashes. I'll have to look into it. And the Variant type is forced to be 32 bytes regardless of architecture.

As for actual performance, I couldn't see anything significant. Probably because there is no project that actually puts the engine to a more realistic situation. And in the samples, most of the execution time is spent in physics, math, occlusion, encoding, decoding etc. Very little that stresses the String implementation.

So to get an idea of the actual performance. I'd have to run some synthetic benchmarks. Which I might do. I'll be back with some results.

-------------------------

QBkGames | 2018-02-12 02:19:43 UTC | #14

After thinking about it for a whole day (and half a night), this is what I came up with:

    /// Only meant as a temporary wrapper around a const char*. Only supports const functions as it does not own the char buffer.
    /// Calling functions that change the char buffer can result in memory corruptions.
    class URHO3D_API ConstString : public String
    {
    public:
    	/// Construct from another string.
    	ConstString(const String& str)
    	{
    		length_ = str.Length();
    		buffer_ = (char*)str.CString();
    	}

    	/// Construct from a C string.
    	ConstString(const char* str)
    	{
    		length_ = CStringLength(str);
    		buffer_ = (char*)str;
    	}
    };

It's a bit hacky, but works. Then you use it:

    mushroomObject->SetModel(cache->GetResource<Model>(ConstString("Models/Mushroom.mdl")));
    mushroomObject->SetMaterial(cache->GetResource<Material>(ConstString("Materials/Mushroom.xml")));

This is the best solution I can think of that requires minimum changes.

-------------------------

QBkGames | 2018-02-12 02:22:37 UTC | #15

By the way, I'm not very familiar with git, do you need some special permission to create a branch and open a pull request? I've cloned the repository, created a branch but I'm unable to publish it.

-------------------------

QBkGames | 2018-02-12 02:34:17 UTC | #16

As to how much String impacts the game/engine performance, probably not that significant (at least not on a PC, might make a bit more difference on a mobile), but to me any wasted clock cycle is taking away my option to add more entities or features that enrich the game.

So, one of the attractions of Urho3D is that is advertised as light weight, which in my mind means very optimised and efficient. And the way String is used, does not fit with that attitude.

There might be other subsystems of the engine that could do with more optimisation (maybe the event system ?), but String is something that jumped at me from the start.

-------------------------

S.L.C | 2018-02-12 03:12:04 UTC | #17

A string with a local buffer does have some benefits. But sometimes it can be even worse. More memory is used. Move semantics, swapping, copying, default construction etc. take a bit more work than usual. And that takes it's toll.

There were definitely things that could have been improved. I might look more into it. I'm pretty sure the quick and dirty implementation I did is far from perfect.

But for now. I'm starting to think that a string view coupled with the regular string implementation might work better. I'll have to try and see.


Default construction empty:

	static void Heap(benchmark::State& state) {
	    for (auto _ : state) {
	        Urho3D::String s("abcd");
	        benchmark::DoNotOptimize(s);
	    }
	}
	BENCHMARK(Heap);

	static void Local(benchmark::State& state) {
	    for (auto _ : state) {
	        Urho3D::String2 s("abcd");
	        benchmark::DoNotOptimize(s);
	    }
	}
	BENCHMARK(Local);

Output:

	--------------------------------------------------
	Benchmark           Time           CPU Iterations
	--------------------------------------------------
	Heap                1 ns          1 ns 1000000000
	Local               2 ns          2 ns  407922793


Default construction with C string of 4 chars:

	static void Heap(benchmark::State& state) {
	    for (auto _ : state) {
	        Urho3D::String s("abcd");
	        benchmark::DoNotOptimize(s);
	    }
	}
	BENCHMARK(Heap);

	static void Local(benchmark::State& state) {
	    for (auto _ : state) {
	        Urho3D::String2 s("abcd");
	        benchmark::DoNotOptimize(s);
	    }
	}
	BENCHMARK(Local);

Output:

	--------------------------------------------------
	Benchmark           Time           CPU Iterations
	--------------------------------------------------
	Heap               34 ns         34 ns   21367384
	Local               5 ns          5 ns  100000000


Default construction with C string of 19 chars:

	static void Heap(benchmark::State& state) {
	    for (auto _ : state) {
	        Urho3D::String s("abcdefghijklmnefgh");
	        benchmark::DoNotOptimize(s);
	    }
	}
	BENCHMARK(Heap);

	static void Local(benchmark::State& state) {
	    for (auto _ : state) {
	        Urho3D::String2 s("abcdefghijklmnefgh");
	        benchmark::DoNotOptimize(s);
	    }
	}
	BENCHMARK(Local);

Constructing with a string that exceeds the local buffer capacity:

	--------------------------------------------------
	Benchmark           Time           CPU Iterations
	--------------------------------------------------
	Heap               33 ns         33 ns   22435754
	Local               6 ns          6 ns  125840759

Default construction with C string of 24 chars:

	static void Heap(benchmark::State& state) {
	    for (auto _ : state) {
	        Urho3D::String s("abcdefghijklmnefghijklmn");
	        benchmark::DoNotOptimize(s);
	    }
	}
	BENCHMARK(Heap);

	static void Local(benchmark::State& state) {
	    for (auto _ : state) {
	        Urho3D::String2 s("abcdefghijklmnefghijklmn");
	        benchmark::DoNotOptimize(s);
	    }
	}
	BENCHMARK(Local);

Output:

	--------------------------------------------------
	Benchmark           Time           CPU Iterations
	--------------------------------------------------
	Heap               33 ns         33 ns   18643076
	Local              37 ns         37 ns   18696461

Copying arrays of strings:

	typedef Urho3D::Vector< Urho3D::String > StringVec;
	typedef Urho3D::Vector< Urho3D::String2 > String2Vec;

	static const unsigned sizes[] = {
		0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,
		32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63
	};
	static const char * cstr = "abcdefghijklmnefghijklmnabcdefghijklmnefghijklmnabcdefghijklmnefghijklmn";

	static void Heap(benchmark::State& state) {
	    StringVec v1, v2;
	    v1.Resize(64);
	    v2.Resize(64);
	    for (unsigned i = 0; i < 64; ++i)
	        v1[i].Append(cstr, i);

	    for (auto _ : state) {
	        v1 = v2;
	    }
	}
	BENCHMARK(Heap);

	static void Local(benchmark::State& state) {
	    String2Vec v1, v2;
	    v1.Resize(64);
	    v2.Resize(64);
	    for (unsigned i = 0; i < 64; ++i)
	        v1[i].Append(cstr, i);

	    for (auto _ : state) {
	        v1 = v2;
	    }
	}
	BENCHMARK(Local);

Output:

	--------------------------------------------------
	Benchmark           Time           CPU Iterations
	--------------------------------------------------
	Heap              308 ns        310 ns    2361658
	Local             409 ns        407 ns    1725827


Integer conversion:

	static void Heap(benchmark::State& state) {
	    for (auto _ : state) {
	        Urho3D::String s(242554);
	        benchmark::DoNotOptimize(s);
	    }
	}
	BENCHMARK(Heap);

	static void Local(benchmark::State& state) {
	    for (auto _ : state) {
	        Urho3D::String2 s(242554);
	        benchmark::DoNotOptimize(s);
	    }
	}
	BENCHMARK(Local);

Output:

		--------------------------------------------------
	Benchmark           Time           CPU Iterations
	--------------------------------------------------
	Heap              111 ns        111 ns    5608938
	Local              68 ns         68 ns    8974301


Environment:

* Windows 7 x64
* MinGW 7.2.0 x64 POSIX SEH
* Ryzen 5 1600x single threaded @3.7.

-------------------------

S.L.C | 2018-02-12 03:20:01 UTC | #18

That's basically how a `string_view` is supposed to look like. Except you're playing with the destructor of the base class which destroys the buffer. And boy oh boy, destruction you'll get.

-------------------------

SirNate0 | 2018-02-12 03:46:01 UTC | #19

[quote="QBkGames, post:15, topic:3994, full:true"]
By the way, I’m not very familiar with git, do you need some special permission to create a branch and open a pull request? I’ve cloned the repository, created a branch but I’m unable to publish it.
[/quote]

Did you fork it on GitHub and then clone your fork, or did you just clone the main repo? While you might be able to do it with just the main repo and your local machine, the only way I know too create a pull request is to do it through my fork on GitHub (push the branch to your fork, which you should have write access to, and then visit the GitHub page for your fork and it should give you the option to create a pull request).

-------------------------

Sinoid | 2018-02-12 04:25:54 UTC | #20

If it wasn't forked first and was instead cloned from the main Urho3d repo then you have to fork on github then change the url on the local clone. https://help.github.com/articles/changing-a-remote-s-url/

-------------------------

QBkGames | 2018-02-12 11:05:45 UTC | #21

[quote="S.L.C, post:18, topic:3994"]
Except you’re playing with the destructor of the base class which destroys the buffer. And boy oh boy, destruction you’ll get.
[/quote]

Actually, as long as the capacity variable remains at 0, the destructor shouldn't be a problem. I've already tried it in practice.

I'm guessing that a "proper" string_view equivalent implementation would be to have the View as the base class with all const methods as its members, and then have the String inherit from the View.
I actually thought of that as well, but then you'll still have to change all function signatures throughout the engine to replace "const String&" to "const StringView&", in which case it would be much easier to replace them simply with "const char*" and not have to mess around with the view at all. I have no idea what the impact would be for the scripting language bindings but for C++ it should not really break too many things (if any at all).

(Of course, you'd still use String internally to store char data, but for passing strings around, I still think const char* is the best, most efficient option).

-------------------------

QBkGames | 2018-02-12 10:40:56 UTC | #22

@SirNate0 & @Sinoid

Thanks for the clarifications with GitHub. I didn't know you had to fork first, so I did clone the main repo. The article helped and I've now changed the url to my fork.

-------------------------

