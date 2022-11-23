ChunFengTsin | 2018-01-01 07:20:40 UTC | #1

Hi , everyone  ^^

I fell puzzled at CustomGeometry in Urho3D.

when I draw chunks like minecraft with OpenGL.

this process like this , in client the game generate, calculate and delete cube data  dynamic, 
( according to CREATE_RADIUS， DELETE_RADIUS )  with multithreading , and send them  in mainthreading to rendering .(also delete data buffer which out of range , in GPU )

But when use CustomGeometry in Urho3D, how I to manage the vertex data , am I need not to delete vertex data manually , how to delete data in GPU, that out of range.

thanks.^^

-------------------------

