grokko | 2020-10-29 06:25:18 UTC | #1

Hi All!,
  I'm compiling an Application framework based on the code from the 'First Project'.
Now, i understand that this framework has one Start method, and from there you set your event handlers and what not. Now, in the examples I happily went through the extra Components like LogicComponent, and Component. However, I cannot for the life of me register a component in my Start method of the 'First Project'.
  In my main class I declare 

WeakPtr<Laser> laser_;

and

Node * laser = scene_->CreateChild "laser";
laser_ = laser->CreateComponent Laser;

But when the main Start() gets to laser_->Start() it crashes 

Correct me when I'm wrong but as soon as i declare
Node * laser = scene_->CreateChild "laser";
laser_ = laser->CreateComponent "Laser"

the registrant of the new <Laser> should be exposed and visible....it's not!

Please Help...I know that the examples are full of extra components but they're wrapped in the Sample framework.

Lord Fiction

-------------------------

Modanung | 2020-10-28 23:23:26 UTC | #2

Did you _register_ the component, or are you getting an unknown component error, followed by a nullptr exception?

```
context_->RegisterFactory<Laser>();
```

-------------------------

grokko | 2020-10-28 23:01:38 UTC | #3

Hi,
  I believe its registered in the Component class like...
void Laser::RegisterObject(Context* context)
{
	cout << "reg here " << endl;
	context->RegisterFactory<Laser>();
}

?????

-------------------------

Modanung | 2020-10-28 23:32:26 UTC | #4

Pretty close, it's a template function=[![80x23](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Ffreepngimages.com%2Fwp-content%2Fuploads%2F2015%2F12%2Fhavana-cigar-transparent-background.png)](https://discourse.urho3d.io/t/app-framework-befudlement/6475/2)

-------------------------

grokko | 2020-10-28 23:03:32 UTC | #5

i dunno how to do text on this!

-------------------------

vmost | 2020-10-28 23:03:34 UTC | #6

Hi and welcome!

You don't need to write your own main function. Instead just inherit from `Urho3D::Application` and write your own `class App final : public Application` class with overrides for `Setup()`, `Start()`, and `Stop()`. At the bottom of your `app.cpp` file write this:
```
URHO3D_DEFINE_APPLICATION_MAIN(MyApp)
```

-------------------------

grokko | 2020-10-28 23:04:18 UTC | #7

i did that. the class is in the website

-------------------------

Modanung | 2020-10-28 23:04:43 UTC | #8

[quote="grokko, post:5, topic:6475, full:true"]
i dunno how to do text on this!
[/quote]

I dunno what you mean by that. :slightly_smiling_face:

-------------------------

Modanung | 2020-10-29 06:25:30 UTC | #9

Also, is the `RegisterObject` being called somewhere? And is it a static function?

In my view, there's usually no need to wrap `RegisterFactory` into a `RegisterObject` function, btw.

-------------------------

vmost | 2020-10-28 23:09:03 UTC | #10

I must say registering new components is quite ambitious for a newbie. Have you tried getting a bare-bones project compiled and running, e.g. just a blank window?

-------------------------

Modanung | 2020-10-28 23:11:28 UTC | #11

>  [:musical_note: **Too Many People** by _Leaves_](https://www.youtube-nocookie.com/embed/NKHNqM4aCOY?autoplay=true)

-------------------------

grokko | 2020-10-28 23:12:52 UTC | #12


Like i could pull the vehicle Sample LogicComponents .cpp and .h and put them in my project and declare
vehicle_ = node->CreateComponent*<Vehicle`>`

and nothing shows up registered or on console as queuing up....

-------------------------

vmost | 2020-10-28 23:19:16 UTC | #13

It's hard to help you without more context. Have ever successfully compiled and run any Urho3D project? That is the starting point. Also, you can use back ticks to autoformat code snippets.
```
``` start backticks
some code
``` end backticks
```

-------------------------

grokko | 2020-10-29 01:33:20 UTC | #14

Okay…I figured it out…we had to make a hard register call…like

…Laser::RegisterObject(context);…once we had the template pointer ‘Laser’.

Works perfectly, my objects are all on the queuing cycle!

Lord Fiction

-------------------------

