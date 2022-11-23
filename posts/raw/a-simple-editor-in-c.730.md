thebluefish | 2017-01-02 01:02:31 UTC | #1

Hey guys,

Another small release here. I have been playing around with creating various tools and helpers in C++. This time around we have a basic editor designed to create Mahjong tile layouts. Dynamic grid sizing and menu bar is ported from the Urho3D editor since it was originally done in Angelscript.

Since I wanted to keep things as simple and portable as possible, I used CustomGeometry for everything but the base scene. I also separated the editor away from my main project, so there shouldn't be too much unrelated code.

Some notes:
- Adjust grid size and layers dynamically.
- Use CTRL + LMB to place a tile.
- Use RMB to look around.
- Camera is clamped to adjustable min/max area

[url=https://github.com/thebluefish/Editor-Demo]You can get the source code here.[/url]

-------------------------

thebluefish | 2017-01-02 01:02:38 UTC | #2

I have updated the editor to include the following changes:

- Added save ability based on Urho3D editor
- Added further tile validation
- Fixed ability to move around tiles
- Many bug fixes
- Many more additions/fixes

I will probably not be updating this project anymore. The editor has gotten to the point where it will be brought over and implemented in my own project. I will likely release a full mahjong solitaire demo sometime in the near future.

-------------------------

