abhishek.sinha | 2017-01-02 01:05:00 UTC | #1

While going through rendering documentation for shadows I hit a line "Another way of fighting self-shadowing issues is to render shadowcaster backfaces, see Materials". I went through materials but could not get any insights on how we can render shadowcaster backfaces.

Could anyone give insights as to what is shadowcaster backface and how to use it

-------------------------

cadaver | 2017-01-02 01:05:00 UTC | #2

In the Editor's Material editor window, scroll down and choose "CW" from the "Shadow cull" dropdown (normal value is CCW, which will render shadow frontfaces)

Or in a material's xml, add the element:

[code]
<shadowcull value="cw" />
[/code]
If your mesh is not continuous (does not have a bottom) this will cause the shadow to disappear partially. You may also see light bleeding artifacts near the backfaces, so this is not a complete problem-free solution.

-------------------------

abhishek.sinha | 2017-01-02 01:05:02 UTC | #3

Thanks for your response. Was just wondering could it lead to any performance or rendering issues

-------------------------

