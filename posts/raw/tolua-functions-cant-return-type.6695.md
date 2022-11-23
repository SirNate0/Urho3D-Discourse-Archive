Lys0gen | 2021-02-12 16:12:53 UTC | #1

Hello,

I know this isn't directly related to Urho3D but since tolua++ has no community, information about it is sparse and is contained as a third party tool I figured maybe someone here knows how to fix my problem.

So the issue is following: I am binding std::vector (Urho3D::Vector would have the same issue) with a bunch of classes. For normal types and objects this works, but for a reason I don't understand binding pointer types is not allowed as the return value of some methods would then be [type]*&.

E.g. my .pkg binding file is this:


	$using namespace std;
	typedef int					size_type;
	
	class vector
	{
		TOLUA_TEMPLATE_BIND(T, 	int, string, double, int*)

		size_type size();
		size_type max_size();
		size_type capacity();

		bool empty();

		void reserve(size_type __n);
		void clear();

		T& operator[](size_type __n);

		T& front();
		T& back();

		void push_back(T __x);
		void pop_back();
	};

When trying to generate the bindings with tolua++ I then get the following error:

---

***curr code for error is int*& front();

stack traceback:
        [string "tolua embedded: lua/basic.lua"]:57: in function 'tolua_error'
        [string "tolua: embedded Lua code 23"]:5: in main chunk

** tolua internal error: [string "tolua embedded: lua/declaration.lua"]:368: #invalid function return type: int*& front.


stack traceback:
        [string "tolua: embedded Lua code 23"]:6: in main chunk

---

Now I'm kind of wondering *why* that is. Returning a reference to a pointer should be perfectly valid?

With a bit of digging I found the lines responsible here:

https://github.com/urho3d/Urho3D/blob/44220053a992aa574fa0aa6de3f47ef06b339346/Source/ThirdParty/toluapp/src/bin/lua/declaration.lua#L470

Although I can't seem to adjust anything in this file, I've made a fresh Urho3D repository, commented out that line and built everything but for some reason that error still keeps appearing - that part seems to be cached somewhere regardless of a fresh install?


Anyone have an idea why?

-------------------------

