vivienneanthony | 2017-01-02 01:00:13 UTC | #1

Hello,

Is there a way to get the material of a skybox? So it can be changed based on time of day or enviornment.

So far I see, in the Material objcect	SetShaderParameter.

I am trying to setup a way to change the sky look based on differerent conditions. The only think I can think of is two skyboxes with one having a clude layer with opacity and another that  has the actual diffused slash color.

Vivienne

-------------------------

setzer22 | 2017-01-02 01:00:13 UTC | #2

Looking at the documentation for Skybox ([urho3d.github.io/documentation/H ... kybox.html](http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_skybox.html)), I see that it inherits this from Drawable:

[code]Material * GetMaterial () const
    Return material.[/code]

So my bet is that you should try getting the material from the skybox object with the GetMaterial method like this:

[C++]
[code]//Assuming skybox is your skybox reference.
Material* mat = skybox->GetMaterial();

//Do anything you want to mat...[/code]

For the script counterpart check out the Skybox documentation on the script API: [urho3d.github.io/documentation/H ... ass_Skybox](http://urho3d.github.io/documentation/HEAD/_script_a_p_i.html#Class_Skybox)

[Angelscript]
[code]Material@ mat = skybox.materials[0];  //Most getters / setters get translated to properties in the script API as you can see.[/code]

Feel free to ask for further details if I missed something. I'll try to help all I can!

PD: I don't know why Skybox.materials is a vector in the Script API (the property "material" seems to be write-only) but having only one material it should be on position 0. I haven't tested it so correct me if I'm wrong.

-------------------------

