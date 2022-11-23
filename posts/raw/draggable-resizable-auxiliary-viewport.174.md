Mike | 2017-01-02 00:58:38 UTC | #1

Code sample to create a draggable/resizable auxiliary viewport.

Steps:
    - Create a Window
    - Subscribe to DragMove event
    - Apply Window's position/size to viewport
Note that I've assumed that using DragMove event is better than using Update event.

Can be tested with example 09_MultipleViewports.

Lua
[spoiler]At the end of SetupViewports():
[code]
	-- Create an invisible/draggable/resizable Window for Viewport#1
	camWindow = ui.root:CreateChild("Window", "CamWindow")
	local rect = renderer:GetViewport(1).rect -- Get Viewport#1's IntRect
	camWindow:SetPosition(rect.left, rect.top)
	camWindow:SetSize(rect.size)
	ui.root.defaultStyle = cache:GetResource("XMLFile", "UI/DefaultStyle.xml")
	camWindow:SetStyleAuto()
	camWindow.imageRect = IntRect(48, 16, 64, 32) -- Apply a transparent frame
	if GetPlatform() == "Android" or GetPlatform() == "iOS" then camWindow.resizeBorder = IntRect(20, 20, 20, 20) end -- Increase resize borders on mobiles to ease edges' grabbing
	camWindow.opacity = 0.5 -- Hide Window (partially or fully)
	camWindow.movable = true
	camWindow.resizable = true
	-- Subscribe to DragMove event
	SubscribeToEvent(camWindow, "DragMove", "HandleDragMoveViewport")
	-- Create a mouse cursor
	input.mouseVisible = true
	local style = cache:GetResource("XMLFile", "UI/DefaultStyle.xml")
	local cursor = ui.root:CreateChild("Cursor")
	cursor:SetStyleAuto(style)
	ui.cursor = cursor
	cursor:SetPosition(graphics.width / 2, graphics.height / 2)
[/code]
At the end of file:
[code]
function HandleDragMoveViewport(eventType, eventData)
	local draggedElement = eventData:GetPtr("UIElement", "Element") -- Get the dragged UI element (camWindow)
	local posX=draggedElement.position.x -- Get current Window left position
	local posY=draggedElement.position.y -- Get current Window top position
	renderer:GetViewport(1):SetRect(IntRect(posX, posY, posX + draggedElement.width, posY + draggedElement.height))
end
[/code][/spoiler]

AngelScript
[spoiler]At the end of SetupViewports():
[code]
	// Create an invisible/draggable/resizable Window for Viewport#1
	Window@ camWindow = ui.root.CreateChild("Window", "CamWindow");
	IntRect rect = renderer.viewports[1].rect; // Get Viewport#1's IntRect
	camWindow.SetPosition(rect.left, rect.top);
	camWindow.SetSize(rect.width, rect.height); // rect.size doesn't work
	ui.root.defaultStyle = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
	camWindow.SetStyleAuto();
	//camWindow.imageRect = IntRect(48, 16, 64, 32); // TODO: Apply a transparent frame (currently don't know how to access Window's BorderImage from script)
	if (GetPlatform() == "Android" || GetPlatform() == "iOS") camWindow.resizeBorder = IntRect(20, 20, 20, 20); // Increase resize borders on mobiles to ease edges' grabbing
	camWindow.opacity = 0.5; // Hide Window (partially or fully)
	camWindow.movable = true;
	camWindow.resizable = true;
	// Subscribe to drag events
	SubscribeToEvent(camWindow, "DragMove", "HandleDragMoveViewport");
	// Create a mouse cursor
	XMLFile@ style = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
	Cursor@ cursor = Cursor();
	cursor.SetStyleAuto(style);
	ui.cursor = cursor;
	cursor.SetPosition(graphics.width / 2, graphics.height / 2);
[/code]
At the end of file:
[code]
void HandleDragMoveViewport(StringHash eventType, VariantMap& eventData)
{
	UIElement@ draggedElement = eventData["Element"].GetPtr(); // Get the dragged UI element (camWindow)
	int posX=draggedElement.position.x; // Get current Window left position
	int posY=draggedElement.position.y; // Get current Window top position
	renderer.viewports[1].rect = IntRect(posX, posY, posX + draggedElement.width, posY + draggedElement.height);
}
[/code][/spoiler]

C++
[spoiler]In MultipleViewports.h:

- Add 'class Window;' to namespace Urho3D
- Add new function in private:
[code]
    /// Handle auxiliary viewport drag/resize.
    void HandleDragMoveViewport(StringHash eventType, VariantMap& eventData);
[/code]

In MultipleViewports.cpp:

Includes:
[code]
#include "Rect.h"
#include "UIElement.h"
#include "UIEvents.h"
#include "Window.h"
[/code]
At the end of MultipleViewports::SetupViewports()
[code]
	// Create an invisible/draggable/resizable Window for Viewport#1
	UI* ui = GetSubsystem<UI>();
	Window* camWindow = new Window(context_);
    ui->GetRoot()->AddChild(camWindow);
	IntRect rect = renderer->GetViewport(1)->GetRect(); // Get Viewport#1's IntRect
	camWindow->SetPosition(rect.left_, rect.top_);
	camWindow->SetSize(rect.Size());
	XMLFile* style = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");
	camWindow->SetStyleAuto(style);
	camWindow->SetImageRect(IntRect(48, 16, 64, 32)); // Apply a transparent frame
	if (GetPlatform() == "Android" || GetPlatform() == "iOS") camWindow->SetResizeBorder(IntRect(20, 20, 20, 20)); // Increase resize borders on mobiles to ease edges' grabbing
	camWindow->SetOpacity(0.5); // Hide Window (partially or fully)
	camWindow->SetMovable(true);
	camWindow->SetResizable(true);
	// Subscribe to DragMove event
	SubscribeToEvent(camWindow, E_DRAGMOVE, HANDLER(MultipleViewports, HandleDragMoveViewport));
	// Create a mouse cursor
    SharedPtr<Cursor> cursor(new Cursor(context_));
    cursor->SetStyleAuto(style);
    ui->SetCursor(cursor);
    cursor->SetPosition(graphics->GetWidth() / 2, graphics->GetHeight() / 2);
[/code]
At the end of file:
[code]
void MultipleViewports::HandleDragMoveViewport(StringHash eventType, VariantMap& eventData)
{
	UIElement* draggedElement = static_cast<UIElement*>(eventData["Element"].GetPtr()); // Get the dragged UI element (camWindow)
	int posX=draggedElement->GetPosition().x_; // Get current Window left position
	int posY=draggedElement->GetPosition().y_; // Get current Window top position
	GetSubsystem<Renderer>()->GetViewport(1)->SetRect(IntRect(posX, posY, posX + draggedElement->GetWidth() , posY + draggedElement->GetHeight()));
}
[/code][/spoiler]

EDIT: added optional transparent Border frame and made edges' grabbing easier on mobiles.

-------------------------

