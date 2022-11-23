dragonCASTjosh | 2017-01-02 01:14:17 UTC | #1

Sorry for the large amount of questions this week :slight_smile: i am trying a larger feature that is outside what i have done before. My question here is how to add the shader defines for a new light type for example in the shader i want to have a define for sphere light and one for tube lights. I believe iv added all the code to get the light working correctly so im not sure what im missing.

-------------------------

cadaver | 2017-01-02 01:14:18 UTC | #2

Look in Renderer.h, which has the shader sub-variation defines, and Renderer.cpp, which has string arrays for the defines, and functions like SetBatchShaders(), SetLightVolumeBatchShaders(), LoadPassShaders(). You will have to change the indexing, which is a bit errorprone.

-------------------------

dragonCASTjosh | 2017-01-02 01:14:18 UTC | #3

[quote="cadaver"]Look in Renderer.h, which has the shader sub-variation defines, and Renderer.cpp, which has string arrays for the defines, and functions like SetBatchShaders(), SetLightVolumeBatchShaders(), LoadPassShaders(). You will have to change the indexing, which is a bit errorprone.[/quote]

Sounds fun :slight_smile: that is likely why unreal treats each light type as a component

-------------------------

cadaver | 2017-01-02 01:14:19 UTC | #4

Well, you could add something like GetShaderDefines() to Light component, but at some point you're going to want to get the actual shader variation needed by a light performantly, ie. without string manipulations / compares.

-------------------------

dragonCASTjosh | 2017-01-02 01:14:19 UTC | #5

Do you think for know it could be worth having Area lights extend point lights in the same manor as unreal 4 rather then adding a new light type. I as this as the system for adding new light types looks way over my head currently.

-------------------------

cadaver | 2017-01-02 01:14:19 UTC | #6

If the area light calculations are more complex, I would hope that every point light would not run them.

It doesn't have to be a new light type as such, but a new boolean / new shader define nevertheless. 

Try to track how the NORMALOFFSET define was added, that was the last time when the light variation string array was being expanded.

-------------------------

