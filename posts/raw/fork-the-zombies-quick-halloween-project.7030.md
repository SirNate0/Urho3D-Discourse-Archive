pilesofspam | 2021-11-02 14:18:43 UTC | #1

Like the title, this is a project completed over 3 weeks of spare time with Halloween as a goal.  Our neighborhood is spaced out just about right for Halloween, so we get kids from the surrounding neighborhoods trick-or-treating through here.  I set up an outdoor movie screen, built a "fork the zombies" game (my 13yo son's idea) and a laser guided (wireless) crossbow.  I'll get some technical details up in a bit but let me post some pictures first.
![game1|666x500](upload://cKLttkCEhTStv6BNzhTExR1yncq.jpeg)
The crossbow has a class 1 red laser built into the front, and there's a webcam up there with a red filter in front of it.  This means I have a calibration routine that I run so that the webcam can correlate where the red dot is on the screen (much like a mouse pointer).  I couldn't run the calibration routine until it got dark and here (just outside Atlanta) it got dark enough at about 6:45.  I think this pic was taken at about 7:00pm.

Here's some close-ups of the crossbow:
![bow1|375x500](upload://l1Y0rsE282Asdi9ia5jZpYG6yXh.jpeg)
![bow2|666x500](upload://5L9CkFkrBawYhoMKy3BfDvKONGT.jpeg)
It's basically a 2x4 stud that I freehand carved into a rough crossbow shape.  I wanted to avoid guns, but you've got to fling forks at zombies.  Few technical points:
1. There's an esp32 wifi board in there, it reads trigger pulls (trigger is a microswitch up there with a 3D printed cap) and sends a UDP packet off to the hit detect.
2.  Hit detect is ALWAYS looking for that red laser, and normalizes it (0-1 in X and Y) from the lower left hand corner of the screen.
3.  When hit detect gets a UDP 'Trigger' packet, it sends a message (I'm using ZMQ pub/sub) to the game, which then spawns a fork in the same direction reported from hit detect.

Game stayed pretty busy all night- my sounds and graphics are fairly cartoonish (flinging a fork is actually a mouth-harp *sproing*
I got some great comments from the kids- a few wanted to know how the whole thing worked, one actually asked "How did you know zombies are allergic to forks?"  Here's one of my favorite pics- a pack of fairies playing:
![faries|666x500](upload://A1qOd0eYVOq6aZDTR8yrGqjHrdC.jpeg)

For technical details, there's a projector connected to a Jetson Nano running the game, and another nano connected to a webcam doing hit detect.  Besides that it's just the laser and the esp32 in the crossow sending UDP packets, all are connected to a wifi router.  Honestly you could skip the nanos and just do it on a single laptop, this is definitely more portable.  I will release the source with instructions to build, but I need to get some credits in order first- the zombies aren't mine (inexpensive turbosquid purchase, I modified the skins) and most of the sounds came from freesound.org.  I need to attribute these to their proper authors before I can release.  I do have the list, hopefully I can get that in order this week.  The game plays fine on a PC, you just mouse click to fire a fork, but it's not as challenging because I have the crossbow limited to 1 shot every 1/2 second.  The game is designed to last 1 minute or less.
The hit detect stuff is python and openCV, I'll probably write (and link to) a separate article on how all that works.  Meanwhile for the Urho stuff- what an awesome engine!  This was a ton of fun.  I started with example 6- skeletal animation, and imported the zombies.  Then I brought in elements of example 11- Physics for hit detect and fork flight.  From there it was just steering things where I wanted them to go!  I think the hardest part was getting ZMQ to work with cmake.

-------------------------

