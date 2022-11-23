lexx | 2017-01-02 01:02:18 UTC | #1

Made little converter which converts .obj file to .xml (gui).
One can create gui in blender, using Planes and naming them
BTN_text  (button)
LST_blah  (list)
CHK_blah (checkbox)
IMG_image.png  (sprite)

Save (do not convert to triangles, materials not needed), convert , then open xml in urho3d's Editor, make needed modifications.

TODO:
checkbox text etc.

Sourcecode, compiled exe: [dropbox.com/s/4sim00ca4bcx8 ... UI.7z?dl=0](https://www.dropbox.com/s/4sim00ca4bcx8qr/Obj2GUI.7z?dl=0)
Test .blend file:                 [dropbox.com/s/illl9mo8qsf02 ... nd.7z?dl=0](https://www.dropbox.com/s/illl9mo8qsf02sm/gui1_blend.7z?dl=0)


obj2gui.cs
[code]
/* Obj to Urho3D GUI converter
 * by mjt, 2014
 * 
 * Usage:
 *  obj2gui mygui.obj
 *  
 * Takes obj file as parameter.
 * One can make GUI in ie Blender:
 *  create Planes (do not convert them to triangles).
 *  name them ie
 *     WND                (creates window)
 *     BTN_OK           (creates button and OK text on it)
 *     LST_text          (list)
 *     CHK_text          (checkbox)
 *     IMG_back.png   (sprite  back.png)
 *     
 * 
 * 
 * 
 */

using System;
using System.Collections.Generic;
using System.IO;
using System.Collections;
using System.Globalization;

namespace Obj2GUI
{
    class Program
    {
        static ArrayList components = new ArrayList();

        static void Main(string[] args)
        {
            if (args.Length == 0)
            {
                Console.WriteLine("Usage:\n  obj2gui [mygui.obj]");
                return;
            }
            string[] lines;
            try
            {
                lines = File.ReadAllLines(args[0]);

            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
                return;
            }

            // parse components
            Boolean window = false;
            Component tmp = null;
            String[] str;
            float minX = 10000, minY = 10000, maxX = -10000, maxY = -10000;
            foreach (String line in lines)
            {
                str = line.Split(' ', '_');
                if (str.Length == 0) continue;

                // new component
                if (str[0].Equals("o"))
                {
                    // add component if we have one
                    if (tmp != null)
                    {
                        tmp.X = minX;
                        tmp.Y = minY;
                        tmp.W = maxX - minX;
                        tmp.H = maxY - minY;

                        components.Add(tmp);
                        tmp = null;

                        minX = 10000;
                        minY = 10000;
                        maxX = -10000;
                        maxY = -10000;
                    }

                    tmp = new Component();
                    if (str.Length >= 1)
                    {
                        tmp.Type = str[1];
                    }
                    if (str.Length >= 2)
                    {
                        tmp.Text = str[2];
                    }

                    continue;
                }

                if (str[0].Equals("v"))
                {
                    float x = Single.Parse(str[1], CultureInfo.InvariantCulture);
                    float y = Single.Parse(str[3], CultureInfo.InvariantCulture);
                    if (x < minX) minX = x;
                    if (x > maxX) maxX = x;
                    if (y < minY) minY = y;
                    if (y > maxY) maxY = y;

                    continue;
                }

            }

            // add last one
            if (tmp != null)
            {
                tmp.X = minX;
                tmp.Y = minY;
                tmp.W = maxX - minX;
                tmp.H = maxY - minY;

                components.Add(tmp);
            }

            str = null;
            tmp = null;

            Component wnd = new Component();
            wnd.X = 0;
            wnd.Y = 0;
            wnd.W = 1024;
            wnd.H = 768;
            float XX = 400, YY = 200;
            String xml = "<?xml version='1.0'?>\n";
            // first find window 
            foreach (Component comp in components)
            {
                if (comp.Type.Equals("WND"))
                {
                    window = true;
                    wnd.X = comp.X;
                    wnd.Y = comp.Y;
                    wnd.W = comp.W;
                    wnd.H = comp.H;
                    break;
                }
            }

            // calculate components' pos & size
            foreach (Component comp in components)
            {
                comp.X -= wnd.X;
                comp.Y -= wnd.Y;
                comp.X /= wnd.W;
                comp.Y /= wnd.H;
                comp.X *= 1024;
                comp.Y *= 768;

                comp.W /= wnd.W;
                comp.H /= wnd.H;
                comp.W *= 1024;
                comp.H *= 768;

                comp.X = (int)comp.X;
                comp.Y = (int)comp.Y;
                comp.W = (int)comp.W;
                comp.H = (int)comp.H;

                if (comp.Type.Equals("WND"))
                {
                    xml += "<element type='Window'>\n";
                    xml += "\t" + "<attribute name='Position' value='" + XX + " " + YY + "' />\n";
                    xml += "\t" + "<attribute name='Size' value='" + comp.W + " " + comp.H + "' />\n";
                }
            }

            // other components (children of window)
            foreach (Component comp in components)
            {
                if (comp.Type.Equals("BTN")) // button
                {
                    xml += "\t<element type='Button'>\n";
                    xml += "\t\t" + "<attribute name='Name' value='Button_" + comp.Text + "' />\n";
                    xml += "\t\t" + "<attribute name='Position' value='" + comp.X + " " + comp.Y + "' />\n";
                    xml += "\t\t" + "<attribute name='Size' value='" + comp.W + " " + comp.H + "' />\n";


                    xml += "\t\t<element type='Text'>\n";
                    //xml += "\t\t\t" + "<attribute name='Text' value='" + comp.5 + " " + comp.Y + "' />\n";
                    // TODO aseta teksti keskelle nappia
                    xml += "\t\t\t" + "<attribute name='Position' value='5 5' />\n";
                    xml += "\t\t\t" + "<attribute name='Font Size' value='10' />\n";
                    xml += "\t\t\t" + "<attribute name='Text' value='" + comp.Text + "' />\n";

                    xml += "\t\t</element>\n";
                    xml += "\t</element>\n";

                    continue;
                }

                if (comp.Type.Equals("LST")) // list
                {
                    xml += "\t<element type='ListView'>\n";
                    xml += "\t\t" + "<attribute name='Name' value='List_" + comp.Text + "' />\n";
                    xml += "\t\t" + "<attribute name='Position' value='" + comp.X + " " + comp.Y + "' />\n";
                    xml += "\t\t" + "<attribute name='Size' value='" + comp.W + " " + comp.H + "' />\n";

                    // TODO  scrollbar

                    xml += "\t</element>\n";

                    continue;
                }

                if (comp.Type.Equals("CHK")) // checkbox
                {
                    xml += "\t<element type='CheckBox'>\n";
                    xml += "\t\t" + "<attribute name='Name' value='CheckBox_" + comp.Text + "' />\n";
                    xml += "\t\t" + "<attribute name='Position' value='" + comp.X + " " + comp.Y + "' />\n";
                    xml += "\t\t" + "<attribute name='Size' value='" + comp.W + " " + comp.H + "' />\n";

                    // TODO  teksti

                    xml += "\t</element>\n";

                    continue;
                }

                if (comp.Type.Equals("IMG")) // image / sprite
                {
                    xml += "\t<element type='Sprite'>\n";
                    xml += "\t\t" + "<attribute name='Position' value='" + comp.X + " " + comp.Y + "' />\n";
                    xml += "\t\t" + "<attribute name='Size' value='" + comp.W + " " + comp.H + "' />\n";
                    xml += "\t\t" + "<attribute name='Texture' value='Texture2D;Urho3D/Bin/Data/Textures/" + comp.Text + "' />\n";
                    xml += "\t\t" + "<attribute name='Image Rect' value='0 0 512 512' />\n";

                    // TODO fix

                    xml += "\t</element>\n";

                    continue;
                }

            }

            if (window) xml += "</element>\n";
            xml = xml.Replace('\'', '"');
            xml = xml.Replace(',', '.');
            Console.Out.WriteLine(xml);

            try
            {
                System.IO.File.WriteAllText(args[0] + ".xml", xml);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
                return;
            }

        }

    }

    class Component
    {
        public String Type = "";
        public String Text = "";
        public float X, Y, W, H;

    }

}
[/code]

-------------------------

JTippetts | 2017-01-02 01:02:19 UTC | #2

I'm having a hard time seeing a use case for this, to be honest. I can't test your code, but a quick skim doesn't reveal how to construct hierarchical relationships between the various elements. It seems to me like it just creates a list of non-associated element definitions, which doesn't seem all that useful to me. Unless I am missing something? Is this an attempt to solve a problem with the existing UI editing functionality in the editor?

-------------------------

lexx | 2017-01-02 01:02:21 UTC | #3

Yeah maybe it isnt useful (to others), I just like to create in blender almost everything, gui as well. Hierarchy can be created in urho editor (obj doesnt support hierarchies), as well other things, in blender just create quick 'layout'.

-------------------------

sabotage3d | 2017-01-02 01:02:22 UTC | #4

I think it is cool can it be used for 3d sprites as well ? Let say in-game power-up or a health-bar ?

-------------------------

