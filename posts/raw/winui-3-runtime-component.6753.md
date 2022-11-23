sahandt | 2021-03-11 18:04:40 UTC | #1

With new release of WinUI 3, " it will be possible to creates a Windows Runtime component written in C++/WinRT that can be consumed by any UWP or desktop app with a WinUI-based user interface, regardless of the programming language in which the app is written."

I think it can be a good replacement for Urhosharp.

-------------------------

JSandusky | 2021-03-11 23:17:46 UTC | #2

Isn't the C++/WinRT stuff hard locked onto the desktop targets and not usable with Azure, ASP, Xamarin mobile, etc?

C++/CX doesn't appear to have fixed C++/CLI's nasty issues with SSE/AVX either, forcing you to prune/#ifdef your headers of any inline code using simd that the C++/CX side may touch in the glue code. Gets old really fast. I use C++/CLI bindings myself and just suck it up and turn off SSE for it.

-------------------------

