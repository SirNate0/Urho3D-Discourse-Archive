vram32 | 2020-12-11 13:12:22 UTC | #1

Empty content.......

-------------------------

vmost | 2020-10-20 19:14:45 UTC | #2

Looks like you'd have to write a custom function. Hold on... this doesn't work since resize calls the `SharedPtr` destructor and `GetViewport()` returns a raw pointer not a smart pointer... hmm. Unless, does the intrusive reference counting keep it alive?
```
void RemoveViewportCustom(unsigned index)
{
    Renderer* ren{GetSubsystem<Renderer>()};
    unsigned num_viewports{ren->GetNumViewports()};

    if (index >= num_viewports || num_viewports == 0)
        return;

    // swap the viewport to remove with the last viewport
    if (num_viewports > 1 && index + 1 != num_viewports)
        ren->SetViewport(index, ren->GetViewport(num_viewports - 1));

    // resize the view port count to get rid of last element
    ren->SetNumViewports(num_viewports - 1);
}
```

-------------------------

Avagrande | 2020-10-20 19:24:42 UTC | #3

Viewports are managed by the Renderer by keeping a list of shared pointers which point to the viewports including yours.
To remove a viewport you need to get the shared pointer reference count to 0. 
So: 
- change the viewport count using renderer->SetViewportNum()
- set a different viewport using renderer->SetViewport() in the same index
- set the shared ptr you are using to null

Once you do this the viewport will be removed provided you are not using it somewhere else. 

Personally I encountered this while in Lua whereby setting the viewports would destroy them as shared pointers do not translate to Lua well. Everytime I would call SetViewport for sorting my viewports dynamically, it would destroy my viewport causing a seg fault when I try to set it to a different index. Same goes for setting another viewport in the index your viewport is set to.

-------------------------

weitjong | 2020-12-12 05:49:29 UTC | #5



-------------------------

