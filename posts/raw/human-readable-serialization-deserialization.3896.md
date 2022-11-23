TrevorCash | 2017-12-29 18:09:43 UTC | #1

Is there a way of writing Urho Data types to a file in string readable format?  For example I can pass an IntVector3 to URHO3D_LOGINFO and the log will show a nicely formatted readable representation of the data.

I'd like a quick facility to write this same data to a file that I can alter manually and then re-read into my program.

Perhaps a way to set the Serializer object to "Text" mode?

-------------------------

jmiller | 2017-12-31 15:13:13 UTC | #2

Urho has String conversions for reading/writing to a File -- String(float), String(Vector3) etc..

Depending on what you want, this .ini parser might fit. It loads/saves VariantMaps of the human-readable types.
https://discourse.urho3d.io/t/a-more-advanced-ini-parser/1449/2?u=carnalis

-------------------------

