practicing01 | 2017-01-02 01:06:22 UTC | #1

[img]http://img.ctrlv.in/img/15/08/09/55c695a632fc1.gif[/img]

Urho2D's asset workflow with spriter is tedious for traditional sprite sheets.  The important bits of the following code can be used to load a "texture atlas" generated with urho's SpritePacker and animate a StaticSprite2D with it (using an animation xml format similar to the old urho2d thread found on this forum).

[github.com/practicing01/Urho3DT ... 1c3e219a80](https://github.com/practicing01/Urho3DTemplate/commit/cb659efaf69087f668adba073d2e811c3e219a80)

Animation format:
[spoiler][code]
<Animation >
    <Name name="idleM" />
    <Loop loop="true" />
    <FrameCount frameCount="10" />
    <Frame0 duration="0.1" sprite="cleric_0_0" />
    <Frame1 duration="0.1" sprite="cleric_0_1" />
    <Frame2 duration="0.1" sprite="cleric_0_2" />
    <Frame3 duration="0.1" sprite="cleric_0_3" />
    <Frame4 duration="0.1" sprite="cleric_0_4" />
    <Frame5 duration="0.1" sprite="cleric_0_5" />
    <Frame6 duration="0.1" sprite="cleric_0_6" />
    <Frame7 duration="0.1" sprite="cleric_0_7" />
    <Frame8 duration="0.1" sprite="cleric_0_8" />
    <Frame9 duration="0.1" sprite="cleric_0_9" />
</Animation>

[/code][/spoiler]

-------------------------

