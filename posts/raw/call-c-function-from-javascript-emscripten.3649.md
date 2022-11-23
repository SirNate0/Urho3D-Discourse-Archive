Petryk | 2017-10-11 09:25:37 UTC | #1

Hi,

I'm trying to call c++ function definied in my Application class from javascript, but with no success.

My application class definition is:

<pre>
SharedPtr<Text> helloText;
public: SampleApplication(Context * context) : Application(context) {}
void CreateText()
	{
		helloText=new Text(context_);
		helloText->SetText("Hello!");
		helloText->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"), 30);
		helloText->SetColor(Color(0.0f, 1.0f, 0.0f));
		helloText->SetHorizontalAlignment(HA_CENTER);
		helloText->SetVerticalAlignment(VA_CENTER);
		GetSubsystem<UI>()->GetRoot()->AddChild(helloText);
	}
public: void ChangeTextFromJs()
{
	helloText->SetText("Hello from JS!");
}
</pre>

I want to call public function ChangeTextFromJs in my javascript code (after click some html button).

<pre>
<script type='text/javascript'>
      var Module = {
        preRun: [],
        postRun: [],
        print: (function() {
.....
</pre>

-------------------------

kostik1337 | 2017-10-11 10:41:48 UTC | #2

Probably, what you need is [embind](https://kripken.github.io/emscripten-site/docs/porting/connecting_cpp_and_javascript/embind.html)

-------------------------

Petryk | 2017-10-11 11:17:15 UTC | #3

@kostik1337 thank You for reply! Could you provide some example code? I don't know how to handle current instance of my SampleApplication...

-------------------------

kostik1337 | 2017-10-11 11:43:35 UTC | #4

Well, I didn't have any experience with Urho3D+emscripten. I can suggest you to create 2 binds, bind for a static C function that returns pointer to SampleApplication, and a bind for ChangeTextFromJs. Most probably, you'll need to rewrite URHO3D_DEFINE_APPLICATION_MAIN macro, to store pointer to application into some static variable in global namespace

-------------------------

