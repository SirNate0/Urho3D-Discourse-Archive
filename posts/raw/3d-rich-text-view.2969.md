Pencheff | 2017-03-29 16:10:32 UTC | #1

Just finished porting my rich-text view to Urho3D.

https://youtu.be/IElD7Ob9CyE

The view renders very similar to the Text3D component, however its structured as a list of subwidgets that can render a specific type - image, text, video, custom.

-------------------------

johnnycable | 2017-03-29 20:32:29 UTC | #2

Interesting. It adds a lot to the UI. Nice effects!

-------------------------

Pencheff | 2017-03-29 21:08:10 UTC | #3

I will probably share the code when I get it done and clean. I've tried keeping it clean but its a port from another project and there are leftovers from there.

-------------------------

Victor | 2017-03-29 22:55:21 UTC | #4

Wow, this is really amazing! It would be cool to see something like this as part of standard Urho3D :)

-------------------------

johnnycable | 2017-03-30 08:29:35 UTC | #5

Yes indeed, rich text is very useful, for instance in chats...

-------------------------

yushli1 | 2017-03-30 09:29:27 UTC | #6

Like to see it integrated into the main branch

-------------------------

Modanung | 2017-03-30 10:20:49 UTC | #7

Looks very good.
Don't hesitate to share your non-perfect code. An enthused passerby might feel like polishing it, save you some time, do so in a jiffy with helpful remarks.

-------------------------

Pencheff | 2017-03-31 11:38:41 UTC | #8

Almost done cleaning up the code and adding more features (line/character spacing). The rich-text view now supports different fonts. In my previous project it was able to load system fonts on Windows and Linux recognizing bold-italic fonts too...I'm not sure how this works with this project license. I'm planning more features like typewriting/morphing effect. I'm not sure if this code should go into the main branch, I consider it more like an utility project but lets see how it goes :slight_smile: I would definitely appreciate some help, so I'll make it public asap

-------------------------

Pencheff | 2017-05-12 13:30:18 UTC | #9

I was busy lately but I found some spare time to rework this. Properties needs to be exposed and the HTML parser has to be rewritten from scratch
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/2e36cae11bd36515078f2ad24f675c48d96ba559.png" width="690" height="350">

-------------------------

johnnycable | 2017-05-12 13:41:06 UTC | #10

I'm eager to try it! But where's the link?

-------------------------

Pencheff | 2017-05-12 13:44:24 UTC | #11

Sorry no link yet, just announcing my progress, I'll commit in my repo very soon

-------------------------

Pencheff | 2017-05-13 10:06:36 UTC | #12

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/7f6c5359d270ff9e519cc7d2fa313eb58a1326ee.jpg" width="690" height="352">

-------------------------

slapin | 2017-05-13 12:01:03 UTC | #13

Offtopic question - how many bones do you have on female model on your screenshot?

-------------------------

Pencheff | 2017-05-13 14:43:41 UTC | #14

Can't tell exactly, you can find it in Urho3D/Data/Models/Kachujin/

-------------------------

Pencheff | 2017-05-16 09:36:59 UTC | #15

I've finished the markup parsing yesturday, here's the result:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/8e516a71822d3d9fab44b3d87c36305c05afd9a1.jpg" width="690" height="352">

[code]
Supported tags:
  <br> - line break
  <b></b> - bold
  <i></i> - italic
  <color=#FF800000></color> - change text color, supports 24/32 bit hex and color names
  <size=14></size> - change text size in pixels
  <font=Fonts/Annonymous Pro.ttf></font> - change text font
  <img src=image.png width=320 height=240 /> - embed an image
[/code]

The markup parser supports nesting, the text on above screenshot has this source:
[code]
<color=blue><color=red>red<br><color=green>green</color><br>red1</color><br>blue1<br>blue2</color><color=orange>orange</color><size=10>size=10</size><br><img src=Textures/Logo.png width=120 height=50 />123
[/code]

I only need to fix the coding style to match the Urho3D conventions and I'll PR this

-------------------------

johnnycable | 2017-05-16 10:58:25 UTC | #16

Good. I see it good-looking in a ghost-in-the-shell like environment, filling out all that living wall with giant ads, you know...

-------------------------

Pencheff | 2017-05-16 11:29:25 UTC | #17

...or scrolling RSS feed on the bottom of the screen with something important ;)

-------------------------

yushli1 | 2017-05-16 11:50:05 UTC | #18

That is a good feature. Hope to see it in the main branch soon.

-------------------------

Pencheff | 2017-05-16 15:41:39 UTC | #19

https://github.com/PredatorMF/Urho3D/tree/rich-text

First commit separated from my code, expect some minor flaws and bugs, the code needs more cleanup.

-------------------------

Dave82 | 2017-05-16 22:47:47 UTC | #20

Looks absolutely great ! Are there any plans for a 2d version too ?

-------------------------

Pencheff | 2017-05-17 03:35:30 UTC | #21

Yes 2d version should be easy....subclassing UIElement instead of Drawable.

-------------------------

godan | 2017-05-17 11:52:34 UTC | #22

This is so good! Thanks for putting it together - it solves a problem that I have with my project :slight_smile:

+1 for 2D version!

-------------------------

Pencheff | 2017-05-24 09:37:54 UTC | #23

So I just finished cleaning up, changed coding style to the rest of the code, cleaned up most of the bugs, here's the result:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/59604c4beae192e83c78cbed25bcb99d991de57c.jpg" width="690" height="351">

Edit:
Pushed to my repo, I would like some feedback :)

-------------------------

johnnycable | 2017-05-24 12:46:33 UTC | #24

I'm downloading, gonna try it soon

-------------------------

slapin | 2017-05-24 21:40:55 UTC | #25

Could you please send PR to main Urho?

-------------------------

Pencheff | 2017-05-25 09:20:04 UTC | #26

I could but there are some features that concern me, like these:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/4367ff9614efe5eefb5d2d26348b43a1bfb47c9e.png" width="690" height="395">
These 3 components are not usable directly but are present in the component list.

Also, there is no script interface yet. Maybe @cadaver could advice here.

-------------------------

johnnycable | 2017-05-25 13:11:17 UTC | #27

I'm not able to run the editor. I get these errors: 

[Thu May 25 15:08:12 2017] INFO: Initialized renderer
[Thu May 25 15:08:12 2017] ERROR: Could not initialize audio output
[Thu May 25 15:08:12 2017] INFO: Initialized engine
[Thu May 25 15:08:12 2017] DEBUG: Loading resource Scripts/Editor.as
[Thu May 25 15:08:12 2017] INFO: Scripts/Editor/EditorActions.as:727,5 Compiling void CreateUIElementAction::Redo()
[Thu May 25 15:08:12 2017] ERROR: Scripts/Editor/EditorActions.as:735,17 Expression must be of boolean type
[Thu May 25 15:08:12 2017] INFO: Scripts/Editor/EditorActions.as:768,5 Compiling void DeleteUIElementAction::Undo()
[Thu May 25 15:08:12 2017] ERROR: Scripts/Editor/EditorActions.as:776,17 Expression must be of boolean type
[Thu May 25 15:08:12 2017] INFO: Scripts/Editor/EditorActions.as:898,5 Compiling void ApplyUIElementStyleAction::ApplyStyle(const String&in)
[Thu May 25 15:08:12 2017] ERROR: Scripts/Editor/EditorActions.as:911,17 Expression must be of boolean type
[Thu May 25 15:08:12 2017] INFO: Scripts/Editor/EditorScene.as:1125,1 Compiling uint SceneFindChildIndex(Node@, Node@)
[Thu May 25 15:08:12 2017] WARNING: Scripts/Editor/EditorScene.as:1133,12 Implicit conversion changed sign of value
[Thu May 25 15:08:12 2017] INFO: Scripts/Editor/EditorScene.as:1136,1 Compiling uint SceneFindComponentIndex(Node@, Component@)
[Thu May 25 15:08:12 2017] WARNING: Scripts/Editor/EditorScene.as:1144,12 Implicit conversion changed sign of value
[Thu May 25 15:08:12 2017] INFO: Scripts/Editor/EditorUIElement.as:294,1 Compiling void LoadChildUIElement(const String&in)
[Thu May 25 15:08:12 2017] ERROR: Scripts/Editor/EditorUIElement.as:319,9 Expression must be of boolean type
[Thu May 25 15:08:13 2017] INFO: Scripts/Editor/EditorUIElement.as:536,1 Compiling bool UIElementPaste(bool = false)
[Thu May 25 15:08:13 2017] ERROR: Scripts/Editor/EditorUIElement.as:562,13 Expression must be of boolean type
[Thu May 25 15:08:13 2017] ERROR: Failed to compile script module Scripts/Editor.as
[Thu May 25 15:08:15 2017] DEBUG: Quitting SDL

Could anyway be something related to my setup... can you publish a code snippet so I can try from there?

-------------------------

Pencheff | 2017-05-25 14:56:08 UTC | #28

It seems like you are missing a media or running the executable with wrong working directory. However, my code has nothing to do with that, it just registers couple of components in UI.cpp. Compile Urho3D as usual and run the editor, you'll see RichText3D component inside Components -> Geometry.

-------------------------

lezak | 2017-05-25 17:03:40 UTC | #29

[quote="Pencheff, post:26, topic:2969"]
These 3 components are not usable directly but are present in the component list.
[/quote]

You can register their factories without specifying category and they won't appear in editor.

-------------------------

Pencheff | 2017-05-26 11:18:35 UTC | #30

I've just implemented the scripting interfaces although haven't test it yet. Seems ready for a PR

-------------------------

johnnycable | 2017-05-29 12:09:37 UTC | #31

It works!

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/5a52172929d984e0821653507bc414fdbec7cecf.png" width="690" height="318">

Built on Ubuntu 16.04

I noticed you implemented an auto clip property. How does it work? I'm doing a parallax scrolling component, and I have to do exactly the same, but didn't find a quick way for it...

-------------------------

Pencheff | 2017-05-29 12:38:59 UTC | #32

The clipping works like a scissor that clips everything outside the defined clipping region. If you set the auto clipping option to true, you'll have a clip rectangle that equals the content size of the text. If auto clipping is off, you can define a clipping region manually (e.g. size is the rectangle that the text will be clipped in). If no clipping is defined (it is all 0), you'll have no clipping, the text that scrolls out of the clip region will not be scissored.

-------------------------

johnnycable | 2017-05-29 17:28:15 UTC | #33

I see. I mean how did you do in code. My scrolling widget is in 2d for now and I didn't find a suitable method for clipping it like you did...
Meanwhile, I noticed it's missing the icon... here...

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/620b0fbba8b6585271515193b481c0ec630f634d.png" width="414" height="500">

<a class="attachment" href="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/cb0b90ddf127b117281ebe08ce02ddec03c1faa4.csv">RichText3D.csv</a> (1.8 KB)

Looks like this forum doesn't allow svg upload... so you'll have to rename it to svg...

-------------------------

Pencheff | 2017-05-29 18:59:46 UTC | #34

Thanks for the icon.

Clipping is done while building the geometry, have a look at [here](https://github.com/PredatorMF/Urho3D/blob/rich-text/Source/Urho3D/UI/RichBatch.cpp#L77). For every corner of a quad I have this code:
[code]
    float leftClip = (float)clip_region.min_.x_ - vertices.min_.x_;
    if (leftClip > 0.0f) 
    {
        if ((float)clip_region.min_.x_ < vertices.max_.x_) 
        {
            texcoords.min_.x_ += (texcoords.max_.x_ - texcoords.min_.x_) * leftClip / (vertices.max_.x_ - vertices.min_.x_);
            vertices.min_.x_ += leftClip;
        } 
        else
            return false;
    }
[/code]
The code checks if the vertex is outside a clip rectangle. If it is and only part of the quad is visible, then the quad size is reduced and the texture coordinates are modified so it looks like its being clipped. 

In your case, I think it would be fairly simple to do parallax mapping by just scrolling a texture on a billboard. Open a new thread, I'm also curios what suggestions people would give.

-------------------------

Pencheff | 2020-09-02 12:22:38 UTC | #35

Added support for Google Fonts in my code, here's the result:
![image|690x388](upload://2zWhhZhntUnBLpk5HThMgOsmLlu.png)

Basically, just typing in [code]<font face="Open Sans">[/code] loads the font from the web or cache and loads it asynchronously.

-------------------------

Pencheff | 2020-09-09 14:42:35 UTC | #36

I created a repo here:
https://github.com/PredatorMF/Urho3D-RichText3D

It could have some leftovers from my code, like logging macros but basically it depends only on Urho3D code, no STL or external dependencies. I would love if it can go into Urho3D main repo, maybe if one could help implementing it as UI component also. 

I tried to make it as modular as possible, so I (and others) could render custom elements inside text, plug in custom fonts and images. Parsing HTML elements is only done once on init or when the text changes, so it has minimal impact on performance.

-------------------------

JTippetts1 | 2020-09-09 15:46:43 UTC | #37

I notice you have an emphasis on RichText3D as an inheritor of Drawable, but why not also include a RichText UIElement? It seems the UI element would be more generally useful. Or is there one and I just missed it?

-------------------------

Pencheff | 2020-09-09 16:42:33 UTC | #38

In my application it is required to have 3D text that is why I focused on that part.

-------------------------

Modanung | 2020-09-09 18:28:49 UTC | #39

Personally I think it would be nice to have one that reads Markdown and understands stylesheets.

-------------------------

Pencheff | 2020-09-09 18:33:33 UTC | #40

It doesn't seem to be a lot of work to make a RichText UI element using almost identical code from RichText3D.

-------------------------

Modanung | 2020-09-10 15:03:39 UTC | #41

Does your RichText3D component support [dextrosinistral](https://en.wikipedia.org/wiki/Right-to-left) languages, btw?

-------------------------

Pencheff | 2020-09-10 18:27:32 UTC | #42

I don't think it does at this point, it does support ticker scrolling from left-to-right :smiley:

-------------------------

Modanung | 2020-09-10 19:00:29 UTC | #43

I don't like anti-[Semitic](https://en.wikipedia.org/wiki/Semitic_languages) text components. :stuck_out_tongue:

@hassanrahimi had to [write his strings in a character map](https://discourse.urho3d.io/t/use-right-to-left-languages/4546) for them to be displayed correctly. I don't blame him for switching engines... assuming he did, based on his silence since.

-------------------------

Pencheff | 2020-09-10 19:50:58 UTC | #44

I just love how I have to go wikipedia on every post you make :D Its not anti-Semitic, I never in my life had to display RTL text in any text field. That doesn't mean this component cannot work with RTL text, probably couple of touches, like x += glyph.width going the other direction and its good to go.

-------------------------

Modanung | 2020-09-10 20:35:30 UTC | #45

[quote="Pencheff, post:44, topic:2969"]
I never in my life had to display RTL text in any text field.
[/quote]

But did you never wish someone from [this part of the world](https://upload.wikimedia.org/wikipedia/commons/2/24/Arabic_Dialects_ar.svg) played your games? If we consider Arabic to be a single language, it has about twice as much native speakers as Russian.

Despite it currently being somewhat of a low priority title, it sure would make sense for Drone Hunter to be available in Arabic. So some day I'd add the support, but there's quite some things I'll tend to before that.

![Screenshot_Sun_Feb_26_02_24_59_2017|690x388](upload://94yUEGlYG0qRbZVhCwM0QuPDRj3.jpeg)

-------------------------

Pencheff | 2020-09-10 21:21:13 UTC | #46

[quote="Modanung, post:45, topic:2969"]
But did you never wish someone from [this part of the world](https://upload.wikimedia.org/wikipedia/commons/2/24/Arabic_Dialects_ar.svg) played your games?
[/quote]

I don't make games, when I must cover RTL, I will probably implement it.

-------------------------

Modanung | 2020-09-10 21:34:56 UTC | #47

Ok. :slightly_smiling_face:

-------------------------

Modanung | 2020-09-17 11:50:11 UTC | #48

From wikipedia:
> **[Arabic script](https://en.wikipedia.org/wiki/Arabic_script)**
>
> [...] It is the second-most widely used writing system in the world by the number of countries using it and the third by the number of users, after the Latin and Chinese scripts.

-------------------------

Lys0gen | 2020-12-22 00:08:24 UTC | #49

Thanks for creating this @Pencheff!

I have created a [fork](https://github.com/Lys0gen/Urho3D-RichText3D) with a **RichTextUI** element added, which is usable inside the UI system.

**Warning: the code is absolute trash**, I didn't really know what I was doing (still don't, mostly) so I just cobbled together parts of *Urho3D::Text* and your *RichWidget* & *RichText3D* until I had something working.

It lacks a few things that the original Text has (e.g. partial selection) and yours (e.g. the Ticker). Might also have a few bugs, but so far it seems to work fine for my purposes.

Hopefully it is useful for someone else who doesn't want to spend hours to get it working in a proper way :)

-------------------------

Lys0gen | 2021-09-02 14:27:36 UTC | #50

Hello again,
a bit late but I was wondering if anyone has actually tried using the bold & italic tags? Because they don't work.

I've done some light debugging and in fact the *RichFontProvider* doesn't really seem to do much at all. The whole RichFontProvider::RequestFont function just seems to rely on the fact that the given font is already in the cache and doesn't bother looking up bold/italic versions of it.

Changing that is easy, I'm more confused about the whole E_RICHTEXT_FONT_REQUEST and the CompleteRequest(..) function, as they don't seem to be made for each other. CompleteRequest is never called from anywhere, as such any font not already loaded won't show.
Fixing that (CompleteRequest handling the event data instead of... nothing) is also simple.

But sadly this still makes it show up like the baseline font. Beyond this I don't know how the font type handling works.


Does anyone have a solution to this? Or do I need to take font files that are bold/italic by default and switch to those with the <font...> tag when necessary? That would be a huge pain.

-------------------------

Pencheff | 2021-09-02 15:27:46 UTC | #51

You have to handle E_RICHTEXT_FONT_REQUEST in your application, load a font based on the request parameters. There you have a chance to load bold/italic font and use CompleteRequest() when you're done. I didn't post that part of the code, since it's very specific to my application. But it basically does the described above and caches the fonts based on their names, not by file paths, so you can just do [code]<font name="Roboto">[/code]

-------------------------

Lys0gen | 2021-09-02 15:56:58 UTC | #52

Ok, so how do you handle bold/italic fonts (if you do that at all)?

I'm assuming there is no pre existing way to handle that?

So to me the simplest solution seems to be to provide additional font files (e.g. for "Arial.ttf" add "Arial_bold.ttf", "Arial_italic.ttf", "Arial_bold_italic.ttf") and load those internally depending on the flags. Or is there a proper way that avoids adding so many files?

Maybe I just don't know enough about fonts though. I was under the impression that most fonts had bold/italic versions integrated into the base file?

-------------------------

Pencheff | 2021-09-02 16:22:05 UTC | #53

Yes, you map Arial_bold.ttf to bold, Arial_italic.ttf to italic, etc. I ship fonts with my application and I know the names of every font, so I have manifest xml that adds all fonts to the FontDatabase class below:

[code]
class FontDatabase : public Urho3D::Object {
  URHO3D_OBJECT(FontDatabase, Urho3D::Object)
public:
  FontDatabase(Urho3D::Context* context);
  ~FontDatabase() override;

  void PrecacheFont(const Urho3D::String& font_name, bool bold, bool italic, bool force_update);

  void ClearCache();

  Urho3D::StringVector GetCachedFonts() const;
  // Check if font is in database
  bool IsFontInCache(const Urho3D::String& font_name, bool bold, bool italic) const;
  // Get font filename from cache
  Urho3D::String GetFontFilenameFromCache(const Urho3D::String& font_name, bool bold, bool italic) const;
  // Add font alias
  void AddFontAlias(const Urho3D::String& alias, const Urho3D::String& target_font);
  // Remove font alias
  void RemoveFontAlias(const Urho3D::String& alias);
  // Pre-cache aliases
  void PrecacheAliasFonts();
private:
  core::FilePath cache_dir_;

  struct FontRequest {
    Urho3D::String name;
    bool bold {false};
    bool italic {false};
    unsigned request_id {0};
    std::shared_ptr<WebResourceTransfer> transfer;
  };

  std::unordered_map<std::string, std::string> font_aliases_;

  std::vector<FontRequest> font_definition_tranfers_;
  std::vector<FontRequest> font_transfers_;

  void HandleRichTextFontRequest(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
  void HandleUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);

  bool HasTransferFor(const Urho3D::String& font_name, bool bold, bool italic, unsigned id) const;
  void RequestFont(const Urho3D::String& font_name, bool bold, bool italic, unsigned id = 0);
  core::FilePath StoreFontFileInCache(const core::FilePath& file, const Urho3D::String& font_name, bool bold, bool italic);
};
[/code]

Again, implementation has a lot of application specific code, SQLite database that caches fonts  downloaded from Google Fonts, it's up to you.

-------------------------

Lys0gen | 2021-09-02 17:44:13 UTC | #54

Thank you, got it working now.
A bit more cumbersome than I had hoped, but it'll do.

-------------------------

Lys0gen | 2022-05-24 14:10:26 UTC | #55

Hello once again :slight_smile: 

Just wondering, have you implemented the underline or strikethrough tags on your end?

-------------------------

Pencheff | 2022-05-24 16:08:19 UTC | #56

I haven't implemented those yet.

-------------------------

