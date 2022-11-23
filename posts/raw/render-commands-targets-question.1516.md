Bananaft | 2017-06-21 16:46:29 UTC | #1

So, as I understand, I can't read from and write to same rendertarget. So when Quad command has blend="replace" (default), it reads viewport, but writes to some other place, and then swaps it. Am I right?

So I have this command, and it does not work as it should:
[code]
    <command type="quad" tag="Sky" vs="Sky" ps="Sky" psdefines="HWDEPTH" depthstencil="depth">
      <texture unit="diffuse" name="viewport" />
      <texture unit="albedo" name="albedo" />
      <texture unit="normal" name="normal" />
      <texture unit="depth" name="depth" />
    </command>
[/code]

If I remove  <texture unit="albedo" name="albedo" />, it works fine, but adding it back seems like forcing command to read albedo instead of viewport.

So there is no way to read all 4 targets, because one of them need to be locked for writing? Does it mean I'm loosing albedo after first blend="replace" command?

-------------------------

thatonejonguy | 2017-06-21 16:46:10 UTC | #2

Hi, Texture unit "Diffuse" and "Albedo" are actually the same value. switching your viewport or albedo to a different TU should resolve it.

Hope that helps,
-Jon

-------------------------

cadaver | 2017-01-02 01:08:14 UTC | #3

The "viewport" input/output is automatically pingponged to 2 different textures, so when you are writing and reading it at the same time, you're actually reading the previous command's content.

For anything else (manually defined rendertargets) there's no auto-pingpong.

-------------------------

Bananaft | 2017-01-02 01:08:14 UTC | #4

[quote="thatonejonguy"]Hi, Texture unit "Diffuse" and "Albedo" are actually the same value. switching your viewport or albedo to a different TU should resolve it.
[/quote]

It works! Thank you very much!

[quote="cadaver"]The "viewport" input/output is automatically pingponged to 2 different textures, so when you are writing and reading it at the same time, you're actually reading the previous command's content.

For anything else (manually defined rendertargets) there's no auto-pingpong.[/quote]

Will keep that in mind, thanks for noticing.

-------------------------

