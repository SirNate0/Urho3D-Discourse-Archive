codingmonkey | 2017-01-02 01:08:34 UTC | #1

Hi folks)
I try to figure out how to get origin position of object in vertex shader on GL renderer
and do not know where it stored

I suppose what translation lays :

there -> vec3 vObjectWorldPos = cModel[3].xyz
        
or

there -> vec3 vObjectWorldPos = vec3(cModel[0][3], cModel[1][3], cModel[2][3])

where exactly?

-------------------------

