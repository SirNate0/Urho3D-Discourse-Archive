Hevedy | 2017-01-02 00:58:21 UTC | #1

I like import the Urho3D to Qt 5 (Windows 7 x64 using Qt5 x32 for VS 2012). 
I added the all includes of engine and the lib of Urho3D.

Now i like run the c++ example HelloWorld but no idea how. (I like use the Qt window and show in one frame the example of Urho3D).

-------------------------

alexrass | 2017-01-02 00:58:21 UTC | #2

[urho3d.github.io/documentation/a00013.html](http://urho3d.github.io/documentation/a00013.html)

Engine has param ExternalWindow 
[quote]ExternalWindow (void ptr) External window handle to use instead of creating an application window. Default null.[/quote]

but i don't try...

-------------------------

aster2013 | 2017-01-02 00:58:21 UTC | #3

You can use following code:

[code]
    VariantMap engineParameters;
    engineParameters["ExternalWindow"] = widget->winId();
    if (!engine_->Initialize(engineParameters))
        return -1;[/code]

-------------------------

Hevedy | 2018-03-16 09:22:03 UTC | #4

But i need some more specific about the files of source, i don't idea about how implement this.

[b]Main.cpp[/b]
[code]
#include "U3DWidget.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    U3DWidget w;
    w.show();

    return a.exec();
}
[/code]

[b]U3DWidget.h[/b]
[code]
#ifndef U3DWIDGET_H
#define U3DWIDGET_H

#include <QtOpenGL>
#include <QGLWidget>
#include "Engine/Core/CoreEvents.h"
#include "Engine/Engine/Engine.h"
#include "Engine/UI/Font.h"
#include "Engine/Input/Input.h"
#include "Engine/Core/ProcessUtils.h"
#include "Engine/UI/Text.h"
#include "Engine/UI/UI.h"
#include "Engine/Container/DebugNew.h"
#include "Samples/Sample.h"

class U3DWidget : public QGLWidget {
    Q_OBJECT
    public:
        U3DWidget();
        ~U3DWidget();

    protected:
        void initializeGL();
        void paintGL();
        void resizeGL(int width, int height);

    private:
};

#endif
[/code]

[b]U3DWidget.cpp[/b]
[code]
#include "U3DWidget.h"
#include <stdexcept>

U3DWidget::U3DWidget() : QGLWidget() { }

U3DWidget::~U3DWidget() {

}

void U3DWidget::initializeGL() {

}

void GLWidget::paintGL() {

}

void GLWidget::resizeGL(int width, int height) {

}
[/code]

Now i no idea about how continue...

-------------------------

Azalrion | 2017-01-02 00:58:26 UTC | #5

Just a quick reply because I've got to run, but in essence you need to use Engine without Application so you control the lifecycle and can call the render / update (I've forgotten what its called) in paintGL(), resize well handle the resizing of the window like normal for Urho and for initialization thats where you initialize the engine class and pass through any parameters etc. Look at the Application class already in urho for what you need to do as youll need to replicate the functionality into the widget.

For a guideline look at how someone integrated ogre: [radmangames.com/programming/ ... and-ogre3d](http://www.radmangames.com/programming/successfully-integrating-qt-and-ogre3d).

If you're still having trouble I'll try write up some pseudo code (won't be tested as I'll be damned if I let the horror that is Qt on my machine again) in the next couple of days that should give you an idea.

-------------------------

Hevedy | 2017-01-02 00:58:26 UTC | #6

[quote="Azalrion"]Just a quick reply because I've got to run, but in essence you need to use Engine without Application so you control the lifecycle and can call the render / update (I've forgotten what its called) in paintGL(), resize well handle the resizing of the window like normal for Urho and for initialization thats where you initialize the engine class and pass through any parameters etc. Look at the Application class already in urho for what you need to do as youll need to replicate the functionality into the widget.

For a guideline look at how someone integrated ogre: [radmangames.com/programming/ ... and-ogre3d](http://www.radmangames.com/programming/successfully-integrating-qt-and-ogre3d).

If you're still having trouble I'll try write up some pseudo code (won't be tested as I'll be damned if I let the horror that is Qt on my machine again) in the next couple of days that should give you an idea.[/quote]

I see the widgets of ogre and repos with that but, i no idea about how make that for urho3d

-------------------------

