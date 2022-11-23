umen | 2017-01-02 01:05:28 UTC | #1

i created new engine tree for codeblocks then i loaded it to QtCreator as new project , all the sources and examples did compiled just fine .
but i noticed that the sources for the examples and the engine are not copied to the new engine source tree but somehow configured to take them form the original Urho3d source tree .
my question is how can i load/include/see all the source's in the IDE 
how can i run the examples in the IDE?

update :
i did created the cmake_codeblock project and loaded it to codeblocks IDE and every thing is working just fine and i can see the source of the examples and also the the sources of the engine .
but there is small problem i guess in the structure of the code blocks workspace tree , 
1. i can't find the names of the libraries the examples are using , the list is empty 
2. to add new libraries  to for example the "Hello_world"  i need to add it to the main Urho3D engine , i can't do it per example . only top level .

-------------------------

GoogleBot42 | 2017-01-02 01:05:29 UTC | #2

Open the CMakeLists.txt in qtcreator's project loader (don't use codeblocks) a nice prompt will come up where you can set cmake args and the build directory.  It is pretty straightforward for there. :wink:

-------------------------

umen | 2017-01-02 01:05:29 UTC | #3

did it , it is loading the project into Qtcreator , compile fine the project but still can't see the sources of the examples or the engine

-------------------------

GoogleBot42 | 2017-01-02 01:05:29 UTC | #4

Hmmm that is strange... I will post again when I am booting linux (where qtcreator is on my comp) and I can investigate...

-------------------------

TikariSakari | 2017-01-02 01:05:29 UTC | #5

Did you add parameter -DURHO3D_SAMPLES=1 for cmake when setting up the build-directory?

-------------------------

umen | 2017-01-02 01:05:30 UTC | #6

yes i did

-------------------------

