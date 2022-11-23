vivienneanthony | 2017-01-02 01:09:13 UTC | #1

Hi

Do anyone know what would cause a window background element not to show up right but everything else does?

[i.imgur.com/gQ3Zw0X.png](http://i.imgur.com/gQ3Zw0X.png)

It's the window you can barely see on the bottom right.


The style file I'm using. The style is on the bottom.

I'm not sure what's going on

Viv

Stylesheet code
[code]<elements>
   <element type="BorderImage">
      <attribute name="Texture" value="Texture2D;Textures/UI.png" />
   </element>
   <element type="Button" style="BorderImage">
      <attribute name="Size" value="16 16" />
      <attribute name="Image Rect" value="16 0 32 16" />
      <attribute name="Border" value="4 4 4 4" />
      <attribute name="Pressed Image Offset" value="16 0" />
      <attribute name="Hover Image Offset" value="0 16" />
      <attribute name="Pressed Child Offset" value="-1 1" />
   </element>
   <element type="ToggledButton" style="Button" auto="false">
      <attribute name="Image Rect" value="160 64 176 80" />
   </element>
   <element type="CheckBox" style="BorderImage">
      <attribute name="Min Size" value="16 16" />
      <attribute name="Max Size" value="16 16" />
      <attribute name="Image Rect" value="80 0 96 16" />
      <attribute name="Border" value="4 4 4 4" />
      <attribute name="Checked Image Offset" value="16 0" />
      <attribute name="Hover Image Offset" value="0 16" />
   </element>
   <element type="CloseButton" style="Button" auto="false">
      <!-- non-auto style is shown explicitly in the Editor's style drop down list for user selection -->
      <attribute name="Min Size" value="16 16" />
      <attribute name="Max Size" value="16 16" />
      <attribute name="Image Rect" value="144 0 160 16" />
      <attribute name="Focus Mode" value="NotFocusable" />
   </element>
   <element type="Cursor">
      <attribute name="Shapes">
         <variant type="VariantVector">
            <variant type="String" value="Normal" />
            <variant type="ResourceRef" value="Image;Textures/UI.png" />
            <variant type="IntRect" value="0 0 12 24" />
            <variant type="IntVector2" value="0 0" />
         </variant>
         <variant type="VariantVector">
            <variant type="String" value="ResizeVertical" />
            <variant type="ResourceRef" value="Image;Textures/UI.png" />
            <variant type="IntRect" value="0 64 20 84" />
            <variant type="IntVector2" value="9 9" />
         </variant>
         <variant type="VariantVector">
            <variant type="String" value="ResizeDiagonalTopRight" />
            <variant type="ResourceRef" value="Image;Textures/UI.png" />
            <variant type="IntRect" value="20 64 40 84" />
            <variant type="IntVector2" value="9 9" />
         </variant>
         <variant type="VariantVector">
            <variant type="String" value="ResizeHorizontal" />
            <variant type="ResourceRef" value="Image;Textures/UI.png" />
            <variant type="IntRect" value="40 64 60 84" />
            <variant type="IntVector2" value="9 9" />
         </variant>
         <variant type="VariantVector">
            <variant type="String" value="ResizeDiagonalTopLeft" />
            <variant type="ResourceRef" value="Image;Textures/UI.png" />
            <variant type="IntRect" value="60 64 80 84" />
            <variant type="IntVector2" value="9 9" />
         </variant>
         <variant type="VariantVector">
            <variant type="String" value="RejectDrop" />
            <variant type="ResourceRef" value="Image;Textures/UI.png" />
            <variant type="IntRect" value="80 64 100 84" />
            <variant type="IntVector2" value="9 9" />
         </variant>
         <variant type="VariantVector">
            <variant type="String" value="AcceptDrop" />
            <variant type="ResourceRef" value="Image;Textures/UI.png" />
            <variant type="IntRect" value="100 64 128 90" />
            <variant type="IntVector2" value="0 0" />
         </variant>
         <variant type="VariantVector">
            <variant type="String" value="Busy" />
            <variant type="ResourceRef" value="Image;Textures/UI.png" />
            <variant type="IntRect" value="128 64 148 85" />
            <variant type="IntVector2" value="9 9" />
         </variant>
      </attribute>
   </element>
   <element type="DropDownList" style="BorderImage">
      <attribute name="Image Rect" value="16 0 32 16" />
      <attribute name="Border" value="4 4 4 4" />
      <attribute name="Pressed Image Offset" value="16 0" />
      <attribute name="Hover Image Offset" value="0 16" />
      <attribute name="Pressed Child Offset" value="-1 1" />
      <attribute name="Layout Mode" value="Horizontal" />
      <attribute name="Layout Border" value="4 1 4 1" />
      <element internal="true">
         <element type="Text" internal="true" />
      </element>
      <element type="Window" internal="true" popup="true">
         <attribute name="Layout Border" value="2 4 2 4" />
         <element type="ListView" internal="true">
            <attribute name="Highlight Mode" value="Always" />
            <element type="BorderImage" internal="true">
               <!-- Override scroll panel attributes from default ListView -->
               <attribute name="Opacity" value="0" />
               <attribute name="Clip Border" value="2 0 2 0" />
            </element>
         </element>
      </element>
   </element>
   <element type="LineEdit" style="BorderImage">
      <attribute name="Border" value="4 4 4 4" />
      <attribute name="Image Rect" value="64 0 80 16" />
      <attribute name="Hover Image Offset" value="0 16" />
      <!-- Background color of the hover image IS the hover color of LineEdit -->
      <element type="Text" internal="true">
         <attribute name="Color" value="0.9 1 0.9 1" />
         <attribute name="Selection Color" value="0.3 0.4 0.7 1" />
      </element>
      <element type="BorderImage" internal="true">
         <attribute name="Size" value="4 16" />
         <attribute name="Priority" value="1" />
         <attribute name="Image Rect" value="12 0 16 16" />
      </element>
   </element>
   <element type="ListView" style="ScrollView">
      <!-- Shortcut to copy all the styles from ScrollView -->
      <element type="BorderImage" internal="true">
         <element internal="true">
            <attribute name="Layout Mode" value="Vertical" />
         </element>
      </element>
   </element>
   <element type="HierarchyListView" style="ListView" auto="false">
      <attribute name="Hierarchy Mode" value="true" />
      <attribute name="Base Indent" value="1" />
      <!-- Allocate space for overlay icon at the first level -->
      <element type="BorderImage" internal="true">
         <element type="HierarchyContainer" internal="true">
            <attribute name="Layout Mode" value="Vertical" />
         </element>
      </element>
   </element>
   <element type="HierarchyListViewOverlay" style="BorderImage">
      <attribute name="Min Size" value="16 16" />
      <attribute name="Max Size" value="16 16" />
      <attribute name="Image Rect" value="176 0 192 16" />
      <attribute name="Checked Image Offset" value="16 0" />
      <attribute name="Hover Image Offset" value="0 16" />
   </element>
   <element type="Menu" style="BorderImage">
      <attribute name="Image Rect" value="112 0 128 16" />
      <attribute name="Border" value="4 4 4 4" />
      <attribute name="Pressed Image Offset" value="16 0" />
      <attribute name="Hover Image Offset" value="0 16" />
   </element>
   <element type="ScrollBar">
      <attribute name="Min Size" value="16 16" />
      <attribute name="Left Image Rect" value="32 32 48 48" />
      <attribute name="Up Image Rect" value="0 32 16 48" />
      <attribute name="Right Image Rect" value="48 32 64 48" />
      <attribute name="Down Image Rect" value="16 32 32 48" />
      <element type="Button" internal="true">
         <attribute name="Size" value="16 16" />
         <attribute name="Border" value="4 4 4 4" />
         <attribute name="Pressed Image Offset" value="64 0" />
         <attribute name="Hover Image Offset" value="0 16" />
      </element>
      <element type="Slider" internal="true">
         <attribute name="Size" value="16 16" />
      </element>
      <element type="Button" internal="true">
         <attribute name="Size" value="16 16" />
         <attribute name="Border" value="4 4 4 4" />
         <attribute name="Pressed Image Offset" value="64 0" />
         <attribute name="Hover Image Offset" value="0 16" />
      </element>
   </element>
   <element type="ScrollView">
      <element type="ScrollBar" internal="true">
         <attribute name="Size" value="0 16" />
      </element>
      <element type="ScrollBar" internal="true">
         <attribute name="Size" value="16 0" />
      </element>
      <element type="BorderImage" internal="true">
         <attribute name="Image Rect" value="48 0 64 16" />
         <attribute name="Border" value="4 4 4 4" />
         <attribute name="Hover Image Offset" value="16 16" />
         <attribute name="Clip Border" value="2 2 2 2" />
      </element>
   </element>
   <element type="Slider" style="BorderImage">
      <attribute name="Size" value="16 16" />
      <attribute name="Image Rect" value="48 0 64 16" />
      <attribute name="Border" value="4 4 4 4" />
      <element type="BorderImage" internal="true">
         <attribute name="Image Rect" value="16 0 32 16" />
         <attribute name="Border" value="4 4 4 4" />
         <attribute name="Hover Image Offset" value="0 16" />
      </element>
   </element>
   <element type="Window" style="BorderImage">
      <attribute name="Image Rect" value="48 0 64 16" />
      <attribute name="Border" value="4 4 4 4" />
      <attribute name="Resize Border" value="8 8 8 8" />
   </element>
   <element type="DialogWindow" style="Window" auto="false">
      <attribute name="Is Movable" value="true" />
      <attribute name="Modal Shade Color" value="0.3 0.4 0.7 0.4" />
      <attribute name="Modal Frame Color" value="0.3 0.4 0.7" />
      <attribute name="Modal Frame Size" value="2 2" />
   </element>
   <element type="ListRow">
      <attribute name="Min Size" value="0 17" />
      <attribute name="Max Size" value="2147483647 17" />
      <attribute name="Layout Mode" value="Horizontal" />
   </element>
   <element type="PanelView" style="ListView" auto="false">
      <!-- todo: rename this to PanelListView -->
      <element type="BorderImage" internal="true">
         <attribute name="Image Rect" value="48 16 64 32" />
         <attribute name="Hover Image Offset" value="80 32" />
         <element internal="true">
            <attribute name="Layout Spacing" value="4" />
            <attribute name="Layout Border" value="4 4 4 4" />
         </element>
      </element>
   </element>
   <element type="Panel" auto="false">
      <attribute name="Layout Mode" value="Vertical" />
      <attribute name="Layout Spacing" value="4" />
   </element>
   <element type="HorizontalPanel" auto="false">
      <attribute name="Layout Mode" value="Horizontal" />
      <attribute name="Layout Spacing" value="4" />
   </element>
   <element type="Text">
      <attribute name="Font" value="Font;Fonts/Anonymous Pro.ttf" />
      <attribute name="Font Size" value="11" />
      <attribute name="Color" value="0.85 0.85 0.85" />
      <attribute name="Color" value="0.9 1 0.9 1" />
      <attribute name="Selection Color" value="0.3 0.4 0.7 1" />
      <attribute name="Hover Color" value="0.3 0.4 0.7 1" />
   </element>
   <element type="DebugHudText" style="Text" auto="false">
      <attribute name="Text Effect" value="Shadow" />
   </element>
   <element type="ConsoleBackground" auto="false">
      <attribute name="Color" value="0.15 0.15 0.15 0.8" />
      <attribute name="Layout Border" value="4 4 4 4" />
   </element>
   <element type="ConsoleText" style="Text" auto="false">
      <attribute name="Hover Color" value="0.3 0.4 0.7 1" />
      <attribute name="Selection Color" value="0.2 0.225 0.35 1" />
   </element>
   <element type="ConsoleHighlightedText" style="ConsoleText" auto="false">
      <attribute name="Color" value="1 0 0 1" />
   </element>
   <element type="ConsoleLineEdit" style="LineEdit" auto="false">
      <attribute name="Min Size" value="0 17" />
      <attribute name="Max Size" value="2147483647 17" />
      <element type="Text" internal="true">
         <attribute name="Selection Color" value="0.3 0.4 0.7 0.75" />
      </element>
   </element>
   <element type="FileSelector" style="DialogWindow" auto="false">
      <attribute name="Size" value="400 300" />
      <attribute name="Is Resizable" value="true" />
      <attribute name="Resize Border" value="6 6 6 6" />
      <attribute name="Layout Mode" value="vertical" />
      <attribute name="Layout Spacing" value="4" />
      <attribute name="Layout Border" value="6 6 6 6" />
   </element>
   <element type="FileSelectorButton" style="Button" auto="false">
      <attribute name="Min Size" value="80 17" />
      <attribute name="Max Size" value="80 17" />
   </element>
   <element type="FileSelectorButtonText" style="Text" auto="false" />
   <element type="FileSelectorListView" style="ListView" auto="false">
      <attribute name="Highlight Mode" value="Always" />
   </element>
   <element type="FileSelectorLineEdit" style="LineEdit" auto="false">
      <attribute name="Min Size" value="0 17" />
      <attribute name="Max Size" value="2147483647 17" />
   </element>
   <element type="FileSelectorFilterList" style="DropDownList" auto="false">
      <attribute name="Min Size" value="64 17" />
      <attribute name="Max Size" value="64 17" />
      <attribute name="Resize Popup" value="true" />
   </element>
   <element type="FileSelectorFilterText" style="Text" auto="false">
      <attribute name="Is Enabled" value="true" />
      <attribute name="Selection Color" value="0.2 0.225 0.35 1" />
      <attribute name="Hover Color" value="0.3 0.4 0.7 1" />
   </element>
   <element type="FileSelectorLayout" auto="false">
      <attribute name="Min Size" value="0 17" />
      <attribute name="Max Size" value="2147483647 17" />
      <attribute name="Layout Spacing" value="4" />
   </element>
   <element type="FileSelectorListText" style="Text" auto="false">
      <attribute name="Hover Color" value="0.3 0.4 0.7 1" />
      <attribute name="Selection Color" value="0.2 0.225 0.35 1" />
   </element>
   <element type="FileSelectorTitleText" style="Text" auto="false" />
   <element type="EditorDivider" style="BorderImage" auto="false">
      <attribute name="Image Rect" value="144 32 160 43" />
      <attribute name="Border" value="4 4 4 4" />
      <attribute name="Min Size" value="0 11" />
      <attribute name="Max Size" value="2147483647 11" />
   </element>
   <element type="EditorDragSlider" style="BorderImage">
      <attribute name="Image Rect" value="240 64 256 80" />
   </element>
   <element type="EditorSeparator" auto="false">
      <attribute name="Min Size" value="0 2" />
      <attribute name="Max Size" value="2147483647 2" />
   </element>
   <element type="EditorMenuBar" style="BorderImage" auto="false">
      <attribute name="Image Rect" value="112 0 127 15" />
      <attribute name="Border" value="4 4 4 4" />
   </element>
   <element type="EditorMenuText" style="Text" auto="false" />
   <element type="EditorAttributeText" auto="false">
      <attribute name="Font" value="Font;Fonts/BlueHighway.ttf" />
      <attribute name="Font Size" value="9" />
   </element>
   <element type="EditorEnumAttributeText" style="EditorAttributeText" auto="false">
      <attribute name="Is Enabled" value="true" />
      <attribute name="Selection Color" value="0.2 0.225 0.35 1" />
      <attribute name="Hover Color" value="0.3 0.4 0.7 1" />
   </element>
   <element type="EditorToolBar" style="BorderImage" auto="false">
      <attribute name="Image Rect" value="112 0 127 15" />
      <attribute name="Border" value="4 4 4 4" />
   </element>
   <element type="ToolBarButton" style="Button">
      <attribute name="Min Size" value="34 34" />
      <attribute name="Max Size" value="34 34" />
      <attribute name="Layout Mode" value="Horizontal" />
      <attribute name="Layout Border" value="2 2 2 2" />
      <attribute name="Focus Mode" value="NotFocusable" />
   </element>
   <element type="ToolBarToggle" style="CheckBox">
      <attribute name="Min Size" value="34 34" />
      <attribute name="Max Size" value="34 34" />
      <attribute name="Image Rect" value="208 0 224 16" />
      <attribute name="Layout Mode" value="Horizontal" />
      <attribute name="Layout Border" value="2 2 2 2" />
      <attribute name="Focus Mode" value="NotFocusable" />
   </element>
   <element type="ToolBarToggleGroupLeft" style="ToolBarToggle">
      <attribute name="Image Rect" value="160 32 176 48" />
   </element>
   <element type="ToolBarToggleGroupMiddle" style="ToolBarToggle">
      <attribute name="Image Rect" value="192 32 208 48" />
   </element>
   <element type="ToolBarToggleGroupRight" style="ToolBarToggle">
      <attribute name="Image Rect" value="224 32 240 48" />
   </element>
   <element type="EditorAttributeEdit" style="LineEdit" auto="false" />
   <element type="ToolTipBorderImage" style="BorderImage">
      <attribute name="Layout Mode" value="Horizontal" />
      <attribute name="Layout Border" value="6 2 6 2" />
      <attribute name="Image Rect" value="48 0 64 16" />
      <attribute name="Border" value="6 2 2 2" />
   </element>
   <element type="ToolTipText" style="Text">
      <attribute name="Font" value="Font;Fonts/BlueHighway.ttf" />
      <attribute name="Font Size" value="9" />
   </element>
   <element type="ViewportBorder" style="BorderImage">
      <attribute name="Image Rect" value="50 5 51 6" />
      <attribute name="Border" value="0 0 0 0" />
   </element>
   <element type="MenuBarUI" style="BorderImage">
      <attribute name="Image Rect" value="112 0 128 16" />
      <attribute name="Border" value="4 4 4 4" />
   </element>
   <element type="ToolBarUI" style="BorderImage">
      <attribute name="Image Rect" value="112 0 128 16" />
      <attribute name="Border" value="8 4 4 8" />
   </element>
   <element type="MiniToolBarUI" style="BorderImage">
      <attribute name="Image Rect" value="112 0 128 16" />
      <attribute name="Border" value="4 4 4 4" />
   </element>
   <element type="WindowFrame" style="BorderImage">
      <attribute name="Image Rect" value="128 0 144 16" />
      <attribute name="Border" value="4 4 4 4" />
      <attribute name="Resize Border" value="8 8 8 8" />
   </element>
   <element type="BasicAttributeUI" auto="false">
      <attribute name="Layout Mode" value="Horizontal" />
      <attribute name="Min Size" value="0 19" />
      <attribute name="Max Size" value="2147483647 19" />
      <element type="Text" style="EditorAttributeText" internal="true">
         <attribute name="Min Size" value="150 0" />
         <attribute name="Max Size" value="150 2147483647" />
      </element>
   </element>
   <element type="BoolAttributeUI" style="BasicAttributeUI" auto="false">
      <element type="CheckBox" internal="true" />
   </element>
   <element type="StringAttributeUI" style="BasicAttributeUI" auto="false">
      <element type="LineEdit" internal="true">
         <attribute name="Min Size" value="0 17" />
         <attribute name="Max Size" value="2147483647 17" />
      </element>
   </element>
   <element type="ResourceRefAttributeUI" style="BasicAttributeUI" auto="false">
      <attribute name="Layout Mode" value="Vertical" />
      <attribute name="Layout Spacing" value="2" />
      <attribute name="Min Size" value="0 17" />
      <attribute name="Max Size" value="2147483647 2147483647" />
      <element internal="true">
         <attribute name="Layout Mode" value="Horizontal" />
         <attribute name="Layout Spacing" value="4" />
         <attribute name="Layout Border" value="10 0 4 0" />
         <attribute name="Min Size" value="0 19" />
         <attribute name="Max Size" value="2147483647 19" />
         <element type="LineEdit" internal="true">
            <attribute name="Min Size" value="0 17" />
            <attribute name="Max Size" value="2147483647 17" />
         </element>
      </element>
   </element>
   <element type="EnumAttributeUI" style="BasicAttributeUI" auto="false">
      <element type="DropDownList" internal="true">
         <attribute name="Layout Mode" value="Horizontal" />
         <attribute name="Layout Border" value="4 1 4 1" />
         <attribute name="Min Size" value="0 17" />
         <attribute name="Max Size" value="2147483647 17" />
      </element>
   </element>
   <element type="AttributeContainer">
      <attribute name="Layout Mode" value="Vertical" />
      <attribute name="Layout Spacing" value="4" />
      <attribute name="Show Non Editable" value="false" />
      <attribute name="Attr Name Width" value="150" />
      <attribute name="Attr Height" value="19" />
      <attribute name="Min Size" value="50 150" />
      <element type="Text" internal="true">
         <element internal="true">
            <attribute name="Layout Mode" value="Horizontal" />
            <attribute name="Layout Spacing" value="2" />
            <element type="Button" internal="true">
               <attribute name="Min Size" value="16 16" />
               <attribute name="Max Size" value="16 16" />
               <attribute name="Layout Mode" value="Horizontal" />
               <element type="BorderImage" internal="true">
                  <attribute name="Texture" value="Texture2D;Textures/UI.png" />
                  <attribute name="Image Rect" value="128 32 144 48" />
               </element>
            </element>
         </element>
      </element>
      <element type="ListView" internal="true">
         <attribute name="Clip Children" value="false" />
      </element>
   </element>
   <element type="TabButton" style="BorderImage" auto="false">
      <attribute name="Image Rect" value="160 96 176 112" />
      <attribute name="Border" value="4 4 4 4" />
      <attribute name="Layout Border" value="2 2 2 2" />
      <attribute name="Pressed Image Offset" value="16 0" />
      <attribute name="Hover Image Offset" value="0 16" />
   </element>
   <element type="TabWindow" style="Window">
      <attribute name="Layout Mode" value="Vertical" />
      <attribute name="Layout Spacing" value="0" />
      <attribute name="Layout Border" value="2 2 2 2" />
      <element internal="true">
         <attribute name="Min Size" value="0 10" />
         <attribute name="Max Size" value="2147483647 25" />
         <attribute name="Layout Mode" value="Horizontal" />
      </element>
   </element>
   <element type="HierarchyWindow" style="Window">
      <attribute name="Is Movable" value="false" />
      <attribute name="Is Resizable" value="true" />
      <attribute name="Resize Border" value="6 6 6 6" />
      <attribute name="Layout Mode" value="Vertical" />
      <attribute name="Layout Spacing" value="4" />
      <attribute name="Layout Border" value="6 6 6 6" />
      <element internal="true">
         <attribute name="Min Size" value="0 16" />
         <attribute name="Max Size" value="2147483647 16" />
         <attribute name="Layout Mode" value="Horizontal" />
         <element type="Text" internal="true" />
         <element type="Button" style="CloseButton" internal="true" />
      </element>
      <element type="BorderImage" style="EditorDivider" internal="true" />
      <element internal="true">
         <attribute name="Min Size" value="0 17" />
         <attribute name="Max Size" value="2147483647 17" />
         <attribute name="Layout Mode" value="Horizontal" />
         <attribute name="Layout Spacing" value="4" />
         <element type="Button" internal="true">
            <attribute name="Name" value="ExpandButton" />
            <attribute name="Min Size" value="60 17" />
            <attribute name="Max Size" value="70 17" />
            <attribute name="Layout Mode" value="Horizontal" />
            <attribute name="Layout Border" value="1 1 1 1" />
            <element type="Text" internal="true">
               <attribute name="Text Alignment" value="Center" />
            </element>
         </element>
         <element type="Button" internal="true">
            <attribute name="Name" value="CollapseButton" />
            <attribute name="Min Size" value="60 17" />
            <attribute name="Max Size" value="70 17" />
            <attribute name="Layout Mode" value="Horizontal" />
            <attribute name="Layout Border" value="1 1 1 1" />
            <element type="Text" internal="true">
               <attribute name="Text Alignment" value="Center" />
            </element>
         </element>
         <element type="CheckBox" internal="true">
            <attribute name="Min Size" value="25 15" />
            <attribute name="Max Size" value="45 15" />
            <attribute name="Indent Spacing" value="30" />
            <attribute name="Indent" value="1" />
            <attribute name="Layout Mode" value="Horizontal" />
            <attribute name="Layout Border" value="5 1 1 1" />
            <element type="Text" internal="true" />
         </element>
      </element>
      <element type="ListView" style="HierarchyListView" internal="true">
         <attribute name="Name" value="HierarchyList" />
         <attribute name="Highlight Mode" value="Always" />
         <attribute name="Multiselect" value="true" />
         <element type="Text" internal="true" />
      </element>
   </element>
   <element type="AssetsHierarchyWindow" style="Window">
      <attribute name="Is Movable" value="false" />
      <attribute name="Is Resizable" value="true" />
      <attribute name="Resize Border" value="6 6 6 6" />
      <attribute name="Layout Mode" value="Vertical" />
      <attribute name="Layout Spacing" value="4" />
      <attribute name="Layout Border" value="6 6 6 6" />
      <element internal="true">
         <attribute name="Min Size" value="0 16" />
         <attribute name="Max Size" value="2147483647 16" />
         <attribute name="Layout Mode" value="Horizontal" />
         <element type="Text" internal="true" />
         <element type="Button" style="CloseButton" internal="true" />
      </element>
      <element type="BorderImage" style="EditorDivider" internal="true" />
      <element internal="true">
         <attribute name="Min Size" value="0 17" />
         <attribute name="Max Size" value="2147483647 17" />
         <attribute name="Layout Mode" value="Horizontal" />
         <attribute name="Layout Spacing" value="4" />
         <element type="Button" internal="true">
            <attribute name="Name" value="ExpandButton" />
            <attribute name="Min Size" value="60 17" />
            <attribute name="Max Size" value="70 17" />
            <attribute name="Layout Mode" value="Horizontal" />
            <attribute name="Layout Border" value="1 1 1 1" />
            <element type="Text" internal="true">
               <attribute name="Text Alignment" value="Center" />
            </element>
         </element>
         <element type="Button" internal="true">
            <attribute name="Name" value="CollapseButton" />
            <attribute name="Min Size" value="60 17" />
            <attribute name="Max Size" value="70 17" />
            <attribute name="Layout Mode" value="Horizontal" />
            <attribute name="Layout Border" value="1 1 1 1" />
            <element type="Text" internal="true">
               <attribute name="Text Alignment" value="Center" />
            </element>
         </element>
         <element type="CheckBox" internal="true">
            <attribute name="Min Size" value="25 15" />
            <attribute name="Max Size" value="45 15" />
            <attribute name="Indent Spacing" value="30" />
            <attribute name="Indent" value="1" />
            <attribute name="Layout Mode" value="Horizontal" />
            <attribute name="Layout Border" value="5 1 1 1" />
            <element type="Text" internal="true" />
         </element>
      </element>
      <element type="ListView" style="AssetHierarchyListView" internal="true">
         <attribute name="Name" value="AssetHierarchyList" />
         <attribute name="Highlight Mode" value="Always" />
         <attribute name="Multiselect" value="true" />
      </element>
   </element>
   <element type="ViewSettingsWindow" style="Window">
      <attribute name="Is Movable" value="false" />
      <attribute name="Is Resizable" value="true" />
      <attribute name="Resize Border" value="6 6 6 6" />
      <attribute name="Layout Mode" value="Vertical" />
      <attribute name="Layout Spacing" value="4" />
      <attribute name="Layout Border" value="6 6 6 6" />
      <element internal="true">
         <attribute name="Min Size" value="0 16" />
         <attribute name="Max Size" value="2147483647 16" />
         <attribute name="Layout Mode" value="Horizontal" />
         <element type="Text" internal="true" />
         <element type="Button" style="CloseButton" internal="true" />
      </element>
      <element type="BorderImage" style="EditorDivider" internal="true" />
      <element internal="true">
         <attribute name="Min Size" value="0 17" />
         <attribute name="Max Size" value="2147483647 17" />
         <attribute name="Layout Mode" value="Horizontal" />
         <attribute name="Layout Spacing" value="4" />
      </element>
   </element>
   <element type="GameAssetInspector" style="Window">
      <attribute name="Is Movable" value="false" />
      <attribute name="Is Resizable" value="true" />
      <attribute name="Resize Border" value="6 6 6 6" />
      <attribute name="Layout Mode" value="Vertical" />
      <attribute name="Layout Spacing" value="4" />
      <attribute name="Layout Border" value="6 6 6 6" />
      <element type="BorderImage" internal="true" />
      <element internal="true">
         <attribute name="Min Size" value="0 16" />
         <attribute name="Max Size" value="2147483647 16" />
         <attribute name="Layout Mode" value="Horizontal" />
         <element type="Text" internal="true" />
         <element type="Button" style="CloseButton" internal="true" />
      </element>
      <element type="BorderImage" style="EditorDivider" internal="true" />
      <element internal="true">
         <attribute name="Min Size" value="0 17" />
         <attribute name="Max Size" value="2147483647 17" />
         <attribute name="Layout Mode" value="Horizontal" />
         <attribute name="Layout Spacing" value="4" />
      </element>
   </element>
   <element type="GameAssetSelector" style="Window">
      <attribute name="Is Resizable" value="true" />
      <attribute name="Resize Border" value="6 6 6 6" />
      <attribute name="Layout Mode" value="Vertical" />
      <attribute name="Layout Spacing" value="4" />
      <attribute name="Layout Border" value="6 6 6 6" />
      <attribute name="Is Movable" value="true" />
      <attribute name="Color" value="1 1 1" />
      <attribute name="Modal Shade Color" value="1 1 1 1" />
      <attribute name="Modal Frame Color" value="1 1 1" />
      <attribute name="Modal Frame Size" value="300 500" />
      <attribute name="Opacity" value="1" />
      <element internal="true">
         <attribute name="Min Size" value="0 48" />
         <attribute name="Max Size" value="2147483647 16" />
         <attribute name="Layout Mode" value="Horizontal" />
         <element type="Text" internal="true" />
         <element type="Button" style="CloseButton" internal="true" />
      </element>
      <element type="BorderImage" auto="true" internal="true">
         <attribute name="Image Rect" value="144 32 160 43" />
         <attribute name="Border" value="4 4 4 4" />
         <attribute name="Min Size" value="0 11" />
         <attribute name="Max Size" value="2147483647 11" />
      </element>
      <element type="ListView" internal="true" auto="true">
         <attribute name="Min Size" value="180 400" />
         <attribute name="Max Size" value="180 400" />
         <attribute name="Highlight Mode" value="Always" />
         <attribute name="Multiselect" value="false" />
         &gt;
         <attribute name="Is Enabled" value="true" />
         <attribute name="Layout Mode" value="Horizontal" />
         <attribute name="Layout Border" value="0 0 0 0" />
         <attribute name="Layout Spacing" value="4" />
      </element>
      <element type="BorderImage" auto="true" internal="true">
         <attribute name="Image Rect" value="144 32 160 43" />
         <attribute name="Border" value="4 4 4 4" />
         <attribute name="Min Size" value="0 11" />
         <attribute name="Max Size" value="2147483647 11" />
      </element>
      <element internal="true">
         <attribute name="Min Size" value="180 24" />
         <attribute name="Max Size" value="180 24" />
         <attribute name="Layout Mode" value="Horizontal" />
         <attribute name="Layout Border" value="1 1 1 1" />
         <attribute name="Layout Spacing" value="16" />
         <attribute name="Vertical Alignment" value="Right" />
         <element type="Button" internal="true" auto="true">
            <attribute name="Name" value="CancelButton" />
            <attribute name="Min Size" value="60 24" />
            <attribute name="Max Size" value="60 24" />
            <attribute name="Layout Mode" value="Horizontal" />
            <attribute name="Layout Border" value="1 1 1 1" />
            <attribute name="Layout Spacing" value="8" />
            <element type="Text" internal="true">
               <attribute name="Text Alignment" value="Center" />
            </element>
         </element>
         <element type="Button" internal="true" auto="true">
            <attribute name="Name" value="SelectButton" />
            <attribute name="Min Size" value="60 24" />
            <attribute name="Max Size" value="60 24" />
            <attribute name="Position" value="100 0" />
            <attribute name="Layout Mode" value="Horizontal" />
            <attribute name="Layout Border" value="1 1 1 1" />
            <attribute name="Layout Spacing" value="8" />
            <element type="Text" internal="true">
               <attribute name="Text Alignment" value="Center" />
            </element>
         </element>
      </element>
   </element>
   <element type="AboutTeamGDPWindow" style="Window" auto="true" internal="true">
      <attribute name="Is Resizable" value="true" />
      <attribute name="Resize Border" value="6 6 6 6" />
      <attribute name="Layout Mode" value="Vertical" />
      <attribute name="Layout Spacing" value="4" />
      <attribute name="Layout Border" value="6 6 6 6" />
      <attribute name="Min Size" value="400 300" />
      <attribute name="Max Size" value="400 300" />
      <attribute name="Is Movable" value="true" />
      <attribute name="Color" value="1 1 1 1" />
      <attribute name="Image Rect" value="128 0 143 16" />
      <attribute name="Border" value="4 4 4 4" />
      <attribute name="Opacity" value="1" />
      <attribute name="Texture" value="Texture2D;Textures/UI.png" />    
      <attribute name="Focus Mode" value="Focusable" /> 
      <element internal="true">
         <attribute name="Min Size" value="0 48" />
         <attribute name="Max Size" value="2147483647 16" />
         <attribute name="Layout Mode" value="Horizontal" />
         <element type="Text" internal="true" />
         <element type="Button" style="CloseButton" internal="true" />
      </element>
      <element type="BorderImage" auto="true" internal="true">
         <attribute name="Image Rect" value="144 32 160 43" />
         <attribute name="Border" value="4 4 4 4" />
         <attribute name="Min Size" value="0 11" />
         <attribute name="Max Size" value="2147483647 11" />
      </element>
      <element type="Text" auto="true" internal="true">
	  <attribute name="Color" value="0.9 1 0.9 1" />
         <attribute name="Selection Color" value="0.3 0.4 0.7 1" />
      </element>
      <element type="BorderImage" auto="true" internal="true">
         <attribute name="Image Rect" value="144 32 160 43" />
         <attribute name="Border" value="4 4 4 4" />
         <attribute name="Min Size" value="0 11" />
         <attribute name="Max Size" value="2147483647 11" />
      </element>
      <element internal="true">
         <attribute name="Min Size" value="180 24" />
         <attribute name="Max Size" value="180 24" />
         <attribute name="Layout Mode" value="Horizontal" />
         <attribute name="Layout Border" value="1 1 1 1" />
         <attribute name="Layout Spacing" value="16" />
         <attribute name="Vertical Alignment" value="Right" />
         <element type="Button" internal="true" auto="true">
            <attribute name="Name" value="CancelButton" />
            <attribute name="Min Size" value="60 24" />
            <attribute name="Max Size" value="60 24" />
            <attribute name="Layout Mode" value="Horizontal" />
            <attribute name="Layout Border" value="1 1 1 1" />
            <attribute name="Layout Spacing" value="8" />
            <element type="Text" internal="true">
               <attribute name="Text Alignment" value="Center" />
            </element>
         </element>[/code]
      </element>
   </element>
</elements>


Code Calling Create Window
[code]
 pAboutTeamGDPWindow = editorView_->GetMainFrame()->CreateChild<AboutTeamGDPWindow>("AboutTeamGDPWindow");

    if(pAboutTeamGDPWindow)
    {
        // Forced Windows Settings - Not sure why the back is not working
        pAboutTeamGDPWindow->SetResizable(true);
        pAboutTeamGDPWindow->SetMovable(true);
        pAboutTeamGDPWindow->SetDefaultStyle(editorData_->GetEditorDefaultStyle());
        pAboutTeamGDPWindow->SetStyleAuto();

        // More settings
        /*pAboutTeamGDPWindow->SetTexture(g_pApp->GetConstantResCache()->GetResource<Texture2D>("Textures/UI.png"));
        pAboutTeamGDPWindow->SetImageRect(IntRect(48, 0, 60, 16));
        pAboutTeamGDPWindow->SetBorder(IntRect(2, 2, 2, 2));
        pAboutTeamGDPWindow->SetResizeBorder(IntRect(0, 0, 0, 0));
        pAboutTeamGDPWindow->SetLayoutSpacing(0);
        pAboutTeamGDPWindow->SetLayoutBorder(IntRect(0, 4, 0, 0));

        pAboutTeamGDPWindow->SetModal(true);
        //pAboutTeamGDPWindow->SetModalFrameColor(Color(1,1,1,1));
        //pAboutTeamGDPWindow->SetModalFrameSize(IntVector2(300,500));
        //pAboutTeamGDPWindow->SetOpacity(1.0f);

        pAboutTeamGDPWindow-> SetPosition(700, 25);*/
        pAboutTeamGDPWindow->SetModal(true);

        /// Attach okresponse
        SubscribeToEvent(pAboutTeamGDPWindow->GetOkButton(), E_RELEASED, URHO3D_HANDLER(EPScene3D,HandleAboutTeamGDPWindowClosePressed));
        SubscribeToEvent(pAboutTeamGDPWindow->GetCloseButton(),E_RELEASED,URHO3D_HANDLER(EPScene3D,HandleAboutTeamGDPWindowClosePressed));

    }[/code]

Code Making Window
[code]
AboutTeamGDPWindow::AboutTeamGDPWindow(Context* context) :
    Window(context)
{
    // Create Window
    SetLayout(LM_VERTICAL, 4, IntRect(6 ,6, 6, 6));
    SetResizeBorder(IntRect(6, 6, 6, 6));
    SetName("AboutTeamGDPWindow");
    SetLayoutMode(LM_VERTICAL);
    SetAlignment(HA_LEFT,VA_TOP);

    SetModalFrameColor(Color(1,1,1,1));

    SetTexture(g_pApp->GetConstantResCache()->GetResource<Texture2D>("Textures/UI.png"));
    SetImageRect(IntRect(48, 0, 60, 16));

    // Create title UIElement
    m_pTitleRegion = CreateChild <UIElement> ("ATGW_TitleRegion");
    m_pTitleRegion->SetInternal(true);
    m_pTitleRegion->SetLayout(LM_HORIZONTAL);
    m_pTitleRegion->SetAlignment(HA_LEFT,VA_TOP);
    m_pTitleRegion->SetHeight(32);

    AddChild(m_pTitleRegion);

    // Add title and Close Button
    m_pTitleText = CreateChild <Text> ("ATGW_TitleText");
    m_pTitleText->SetInternal(true);
    m_pTitleText -> SetText("About Us");

    m_pTitleRegion-> AddChild(m_pTitleText);

    m_pCloseButton = CreateChild <Button> ("ATGW_CloseButton");
    m_pCloseButton->SetInternal(true);
    m_pTitleRegion -> AddChild(m_pCloseButton);


    // set color
    Color HoverColor(1.0f,0.5f,0.1f);
    Color SelectionColor(0.5f,0.1f,0.2f);
    Color ItemColor(1.0f,1.0f,1.0f);

    BorderImage * spacer = CreateChild<BorderImage>("ATGW_Spacer");
    spacer->SetInternal(true);

    // Add List View
    m_pAboutUs = CreateChild <Text> ("ATGW_AboutUs");
    AddChild(m_pAboutUs);
    m_pAboutUs->SetInternal(true);

    m_pAboutUs->SetText("Vivienne Anthony");


    BorderImage * spacer2 = CreateChild<BorderImage>("ATGW_Spacer2");
    spacer2->SetInternal(true);

    // Add A button region
    m_pButtonRegion = CreateChild <UIElement> ("ATGW_ButtonRegion");
    m_pButtonRegion->SetLayout(LM_HORIZONTAL);
    m_pButtonRegion->SetInternal(true);

    AddChild(m_pButtonRegion); // Add spacer

    // Ok Button
    m_pOkButton = CreateChild <Button> ("ATGW_OkButton");
    m_pOkButton ->SetInternal(true);

    Text * okButtonText = CreateChild <Text> ("ATGW_OkButtonText");
    okButtonText->SetAlignment(HA_CENTER, VA_CENTER);
    okButtonText->SetInternal(true);
    okButtonText->SetText("Ok");
    m_pOkButton->AddChild(okButtonText);

    m_pButtonRegion->AddChild(m_pOkButton);

    AddChild(m_pButtonRegion);

    m_pOkButton->SetPosition(0,100);


    return;
}[/code]

-------------------------

Sir_Nate | 2017-01-02 01:09:14 UTC | #2

To me it looks like the other stuff is being drawn overtop of the window, with the window's children drawn atop those things. I've no suggestions as to why, though.
You could try calling BringToFront() on the AboutTeamGDPWindow after you create the other elements (the attribute inspector, etc.).

-------------------------

