freegodsoul | 2017-01-02 01:08:12 UTC | #1

Is there a simple method of setting a [b]background color[/b] of a viewport or of a whole scene [b]without[/b] creating Zone object (example 05_AnimatingScene) ?
I want something like Ogre's [b]Viewport::setBackgroundColour()[/b] or Unity's [b]Camera.backgroundColor[/b]. Thanks!

-------------------------

codingmonkey | 2017-01-02 01:08:12 UTC | #2

You may try to change RenderPath clear color value
get RP from viewport and find clear command 
or change xml file forward.xml

-------------------------

freegodsoul | 2017-01-02 01:08:12 UTC | #3

[quote="codingmonkey"]You may try to change RenderPath clear color value
get RP from viewport and find clear command 
or change xml file forward.xml[/quote]

I've put this code right after viewport initialization, and everything works well:

[code]
	RenderPath * rp = viewport->GetRenderPath();
	for ( int i = 0; i < rp->GetNumCommands(); i++ )
	{
		RenderPathCommand * cmd = rp->GetCommand( i );
		if ( cmd->type_ == RenderCommandType::CMD_CLEAR )
		{
			cmd->useFogColor_ = false;
			cmd->clearColor_ = Color( 0.2f, 0.25f, 0.3f, 1.0f );
		}
	}
[/code]

Thank you, [b]CodingMonkey[/b]!

-------------------------

