codingmonkey | 2017-01-02 01:06:09 UTC | #1

Hi folks!
I'm try to set new value for material.shaderParameters("MatDiffColor") 
[code]
                StaticModel@ model = cast<StaticModel>(firstDrawable);
                if (model !is null) 
                {
                    WeakHandle mat = model.materials[0];
                    //Material@ mat = model.material;
                    if (mat.Get() !is null) 
                    {
                        Material@ m = mat.Get();
                        m.shaderParameters["MatDiffColor"] = Variant(c);
                        //model.material = mat;
                    }
                }
[/code]

[spoiler][pastebin]pHzdHMgc[/pastebin][/spoiler]
and got an error when I try to open Material Editor, after color changing, this happen only for static model with material and not happened with light and zones. But why this happen with material or static model ? am also trying change mat parameter  through weakHangle but this not helped.

console error screen
[spoiler][url=http://savepic.ru/7611003.htm][img]http://savepic.ru/7611003m.png[/img][/url][/spoiler]

-------------------------

codingmonkey | 2017-01-02 01:06:09 UTC | #2

I found that the editor eat colors in strange format - strings with spaces :slight_smile: I guess this made for friendly shader parsing in shader values part of material window.
Well, am solve this problem like this. Code similar as in EditShaderParameter in material editor. 

[code]
            }
            else if ( firstDrawable.typeName == "StaticModel" )
            {
                StaticModel@ model = cast<StaticModel>(firstDrawable);
                if (model !is null)
                {
                    Material@ mat = model.materials[0];
                    //Material@ mat = model.material;
                    if (mat !is null)
                    {
                        Variant oldValue = mat.shaderParameters["MatDiffColor"];
                        Variant v;
                        
                        String valueString;
                        valueString += String(c.r);
                        valueString += " ";
                        valueString += String(c.g);
                        valueString += " ";
                        valueString += String(c.b);
                        valueString += " ";
                        valueString += String(c.a);
                            
                        v.FromString(oldValue.type, valueString);
                        
                        mat.shaderParameters["MatDiffColor"] = v;
                    }
                }
            }
[/code]

-------------------------

