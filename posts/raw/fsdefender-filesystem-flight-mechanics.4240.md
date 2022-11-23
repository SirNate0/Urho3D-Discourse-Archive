wakko | 2018-05-19 09:50:26 UTC | #1

Hi everyone,
I am currently making a game where you must defend your own filesystem against (virtual) viruses based on the mechanics shown in this video. At the moment it is only a fly-through-your-own-filesystem prototype and a pretty fun image viewer. My focus was to make the directory and image access as fluent as possible and for this reason I had to bypass/abuse some of the engine's functionality (e.g. loading arbitrary images as textures from outside the resource paths, dynamic scene generation, threading). Images on your hard drive are used as textures ( when supported) and loaded on the fly by using a separate thread. 
My next steps is some UI and settings dialogs. Then gameplay functionality. 

https://www.youtube.com/watch?v=vQloBKmSaLo

-------------------------

extobias | 2018-05-19 14:57:12 UTC | #2

Nice work, it remind me the unix scene in the first jurassic park movie.
https://www.youtube.com/watch?v=dxIPcbmo1_U

-------------------------

