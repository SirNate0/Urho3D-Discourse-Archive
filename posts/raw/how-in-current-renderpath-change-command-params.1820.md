codingmonkey | 2017-01-02 01:10:27 UTC | #1

I have this script (*.as)

[code]void AddMRT1OutputInPostopaquePass() 
{
    for (int i=0; i<procSkyRenderPath.numCommands; i++) 
    {
        if (renderPath.commands[i].pass == "postopaque")
        {
            renderPath.commands[i].SetOutput(0, "Viewport");
            renderPath.commands[i].SetOutput(1, "SunHalo");
        }   
    }    
}[/code]

and it no work, tells something about missed proc signature

-------------------------

1vanK | 2017-01-02 01:10:27 UTC | #2

Why cycle over procSkyRenderPath, but you modify renderPath?

-------------------------

codingmonkey | 2017-01-02 01:10:27 UTC | #3

Yes, i forgot change name for cycle var
for a while I try to hardcode needed commands into Forward.xml file )

-------------------------

cadaver | 2017-01-02 01:10:28 UTC | #4

The renderpath commands are value types, so they're exposed a bit poorly; changing parameters in-line likely doesn't have effect. Copy the command to a local variable, change it, then set it back to the renderpath.

-------------------------

codingmonkey | 2017-01-02 01:10:28 UTC | #5

Thanks for reply. I'm also thinking about this behavior of cmd variables. 
For a while I'm use manual create RenderPath.xml file, but soon i want to return to this.

-------------------------

