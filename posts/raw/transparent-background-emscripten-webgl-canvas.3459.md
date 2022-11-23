eldog | 2017-08-24 16:31:48 UTC | #1

Hi all,

I'd like to have a transparent background using Emscripten/WebGL as I'd like to display a video behind the scene (attempting some AR).

I've tried setting the clear color alpha value using some code I found on the forums, but to no avail. 

I'm doing something like

       // Does *NOT* create a transparent canvas in Emscripten/WebGL
       RenderPath * rp = viewport->GetRenderPath();
       for ( int i = 0; i < rp->GetNumCommands(); i++ )
       {
          RenderPathCommand * cmd = rp->GetCommand( i );
          if ( cmd->type_ == RenderCommandType::CMD_CLEAR )
          {
             cmd->useFogColor_ = false;
             cmd->clearColor_ = Color(1.0f, 1.0f, 1.0f, 0.5f );
          }
       }

Thanks

-------------------------

eldog | 2017-08-24 16:31:36 UTC | #2

OK I got it working by setting `Module.preinitializedWebGLContext` in my html code.

E.g. something like

`Module.preinitializedWebGLContext = canvas.getContext('2d');`

Where `canvas` is the canvas used by the `Module`.

Also edit your `Forward.xml` and ensure your `clear` command has the transparent value you want, e.g.,  `color="0 0 0 0"`.

-------------------------

