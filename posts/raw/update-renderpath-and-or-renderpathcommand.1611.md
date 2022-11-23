ghidra | 2017-01-02 01:08:55 UTC | #1

I've got an example that I am trying to wrap up. The last step is the ability to pick a shader define with a drop down.

The first method that I tried, was to change the pixelShaderDefine on the renderpathcommand. I didnt get any errors, but it didnt have an effect.
It looks as though I can not just set the pixelShaderDefines on the renderpathcommand. I can read it, just not set it, though the docs do not say that it is read only.

The second method, was to rebuild an entire renderpathcommand. Remove the original one, and add the new one. That seems to have an effect, however, I only get a black screen. But I can print out the values, and everything seems fine. Assuming that its the last command of three on the renderpath.
This method. I remove command[2], build a new renderpathcommand ( RenderPathCommand rpc = RenderPathCommand(); ), and fill in the relevant values. and set it ( renderer.viewports[0].renderPath.AddCommand(rpc); ). After removing I can Print I have 2 commands, add it, I can print I have 3.

Is there a command that I need to send to tell it to recompile the shader?

Thanks for any insight into how I might be able to achieve this if its possible.

-------------------------

cadaver | 2017-01-02 01:08:55 UTC | #2

I think you're hitting a stupidity of the AngelScript bindings related to a value type such as the RenderPathCommand, and accessors.

Try making a copy of the renderpathcommand, change the defines on the copy, then set the command back.

-------------------------

ghidra | 2017-01-02 01:08:56 UTC | #3

Yup, that did it. Thanks.

-------------------------

