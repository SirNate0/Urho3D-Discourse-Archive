szamq | 2017-01-02 00:57:42 UTC | #1

Flickering light script which imitates torch or candle. Values can be tweaked by editing ScriptInstance

Usage:
add it as ScriptInstance component to a node with point light. You need two parented nodes to be able to move the flickering light (see structure below), this is because one of the nodes is used internally by FlickeringLight

Hierarchy:
-node
--node
---Light
---ScriptInstance (FlickeringLight)

[code]
class FlickeringLight : ScriptObject
{

	float flickerSpeed=0.2f;
	float _time=0.f;
	
	Vector3 _randomPosition=Vector3(0.f,0.f,0.f);
	Color _randomColor=Color(0.f,0.f,0.f);
	
	float maxPositionChange=0.01f;
	float maxBrightnessChange=0.3f;
	
	
	Vector3 _oldPosition;
	Color _oldColor;
	Color normalColor;
	
    FlickeringLight(){}
    void Start()
	{
		Light@ light=node.GetComponent("Light");
		if(light is null) return;
		normalColor=light.color;
	}

	
    void FixedUpdate(float timeStep)
    {	 
		Light@ light=node.GetComponent("Light");
		if(light is null) return;
		_time+=timeStep;
		if(_time>flickerSpeed)
		{
			_oldPosition=node.position;
			_randomPosition=Vector3(
			Random(maxPositionChange*2.f)-maxPositionChange,
			Random(maxPositionChange*2.f)-maxPositionChange,
			Random(maxPositionChange*2.f)-maxPositionChange);
			float randomBri=Random(Random(maxBrightnessChange*2.f)-maxBrightnessChange);
			_oldColor=light.color;
			_randomColor=normalColor+Color(randomBri,randomBri,randomBri,randomBri);
			
			_time=0.f;
		}
		float mod=_time/flickerSpeed;
		
		node.position=_oldPosition.Lerp(_randomPosition,mod);
		light.color=_oldColor.Lerp(_randomColor,mod);

	}	
}
[/code]

-------------------------

