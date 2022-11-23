lucasvinbr | 2022-08-01 00:24:30 UTC | #1

Hi, I've been putting together a hook based on TozeroBraneStudioHook.lua for providing some extra autocompletion for (1.8) Urho stuff when using sumneko's vscode lua plugin (https://github.com/sumneko/vscode-lua).

Currently, it kind of works and has some nice stuff, like getting types in getResource and createComponent calls:
![Code_2022-07-31_20-57-52|690x122](upload://etnuvrHXDv3s0VJgLyHsxKYdWf0.png)

The hook's code is a mess hahah, but it runs the same way as the Tozerobrane hook (instructions are in the file), and should generate a .lua file that should be added as a library via the lua plugin.
Here's the link for the hook:
https://gist.github.com/lucasvinbr/d35507785b927f70f71e51936fd93621

-------------------------

