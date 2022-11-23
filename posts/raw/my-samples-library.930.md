scorvi | 2019-01-15 14:56:15 UTC | #1

hey ho,

I decided to upload some of my Components / Objects that can extend the Urho3D engine a bit.
They are extracted from some of my current work but they are all in a WIP state, that i will edit on the way, so if you find a bug or find a better solution to that task please notify me ^^ 

I hope they are somewhat helpful for others and i would appreciate some feedback ... :slight_smile: 

added Samples:

* 01_AttributeInspector
* 02_OpenVGRenderer
* 03_NanoSVGRendering
* 05_HierarchyWindow
* 06_InGameEditor
* 07_NinjaSnowWar

to be added (have to extract them from my current work so it can take some time ... ) :

* Component preset manager 
* AppStateManager
* TranslationManager
* Database(sqlite)
* Social(Amazon/Google)
* UI AnalogStick
* EventTimer/ExperationTimer
* [url]http://soom.la/features/[/url]
* ASCII RogueLike Console

https://github.com/scorvi/Urho3DSamples

-------------------------

sabotage3d | 2017-01-02 01:04:10 UTC | #2

Awesome work man, can't wait to try them out :slight_smile:

-------------------------

vivienneanthony | 2017-01-02 01:04:10 UTC | #3

I will love to see the sqlite implementation.

-------------------------

GoogleBot42 | 2017-01-02 01:04:10 UTC | #4

[quote="vivienneanthony"]I will love to see the sqlite implementation.[/quote]

Me too!  This looks really auesome!

UI analog stick would be cool too!  Will it scale based on pixel density (so it isn't microscopic on retina displays :slight_smile: )?

I have never heard of soonla.  It looks quite interesting.  I might use it.

Great work so far!

-------------------------

Faizol | 2017-01-02 01:04:10 UTC | #5

I don't know much about soom.la to say anything about it, but just to be on the precaution side while trying to generate discussion, how safe it is to use a third party payment system like soom.la?
I've stumbled upon this link on reddit; "How two third of my AdMob revenue is stolen."
[reddit.com/r/gamedev/comment ... is_stolen/](http://www.reddit.com/r/gamedev/comments/2mef9h/how_two_third_of_my_admob_revenue_is_stolen/)
where the said library provides the tainted binary download while the source isn't compilable.

-------------------------

GoogleBot42 | 2017-01-02 01:04:10 UTC | #6

[quote="Faizol"]I don't know much about soom.la to say anything about it, but just to be on the precaution side while trying to generate discussion, how safe it is to use a third party payment system like soom.la?
I've stumbled upon this link on reddit; "How two third of my AdMob revenue is stolen."
[reddit.com/r/gamedev/comment ... is_stolen/](http://www.reddit.com/r/gamedev/comments/2mef9h/how_two_third_of_my_admob_revenue_is_stolen/)
where the said library provides the tainted binary download while the source isn't compilable.[/quote]

Interesting point.  You can never be too careful... The project is open source under the MIT licience so that does help.

EDIT: Never mind open source doesn't mean anything... I checked your link and those were open source too...  :frowning:

EDIT2: Hmmm not entirely true, open source is still safer than binaries, their are two admob versions mentioned by the author and one of them isn't even open source their other doesn't compile because code is missing...  But one can never be too careful still.  It is people like those two that released the bad libraries that give open source a bad name.  :frowning:   :angry:

-------------------------

rogerdv | 2017-01-02 01:04:13 UTC | #7

Im interested in the state Manager!

-------------------------

thebluefish | 2017-01-02 01:04:13 UTC | #8

Really confused me with the "OpenVG" render sample vs the "NanoSVG" sample. Turns out NanoVG and NanoSVG are two separate things made by the same person. No idea why you called it "OpenVG" when it's "NanoVG", maybe to be less confusing?

Still, nice release! I've been meaning to implement [url=https://bitbucket.org/duangle/oui-blendish/src]oui-blending[/url] once I'm done with my libRocket port. This will make it much easier :slight_smile:

-------------------------

GoogleBot42 | 2017-01-02 01:04:13 UTC | #9

[quote="thebluefish"]Really confused me with the "OpenVG" render sample vs the "NanoSVG" sample. Turns out NanoVG and NanoSVG are two separate things made by the same person. No idea why you called it "OpenVG" when it's "NanoVG", maybe to be less confusing?[/quote]

I was confused too.... Seems that OpenVG is backed by khronos.org and NanoSVG is a github project.  Based on the names I would guess that NanoSVG is smaller and OpenVG may be faster?  But IDK.  :stuck_out_tongue:

-------------------------

scorvi | 2017-01-02 01:04:14 UTC | #10

sry, i dont know why i did that ... ?? but i just fixed that :slight_smile:

-------------------------

Faizol | 2017-01-02 01:04:14 UTC | #11

It would be awesome if some of the samples/utilities could be merged into the Urho3D master branch (after some modifications - if needed). Database, social and virtual currency/in app billing are among much sought after features for a game engine. As per virtual currency and security in using a third party library, the more users use it, the more people can audit the library, thus the slimmer chances of fraud to happen. 

Is it advisable to have a wrapper for in-app billing libraries in Urho3D? There are other in-app billing libraries like [github.com/onepf/OpenIAB](https://github.com/onepf/OpenIAB) and a few others that could be used as options should one doesn't want to use soom.la.

-------------------------

thebluefish | 2017-01-02 01:04:18 UTC | #12

I can't use Github where I'm at, but I will be submitting some changes soon. At the moment, I'm working with the 06_InGameEditor sample.

The primary things that I changed in my copy:

- Changing macros to templates. C-style macros are dangerous at best, and a nightmare at worst.
- Changing actions into events. Events are tremendously more scale-able, and allow better readability. This is done to better support the plugin system concept. Creating a menu item now looks like the following:
[code]menubar_->CreateMenuItem("File", "Exit Editor", HANDLER(EditorState, HandleMenuBarAction_File_Exit));[/code]
- Changing the heirarchy window to work off a node instead of the root scene. By default it will use the scene root (scene is technically a node). This is done to allow in-editor visuals, such as a grid and 3-axis, without seeing/modifying those elements within the editor.
- Changed CreateMenuItem to replace menuTitle with a Menu object. This way, there's no conflicts with items that have the same name. While that generally isn't a problem, why go through the effort of searching strings where you will have the menu objects anyways?
- Changed CreateMenu to not return an existing Menu if one has the same name. Done for the same reason as above.
- Created a function, CreateSubMenu, that allows adding drop-down menus. Similar to above, the parent menu is passed in.

Of course there will be more as I play around with it :slight_smile:

-------------------------

scorvi | 2017-01-02 01:04:19 UTC | #13

[quote="thebluefish"]I can't use Github where I'm at, but I will be submitting some changes soon. At the moment, I'm working with the 06_InGameEditor sample.

The primary things that I changed in my copy:

- Changing macros to templates. C-style macros are dangerous at best, and a nightmare at worst.
- Changing actions into events. Events are tremendously more scale-able, and allow better readability. This is done to better support the plugin system concept. Creating a menu item now looks like the following:
[code]menubar_->CreateMenuItem("File", "Exit Editor", HANDLER(EditorState, HandleMenuBarAction_File_Exit));[/code]
- Changing the heirarchy window to work off a node instead of the root scene. By default it will use the scene root (scene is technically a node). This is done to allow in-editor visuals, such as a grid and 3-axis, without seeing/modifying those elements within the editor.
- Changed CreateMenuItem to replace menuTitle with a Menu object. This way, there's no conflicts with items that have the same name. While that generally isn't a problem, why go through the effort of searching strings where you will have the menu objects anyways?
- Changed CreateMenu to not return an existing Menu if one has the same name. Done for the same reason as above.
- Created a function, CreateSubMenu, that allows adding drop-down menus. Similar to above, the parent menu is passed in.

Of course there will be more as I play around with it :slight_smile:[/quote]


nice ^^ can you make a pull request for that ? 

i uploaded my IDE, that cannot do anything yet. so help is appreciated and i will add your changes to it too.

-------------------------

thebluefish | 2017-01-02 01:04:21 UTC | #14

Git is still broken for me on this machine :frowning:

For certain reasons I want to restrict which items get added to the components list, so I am manually adding components to the list instead of using the built-in categories. I have made some additional updates as well, but my editor is not yet complete and there is still plenty of stuff to do.

ToolbarUI.h:
[code]
/*!
 * /file ToolBarUI.h
 *
 * /author vitali
 * /date Februar 2015
 *
 * 
 */

#pragma once

#include <Urho3D/Urho3D.h>
#include <Urho3D/UI/UIElement.h>
#include <Urho3D/UI/BorderImage.h>

namespace Urho3D
{

	EVENT(E_TOOLBARTOGGLE, ToolBarToggle)
	{
		PARAM(P_CHECKBOX, Checkbox);              // Checkbox pointer 
	}

	class BorderImage;
	class XMLFile;
	class Menu;
	class Window;
	class Text;
	class ScrollBar;
	/// /todo use dirty masks
	class ToolBarUI : public BorderImage
	{
		OBJECT(ToolBarUI);
	public:
		ToolBarUI(Context* context);
		virtual ~ToolBarUI();
		static void RegisterObject(Context* context);
		static ToolBarUI* Create(UIElement* context, const String& idname, XMLFile* iconStyle, const String& baseStyle ="ToolBarToggle", int width = 0, int height = 41, XMLFile* defaultstyle = NULL);

		// handler: will provide E_TOGGLED event to children if they do not specify their own
		UIElement*	CreateGroup(const String& name, LayoutMode layoutmode = LM_HORIZONTAL);
		UIElement*	CreateToolBarToggle(const String& title, UIElement* group, Urho3D::EventHandler* handler = 0);
		UIElement*	CreateToolBarToggle(const String& title, Urho3D::EventHandler* handler = 0);
		UIElement*	CreateToolBarIcon(UIElement* element);
		UIElement*	CreateToolTip(UIElement* parent, const String& title, const IntVector2& offset);
		UIElement*  CreateToolBarSpacer(int width);

		// By default groups will require at least one element to be selected
		void SetRequireSelection(UIElement* group, bool requireSelection = true);

		void SetIconStyle(XMLFile* iconStyle) { iconStyle_ = iconStyle; }
		void SetBaseStyle(const String& baseStyle) { baseStyle_ = baseStyle; }
	protected:
		void FinalizeGroupHorizontal(UIElement* group, const String& baseStyle);
	
		void HandleToolbarToggle(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);

		SharedPtr< XMLFile> iconStyle_;
		/// Horizontal scroll bar.
		SharedPtr<ScrollBar> horizontalScrollBar_;
		String baseStyle_;
	private:
	};
}
[/code]

ToolbarUI.cpp:
[code]
#include "ToolBarUI.h"

#include <Urho3D/Urho3D.h>
#include <Urho3D/Core/Context.h>
#include <Urho3D/UI/BorderImage.h>
#include <Urho3D/UI/UI.h>
#include <Urho3D/UI/Menu.h>
#include <Urho3D/Math/Rect.h>
#include <Urho3D/UI/Text.h>
#include <Urho3D/UI/Window.h>
#include <Urho3D/Input/InputEvents.h>
#include <Urho3D/UI/UIEvents.h>

#include <Urho3D/UI/CheckBox.h>
#include <Urho3D/UI/ToolTip.h>
#include <Urho3D/UI/ScrollBar.h>

namespace Urho3D
{


	ToolBarUI* ToolBarUI::Create(UIElement* parent, const String& idname, XMLFile* iconStyle, const String& baseStyle, int width/*=0*/, int height /*= 21*/, XMLFile* defaultstyle /*= NULL*/)
	{
		ToolBarUI* menubar = parent->CreateChild<ToolBarUI>(idname);
		//menubar->SetStyle("Window",styleFile);
		if (defaultstyle)
			menubar->SetDefaultStyle(defaultstyle);
		menubar->SetStyleAuto();
		if (width > 0)
			menubar->SetFixedWidth(width);
		else
			menubar->SetFixedWidth(parent->GetMinWidth());
		menubar->SetFixedHeight(height);
		menubar->iconStyle_ = iconStyle;
		menubar->baseStyle_ = baseStyle;
		return menubar;
	}

	void ToolBarUI::RegisterObject(Context* context)
	{
		context->RegisterFactory<ToolBarUI>();
		COPY_BASE_ATTRIBUTES(BorderImage);
		UPDATE_ATTRIBUTE_DEFAULT_VALUE("Is Enabled", true);

	}

	ToolBarUI::~ToolBarUI()
	{

	}

	ToolBarUI::ToolBarUI(Context* context) : BorderImage(context)
	{
		bringToFront_ = true;
		clipChildren_ = true;
		SetEnabled(true);
		SetLayout(LM_HORIZONTAL, 4, IntRect(8, 4, 4, 8));
		SetAlignment(HA_LEFT, VA_TOP);
// 		horizontalScrollBar_ = CreateChild<ScrollBar>("TB_HorizontalScrollBar");
// 		horizontalScrollBar_->SetInternal(true);
// 		horizontalScrollBar_->SetAlignment(HA_LEFT, VA_BOTTOM);
// 		horizontalScrollBar_->SetOrientation(O_HORIZONTAL);

	}

	UIElement* ToolBarUI::CreateGroup(const String& name, LayoutMode layoutmode)
	{
		UIElement* group = GetChild(name);
		if (group)
			return group;

		group = new UIElement(context_);
		group->SetName(name);
		group->SetDefaultStyle(GetDefaultStyle());
		group->SetLayoutMode(layoutmode);
		group->SetAlignment(HA_LEFT,VA_CENTER);

		AddChild(group);
		return group;
	}

	UIElement* ToolBarUI::CreateToolBarToggle(const String& title, UIElement* group, Urho3D::EventHandler* handler)
	{
		if (group)
		{
			CheckBox* toggle = new CheckBox(context_);
			toggle->SetName(title);
			toggle->SetDefaultStyle(GetDefaultStyle());
			toggle->SetStyle(baseStyle_);
			toggle->SetOpacity(0.7f);
			CreateToolBarIcon(toggle);
			CreateToolTip(toggle, title, IntVector2(toggle->GetWidth() + 10, toggle->GetHeight() - 10));

			group->AddChild(toggle);
			FinalizeGroupHorizontal(group, baseStyle_);
			
			SubscribeToEvent(toggle, Urho3D::E_TOGGLED, HANDLER(ToolBarUI, HandleToolbarToggle));

			if (handler)
				toggle->SubscribeToEvent(toggle, Urho3D::E_TOGGLED, handler);

			return toggle;
		}
		return NULL;
	}

	UIElement* ToolBarUI::CreateToolBarToggle(const String& title, Urho3D::EventHandler* handler)
	{
		CheckBox* toggle = new CheckBox(context_);
		toggle->SetName(title);
		toggle->SetDefaultStyle(GetDefaultStyle());
		toggle->SetStyle(baseStyle_);
		toggle->SetOpacity(0.7f);

		CreateToolBarIcon(toggle);
		CreateToolTip(toggle, title, IntVector2(toggle->GetWidth() + 10, toggle->GetHeight() - 10));
		AddChild(toggle);

		toggle->SubscribeToEvent(toggle, Urho3D::E_TOGGLED, handler);

		return toggle;
	}

	UIElement* ToolBarUI::CreateToolBarIcon(UIElement* element)
	{
		BorderImage* icon = new BorderImage(context_);
		icon->SetName("Icon");
		icon->SetDefaultStyle(iconStyle_);
		icon->SetStyle(element->GetName());
		icon->SetFixedSize(GetHeight() - 11, GetHeight() - 11);
		icon->SetAlignment(HA_CENTER, VA_CENTER);
		element->AddChild(icon);
		return icon;
	}

	UIElement* ToolBarUI::CreateToolTip(UIElement* parent, const String& title, const IntVector2& offset)
	{
		ToolTip* toolTip = parent->CreateChild<ToolTip>("ToolTip");
		toolTip->SetPosition(offset);

		BorderImage* textHolder = toolTip->CreateChild<BorderImage>("BorderImage");
		textHolder->SetStyle("ToolTipBorderImage");

		Text* toolTipText = textHolder->CreateChild<Text>("Text");
		toolTipText->SetStyle("ToolTipText");
		toolTipText->SetText(title);

		return toolTip;
	}

	void ToolBarUI::FinalizeGroupHorizontal(UIElement* group, const String& baseStyle)
	{
		int width = 0;
		for (unsigned int i = 0; i < group->GetNumChildren(); ++i)
		{
			UIElement* child = group->GetChild(i);
			width += child->GetMinWidth();
			if (i == 0 && i < group->GetNumChildren() - 1)
				child->SetStyle(baseStyle + "GroupLeft");
			else if (i < group->GetNumChildren() - 1)
				child->SetStyle(baseStyle + "GroupMiddle");
			else
				child->SetStyle(baseStyle + "GroupRight");
			child->SetFixedSize(GetHeight() - 6, GetHeight() - 6);
		}
		/// /todo SetMaxSize(group->GetSize()) does not work !? 
		//group->SetMaxSize(group->GetSize());
		group->SetFixedWidth(width);
	}

	UIElement* ToolBarUI::CreateToolBarSpacer(int width)
	{
		UIElement* spacer = new UIElement(context_);
		spacer->SetFixedWidth(width);
		AddChild(spacer);
		return spacer;
	}

	void ToolBarUI::SetRequireSelection(UIElement* group, bool requireSelection)
	{
		group->SetVar("RquireSelection", requireSelection);
	}

	void ToolBarUI::HandleToolbarToggle(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
	{
		using namespace Toggled;

		CheckBox* checkbox = static_cast<CheckBox*>(eventData[P_ELEMENT].GetPtr());
		bool state = eventData[P_STATE].GetBool();

		UIElement* parent = checkbox->GetParent();

		if (parent)
		{
			auto children = parent->GetChildren();
			for (auto itr = children.Begin(); itr != children.End(); itr++)
			{
				CheckBox* child = static_cast<CheckBox*>(itr->Get());
				
				bool shouldBeChecked = false;
				if (child == checkbox)
				{
					shouldBeChecked = true;
					Urho3D::Variant variant = child->GetVar("RquireSelection");
					if (variant != NULL && !state)
					{
						shouldBeChecked = variant.GetBool();
					}
				}
				
				UnsubscribeFromEvent(child, E_TOGGLED);
				child->SetChecked(shouldBeChecked);
				SubscribeToEvent(child, E_TOGGLED, HANDLER(ToolBarUI, HandleToolbarToggle));
			}
		}
	}
}
[/code]

MenuBarUI.h:
[code]
/*!
 * /file MenuBarUI.h
 *
 * /author vitali
 * /date Februar 2015
 *
 *
 */

#pragma once

#include <Urho3D/Urho3D.h>
#include <Urho3D/UI/UIElement.h>
#include <Urho3D/UI/BorderImage.h>

namespace Urho3D
{

	/// Menu selected.
	//EVENT(E_MENUBAR_ACTION, MenuBarAction)
	//{
	//	PARAM(P_ACTION, Action);              // stringhash 
	//}
	class BorderImage;
	class XMLFile;
	class Menu;
	class Window;
	class Text;
	class EventHandler;

	/// /todo use dirty masks
	class MenuBarUI : public BorderImage
	{
		OBJECT(MenuBarUI);
	public:
		MenuBarUI(Context* context);
		virtual ~MenuBarUI();
		static void RegisterObject(Context* context);
		static MenuBarUI* Create(UIElement* context, const String& idname, int width = 0, int height = 21, XMLFile* defaultstyle = NULL);

		Menu* CreateMenu(const String& title);
		Menu* CreateSubMenu(const Menu* parent, const String& title, int accelKey = 0, int accelQual = 0);
		Menu* CreateMenuItem(const Menu* parent, const String& title, Urho3D::EventHandler* handler = 0, int accelKey = 0, int accelQual = 0, bool addToQuickMenu = true, String quickMenuText = "");
		Menu* CreateIconizedMenuItem(const Menu* parent, const String& title, const String& iconStyle = "", Urho3D::EventHandler* handler = 0, int accelKey = 0, int accelQual = 0, bool addToQuickMenu = true, String quickMenuText = "");

		

	protected:
		void FinalizedPopupMenu(Window* popup);
		void IconizeUIElement(UIElement* element, const String& iconType);
		Text* CreateAccelKeyText(int accelKey, int accelQual);

		void HandleMenuSelected(StringHash eventType, VariantMap& eventData);
	private:
	};
}
[/code]

MenuBarUI.cpp:
[code]
#include "MenuBarUI.h"
#include "UIGlobals.h"

#include <Urho3D/Urho3D.h>
#include <Urho3D/Core/Context.h>
#include <Urho3D/UI/BorderImage.h>
#include <Urho3D/UI/UI.h>
#include <Urho3D/UI/Menu.h>
#include <Urho3D/Math/Rect.h>
#include <Urho3D/UI/Text.h>
#include <Urho3D/UI/Window.h>
#include <Urho3D/Input/InputEvents.h>
#include <Urho3D/UI/UIEvents.h>
#include <Urho3D/Resource/ResourceCache.h>

namespace Urho3D
{
	

	MenuBarUI* MenuBarUI::Create(UIElement* parent, const String& idname, int width/*=0*/, int height /*= 21*/, XMLFile* defaultstyle /*= NULL*/)
	{
		MenuBarUI* menubar = parent->CreateChild<MenuBarUI>(idname);
		//menubar->SetStyle("Window",styleFile);
		if (defaultstyle)
			menubar->SetDefaultStyle(defaultstyle);
		menubar->SetStyleAuto();
		if (width > 0)
			menubar->SetFixedWidth(width);		
		else
			menubar->SetFixedWidth(parent->GetWidth());
		menubar->SetFixedHeight(height);

		return menubar;
	}

	void MenuBarUI::RegisterObject(Context* context)
	{
		context->RegisterFactory<MenuBarUI>();
		COPY_BASE_ATTRIBUTES(BorderImage);
		UPDATE_ATTRIBUTE_DEFAULT_VALUE("Is Enabled", true);

	}

	MenuBarUI::~MenuBarUI()
	{

	}

	MenuBarUI::MenuBarUI(Context* context) : BorderImage(context)
	{
		bringToFront_ = true;
		clipChildren_ = true;
		SetEnabled(true);
		SetLayout(LM_HORIZONTAL);
		SetAlignment(HA_LEFT, VA_TOP);
	}

	Menu* MenuBarUI::CreateMenu(const String& title)
	{
		Menu* menu = new Menu(context_);
		menu->SetName(title);
		menu->SetStyleAuto(GetDefaultStyle());
		menu->SetLayout(LM_HORIZONTAL, 0, IntRect(8, 2, 8, 2));

		// Create Text Label
		Text* menuText =new Text(context_);
		menuText->SetName(title + "_text");
		menu->AddChild(menuText);
		menuText->SetStyle("EditorMenuText");
		menuText->SetText(title);

		// set menubutton size
		menu->SetFixedWidth(menu->GetWidth());

		// create popup
		Window* popup = new  Window(context_);
		popup->SetName(title + "_popup");
		popup->SetLayout(LM_VERTICAL, 1, IntRect(2, 6, 2, 6));
		popup->SetStyleAuto(GetDefaultStyle());
		menu->SetPopup(popup);
		menu->SetPopupOffset(IntVector2(0, menu->GetHeight()));

		AddChild(menu);	
		return menu;
	}

	Menu* MenuBarUI::CreateSubMenu(const Menu* parent, const String& title, int accelKey, int accelQual)
	{
		Menu* menu = CreateMenuItem(parent, title, 0, accelKey, accelQual);

		// create popup
		Window* popup = new  Window(context_);
		popup->SetName(title + "_popup");
		popup->SetLayout(LM_VERTICAL, 1, IntRect(2, 6, 2, 6));
		popup->SetStyleAuto(GetDefaultStyle());
		menu->SetPopup(popup);
		menu->SetPopupOffset(IntVector2(0, menu->GetHeight()));

		FinalizedPopupMenu((Window*)parent->GetPopup());

		return menu;
	}

	Menu* MenuBarUI::CreateMenuItem(const Menu* parent, const String& title, Urho3D::EventHandler* handler, int accelKey, int accelQual, bool addToQuickMenu, String quickMenuText)
	{
		Window*  popup = (Window*)parent->GetPopup();
		if (!popup)
			return NULL;

		// create Menu item
		Menu* menuItem = new Menu(context_);
		menuItem->SetName(title);
		menuItem->SetStyleAuto(GetDefaultStyle());
		menuItem->SetLayout(LM_HORIZONTAL, 0, IntRect(8, 2, 8, 2));
		if (handler)
		{
			menuItem->SetVar(HANDLER_VAR, handler);
		}
		if (accelKey > 0)
			menuItem->SetAccelerator(accelKey, accelQual);

		// Create Text Label
		Text* menuText = new Text(context_);
		menuText->SetName(title + "_text");
		menuItem->AddChild(menuText);
		menuText->SetStyle("EditorMenuText");
		menuText->SetText(title);

		if (accelKey != 0)
		{
			UIElement* spacer = new UIElement(context_);
			spacer->SetMinWidth(menuText->GetIndentSpacing());
			spacer->SetHeight(menuText->GetHeight());

			menuItem->AddChild(spacer);
			menuItem->AddChild(CreateAccelKeyText(accelKey, accelQual));
		}

		popup->AddChild(menuItem);
		SubscribeToEvent(menuItem, E_MENUSELECTED, HANDLER(MenuBarUI, HandleMenuSelected));
		/// /todo use dirty masks
		FinalizedPopupMenu(popup);

		return menuItem;
	}

	Menu* MenuBarUI::CreateIconizedMenuItem(const Menu* parent, const String& title, const String& iconStyle, Urho3D::EventHandler* handler, int accelKey, int accelQual, bool addToQuickMenu, String quickMenuText)
	{
		Menu* menu = CreateMenuItem(parent, title, handler, accelKey, accelQual, addToQuickMenu, quickMenuText);

		IconizeUIElement(menu->GetChild(Urho3D::String(title + "_text")), iconStyle.Empty() ? title : iconStyle);

		return menu;
	}

	void MenuBarUI::FinalizedPopupMenu(Window* popup)
	{
		// Find the maximum menu text width
		Vector<SharedPtr<UIElement> > children = popup->GetChildren();

		int maxWidth = 0;

		for (unsigned int i = 0; i < children.Size(); ++i)
		{
			UIElement* element = children[i];
			if (element->GetType() != MENU_TYPE)    // Skip if not menu item
				continue;

			int width = element->GetChild(0)->GetWidth();
			if (width > maxWidth)
				maxWidth = width;
		}

		// Adjust the indent spacing to slightly wider than the maximum width
		maxWidth += 20;
		for (unsigned int i = 0; i < children.Size(); ++i)
		{
			UIElement* element = children[i];
			if (element->GetType() != MENU_TYPE)
				continue;
			Menu* menu = (Menu*)element;

			Text* menuText = (Text*)menu->GetChild(0);
			if (menuText->GetNumChildren() == 1)    // Skip if menu text does not have accel
				menuText->GetChild(0)->SetIndentSpacing(maxWidth);

			// Adjust the popup offset taking the indentation into effect
			if (menu->GetPopup() != NULL)
				menu->SetPopupOffset(IntVector2(menu->GetWidth(), 0));
		}
	}

	void MenuBarUI::IconizeUIElement(UIElement* element, const String& iconType)
	{
		Urho3D::ResourceCache* cache = GetSubsystem<Urho3D::ResourceCache>();

		Urho3D::XMLFile* iconStyle = cache->GetResource<Urho3D::XMLFile>("UI/IDEIcons.xml");

		BorderImage* icon = (BorderImage*)element->GetChild(Urho3D::String("Icon"));

		if (!iconType.Empty())
		{
			if (icon)
			{
				icon->Remove();
			}

			if (element->GetVar(INDENT_MODIFIED_BY_ICON_VAR).GetBool())
			{
				element->SetIndent(0);
			}

			if (element->GetIndent() == 0)
			{
				element->SetIndent(1);
				element->SetVar(INDENT_MODIFIED_BY_ICON_VAR, true);
			}

			if (!icon)
			{
				icon = new BorderImage(context_);
				icon->SetIndent(element->GetIndent() - 1);
				icon->SetFixedSize(element->GetIndentWidth() - 2, 14);
				element->InsertChild(0, icon);
			}

			if (!icon->SetStyle(iconType, iconStyle))
			{
				icon->SetStyle("Unknown", iconStyle);
			}
			icon->SetColor(Color(1, 1, 1, 1));
		}
	}

	Text* MenuBarUI::CreateAccelKeyText( int accelKey, int accelQual)
	{
		Text* accelKeyText = new Text(context_);
		accelKeyText->SetDefaultStyle(GetDefaultStyle());
		accelKeyText->SetStyle("EditorMenuText");
		accelKeyText->SetTextAlignment(HA_RIGHT);

		String text;
		if (accelKey == KEY_DELETE)
			text = "Del";
		else if (accelKey == KEY_SPACE)
			text = "Space";
		// Cannot use range as the key constants below do not appear to be in sequence
		else if (accelKey == KEY_F1)
			text = "F1";
		else if (accelKey == KEY_F2)
			text = "F2";
		else if (accelKey == KEY_F3)
			text = "F3";
		else if (accelKey == KEY_F4)
			text = "F4";
		else if (accelKey == KEY_F5)
			text = "F5";
		else if (accelKey == KEY_F6)
			text = "F6";
		else if (accelKey == KEY_F7)
			text = "F7";
		else if (accelKey == KEY_F8)
			text = "F8";
		else if (accelKey == KEY_F9)
			text = "F9";
		else if (accelKey == KEY_F10)
			text = "F10";
		else if (accelKey == KEY_F11)
			text = "F11";
		else if (accelKey == KEY_F12)
			text = "F12";
		else if (accelKey == SHOW_POPUP_INDICATOR)
			text = ">";
		else
			text.AppendUTF8(accelKey);
		if ((accelQual & QUAL_ALT) > 0)
			text = "Alt+" + text;
		if ((accelQual & QUAL_SHIFT ) > 0)
			text = "Shift+" + text;
		if ((accelQual & QUAL_CTRL) > 0)
			text = "Ctrl+" + text;
		accelKeyText->SetText(text);

		return accelKeyText;
	}

	void MenuBarUI::HandleMenuSelected(StringHash eventType, VariantMap& eventData)
	{
		using namespace MenuSelected;

		UIElement* element = static_cast<UIElement*>(eventData[P_ELEMENT].GetPtr());
		if (element && element->GetType() == MENU_TYPE)
		{
			const Variant& handler = element->GetVar(HANDLER_VAR);
			if (handler != Variant::EMPTY)
			{
				Urho3D::EventHandler* eventHandler = static_cast<Urho3D::EventHandler*>(handler.GetVoidPtr());
				if (eventHandler)
				{
					VariantMap& newEventData = GetEventDataMap();
					eventHandler->Invoke(newEventData);
				}
			}
		}
	}
}
[/code]

Creating the menu bar:
[code]
// Setup UI root container
			_container = root->CreateChild<Urho3D::UIElement>();
			_container->SetFixedSize(graphics->GetWidth(), graphics->GetHeight());
			_container->SetPosition(0, 0);
			_container->SetLayoutMode(Urho3D::LM_FREE);
			_container->SetTraversalMode(Urho3D::TM_DEPTH_FIRST);

			//////////////////////////////////////////////////////////////////////////
			/// create menu bar with default menu entries
			menubar_ = Urho3D::MenuBarUI::Create(_container, "EditorMenuBar");

			Urho3D::Menu* fileMenu = menubar_->CreateMenu("File");
			menubar_->CreateMenuItem(fileMenu, "New", HANDLER(EditorState, HandleMenuBarAction_File_New), 'N', Urho3D::QUAL_SHIFT | Urho3D::QUAL_CTRL);
			menubar_->CreateMenuItem(fileMenu, "Open", HANDLER(EditorState, HandleMenuBarAction_File_Open), 'O', Urho3D::QUAL_CTRL);
			menubar_->CreateMenuItem(fileMenu, "Save", HANDLER(EditorState, HandleMenuBarAction_File_Save), 'S', Urho3D::QUAL_CTRL);
			menubar_->CreateMenuItem(fileMenu, "Save As", HANDLER(EditorState, HandleMenuBarAction_File_SaveAs), 'S', Urho3D::QUAL_SHIFT | Urho3D::QUAL_CTRL);
			menubar_->CreateMenuItem(fileMenu, "Exit Editor", HANDLER(EditorState, HandleMenuBarAction_File_Exit));

			Urho3D::Menu* editMenu = menubar_->CreateMenu("Edit");
			menubar_->CreateMenuItem(editMenu, "Undo", 0, 'Z', Urho3D::QUAL_CTRL);
			menubar_->CreateMenuItem(editMenu, "Redo", 0, 'Y', Urho3D::QUAL_CTRL);
			menubar_->CreateMenuItem(editMenu, "Cut", 0, 'X', Urho3D::QUAL_CTRL);
			menubar_->CreateMenuItem(editMenu, "Copy", 0, 'C', Urho3D::QUAL_CTRL);
			menubar_->CreateMenuItem(editMenu, "Paste", 0, 'V', Urho3D::QUAL_CTRL);
			menubar_->CreateMenuItem(editMenu, "Delete", 0, Urho3D::KEY_DELETE, Urho3D::QUAL_ANY);
			menubar_->CreateMenuItem(editMenu, "Select all", 0, 'A', Urho3D::QUAL_CTRL);

			//////////////////////////////////////////////////////////////////////////
			/// create "Create" menu w/ node & components
			Urho3D::Menu* createMenu = menubar_->CreateMenu("Create");
			menubar_->CreateIconizedMenuItem(createMenu, "Node", "Node");

			Urho3D::Menu* componentMenu = menubar_->CreateSubMenu(createMenu, "Component", -1);

			Urho3D::Menu* gameMenu = menubar_->CreateSubMenu(componentMenu, "Game", -1);
			menubar_->CreateIconizedMenuItem(gameMenu, "DeathZone");
			menubar_->CreateIconizedMenuItem(gameMenu, "SpawnPoint");

			Urho3D::Menu* audioMenu = menubar_->CreateSubMenu(componentMenu, "Audio", -1);
			menubar_->CreateIconizedMenuItem(audioMenu, "SoundListener");
			menubar_->CreateIconizedMenuItem(audioMenu, "SoundSource");
			menubar_->CreateIconizedMenuItem(audioMenu, "SoundSource3D");

			Urho3D::Menu* geometryMenu = menubar_->CreateSubMenu(componentMenu, "Geometry", -1);
			menubar_->CreateIconizedMenuItem(geometryMenu, "AnimatedModel");
			menubar_->CreateIconizedMenuItem(geometryMenu, "BillboardSet");
			menubar_->CreateIconizedMenuItem(geometryMenu, "CustomGeometry");
			menubar_->CreateIconizedMenuItem(geometryMenu, "DecalSet");
			menubar_->CreateIconizedMenuItem(geometryMenu, "ParticleEmitter");
			menubar_->CreateIconizedMenuItem(geometryMenu, "Skybox");
			menubar_->CreateIconizedMenuItem(geometryMenu, "StaticModel");
			menubar_->CreateIconizedMenuItem(geometryMenu, "StaticModelGroup");
			menubar_->CreateIconizedMenuItem(geometryMenu, "Terrain");
			menubar_->CreateIconizedMenuItem(geometryMenu, "Text3D");

			Urho3D::Menu* logicMenu = menubar_->CreateSubMenu(componentMenu, "Logic", -1);
			menubar_->CreateIconizedMenuItem(logicMenu, "AnimationController");
			menubar_->CreateIconizedMenuItem(logicMenu, "ScriptInstance");
			menubar_->CreateIconizedMenuItem(logicMenu, "SplinePath");

			Urho3D::Menu* navigationMenu = menubar_->CreateSubMenu(componentMenu, "Navigation", -1);
			menubar_->CreateIconizedMenuItem(navigationMenu, "Navigable");
			menubar_->CreateIconizedMenuItem(navigationMenu, "NavigationMesh");
			menubar_->CreateIconizedMenuItem(navigationMenu, "OffMeshConnection");

			Urho3D::Menu* physicsMenu = menubar_->CreateSubMenu(componentMenu, "Physics", -1);
			menubar_->CreateIconizedMenuItem(physicsMenu, "RigidBody");
			menubar_->CreateIconizedMenuItem(physicsMenu, "CollisionShape");
			menubar_->CreateIconizedMenuItem(physicsMenu, "Constraint");

			Urho3D::Menu* sceneMenu = menubar_->CreateSubMenu(componentMenu, "Scene", -1);
			menubar_->CreateIconizedMenuItem(sceneMenu, "Camera");
			menubar_->CreateIconizedMenuItem(sceneMenu, "Light");
			menubar_->CreateIconizedMenuItem(sceneMenu, "Zone");

			Urho3D::Menu* subsystemMenu = menubar_->CreateSubMenu(componentMenu, "Subsystem", -1);
			menubar_->CreateIconizedMenuItem(subsystemMenu, "DebugRenderer");
			menubar_->CreateIconizedMenuItem(subsystemMenu, "Octree");
			menubar_->CreateIconizedMenuItem(subsystemMenu, "PhysicsWorld");
			menubar_->CreateIconizedMenuItem(subsystemMenu, "PhysicsWorld2D");

			Urho3D::Menu* urho2dMenu = menubar_->CreateSubMenu(componentMenu, "Urho2D", -1);
			menubar_->CreateIconizedMenuItem(urho2dMenu, "AnimatedSprite2D");
			menubar_->CreateIconizedMenuItem(urho2dMenu, "CollisionBox2D");
			menubar_->CreateIconizedMenuItem(urho2dMenu, "CollisionCircle2D");
			menubar_->CreateIconizedMenuItem(urho2dMenu, "CollisionEdge2D");
			menubar_->CreateIconizedMenuItem(urho2dMenu, "CollisionPolygon2D");
			menubar_->CreateIconizedMenuItem(urho2dMenu, "ParticleEmitter2D");
			menubar_->CreateIconizedMenuItem(urho2dMenu, "RigidBody2D");
			menubar_->CreateIconizedMenuItem(urho2dMenu, "StaticSprite2D");
			//SubscribeToEvent(menubar_, Urho3D::E_MENUBAR_ACTION, HANDLER(EditorState, HandleMenuBarAction));

			//menubar_->FinalizedPopupMenu((Urho3D::Window*)componentMenu->GetPopup());

			Urho3D::Menu* windowMenu = menubar_->CreateMenu("Window");
			menubar_->CreateMenuItem(windowMenu, "Attribute Editor", HANDLER(EditorState, HandleMenuBarAction_Window_AttributeEditor));
			menubar_->CreateMenuItem(windowMenu, "Scene Hierarchy", HANDLER(EditorState, HandleMenuBarAction_Window_SceneHierarchy));
			menubar_->CreateMenuItem(windowMenu, "Hide editor");
[/code]

Creating the toolbar:
[code]
toolbar_ = Urho3D::ToolBarUI::Create(_container, "EditorMenuBar", iconStyle);
			toolbar_->SetPosition(0, menubar_->GetHeight());

			Urho3D::UIElement* updateModeGroup = toolbar_->CreateGroup("RunUpdateGroup", Urho3D::LM_HORIZONTAL);
			toolbar_->CreateToolBarToggle("RunUpdatePlay", updateModeGroup, HANDLER(EditorState, HandleUpdateModeGroupToggle));
			toolbar_->CreateToolBarToggle("RunUpdatePause", updateModeGroup, HANDLER(EditorState, HandleUpdateModeGroupToggle));
			toolbar_->CreateToolBarToggle("RevertOnPause", updateModeGroup, HANDLER(EditorState, HandleUpdateModeGroupToggle));

			toolbar_->CreateToolBarSpacer(4);
			Urho3D::UIElement* editModeGroup = toolbar_->CreateGroup("EditModeGroup", Urho3D::LM_HORIZONTAL);
			toolbar_->CreateToolBarToggle("EditMove", editModeGroup, HANDLER(EditorState, HandleEditModeGroupToggle));
			toolbar_->CreateToolBarToggle("EditRotate", editModeGroup, HANDLER(EditorState, HandleEditModeGroupToggle));
			toolbar_->CreateToolBarToggle("EditScale", editModeGroup, HANDLER(EditorState, HandleEditModeGroupToggle));
			toolbar_->CreateToolBarToggle("EditSelect", editModeGroup, HANDLER(EditorState, HandleEditModeGroupToggle));

			toolbar_->CreateToolBarSpacer(4);
			Urho3D::UIElement* axisModeGroup = toolbar_->CreateGroup("AxisModeGroup", Urho3D::LM_HORIZONTAL);
			toolbar_->CreateToolBarToggle("AxisWorld", axisModeGroup, HANDLER(EditorState, HandleAxisModeGroupToggle));
			toolbar_->CreateToolBarToggle("AxisLocal", axisModeGroup, HANDLER(EditorState, HandleAxisModeGroupToggle));

			toolbar_->CreateToolBarSpacer(4);
			toolbar_->CreateToolBarToggle("MoveSnap", HANDLER(EditorState, HandleSnapGroupToggle));
			toolbar_->CreateToolBarToggle("RotateSnap", HANDLER(EditorState, HandleSnapGroupToggle));
			toolbar_->CreateToolBarToggle("ScaleSnap", HANDLER(EditorState, HandleSnapGroupToggle));

			toolbar_->CreateToolBarSpacer(4);
			Urho3D::UIElement* snapScaleModeGroup = toolbar_->CreateGroup("SnapScaleModeGroup", Urho3D::LM_HORIZONTAL);
			toolbar_->SetRequireSelection(snapScaleModeGroup, false);
			toolbar_->CreateToolBarToggle("SnapScaleHalf", snapScaleModeGroup, HANDLER(EditorState, HandleSnapScaleModeGroupToggle));
			toolbar_->CreateToolBarToggle("SnapScaleQuarter", snapScaleModeGroup, HANDLER(EditorState, HandleSnapScaleModeGroupToggle));

			toolbar_->CreateToolBarSpacer(4);
			Urho3D::UIElement* pickModeGroup = toolbar_->CreateGroup("PickModeGroup", Urho3D::LM_HORIZONTAL);
			toolbar_->CreateToolBarToggle("PickGeometries", pickModeGroup, HANDLER(EditorState, HandlePickModeGroupToggle));
			toolbar_->CreateToolBarToggle("PickLights", pickModeGroup, HANDLER(EditorState, HandlePickModeGroupToggle));
			toolbar_->CreateToolBarToggle("PickZones", pickModeGroup, HANDLER(EditorState, HandlePickModeGroupToggle));
			toolbar_->CreateToolBarToggle("PickRigidBodies", pickModeGroup, HANDLER(EditorState, HandlePickModeGroupToggle));

			toolbar_->CreateToolBarSpacer(4);
			Urho3D::UIElement* fillModeGroup = toolbar_->CreateGroup("FillModeGroup", Urho3D::LM_HORIZONTAL);
			toolbar_->CreateToolBarToggle("FillPoint", fillModeGroup, HANDLER(EditorState, HandleFillModeGroupToggle));
			toolbar_->CreateToolBarToggle("FillWireFrame", fillModeGroup, HANDLER(EditorState, HandleFillModeGroupToggle));
			toolbar_->CreateToolBarToggle("FillSolid", fillModeGroup, HANDLER(EditorState, HandleFillModeGroupToggle));
[/code]

What it looks like:
[url=http://i.imgur.com/kLcfN9M.gif][img]http://i.imgur.com/kLcfN9Mm.gif[/img][/url]
(click on image to open gif)

-------------------------

thebluefish | 2017-01-02 01:04:34 UTC | #15

Alright, so earlier I mentioned in IRC that the AttributeEditor wasn't updating dynamic options. For example, selecting a Model in StaticModel did not show the option to pick a Material.

I changed:
[code]
PostEditAttribute(editorResourcePicker_->GetresourceTargets(), editorResourcePicker_->GetresourcePickIndex(), oldValues);
Update(false);
[/code]
to:
[code]
PostEditAttribute(editorResourcePicker_->GetresourceTargets(), editorResourcePicker_->GetresourcePickIndex(), oldValues
Update(true);
[/code]

as well as:
[code]
if (fullUpdate)
{
	attributesFullDirty_ = false;
	componentContainers_.Clear();
}
[/code]

in AttributeInspector.cpp, and now it's working fine.

Edit: I made some changes, and added a new tab that allows you to play the map from within the editor. I like the workflow a lot. It's integrated into my project, but I've properly placed it into its own namespaces, so it can be easily ripped out if you want.

[github.com/thebluefish/Urho3DEditor](https://github.com/thebluefish/Urho3DEditor)

Thanks again for your work!

-------------------------

sabotage3d | 2017-01-02 01:04:49 UTC | #16

Will the SVG rendering work with OpenGL ES on mobile ?

-------------------------

