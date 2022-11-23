Azalrion | 2017-01-02 00:57:35 UTC | #1

So at the moment a text element is simply a font, size, colour and text effect (in essence), which is fairly limited on in game gui's especially for something like a strategy game where you might need to format the text to make sure certain information stands out. We're looking to overhaul the class to provide in-line formatting similar to bbcode and would like to hear any views on the implementation. So far we're looking to support the following tags:

[code]
[color=#FF40FF][/color] - Color of the text.
[b][/b] - Bold formatting.
[i][/i] - Italic formatting.
[size=16][/size] - Font size. (This is one of the ones we're not sure about, depends on supportability when creating batches [row height being the big question] and feedback).
[shadow=#FF40FF][/shadow] - Shadow with shadow colour (replaces TextEffect).
[stroke=#ff40ff][/stroke] - Stroke with stroke colour (replaces TextEffect).
[/code]
This would require a change to batch construction where we would parse the text and when finding a' [' parse up till the next ']' and check if its a supported tag, if it is until the closing tag is reached the defaults set for that text will be over-ridden or alternatively split the printText vector up into subsets which are parsed during the UpdateText phase and batches are based off the parameters in those subsets. 

Since the tags will be effectively ignored and edge cases such as space before and after the tags re-formatted, we believe it should be viable.

If anyone has any suggestions or feedback we'd like to hear them.

-------------------------

cadaver | 2017-01-02 00:57:35 UTC | #2

Looks like a nice idea, and it would actually simplify the Text / Text3D class attributes. Definitely do all the expensive work during UpdateText(), the UIBatch construction phase should just dump out ready-collected information as fast as possible. It will also need being able to turn off the tag parsing completely per Text element so that you can edit such text :wink:

-------------------------

JTippetts | 2017-01-02 00:57:44 UTC | #3

I'm watching this topic with GREAT interest, as currently I'm using a cobbled together nightmare mess for my combat log and item descriptions, which embed color coding.

-------------------------

Azalrion | 2017-01-02 00:57:45 UTC | #4

Hopefully find time to finish it soon (9 hours of coding at work really puts you off turning on the pc at home) about halfway there moved all the functionality over to binding to subsets based on formatting just need to do the parsing.

-------------------------

