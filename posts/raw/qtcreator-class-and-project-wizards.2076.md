Modanung | 2020-03-12 03:26:18 UTC | #1

https://gitlab.com/LucKeyProductions/QtCreatorUrho3DWizards

Placing, or linking to (`ln -s`), the _templates_ folder inside the `~/.config/QtProject/qtcreator/` folder (in Linux) will add both an **Urho3D Project** and an **Urho3D C++ Class** to the _New File or Project_ dialog in QtCreator.

Feel free to fork and modify these wizards to your own liking. Pull requests are also welcome.

### Class wizard

In case of the class wizard this will open a dialog allowing you to name your new class and specify its base class. Instead of typing the name of the base class there's also a drop down containing a selection of commonly inherited-from Urho3D classes to pick from.

### Project wizard

When creating a project with the wizard it should compile _after_ linking to the Urho3D directory from inside the project folder. Don't forget to link to resource folders from inside each build directory as well.

-----

If **CodeBlocks** is your IDE of choice there's also a [project wizard](https://discourse.urho3d.io/t/urho3d-codeblocks-wizard/1379) for that.

-------------------------

kostik1337 | 2017-03-12 12:42:04 UTC | #3

Awesome! Actually, you can place custom wizards into ~/.config/QtProject/qtcreator/templates/wizards/, not /usr/share/..., they'll be local for user

-------------------------

Modanung | 2017-05-15 18:16:24 UTC | #4

Ah thanks, that saves some sudoing. :)

-------------------------

johnnycable | 2017-05-15 15:36:48 UTC | #5

Txx, this is useful!

-------------------------

Modanung | 2020-03-12 03:24:20 UTC | #6

I just extended the *class* wizard somewhat. When creating a class that inherits from either `Component`, `LogicComponent`, `Serializable`, `Drawable`, `Resource` or `ResourceWithMetadata` all virtual functions of the base class will now be overridden with a minimal function.

-------------------------

