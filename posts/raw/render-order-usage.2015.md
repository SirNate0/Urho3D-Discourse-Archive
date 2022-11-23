Enhex | 2017-01-02 01:12:18 UTC | #1

Render order need to be used with depth testing to work.
Every pass in the material's technique needs to either always pass the depth test to render in front, or disable depth writing to render behind.

Examples with sample 04_StaticScene:
[gist]https://gist.github.com/Enhex/158a37ad94cd06d6070fedbccf139c70[/gist]

-------------------------

