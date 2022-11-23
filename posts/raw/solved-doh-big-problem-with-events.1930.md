Kanfor | 2017-01-02 01:11:38 UTC | #1

Hi, urhofans.

I have a rare problem. I don't know why but I can't subscribe to new events in my new class.
I have scene, logicomponent, Ui, Uicomponent, etc.

The new class is a simple LogicComponent, but when I add SubscribeToEvent, it crash.

[code]using namespace Urho3D;

class Prueba : public LogicComponent {
    URHO3D_OBJECT(Prueba, LogicComponent)
public:
    Prueba(Context* context);
    virtual ~Prueba();
private:
    void Function();
};[/code]

[code]#include "Prueba.h"

Prueba::Prueba(Context* context) : LogicComponent(context)
{
    SubscribeToEvent(E_SCENEUPDATE, URHO3D_HANDLER(Prueba, Function));
}


Prueba::~Prueba()
{
}

void Prueba::Function()
{
    
}[/code]

I think is all right. Please, help me  :cry:

-------------------------

yushli | 2017-01-02 01:11:38 UTC | #2

Function should be 
Function(StringHash eventType, VariantMap& eventData)

-------------------------

Kanfor | 2017-01-02 01:11:38 UTC | #3

[img]http://vignette1.wikia.nocookie.net/lossimpson/images/e/e1/Doh.jpg/revision/latest?cb=20100310193338&path-prefix=es[/img]


ONE HOUR!!!!  :blush:

Thank you!

-------------------------

