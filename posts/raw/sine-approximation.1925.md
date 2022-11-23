Modanung | 2017-01-02 01:11:34 UTC | #1

[url=https://github.com/urho3d/Urho3D/pull/1271]SPLIT FROM GITHUB[/url]

To get fast sines I use a Vector of floats as a look-up table. It is generated when the program starts - but this should be possible during compile time - and after that you get pretty accurate (depending on the resolution) and fast results. Quarter of a period would be enough to generate since this data could be mirrored to fill in the rest.
Would this be a good way to have fast sines built into Urho? Since sines are pretty versatile and useful for game world control.
[quote="damu"]I also thought of using a look-up table with a resolution of for example 1 degree. It would have to be interpolated. I have the feeling it would be slower as one of the variants from/based on Michaels work but it is worth to benchmark and to compare the precision. With caching it might actually be faster.

But it would be also an approximation (and require fmod) which cadaver might not approve?

In general a speedup there and maybe in other places would be good of course. It's a design decision and I also thought of the possibility of making such faster but more inaccurate versions optional via Urho CMake options. That may not be that important for this case but there might be other places where an inaccurate approximation makes a higher performance impact which might be desired.

Oh I also saw a talk (here: [youtu.be/Nsf2_Au6KxU?t=41m40s](https://youtu.be/Nsf2_Au6KxU?t=41m40s)) by a Valve developer who worked at "Left for Dead" and he showed a fast and approximated sincos using SIMD, so it seems that Valve uses such things. I also heard of Unreal having various fast approximations.[/quote]

-------------------------

weitjong | 2017-01-02 01:11:34 UTC | #2

I don't want to upload my graphs to somewhere else just so that I can link them here, so I uploaded them to the same github issue that you splitted. [github.com/urho3d/Urho3D/pull/1 ... -202431947](https://github.com/urho3d/Urho3D/pull/1271#issuecomment-202431947). Based on these graphs, the squared quadratic approximation of the sine function looks pretty darn good.

Range from -pi to pi:
[img]https://cloud.githubusercontent.com/assets/5548048/14080685/48aeef08-f539-11e5-8751-7c26fcf0e7da.png[/img]

Zoom in on range from 0 to pi:
[img]https://cloud.githubusercontent.com/assets/5548048/14080694/534ac9be-f539-11e5-9fac-a44a797b0817.png[/img]

-------------------------

gawag | 2017-01-02 01:11:34 UTC | #3

Cool graph drawings.
Reposting my test output where one can compare the squared quadratic with sinf and cosf by values: [i.imgur.com/b8LEPUY.jpg](http://i.imgur.com/b8LEPUY.jpg)
Just to be sure: That graphs function is the same as in the code currently in the pull request, right? [github.com/urho3d/Urho3D/pull/1 ... a772275bae](https://github.com/urho3d/Urho3D/pull/1271/commits/86ff45ce74251b03d2edea56691220a772275bae)
My test output was made with that. Also in my benchmark this approximation was nearly 3 times as fast as sincosf.

-------------------------

weitjong | 2017-01-02 01:11:34 UTC | #4

Yes, the graph uses the same equation sighted in the original post made by Nick which your program's algorithm derived from.

-------------------------

Modanung | 2017-01-02 01:11:34 UTC | #5

Right, and there's no need trying to be faster than a squared quadratic function?
It does line up real nice.

-------------------------

weitjong | 2017-01-02 01:11:35 UTC | #6

I don't think there is a need to be more accurate than the squared quadratic approximation approach. The implementation, of course, is always the faster the better. Nick in his post has already showed how to eliminate the code branching to speed up the code execution, for one instance. I am not sure why Gawag does not use that. So, I have a good feeling it could be potentially more than 3x faster.

-------------------------

TheComet | 2017-01-02 01:11:35 UTC | #7

How does a small-ish lookup table with linear interpolation compare to the quadratic approximation? I'd imagine it'd be faster, but obviously you consume more memory.

[quote="Modanung"]but this should be possible during compile time[/quote]

The memory needs to be stored somewhere, so there's no way around having to fill in the array at some point during runtime. Unless you do something like have CMake generate the array and store it in a #define or something.  :open_mouth: 

You could use the magic of templates to generate it during startup.

[code]#include <iostream>
#include <cmath>

namespace detail {
    template <class T, int N, int D>
    struct SineInitializer;
    
    template <class T, int N>
    struct SineInitializer<T,N,0>
    {   
        static void init(T* tableSlot) { (void)tableSlot; }
    };
    
    template <class T, int N, int D>
    struct SineInitializer
    {   
        static void init(T* tableSlot)
        {   
            *tableSlot = sin(M_PI * 0.5 * T(N-D)/N);
            SineInitializer<T, N, D-1>::init(tableSlot + 1);
        }
    };
    
} // namespace detail

template <class T, int N>
struct SineTable
{
    SineTable()
        { detail::SineInitializer<T,N,N>::init(table); }

    T table[N];
};


SineTable<double, 16> gSine;

int main()
{
    for(int i = 0; i != 16; ++i)
        std::cout << i << ": " << gSine.table[i] << std::endl;
}[/code]

Beautiful, isn't it? Why wouldn't everyone want code like that in their program?

This line here generates a static array of 16 doubles (double arr[16];) and fills it with a quarter of a sine function (ranging from 0? to 84.375?).
[code]SineTable<double, 16> gSine;[/code]

Since it's static, the constructor is called during start up and you'll have your array filled when entering main(). When compiling with -O3 it ends up inlining all function calls, so it's efficient.

[code]0: 0
1: 0.0980171
2: 0.19509
3: 0.290285
4: 0.382683
5: 0.471397
6: 0.55557
7: 0.634393
8: 0.707107
9: 0.77301
10: 0.83147
11: 0.881921
12: 0.92388
13: 0.95694
14: 0.980785
15: 0.995185[/code]

-------------------------

weitjong | 2017-01-02 01:11:35 UTC | #8

Have you considered the time to fetch the data from the memory and the time required to interpolate between two pre-calculated sine values? Not to mention how would you do the latter without sacrificing the accuracy?

I just spend some time to lookup how the glibc implements the sincosf() function. It appears that the function just internally call __kernel_sinf() and __kernel_cosf() functions separately. There is no magic there. The __kernel_sinf() and __kernel_cosf() functions are implemented using, guess what, some kind of polynomial expansion approximation too. It just that they approximate the true sine/cosine values at a very high accuracy because they expand to a longer series. In this case until the sixth series.

The bottom line. We are just comparing one sine approximation with another. It is a trade-off between accuracy and speed. So, unless we could get a massive speed boost without sacrificing too much on accuracy, I see now why Lasse prefers to stick with the "native" implementation.

-------------------------

Modanung | 2017-01-02 01:11:35 UTC | #9

[quote="TheComet"]You could use the magic of templates to generate it during startup.[/quote]
That's one option. c++11 introduced the [url=http://en.cppreference.com/w/cpp/language/constexpr]constexpr[/url] keyword, which I think might be used for this as well?
But since it's c++11 that's no option for a built-in solution at the moment.

-------------------------

gawag | 2017-01-02 01:11:36 UTC | #10

[quote="weitjong"]Nick in his post has already showed how to eliminate the code branching to speed up the code execution, for one instance. I am not sure why Gawag does not use that. So, I have a good feeling it could be potentially more than 3x faster.[/quote]
Depending on how abs is implemented there is still branching but just outsourced into a library function.
I started testing out various things and also read the article from Nick by now, which I didn't before for some reason. I may be able to make a degree version of the squared quadratic approach as he describes how he got those values.
There are various things one can try like testing abs, testing small branches, testing big branches, comparing assembler output, ... No idea how all that changes the performance. Haven't had much time so far, I'll try to find some tomorrow.
I could also test a version with a cache. I suspect it's less precise than the squared quadratic approach and slower but I'm not sure how good the CPU cache actually is, maybe we'll get a surprise. Also performance numbers are actually interesting as well.
I think the fmodf is one of the more expensive things in the code... Could compare some degree-int(degree/180.0f)*180 thingy or something as an alternative as well...

-------------------------

gawag | 2017-01-02 01:11:37 UTC | #11

The version with abs (fabsf) from Nick is a bit slower as my version with manual branching: [i.imgur.com/ErnfeLu.jpg](http://i.imgur.com/ErnfeLu.jpg)
I added cosine calculation and value wrapping. The resulting values are identical.
Does someone see a further optimization?

Testing caching now and moving that to a separate testing project and uploading that to GitHub. Oh and I also could try my idea to get rid of fmodf.

-------------------------

gawag | 2017-01-02 01:11:37 UTC | #12

Made a separate test project: [github.com/damu/test_sincosf](https://github.com/damu/test_sincosf)
The sincos using a cache is not finished yet but the first results are not as bad as expected. It seems to be a bit slower as the squared quadratic approach but maybe I can optimize that more and I'm also not sure how the precision is.

My idea with a faster fmodf actually worked and is around 3 times faster  :open_mouth: : [i.imgur.com/36IMOTu.png](http://i.imgur.com/36IMOTu.png) (build with -O3 and -ffast-math as can be seen at the bottom)
How can that be? Does one have to do everything himself if one wants performance?

Has anyone another idea for a/the non-cached version (regarding more optimization)?
SIMD (SSE2) could help but I'm not sure if that can be used in that billboard place and it also kinda restricts to x86 and I've also never used that personally. Also it would be quite special for that one place and the idea is more to get a general better sincosf.

Such optimizations are quite work intense and I've again put several hours into it. But I'm also learning more by doing that.

-------------------------

gawag | 2017-01-02 01:11:37 UTC | #13

Oops.  :blush: 
The fabsf version from Nick is actually a bit faster as my branched version. The slower code was caused by the option "-march=pentium-m" which I had enabled in CodeBlocks because I wanted to enable SSE2 and other optimizations but that actually made Nicks fabsf version and sinf and cosf slower. Only found that out as I got quite different numbers in QtCreator.
Hm, actually it was slower with Urho's default CMake options as well. Uhm?
The numbers without that option are:
[code]
0.807046 	<- sinf cosf
0.873049 	<- sincosf
0.19101 	<- sincosf_fast (unprecise)
0.18301 	<- SinCosfFast (unprecise)
0.309017 	<- sincosf_fast2 (precise and better branching)
0.280016 	<- sincosf_fast3 (precise and using fabsf instead of branches)
0.897051 	<- SinCosf_cached_90 (incorrect results, speed could be a bit different with correct calculations)
0.283016 	<- SinCosf_cached_360
[/code]
- a separate sinf and cosf is now slightly faster as sincosf.
- Nicks fabsf version (sincosf_fast3) is slightly faster as my branch version (sincosf_fast2)
- the version with a cache with 360 degrees is as fast as the precise fabsf version from Nick and weirdly really precise. Almost looks like sincosf uses a look-up table as well but slower.

Nicks fabsf version has the advantage of not using memory and not getting cold cache effects which the cached_360 does. Also it is possible to avoid the degree to radians conversion to make it even faster.

Also I'm now using my "faster" fmodf (fmodf_fast). The relevant results with fmodf instead are:
[code]
0.259014 	<- sincosf_fast (unprecise)
0.255014 	<- SinCosfFast (unprecise)
0.287016 	<- sincosf_fast2 (precise and better branching)
0.272015 	<- sincosf_fast3 (precise and using fabsf instead of branches)
0.828047 	<- SinCosf_cached_90 (incorrect results, speed could be a bit different with correct calculations)
0.259014 	<- SinCosf_cached_360
[/code]
For some reason some variants are faster with fmodf and others with my fmodf_fast. I guess it has to do with inlining and mine is only faster when inlined, which GCC only does in the shorter loops. :unamused: 

I'll try to dig more into the fmodf and fmodf_fast weirdness and try to optimize Nicks version with degrees and maybe other stuff, like a manually inlined fmodf_fast. Oh and I'll also get some precision statistics which is especially interesting in comparison with the cached version.

Edit: parts of the things stated here are wrong. I had some compiler version and 32bit vs 64bit executable chaos. The compiler option mentioned above was not the cause.

-------------------------

weitjong | 2017-01-02 01:11:37 UTC | #14

Just wonder how did you time your program. In Linux, I could just wrap the program that I want to time with a "time" command. And also for this kind of the tests, I would ensure my CPU speed scaling not causing wrong reading by setting the CPU frequency governor to the highest setting available (instead of default powersave mode). But ignore me if you have already done so.

-------------------------

gawag | 2017-01-02 01:11:38 UTC | #15

[quote="weitjong"]Just wonder how did you time your program. In Linux, I could just wrap the program that I want to time with a "time" command. And also for this kind of the tests, I would ensure my CPU speed scaling not causing wrong reading by setting the CPU frequency governor to the highest setting available (instead of default powersave mode). But ignore me if you have already done so.[/quote]
I'm using std::chrono::high_resolution_clock as you can see in the code: [github.com/damu/test_sincosf/bl ... ain.cpp#L6](https://github.com/damu/test_sincosf/blob/master/main.cpp#L6)
It's a real time clock, so no cycle counting stuff.
I'm on a desktop so no real adjustable CPU speed or powersave mode. Also the program should be always executed at full speed as it is not waiting or something. The results are quite consistent and close to each other when starting the program several times or when executing the same test several times.

Optimizing code is always weird. Really small things can make big differences.

Oh what the hay. I think I found the reason:
The version with the slow sinf and cosf and fast fmodf_fast was a 64bit application build by a GCC 4.8.2.
The version with the fast sinf and cosf and slow fmodf_fast was a 32bit application build by a GCC 4.9.2. Both from the MinGW64 project.
I guess the newer GCC/MinGW version has a faster sinf and cosf but my fmodf_fast is slightly slower than fmodf in 32bit mode but way faster in 64bit mode. Also the whole sincosf_cached_360 is way faster on 64bit.

I actually had already checked for 32bit/64bit stuff and different compiler versions but it seems my QtCreator was wrongly configured as the "32bit" build there was actually a 64bit build with the same 4.8.2 GCC.
I'll try to get more up to date compilers and test with properly configured IDEs...  :unamused: That took really long to figure out...

-------------------------

weitjong | 2017-01-02 01:11:38 UTC | #16

[quote="gawag"]I'm on a desktop so no real adjustable CPU speed or powersave mode. Also the program should be always executed at full speed as it is not waiting or something.[/quote]
I won't be so sure about that. I am using desktop CPU from Intel and I know mine has frequency scaler, my motherboard from Asus also has feature like Cool n Quiet. Anyway if you got a consistent readings then I suppose it's non issue for you.

-------------------------

gawag | 2017-01-02 01:11:40 UTC | #17

This is really weird. Some things I assumed are again wrong.
Sorry for spamming this thread so much. I'm out of ideas regarding the compiler dependent results and stopping that now with final results:

[b]Windows with MinGW:[/b]
I've now benchmarked with GCC 5.3.0 in 64bit and 32bit, both 64bit and 32bit are around these values:
[code]
1.61709         <- sinf cosf
0.830047        <- sincosf
with using fmodf:
0.263015        <- sincosf_fast
0.242013        <- SinCosfFast
0.274015        <- sincosf_fast2 (precise and better branching)
0.249014        <- sincosf_fast3 (precise and using fabsf instead of branches)
0.278015        <- SinCosf_cached_90
0.239013        <- SinCosf_cached_360
with using my fmodf_fast:
0.157009        <- sincosf_fast
0.147008        <- SinCosfFast
0.216012        <- sincosf_fast2 (precise and better branching)
0.17901         <- sincosf_fast3 (precise and using fabsf instead of branches)
0.222012        <- SinCosf_cached_90
0.17901         <- SinCosf_cached_360
[/code]
I've no idea what's going on. My fmodf_fast is actually faster as fmodf, as I had hoped. The results are the same with this MinGW in CodeBlocks and QtCreator with their default options (both with additionally -O3 -ffast-math).
I assume the one MinGW with the faster sinf and cosf was some special one. I have now four MinGW (AKA GCC on Windows) versions (two 32bit and two 64bit and three different GCC versions(4.8.2, 4.9.2 and 5.3)) that all have the same results with a slow sinf and cos and fast fmodf_fast.

[b]Linux[/b]
Benchmark results on a 64bit Linux system with GCC 5.2.0:
[code]
0.23583 	<- sinf cosf
0.252991 	<- sincosf
with using fmodf:
0.254887 	<- sincosf_fast
0.217493 	<- SinCosfFast
0.287769 	<- sincosf_fast2 (precise and better branching)
0.232882 	<- sincosf_fast3 (precise and using fabsf instead of branches)
0.533353 	<- SinCosf_cached_90
0.250574 	<- SinCosf_cached_360
with using my fmodf_fast:
0.168701 	<- sincosf_fast
0.127137 	<- SinCosfFast
0.231201 	<- sincosf_fast2 (precise and better branching)
0.194316 	<- sincosf_fast3 (precise and using fabsf instead of branches)
0.517385 	<- SinCosf_cached_90
0.208518 	<- SinCosf_cached_360
[/code]

[b]Windows with VS2015[/b]
And here comes the troll Visual Studio 2015  :open_mouth: : [i.imgur.com/wFQLowA.png](http://i.imgur.com/wFQLowA.png) I've tested everything five times as you can see.
I'll call it Banana Studio from now on. Also there are more "wat" results as the ones I've marked, kinda missed at least the sincosf_fast3 weirdness.

The fmodf benchmark on Visual Studio is relative consistent around these values:
[code]
x86:
5.47131         <- fmodf
0.475393        <- manual
0.474258        <- fmodf_fast
x64:
1.84036         <- fmodf
0.497435        <- manual
0.497714        <- fmodf_fast
[/code]

The fmodf benchmark is around these value for GCC 5.3.0 32bit and 64bit on Windows and GCC 5.2.0 64bit on Linux (haven't tested 32bit on Linux):
[code]
0.977551 	<- fmodf
0.334571 	<- manual
0.332621 	<- fmodf_fast
[/code]

[b]Conclusion:[/b]
So the fmodf_fast approach seems to be mostly way faster. But the sinf, cosf and sincosf functions are all over the place depending on the system and STL implementation.
Also Visual Studio is really weird.
An alternative for sinf&cosf or sincosf would be good for at least MinGW as it is really slow there. Not sure about Banana Studio though as it seems to be doing a lot of code elimination in this test.

Edit (don't want to make a new post for this):
I tried making the currently best approximation SinCos3 with degrees so that one saves the degrees to radians conversion. I couldn't get the values right to have the best values but the measured time in my test is 0.18 seconds compared to the version with radians (and the required conversion) which is 0.21 seconds. As expected the degree version is slightly faster.

-------------------------

