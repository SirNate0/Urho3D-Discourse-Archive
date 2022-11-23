itisscan | 2017-01-02 01:14:47 UTC | #1

I need to use logarithmic function of x - log(x).
In AngelScriptAPI.h i have not found log(x) function.

question.
How i can bound log(x) function to AS ? 

Thanks.

-------------------------

itisscan | 2017-01-02 01:14:47 UTC | #2

I have solved the problem.
 
I added following lines:
1)MathDefs.h
[code]
/// Return base e logarithm of a X number 
template <class T>
inline T Ln(T x) { return log(x); }
template <> inline float Ln<float>(float x) { return log(x); }
[/code]

(note. log(x) function is included from math.h header)

2)MathAPI.cpp 
[code]engine->RegisterGlobalFunction("float Ln(float)", asFUNCTION(Ln<float>), asCALL_CDECL);[/code] 

3)AngelScriptAPI.h
[code]float Ln(float);[/code]

-------------------------

