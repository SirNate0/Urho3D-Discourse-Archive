Naros | 2021-04-19 20:02:35 UTC | #1

I have defined a very basic & simple menu bar in XML as follows:
```
<?xml version="1.0"?>
<element type="BorderImage" style="EditorMenuBar">
    <attribute name="Name" value="MenuBar" />
    <attribute name="Position" value="0 0" />
    <attribute name="Min Size" value="5 20" />
    <attribute name="Max Size" value="1920 20" />
    <attribute name="Layout Mode" value="Horizontal" />
    <attribute name="Layout Spacing" value="0" />
    <attribute name="Layout Border" value="0 0 0 0" />
    <element type="Menu">
        <attribute name="Name" value="FileMenu" />
        <attribute name="Layout Mode" value="Horizontal" />
        <attribute name="Layout Spacing" value="0" />
        <attribute name="Layout Border" value="8 2 8 2" />
        <attribute name="Size" value="24 20" />
        <attribute name="Popup Offset" value="2 20"/>
        <element type="Text" style="EditorMenuText">
            <attribute name="Text" value="File" />
        </element>
        <element type="Window" popup="true">
            <attribute name="Layout Mode" value="Vertical" />
            <attribute name="Layout Spacing" value="1" />
            <attribute name="Layout Border" value="2 6 2 6" />
            <attribute name="Min Size" value="10 30" />
            <attribute name="Max Size" value="150 150" />
            <attribute name="Size" value="250 20" />
            <element type="Menu">
                <attribute name="Name" value="FileMenuExit" />
                <attribute name="Layout Mode" value="Horizontal" />
                <attribute name="Layout Spacing" value="0" />
                <attribute name="Layout Border" value="8 2 8 2" />
                <attribute name="Size" value="60 20" />
                <element type="Text" style="EditorMenuText">
                    <attribute name="Text" value="Exit" />
                </element>
            </element>
        </element>
    </element>
    <element type="BorderImage" style="EditorMenuBar">
        <attribute name="Min Size" value="1920 20" />
        <attribute name="Name" value="MenuBarSpacer" />
    </element>
</element>
```
I'm trying to mirror the Editor UI behavior and I'm getting notified when the top-level file `Menu` is selected but I am unable to get any events to fire for the `Exit` option.  The event registration I'm using is as follows:

```
auto *element = uiRoot_->GetChildStaticCast<Urho3D::Menu>( "FileMenuExit", true );
SubscribeToEvent( element, Urho3D::E_MENUSELECTED, URHO3D_HANDLER( Application, OnFileMenuExitClicked ) );
```

Any suggestions?

-------------------------

