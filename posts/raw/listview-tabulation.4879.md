sandsound | 2019-01-30 07:46:28 UTC | #1

The code (c++) below is what I'm using to generate a inventory listview.
Is there a better way to make indentation in a listview?


    /// loop through inventory items and add to listview if there is one or more
    for (int i=0; i < item_count; i++)
    {
        if (item_num[i] > 0)
        {
            auto* text = new Text(context_);
            text->SetStyleAuto();

            /// get string lenght and add spaces to make all equal length
            int str_length = strlen(item_name[i]);
            std::stringstream ss;
            ss << item_name[i];
            for (int i=0; i < (18 - str_length); i++)
            {
                ss << " ";
            }
            /// add item amount last
            ss << item_num[i];

            text->SetText(ToString(ss.str().c_str()));
            text->SetName(ToString(item_name[i]));
            list_name->AddItem(text);
        }
    }

btw. it looks like this:

![listview_test|644x500](upload://7vATNgCFOE1o8MdgX4UtGppbwGE.jpeg)

-------------------------

Miegamicis | 2019-01-29 13:20:18 UTC | #2

Use LM_HORIZONTAL layout to the parent view.

```
SharedPtr<UIElement> lineContainer(new UIElement(context_));
lineContainer->SetLayout(LM_HORIZONTAL, 20); // 20 pixel spacing between items in the lineContainer

// Add multiple Text elements to the lineContainer
auto* text1 = new Text(context_);
text1->SetStyleAuto();
text1->SetFixedWidth(100);
lineContainer->AddChild(text1);

auto* text2 = new Text(context_);
text2->SetStyleAuto();
text2->SetFixedWidth(100);
lineContainer->AddChild(text2);

list_name->AddItem(lineContainer);
```

Let me know if this helps.

-------------------------

sandsound | 2019-01-29 14:12:38 UTC | #3

[quote="Miegamicis, post:2, topic:4879"]
Use LM_HORIZONTAL layout to the parent view.
[/quote]

I must be doing it wrong, cause I can't make this work inside the listview.

edit: perhaps my problem is not describing the problem right.
what I want is to have a listview-format something like this:

    shortname          amount    value
    amuchlongername    amount    value

edit2: Yes... I'm an idiot :slight_smile:
what I meant to write was tabulation (as you might have guessed, English is not my native tounge)

-------------------------

