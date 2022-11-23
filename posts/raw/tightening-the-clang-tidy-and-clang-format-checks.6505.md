weitjong | 2020-11-07 11:13:09 UTC | #1

I need more eye balls to verify the automated bulk update results on my current active dev branch. 

https://github.com/urho3d/Urho3D/commit/31b04df4ee99d866ced653f03fdfb1704896af7f

This is only the initial bulk update. More will come until everything snaps into place; or not if I failed, and these two jobs that use clang-tidy and clang-format will be removed.

This initial bulk update was from `clang-format` command only. Let me know if you see anything **that is not acceptable for the Urho3D project**. Just to be clear, I am not asking for your personal setting.

-------------------------

1vanK | 2020-11-08 09:10:38 UTC | #2

```
camera->SetZoom(1.2f * Min((float)graphics->GetWidth() / 1280.0f,
                               (float)graphics->GetHeight() /
                                   800.0f)); // Set zoom according to user's resolution to ensure full visibility
                                             // (initial zoom (1.2) is set for full visibility at 1280x800 resolution)
```

-------------------------

weitjong | 2020-11-07 11:20:00 UTC | #3

When the long parameters line is wrapped then it will "align" the next line. There is also option to "not align". I am OK with both. Currently it is "align" I think. Is that what you objecting?

For future, please also provide the name of the file for easy lookup.

-------------------------

1vanK | 2020-11-08 09:10:53 UTC | #4

DynamicGeometry::CreateScene()

corrupted table float vertexData[]

https://github.com/urho3d/Urho3D/blob/31b04df4ee99d866ced653f03fdfb1704896af7f/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp#L168

-------------------------

1vanK | 2020-11-07 11:24:19 UTC | #5

```
void L10n::HandleChangeLanguage(StringHash eventType, VariantMap& eventData)
```

```
windowTitle->SetText(l10n->Get("title") + " (" + String(l10n->GetLanguageIndex()) + " " + l10n->GetLanguage() +
                         ")");
```
[Source/Samples/40_Localization/L10n.cpp](https://github.com/urho3d/Urho3D/commit/31b04df4ee99d866ced653f03fdfb1704896af7f#diff-33a7e688b37cf292d822b8bcae4bd8b8e633898883ba4044dcb5cf555930e95d)

-------------------------

weitjong | 2020-11-07 11:26:11 UTC | #6

This is the same issue. It will wrap when the column limit 120 is hit. The number is configurable. Can set to 0 for don't wrap. I think it was 80 originally and I changed it to 120. But this wrapping can happen on any number we choose. Unless, if we set it to 0.

-------------------------

1vanK | 2020-11-07 11:26:45 UTC | #7

[Source/Samples/47_Typography/Typography.cpp](https://github.com/urho3d/Urho3D/commit/31b04df4ee99d866ced653f03fdfb1704896af7f#diff-5726427136f4dd1150ead228a04a8c63eda1ba0cae0b3bb8e6116c3f399ebf88)

corrupted tables `const char* levels[]` `thresholds[]` `limits[]`

-------------------------

1vanK | 2020-11-07 11:28:57 UTC | #8

void Urho2DStretchableSprite::ScaleSprites(float timeStep)

```
        const auto scale = Vector2{1.0f + (right  ? quantum
                                           : left ? -quantum
                                                  : 0.0f),
                                   1.0f + (up     ? quantum
                                           : down ? -quantum
                                                  : 0.0f)};
```

-------------------------

1vanK | 2020-11-07 11:30:44 UTC | #9

[Source/Urho3D/LibraryInfo.cpp](https://github.com/urho3d/Urho3D/commit/31b04df4ee99d866ced653f03fdfb1704896af7f#diff-d1544dbfefffc11d6bb686587c20e8d8373757aa4e7c3accf4f0577e042bd7f8)

wrong indents in GetCompilerDefines()

-------------------------

weitjong | 2020-11-07 11:31:38 UTC | #10

what wrong about this wrapping? It is kind of nice :slight_smile: If you want may be I could retry without alignment too.

-------------------------

1vanK | 2020-11-07 11:32:23 UTC | #11

Everywhere, line fragments start with the same indentation, but here it is different

-------------------------

Eugene | 2020-11-07 13:30:54 UTC | #12

So far the only thing that looks weird and foreign for me is non-multiple-of-4 indentation.
As far as I remember, Urho have never (or almost never) used this kind of formatting in its codebase.
![image|690x68](upload://3Wv7b6RJcuhTpTnL30LRuwxWAhN.png) 

In this particular example it looks good, but in general it tends to waste horizontal line space.
It's also more annoying to format manually, which may or may not be an issue depending on the editor used by specific person.

Offtopic: I'm forced to use this style of formatting when I'm working with Python code. I don't know if I like it or not.

TL;DR: I think that multiple-of-4-indentation is more in line with current Urho formatting, and I also personally prefer it due to reasons stated above.

-------------------------

weitjong | 2020-11-07 11:34:40 UTC | #13

Yes, that the same issue 1vanK is highlighting. It wraps with alignment taking consideration where the previous parameter starts.

-------------------------

weitjong | 2020-11-07 11:35:55 UTC | #14

OK. Let stop here first. Let me see if I could reconfigure the wrapping setting.

About the column limit, 120 is OK with you guys?

-------------------------

1vanK | 2020-11-07 11:37:06 UTC | #15

I would do with no limit at all

-------------------------

weitjong | 2020-11-07 11:40:09 UTC | #16

I am contemplating with that option too. I have LG ultra wide screen monitor, so personally I don't have any issue with that. Anyway, I don't think we have too many places with extra long lines, so it should be fine.

-------------------------

Eugene | 2020-11-07 11:42:11 UTC | #17

[quote="weitjong, post:14, topic:6505"]
About the column limit, 120 is OK with you guys?
[/quote]
++ for 120 column limit, we use the same setting on my dayjob. It really helps at diffs review. Although if you really want to keep it as is... well, no limit worked fine for 15 years.
++ for constructor initializer list refactoring
++ for uniform spacing all over the code

Unsure about alignment, I would prefer to keep 1-tab alignment.
I didn't read whole commit, so maybe I didn't notice other changes.

-------------------------

weitjong | 2020-11-07 11:44:12 UTC | #18

Yes, I agree the column limit is good for diffs review, and also for browsing the code through GitHub web interface.

-------------------------

1vanK | 2020-11-07 11:48:20 UTC | #19

The limit of 120 is large. Lines that exceed this limit do so for some reason. Do you really want to interfere with this? If you really want to set a high limit, then don't set a limit at all.

-------------------------

Eugene | 2020-11-07 12:31:52 UTC | #20

120 symbols is not “huge” limit, it is exactly how much fits on Full HD monitor in Beyond Compare for 2-way diff. 120 symbols is also how much code fits on average laptop display with IDE side bar. 

120 or 130 symbols is often used as middle ground between unlimited lines and 80-char limit from DOS epoch

80 is too little, especially if you want to apply it to legacy codebase that was written without this limit in mind.

No limit works okay as long as people writing code stay reasonable and keep their lines generally short.

-------------------------

1vanK | 2020-11-07 12:47:50 UTC | #21

okay, another question, now we have a lot of generated code, should I now complicate the generator, calculate the length of each line (currently I just write to stream directly), etc. or will clan-tidy constantly struggle with the generator?

-------------------------

Eugene | 2020-11-07 12:55:08 UTC | #22

I'm 99% certain that generated code should be extempt from auto formatting in any form as it is not supposed to be read or edited by a person.

I just did a bit of math. 97% of `Source/Urho3D/` is already under 120 char limit. 98% is under 130.
It's gonna be about 4-6k lines of code changed due to enforcing line limit. It's a lot, but it's _probably_ okay.

-------------------------

1vanK | 2020-11-07 13:13:11 UTC | #23

Generated code is human readable. But in fact I should integrate own realization clang-format into generator to full match.

-------------------------

1vanK | 2020-11-07 14:15:44 UTC | #24

I suggest to disable formatting for arrays altogether

Source/Urho3D/Graphics/Material.cpp

textureUnitNames[] - array with define

-------------------------

weitjong | 2020-11-07 16:32:50 UTC | #25

Thanks for all your inputs. I will try to fine-tune the setting later. I may or may not be able to find the right switch for each issue. So, just like the clang-tidy, we may not always get exactly what we want. The goal is to find the right mix that could get the acceptable overall result.

For the generated code, Lua bindings are excluded already simply because they are generated on the fly and not in the source tree. The new AS bindings are included though at the moment. However, they could be easily excluded too.

I also plan to have separate workflow that would be triggered by scheduler, something like a nightly batch. In this workflow, I could have one job to do the same bulk update that I was doing manually earlier. This would allow maintainers to still merge a PR even though there are still small formatting errors. Instead of forcing the PR author to rectify, we can let the nightly batch to take care of them automatically. This is all provided we can agree on the acceptable settings.

-------------------------

1vanK | 2020-11-08 07:15:33 UTC | #26

Clang-format moves content of namespaces to first column. Sometime namespace used as "singleton" and moving is not required:
`Source/Tools/BindingGenerator/XmlSourceData.cpp` -> `namespace SourceData`

-------------------------

1vanK | 2020-11-08 07:20:06 UTC | #27

```Source/Urho3D/Graphics/ShaderVariation.cpp```

```
ShaderParameter::ShaderParameter(const String& name, unsigned glType, int location)
    : // NOLINT(hicpp-member-init)
    name_{name}
    , glType_{glType}
    , location_{location}
{

}
```

-------------------------

weitjong | 2020-11-08 09:15:58 UTC | #28

[quote="1vanK, post:9, topic:6505"]
wrong indents in GetCompilerDefines()
[/quote]

The string continuation looks correctly indented to me.

-------------------------

weitjong | 2020-11-08 09:24:09 UTC | #29

The namespace indentation is set to none. This should give similar result as `Urho3D` namespace. The other options is "inner" and "all". The "all" may give you the indent even on the first level, but that would change the code base all over the place including the `Urho3D` namespace.

-------------------------

Eugene | 2020-11-08 13:31:24 UTC | #30

[quote="1vanK, post:26, topic:6505"]
Sometime namespace used as “singleton” and moving is not required:
[/quote]
Maybe don’t use namespaces as singletons then?

If user is okay with non-indented content, they can use namespace.
If user is not okay with it, they can use struct or class.

Indenting all the namespaces is not an option, it would affect 99% of Urho codebase and waste a lot of line space.

Disabling namespace formatting is an option, but I don’t think it’s good idea to surrender automatic formatter for sake of 10 lines somewhere in code.

-------------------------

1vanK | 2020-11-08 13:33:25 UTC | #31

I am withdrawing from this discussion, I don't like this auto-formatting idea at all

-------------------------

1vanK | 2020-11-08 13:36:18 UTC | #32

If a smart auto-formatting system decides for me how my code should look like, where auto should be, and so on, then let the system write this code

-------------------------

Eugene | 2020-11-08 14:25:33 UTC | #33

[quote="1vanK, post:31, topic:6505, full:true"]
I am withdrawing from this discussion, I don’t like this auto-formatting idea at all
[/quote]
It's offtopic, but have you ever tried writing in Python?
They have this whole PEP thing, which is basically clang-format, except it's turned on by default in all modern IDEs and much more strict.
Whole language community is de-facto required to write the code in single style.
Sometimes I wish C++ had something like that.

I like auto formatting as long as it is conforming with the existing codebase (doesn’t cause too much changes), but I can live without it.

-------------------------

weitjong | 2020-11-08 14:52:58 UTC | #34

In that case then I will just stop. Do what you like with the two jobs. I don’t care anymore. I hereby declare I have completed the migration work even though it is not yet finished.

-------------------------

1vanK | 2020-11-08 14:57:00 UTC | #35

[quote="Eugene, post:33, topic:6505"]
It’s offtopic, but have you ever tried writing in Python?
[/quote]

Yes, I have modified the exporter for Blender 2.8. Python is a disgusting language.

-------------------------

1vanK | 2020-11-08 15:11:09 UTC | #36

There is one useful thing - clearing lines that only have spaces.

-------------------------

weitjong | 2020-11-08 15:22:55 UTC | #37

I don't think I can continue if only formatting already caused so much contention. And, I have actually just started and haven't done anything with its big cousin, clang-tidy, yet. So, let's can this first. I have other better things to do too.

-------------------------

rku | 2020-11-09 07:28:21 UTC | #38

For what its worth i think auto-formatting is a good idea. It may not be simple to achieve. It may not be perfect in all edgecases. But if it can be done, it would save a lot of time for contributors and maintainers alike. Personal likes or dislikes of minority should not be stopping progress of a project.

@1vanK that is some rather toxic attitude. Instead of trying to find a middle ground you chose to (╯°□°）╯︵ ┻━┻ instead. This is not something people expect from a moderator.

-------------------------

Modanung | 2020-11-09 08:23:54 UTC | #39

[quote="rku, post:38, topic:6505"]
But if it can be done, it would save a lot of time for contributors and maintainers alike.
[/quote]

In my view, it means less *attention* spent on code, and more on _bla_. It's like having a garbage collector; why are you making a mess?

Also, table flips represent break-throughs, but you'd have to be a dreamer to understand that.

-------------------------

weitjong | 2020-11-09 11:01:09 UTC | #40

The auto formatting can be disabled locally to keep the the original author intent if it is absolutely needed to keep the format verbatim. Like I said, I just barely started. But until we have a true team lead that everyone blindly obey in this matter, I see this kind of discussion is pointless as everyone has personal own taste. So I am closing this thread.

-------------------------

weitjong | 2020-11-09 08:49:17 UTC | #41



-------------------------

1vanK | 2020-11-09 12:39:05 UTC | #42

[quote="rku, post:38, topic:6505"]
@1vanK that is some rather toxic attitude. Instead of trying to find a middle ground you chose to (╯°□°）╯︵ ┻━┻ instead.
[/quote]

Instead of trying to find a middle ground you chose to create a separate fork and split the community.

-------------------------

Modanung | 2020-11-09 17:11:44 UTC | #43

Respect the compulsive proctologist. :fu:

-------------------------

