krokodilcapa | 2017-01-02 01:11:23 UTC | #1

I just started to use Code::Blocks, because I have Ubuntu on my notebook, and I want to work with Urho when I'm not at home too.
Maybe somebody CB expert could help me? My first problem is I can't parse Urho headers so the "Find declarations for..." function isn't working, and of course the code completion for Urho classes aren't too. I tried to set in the project options/ C++ parser option the path of Urho's include directory (/home/user/Urho3D/include), but nothing changed.
Also I wanted to store the sources in an 'src' folder, but then the project won't build.. Do I need to store them all in the same directory where the code::blocks project exists? - of course its not really important, because I can use virtual folders to see them clear in the projects, but I think its good to know if I can somehow :slight_smile:

Thanks, and sorry for dumb question, but I never used Code::Blocks before, and also rarely used Linux yet.

Edit: Almost forgot some infos: I used the Urho's cmake_codeblocks.sh file, and maybe good to know I wasn't succeed with the URHO3D_HOME, so cmake didn't find URHO home, I had to browse it by hand. Also the projects builds fine when I have my sources in the project root directory.

-------------------------

