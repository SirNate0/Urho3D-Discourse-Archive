SteveU3D | 2017-07-21 17:16:10 UTC | #1

Hi,

I created an application which integrates Urho3D in a QML window via external window.
The problem I ran into is about threads. Indeed, in my code, I have : 

    int main(int argc, char *argv[])
    {
        QGuiApplication app(argc, argv);
        QQmlApplicationEngine engine;

        //declaration of instances, ...
        ....

        //Urho3D
        mUrho3DContext = new Urho3D::Context();
        mUrho3DApplication = new Urho3DApplication(mUrho3DContext);

        //qml interface is loaded
        engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

        mUrho3DApplication->Run();
    
        return app.exec();
    }

The problem is that when Urho3D starts, it keeps the hand and consequently "return app.exec()" is never executed, which is a real problem for my Qt application which requires that instruction to run correctly.

So is it possible to run all Urho3D in a complete separated thread so that my main thread is handled by Qt, so no Urho3D in the main thread? For what I read, Urho3D needs the main thread so ... not sure about the  feasability of what I need.

Thanks.

-------------------------

kostik1337 | 2017-07-20 13:12:53 UTC | #2

I don't think having multiple threads is really good idea. You need Qt and Urho3D both running main loop, and as I understand, common workaround is to call RunFrame() by hand via timer. Check out and how it is done in ParticleEditor2D:
https://github.com/aster2013/ParticleEditor2D/blob/master/Source/Tools/ParticleEditor2D/ParticleEditor.cpp#L86

-------------------------

Eugene | 2017-07-20 13:13:44 UTC | #3

You shall probably avoid using Appliaction if you don't want Urho to be the ruler of application life.

Think twice before bringing multithread hell into your application.

-------------------------

johnnycable | 2017-07-20 14:20:08 UTC | #4

@SteveU3D 
Check Urho code for starting Emscripten or Ios. There's a different launch procedure, because of same problem; i don't remember the details, but emsc use web workers and cannot return directly, or so; and ios never return, because there's no such thing as a "exit app" on ios...

-------------------------

Modanung | 2017-07-20 14:59:56 UTC | #5

I see multiple inheritance is another part of the key in the case of the ParticleEditor:
https://github.com/aster2013/ParticleEditor2D/blob/master/Source/Tools/ParticleEditor2D/ParticleEditor.cpp#L51-L53

-------------------------

SteveU3D | 2017-07-21 17:16:42 UTC | #6

Thanks for your answer. I was able to do it like in the Particle example.

* a class which inherits from Urho3D::Object (the Urho3D class with the scene, all 3D objects, ...) instead od Urho3D::Application, and with in particular a function to update the scene with engine_->RunFrame(),
* a class which inherits from QApplication with a slot which is executed all n milliseconds, this slot executes the update function of the Urho3D class.

And the 

    return app.exec();

of Qt is well executed.

-------------------------

jonathan | 2017-10-08 18:06:01 UTC | #7

Hey @SteveU3D, I'd be very interested to see a minimal example of how to integrate Urho into a QML application. If you've made any progress, posting some example code to GitHub would be greatly appreciated!

Thanks

EDIT: I'll be trying this this week, so if I'm able to make a working example I'll post here.

-------------------------

SteveU3D | 2017-10-19 13:45:04 UTC | #8

Hi,
@jonathan 

Sorry for that late answer.
Here is a simple code integrating Urho3D in a QML application. I used it like that (with my own scene, objects, ... not put in the code) but it needs to be improved, so don't hesitate to do it :slight_smile: .

In particular, one thing I didn't succeed to do and I really need in my final application is to delete the Urho3DApplication class and create it again at runtime with Urho3DManager class (I deleted from the code on github the tests I did in Urho3DApplication destructor).

I wrote some explanations in README file but if you have questions, ask :) .

Repository : https://github.com/SteveTJS/urho3DInQML

Thanks.

-------------------------

