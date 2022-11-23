ghidra | 2017-01-02 01:02:10 UTC | #1

This might be more of a glsl question than a urho one. 
I'm trying to create an array in glsl.
in a function
[code]
int myarray[8] = int[](0, 32, 8, 40, 2, 34, 10, 42);
[/code]
I'm getting this error:
[code]
error: array constructors forbidden in GLSL 1.10 (GLSL 1.20 or GLSL ES 3.00 required)
[/code]
Is there no way to achieve this?
Thank you.

-------------------------

ghidra | 2017-01-02 01:02:11 UTC | #2

[quote]

I guess i solved it. It just seems kind of messy.
[code]
int d[8];
d[0]=0;d[1]=32;d[2]=8;d[3]=40;d[4]=2;d[5]=34;d[6]=10;d[7]=42;
[/code]

However I am still trying to find a better way to achive this. This method seems to drop my frame range from 120fps to 70-90fps. 
I should probably move the array out of the function. Or at the least figure out a way to not have to set the values every call to the function.

[/quote]

UPDATE:

I managed to get my Framerates back up, with a silly hack. Maybe that is just the nature of glsl, I dont know.
Before I was calling a function that had that origional int array, and set the values. This was being run on every fragment.
Instead, I make a global int array, and set the length. then before doing anything else i call a function that builds that array, so in theroy it only calls once when the shader is run on the object, saving a lot of setting.

psuedo code:
[code]
int array[64];
build_array(){
     array[0]=0;array[1]=1;array[3]=3;...."61 more values"
}
PS(){
     build_array();
     "now everything else"
}
[/code]

Still seems hacky to me. When trying to do anything i found from the web on how to set arrays in glsl, i got errors.
I tried:
[code]
int array[64] = int[64]{...};
int array[64] = int[]{...};
const length = 64;
int array[length] = {...};
etc..
[/code]
errors were:
[code]
error: C-style initialization requires the GL_ARB_shading_language_420pack extension
-or-
error: array constructors forbidden in GLSL 1.10 (GLSL 1.20 or GLSL ES 3.00 required)
[/code]

Should I consider my work around the solve for this, as acording to the errors, we cant declare arrays with values?

-------------------------

