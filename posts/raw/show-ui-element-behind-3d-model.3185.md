redmouth | 2017-06-01 03:22:34 UTC | #1

How to display 3d model in front of UI elements, such as a button.

-------------------------

Dave82 | 2018-01-07 16:23:49 UTC | #2

The easiest way is create a custom pass.If you define a pass after "renderui" then all these models will appear on top of the UI elements

Create a renderpath like this : 
[code]

<renderpath>
	<command type="renderui"/>
    <command type="clear" depth="1.0" />
    <command type="scenepass" pass="TopObjects"/>
</renderpath> 
[/code]

Now create a custom technique for your models.
Example (An unlit model with diffuse texture)

[code]
<technique vs="Unlit" ps="Unlit" psdefines="DIFFMAP" >
	<pass name="TopObjects"/>
</technique>
[/code]
Using this technique on models will draw them on top of uielements

-------------------------

yushli1 | 2017-06-02 02:32:23 UTC | #3

Thank you for your reply. I learned something from your method.

-------------------------

