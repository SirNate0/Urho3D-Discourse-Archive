Miegamicis | 2020-04-02 14:29:23 UTC | #1

The last major release was 1.7 back in 2017. Till then we had 2 other releases 1.7.1 (which was simply a bugfix to 1.7) and 1.8-ALPHA which as the name suggests is not a proper public release.

Our homepage shows 1.7.1 as the last stable release, which is very outdated and is missing a lot of new functionality and bugfixes, but since it's there, a lot of people decide to use the 1.7.1 instead of the 1.8-ALPHA or maybe using the code directly from the master branch.

What are your thoughts about releasing a proper 1.8 version? Of course that wouldn't mean that we will or have to do it right away, but we need to look at the opened PR's, completed PR's and get a list of critical bugs that should be fixed before the release.

See the list of opened [PR's](https://github.com/urho3d/Urho3D/pulls)
Registered [issues](https://github.com/urho3d/Urho3D/issues)

And maybe there's other improvements that hasn't been submitted yet or maybe even additional bugs that hasn't been registered.

Let me know what you think have to be in the next release, just so we have some sort of task list to begin with. Will update this thread with all of the suggestions.

-------------------------

tvault | 2020-04-02 17:25:10 UTC | #2

I think it's a great idea, i've recently built 1.8-ALPHA for Raspberry Pi 4, no hassle building and most of the examples run great. I'm planning on working on a 90's style FPS game using 1.8 and I'm looking forward to finding out what I can do with Urho3D.

-------------------------

1vanK | 2020-04-03 15:15:48 UTC | #3

I have some progress with AS autobindings, but I can not send PR because I use c++11 iterators from https://github.com/urho3d/Urho3D/pull/2610

-------------------------

Eugene | 2020-04-04 11:47:15 UTC | #4

I think it's good to go when first version of Web shell is merged and maybe some trivial PRs too.
I see no point in waiting longer.

-------------------------

rku | 2020-04-04 12:30:29 UTC | #5

Didnt Urho3D switch to C++11?

-------------------------

Miegamicis | 2020-04-04 13:57:23 UTC | #6

We also have HTTPS one finished. But I would like to see lua fixed before the release, atm seems like its broken in android builds

-------------------------

1vanK | 2020-04-04 14:51:26 UTC | #7

The old version pugi::xml did not support C ++ 11 iterators

old:
```
            xml_node sectiondef = compounddef.child("sectiondef");
            for (; sectiondef; sectiondef = sectiondef.next_sibling("sectiondef"))
            {
                xml_node memberdef = sectiondef.child("memberdef");
                for (; memberdef; memberdef = memberdef.next_sibling("memberdef"))
                {
                    string id = memberdef.attribute("id").value();
                    _memberdefs.insert({ id, memberdef });
                }
            }
```

new:
```
        for (xml_node compound : doxygenindex.children("compound"))
        {
            for (xml_node member : compound.children("member"))
            {
                string kind = member.attribute("kind").value();

                if (kind == "define")
                {
                    string name = member.child("name").child_value();
                    SourceData::_defines.push_back(name);
                }
            }
        }

```

-------------------------

Modanung | 2020-04-04 21:59:10 UTC | #8

I'd say focus only on bug-fixing and ship it... 1.7 has been up there for too long. The new web shell *is* nice, but I'd rather see it well-tested and included with 1.9. The same goes for the updating of dependecies like Box2D and Bullet. HEAD/1.8 contains enough changes in comparison to 1.7 and it's no use leaving the _alpha_ dangling until _it_ is outdated.
Automatic script binding - although useful to end-users - should primarily be considered a tool for smoothing engine development, and therefor be of little importance within the scope of release candidacy.

Welcome to the forums, @tvault! :confetti_ball: :slightly_smiling_face:

-------------------------

