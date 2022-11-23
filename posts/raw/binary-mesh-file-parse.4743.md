k7x | 2018-12-15 11:04:03 UTC | #1

Pliss help read binary data from mesh.

I disassembled such a structure :
>         int 0
>         int numGeometryes / materials
>         int 1
>         int 0
>         byte 0
> 
>         byte stringLength
>         String texture name.tex
>         int num vertex
>         int num tris
>         array
>             float data. packed ?
>         
>         everywhere as if the block identifier is such a record 00 00 00 01
>         01. After 3 float (12b)
>         and main data its short floats
>         array
>             Vector3 vertex pos packed ? can be read using ReadPackedVector3()
>             4b ?
>             Vector2 uv на simple floats 0.0 - 1.0 as normal uv. not packed
>         array
>         
>         array indices 
>             short
>         array

Please, help.

The size of the blocks with the texture varies in different files of this mesh.
after string and until the end of the block, sometimes the size is 90 bytes. Sometimes 85. Next comes zeros, empty space is 65 bytes.
Sometimes in some files there is no empty space.
Sometimes it is as if a block of 90 bytes is written with a texture, and after it is not the same block, but immediately something similar to the records of the vertices and the se.
How to read this file or how to go directly to the record with vertex, 4b, uv?
Very similar to DirectXSDK MeshConventer.

[file][1]

  [1]: https://mega.nz/#F!eSowXYCI!LEguGFB5sWPEJfSKp3E-mQ

-------------------------

johnnycable | 2018-12-14 16:06:00 UTC | #2

Don't know what you're trying to do, but maybe this can help...

https://discourse.urho3d.io/t/directly-loading-a-model/641

-------------------------

k7x | 2018-12-14 17:02:36 UTC | #3

 Thank ! 

I try to get order for read binary correctly.
I port pc game to urho on android)

And write small util to do it. Finnaly spend around 18 hours to read binary
![imgpsh_fullsize|150x250](upload://iet28kz4oGhoNNGupOFcmo4SxGo.png)

-------------------------

