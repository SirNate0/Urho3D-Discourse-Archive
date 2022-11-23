sabotage3d | 2017-01-02 01:11:21 UTC | #1

Is there any way to do aggregate initialization with Urho3D containers? Similar to std::initializer_list and the nice functionality of Boost's Assignment library:[url]http://www.boost.org/doc/libs/master/libs/assign/doc/index.html[/url] .

-------------------------

rku | 2017-01-02 01:11:31 UTC | #2

Does not look like it. However it is easy to add:
[code]
#include <initializer_list>
#include <utility>

    /// Aggregate initialization constructor
    HashMap(std::initializer_list<std::pair<T, U>> list)
    {
        for (auto it = list.begin(); it != list.end(); it++)
        {
            Insert(Pair<T, U>(it->first, it->second));
        }
    }
[/code]

Note that this uses c++11 features therefore urho needs to be built with -DURHO3D_C++11=ON

EDIT:
Although i noticed we cant still do SendEvent("Some event", {{"key", value}}); due to fact that SendEvent() does not take const VariantMap. This is very unfortunate. Sure we could add overload with const and cast constness away but IMO it would be better to just make VariantMap const. But it triggers ugly cascade of changes in source code. Bummer.

-------------------------

weitjong | 2017-01-02 01:11:31 UTC | #3

A few events actually expect the VariantMap to be non-const. The map can be used as input as well as output. i.e. the event handler can also put data into the map so that the event sender can read it back.

-------------------------

rku | 2017-01-02 01:11:31 UTC | #4

[quote="weitjong"]A few events actually expect the VariantMap to be non-const. The map can be used as input as well as output. i.e. the event handler can also put data into the map so that the event sender can read it back.[/quote]


Well maybe it is not that big of a problem, since events are executed right on SendEvent() call. Until SendEvent() completes that const VariantMap is guaranteed to be alive anyway and there is little harm done in modifying that variant map in calls like SendEvent("...", {{"a", 1}}). However it could be a problem if someone makes wrong assumption and passes his own instance of const VariantMap and it gets modified while user expects it to not be touched. So either risk that or give up "SendEvent("...", {{"a", 1}})" in favour of uglier "VariantMap args = {{"a", 1}}; SendEvent("...", args)". I personally hate writing two lines where one does suffice and is even more readable. Another solution would be boost way which looks like "VariantMap()(key, value)(key2, value2)" but i dont like it. It is a hack for pre-c++11 times. IMHO we should use built-in language stuff first if it is available. What do you think right way would be to go about this?

P.S. I already implemented these constructors for urho's containers + SendEvent() with casting constness away. Ill make a PR when we figure out this const thing.

-------------------------

yushli | 2017-01-02 01:11:31 UTC | #5

I would like to see this feature in main branch soon. It helps keep code more concise.

-------------------------

rku | 2017-01-02 01:11:33 UTC | #6

Meanwhile you can use it as a patch if you want: [github.com/r-ku/Urho3D/commit/1 ... 82facbefd1](https://github.com/r-ku/Urho3D/commit/12d5f535c288155c3040a5720fc22382facbefd1)

-------------------------

sabotage3d | 2017-01-02 01:11:33 UTC | #7

I always thought we have to conform to C++98 for PRs. Is that a new flag URHO3D_CXX11?

At the moment I have settled for this syntax.

[code]Vector<float> vec;
vec += 1.0, 2.0, 3.0, 4.0;[/code]

Using this template without C++11.

[code]template<typename S, typename T>
Urho3D::Vector<S>& operator += (Urho3D::Vector<S>& v, const T & item)
{
    v.Push(item);  return v;
}
template<typename S, typename T>
Urho3D::Vector<S>& operator,(Urho3D::Vector<S>& v, const T & item)
{
    v.Push(item);  return v;
}[/code]

-------------------------

rku | 2017-01-02 01:11:33 UTC | #8

Yes that flag seems new. Aside from passing relevant compiler param (like -std=c++11) and adding preprocessor define its not used anywhere else. Although IMO we should take advantage of these new features. Would be especially handy if we could use lambdas in place of URHO3D_HANDLER(). Ill definitely add that for myself.

-------------------------

weitjong | 2017-01-02 01:11:33 UTC | #9

I think you guys meant compiler define. Yes, that "URHO3D_CXX11" is defined exactly for this kind of usage. The idea is to ease the transition to c++11 standard. Naturally since we could not (yet) set the c++11 standard as the default now, nothing should break when the new standard is not enabled. If you can ensure that then I think there is a good chance the patch such as this one will be accepted when you submit it as PR. However, having both const and non-const VariantMap version of SendEvent() may not be a good idea.  I recall we have already address the constant reallocation issue of event data map by reusing the map object. See the Context::GetEventDataMap().

-------------------------

rku | 2017-01-02 01:11:34 UTC | #10

weitjong what do you think solution for const problem should be then? I mean requiring to write
[code]
VariantMap args = {{"a", 1}};
SendEvent("event", args);
[/code]
instead of
[code]
SendEvent("event", {{"a", 1}});
[/code]
is solving aggregate initializer problem only half-way. Everyone would really appreciate ability to use them in-place on one line.

-------------------------

sabotage3d | 2017-01-02 01:11:34 UTC | #11

If we can use C++11 I think Variadic templates are far more readable for functions than using initializer lists.

-------------------------

gawag | 2017-01-02 01:11:34 UTC | #12

[quote="sabotage3d"]If we can use C++11 I think Variadic templates are far more readable for functions than using initializer lists.[/quote]
Yeah I would prefer them too.
Also initializer lists are completely broken when used together with a variadic template, they really screwed that up. I tend to avoid initializer lists due to that completely.

Though variadic templates are more expensive compile time wise and force function definitions into headers which initializer lists do not (I think).

-------------------------

weitjong | 2017-01-02 01:11:34 UTC | #13

[quote="rku"]weitjong what do you think solution for const problem should be then?[/quote]
I don't have the solution for that. Instead of creating another overload taking const VariantMap,  probably it is user own responsibility to do the const_cast when calling the existing one. And perhaps if we really want to create an overload to make SendEvent() usage simpler then we should make a variadic  template version of it, as already suggested by others. I believe we could implement a new one that internally call GetEventDataMap(), populate the map object with variadic arguments, and then call the existing SendEvent(). Thus, replacing the whole boilerplate code for sending event to just one line of code, similar to what you setup to do initially. 

I think the aggregate initialization with Urho3D containers has its merit points in its own right.

-------------------------

TheComet | 2017-01-02 01:11:35 UTC | #14

[quote="weitjong"]A few events actually expect the VariantMap to be non-const. The map can be used as input as well as output. i.e. the event handler can also put data into the map so that the event sender can read it back.[/quote]

This seems very wrong to me. The very idea of an event is to transport data from A to B and not the other way around, simply because the event sender cannot know who's listening.

Would it be possible to extract those few cases where receivers put data back into some other mechanism?

[EDIT] A dirty hack would be to make the signature const, but have those few cases use const_cast.  :smiley:

-------------------------

rku | 2017-01-02 01:11:35 UTC | #15

[quote="TheComet"][quote="weitjong"]A few events actually expect the VariantMap to be non-const. The map can be used as input as well as output. i.e. the event handler can also put data into the map so that the event sender can read it back.[/quote]

This seems very wrong to me. The very idea of an event is to transport data from A to B and not the other way around, simply because the event sender cannot know who's listening.
[/quote]

I lean towards agreeing with you, but obviously thats not how Urho's events are designed. They are more like a wrapper over a function calls rather than events, because SendEvent() directly invokes event handlers. In turn we suffer from various issues like lack of control during which stage event is invoked or inability to send events from other threads too.

-------------------------

weitjong | 2017-01-02 01:11:35 UTC | #16

[quote="TheComet"][quote="weitjong"]A few events actually expect the VariantMap to be non-const. The map can be used as input as well as output. i.e. the event handler can also put data into the map so that the event sender can read it back.[/quote]

This seems very wrong to me. The very idea of an event is to transport data from A to B and not the other way around, simply because the event sender cannot know who's listening.

Would it be possible to extract those few cases where receivers put data back into some other mechanism?

[EDIT] A dirty hack would be to make the signature const, but have those few cases use const_cast.  :smiley:[/quote]

Those cases are really a few. I can think of two events as it was contributed by me not long ago. See NavigationEvents.h and DatabaseEvents.h. These events are not supposed to be subscribed by multiple listeners. But of course there is nothing prevented that and should they actually send conflicting data input. You are welcome to change it if there is better way. Unless the signature has been changed, I treat the map object as the container to communicate data between event sender and event subscribers in both directions (although mostly only one direction).

Regarding sending events in worker threads, I believe that topic has been discussed here in the forums too. This is the latest discussion I could find quickly using google. [topic1753.html](http://discourse.urho3d.io/t/sending-event-from-non-main-thread/1687/1).

-------------------------

cadaver | 2017-01-02 01:11:35 UTC | #17

Allowing the VariantMap to be modified is a feature, think of it as a return value. When doing that it's true that you've got to be careful if you have multiple subscribers.

-------------------------

weitjong | 2017-01-02 01:11:49 UTC | #18

The variadic template version of the SendEvent() method is just in.

-------------------------

rku | 2017-01-02 01:11:50 UTC | #19

I think it is messed it up. How about simpler:
[code]void Object::SendEvent(StringHash eventType, const VariantMap& eventData)
{
    VariantMap& globalEventData = GetEventDataMap();
    for (auto it = eventData.Begin(); it != eventData.End(); it++)
        globalEventData.Insert(it);
    SendEvent(eventType, globalEventData);
}[/code]

Does exactly what variadic one does, however it can be used in a obvious way passing {{"a", b}, {"c", d}}. Also it does not need to be under c++11 so everyone can get it. As a nice bonus it does not bloat executable by making separate function for every N of pairs we pass.

-------------------------

weitjong | 2017-01-02 01:11:50 UTC | #20

In a nutshell what you proposed is similar to what I have just done, except that my approach requires less punctuation marks. The variadic template is type safe. The compiler would ensure you cannot enter garbage parameter type in or that the parameter list is not correctly paired up. As for the bonus, I would even say mine has the advantage. A good C++11 compiler should resolve the recursiveness of the variadic template during compile time and inline the call, while your loop may or may not be unrolled to achieve the same result.

-------------------------

rku | 2017-01-02 01:12:08 UTC | #21

What i proposed is proper way of doing things. That template function is abuse of programming language. It is counter-intuitive as well as possibly generating bloat because thats what c++ templates do. Yes, it saves two characters, but at what expense?

-------------------------

sabotage3d | 2017-01-02 01:12:08 UTC | #22

Templates are the way to go especially in C++11 and C++14. The only clean way of doing inifinite number of arbitary arguments are variadic templates.

-------------------------

weitjong | 2017-01-02 01:12:08 UTC | #23

I would just address your concern of the code bloat part. I believe it is actually unfounded. I have briefly explained in my previous comment why I believe that. I can even confirm that because I had already done the unit test before submitting the patch. In my test it showed that the generated assembly code from the variadic template (when fully optimized using -O3) had resolved all the recursive calls and all the functions were being inlined as if I had written all the boilerplate code by hand.

-------------------------

