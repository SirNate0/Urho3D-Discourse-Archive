AlCaTrAzz | 2017-01-02 01:13:25 UTC | #1

is it possible to call SendEvent from within a static function? i'm using an extenal library that has callback functions which are static, and i'd like to be able to fire an event as part of the callback, how do i do this?

-------------------------

weitjong | 2017-01-02 01:13:26 UTC | #2

You need a Urho3D object to send events. In order to send events from a static function then you must find a way to pass a piece of data (an instance of Urho3D::Object class) to your callback function.

-------------------------

AlCaTrAzz | 2017-01-02 01:13:27 UTC | #3

cheers mate, got it sorted. i'm storing a static pointer to my class which inherits from object, and calling SendEvent that way :slight_smile:

-------------------------

