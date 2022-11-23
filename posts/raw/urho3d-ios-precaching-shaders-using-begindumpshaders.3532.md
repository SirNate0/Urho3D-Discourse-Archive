Andre_B | 2017-09-06 16:53:21 UTC | #1

Hi,

Id like to precompile the shaders im using on an app running on IOS, i've read that i can use the function BeginDumpShaders with a filename, and a EndDumpShaders.

Id like to know where is this file saved, or if its saved at all on a iphone. Im loading a file with the same name from the ios documents folder but so far i have not had any luck with it.

-------------------------

Andre_B | 2017-09-07 09:01:22 UTC | #2

It seems that on iOS it tries to write into the application support folder which is not allowed and crashes the app.
Ill have to manually implement what ShaderCache does in the engine and instead write into the documents folder.

-------------------------

cadaver | 2017-09-07 09:26:02 UTC | #3

ShaderPrecache class should just take the filename given to it verbatim, so you should be able to feed the absolute path you want to Graphics::BeginDumpShaders().

-------------------------

Andre_B | 2017-09-07 09:16:18 UTC | #4

Aparently i was Missing a forward slash when last i tried to use the documents folder, thanks, i can now download the device container and theres a file there named ShaderCache

	Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
	this.Graphics.BeginDumpShaders(documents+ "/" + "ShaderCache");

-------------------------

