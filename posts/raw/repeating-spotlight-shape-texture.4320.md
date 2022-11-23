GoldenThumbs | 2018-06-15 02:21:23 UTC | #1

Hello, I'm some-what new to Urho3D. I've been working on a game for a little more than a week now and I decided to add a flashlight to it, but when I define the light shape texture it repeats instead of just scaling with the spotlight. Anyone know how to fix this? Is it really simple and I'm just missing something?![Repeating_Spotlight|690x388](upload://ybgwL2B9n7NzzR8Nt8sW5mPZlX9.PNG)

-------------------------

Alex-Doc | 2021-02-06 19:26:22 UTC | #2

You could try by adding am xml file in the same folder of the texture, using the same name, i.e.

Spot.png is the texture, make a file and name it Spot.xml, then add this into it:
[code]
<texture>
    <address coord="u" mode="border" />
    <address coord="v" mode="border" />
    <border color="0 0 0 0" />
    <mipmap enable="false" /> 
    <quality low="0" />
</texture>
[/code]

see [the docs here](https://urho3d.github.io/documentation/1.7/_materials.html)

-------------------------

GoldenThumbs | 2018-06-15 11:26:24 UTC | #3

Yeah I already did that after posting this and it fixed it. Thanks for the help though!

-------------------------

