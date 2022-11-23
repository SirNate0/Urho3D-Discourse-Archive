1vanK | 2020-10-21 10:19:16 UTC | #1

We already had a discussion about `auto`, but here is an example that excessive using `auto` degrades the readability of the code, rather than improves it <https://github.com/urho3d/Urho3D/pull/2700>. I suggest using `auto` only where it leads to notable code shortening (like `map<int,list<string>>::iterator`)

-------------------------

Modanung | 2020-10-21 14:23:47 UTC | #3

It's the Marklar of marklar-oriented marklar.

-------------------------

Eugene | 2020-10-31 09:27:38 UTC | #4

I'm going to continue [PR](https://github.com/urho3d/Urho3D/pull/2712) discussion here.

> In fact, I do not see people with whom I can argue about this

This topic is kinda vague now: "let's use auto less" is not really a rule.

If you disagree with current coding conventions regarding `auto`, please make explicit proposal how to change this section of coding conventions:
![image|690x130](upload://2pKNgsQy9ffvbJbqoCquH6UYeHC.png) 

And let's discuss it here. @Miegamicis writes code, so I think he would care?

> But Eugene blocks my PR

I don't. You block your own PR by not following Urho coding conventions enforced by CI.
I don't understand how you can blame me for _you_ breaking rules.
Of if you see yourself above coding conventions and you have the right to violate them however and whenever you wish, just say so.

-------------------------

Modanung | 2020-10-31 09:48:12 UTC | #5

[CppCoreGuidelines](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#es11-use-auto-to-avoid-redundant-repetition-of-type-names) advise the following:

> 
> ### <a name="Res-auto"></a>ES.11: Use `auto` to avoid redundant repetition of type names
> 
> ##### Reason
> 
> * Simple repetition is tedious and error-prone.
> * When you use `auto`, the name of the declared entity is in a fixed position in the declaration, increasing readability.
> * In a function template declaration the return type can be a member type.
> 
> ##### Example
> 
> Consider:
> 
>     auto p = v.begin();   // vector<int>::iterator
>     auto h = t.future();
>     auto q = make_unique<int[]>(s);
>     auto f = [](int x) { return x + 10; };
> 
> In each case, we save writing a longish, hard-to-remember type that the compiler already knows but a programmer could get wrong.
> 
> ##### Example
> 
>     template<class T>
>     auto Container<T>::first() -> Iterator;   // Container<T>::Iterator
> 
> ##### Exception
> 
> Avoid `auto` for initializer lists and in cases where you know exactly which type you want and where an initializer might require conversion.
> 
> ##### Example
> 
>     auto lst = { 1, 2, 3 };   // lst is an initializer list
>     auto x{1};   // x is an int (in C++17; initializer_list in C++11)
> 
> ##### Note
> 
> When concepts become available, we can (and should) be more specific about the type we are deducing:
> 
>     // ...
>     ForwardIterator p = algo(x, y, z);
> 
> ##### Example (C++17)
> 
>     auto [ quotient, remainder ] = div(123456, 73);   // break out the members of the div_t result
> 
> ##### Enforcement
> 
> Flag redundant repetition of type names in a declaration.

The Urho3D coding conventions used to have a link to these guidelines, but it seems to have disappeared.

-------------------------

1vanK | 2020-10-31 09:52:02 UTC | #6

[quote="Eugene, post:4, topic:6449"]
I don’t understand how you can blame me for *you* breaking rules.
[/quote]

After all, you wrote these rules and they were not discussed enough.

-------------------------

1vanK | 2020-10-31 09:53:28 UTC | #7

[quote="Eugene, post:4, topic:6449"]
Of if you see yourself above coding conventions and you have the right to violate them however and whenever you wish, just say so.
[/quote]

I can't break the rules that don't work anyway. I opened the first file that came across and showed examples of this.

-------------------------

rku | 2020-10-31 09:57:27 UTC | #8

[quote="1vanK, post:7, topic:6449"]
I can’t break the rules that don’t work anyway. I opened the first file that came across and showed examples of this.
[/quote]

Rules changed. Nobody did a pass over old code to change it all. How is that of any issue? New code follows new rules. Old rewritten code follows new rules. I do not see a conflict honestly.

-------------------------

1vanK | 2020-10-31 09:57:51 UTC | #9

I see a conflict in the fact that Eugene wrote the rules that he doesn’t like by himself and left to another project. And we must adhere to these rules.

-------------------------

rku | 2020-10-31 09:59:24 UTC | #10

There was a poll with considerable majority voting for following c++ core guidelines, which i believe `auto` rules derive from. https://discourse.urho3d.io/t/coding-guidelines/3509

-------------------------

1vanK | 2020-10-31 10:01:25 UTC | #11

> There was a poll with considerable majority voting for following c++ core guidelines, which i believe `auto` rules derive from. [Coding Guidelines](https://discourse.urho3d.io/t/coding-guidelines/3509)

Just show me this vote and I'll shut up. Personally, I did not participate in any voting.

-------------------------

Modanung | 2020-10-31 10:02:32 UTC | #12

https://discourse.urho3d.io/t/coding-guidelines/3509

-------------------------

rku | 2020-10-31 10:04:10 UTC | #13

![image|690x342](upload://iQxATJKwoSceJQ9k9X7IxijvFWF.png) 
You also participated in the thread. When people abstain from voting they either have no opinion or do not care.

P.S. I do not like current style guidelines either by the way. Yet there is nothing else to do other than follow them.

-------------------------

1vanK | 2020-10-31 10:05:04 UTC | #14

Ok you're right then I admit my mistake

-------------------------

Modanung | 2020-10-31 10:34:27 UTC | #15

What mistake?

The guidelines tell us to avoid `auto` in general, and provides examples of cases it _should_ be applied to, exactly as you suggested in this thread's OP.
Despite these guidelines being voted _in_, it seems the link to them was removed. **[false]**

-------------------------

Eugene | 2020-10-31 10:32:41 UTC | #16

[quote="Modanung, post:15, topic:6449"]
Despite these guidelines being voted *in* , it seems the link to them was covertly removed. :face_with_raised_eyebrow:
[/quote]
I don’t quite follow wdym. Link to CppCG is still in Urho coding conventions, as it was since my thread years ago. Do you mean some other link?

-------------------------

Modanung | 2020-10-31 10:33:42 UTC | #17

Ah, I wasn't looking at HEAD.

-------------------------

1vanK | 2020-10-31 10:36:45 UTC | #18

By the way, we voted for CppCoreGuidelines. But in rules refs to another resources. Wtf?

-------------------------

Eugene | 2020-10-31 11:13:29 UTC | #19

[quote="1vanK, post:18, topic:6449"]
CppCoreGuidelines. But in rules refs to another resources.
[/quote]
I don’t quite follow wdym (2). Can you quote what particular reference you are taking about?

-------------------------

1vanK | 2020-10-31 11:30:52 UTC | #20

CppCoreGuidelines is a fairly extensive document. I even doubt that those who voted for him have studied it entirely. Didn't it contain rules for using `auto`? Why need refs [here](https://clang.llvm.org/extra/clang-tidy/checks/modernize-use-auto.html) and [here](https://google.github.io/styleguide/cppguide.html#auto). By the way, I agree with the paragraph that you wrote in the rules and it does not contradict what I propose. But  need to remove links to rules for which there was no vote.

EDIT: I would even replace this paragraph with one sentence. Use auto only if it shortens your code significantly.

-------------------------

1vanK | 2020-10-31 11:49:46 UTC | #21

 https://clang.llvm.org/extra/clang-tidy/checks/modernize-use-auto.html

very funny document.

> TypeName *my_pointer = new TypeName(my_param);
> // becomes
> auto *my_pointer = new TypeName(my_param);

Now we have ```auto* ui = GetSubsystem<UI>();```.

-------------------------

Modanung | 2020-10-31 11:55:40 UTC | #22

I don't understand people who stick their asterisks & ampersands to the variable name at definition.

-------------------------

rku | 2020-10-31 11:55:58 UTC | #23

Following core guidelines is a recommendation, not an absolute requirement.

[quote="1vanK, post:21, topic:6449"]
Now we have `auto* ui = GetSubsystem<UI>();` .
[/quote]
That is a perfect example of how to use guidelines. Yes, it is two letters more. On the other hand it is many letters less for other subsystems. Net win.

-------------------------

1vanK | 2020-10-31 11:57:32 UTC | #24

Can you quote me where I said that all `auto` need to be removed?

-------------------------

Modanung | 2020-10-31 11:59:08 UTC | #25

Well, there _is_ something to be said about consistency.

As an aside, I believe the bar for using `auto` should be quite a bit higher within samples.

-------------------------

1vanK | 2020-10-31 12:02:51 UTC | #26

[quote="rku, post:23, topic:6449"]
Following core guidelines is a recommendation,
[/quote]

If this is not a rule, but a recommendation, then I can either follow it or not, at my discretion, right?

-------------------------

Modanung | 2020-10-31 13:26:21 UTC | #27

In my view the keyword has most value within the head of `while`s and `for`s. Here we are dealing with (up to) three statements in a row, often containing a long iterator type name.
Generally, when `auto` replaces a type at the beginning of a line, readability is impaired. If you write `auto` to save on _keystrokes_, I think you may:

* Not be using autocomplete properly
* Want to rethink some of your type names
* Add a `using` definition

-------------------------

Eugene | 2020-10-31 13:21:59 UTC | #28

[quote="1vanK, post:20, topic:6449"]
CppCoreGuidelines is a fairly extensive document. I even doubt that those who voted for him have studied it entirely.
[/quote]
Yep. CppCG as code style reference wouldn’t work — it’s way too huge to be strictly followed. I tried to extract the most relevant bits briefly on Urho code style page.

Current rules regarding auto are very formal. They are easy to follow and leave no room for personal discussion. They are even automatized with CI.

“Use auto when it makes code significantly shorter” is bad rule. Not because I disagree with it in principle, but because exact interpretation depends on user. How much is “significantly”? Can you formulate this rule in the way that every person will follow this rule the same way? If no, it’s just pointless to have such rule in document.

I would say that the most important aspect of code style quality is not whether the code looks good, but whether the code style is formal enough to leave no room for argument.

-------------------------

1vanK | 2020-10-31 13:26:12 UTC | #29

Do you keep claiming that it's okay
```auto* ui = GetSubsystem<UI>(); .```

-------------------------

rku | 2020-10-31 13:27:53 UTC | #30

[quote="1vanK, post:24, topic:6449, full:true"]
Can you quote me where I said that all `auto` need to be removed?
[/quote]

I may have misunderstood example with `UI` subsystem. The fact that `auto` is longer by two letters was the only thing that stood out like a downside..

[quote="1vanK, post:26, topic:6449"]
If this is not a rule, but a recommendation, then I can either follow it or not, at my discretion, right?
[/quote]
Not at your discretion. At project's discretion. Documentation lists notable exceptions. However if such exception is not listed we should observe surrounding code and follow it as an example.

[quote="1vanK, post:29, topic:6449, full:true"]
Do you keep claiming that it’s okay
`auto* ui = GetSubsystem<UI>(); .`
[/quote]
Could you please clarify what you think is wrong here?

-------------------------

Modanung | 2020-10-31 13:35:36 UTC | #31

[quote="rku, post:30, topic:6449"]
[quote="1vanK, post:29, topic:6449"]
Do you keep claiming that it’s okay
> `auto* ui = GetSubsystem<UI>(); .`
[/quote]

Could you please clarify what you think is wrong here?
[/quote]

1. Class name syntax highlighting tends to be brighter than common code
2. Eye inertia is disturbed during lookup
3. `auto` is the only part of the C++ language that does not provide information

-------------------------

Eugene | 2020-10-31 13:32:16 UTC | #32

[quote="1vanK, post:29, topic:6449"]
Do you keep claiming that it’s okay
`auto* ui = GetSubsystem<UI>(); `
[/quote]
It doesn’t concern me. I am fine with both options (with or without auto).

-------------------------

1vanK | 2020-10-31 13:39:27 UTC | #33

[quote="rku, post:30, topic:6449"]
Not at your discretion. At project’s discretion. Documentation lists notable exceptions. However if such exception is not listed we should observe surrounding code and follow it as an example.
[/quote]

Did the project arise by itself or was the project created by people? Whyam I not allowed to vote? I was here even before Eugene and many others. The vote was about the C ++ Core Guidelines document. But not for others documents. Therefore, need to give links only to C ++ Core Guidelines.

-------------------------

Modanung | 2020-10-31 13:44:57 UTC | #34

[quote="rku, post:30, topic:6449"]
However if such exception is not listed we should observe surrounding code and follow it as an example.
[/quote]

This is _exactly_ what conventions and guidelines are there to avoid.

![](https://camo.githubusercontent.com/af8ab25a01950e0bc6545d2dfa5cb428296bd5a4/68747470733a2f2f6c75636b657970726f64756374696f6e732e6e6c2f696d616765732f6c6f6769632e706e67)

-------------------------

rku | 2020-10-31 13:46:03 UTC | #35

Who did not allow you to vote? Thread discussing it was public. You abstained from vote. However even if you voted you would have been a minority. This is what happens when many more people participate. About half of participants may not get what they want unfortunately. I do not believe there is a way to make every single person happy.

I did not vote to have `_` suffix for class fields either. I hate it. So what..

[quote="Modanung, post:34, topic:6449"]
This is *exactly* what conventions and guidelines are there to avoid.
[/quote]
This is also not realistic in practice, even though ideal in theory.

-------------------------

Modanung | 2020-10-31 13:47:22 UTC | #36

[quote="rku, post:35, topic:6449"]
This is also not realistic in practice, even though ideal in theory.
[/quote]

Conventions are not the same as auto-programming. Choices will have to be made.

-------------------------

Eugene | 2020-10-31 13:49:53 UTC | #37

[quote="1vanK, post:33, topic:6449"]
Whyam I not allowed to vote?
[/quote]
If you had issues with current items in Urho code standard, you should have risen them when there was discussion and before these items were added and enforced by WeiTjong. You had months to voice your objections. Why didn’t you?

-------------------------

rku | 2020-10-31 13:51:01 UTC | #38

Choice pool is very large. Documenting each possible variation takes a lot of effort. If we all, instead of bikeshedding in the forum, sat down to write such conventions, we would not finish any time soon nor produce anything worthwhile.

I believe that an end to all of discussions would be automated tool that does formatting and does not allow any deviation. This however has it's own issues. C++ is a complicated beast and tools are never perfect. Even use of such tool would sometimes result in worse-looking code.

What do you suggest? How do you retroactively apply extensive guidelines on to a large legacy codebase?

-------------------------

Modanung | 2020-10-31 13:52:57 UTC | #39

[quote="rku, post:38, topic:6449"]
What do you suggest?
[/quote]

That you create an **rbfx** forum.

-------------------------

1vanK | 2020-10-31 13:52:46 UTC | #40

[quote="rku, post:35, topic:6449"]
You abstained from vote. However even if you voted you would have been a minority.
[/quote]

Are you kidding or don't you really understand? The vote was about one document, and the rules contained links to other documents.

-------------------------

1vanK | 2020-10-31 13:54:40 UTC | #41

[quote="Eugene, post:37, topic:6449"]
If you had issues with current items in Urho code standard, you should have risen them when there was discussion and before these items were added and enforced by WeiTjong. You had months to voice your objections. Why didn’t you?
[/quote]

I raised the qustion and am raising it now. The changes to ʻauto` were adopted without a vote.

-------------------------

Eugene | 2020-10-31 13:55:15 UTC | #42

[quote="1vanK, post:40, topic:6449"]
The vote was about one document, and the rules contained links to other documents.
[/quote]
I don’t quite follow wdym (3). Vote was about CppCG. Urho code style is based on CppCG and links it. What “different documents” you mean?

-------------------------

rku | 2020-10-31 13:55:56 UTC | #43

I do not follow. https://discourse.urho3d.io/t/coding-guidelines/3509 thread links https://github.com/isocpp/CppCoreGuidelines and documentation links to a file within that repository: https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md. Seems to me like there was no confusion what discussion was about.

-------------------------

Modanung | 2020-10-31 13:57:53 UTC | #44

He even linked to them, because you asked before. :disappointed:

-------------------------

1vanK | 2020-10-31 13:57:31 UTC | #45

https://urho3d.github.io/documentation/HEAD/_coding_conventions.html

More details !!!!!!!!!!!!!!!!!!!!!!! >>>>>>>>>>>>>>>>>>>> [here](https://clang.llvm.org/extra/clang-tidy/checks/modernize-use-auto.html) and [here](https://google.github.io/styleguide/cppguide.html#auto) <<<<<<<<<<<<<<<<<<<!!!!!!!!!!!!!!!!!!!!!!!!!!!.

-------------------------

rku | 2020-10-31 14:00:31 UTC | #46

Seems to me like those links were meant as an extra context.

-------------------------

Modanung | 2020-10-31 14:03:41 UTC | #47

To cast the net of clarity more widely? [spoiler]:goal_net:[/spoiler]

May the labyrinth guide us.

-------------------------

1vanK | 2020-10-31 14:03:19 UTC | #48

[quote="rku, post:46, topic:6449, full:true"]
Seems to me like those links were meant as an extra context.
[/quote]

Does this mean that I can add other links with some other context?

-------------------------

rku | 2020-10-31 14:04:48 UTC | #49

If they improve quality of documentation - by all means.

I do not understand purpose of this question.

-------------------------

Modanung | 2020-10-31 14:05:32 UTC | #50

The worst part about this thread is that @rku and @Eugene are probably not even trolling.

-------------------------

1vanK | 2020-10-31 14:05:54 UTC | #51

[quote="rku, post:49, topic:6449, full:true"]
If they improve quality of documentation - by all means.

I do not understand purpose of this question.
[/quote]

Is it possible to add links that will improve the document as I see it?

-------------------------

rku | 2020-10-31 14:07:49 UTC | #52

You perfectly know the answer... What would happen if everyone who comes by changes things the way they see fit? What if i submitted a PR removing `_` suffix from class fields? Everyone would laugh at such PR, and rightly so.

-------------------------

Modanung | 2020-10-31 14:10:45 UTC | #53

Please stick to the *topic*. :warning:

Feel free to create a separate one.

-------------------------

1vanK | 2020-10-31 14:08:41 UTC | #54

[quote="rku, post:52, topic:6449, full:true"]
You perfectly know the answer… What would happen if everyone who comes by changes things the way they see fit? What if i submitted a PR removing `_` suffix from class fields? Everyone would laugh at such PR, and rightly so.
[/quote]

Then why did someone decide to improve the document without voting?

-------------------------

rku | 2020-10-31 14:09:29 UTC | #55

Thread with poll: https://discourse.urho3d.io/t/coding-guidelines/3509

-------------------------

1vanK | 2020-10-31 14:10:52 UTC | #56

Okay, I'll ask another question. Do you understand that the vote was for one document, and there are three documents in the rules?

-------------------------

rku | 2020-10-31 14:12:51 UTC | #57

As i understand documentation does not claim that all three documents should be followed. I do not understand what is the issue at all to be honest. If you do not like those other too links - ok. Follow cpp core guidelines only, where applicable.

-------------------------

1vanK | 2020-10-31 14:14:12 UTC | #58

there is problem https://github.com/urho3d/Urho3D/pull/2712

-------------------------

rku | 2020-10-31 14:15:02 UTC | #59

Do cpp core guidelines claim different rules regarding `auto` compared to other two links?

-------------------------

1vanK | 2020-10-31 14:18:20 UTC | #60

I don’t know, it’s too big to read it. Nobody read it, people just voted. I want to know what is written ʻauto` in this document. Good luck with that. (a little hint, most likely these rules are not there)

-------------------------

Eugene | 2020-10-31 14:22:38 UTC | #61

Sorry, I didn’t realize that you consider clang tidy docs as separate documents. You are right, tho. CppCG is not directly affiliated with Clang.

However, clang tidy was the only realistic option to enforce CppCG at least in some degree. Clang tools don’t contradict CppCG, they implement it. 

We decided that CppCG is a good thing, and clang tidy was the execution of this decision.

-------------------------

1vanK | 2020-10-31 14:23:25 UTC | #62

But we didn't decide.

-------------------------

1vanK | 2020-10-31 14:25:19 UTC | #64



-------------------------

1vanK | 2020-10-31 14:28:00 UTC | #65

These are not just different documents. These are different rules. If people who don't even commit to the engine vote for the document and we have to live with it, then let's at least refer to this document.

-------------------------

Eugene | 2020-10-31 15:11:27 UTC | #66

You are right, there were no votes about individual rules of clang tidy. They were just applied later, mostly at WeiTjong discretion. Apparently no one bothered to create additional polls.

It doesn’t really matter in scope of this specific discussion, tho. We have this code standard and this CI now.

If you want to change something in code standard, that’s fine for me. Let’s make a formal proposal of change and discuss it.

-------------------------

1vanK | 2020-10-31 15:09:57 UTC | #67

No problem: using `auto` only for variables with length > 10 and contains symbols :: and < > at the same time

-------------------------

weitjong | 2020-10-31 15:24:49 UTC | #68

If I may add it here. I have used the settings from CLion to configure the clang-tidy. My work at that time was in the branch for review before it get merged. It did not go through a "formal discussion" because I am sick of the academic (formal) discussions already, and in the end they all just end up as talks and no action. If the auto or not to auto alone already this difficult, why do you think you can get everyone agree on all aspects of the new C++11 standard.

Arguably Lasse should be right person to make the new "rules" for the new C++ standard, but he has left the project at the time we migrated to C++11. The original code convention was his and everyone just followed. Personally I did not start my function/method name with an initial capital, for instance. But when contribution in Urho, I just follow the rule. For the C++11 standard, we have to start somewhere by ourselves. The clang-tidy is one of my action and concrete contribution to the project. The rules/checks are configurable. So, please do configure them to your liking if by chance you all can come to an agreement this time.

-------------------------

1vanK | 2020-10-31 15:32:13 UTC | #69

It is hardly possible to come to an agreement in the current situation. It's even unclear whose opinion should be taken into account when discussing. Should we, for example, take into account the opinion of people who do not participate in the development of the engine or, even worse, left to rival project. Perhaps they would like the opposite, so that it would be impossible to come to some kind of agreement.

-------------------------

1vanK | 2020-10-31 15:49:22 UTC | #71

I don’t want to explain the words I didn’t say.

-------------------------

Eugene | 2020-10-31 17:22:22 UTC | #72

Okay, just to clarify my position. I don’t care how you decide to use/not to use auto, but please keep these three things consistent with each other: (1) PRs, (2) CI and (3) code style document.

-------------------------

