TikariSakari | 2017-01-02 01:03:53 UTC | #1

I was trying to do some ui-scaling like buttons mostly so that they would scale according to screen resolution, this is the code I have. I think I managed to get it to work at least up to some level. Maybe it will help others or maybe even someone can improve the code a lot.

The code is definitely not pretty, just a warning. I am using the sample as a base class.

[code]

void MyProj::Setup()
{
	Sample::Setup();
	engineParameters_["WindowResizable"] = true; // to make window resizable.

}

void MyProj::SubscribeToEvents()
{
    // Subscribe HandleUpdate() function for processing update events
    SubscribeToEvent(E_UPDATE, HANDLER(SkeletalAnimation, HandleUpdate));

    // Subscribe HandlePostRenderUpdate() function for processing the post-render update event, sent after Renderer subsystem is
    // done with defining the draw calls for the viewports (but before actually executing them.) We will request debug geometry
    // rendering during that event
    SubscribeToEvent(E_POSTRENDERUPDATE, HANDLER(SkeletalAnimation, HandlePostRenderUpdate));

   // For resizing UI
    SubscribeToEvent( E_SCREENMODE,  HANDLER( MyProj, ResizeUI));
}

/// Handle ScreenMode event. Resize and such.
void MyProj::ResizeUI( StringHash eventType, VariantMap& eventData ) {
    auto rootSize = GetSubsystem<UI>()->GetRoot()->GetSize();


   // I am using class called GameUI for handling the ui.
    if( gameUI_ )
        gameUI_->resizeUI( rootSize.x_, rootSize.y_,
            GetSubsystem<ResourceCache>()->GetResource<Font>(("Fonts/Anonymous Pro.ttf")));

}


void UIGame::resizeUI( const int& width, const int& height, Urho3D::Font* font ) {

    fontSize_ = std::min( width, height ) / 20;

    setElementsZero( root_ );
    resizeElement( root_ );

    root_->SetSize( width, height );
}


// Set all sizes to 0 from deepest first, because if child node is not 0, the parent cannot
// be set to 0. This will not shrink components when making window smaller
void UIGame::setElementsZero( Urho3D::UIElement* element ) {
    for( int i = 0; i < element->GetChildren().Size(); ++i ){
        if( auto tmp = dynamic_cast<Urho3D::DropDownList*>( element ) ) {
            for( int j = 0; j < tmp->GetItems().Size(); ++j )
                setElementsZero( tmp->GetItems()[j] );
        }
        setElementsZero( element->GetChildren()[i] );
    }

    element->SetMinSize(0,0);
    element->SetSize(0,0);
}

// Sets elements size according to childrens size.
void UIGame::resizeElement( Urho3D::UIElement* element ) {

    auto elements = element->GetChildren();
    if( elements.Size() == 0 )
        return;

    int width = 0;
    int height = 0;


    for( auto elementIter = elements.Begin(); elementIter != elements.End(); ++elementIter ) {
        Urho3D::UIElement* ele = elementIter->Get();

        resizeElement( ele );

        findUIType( ele );



        switch(  element->GetLayoutMode() ) {
            case Urho3D::LM_HORIZONTAL:
                height = std::max(  ele->GetHeight(), height );
            break;

            case Urho3D::LM_VERTICAL:
                width = std::max(  ele->GetWidth(), width );
            break;

            default:
                height = std::max(  ele->GetHeight(), height );
                width = std::max(  ele->GetWidth(), width );
            break;
        }


    }


    switch(  element->GetLayoutMode() ) {
        case Urho3D::LM_HORIZONTAL:
            element->SetMinWidth( width );
            element->SetWidth( width );
        break;

        case Urho3D::LM_VERTICAL:
            element->SetMinHeight( height );
            element->SetHeight( height );
        break;

        default:
            element->SetMinSize( width, height );
            element->SetSize( width, height );
        break;
    }

}


// Find the elements type and do stuff according to element type
void UIGame::findUIType( Urho3D::UIElement* ele ) {

    if( Urho3D::BorderImage* tmp = dynamic_cast<Urho3D::BorderImage*>( ele )  ) {
        if( Urho3D::Button* tmp2 = dynamic_cast<Urho3D::Button*>( ele )  ) {
            if( Urho3D::DropDownList* tmp3 = dynamic_cast<Urho3D::DropDownList*>( ele ) ) {
                int width = 0;
                int height = 0;
                for( int i = 0; i < tmp3->GetItems().Size(); ++i ) {
                    findUIType(tmp3->GetItems()[i]);
                    width = std::max( tmp3->GetItems()[i]->GetWidth(), width );
                    height = std::max( tmp3->GetItems()[i]->GetHeight(), height );
                }
                tmp3->SetMinSize(width, height);
                tmp3->SetSize(width, height);
            }
            else if( Urho3D::Menu* tmp3 = dynamic_cast<Urho3D::Menu*>( ele ) ) {
            }
            else { // Button
            }
        }
        else if(Urho3D::CheckBox* tmp2 = dynamic_cast<Urho3D::CheckBox*>( ele )) {

        }

        else if(Urho3D::Cursor* tmp2 = dynamic_cast<Urho3D::Cursor*>( ele )) {

        }

        else if(Urho3D::LineEdit* tmp2 = dynamic_cast<Urho3D::LineEdit*>( ele )) {

        }

        else if(Urho3D::Slider* tmp2 = dynamic_cast<Urho3D::Slider*>( ele )) {

        }

        else if(Urho3D::Window* tmp3 = dynamic_cast<Urho3D::Window*>( ele )) {
            if(Urho3D::View3D* tmp3 = dynamic_cast<Urho3D::View3D*>( ele )) {

            }
            else { // Window
            }

        }
        else { // borderImage

        }

    }

    else if(Urho3D::ScrollBar* tmp = dynamic_cast<Urho3D::ScrollBar*>( ele )) {

    }

    else if(Urho3D::ScrollView* tmp = dynamic_cast<Urho3D::ScrollView*>( ele )) {
        if(Urho3D::ListView* tmp = dynamic_cast<Urho3D::ListView*>( ele )) {

        }
        else {

        }


    }

    else if(Urho3D::Sprite* tmp = dynamic_cast<Urho3D::Sprite*>( ele )) {


    }

    else if(Urho3D::Text* tmp = dynamic_cast<Urho3D::Text*>( ele )) {
        tmp->SetMinSize(0,0);
// There is probably a lot smarter way to do this, but if the fontsize is same
// this does nothing. Since we already zeroed the text element earlier, this means
// the whole text will be 0 pixel size otherwise.
        tmp->SetFont(tmp->GetFont(), fontSize_ - 1 );
        tmp->SetFont(tmp->GetFont(), fontSize_ );

        tmp->SetMinSize( tmp->GetSize() );
    }

    else if(Urho3D::ToolTip* tmp = dynamic_cast<Urho3D::ToolTip*>( ele ) ) {

    }
    else { // UIElement

    }

}

[/code]

This code assumes that every type that has children does not contain things on their own. Also basically the only thing it does is change fonts size to an object. It doesn't handle position changes according to resolution, since I am only using elements in corners and edges nor it handles images neither.

Anyways do what you want with it. Oh and I am using c++11 autos, so c++11 must be used for the code to work.

-------------------------

