scorvi | 2017-01-02 00:57:41 UTC | #1

hey,

i am programming a app state manager and have some problems with the loading screen :-/ 

i had something like this in mind 

[code]bool GamePlayState::Begin( )
{
	// Switch in to the loading state.
	Loading * mLoadingState = (Loading*) SpawnChildState( "Loading", true );
	mLoadingState->Render();

	// Create the scene content
	CreateScene();
	mLoadingState->Render();
	// Create the UI content
	CreateInstructions();
	mLoadingState->Render();
	// Setup the viewport for displaying the scene
	SetupViewport();
	mLoadingState->Render();

	mLoadingState->End();
    // Call base class implementation last.
    return AppState::Begin();
}[/code]

i know there is a the  LoadAsyncXML() function to load a scene but  i dont load a xml file .... 

i thought i could do somthing like that 
[code]void Loading::Render()
{
	String text = instructionText->GetText();
	text.Append(".");
	instructionText->SetText(text);

	Graphics* graphics = GetSubsystem<Graphics>();
	if (!graphics->BeginFrame())
		return;

	GetSubsystem<Renderer>()->Render();
	GetSubsystem<UI>()->Render();
	graphics->EndFrame();
}[/code]
manualy rendering the view screen but that does not work :-/

is there a way to do it ? or is there a better way to create a loading screen ?

-------------------------

cadaver | 2017-01-02 00:57:41 UTC | #2

Loading a binary scene asynchronously is done with Scene::LoadAsync().

You have two options:
- Loading scene asynchronously and redrawing the loading screen each frame (+ perhaps updating a progress bar, you can query the async progress from scene) while it's loading
- Render the loading screen at least once before you enter a synchronous scene loading function

In a more complicated C++ application you're free to ditch the provided Application class framework and run the engine frame iteration Engine::RunFrame() just as you wish. You could setup the loading screen with UI elements that fill the entire screen, call Engine::RunFrame() once to update that UI view & render it, then load the scene.

You also get an event (E_ENDRENDERING) each frame when rendering the 3D views + UI is otherwise complete, at which point you can add custom rendering using the Graphics system directly, before it flips the backbuffer visible. But that's more complicated than setting up the loading screen with UI.

-------------------------

carlomaker | 2017-01-02 00:57:41 UTC | #3

I resolved creating a GameHandler as Object that handle a custom event ,
any gamestate is a component that GameHandler  create/ destroy  for a event type, i can post the snipet ..

-------------------------

scorvi | 2017-01-02 00:57:41 UTC | #4

thx,

i will test the second option.
 
@ carlomaker : i would really like to see your source snipets  :slight_smile:

-------------------------

carlomaker | 2017-01-02 00:57:43 UTC | #5

ok i created a mini  [url=http://urho3d.prophpbb.com/topic43.html]wiki[/url]  about.

-------------------------

scorvi | 2017-01-02 00:57:48 UTC | #6

ok thx

for now i am using GetSubsystem<Engine>()->RunFrame();	 to render my loading screen :slight_smile:

-------------------------

