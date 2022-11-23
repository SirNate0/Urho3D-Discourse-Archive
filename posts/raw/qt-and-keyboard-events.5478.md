codexhound | 2019-08-16 09:54:22 UTC | #1

So I've been messing around with integrating qt and urho. I have it set up to render frames with a qtimer (one frame at a time) and in my update event it won't detect keyboard events. Mouse events work but it won't detect any key presses. Is there something extra I have to do? My app is deriving from object and qapplication and has a run function which initializes engine.

-------------------------

Modanung | 2019-08-16 22:14:41 UTC | #2

`QWidget` has virtual input event functions that can be overridden. A `QMainWindow` _is_ a `QWidget` while a `QApplication` is not.
For example: You can use `keyPressEvent(QKeyEvent* event)` **`override`** to catch widget events.
[details=From qwidget.h]
```
    // Event handlers
    bool event(QEvent *event) Q_DECL_OVERRIDE;
    virtual void mousePressEvent(QMouseEvent *event);
    virtual void mouseReleaseEvent(QMouseEvent *event);
    virtual void mouseDoubleClickEvent(QMouseEvent *event);
    virtual void mouseMoveEvent(QMouseEvent *event);
#if QT_CONFIG(wheelevent)
    virtual void wheelEvent(QWheelEvent *event);
#endif
    virtual void keyPressEvent(QKeyEvent *event);
    virtual void keyReleaseEvent(QKeyEvent *event);
    virtual void focusInEvent(QFocusEvent *event);
    virtual void focusOutEvent(QFocusEvent *event);
    virtual void enterEvent(QEvent *event);
    virtual void leaveEvent(QEvent *event);
    virtual void paintEvent(QPaintEvent *event);
    virtual void moveEvent(QMoveEvent *event);
    virtual void resizeEvent(QResizeEvent *event);
    virtual void closeEvent(QCloseEvent *event);
#ifndef QT_NO_CONTEXTMENU
    virtual void contextMenuEvent(QContextMenuEvent *event);
#endif
#if QT_CONFIG(tabletevent)
    virtual void tabletEvent(QTabletEvent *event);
#endif
#ifndef QT_NO_ACTION
    virtual void actionEvent(QActionEvent *event);
#endif

#ifndef QT_NO_DRAGANDDROP
    virtual void dragEnterEvent(QDragEnterEvent *event);
    virtual void dragMoveEvent(QDragMoveEvent *event);
    virtual void dragLeaveEvent(QDragLeaveEvent *event);
    virtual void dropEvent(QDropEvent *event);
#endif

    virtual void showEvent(QShowEvent *event);
    virtual void hideEvent(QHideEvent *event);
    virtual bool nativeEvent(const QByteArray &eventType, void *message, long *result);

    // Misc. protected functions
    virtual void changeEvent(QEvent *);
```
[/details]

-------------------------

Sinoid | 2019-08-18 07:04:46 UTC | #3

You have to disable the input handling in Urho3D. If you need more than one instance of Urho3D running then there's some tweaks you have to do to the handling of MM_FREE in `Input.cpp`. 

When hosting you definitely want QT to be in charge as SDL input capture and handling is complete garbage anyways. Using QT for input will get you reliable captures, while SDL stands around wearing a wife beater and hurling slurs instead of doing anything to help you out.

-------------------------

Modanung | 2019-08-18 11:01:43 UTC | #4

[quote="Sinoid, post:3, topic:5478"]
If you need more than one instance of Urho3D running...
[/quote]
But why would you do that?

I use multiple viewports instead. They are rendered to a texture using manual updates, which is then converted to a `QPixmap`. This way everything remains within the same context.

-------------------------

codexhound | 2019-08-18 13:04:58 UTC | #5

I decided to use QT only for the keyboard events because it's apparently blocking the signals to Urho.

Heres a sample starter project integrating with qt if anyone is interested. Theres a handler for the keyboard and it uses a q timer and a widget as the external render window.

https://github.com/codexhound/Urho3D_QT/

-------------------------

Sinoid | 2019-08-20 04:59:28 UTC | #6

[quote="Modanung, post:4, topic:5478"]
But why would you do that?
[/quote]

Isolation only really. It would be nice to support multiple *heads* someday.

QPixmap or GL context sharing works.

-------------------------

