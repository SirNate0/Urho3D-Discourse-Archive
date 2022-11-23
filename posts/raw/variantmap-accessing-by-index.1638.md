vivienneanthony | 2017-01-02 01:09:10 UTC | #1

Question

If I want to access a variantmap easily by index. How? I could probably figure it out but I rather get some input first.


[code]    // convert to variant map
    VariantMap viewSettings_ = m_pViewSettings->ToVariantMap();

    // get count
    for(unsigned int currentSetting=0; currentSetting<10; currentSetting++)
    {

        //thisSettingElement->GetChild(0).SetText= viewSettings_[currentSetting].name();  - I want to set a Text element with the name of viewsettings index currentSetting.
        //thisSettingElement->GetChild(1).SetText= viewSettings_[currentSetting].GetFloat(); - I want to get the value of the float and set the text of the second UIelement with it in String form
    }
[/code]


Vivienne

-------------------------

Sir_Nate | 2017-01-02 01:09:10 UTC | #2

You will probably need to store the settings in another manner, or have another map that relates all of the StringHash values to their original name strings. The VariantMap doesn't store the strings used to create the StringHash keys, only the unsigned hash values themselves. If you just want the number that constitutes the hash value, just use the Keys() function of the VariantMap and iterate through that (or use Begin() or End() and use that iterator to iterate through the key value pairs). If you don't specifically need a VariantMap, try a HashMap<String, Variant> instead of a VariantMap for the settings. Or store them in a variant vector with two variants (a String for the name and then another for the value) used for every setting.

-------------------------

aster2013 | 2017-01-02 01:09:13 UTC | #3

You can get all keys from VariantMap by Call Keys(). then access the keys vector by index.

-------------------------

vivienneanthony | 2017-01-02 01:09:13 UTC | #4

Thanks. I swill try it. Right now I'm just working on trying to get a window background to show up

-------------------------

