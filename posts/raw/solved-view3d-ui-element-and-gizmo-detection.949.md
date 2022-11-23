scorvi | 2017-01-02 01:04:20 UTC | #1

i am currently porting some angelscript code to c++ and have a problem with the gizmo detection.

i am using the View3D UI Element to display my scene and this code  :
[code]		void GizmoScene3D::UseGizmo()
	{
		if (gizmo == NULL || !gizmo->IsEnabled() || epScene3D_->editMode == EDIT_SELECT)
		{
// 			StoreGizmoEditActions();
// 			previousGizmoDrag = false;
			return;
		}
		UI* ui = GetSubsystem<UI>();
		
		IntVector2 pos = ui->GetCursorPosition();
		UIElement* e = ui->GetElementAt(pos);

		if (e != epScene3D_->activeView)
			return;
		
		Ray cameraRay = epScene3D_->camera_->GetScreenRay((float)pos.x_, (float)pos.y_);
		float scale = gizmoNode->GetScale().x_;

		Input* input = GetSubsystem<Input>();
		// Recalculate axes only when not left-dragging
		bool drag = input->GetMouseButtonDown(MOUSEB_LEFT);
		if (!drag)
			CalculateGizmoAxes();
		
		gizmoAxisX->Update(cameraRay, scale, drag, epScene3D_->cameraNode_->GetPosition());
		gizmoAxisY->Update(cameraRay, scale, drag, epScene3D_->cameraNode_->GetPosition());
		gizmoAxisZ->Update(cameraRay, scale, drag, epScene3D_->cameraNode_->GetPosition());
...
...
[/code]

but the gizmo axis are not selected at all ...

Edit:
ok found the solution ... 
[code]
	void GizmoScene3D::UseGizmo()
	{
		if (gizmo == NULL || !gizmo->IsEnabled() || epScene3D_->editMode == EDIT_SELECT)
		{
			// 			StoreGizmoEditActions();
			// 			previousGizmoDrag = false;
			return;
		}
		UI* ui = GetSubsystem<UI>();

		IntVector2 pos = ui->GetCursorPosition();
		UIElement* e = ui->GetElementAt(pos);

		if (e != epScene3D_->activeView)
			return;

		const IntVector2& screenpos = epScene3D_->activeView->GetScreenPosition();
		float	posx = float(pos.x_ - screenpos.x_) / float(epScene3D_->activeView->GetWidth());
		float	posy = float(pos.y_ - screenpos.y_) / float(epScene3D_->activeView->GetHeight());

		Ray cameraRay = epScene3D_->camera_->GetScreenRay(posx, posy);
		float scale = gizmoNode->GetScale().x_;

		Input* input = GetSubsystem<Input>();
		// Recalculate axes only when not left-dragging
		bool drag = input->GetMouseButtonDown(MOUSEB_LEFT);
		if (!drag)
			CalculateGizmoAxes();

		gizmoAxisX->Update(cameraRay, scale, drag, epScene3D_->cameraNode_->GetPosition());
		gizmoAxisY->Update(cameraRay, scale, drag, epScene3D_->cameraNode_->GetPosition());
		gizmoAxisZ->Update(cameraRay, scale, drag, epScene3D_->cameraNode_->GetPosition());[/code]

-------------------------

