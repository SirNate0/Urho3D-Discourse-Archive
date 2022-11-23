devrich | 2017-01-02 01:03:00 UTC | #1

I'm not trying to start any kind of flame wars or anything but I do have to ask; what IDE/platform do the developers of Urho3D use to develop Urho3D?

and is there any particular reason for choosing the IDE/platform?

I'm just wondering :slight_smile:

-------------------------

friesencr | 2017-01-02 01:03:00 UTC | #2

When I am windows i use vs2013 community edition when doing c++ work or when I want a debugger.  I use vim when doing any angelscript work or when I want to find code in c++.   Since angelscript/lua don't have real great ide support I fall back to things like grep an awful lot.  I use a pretty neat tool called silversearcher [blog.kowalczyk.info/software/the ... ndows.html](http://blog.kowalczyk.info/software/the-silver-searcher-for-windows.html), it behaves like grep but is more opinionated and more or less just tries to do what you want 99% with ease.  On linux i use vim, dbg and sometimes kdevlop.  

My vim setup is rather extensive, I have been working in vim for 5 years now and it has become an extension of my mind.  I am always trying to exercise reduction and simplicity but still find myself reaching for customization and plugins.

[github.com/friesencr/vim-settin ... ter/.vimrc](https://github.com/friesencr/vim-settings/blob/master/.vimrc)

The interesting bits for an urho programmer would be:
vim-projectionist -- this maps my :A to switch between header and cpp files
vim-dispatch -- for running make in vim
vim-glsl -- glsl syntax
ag.vim -- silver searcher integration
ctrlp / vinegar -- for fast file navigation

i use this line for getting syntax highlighting for angelscript
au BufRead,BufNewFile *.as set filetype=cpp

If you notice the vim settings to be a bit fishy that is because I am primarily a web programmer.

-------------------------

OvermindDL1 | 2017-01-02 01:03:15 UTC | #3

For note, I use KDevelop/Linux for all my Urho3D C++ work and it works fantastically with it (even more so lately with the CMakeLists.txt moved to root), especially as its intellisense is one of the most powerful out.

-------------------------

alexrass | 2017-01-02 01:03:17 UTC | #4

I am using QtCreator for C++. Also generate help in qch format and all cool.
For AngelScript using CodeLite: [url]http://discourse.urho3d.io/t/configuring-codelite-for-editing-as-scripts/68/1[/url]

-------------------------

devrich | 2017-01-02 01:03:18 UTC | #5

Thanks guys!

For me; I've been using gedit on Linux Mint 17.1 cinnamon 64-bit ( ubuntu 14.04 )

I really like the idea of switching to CodeLite and I had it working before but i just recently re-built my computer with new hardware and re-installed everything so I am having trouble getting code complete to work with CodeLite for c++ and lua.  :blush: 

Any ideas would be most appreciated

-------------------------

jmiller | 2017-01-02 01:03:18 UTC | #6

[quote="devrich"]I really like the idea of switching to CodeLite and I had it working before but i just recently re-built my computer with new hardware and re-installed everything so I am having trouble getting code complete to work with CodeLite for c++ and lua.  :blush: 

Any ideas would be most appreciated[/quote]

With C++, using Urho3D master branch, I'm using include directives in this form: #include <Urho3D/Engine/Engine.h>
My code completion paths are simpler than before:
c:\urho_build\include
c:\urho_build\include\Urho3D\ThirdParty
I have these set in Project settings, but they can be set in workspace or globally. In settings I have "only use clang". Can try Workspace>Retag.

-------------------------

devrich | 2017-01-02 01:03:18 UTC | #7

Thanks carnalis! ( again i think )

I found in CodeLite ( version 6.1 as of this writing ) > Workspace ( menu ) > Workspace Settings ( sub-menu ) > CodeCompletion ( tab ) > Typed in the "Search paths:" textbox:
[code](path_to_my_urho3d_source_folder)/Urho3D-1.32/Build/include
(path_to_my_urho3d_source_folder)/Urho3D-1.32/Build/ThirdParty[/code]

I also checked the box in that "Workspace Settings" dialog window > [X] Enable C++11 Standard (clang)

No matter what I do; the code completion still only does c or lua but not the Urho3D c++ and lua :frowning:

-------------------------

rasteron | 2017-01-02 01:03:18 UTC | #8

When I was doing some AS experimenting in Urho3D a while back, it's the good old trusted [url=http://www.flos-freeware.ch/notepad2.html]Notepad2[/url] :smiley:

-------------------------

Stinkfist | 2017-01-02 01:03:21 UTC | #9

Visual Studio (2010 and newer) and Notepad++. CodeLite looks promising if there ever would become a need to jump into doing some serious AS dev.

-------------------------

