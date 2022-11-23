Eugene | 2020-02-06 08:46:53 UTC | #1

Okay, I'm gonna extract this question into separate thread to keep discussion on-topic.

Currently there's very good opportunity to move Urho from custom containers to proper 3rd party container library. Most of the porting is already done.

The issue is that this change is breaking. There are adapters that covers common cases but they don't provide 100% backward compatibility. And names are not in `CamelCase` /outcry of shock/.

What this migration offers:

- Container library maintained by _companies_ instead of custom-made library that nobody maintains;
- Move-semantics friendly containers;
- Containers that don't allocate memory dynamically;
- Algorithms;

Why one may want this change?

When a person is used to work with `std` container library in its entirety (more than just `vector.push_back`), using custom Urho Containers becomes a pain. There're so many things missing. I have refactored `Urho3D::Vector<T>` two times when I needed something from it and it's not even close to "enough".

Small buffer optimization? Nope. Allocators? Nope. Algorithms? Nope. Containers except vector and hash map? Nope. Move semantics? Barely. Spans and string views? Nope.

Urho is outsourcing physics, navigation, image decoding and tons of other tasks. Why it cannot outsource container library too?

So, what do you think? Is it worth it?

[poll type=regular public=true chartType=bar]
* [supportive] I want to switch to EASTL or std library.
* [supportive] I don't need any features from EASTL but I'm ok with switching to it.
* [against] I don't want to switch to EASTL but I have a proposal how to make Urho Containers more convinient to use.
* [against] I don't want to switch to EASTL and I have nothing to suggest.
[/poll]

-------------------------

1vanK | 2020-02-06 09:07:38 UTC | #2

Are there any tests comparing Urho and EASTL containers? As far as I understand, Urho3D containers are designed to binding with scripting languages and work fast. Who forbids users to use their own containers in their projects? I am not against progress, however, the loss of binding to scripting languages is a regression. C # cannot replace scripting languages because you cannot quickly call managed code from native code. You can only quickly call native code from managed code.

-------------------------

Eugene | 2020-02-06 09:22:12 UTC | #3

When I checked last time, script bindings are not heavily dependent on exact container types. They will need some revise, but I think it’s doable.

About performance... measuring performance properly is hard task that requires time and effort. I may try it when I have time for it.

-------------------------

Pencheff | 2020-02-06 11:03:42 UTC | #4

I'm totally voting up for EASTL, I love how Urho3D containers work right now, but the couple of times I had to extend with functionality that's already in STL I felt like I was failing a job interview. I don't mind spending 2 days refactoring my code replacing .Push with .push_back.

-------------------------

Modanung | 2020-02-06 11:10:22 UTC | #5

If this change is decided upon, it would probably be best to make it part of Urho 2.0.

[quote="Eugene, post:1, topic:5872"]
Urho is outsourcing physics, navigation, image decoding and tons of other tasks. Why it cannot outsource container library too?
[/quote]
Does this mean you are suggesting to wrap EASTL in Urho classes too? Could there be some backwards compatibility this way or engine modifications averted?

-------------------------

adhoc99 | 2020-02-06 11:15:55 UTC | #6

Yeah, great idea.
Aprove this here to pave the way for getting rbfx in regardless.

-------------------------

Eugene | 2020-02-06 11:45:45 UTC | #7

Don't mix topics.
This topic is about this specific feature _that I personally missed in Urho for years_.

Here is specific scenario:
People want to use Urho. Not some _fork_, but the master branch. I'm one of these people, but there are more. This is given.
People want to have decent container library in Urho. I'm one of these people, but there are more. This is given too.

What solution do you offer? I expect constructive answer here.

-------------------------

WangKai | 2020-02-06 13:01:32 UTC | #8

Could you guys pro stl changes divide the issue a little bit? Pls explain the eastl introduction to Urho3D a little technical detailed? 

As a proposal, shall we list merits and demerits? Challenges and opportunities? Future plans?

There will be a lot of code changes to Urho as well as your own code. If we gain more, only cost the unification and aesthetics of the engine, its opportunity.

I like the current containers, since they are just simple and good for my usage. But obviously, many people ask more and have their own needs and pains.

Edit: I have to point out that, rbfx's Editor is not because of the container changes, it is mainly because of the auther's hard working. I really respect that. So, I don't want to mix the rbfx's features with the introduction of stl.

There are many people who are silent in this community, including the leaders and ex-leaders, they may have their own private fork or workflow, or have quit using Urho, but for the containers change, please stand out and speak out.

-------------------------

Eugene | 2020-02-06 12:57:28 UTC | #9

Writing huge posts is always taxing. I may do it when I get energy for it.
// TODO:

-------------------------

Dave82 | 2020-02-06 13:03:05 UTC | #10

I support this idea unless it turns Urho into a gargantuan giant monster where opening the project in the IDE takes 10 minutes , the building process takes 1 hour and the resulted binary is over 30 mb ... Also i expect smooth out of box Cmake scripts without any hassle over fixing broken cumbersome scripts. Right now the cmake scripts (at least on windows) are perfect !! I download Urho3d , build it and start working on my game.

-------------------------

Eugene | 2020-02-06 13:46:33 UTC | #11

Sorry I missed your reply here.

[quote="Modanung, post:5, topic:5872"]
Does this mean you are suggesting to wrap EASTL in Urho classes too?
[/quote]
It would be a waste of performance and manpower to do it.

I understand beauty of having all code in single CamelCase style and whatever.
However, one-line trivial wrappers like we have for `Sqrt` is weird thing to do.

[quote="Modanung, post:5, topic:5872"]
Could there be some backwards compatibility this way or engine modifications averted?
[/quote]
There are CamelCase adapters in augmented EASTL containers to simplty porting. They are disabled by default and do not cover everything.

-------------------------

Modanung | 2020-02-06 14:24:43 UTC | #12

[quote="Eugene, post:11, topic:5872"]
I understand beauty of having all code in single CamelCase style and whatever.
However, one-line trivial wrappers like we have for `Sqrt` is weird thing to do.
[/quote]

I too am quite fond of this consistency, and if it would break over this, I think it would be better to use `std` (to avoid the road to Boost) and change the Urho code style accordingly _or_ leave things the way they are.

-------------------------

WangKai | 2020-02-06 14:19:41 UTC | #13

If the community is convinced, as long as EASTL itself alone does not break things too much, we may provide some scripts/way to help people migrate their own projects.

As for AngelScript, can we make things automatic? like SWIG for C#? So we just keep lua, AngelScript and scripts based Editor, as long as we don't have a better alternative yet so discarding any of the parts are not considerable. If people love C#, use it.

So, everyone is happy and Urho is stronger. Am I asking too much (based on the community size and contributor number)?

-------------------------

Eugene | 2020-02-06 14:34:12 UTC | #14

[quote="Modanung, post:12, topic:5872"]
I think it would be better to use `std` (to avoid the road to Boost) and change the Urho code style accordingly *or* leave things the way they are.
[/quote]
So you are considering only there two options: break *all* API compatiblity or do nothing.
This is quite unusual developement position.

[quote="1vanK, post:2, topic:5872"]
Are there any tests comparing Urho and EASTL containers?
[/quote]
I made quick benchmark, feel free to criticize because I'm totally not an expert in benchmarking.
 https://gist.github.com/eugeneko/2cbad3b16ca2f8e250d57a17c2d4d207
```
Run on (12 X 2208 MHz CPU s)
CPU Caches:
  L1 Data 32 KiB (x6)
  L1 Instruction 32 KiB (x6)
  L2 Unified 256 KiB (x6)
  L3 Unified 9216 KiB (x1)
----------------------------------------------------------------------
Benchmark                            Time             CPU   Iterations
----------------------------------------------------------------------
Trivial_StringVector_EA        1190020 ns      1199777 ns          560
Trivial_StringVector_Urho      5742792 ns      5719866 ns          112
Trivial_StringHashMap_EA       1692161 ns      1689189 ns          407
Trivial_StringHashMap_Urho     6291083 ns      6277902 ns          112
Real_StringVector_EA           1441662 ns      1443273 ns          498
Real_StringVector_Urho         6115403 ns      5998884 ns          112
Real_SmallStringVector_EA       355737 ns       352926 ns         1948
Real_SmallStringVector_Urho    2116384 ns      2128623 ns          345
Real_HugeHashMap_EA          385838650 ns    390625000 ns            2
Real_HugeHashMap_Urho       1074992600 ns   1078125000 ns            1
```

-------------------------

Modanung | 2020-02-06 14:43:41 UTC | #15

[quote="Eugene, post:14, topic:5872"]
So you are considering only there two options: break *all* API compatiblity or do nothing.
This is quite unusual developement position.
[/quote]
You are suggesting to break both compatibility _and_  consistency.

-------------------------

SirNate0 | 2020-02-06 15:01:42 UTC | #16

One concern I have with the benchmark is that it may be more of a test of the incremental creation of the strings than of the actual containers. What is you used the same object type for all of the containers (maybe key type as well for the maps, but I understand that might be an issue since the hash function needs to exist).

Also, the suggestion is to break comparability and internal Urho consistency in exchange for a (potentially) better preforming set of containers (and likely greater comparability with external library's that likely use the stl containers (which I believe share the same function names as EASTL, though not the same classes)).

-------------------------

Eugene | 2020-02-06 15:21:14 UTC | #17

Proposed compatibility changes differ in scope by the orders of magnitude. Smaller breaking change is always better than bigger breaking change, unless you have *strong* arguments for doing bigger change.

Consistently is weak argument. Urho way to wrap everything is perfectionism borderline to mental disorder. We have garbage code that is suboptimal and need to be maintained just to have fancy names.

Cmon, why on earth do we need Sqrt? Especially considering that we don’t wrap everything because it is impossible to wrap everything. So Urho is already inconsistent. The moment user wants to use anything from standard library, consistency is gone.

So what if we return vector instead of Vector? We already return bool and not Bool, and we use initializer_list instead of... whatever.

-------------------------

Eugene | 2020-02-06 15:20:48 UTC | #18

Thanks! That's really good point, I knew I missed something.

I tried it with ints.
I found one specific case when Urho wins.
```
Trivial_IntHashMap_EA       1538931 ns      1568775 ns          498
Trivial_IntHashMap_Urho      769266 ns       784738 ns          896
```
Small hash maps (e.g. 1000 ints) are qucker to fill due to allocator in Urho hash map.
I may try to write EASTL allocator to mimic this behavior, but I don't wanna do it now.

In the rest of cases Urho is either same or slower.

-------------------------

Modanung | 2020-02-06 15:33:32 UTC | #19

[quote="Eugene, post:17, topic:5872"]
Urho way to wrap everything is perfectionism borderline to mental disorder. We have garbage code that is suboptimal and need to be maintained just to have fancy names.
[/quote]

Changing the coding style together with switching to a container library would remedy this while upholding consistency.

@Eugene Could you include `std` containers in your tests?

-------------------------

Eugene | 2020-02-06 15:36:38 UTC | #20

[quote="Eugene, post:17, topic:5872"]
Changing the coding style together with switching to a container library would remedy this while upholding consistency
[/quote]
You know, I don’t oppose the idea of snake case itself, since it’s native code style of c++. Given choice, I would have probably started new library in this style. 

But the idea of global style change in Urho is unviable due to many reasons I don’t even care to mention.

-------------------------

Eugene | 2020-02-06 15:43:42 UTC | #21

About std containers, since you all keep mentioning them.

You see, I included std and EASTL in the same vote option for a reason. In order to switch to std, you have to switch to EASTL first, and *then* switch even deeper. I’m not kidding. EASTL is exactly between Urho Containers and std so we will have to pass this point anyway. 

So we can postpone all std-related questions until we completely switch to EASTL.

-------------------------

Modanung | 2020-02-06 15:46:34 UTC | #22

[quote="Eugene, post:21, topic:5872"]
In order to switch to std, you have to switch to EASTL first, and *then* switch even deeper.
[/quote]
Could you clarify this? Intuitively it just sounds like an extra leap.

-------------------------

rku | 2020-02-06 15:48:25 UTC | #23

[quote="Eugene, post:20, topic:5872"]
You know, I don’t oppose the idea of snake case itself, since it’s native code style of c++. Given choice, I would have probably started new library in this style.

But the idea of global style change in Urho is unviable due to many reasons I don’t even care to mention.
[/quote]

Same. I would **LOVE** to have snake_case codebase. At the same time it is a crazy undertaking. Not only because it is huge, but also because it is very error-prone. I have been there already. Switching to EASTL was not exactly easy. IDE could help only so much when renaming things. There always are code sections disabled by preprocessor where refactoring does not work. And when it works it isnt perfect. So who is going to do it?

-------------------------

Modanung | 2020-02-06 15:51:50 UTC | #24

[quote="rku, post:23, topic:5872"]
So who is going to do it?
[/quote]
I do not know, but it seems *unlikely* your stance increases the chances of it happening.

-------------------------

Eugene | 2020-02-06 16:24:52 UTC | #25

[quote="Modanung, post:22, topic:5872"]
Could you clarify this? Intuitively it just sounds like an extra leap.
[/quote]

Urho Containers doesn't have standard interface in any way. They have custom API names and style (CamelCase), custom features that don't really match `std`.

EASTL has standart API names and style (snake_case), and custom functionality (additional helper functions in containers and CamelCase bridges).

`std` is, obviously, standard.

So,

Urho: custom API, custom features;
EASTL: `standard` API, custom features;
`std`: `standard` API, `standard` features;

Every transition from "custom" to "`standard`" is manual and separate work in codebase.
So, transition from Urho to `std` is perfectly split into two phases:
1) Transition from Urho to EASTL, old interface is deprecated (partially removed and partially supported by adapters);
2) Transition from EASTL to `std`, old interface is removed.

-------------------------

adhoc99 | 2020-02-06 16:37:31 UTC | #26

Oh sure. These are totally not related. Not at all. My bad.
Just a convenient coincidente you need Urho Containers out of the way to get the road clear to rbfx.
Rbfx will totally not take over once EASTL is in.

-------------------------

Modanung | 2020-02-06 16:55:50 UTC | #27

@adhoc99 Although I understand your suspicion, please try to keep clear mind.

-------------------------

Eugene | 2020-02-06 16:57:56 UTC | #28

[quote="adhoc99, post:26, topic:5872"]
These are totally not related
[/quote]
Of course they are related!

Can you understand the concepts of "reason" and "consequence"?

I switched to rbfx **BECAUSE** I missed propper container library in Urho.
I want to merge some changes from rbfx (like EASTL) **BECAUSE** I want to have decent container library in Urho.

-------------------------

adhoc99 | 2020-02-06 17:01:10 UTC | #29

Yeah, but the timing and coincidence are very hard to ignore.

-------------------------

Modanung | 2020-02-06 17:01:41 UTC | #30

[quote="Eugene, post:28, topic:5872"]
Can you understand the concepts of “reason” and “consequence”?
[/quote]
Just because people acknowledge reality does not mean they all perceive it the same way.

-------------------------

rku | 2020-02-06 18:03:49 UTC | #31

@adhoc99 you have some VERY strong opinions for a nobody. I mean i do not recall ever seeing you posting anything. Of course i could be wrong, but your profile is conveniently private so we can not check. Seems to me like someone is afraid to speak their mind using their real identity and is hiding behind a dummy account. You do sound awfully a lot like @Modanung.

-------------------------

adhoc99 | 2020-02-06 18:11:17 UTC | #32

What part of *"Hello, this is my first time using the forum although I have been using Urho3D for about 2 or 3 years now."* is hard to understand?

Yeah, sure, let me dox myself, that is a great idea.

I'm not Modanung. Modanung has the patience of Saint and he have been here for ages. You should really apologize to him for saying that.

-------------------------

1vanK | 2020-02-06 18:14:38 UTC | #33

@adhoc99 Do you have github, gitlab profile or something like this?

-------------------------

adhoc99 | 2020-02-06 18:16:10 UTC | #34

Sure, but that would dox me.
Sorry, not going to happen.

-------------------------

Eugene | 2020-02-06 18:24:53 UTC | #35

@Modanung can you please transfer posts of @adhoc99, my responses to them, and your response in the middle, to rbfx thread?
And discussion in the tail too.
rbfx thread is already wasted, so let it be offtopic, but this one I want to keep on topic.

-------------------------

1vanK | 2020-02-06 18:20:17 UTC | #36

@adhoc99 I do not mind anonymity in the Internet, just your IP looks weird `tor-exit.r1.darknet.dev`

-------------------------

adhoc99 | 2020-02-06 18:23:08 UTC | #37

1vanK, that is because I am using https://www.torproject.org/
And that is exactly to protect my privacy.

-------------------------

bvanevery | 2020-02-06 18:42:48 UTC | #38

Would you guys please shut up about adhoc99 and get back to topic.  He's obviously not Modanung, any fool who's been following this forum for any time at all can tell that.  His emotional tones and cadence of speech are *completely* different.  And no, I have no reason to believe that Modanung is some kind of sock puppet *actor* doing a great job playing multiple roles.  Get over yourselves and shut up about the personality tiffs already.

Asking for a monolithic port of EASTL and the removal of currently working code, is *foolish*.  People who actually care about this, should be devising *incremental* strategies to gradually introduce EASTL into Urho3D.  Triggered by appropriate build switches, for those who actually want it.  Until such a time as it is *feature complete* and *well tested* as compared to currently working code.

This is like Software Engineering 101, or at least Open Source 101.  So who of you is going to actually start *doing* this?

Maybe some of you don't actually want to do this, you want the blessing for monolithic churn.  I personally don't think anyone should be giving that!  YMMV.

Long boring merges like this are not exciting.  Maybe the political angle is to create enough excitement, to get a rbfx developer to actually do something.  Or convince a Urho3D developer to do something.  But that doesn't actually matter past this moment, because what is proposed is a *marathon*.  You either have the discipline to run a marathon, or you *don't*.  You are best off being honest with yourselves about this now, instead of starting something you *won't* finish.

Pointing fingers at other people about what you want to have happen, isn't how open source gets done.  Those who wish to champion the EASTL cause, *get to work* already.  You dig into the codebases, you find something you can refactor, you provide a build flag for it.  It's boring and it's not rocket science.  It doesn't demand discussion.

Actually providing a minor build feature somewhere, is also proof-of-concept that you're *serious*, that you intend to stay the course.

If you eyeball all of that, and decide it's too much work in the real world, that's fine.  Happens to me looking at open source projects all the time.

-------------------------

Eugene | 2020-02-06 18:53:33 UTC | #39

[quote="bvanevery, post:38, topic:5872"]
Those who wish to champion the EASTL cause, *get to work* already
[/quote]
Sorry, what?.. Did you even read the starting post?
The work is already done. 100% for rbfx, therefore 80-95% for Urho.

[quote="bvanevery, post:38, topic:5872"]
gradually introduce EASTL into Urho3D. Triggered by appropriate build switches, for those who actually want it.
[/quote]
Can you elaborate how do you see build switch for containers?

This thing for every single line of code using containers?
```
#if URHO3D_EASTL
const auto first = pair.first;
#else
const auto first = pair.first_;
#endif
```

-------------------------

bvanevery | 2020-02-06 18:58:55 UTC | #40

[quote="Eugene, post:39, topic:5872"]
The work is already done. 100% for rbfx, therefore 80-95% for Urho.
[/quote]

BS.  When you have proof of concept in Urho3D *with a build switch*, and the limited case test works side by side with extant Urho3D code, I'll believe you.

If you think it's trivial to get this cooked up and demonstrated, great!  Have at it already.  Stop discussing, start showing.

-------------------------

Eugene | 2020-02-06 23:47:21 UTC | #41

[quote="bvanevery, post:40, topic:5872"]
When you have proof of concept in Urho3D
[/quote]
rbfx _is_ proof of concept Urho3D with EASTL containers.
If you disagree, prove me wrong.

[quote="bvanevery, post:40, topic:5872"]
If you think it’s trivial to get this cooked up and demonstrated, great! Have at it already. Stop discussing, start showing.
[/quote]
Go open rbfx samples. They are exactly the same as Urho samples and they run on EASTL containers.

[quote="bvanevery, post:40, topic:5872"]
with a build switch
[/quote]
Unless you propose any requirements on how said build switch should behave, it will not happen.
You want build switch? Do something for it. For example, explain requirements. What exactly do you want from said switch.

-------------------------

Modanung | 2020-02-06 19:10:15 UTC | #42



-------------------------

Modanung | 2020-02-07 00:25:26 UTC | #43



-------------------------

SirNate0 | 2020-02-07 05:36:36 UTC | #44

[quote="bvanevery, post:38, topic:5872"]
Asking for a monolithic port of EASTL and the removal of currently working code, is *foolish* . People who actually care about this, should be devising *incremental* strategies to gradually introduce EASTL into Urho3D. Triggered by appropriate build switches, for those who actually want it. Until such a time as it is *feature complete* and *well tested* as compared to currently working code.
[/quote]

On the one hand, I do agree that a sudden and complete jump to EASTL may be inappropriate (unless we timed it to coincide with the start of Urho's 2.0 work), I do feel the push for a build option enabling it is a pretty unreasonable request, as Eugene's  `#ifdef` example illustrates. If your proposal is instead we wrap the EASTL classes for the most part so that we can still call, for example, Vector::Front(), with some exceptions for HashMap's key value pairs,  I think that might be doable (though I still don't know if that could be enabled with a build option - unless we change a couple features of the Urho containers like switching to `first` instead of `first_`). Then again, I haven't looked much into how this would work, so others with more knowledge may be able to provide better insight.

Honestly though I don't care too much about what version of a hash map and the like we use. There are a few changes I do want, however. Firstly, PODVector is still slightly broken, and it would be nice for Urho to not have subtle bugs that will corrupt the heap. Stepping through hundreds of graphics driver memory 'issues' (I have no idea if they actually are bugs or not) to get to the point where my program actually wrote to the wrong address to learn that it was because you couldn't always Push a PODVector to itself was an awful experience.

Secondly, to ease the process of automatically generating script bindings without having to add a large number of annotations, I want every instance possible of `function(T* array, unsigned size)` to be replaced and/or supplemented by `function (span<T> array)`. (Replacement is my preference, but to avoid removing the existing API I would be content with simply adding the span function and then some additional work can be done to ignore the pointer,size overload)

If there is not strong opposition to the second, I will go ahead and start the work of adding span support to the library (and yes, I do plan on using EASTL for this). That would, I believe, meet your idea of gradually adding EASTL to Urho. I would like other's feedback on this first, though, as I don't like having all these pull requests lying around for features I've wanted that others were lukewarm to (particularly since the only thing I would directly gain from this is that my very, very side project of automatic script bindings might get easier).

-------------------------

Eugene | 2020-02-07 09:19:42 UTC | #45

[quote="SirNate0, post:44, topic:5872"]
If there is not strong opposition to the second, I will go ahead and start the work of adding span support to the library (and yes, I do plan on using EASTL for this)
[/quote]
Do you mean you will use EASTL span as it is? In this case, this would be awesome. 

[quote="SirNate0, post:44, topic:5872"]
wrap the EASTL classes for the most part so that we can still call, for example, Vector::Front(), with some exceptions for HashMap’s key value pairs, I think that might be doable
[/quote]

This is exactly what adaptors are. I didn’t test them on real code tho.

-------------------------

rku | 2020-02-08 08:31:19 UTC | #46

Frankly speaking: accepting EASTL is bare minimum required in order to get a chance for future. Without it merging anything from rbfx will be too hard and nobody will step up to do that. Do we need it? Not even remotely. I am fine doing merges from upstream. I do them often and there is so little upstream activity that huge divergence is not a problem. Urho3D needs this however. I already did all the hard migration work and @Eugene did astounding job to ease transition by implementing container adapters. It does not get better than that. This is your chance at **maybe** having a future. Take it or leave it. I dont think anyone else is coming to offer something like this.

-------------------------

dertom | 2020-02-08 09:50:35 UTC | #47

[quote="rku, post:46, topic:5872"]
This is your chance at **maybe** having a future.
[/quote]
Man, this is so ridiculous.

-------------------------

rku | 2020-02-08 10:01:59 UTC | #48

Please i would like to hear why. Project is stagnating. Nobody is stepping up. Most developed part of the engine by core devlopers is... build system. I do not see a way forward with no contributors. If you do please tell me. I know i can be wrong and i am ready to admit it.

-------------------------

Modanung | 2020-02-08 12:03:50 UTC | #49

And I wonder why rbfx has no forum to keep you busy, since it is doing so great.

-------------------------

1vanK | 2020-02-08 12:18:56 UTC | #50

[quote="rku, post:48, topic:5872, full:true"]
Please i would like to hear why. Project is stagnating. Nobody is stepping up. Most developed part of the engine by core devlopers is… build system. I do not see a way forward with no contributors. If you do please tell me. I know i can be wrong and i am ready to admit it.
[/quote]

You are absolutely right, it makes no sense to argue that the project is stagnating. But let's say we close the Urho3D project and rename rbfx to Urho 2.0. Will the number of developers increase? On my own, I can say that I just stay with the old version on my HDD, simply because there is functionality that I need. But in the new project I will not take part in the same way as I do not take part in the rbfx project.

-------------------------

rku | 2020-02-08 12:36:08 UTC | #51

Does getting updates from downstream count as increase of developers? Current state of things surely does not help developer retention, let alone increase. Urho3D lost me, @Eugene and now @Sinoid. This isnt exactly a healthy project growth.

-------------------------

1vanK | 2020-02-08 12:47:53 UTC | #53

That is, the whole thing is only in the name of the project? You will continue to work on rbfx just want it to be called Urho3d. And where to go to Urho3D users?

-------------------------

rku | 2020-02-08 14:28:16 UTC | #54

I do not want any users. I never intended to compete with upstream. All we wanted is to share some improvements we have made. Be friendly and contribute, you know. I do not want commit rights to urho repository. I do not want to deal with a community (especially this one). I am interested in code without drama. Some people somehow got the idea that we are looking to take over urho3d while @Modanung fishing for being project leader whose sole contribution is words, and not exactly kind ones towards some. We reiterated multiple times: all we want is to share. Do not want it - fine by me. Less work for @Eugene because after all of this i am not moving my finger to better this community in any way. We could have had a civil discussion that ends with "... but we respectfully decline because of technical reasons X Y Z". Instead very first reply to @Eugene's suggestion was calling my bloody sweat a "filth". This is just disgraceful. No good deed goes unpunished.

-------------------------

Modanung | 2020-02-08 14:42:04 UTC | #55

[quote="rku, post:54, topic:5872"]
I do not want any users.
[/quote]

You wish for rbfx to be useless? :face_with_raised_eyebrow:
Like a clockwork statue.

-------------------------

rku | 2020-02-08 16:18:34 UTC | #56

Nice try.

By the way im sorry for saying you are behind adhoc99 account. Now it seems to me it is pretty clear that you are not and i hope i misread your personality and you would never even think of pulling that stunt.

-------------------------

SirNate0 | 2020-02-08 16:10:52 UTC | #58

[quote="adhoc99, post:57, topic:5872"]
How dare we not bow down to the glorious gifts being offered.
[/quote]

@adhoc99 would you kindly not use the word "we" as if you speak for the community. I am not someone who uses rbfx and I am someone who uses AngelScript, so I have my doubts about accepting everything the rbfx users have offered, but I am supportive of things that would almost certainly improve Urho like a more complete and compatible set of containers. I am clearly a member of the community who's been here longer than you, and I would appreciate it if you didn't try to put words in my mouth.

-------------------------

Bluemoon | 2020-02-08 21:18:38 UTC | #59

From the heated discussion that has been going for few days I'm really getting a bit confused. 

Let me ask in all sincerity and not to offend anyone, if the reason rbfx was forked was for there to be a better alternative to the vanilla urho3d then why does there seem to be this aggressive push for urho3d to be like rbfx. If the devs and users of rbfx are cool with rbfx then why do they have to "rub it on our face" that rbfx is better than urho3d and/or that we should upgrade and be like them. Why can't they just go ahead using it in peace.

It is particularly disappointing that there is a barrage of vitriol, negative and condescending statements coming from the rbfx team against does that do not want to tow their path. If they really claim they care about Urho3d, observing from how its really been a messy debate, I really doubt them.

I am for progress in all of its form, but what I see going on here is either dominance assertion or a mockery campaign aimed at ridiculing users of Urho3d.

-------------------------

Eugene | 2020-02-08 22:24:57 UTC | #60

TL;DR: It went weird way.
Let this post be post-mortem of this event.

[quote="Bluemoon, post:59, topic:5872"]
why does there seem to be this aggressive push for urho3d to be like rbfx
[/quote]
If you read starting posts of both threads, they are both technical proposals with listed benefits and disadvantages. Proposals from _third party_ that has no authority to push these proposals without consent of Urho mainainers (Note: even if I tecnhically can merge my own PRs, I cannot do it without review and approval of other maintainers).

These proposals were met with accepting attitude from one part of community, conservative scepticism of another part of communtiy, and outright aggression from the third part, which was the most unpleasant part.

You see, when I spend hours writing a _proposal_, I expect it do be discussed, and accepted or declined. Apparently, certain part of community is incapable of discussion and prefer insults.

[quote="Bluemoon, post:59, topic:5872"]
It is particularly disappointing that there is a barrage of vitriol, negative and condescending statements coming from the rbfx team against does that do not want to tow their path
[/quote]
I'm not going to speak here for @rku, but I did my best to refrain from unfounded or exagerrated statements.
If you remember any, point me out so I can revise them with cooler head.
By the way, what do you call "rbfx team"? @rku and me or whole pro-rbfx side of the argument?

[quote="Bluemoon, post:59, topic:5872"]
observing from how its really been a messy debate
[/quote]
If you look at threads as a whole, you will see that the most of the mess was around single person thowing shit on the fan due to absense of moderation.

[quote="Bluemoon, post:59, topic:5872"]
I see going on here is either dominance assertion or a mockery campaign aimed at ridiculing users of Urho3d
[/quote]
I agree with you on this, with one comment.
This event *started* as technical proposal, and the outcome is what communtiy made of it.

-------------------------

George1 | 2020-02-08 23:22:24 UTC | #62

Here is an idea!
For the people who wanted to make Urho3d better.

1. Provide a summary in dot point on what they can do to this engine in terms of features, optimisation.
2. What is their plan on how to add these things.
3. What are expected to be broken if these things gets added.
4. How are you going to draw more developer and user to this engine?
5. Provide examples where the new changes or features that are better than the current Urho3d.

-------------------------

SirNate0 | 2020-02-09 20:23:48 UTC | #63

Assuming this is a feature by feature thing (as opposed to a more personal thing - X, you accepted to work on the engine, Y, you are not), how about this:

1. Add relative path support to the engine. This allows the grouping of resources more easily by map section or character, so that within, for example, "Map/World1/Level1/node.xml" resources can be identified as "./tree1.mdl", "./tree1leaves.png" without having to write out the full path for every resource. It also makes some situations of getting resources from the code simpler (I want the clothes.png file from the same directory as this character specification file, for example). 
2. See 6 below
3. Existing resource loading will be changed (all of the GetResource type functions), requiring an additional parameter (a base path) or switching the String resourceName (i.e. path) parameters to a separate Path class so that the relative paths can be resolved. The extra parameter will be inserted before the bool argument as it should be grouped with the actual resource path requested rather than whether an event is sent on failure. It will have a default empty string parameter, so only the case of specifically requesting an event not be sent on failure will existing user code need to be changed (and possibly also custom resources will need to be modified).
4. That's really not my job, but an engine that is easier to use is certainly not worse. Though you could argue that I have drawn at least one more user to the engine since my friend is now using it for his own project.
5. See 1. In terms of a cost-benefit, we gain support for relative paths at the cost of a *slight* increase in complexity in searching for a resource, which is likely not a bottleneck in anyone's programs, so this should be fine.
6. I submitted a [Pull Request](https://github.com/urho3d/Urho3D/pull/2070) for this addition two and a half years ago that is still open. Granted, since then I have let it grow out of date with Master so it needs an update to work again, but no one has really indicated support for or against it for over two years, so why would I bother updating the online branch when no one seems interested. I still use it, but I'd have to extract it from my other changes to the engine, which wouldn't be hard, but I'd just be maintaining a PR that no one seems to want or explicitly not want.

**Edit: A new thread has been created to discuss the above proposal. Please direct further comments about relative paths to https://discourse.urho3d.io/t/adding-relative-paths-to-resource-loading/5911**

I wrote the above mostly as an illustration of why I think Eugene has asked these questions on the forum. Except for very minor bug fixes (which are almost always very shortly accepted if the coding standards were followed), Urho hasn't always been too favorable towards adding functionality. It's not that it's been particularly unfavorable either, but I can't say that there's a small chance one's work will just sit unused or be outright rejected for even relatively minor changes like adding relative path support to resource cache loading (which does not break existing functionality, and could be made to not alter existing APIs as well). 

Certainly, I don't think your questions are unreasonable, but at the same time how is answering them going to help solve anything?

That aside, here's another set of answers specifically for the containers question

1. Replace existing Urho containers with EASTL containers. These provide the same guarantee as Urho's container about consistent cross-platform behavior and size, can also be configured to assert instead of throwing exceptions, and can be modified/extended for Urho as a single set of code as opposed to the highly platform-specific code of the STL. In addition, they add additional types of containers Urho does not have out of the box (and that few are likely willing to reinvent just so Urho can have one as well given the many opensource ones available that would save said developer's time). One such example is `span`, which would allow us to replace (or extend) our current interfaces that are along the lines of `T* array, unsigned size` to a (hopefully) less error prone form that should also be easier to automate script bindings.
2. This work has mostly away been completed by Eugene (and possibly others from rbfx), though I intend to add the span support myself.
3. HashMap key value pairs will require removing the underscore from `first_` and `second_` (or potentially very fat wrappers to reference the old names to the new ones). Other minor changes may be required, but I am unaware of them at this point.
4. Same as 4 above. I'm still not sure why this question was asked, particularly in this thread.
5. At least one of Urho's containers is subtly broken in a way not covered by the documentation but only mentioned in some GitHub issues. PODVector cannot safely Push a value from itself into itself, i.e. `PODVector<int> v{1,2,3}; v.Push(v.Front());` is unsafe and can corrupt the heap, in this case a very difficult to track down bug since it doesn't always happen (only when the vector just be resized) and it will simply write a little past the end of the array, so likely no segmentation fault). Likely this bug has existed for years in Urho without anyone noticing until relatively recently. Rather than having to find and fix these bugs ourselves, we can use the work of others and focus on the important issues in the engine like graphics and such, rather than spending hours on yet another implemention of a Vector in c++. Beyond this, we gain many types of containers Urho has no implementation of which, while not a great benefit, is nice to be able to use a single library's containers rather than mixing and matching Urho's and another libraries.

-------------------------

Modanung | 2020-02-09 04:01:41 UTC | #64

[quote="SirNate0, post:63, topic:5872"]
Add relative path support to the engine.
[/quote]
This *does* sound like a nice feature to have. :thinking:

-------------------------

George1 | 2020-02-09 06:36:50 UTC | #65

Ok, with those idea that you have.
What are your plan to execute it?  What are the expected timeline...  What are the priority?

Is relative path hard to do?  Can't you manually support it?     Some game uses package  pk2 etc.

My concern is putting too many things up without a clear plan, schedule  and task allocation is not how things should be operated.  I can come up with 20 things, but that won't help much.

-------------------------

Eugene | 2020-02-09 10:49:59 UTC | #66

[quote="George1, post:65, topic:5872"]
My concern is putting too many things up without a clear plan, schedule and task allocation is not how things should be operated.
[/quote]
Have Urho ever had clear plan, schedule and task allocation in the past?
Don't really remember it.

---

Maybe I will be obvious here, but I think I understand the core of the argument.
It is about prioritizing. Preservation before development or development before preservation.

One thinks we should keep what we have first, because otherwise we will harm and chase away exising users.

Another thinks we should develop even if it means reasonable losses in functionality and/or compatibility, because it is pointless to preserve something outdated and outmatched (it's not about Urho as a whole, but about certain aspects of it).

First group considers this event as an attempt to enforce rbfx politics onto Urho without care about existing users.
Second group considers this event as an attempt to break stagnation of the engine they like and use.

aaa: Why do you have to break code that works?
bbb: Why don't you stay on stable version if you are fine with current state of things?
aaa: Why don't _you_ just move to fork and change it as you wish?
bbb: Why don't _you_ move to fork and keep it unchanged?

As you can see, this argument is very symmetric and very subjective, so I won't comment it in any way.

-------------------------

Modanung | 2020-02-09 12:08:22 UTC | #67

[quote="Eugene, post:66, topic:5872"]
Preservation before development or development before preservation.
[/quote]
Moving forward only makes sense when facing the right direction.

-------------------------

Eugene | 2020-02-09 13:38:14 UTC | #68

[quote="Modanung, post:67, topic:5872"]
Moving forward only makes sense when facing the right direction.
[/quote]
Lasse pretty much confirmed that Urho doesn't have and never had any direction.
Therefore, no matter what direction is choosen, there will be ones who disagree with said direction (=doesn't consider it "right").

-------------------------

George1 | 2020-02-09 14:47:12 UTC | #69

Current Urho3d is feature complete to me.  It only need a faster,
 pretty, rendering technique.

-------------------------

Modanung | 2020-02-09 14:02:34 UTC | #70

Any vector with a non-zero magnitude has a direction. Direction is not the same as a 5-year plan that has been set in stone and signed with blood.

-------------------------

Eugene | 2020-02-09 14:06:36 UTC | #71

[quote="George1, post:69, topic:5872"]
Current Urho3d is feature complete to me
[/quote]
It's good.
What are your reasons to participate in this discussion instead of using current version of Urho from now on without any care about future plans?
We do it with 3rd-party libraries all the time. You are fine with version -- you stick with it.

[quote="George1, post:69, topic:5872"]
It only need a faster
pretty render technique.
[/quote]
Can you please elaborate? I don't really understand what do you mean here.

-------------------------

rku | 2020-02-09 14:33:12 UTC | #72

[quote="Modanung, post:67, topic:5872"]
right direction
[/quote]

What is a right direction for some people may not be a right direction for others. This means there is no right direction. Nor wrong one. People who write code set the direction. You can write the code and promote direction you see as right. Just like we do.

-------------------------

George1 | 2020-02-09 14:43:45 UTC | #73

1) Urho current PBR implementation is slow and not complete.
2) Urho defer render, lightning method is not pretty.  
3) We need xxAO variant of render technique support.  Your variant of AO looks good.

If you think you can identify the trajectory and milestone for your proposal, you should first come up with a plan. Identify the required tasks and time line.  This will help inform people so that they can support your topic.

It seems to me that most of the posts in this thread are individual targeting and bashing without much constructive material.  This maybe due to lack of persuasive approach and plan given. 

I know that you and some others have been here long enough and contributed to some area in the engine, which is great.      But I do think some people really act like they are god, which is really getting out of hand :slight_smile:   

Anyway, I'm supporting any changes and bug fixes that help this engine.  Please give some constructive information to persuade the community.

-------------------------

Eugene | 2020-02-09 15:06:34 UTC | #74

Thank you for elaborate answer.

I do have certain plans that partially cover your items, but I’m not sure about implementation details. It’s always risky and hard to make changes in Urho renderer. 

I’m the type who prefer talking about something after it’s done, not before or in-progress. For example, I’ve posted my lightmap/GI solution the moment I considered it finished and ready to use, not incomplete prototype for show.

I have several ideas how to change renderer, but I will not make any plans or promises until I confirm they will work out well.
I want to try one radical approach, but it will require huge commitment of effort and therefore you will not get any updates in the nearest months about it.

-------------------------

Modanung | 2020-02-09 22:16:50 UTC | #75

4 posts were merged into an existing topic: [Adding Relative Paths to Resource Loading](/t/adding-relative-paths-to-resource-loading/5911/6)

-------------------------

cosar | 2020-02-12 00:53:42 UTC | #80

@Eugene @rku Any pull requests for EASTL coming soon? :slight_smile: 
Given EASTL compatibility with stl, it's going to be very easy to switch to stl containers in the future if needed. For now, it looks like a decent choice.

@Modanung We all appreciate what you do, but the engine does lack contributors today, and Eugene and rku are to be appreciated for their willingness to move urho forward. Sometimes a leader has to compromise a little on his vision for the greater good.

@adhoc99 You are very disruptive. You remind me of Leith (if you are not him). A change in your attitude might be beneficial to you too.

-------------------------

Eugene | 2020-02-12 06:48:24 UTC | #81

[quote="cosar, post:80, topic:5872"]
Any pull requests for EASTL coming soon?
[/quote]
You see, I’m not willing to deal with AngelScript bindings. 
They may be nice for user, but they are a hindrance for ones who want to make wide-scope changes.
And Urho cannot abandon AS, since about 1/3 of people here (or so I think, according to poll) really want AS.

If you want to get EASTL in Urho, you probably better ask people who are ready to deal with AS whether they want to do such PRs, not me.

Maybe I will eventually try to do such PR, even if it means working with AS, but I’m totally not in the mood to do it now, not after reaction I got. If so many people are reluctant to accept just EASTL, why would I push?.. I still somewhat want to try PR EASTL into Urho, but it’s very low priority task for me.

-------------------------

Modanung | 2020-02-12 15:03:58 UTC | #82

21 posts were split to a new topic: [Script binding automation](/t/script-binding-automation/5921)

-------------------------

Modanung | 2020-02-12 14:09:29 UTC | #86

@cosar I very much appreciate @Eugene's presence, but "forward" is a subjective term that - if a project is not to rip itself apart - has to be agreed upon before taking leaps. Part of @rku's efforts have been directed at actively demotivating engine and game developers alike from continuing to use and contribute to Urho3D. I appreciate his positive contributions, but he has often displayed the opposite.

-------------------------

Modanung | 2020-02-12 14:19:35 UTC | #89

2 posts were merged into an existing topic: [About rbfx and Urho3D](/t/about-rbfx-and-urho3d/5913/21)

-------------------------

cosar | 2020-02-12 17:32:36 UTC | #90

@Eugene If you don't want to deal with AS bindings, then just don't do it. If you are willing to, you can get the branch started and change to EASTL without modifying AS bindings (you can disable AS) and somebody else can step in for helping with the bindings. I guess I can find some time to help if needed.

-------------------------

cosar | 2020-02-12 17:41:36 UTC | #91

@Modanung I understand your position, but the truth is that Urho3D had a significant drop in contributions for some time now. I know I probably shouldn't talk since I don't contribute,  but I do like this engine and I would love to see it moving forward.
One good thing from all this discussions is that there is still a lot of interest to see this engine thrive. Maybe @Eugene and @rku can also pull back a little bit and help getting things from rbfx one by one with support from the rest of Urho3D community.

-------------------------

Eugene | 2020-02-12 17:54:57 UTC | #92

[quote="cosar, post:91, topic:5872"]
Maybe @Eugene (...) can also pull back a little bit and help getting things from rbfx one by one with support from the rest of Urho3D community.
[/quote]
As I said, it may happen in the future after I finish my current tasks.
It was my intention in the beginning, as I explained in the very first post, but after received pushback I’m not inspired to change anything in Urho for now.

About EASTL branch... you see, unless AS is dealt with, such branch will never get merged, and I hate wasting time on something that may never get merged. I can start working on EASTL branch when/if I have the confidence I can complete this work on my own.

-------------------------

bvanevery | 2020-02-14 20:25:45 UTC | #93

[quote="Eugene, post:92, topic:5872"]
unless AS is dealt with, such branch will never get merged
[/quote]

From a technical "all options on the table" standpoint, this statement is *false*.  Code that does EASTL could be merged, if it leaves AS mechanisms *alone*.  2 different ways would have to be supported, for quite some time.  "Merge" doesn't mean "I take over with my way, you have to lose *your* way."  Migration strategies, in general, do not have to be all-or-nothing propositions.  They *can* require end users to make choices, like what feature set they're going to utilize, and making people rewrite some code if they want to migrate.  Providing multiple options *does* increase complexity and work, especially for test coverage.  In software engineering, that is generally the cost of keeping working code working.

From a *personal energy* standpoint, it is of course true that you will work on, whatever you actually want to work on.  If you don't have the software engineering appetite for doing a long term incremental migration to EASTL, and really only would ever choose to implement a simpler, all-or-nothing, disruptive approach, that's your choice.

I just hope we're all clear on what is *possible*.  The tradeoff is *work*.

People look at any given rbfx "feature" or "offer" in exactly the same way.  What people will actually do, depends on what people think is important to actually build towards.

-------------------------

Eugene | 2020-02-14 20:45:15 UTC | #94

[quote="bvanevery, post:93, topic:5872"]
From a technical “all options on the table” standpoint, this statement is *false* . Code that does EASTL could be merged, if it leaves AS mechanisms *alone* .
[/quote]
If some class is moved to EASTL, then interface of this class is likely to change too.
If interface changes, bindings have to be updated in order to build scripts.
If bindings are not updated, then PR cannot be merged due to broken bindings.
Therefore, without changing bindings PR cannot be finished. 
Please point out what exactly statement here is false. 

[quote="bvanevery, post:93, topic:5872"]
If you don’t have the software engineering appetite for doing a long term incremental migration to EASTL, and really only would ever choose to implement a simpler, all-or-nothing, disruptive approach, that’s your choice.
[/quote]
You keep talking about incremental migration, but you never offered a solution regarding how migrated modules shall interact with not migrated modules without redundant overhead.

Unless you have something in mind, please refrain from suggesting unviable strategies.
I have no clue how to incrementally migrate A without touching B:
```
class A
{
	Vector<int> GetNumbers();
};

class B
{
	void Update(A* a)
	{
		numbers_ = a->GetNumbers();
	};
	Vector<int> numbers_;
};
```

-------------------------

bvanevery | 2020-02-14 21:21:24 UTC | #95

[quote="Eugene, post:94, topic:5872"]
If some class is moved to EASTL, then interface of this class is likely to change too.
[/quote]

Write a 2nd one.  Or subclass it.  FFS why do you think C++ and OO got popular in the 1st place?  Why do you always talk about *moving* things?  Why not *adding* things?

[quote="Eugene, post:94, topic:5872"]
If bindings are not updated, then PR cannot be merged due to broken bindings.
[/quote]

This sounds like some managerial policy BS that could be addressed *if* someone had a reason to do so.  Like if additive EASTL insertions were valued.

[quote="Eugene, post:94, topic:5872"]
you never offered a solution
[/quote]

Of course I didn't.  It's all details, down in the weeds.  I've got my sleeves rolled up for *other kinds of game development* right now.  You just keep talking categorically like these sorts of things can't be addressed in projects, and *they can.*  Long Ago, I got paid real money to work on CMake build systems, for Mozilla.  I can hum a few bars at software engineering and migration.  This isn't rocket science stuff.  It's a question of *will*, and *realism* about how much work something entails.

I *get it* if you don't want to do migration and build systems "flip a switch" stuff.  I got good at that sort of thing, because of all the people in Open Source Land who *don't* relish doing all that stuff.  Leaving *me* to figure out how to even build their !#$!#$ broken ass software.  And it was ultimately a career ender, I got real good at something I *hated*.

[quote="Eugene, post:94, topic:5872"]
without redundant overhead.
[/quote]

*What* is your problem with that?  *Pay a cost* already.  SW ENGR 101.

-------------------------

Eugene | 2020-02-14 21:37:18 UTC | #96

[quote="bvanevery, post:95, topic:5872"]
Write a 2nd one. Or subclass it. FFS why do you think C++ and OO got popular in the 1st place? Why do you always talk about *moving* things? Why not *adding* things?
[/quote]
Did you ever considered that non-incremental "all-together" migration may cost *by the order of magnitude* less effort than incremental?
Writing a second interface is _a lot_ of work. And only a fraction of classes may be subclassed in Urho.
[quote="bvanevery, post:95, topic:5872"]
Of course I didn’t. It’s all details, down in the weeds
[/quote]
It's very easy to be theorethical and speak about abstract changes in abstract projects and how they should be done in perfect world.
Sometimes the world is not perfect and abstract solutions don't work here as well as in dreamland.
For example, you proposed abstract solution may cost 10-100 times more than solution already implemented, de-facto making whole migration thing unviable.

[quote="bvanevery, post:95, topic:5872"]
*What* is your problem with that? *Pay a cost* already
[/quote]
Did you really just suggested to introduce redundant performance overhead in _real-time game engine_?

If we go incremental, we introduce performance loss at the joints between old and new containers.
And performance loss is something I care about, especially in real-time game engine.

-------------------------

bvanevery | 2020-02-14 21:41:33 UTC | #97

[quote="Eugene, post:96, topic:5872"]
Did you really just suggested to introduce redundant performance overhead in *real-time game engine* ?
[/quote]

Yes.  You clearly think like a bog standard 3d optimization jock, not a project manager concerned with multiple generations of user support.  You wouldn't believe the amount of stuff that exists in CMake to support backwards compatibility for build systems.  You dismiss engineering solutions that are obvious to other people in the computer industry because they are *not perfect, speed of light code*.  Get over that, and you can actually solve the political issue with Urho3D and rbfx development.  *If* you want to.

The problem is you like EASTL in the 1st place because you believe in speed of light code and don't want to ever compromise.

Here is your political framework at the build system level:
USE_URHO_CONTAINER - no new code
USE_EASTL_CONTAINER - only new EASTL code, breaks AS and anything else in your way.
USE_BOTH_CONTAINER = USE_URHO_CONTAINER & USE_EASTL_CONTAINER - the most difficult mode that makes both work simultaneously.  *It can sacrifice some performance.*

Your political goal is to get people to move between the 3 categories.  Until such a time most people don't value the old stuff anymore and it can be gotten rid of.  That will be years from now.

-------------------------

Eugene | 2020-02-14 22:48:01 UTC | #98

[quote="bvanevery, post:97, topic:5872"]
Yes. You clearly think like a bog standard 3d optimization jock,
[/quote]
Great.
So, user had his nice function in the engine API that returned `String` by reference and has literally zero cost.
User used this function a lot in the hotpath.
Then we do migration, and now this function always return copy of `String` because there is no more `String` because underlying container was migrated to `ea::string`.
This may literally nuke whole application performance.
And you are saying this is totally fine because nobody should expect real-time game engine to work fast. Right?

[quote="bvanevery, post:97, topic:5872"]
Here is your political framework at the build system level:
USE_URHO_CONTAINER - no new code
USE_EASTL_CONTAINER - only new EASTL code, breaks AS and anything else in your way
[/quote]
There is _no new code and no old code_. There is just one copy of code, with very high level of entanglement and a lot of containers.

[quote="bvanevery, post:97, topic:5872"]
and don’t want to ever compromise.
[/quote]
I don't want to implement detached from reality suggestions from a person who has no clue about the task. If you used some approach to solve your tasks in the past, it doesn't mean that the same approach works on all tasks in the world.

I understand the concepts of migration and legacy compatibility and how it should be done, and I employ this approach more often than not.
I also see no proof that your proposed approach is even remotely viable in _this specific task_.
Past experience _with completely different tasks_ is not a proof. Neither authority is.

[quote="bvanevery, post:97, topic:5872"]
not a project manager concerned with multiple generations of user support
[/quote]
[quote="bvanevery, post:97, topic:5872"]
don’t want to ever compromise.
[/quote]
I'm ready to compromise and I'm concerned about legacy compatibility.
I also understand physical limitations and understand that sometimes it is de-facto impossible to upgrade things perfectly.

> It’s all details, down in the weeds

I've seen a lot of project managers (it was a lie, I think I saw only one or two) who forget that the code is the core. And architectural or management decision is worthless if it doesn't take into consideration the code it is going to be implemented in.

I've spent a lot of time thinking how to make container migration as smooth as possible, and I haven't found acceptable solution. And here you are, saying that it's totally doable and giving literally zero actual practical advice. What gives you a reason to think that person who never worked on the task knows more than a person who spent a lot of time doing said task?.. I'm not a project manager and I'm not an architect, but I worked on the architecture and I'm not an idiot.

-------------------------

bvanevery | 2020-02-14 23:48:31 UTC | #99

You asked why.  The answer is you're basically biased towards your favorite piece of tech, EASTL.  You don't see the reality of other people wanting their stability.  Like a lot of open source developers, it's not that important to you.  Nobody's *paying* you to make it important, so you don't look for a win-win solution.

You aren't thinking in terms of phased migration, either in your own work, or in other people's work.  Developers can make choices about whether string functions are critical to them.  They can rewrite some code as they migrate, if the new regime is bringing enough benefits in other areas.  To worry about whether USE_BOTH_CONTAINER is suboptimal, is to completely miss the point that it's a *transitional* framework.  If people *really* care about the performance of something, they're going to either go forwards to the EASTL and no AS approach, or stay back on the USE_URHO_CONTAINER approach.  *Your* goal *should* be to get people to migrate forwards.  If you're serious about transitions, and implementing "depreciations", like big projects like CMake or OpenGL actually do in the real world.

What do *I* get out of participating in this discussion?  I've been watching Urho3D for a long time.  I know the project leadership and more importantly project *cooperation* is in trouble.

I'm *hoping*, that you are clever enough to see what I'm telling you, so that I don't *personally* have to show you how to implement EASTL without harming AS.  Because if I have to do that, then you haven't contributed any development value to me.  In fact it would pull me deep into the weeds for an issue I'm *not* that vested in, "what the perfect container class is, and how that can contribute to other rbfx migrations".  But I've been around the block in Open Source often enough to know what the technical and political dimensions of the problem are.  It's a shame to see a concept fail, for lack of know-how.

I *can* help you with the CMake build system end of the problem.  I don't care what Weitjong has cooked up, I'm quite sure I can implement whatever he thinks is The Right Way To Do It.

The real question, to me, is whether you actually want to change the DNA of Urho3D over time, *or* you just want to do everything your way because that's easy for you.  It's not easy for everyone else which is why such generous offers in open source are respectfully declined.  Making everyone happy is *work*.  A price must be paid somewhere, either in designing interfaces, or performance, or multiple transitional steps over time.  A user might ultimately have to write 3 versions of code to make a final transition to your new regime.  If they can do that *gradually*, and keep things working without suffering *too much* performance loss to get there, it's a win.

-------------------------

Eugene | 2020-02-15 05:51:29 UTC | #100

[quote="bvanevery, post:99, topic:5872"]
You aren’t thinking in terms of phased migration, either in your own work, or in other people’s work.
[/quote]
I am, and the current state of affairs (migration all at once, optional container adapters) is *already* the best and the smoothest way to migrate I managed to find. You (person who never touched the task) keep saying there is a better way, while I (person who spend a lot of time on this task) don’t see any. It’s not just me being stubborn, you know.

[quote="bvanevery, post:99, topic:5872"]
they’re going to either go forwards to the EASTL and no AS approach, or stay back on the USE_URHO_CONTAINER approach.
[/quote]
It is technically impossible to make existing Urho code work with both old and new containers without significant decrease in code quality, maintainability and/or critical impact on performance.
If you think otherwise, please provide *arguments*, not baseless theoretical statements detached from reality.
If you think it’s possible, prove it. Explain on real code (e.g. Node), not on imaginary examples.

If you don’t have time or willingness to do so, that’s totally fine, you don’t owe us anything. Just remember that suggestions from a person who never worked on the task have very little relevance. It’s too easy to talk about perfect solutions when you have no codebase limiting your fantasies.

-------------------------

SirNate0 | 2020-02-15 05:45:09 UTC | #101

@bvanevery While I don't doubt your experience in related issues in other projects, I'm going to have to take Eugene's side in this. Even if someone were to make a PR in which support were added for both EASTL and the Urho containers, presumably through a large number of `#ifdef`'s, I would actually recommend against accepting that into the Urho codebase. It seems pointless to me to have twice the number of functions (and five+ times the number of lines) in header files alone for *everything* that uses a container. Simplicity is a good thing, and this seems like trying to make many times the present work that would be required simply for the sake of people not having to refactor their code to use `first` instead of `first_`.

[quote="bvanevery, post:99, topic:5872"]
A user might ultimately have to write 3 versions of code to make a final transition to your new regime. If they can do that *gradually* , and keep things working without suffering *too much* performance loss to get there, it’s a win.
[/quote]

Personally, I think this is only sometimes true. Certainly, it could be (dividing breaking changes into minor refactoring sessions seems like a pretty decent approach, overall), but what if, following your own setup, it's something like user has to spend 1 hour refactoring now vs half an hour every few months. I think then the win is actually with just getting it over with quickly - here's where you were, here's a clear list of instructions for how to port to the new containers, it should take an hour or two, have at it (rather than dragging it out marking features as deprecated and removing them slowly piece by piece (so user's code ends up broken several times over rather than once).

Also, others may disagree, but I don't see how doing many times the work so others can make all the same changes (just later rather than sooner) is a win for Eugene. It's a win-win for the paid developers *because* they get paid to make the other people win, but I don't really see how Eugene wins in this situation (nor, for that matter, how we add the community win other than that someone is volunteering their effort to bring an improved container library to Urho)

That's not too say I don't agree with some of your ideas. By all means, let's go for a gradual transition, provided it's only going to be a bit more work and not like ten times as much. I would like some clarification as to how you think cmake solves the problem, though - wouldn't that literally just be adding a cmake option that adds a preprocessor define? (Which, speaking from personal experience, is really straightforward with our build system - just copying the existing cmake code and changing some names). Perhaps I'm just missing something, though. I have very limited knowledge of cmake.


[quote="Eugene, post:11, topic:5872"]
There are CamelCase adapters in augmented EASTL containers to simplty porting. They are disabled by default and do not cover everything.
[/quote]

@Eugene, do you know what features are missing from these? If it's not too many (i.e. unless that actually makes the classes useless) I say we add an anonymous union to Pair<> between first and first_, etc., and mark the underscore variant as deprecated, as well as all the other functions not supported by the adapters. Then in a few months from now, or perhaps with version 2.0, we actually switch to early EASTL (as long as someone deals with the AngelScript bindings). Thoughts?

-------------------------

bvanevery | 2020-02-15 10:40:25 UTC | #102

At this point, I believe Eugene lacks the will to steward this transition.

I am insufficiently invested in the core issues, "EASTL --> migrating rbfx features", to provide a solution for him.  I will bow out from any further discussion of rbfx related stuff.  AFAIAC, it's all DOA.  My opinion after reading *many* posts now.

I will save my Urho3D potential energy for my own, currently undisclosed core concerns.  My own issue is, they tend to run counter to a lot of publicly expressed concerns.  Worst case, Urho3D has no value to me.  But I'm on the cusp of either writing my own 3D engine or trying to make Urho3D work.

I believe open source is about *one's will*, and not about squabbling with any developer over the details.  Like whether something is "advised" or not, or will be "more work for someone".  People who *want* something to happen, go make it happen.  Then others follow in their wake, because they *actually did the work, and it works.*  That is how open source projects actually get changed.  It may not be Open Source 101, but it's no more than a 300 level course in What Is To Be Done.

-------------------------

1vanK | 2020-02-15 11:11:05 UTC | #103

When viewing the rbfx repository, I am increasingly convinced that switching to EASTL containers is simply a change for changes. There is nothing ideal in them and they have to be supplemented with the necessary functionality. In theory, we probably get some kind of speed increase (which is debatable, since no one checked the difference in real projects) and get an ugly syntax that stands out from the general style. Just as it is necessary to add functionality to EASTL, we can fix / modify / improve Urho3D containers.

p.s. That's not cool https://github.com/rokups/rbfx/blob/master/Source/Urho3D/Container/Str.cpp

-------------------------

Eugene | 2020-02-15 11:00:25 UTC | #104

[quote="bvanevery, post:102, topic:5872"]
I am insufficiently invested in the core issues, “EASTL --> migrating rbfx features”, to provide a solution for him.
[/quote]
Or, in other words, you can only talking about abstract ideas and have no clue how to implement your own suggestions.

I wonder if you ever did transition as pervasive as container switch in project with strict performance requirements.

[quote="bvanevery, post:102, topic:5872"]
At this point, I believe Eugene lacks the will to steward this transition.
[/quote]
At this point, I believe that you understand only a fraction of issues that arise in this task. You are addressing only the issue of compatibility, completely ignoring the rest of issues related to code quality and performance in critical paths.

When several Urho developers tell you that your suggestions are unviable, it means something, you know. I believe that any Urho contributor will tell you the same.

-------------------------

Eugene | 2020-02-15 11:13:02 UTC | #105

[quote="1vanK, post:103, topic:5872"]
Just as it is necessary to add functionality to EASTL, we can fix / modify / improve Urho3D containers.
[/quote]
Are you ready to invest hundreds of hours into Urho containers so they get on the level of standard library? I wasn’t, and so I switched. 
Standard library exists for a reason.

[quote="1vanK, post:103, topic:5872"]
and get an ugly syntax that stands out from the general style
[/quote]
This is syntax of standard library. You cannot get rid of it.
Wrapping every single name in CamelCase for sake of consistency is weird path to walk. I prefer making interesting things instead of reimplementing things already done.

-------------------------

1vanK | 2020-02-15 11:19:46 UTC | #106

> Are you ready to invest hundreds of hours into Urho containers so they get on the level of standard library

The fact is that I have never experienced any problems with standard containers. In the end, you can use any containers in your projects, why change the containers that the engine uses?

-------------------------

Eugene | 2020-02-15 11:31:55 UTC | #107

[quote="1vanK, post:106, topic:5872"]
In the end, you can use any containers in your projects, why change the containers that the engine uses?
[/quote]
Because I don’t only write code for my projects, I write code for the engine. Also, using multiple container libraries require ugly transition layer in between.

[quote="1vanK, post:106, topic:5872"]
The fact is that I have never experienced any problems with standard containers.
[/quote]
You have just admitted that you cannot properly utilize C++ standard library.
Because a person who regularly uses C++ to full extent cannot *not* complain about non-standard container library missing features. 

For example, if you are good C developer and used to write code this way, you will see no benefit in migration from C++98 to C++11. They will both look the same for you. However, for a person who used to use C++11, such migration will be critical, because on C++98 they will feel crippled.

Same for Urho containers. If you learned 5% of standard library and that’s enough for you, Urho Containers will be fine for you too. If a person learned 90% of standard library, Urho containers are quite annoying to use.

-------------------------

1vanK | 2020-02-15 11:34:30 UTC | #108

Can you show your projects?

-------------------------

Eugene | 2020-02-15 11:44:55 UTC | #109

Define “projects”.
Also, I don’t get how this question is related to topic.
Considering that I just said I don’t need EASTL in Urho for projects. I need it for the engine itself.

-------------------------

1vanK | 2020-02-15 12:12:55 UTC | #110

> Define “projects”.

...

> Considering that I just said I don’t need EASTL in Urho for projects. I need it for the engine itself.


Is Urho3D works 5% of opportunities, but rbfx 100%?

-------------------------

Eugene | 2020-02-15 12:21:51 UTC | #111

I have published my project few weeks ago and you have seen it. You either have terrible memory or different definition of the word “project”

And yes, if we are speaking about fine tuning and optimization capabilities, it is 5% vs 100%. With Urho containers you have no options, only default vector on heap, default string on heap and default hash table on heap. And no algorithms, except sorting.

-------------------------

1vanK | 2020-02-15 12:27:01 UTC | #112

As an inexperienced user, I understand best of all through examples. What restrictions have you encountered?

-------------------------

