throwawayerino | 2019-06-28 19:07:01 UTC | #1

Calling `SetStyleAuto()` on a UI element is translated to `SetStyle("ClassName")` where ClassName is the name of the UI element's class. It then searches for the name in the xml file set in `SetDefaultStyle()`.  If you subclass from `Button` for example and call the new class `MyButton`, calling `SetStyleAuto()` will search for "MyButton" in the default style. If you don't have a style set for it you'll get a white rectangle or box.
A solution is to either to call `SetStyle("Button")` to get the parent's style, or to define a style called "MyButton" in the xml and customize it

Also, in the `RegisterObject()` method (if you made one) calling `URHO3D_COPY_BASE_ATTRIBUTES(ParentClassName)` after registering it is important to make sure the editor knows how to handle it.

EDIT: wtf I just want to talk about UI

-------------------------

Modanung | 2019-06-26 08:14:54 UTC | #2

Wouldn't it make more sense if `SetStyleAuto()` were only to *report the absense* of any appropriate style, *without* clearing the element's style, in cases where no suitable style is found?

-------------------------

Leith | 2019-06-26 10:43:22 UTC | #3

Absolutely, I do not like obscurity in my game engine codebase. I would rather try to reduce or remove it.

-------------------------

weitjong | 2019-06-26 11:05:06 UTC | #4

When the style is not applied then you get a naked UI-element. The `SetStyleAuto()` is just a shorthand for calling `SetStyle()` with the class name as parameter. It does not perform the “clearing” first.

Probably worth to mention that the style can be inherited in the stylesheet.

-------------------------

Leith | 2019-06-26 11:06:24 UTC | #5

You missed your opportunity to explain all this, it was explained several posts ago, but thanks

-------------------------

Modanung | 2019-06-26 12:57:05 UTC | #6

[quote="weitjong, post:4, topic:5254"]
The `SetStyleAuto()` is just a shorthand for calling `SetStyle()` with the class name as parameter.
[/quote]
*That* seems to be the case. But don't you think it would maybe make more sense for `SetStyleAuto()` to look more like this?
```
if (StyleExists(className))
    SetStyle(className);
```
...instead of `style = noStyle`.
When I'm out of clean clothes, I wear dirty clothes. I do not walk the streets naked. :vulcan_salute:t3:

-------------------------

weitjong | 2019-06-26 13:00:42 UTC | #7

I haven’t looked at the code yet in the UI Subsystem, but in my view unless we have changed how the style is applied fundamentally, otherwise what you proposed with the extra if exists check would produce exactly the same thing. Except, when you also add another else logic to, say, trying to get the name of the parent class via some kind of reflection and use the style of the parent class name.

-------------------------

throwawayerino | 2019-06-26 13:58:10 UTC | #8

You could have a template method like this:
```
template<class T>
void SetStyleAuto() {
	if(StyleExists(T))
		SetStyle(T)
	else
		SetStyle(T::BaseClassName)
}
```

-------------------------

weitjong | 2019-06-26 14:20:20 UTC | #9

But why do we need to go that far to achieve this? When someone derives a new class from a base UI class, it is most likely he/she wants to add more attributes or logic, and that would mean the style of the base class is actually not fit for the derived class. Granted it will make the derived class get some base style applied when its user forget to define the derived style for the derived class in the stylesheet file. Isn't it the easier solution would be to do something like:

```
<element type="MyButton" style="Button" auto="false">
    <attribute name="My Extra Attribute" value="true"/>
</element>
```

-------------------------

throwawayerino | 2019-06-26 14:21:36 UTC | #10

That also works, but when you're prototyping (or simply don't know about this) it can act as a safeguard. But in the end your solution is the most optimal

-------------------------

Modanung | 2019-06-26 14:42:26 UTC | #11

I wasn't so much talking about subclassing actually. *With little experience with Urho's UI*, my logic tells me it does not make sense to overwrite existing style settings with none as I imagine `SetStyleAuto()` would be most useful when iterating over a bunch of `UIElement`s. One could make differently coloured themes that share a single base style that would always be loaded first. Elements without colour could be left out the settings for the coloured elements.

-------------------------

Leith | 2019-06-26 14:50:54 UTC | #12

Urho's gui is horrible, to be honest but we can mostly ignore it

-------------------------

Leith | 2019-06-26 14:53:01 UTC | #13

dropping in a replacement gui rendering system is completely doable

-------------------------

Leith | 2019-06-26 14:55:12 UTC | #14

dont let these guys make you think there are limits, they are not clearly stating there are, so the chances are good

-------------------------

weitjong | 2019-06-26 15:35:22 UTC | #15

It almost sounded like you want to reimplement the “cascading style sheet”. :slight_smile:

-------------------------

Modanung | 2019-06-26 15:38:48 UTC | #16

For now I'm dealing with Qt. ;)
...which has its own minor flaws and some bugs that are reaching puberty.

-------------------------

Leith | 2019-06-26 15:39:12 UTC | #17

does urho conform to css? lmao

-------------------------

throwawayerino | 2019-06-26 15:39:48 UTC | #18

That would be a nightmare for everyone.

-------------------------

Leith | 2019-06-26 15:46:22 UTC | #19

do what you need to do, ask what you need to ask, I for one will help you achieve it, but do not think for a second that urho is some kind of panacea - it hurts my head just asking about making moderate changes, let alone the harder ones. People around here are allergic to change, they think we carry in disease, they are closed of mind and their eyes are shaded, but this does not mean that I can not help you.

-------------------------

throwawayerino | 2019-06-26 16:02:26 UTC | #20

real deep thoughts here

-------------------------

Modanung | 2019-06-26 18:44:52 UTC | #21

[quote="Leith, post:19, topic:5254"]
People around here are allergic to change, they think we carry in disease, they are closed of mind and their eyes are shaded
[/quote]

@Leith I don't think this is true at all. Apart from the fact that some changes *should* be resisted, more often progress is welcomed by the community but left unfinished by the loudmouth that bites off more than (s)he can chew.

Planning a journey is not the same as refusing to travel... also there's no _team_ in h**i**tchh**i**k**i**ng. :ghost::+1:

-------------------------

Leith | 2019-06-27 06:58:25 UTC | #23

I'm an agent of (hopefully, positive) change, it is my nature to question the status quo, and find fault in the machine. I am a systems analyst among other titles, it's hard not to apply that to everything that comes my way. So far I have issued a range of suggestions for improving Urho, but the only one that has been well-received is also the only one that could break existing projects. I don't really know what to make of that :slight_smile:

-------------------------

Pencheff | 2019-06-27 18:48:04 UTC | #24

You can always fork/branch and PR. Atomic went this way of changing too much, look at where it is now...

-------------------------

Modanung | 2019-06-28 00:27:39 UTC | #25

Panta rhei *is* the status quo, although sometimes the flow may seem viscous to the point of asphalt. :volcano:

-------------------------

guk_alex | 2019-06-28 07:47:02 UTC | #26

In some point when your changes gone radically different and you don't want to fork - you can try to convince everybody else about major version update, 2.0, in this situation people can accept compatibility breaks without arguing too much. And it seems more reasonable instead of working on you own with your fork with the same kind of updates. But you need to convince the rest of active community to do that and make rough plans about the future.

-------------------------

Leith | 2019-06-28 08:07:09 UTC | #27

Man, I have not made any game breaking changes. I would like you, or anyone, possibly an ass hat, to show me where I ever did. I have some changes in mind. I will offer them back. Free of charge.

-------------------------

Leith | 2019-06-28 08:08:55 UTC | #28

thats not my intent, and heres some more character to meet the 20 character quota

-------------------------

weitjong | 2019-06-28 08:16:36 UTC | #29

Closed as it has gone off topic.

-------------------------

