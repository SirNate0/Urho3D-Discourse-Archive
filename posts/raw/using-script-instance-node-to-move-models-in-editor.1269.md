dragonCASTjosh | 2017-01-02 01:06:30 UTC | #1

Is it possible to use the Script Instance component to move objects in the editor's play mode? 
Currently i have the script instance as a child of Sphere node along with a static model. The plan is to make the object bounce in the editors play mode.

-------------------------

cadaver | 2017-01-02 01:06:30 UTC | #2

Yes. For example: 

- Create -> Builtin object -> Box. 
- Add ScriptInstance component to the box node.
- Pick Scripts/Rotator.as as the "Script File" attribute
- Type Rotator into "Class Name"
- If the script was compiled successfully, the "rotationSpeed" attribute (a script public variable) should appear in the inspector. Type something large, for example 50 0 0
- Start the play mode
- Object should rotate.

The Rotator script rotates the script's own node. To move the parent, you would just access node.parent in the script instead.

-------------------------

dragonCASTjosh | 2017-01-02 01:06:30 UTC | #3

thanks that worked perfectly

-------------------------

