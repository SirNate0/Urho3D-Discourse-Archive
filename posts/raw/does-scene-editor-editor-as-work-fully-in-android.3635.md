alanm | 2017-10-04 15:15:20 UTC | #1

I would like to use Editor.as in my android device for content editing on the road. I built the andorid package from Urho3D-1.7.  As it is I cannot rotate or pan the  3d view with touch and I could not figure how to simulate a right mouse click with touch.  it seems model/scene import relies on a external executable (AssetImporter) which freeze when I click on the import menu. Does Editor.as suppose to work in Android?

-------------------------

Eugene | 2017-10-04 15:20:03 UTC | #2

In fact, nobody tried to make Editor work on mobiles.
You could try to use smth like that:
https://github.com/scorvi/Urho3DSamples/tree/master/06_InGameEditor

-------------------------

