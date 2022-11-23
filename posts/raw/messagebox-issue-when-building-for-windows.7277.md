zedraken | 2022-06-05 07:33:54 UTC | #1

Hello,

I am working on a game using Urho3D and in this game, I need to display informations through the use of the Urho3D::MessageBox class.

I am creating an instance of a MessageBox with the following statement:


```
XMLFile *layout = mResourcesCache->GetResource<XMLFile>("UI/SpaceMsgBox.xml");
XMLFile *style = mResourcesCache->GetResource<XMLFile>("UI/SpaceStyle.xml");
Urho3D::MessageBox *errMsgBox = new Urho3D::MessageBox(context_, String("No joystick found!\nClick OK to exit."), String("Error message"), layout, style);
```

Building and running on Linux works perfectly.

However, I am trying to build on Windows as well and then, at link time, I get the following error message:

`undefined reference to ’Urho3D::MessageBoxA::MessageBoxA(Urho3D::Context*, Urho3D::String const&, …)`

It looks like it has something to deal with the MessageBoxA() method defined in the win32 API, but I am not sure.
I do not really understand where this reference to MessageBoxA comes from, it is quite confusing.

I would just like to know if anyone else already experienced this issue, and if yes, how to get rid of it.

Feel free to ask me for more details if relevant.

Thanks!

Charles

-------------------------

JSandusky | 2022-06-05 09:04:08 UTC | #2

Windows headers hide MessageBoxA or MessageBoxW behind a MessageBox macro based on build flags (multibyte vs wide character set), either you or someone maintaining master bungled their headers or build setup. 

With Windows some headers aren't safe for use in headers but only in source files as they do crazy stuff like #define min that bungles std::min, etc. Thus the ole #define WIN32_LEAN_AND_MEAN.

-------------------------

zedraken | 2022-06-05 10:46:30 UTC | #3

Thanks for your answer. This confirms that things are messy with those redefinitions of various flavors of MessageBox…
I had a look at the winuser.h file and I just realized that it comes along with the MinGW toolchain installation. I am using MinGW with Codeblocks to build up my executable.

And in this file, I can see various redefinitions like this one…

```
#if WINAPI_FAMILY_PARTITION (WINAPI_PARTITION_DESKTOP)
#define MessageBox __MINGW_NAME_AW(MessageBox)
#define MessageBoxEx __MINGW_NAME_AW(MessageBoxEx)

 WINUSERAPI int WINAPI MessageBoxA(HWND hWnd,LPCSTR lpText,LPCSTR lpCaption,UINT uType);
  WINUSERAPI int WINAPI MessageBoxW(HWND hWnd,LPCWSTR lpText,LPCWSTR lpCaption,UINT uType);
  WINUSERAPI int WINAPI MessageBoxExA(HWND hWnd,LPCSTR lpText,LPCSTR lpCaption,UINT uType,WORD wLanguageId);
  WINUSERAPI int WINAPI MessageBoxExW(HWND hWnd,LPCWSTR lpText,LPCWSTR lpCaption,UINT uType,WORD wLanguageId);
```
Maybe this is the source of the confusion.
So I see two possibilities:
* trying to get rid of these definitions (by maybe applying some #undef statements)
* try with another toolchain (like Visual Studio)

Let’s see how things are going…

Charles

-------------------------

zedraken | 2022-06-05 10:53:12 UTC | #4

Looking at the __MINGW_NAME_AW(…) macro definition, I was able to find it in the _mingw_unicode.h header file as part of the MinGW toolchain.
It contains the following:

```
#if !defined(_INC_CRT_UNICODE_MACROS)
/* _INC_CRT_UNICODE_MACROS defined based on UNICODE flag */

#if defined(UNICODE)
# define _INC_CRT_UNICODE_MACROS 1
# define __MINGW_NAME_AW(func) func##W
# define __MINGW_NAME_AW_EXT(func,ext) func##W##ext
# define __MINGW_NAME_UAW(func) func##_W
# define __MINGW_NAME_UAW_EXT(func,ext) func##_W_##ext
# define __MINGW_STRING_AW(str) L##str	/* same as TEXT() from winnt.h */
# define __MINGW_PROCNAMEEXT_AW "W"
#else
# define _INC_CRT_UNICODE_MACROS 2
# define __MINGW_NAME_AW(func) func##A
# define __MINGW_NAME_AW_EXT(func,ext) func##A##ext
# define __MINGW_NAME_UAW(func) func##_A
# define __MINGW_NAME_UAW_EXT(func,ext) func##_A_##ext
# define __MINGW_STRING_AW(str) str	/* same as TEXT() from winnt.h */
# define __MINGW_PROCNAMEEXT_AW "A"
#endif
```
Then, you are right when saying that the MessageBox is redefined to either MessageBoxA or MessageBoxW depending on the character charset.

Then I understand now why the linker is trying to link with MessageBoxA, which is not part of the Uhro3D engine!

Now that the problem becomes more clear, let’s try to solve it.

Thanks!

-------------------------

JSandusky | 2022-06-06 03:37:45 UTC | #5

I'd start with running header hero (https://bitsquid.blogspot.com/2011/10/caring-by-sharing-header-hero.html) on the file that is erroring, that'll get you a list of headers and you can start narrowing down where something naughty is being done one-by-one (by running header hero again on those headers, down the list - I would expect it to be somewhere in Urho or your code so I'd save crazy headers until the end when it gets down to looking for missing WIN32_LEAN_AND_MEAN etc).

-------------------------

zedraken | 2022-06-11 08:45:09 UTC | #6

Thanks for the tip, I did not know about this tool.
I just focused on following up the header files hierarchy and I was able to solve my issue by doing the following…

In my cpp file where I have the issue, after all include statements, I just add the following code snippet:

> #ifdef MessageBox
> #undef MessageBox
> #warning "MessageBox already defined!"
> #endif

Then everything builds perfectly on Windows now. I just have to check that I did not break the Linux build :slight_smile:

These few lines (the `#warning` is useless here, just for information) have to be placed **after** any other include statement. Otherwise, an include statement can include an Urho3D header that includes itself some other headers that at the end lead to the inclusion of the win32.h file in which the `MessageBox` is redefined.

-------------------------

