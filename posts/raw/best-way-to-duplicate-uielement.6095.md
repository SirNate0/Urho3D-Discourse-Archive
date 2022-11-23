Lys0gen | 2020-04-18 00:51:34 UTC | #1

Hello,
I would like to duplicate certain UI elements in order to have "template" elements that go beyond the defaultStyle settings. Since there is no copy constructor I tried doing this with the SaveXML(XMLElement& dest) & LoadXML(XMLElement& source) functions as follows:

        Urho3D::Button* buttonTemplate = ...
        XMLElement templateStyle;            
        buttonTemplate->SaveXML(templateStyle);

        Urho3D::Button* duplicateButton = new Button(context_);
        duplicateButton->LoadXML(templateStyle);

Sadly this fails, SaveXML returns false, the XMLElement and the duplicate remain without any attributes. Saving into a file for test purposes like this works as expected though, the file contains all the attributes

        Urho3D::File serializedFile(context_, "test.xml", FILE_WRITE);
        buttonTemplate->SaveXML(serializedFile);

What am I doing wrong? Is there a better way to achieve this?
Thanks!

-------------------------

SirNate0 | 2020-04-18 19:29:14 UTC | #2

I don't remember if `XMLElements` can exist on their own like that. Try creating an `XMLFile` and saving it to an element in that. Other than that, check and see if there are error messages in the log.

-------------------------

Modanung | 2020-04-18 13:03:59 UTC | #3

Indeed `XMLElement::SetAttribute` returns false when it is not associated with an `XMLFile`.

-------------------------

Lys0gen | 2020-04-18 19:29:08 UTC | #4

Thanks guys!
Seems a bit convoluted to me, I don't really know why the XMLFile is necessary but it works, I guess.


            XMLFile blankFile(context_);
            XMLElement templateStyle = blankFile.CreateRoot("thisNameIsIrrelevant");
            
            Urho3D::Button* buttonTemplate = ...
            buttonTemplate->SaveXML(templateStyle);
            
            Urho3D::Button* duplicateButton = new Button(context_);
            duplicateButton->SetStyle(templateStyle);

-------------------------

Modanung | 2020-04-18 19:46:28 UTC | #5

Hey... now it says `SetStyle`.

-------------------------

Lys0gen | 2020-04-18 20:01:18 UTC | #6

Yup, LoadXML doesn't properly do what I want, i.e. size gets copied but the whole element is just white (doesn't copy the default style settings maybe?). SetStyle makes the whole thing look exactly like the template.

-------------------------

Modanung | 2020-04-18 20:22:35 UTC | #7

I have barely any practical experience with the UI system, but some `Clone` function (as `Material` has) seems to be what you're after. [spoiler]I would not expect `SaveXML` and `SetStyle` to be compatible. EDIT: Although `SetStyle` *does* seem to call `UIELement::LoadXML`.[/spoiler]

Did you call `SetDefaultStyle` on the `UI` root?
And maybe try `SetStyleAuto(blankFile)`.

-------------------------

Lys0gen | 2020-04-18 20:25:09 UTC | #8

Huh, the code above works now, did you overlook my statement or do you want to discuss the intricacies of Urhos UI system now? :slight_smile: As said, I am not entirely sure why it has to be like this and it certainly seems like it is not completely intended to be used like this but... it works. So that is good enough for me currently :D
Thanks for taking your time digging through it. And yes, my UI root has a defaultStyle set.

-------------------------

Modanung | 2020-04-18 20:42:02 UTC | #9

Well you _could_ create a second style file beforehand, I guess. Would that seem less convoluted?

...or save the style during one run, after which you can remove/comment the saving code.

[quote="Lys0gen, post:8, topic:6095"]
Huh, the code above works now, did you overlook my statement or do you want to discuss the intricacies of Urhos UI system now?
[/quote]
[quote="Lys0gen, post:6, topic:6095"]
SetStyle makes the whole thing look exactly like the template.
[/quote]

I misunderstood template as meaning default style.

-------------------------

Eugene | 2020-04-18 20:44:19 UTC | #10

[quote="Lys0gen, post:4, topic:6095"]
I don’t really know why the XMLFile is necessary
[/quote]
I can answer this one. `XMLElement` is handler type, somewhat like pointer. It doesn't *store* anything.

-------------------------

