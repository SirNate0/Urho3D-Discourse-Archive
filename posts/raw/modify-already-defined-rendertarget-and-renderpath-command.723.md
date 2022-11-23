ucupumar | 2017-01-02 01:02:25 UTC | #1

Happy new year to you all Urho people!  :mrgreen: 

I want to modify already defined rendertarget and renderpath on my application, but I can't seems to get them on my renderpath object. 
Urho only provide GetNumCommands() and GetNumRenderTargets() on RenderPath class.
Can I actually do it?  :question:

-------------------------

cadaver | 2017-01-02 01:02:28 UTC | #2

Which language are you using?

-------------------------

ucupumar | 2017-01-02 01:02:28 UTC | #3

I use C++, but if it's can be done with scripting too, please let me know.  :unamused:

-------------------------

cadaver | 2017-01-02 01:02:28 UTC | #4

In C++ you can modify the RenderPath's public commands_ and renderTargets_ vectors. In AngelScript this corresponds to the "commands" and "rendertargets" arrays. Lua currently provides functions to set new commands, but you can't "get" an existing command.

-------------------------

ucupumar | 2017-01-02 01:02:32 UTC | #5

Sorry for late response. I just tested it, and it works like magic! Thaaanks!  :mrgreen: 
One more question, is there more easy way to check if certain command is enable or not? For now I can only think the solution is iterating through RenderPath->commands_ and checks command.tag_ 
Is that the only way?

-------------------------

cadaver | 2017-01-02 01:02:34 UTC | #6

Yes, the best way is to index or iterate the commands, because we cannot guarantee a single correct answer for the enabled state of a tag (in case user modifies enabled state of commands manually, outside the tag system.)

-------------------------

ucupumar | 2017-01-02 01:02:34 UTC | #7

Oh, I see. Thanks for the answer!  :mrgreen:

-------------------------

