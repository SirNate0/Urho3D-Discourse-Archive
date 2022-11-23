AntiLoxy | 2019-02-13 21:19:51 UTC | #1

All the problem is in the title.

    class FileControl : public UIElement
    {
        URHO3D_OBJECT(FileControl, UIElement)

    public:
        explicit FileControl(Context* context): UIElement(context)
        {
            lineEdit_ = CreateChild<LineEdit>("FC_LineEdit");
            lineEdit_->SetInternal(true);

            selectBtn_ = CreateChild<ButtonText>("FC_ButtonText");
            selectBtn_->SetInternal(true);
            selectBtn_->SetLabel("Select");

            SubscribeToEvent(selectBtn_, E_RELEASED, URHO3D_HANDLER(FileControl, HandleSelectButtonReleased));
        }

        static void RegisterObject(Context* context);

    private:
        void HandleSelectButtonReleased(StringHash eventType, VariantMap& eventData)
        {
            if (fileSelector_.NotNull())
            {
                fileSelector_.Reset();
            }

            fileSelector_ = MakeShared<FileSelector>(context_); // this line make the crash;
            fileSelector_->SetDefaultStyle(GetDefaultStyle());
        }

    private:
        SharedPtr<FileSelector> fileSelector_;
        ....
    };

I have the same code in Main class (subclass of Application) and all work fine...

-------------------------

AntiLoxy | 2019-02-15 20:27:05 UTC | #2

Oups sorry, error due to my fault.

You can delete this topic.

-------------------------

