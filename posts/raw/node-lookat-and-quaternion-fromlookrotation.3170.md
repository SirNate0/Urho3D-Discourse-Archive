slapin | 2017-05-27 23:13:40 UTC | #1

when both LookAt anf FromLookRotation rotate node to reverse direction, where to look?
I need to rotate head of the mode lin direction of player or camera. I do this:

    void BTBlackboard::HandleSceneDrawableUpdateFinished(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
    {
            Node *head = node_->GetChild("head", true);
            Node *spine = node_->GetChild("spine02", true);
            Node *root = node_->GetChild("root", true);
            if (look_at_enabled && look_at) {
                    Node *lookat_target = look_at;
                    if (look_at->HasTag("player")) {
                            VariantMap vars = look_at->GetVars();
                            bool first_person = vars["first_persin"].GetBool();
                            if (first_person)
                                    lookat_target = (Node *) vars["camera_node"].GetPtr();
                            else {
                                    lookat_target = look_at->GetChild("head", true);
                            }
                    } else {
                            lookat_target = look_at->GetChild("head", true);
                    }
                    if (!lookat_target)
                            lookat_target = look_at;
                    URHO3D_LOGINFO("looking at: " + lookat_target->GetName() + " " + lookat_target->GetWorldPosition().ToString());
                    URHO3D_LOGINFO("from: " +  head->GetWorldPosition().ToString());
                    Quaternion prep;
                    Vector3 dir = -(lookat_target->GetWorldPosition() - node_->GetWorldPosition() - Vector3(0.0f, 0.7f, 0.0f));
                    URHO3D_LOGINFO("dir: " +  dir.ToString());
                    prep.FromLookRotation(dir, Vector3(0.0f, 1.0f, 0.0f));
                    Quaternion rot = root->GetWorldRotation();
    //              Quaternion head_initial = head->GetParent()->GetWorldRotation().Inv();
    //              Quaternion rot = spine->GetWorldRotation();
    ////            spine->SetWorldRotation(rot.Slerp(prep * Quaternion(0.0f, -180.0f, 0.0f), 0.5));
                    spine->SetWorldRotation(rot.Slerp(prep, 0.5));
    //              Quaternion rotl = head->GetWorldRotation();
    ////            head->SetWorldRotation(prep * Quaternion(0.0f, -180.0f, 0.0f));
    ///             Quaternion correction(-15.0f, 0.0f, 0.0f);
                    head->SetWorldRotation(prep);
    ////            head->LookAt(lookat_target->GetWorldPosition());

            }
    }

When code is written this way, it works. if I uncomment LookAt it looks in reverse direction.
Also if I remove minus sign from dir variable it looks in reverse, while it should not.
I remember using this functions without problems somewhere on 1.5. Probably I do something wrong.
Any ideas? (everything is done in world coordinates, so these absolutely should work. Are they?)

-------------------------

