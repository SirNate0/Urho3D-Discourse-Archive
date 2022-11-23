ksmit799 | 2020-03-01 13:02:36 UTC | #1

Hey everyone,

I'm wondering what's the best way to programmatically create an empty JSON object (file), populate it with some data and then save it to the file system. An abridged version of what I'm trying to do is below, however, when saving the file it only contains the text 'null' and nothing else. Any help would be appreciated.

    // Creating the *new* JSON file.
    settings_ = context_->CreateObject<JSONFile>();
    // The root object seems to be the issue?
    // It appears as if it is null unless you load an existing JSON file.
    JSONValue root = settings_->GetRoot();
    // Create some dummy data.
    root.Set("test", "it works");
    // Save the new JSON file.
    settings_->SaveFile(path);

Expected file contents:
{ "test": "it works"}

Actual file contents:
null

-------------------------

Modanung | 2020-03-03 08:15:34 UTC | #2

Try:
```
JSONValue root{};
root.Set("test", "it works");

settings_ = context_->CreateObject<JSONFile>();
settings_->GetRoot() = root;
settings_->SaveFile(path);
```
And welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

ksmit799 | 2020-03-03 08:21:03 UTC | #3

Thanks for the help and welcome! I was able to get it saving properly using the snippet you provided.

-------------------------

