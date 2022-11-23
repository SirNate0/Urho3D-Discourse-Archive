claudeHasler | 2020-03-18 18:16:04 UTC | #1

Im trying to display a cross at the pixel where a mouseclick is performed, but I havent figured out how. Does Urho have a 2d primitives drawing system?

-------------------------

throwawayerino | 2020-03-18 17:39:20 UTC | #2

You could get mouse position from UI subsystem and draw a borderimage

-------------------------

claudeHasler | 2020-03-18 18:00:11 UTC | #3

Ill try that. What i've tried is to set a text "X" at the place where I clicked but nothing shows up.
This is subscribed to E_MOUSEBUTTONUP, and the handler gets called. It just doesnt draw the ui
[Code]
void MyApp::HandleEvent(StringHash eventType, VariantMap& eventData)
{
    std::cout << "clicked" << std::endl;

    Input* input = GetSubsystem<Input>();
    UI* ui = GetSubsystem<UI>();
    if (input) {
        std::cout << input->GetMousePosition().x_ << " " << input->GetMousePosition().y_ << std::endl;
        if (ui) {
            auto root = ui->GetRoot();
            auto text = root->CreateChild<Text>();
            text->SetPosition(input->GetMousePosition().x_, input->GetMousePosition().y_);
            text->SetText("X");
            text->SetColor(Color(255, 0, 0));
        }
    }
}
[/Code]

-------------------------

Modanung | 2020-03-18 18:17:55 UTC | #4

Does your `UI` have a (default) style assigned to it? Sample 2 shows you how.

-------------------------

claudeHasler | 2020-03-18 19:23:59 UTC | #5

No im not setting any styles, is this necessary?

-------------------------

Modanung | 2020-03-18 19:31:34 UTC | #6

Yes, I believe this to be the case.

-------------------------

throwawayerino | 2020-03-18 20:32:00 UTC | #7

yes it is. UI is a bit weird right now, but trust me you'll love it once you get used to it.

-------------------------

claudeHasler | 2020-03-19 16:53:31 UTC | #8

Thanks to both of you. Drawing both sprites and text is now working.

When drawing a sprite, im currently assigning loading texture like so:
[Code]
auto texture = GetSubsystem<ResourceCache>()->GetResource<Texture2D>("Textures/cross.png");
sprite->SetTexture(texture);
[/Code]

What is the lifetime of such a texture? Should I be loading the texture once for every Sprite I assign it to? Or only once and share it? If I share the texture, may I store it in a SharedPtr<Texture> or should it be a raw pointer?

-------------------------

SirNate0 | 2020-03-19 18:44:27 UTC | #9

The resource cache stores a pointer to the loaded resource and returns it when you request the same resource. So they are shared between all of them, and as long as you know that the resource cache will keep the texture alive longer than you keep the pointer you can use a raw pointer. If you're not certain, stick with the shared pointer.

-------------------------

