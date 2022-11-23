Lumak | 2017-01-02 01:05:42 UTC | #1

This code example solves how to group multiple CheckBoxes and have only one checkbox be selected in the group, similar to how a group of radial buttons typically function. I think something like this would be a common feature, but I couldn't find it in the engine.

1) A minor change required in CheckBox.h - add:
[code]
    void InternalSetChecked(bool _bChecked)
    {
        checked_ = _bChecked;
    }
[/code]

2) Add UIEvent
[code]
EVENT(E_GROUPCHECKBOX, GroupCheckBoxNamespace)
{
    PARAM(P_ELEMENT, Element);             // UIElement pointer
}

[/code]
3) GroupCheckBox class
[code]
class GroupCheckBox : public UIElement
{
    OBJECT(GroupCheckBox);
public:
    GroupCheckBox(Context *_pContext)
        : UIElement( _pContext )
    {
        m_vpCheckBox.Clear();
    }

    ~GroupCheckBox()
    {
        m_vpCheckBox.Clear();
    }

    void AddCheckBox(CheckBox *_pCheckBox, bool _bChecked)
    {
        if ( _pCheckBox )
        {
            _pCheckBox->InternalSetChecked( _bChecked );

            AddChild( _pCheckBox );

            m_vpCheckBox.Push( _pCheckBox );

            SubscribeToEvent( _pCheckBox, E_TOGGLED, HANDLER(GroupCheckBox, HandleCheckBoxToggle));
        }
    }

    CheckBox* GetCheckBox(unsigned _idx)
    {
        if ( _idx < m_vpCheckBox.Size() )
        {
             return m_vpCheckBox[ _idx ];
        }
        return NULL;
    }

    void HandleCheckBoxToggle(StringHash _eventType, VariantMap& _eventData)
    {
        using namespace Toggled;

        CheckBox *pCheckBox = (CheckBox*)_eventData[P_ELEMENT].GetVoidPtr();

        if ( pCheckBox )
        {
            for ( unsigned i = 0; i < m_vpCheckBox.Size(); ++i )
            {
                m_vpCheckBox[ i ]->InternalSetChecked( m_vpCheckBox[ i ] == pCheckBox );
            }

            VariantMap& eventData = GetEventDataMap();
            eventData[P_ELEMENT]  = this;

            SendEvent( E_GROUPCHECKBOX, eventData );
        }
    }

protected:
    Vector<CheckBox*>   m_vpCheckBox;
};

[/code]

-------------------------

weitjong | 2017-01-02 01:05:42 UTC | #2

The RadioButton class is missing in our class hierarchy. Instead of calling it group checkbox, I suppose you could refactor to rename your new class to RadioButton proper and then modify the bin/Data/Textures/UI.png to have the images of radio button in various states, and modify the bin/Data/UI/DefaultStyle.xml to specify that your new RadioButton should use the new textures. If you make a pull request for those changes, I reckon it would be accepted.

-------------------------

Lumak | 2017-01-02 01:05:43 UTC | #3

I'm fairly new to Urho3D, so I probably wouldn't make any pull requests anytime soon.  As for my current project, I'm still debating whether the checkbox image looks alright being used as radial buttons.  It doesn't look all that bad, but I might end up doing what you've suggested.

-------------------------

