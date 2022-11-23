TheComet | 2017-01-02 01:11:46 UTC | #1

I ran into a problem that caused some annoying segfaults.

[b][size=150]The Problem[/size][/b]

Consider the following factory pattern (reduced for simplicity):

[code]class Item
{
public:
    static SharedPtr<Item> Item::create(Item_e item)
    {
        switch(item) {
            case ITEM_FLOWER: return new FlowerItem;
            /* etc */
        }
        return SharedPtr<Item>();
    }
};[/code]

Now consider the following call to this factory method:
[code]Item* item = Item::create(ITEM_FLOWER);
// Oh oh, the FlowerItem object was destroyed here[/code]

It shouldn't be possible to convert SharedPtr to a raw pointer like this. This basically makes [b]SharedPtr::Get()[/b] a useless method.

Furthermore, although not as bad as above, these implicit conversions allow for somewhat confusing code. For example:
[code]SharedPtr<Foo> foo;
doAThing(foo);[/code]

Does [b]doAThing()[/b]; take a raw pointer Foo* or a SharedPtr<Foo>? We cannot know without looking up the function signature.

Or this:
[code]Foo* MyClass::SomeMethod() { return foo_; }[/code]

Is [b]foo_[/b] a SharedPtr or a raw pointer? Again, we cannot know without looking at the definition of foo_.


[b][size=150]Proposed solution[/size][/b]

I propose to make the following change to SharedPtr and WeakPtr. Change this:
[code]operator T*() const { return ptr_; }[/code]
to this:
[code]operator const T*() const { return ptr_;}[/code]

This change will fix all of the problems explained above and at the same time it will still allow for code such as this:
[code]SharedPtr<Item> item = Item::create(ITEM_FLOWER);
if(!item) // This is still valid!
    return;[/code]

This change will force us to change these examples:
[code]// 1
SharedPtr<Foo> foo;
doAThing(foo);

// 2
Foo* MyClass::SomeMethod() { return foo_; }[/code]

Into this:
[code]// 1
SharedPtr<Foo> foo;
doAThing(foo.Get());

// 2
Foo* MyClass::SomeMethod() { return foo_.Get(); }[/code]

Which allows us to instantly see that if SharedPtr is being used or not.

If the dev team agrees, I shall go ahead and make this change.

-------------------------

cadaver | 2017-01-02 01:11:47 UTC | #2

I would agree this is good, however I will reserve final judgement until I see the PR (and exact amount of engine changes.) WeakPtr should be safe to keep as is, as getting a raw ptr from a weak ptr should have no unintended consequences.

-------------------------

gawag | 2017-01-02 01:11:47 UTC | #3

Good idea.

[quote]
This change will fix all of the problems explained above and at the same time it will still allow for code such as this:
[code]
    SharedPtr<Item> item = Item::create(ITEM_FLOWER);
    if(!item) // This is still valid!
        return;
[/code]
[/quote]
One could also use "operator bool() const" which is usually done for such checks. The obvious archetype std::shared_ptr does that too: [cplusplus.com/reference/memory/shared_ptr/](http://www.cplusplus.com/reference/memory/shared_ptr/)

T* and SharedPtr<T> feel weirdly mixed in Urho. What is the guideline behind that? Is there a consistent style?
Is there a case of getting a T* from a function and being responsible for that object (having to delete it)? Would be weird. Should be a unique or shared pointer.
Is there a case of passing a T* to a function, returning from it and not being able to safely delete the T? Should be a shared or weak pointer then.
There could be more pitfalls which can be avoided with types and not having error prone implicit conversions like SharedPtr::operator T*().

Also functions like Terrain::SetHeightmap(Image*) could act differently depending on whether they got a naked pointer or a shared pointer. In the first case the ressource would be copied and managed internally (if it is actually needed after returning from the function of course). In the second case the same ressource could be shared across objects to save memory. Maybe that is already done internally, having that more explicit would be better though.

-------------------------

TheComet | 2017-01-02 01:11:47 UTC | #4

[b]@cadaver[/b] - I will begin work on creating the PR in that case.

As a side note, I'm interested in where you first learned about intrusive reference counts? I've never seen anything quite like it before Urho3D.

[quote="gawag"]One could also use "operator bool() const" which is usually done for such checks. The obvious archetype std::shared_ptr does that too: [cplusplus.com/reference/memory/shared_ptr/](http://www.cplusplus.com/reference/memory/shared_ptr/)[/quote]

This is a good idea. That means we can get rid of [b]operator T*() const[/b] completely.

[quote="gawag"]T* and SharedPtr<T> feel weirdly mixed in Urho. What is the guideline behind that? Is there a consistent style?[/quote]

It's dangerous to think of Urho's SharedPtr<T> as being analogous to std::shared_ptr<T> because they don't have the same semantic meaning. As I've come to understand, in Urho3D, everything inheriting from [b]RefCounted[/b] is considered a shared resource, regardless of whether a function takes T* or SharedPtr<T> as an argument. For instance, I could easily write a function that manually increments the refcount:

[code]void foo(Bar* bar) {
    bar->AddRef();
}[/code]

You simply cannot make the assertion that just because a function takes a raw T* pointer it does not increment the refcount later on. You have to assume that every object is a shared object by default (since virtually everything in Urho3D inherits from RefCounted).

So with that in mind, Urho3D's guideline is to pass around raw pointers whenever possible (for speed), and if it so happens that an object wishes to store the pointer for later use, it will wrap it in a SharedPtr<T> in order to increment the refcount and stop it from potentially being deleted elsewhere.

-------------------------

cadaver | 2017-01-02 01:11:47 UTC | #5

I no longer remember where I first saw intrusive pointers, possibly in kNet library.

The primary reasons Urho uses intrusive shared pointers is:
- Prevent situations where shared -> raw -> shared conversions could result in two separate refcounts being created, which later leads to double-delete and crash. Std::shared_ptr has make_shared mechanism to prevent this, but the classes must remember to inherit shared_from_this, and you must remember to use make_shared.
- Easiest interoperability with AngelScript handles, as the API can just hand out raw ptrs in all cases where it still owns the objects somewhere (like in the scene graph.)

In C++ application code IMO you should never do manual AddRef() or ReleaseRef(), but use shared ptrs. Script bindings would sometimes need to use these when "transferring" ownership from a shared ptr.

-------------------------

sabotage3d | 2017-01-02 01:11:47 UTC | #6

Just as a side note. Are going for the for something similar to the behaviour of Boost intrusive_ptr?  
[b]Boost intrusive_ptr:[/b] [url]http://www.boost.org/doc/libs/1_57_0/libs/smart_ptr/intrusive_ptr.html[/url]

-------------------------

gawag | 2017-01-02 01:11:48 UTC | #7

Ha!  :laughing: That's funny. This situation is kinda hilarious:

[quote]
This is a good idea. That means we can get rid of operator T*() const completely.
[/quote]
I actually wrote a whole and long paragraph about it, thought about it for quite a while and removed it again. The "problem" I saw is that functions who take a specific object (like an Image or a Texture) may not really care how it is managed. From a user perspective you want to give them the resource independent if it's a T* or a SharedPtr<T> or a UniquePtr<T> or whatever. This can be either done by having a huge amount of overloads for every common T* or T* wrapper but one doesn't really want to do and maintain that.
The other option is the current existing one with the implicit conversion to T* in some way so that every function taking a T* does also directly accept SharedPtr<T> without having to use the .Get() (code bloat). I actually thought you thought about the same thing already and intentionally suggesting making it an implicit conversion to T* const as this could still allow giving functions taking an T* (or T* const) a SharedPtr<T>.

Actually just another option came to my mind but I would need to test that and it would be kinda odd... I'll test that...

Was the reason for the implicit SharedPtr<T> to T* conversion the passing to functions taking a T*? Am I missing something else?
The conversion is quite a big and dangerous pitfall but I see this one big reason for it and no perfect solution.

[quote]
[all that SharedPtr and intrusive pointer stuff]
[/quote]
Eww. :confused: Really? That's totally unexpected. I thought it was similar to std::shared_ptr like the name suggested. I kinda assumed something like that happening in Urho but I didn't know exactly until now.
I see the reason for that but at least the naming is terrible. What about IntrusivePtr<T>? Is SharedPtr also used like a normal shared pointer (like std::shared_ptr) and not like an intrinsic pointer? Smells like two different use cases that suggest two different types.

-------------------------

gawag | 2017-01-02 01:11:48 UTC | #8

I've researched the idea I mentioned: [github.com/damu/wiki/blob/maste ... classes.md](https://github.com/damu/wiki/blob/master/converter_classes.md)
If one wants to avoid having many overloads like:
[code]
Terrain::SetHeightmap(Image*)
Terrain::SetHeightmap(SharedPtr<Image>)
Terrain::SetHeightmap(WeakPtr<Image>)
...
[/code]
One could use the described technique of using a converter class:
[code]
Terrain::SetHeightmap(AnyPtr<Image>)
[/code]
With that the SetHeightmap function (and any other function taking a "AnyPtr") accepts all pointer types it is configured for like T*, SharedPtr<T> and WeakPtr<T>. Without having to have the wrapper implicitly be convertible to T*, that implicit conversion is type safe offloaded to AnyPtr.
I've included a screenshot of the assembler output. It's practically cost free, depending on the case it can even be cheaper.

Comments?

-------------------------

TheComet | 2017-01-02 01:11:48 UTC | #9

[quote="cadaver"]In C++ application code IMO you should never do manual AddRef() or ReleaseRef(), but use shared ptrs. Script bindings would sometimes need to use these when "transferring" ownership from a shared ptr.[/quote]

Obviously, yeah. I just wanted to be as clear as possible in that example.

[quote="gawag"]I've researched the idea I mentioned: [github.com/damu/wiki/blob/maste ... classes.md](https://github.com/damu/wiki/blob/master/converter_classes.md)[/quote]

There are many problems with your proposed solution using [b]any_pointer[/b]. The TL;DR version is you're breaking semantic meaning and you're re-introducing the issue I explained in the first post:

[code]class Item
{
public:
    static SharedPtr<Item> Item::create(Item_e item)
    {
        switch(item) {
            case ITEM_FLOWER: return new FlowerItem;
            /* etc */
        }
        return SharedPtr<Item>();
    }
};

class Player
{
    Item* item_;
public:
    void HoldItem(AnyPtr<Item> item)
    {
        item_ = item;
    }
}[/code]

Here's the problem again:
[code]Player player;
player.HoldItem(Item::create(ITEM_FLOWER));
// Oh oh, player.item_ is now pointing to a destroyed object
// This is exactly what I'm trying to fix, AnyPtr re-introduces the issue[/code]

[quote="gawag"]One could use the described technique of using a converter class:
[code]
Terrain::SetHeightmap(AnyPtr<Image>)
[/code]
With that the SetHeightmap function (and any other function taking a "AnyPtr") accepts all pointer types it is configured for like T*, SharedPtr<T> and WeakPtr<T>. Without having to have the wrapper implicitly be convertible to T*, that implicit conversion is type safe offloaded to AnyPtr.
I've included a screenshot of the assembler output. It's practically cost free, depending on the case it can even be cheaper.[/quote]

Again, it re-introduces the issue from my original post. As far as semantics go, what does Terrain::SetHeitmap(AnyPtr<Image>) [i]mean[/i] semantically? Does Terrain own that resource afterwards? Or does Terrain hold a weak reference to it? Or does Terrain rely on the parent object's lifetime and simply hold a raw pointer?

The fact that Image [i]is[/i] a [b]RefCounted[/b] object makes it a shared object, end of story. It doesn't matter how many wrapper classes you create, you won't be able to change the semantic meaning. Like I tried to explained in my previous post, you are confusing SharedPtr<T> with std::shared_ptr.

What's wrong with just calling
[code]terrain->SetHeightMap(myImage.Get())[/code]
where [b]SetHeigtMap()[/b] accepts a raw pointer [b]Image*[/b]? It's clear that we're passing a raw pointer, and it's clear that since Image inherits RefCounted, it is a shared resource, meaning that Terrain could potentially gain ownership of the image passed. There is no confusion in this call.

-------------------------

gawag | 2017-01-02 01:11:48 UTC | #10

Ah, you got got me wrong there.
The idea of my AnyPtr is just to avoid overloads if one wants to not have a semantic meaning. Just as in "do stuff with X". For example blurring a given Image.
If one should pass a std::shared_ptr, the function should take a std::shared_ptr.
If the function should take a weak pointer, it should take a weak pointer.
The "dirty hack" that Urho is doing with it's T* when T is a child of RefCounted is pretty misleading as a naked pointer has no semantic meaning but the RefCounted naked pointer actually has a semantic meaning. Ideally there should be a type for this slightly different smart pointer.
The AnyPtr should be only used as a replacement for T* (with no semantic meaning) so that also a SharedPtr<T> (and maybe others as well) can be passed without requiring .Get().

To the player with the item example:
You are using an Item* but want to manage that resource. There's nothing hinting towards any kind of resource management as it is just a naked pointer. It would be clear if it would be a SharedPtr<Item> and the Item would be passed as a SharedPtr<Item>. We are in the age of smart pointers and having a naked pointer but wanting any kind of smart behavior from it can be considered a bug.

[quote]Again, it re-introduces the issue from my original post. As far as semantics go, what does Terrain::SetHeitmap(AnyPtr<Image>) mean semantically? Does Terrain own that resource afterwards? Or does Terrain hold a weak reference to it? Or does Terrain rely on the parent object's lifetime and simply hold a raw pointer?[/quote]
In the ideal case: It doesn't do anything with that Image afterwards. It may have modified it or copied it but it is safe to delete that Image directly after SetHeightmap.
I just looked at the code and the SetHeightMapInternal sets a SharedPtr with that given image. So it is using the Image shared but that was not hinted in any way as it only got an Image* originally.This hidden smart pointer stuff is really dirty.

So it kinda boils down to:
- wanting shared ownership without costs at every argument pass
- ideally: wanting to indicate that the thing the pointer is passed to will use it shared (like the SetHeightmap) or not care at all after leaving the function

[quote]
What's wrong with just calling
[code]
    terrain->SetHeightMap(myImage.Get())
[/code]
where SetHeigtMap() accepts a raw pointer Image*? It's clear that we're passing a raw pointer, and it's clear that since Image inherits RefCounted, it is a shared resource, meaning that Terrain could potentially gain ownership of the image passed. There is no confusion in this call.[/quote]
Two problems: Currently .Get() is not required and removing the implicit cast in SharedPtr to T* would break code. Secondly requiring .Get() everywhere adds a lot of code bloat. Both could be avoided by for example my approach with a converter class.
Also having to distinguish between naked pointers in general and naked pointers with the base RefCounted is pretty misleading. As already said having a zero cost type (like no ref count changes when copied and similar) would be better as it would be also fast (the speed reason you mentioned) but less misleading and add type safety.

I'm currently not seeing a perfect way to solve the issues with functions like SetHeightmap that ideally should take a shared pointer but without the cost.
Seems to be a common issue:
[stackoverflow.com/questions/8385 ... -reference](http://stackoverflow.com/questions/8385457/should-i-pass-a-shared-ptr-by-reference)
[stackoverflow.com/questions/3275 ... shared-ptr](http://stackoverflow.com/questions/327573/c-passing-references-to-stdshared-ptr-or-boostshared-ptr)
[stackoverflow.com/questions/1082 ... -arguments](http://stackoverflow.com/questions/10826541/passing-shared-pointers-as-arguments)
[herbsutter.com/2013/06/05/gotw- ... arameters/](https://herbsutter.com/2013/06/05/gotw-91-solution-smart-pointer-parameters/)

Though in the case of SetHeightmap the cost for passing a shared pointer by value can be neglected as that function isn't called that often. But there may be similar cases that are actually performance critical.
Besides the neglectable cost there's nothing speaking against Terrain::SetHeighmap(SharedPtr<Image>) am I right?

Hm one option would be Terrain::SetHeighmap(SharedPtr<Image>&). Zero cost at first but also "shareable" due to not being const. Still kinda dirty.

-------------------------

TheComet | 2017-01-02 01:11:48 UTC | #11

Maybe I'm missing something here, but how does your solution solve the problem in the first post?

Because from what I understand, you basically disagree with everything I proposed. I want to make these changes to fix a problem I encountered.
1) Force explicit use of [b]SharedPtr<T>::Get()[/b] instead of relying on implicit conversions
2) Add [b]bool operator() const { return ptr_ != NULL; }[/b]

You appear to disagree with 1) because of "code bloat". However, your solution doesn't fix any of the issues in my first post, so I don't know where that leaves us.

-------------------------

Dave82 | 2017-01-02 01:11:48 UTC | #12

[quote]gawag : You are using an Item* but want to manage that resource. There's nothing hinting towards any kind of resource management as it is just a naked pointer. It would be clear if it would be a SharedPtr<Item> and the Item would be passed as a SharedPtr<Item>. We are in the age of smart pointers and having a naked pointer but wanting any kind of smart behavior from it can be considered a bug.[/quote]

That's exacly what i thought too.

if a function returns a smart pointer you are responsible to pass it as a smart pointer.
This :
[code]Item* item = Item::create(ITEM_FLOWER);[/code]
looks like you intentionally try to make a mistake.If the return type is SharedPtr the use a SharedPtr
[code]SharedPtr<Item> item = Item::create(ITEM_FLOWER);[/code]

-------------------------

gawag | 2017-01-02 01:11:48 UTC | #13

[quote="TheComet"]Maybe I'm missing something here, but how does your solution solve the problem in the first post?[/quote]
I'm getting confused as well.

[quote="TheComet"]
Because from what I understand, you basically disagree with everything I proposed. I want to make these changes to fix a problem I encountered.
1) Force explicit use of [b]SharedPtr<T>::Get()[/b] instead of relying on implicit conversions[/quote]
Yes we agree on the implicit conversion being bad. But I saw problems resulting in removing that and tried fixing those.

[quote="TheComet"]
2) Add [b]bool operator() const { return ptr_ != NULL; }[/b][/quote]
That's also good, std::shared_ptr does that too.

[quote="TheComet"]
You appear to disagree with 1) because of "code bloat". However, your solution doesn't fix any of the issues in my first post, so I don't know where that leaves us.[/quote]
I don't disagree but it would force to add .Get() to every place where the implicit conversion was used (breaking old code). My solution fixes this at the places where a naked pointer was used "properly" (without any semantic meaning or sharing) without having the issues you mentioned (as it is not used shared).
In Terrain::SetHeightmap the Image* is actually used shared (if I got that right) but that is confusing as a naked pointer doesn't hint to that. So I suggested passing the SharedPtr either per value (extra cost) or per reference in such cases where the object is actually used in a shared way.

Oh I just notized this: Texture2D::SetData(SharedPtr<Image>). That function is actually getting passed a SharedPtr... And that function isn't using the Image shared at all. It's copying the data.
Why is Texture2D::SetData getting passed a SharedPtr but not using the Image in any way shared but Terrain::SetHeightmap is receiving the Image as a naked pointer but using the reference counting feature (using it shared)? Smells fishy. :unamused: 

Basically I'm suggesting to use a converter class in functions that don't use the ressource shared like Texture2D::SetData as it would allow to pass SharedPtr<Image> in there as well as Image* and that without having an implicit T* conversion in SharedPtr (as we want to get rid of that unsafe implicitness). And to use SharedPtr (potentially as a reference or somehow "disguised" for speed) in functions like Terrain::SetHeightmap that actually use the resource shared.
AnyPtr is also kinda clumsy especially when passing a naked pointer but I don't see a better solution if one doesn't want the implicit cast SharedPptr::T* or function overloads everywhere for every "pointer type".

Oh Dave82 posted while I was writing this. I completely agree with that post. *nonexisting thumbs up smiley*

Edit: Oh isn't a SharedPtr of a RefCounted object not kinda weird and doubled shared? Oh they work in conjunction, that's still odd.

Edit2: Also SharedPtr can't be used with any class: "error: 'class person' has no member named 'AddRef'" "error: 'class person' has no member named 'ReleaseRef'"
Someone not knowing that Urho specialty "But I thought it would be like std::shared_ptr or QSharedPointer or boost::shared_ptr or ...  :frowning: "

-------------------------

TheComet | 2017-01-02 01:11:48 UTC | #14

[quote="Dave82"]This :
[code]Item* item = Item::create(ITEM_FLOWER);[/code]
looks like you intentionally try to make a mistake.If the return type is SharedPtr the use a SharedPtr
[code]SharedPtr<Item> item = Item::create(ITEM_FLOWER);[/code][/quote]

You're missing the point. I'm saying it shouldn't be possible for this to compile:
[code]Item* item = Item::create(ITEM_FLOWER);[/code]

Of course you have to use a SharedPtr if the return type is a SharedPtr, but the fact of the matter is, if you happen to forget it is returning a SharedPtr and you use a raw pointer accidentally, the code compiles and runs anyway (and will later crash). This is what I'm trying to fix. Does that make sense?

[quote="gawag"]My solution fixes this at the places where a naked pointer was used "properly" (without any semantic meaning or sharing) without having the issues you mentioned (as it is not used shared).[/quote]

No, it still has the issues I mentioned. This code I posted earlier - which uses your [b]AnyPtr[/b] - shows exactly how the issue still exists.
[code]class Item {
public:
    static SharedPtr<Item> Item::create(Item_e item) {
        switch(item) {
            case ITEM_FLOWER: return new FlowerItem;
            /* etc */
        }
        return SharedPtr<Item>();
    }
};

class Player {
    Item* item_;
public:
    void HoldItem(AnyPtr<Item> item) {
        item_ = item;
    }
}[/code]

[code]Player player;
player.HoldItem(Item::create(ITEM_FLOWER));
// Oh oh, player.item_ is now pointing to a destroyed object
// This is exactly what I'm trying to fix, AnyPtr re-introduces the issue[/code]

I still fail to see how offloading the implicit conversion to a new wrapper class is any different than just leaving the implicit conversion as-is?

-------------------------

gawag | 2017-01-02 01:11:48 UTC | #15

[quote="TheComet"]
No, it still has the issues I mentioned. This code I posted earlier - which uses your [b]AnyPtr[/b] - shows exactly how the issue still exists.
[code]...
class Player {
    Item* item_;
public:
    void HoldItem(AnyPtr<Item> item) {
        item_ = item;
    }
}
...
[/code]

I still fail to see how offloading the implicit conversion to a new wrapper class is any different than just leaving the implicit conversion as-is?[/quote]
You are taking the AnyPtr and storing a shared resource in a naked pointer. Yes that can be done, but that is not what AnyPtr is supposed to be used for.
Your HoldItem could also receive a SharedPtr and still save it incorrectly as an Item* by using the .Get() function. As I already said, in that case you should use a SharedPtr.

I think misusing AnyPtr in that way can't be prevented. ...
Oh wait I think it can: If the AnyPtr does also not have an implicit cast to T*. Instead it can be compared like a pointer and does also have operator*. It would still be constructable via T* and any SharedPtr<T> and whatever, so that functions taking an AnyPtr would accept any pointer as intended.
Is that the solution?

-------------------------

rku | 2017-01-02 01:11:49 UTC | #16

[quote="TheComet"]I'm saying it shouldn't be possible for this to compile:
[code]Item* item = Item::create(ITEM_FLOWER);[/code]
[/quote]

I stepped on this rake once too. Not doing that again though. Is it not too much fuss over non-issue really? I prefer cleaner and more convenient code to write. Having to .Get() all over the place will be less clean and convenient. Besides in modern IDEs return type is mouse-over-method away in modern IDEs. While forcing .Get() in various contexts is indeed correct way to do it in theory - in reality it is not that practical. It would be annoyance. Minor one but annoyance. And for what? To avoid a bug that is immediately visible? Not worth it imho.

-------------------------

gawag | 2017-01-02 01:11:49 UTC | #17

The bug is not that immediately visible. Also I've made a suggestion how .Get() could be avoided and still be typesafe.

-------------------------

cadaver | 2017-01-02 01:11:50 UTC | #18

Texture2D::SetData does image = image->GetNextLevel(), which is runtime MIP calculation that returns a new image inside a new SharedPtr. In this case, forcing the user to pass a SharedPtr ensures the original image doesn't get destroyed within the function. It could be refactored to not manipulate the original image pointer, at the cost of slightly more complex code. In fact this would be preferable for more straightforward script bindings.

Terrain::SetHeightMap does nothing unusual, it just takes ownership of the passed image, in which case a raw ptr is sufficient. The Urho documentation states this of ownership in general:

"When an object's public API allows assigning a reference counted object to it through a Set...() function, this implies ownership through a SharedPtr. For example assigning a Material to a StaticModel, or a Viewport to Renderer. To end the assignment and free the reference counted object, call the Set...() function again with a null argument."

([urho3d.github.io/documentation/H ... tions.html](http://urho3d.github.io/documentation/HEAD/_conventions.html))

-------------------------

cadaver | 2017-01-02 01:11:51 UTC | #19

Texturexxx::SetData() has been changed in master branch to use just a raw pointer. It will now rather manage the created MIP images internally by a different shared pointer.

-------------------------

TheComet | 2017-01-02 01:11:59 UTC | #20

I've decided to not go forth with this change. I didn't understand SharedPtr when I made this thread and now I do. It makes a lot of sense to allow implicit casting from and to raw pointers.

-------------------------

