nickwebha | 2021-02-16 19:26:42 UTC | #1

I need my application to work where Urho3D networking does not (the web). I built a websocket client and when I try to include both Urho3D and OpenSSL I get:
> In file included from /usr/include/openssl/engine.h:24,
>                  from ../include/boost/asio/ssl/detail/openssl_types.hpp:26,
>                  from ../include/boost/asio/ssl/context_base.hpp:19,
>                  from ../include/boost/asio/ssl/context.hpp:23,
>                  from ../include/boost/asio/ssl/stream.hpp:26,
>                  from ../include/boost/beast/websocket/ssl.hpp:16,
>                  from ../include/boost/beast/ssl/ssl_stream.hpp:16,
>                  from ../include/boost/beast/ssl.hpp:15,
>                  from include/websocket.hpp:111,
>                  from login.hpp:10,
>                  from main.cpp:1:
> **/usr/include/openssl/ui.h:42:1: error: reference to ‘UI’ is ambiguous**
>    42 | UI *UI_new(void);
> **/usr/local/include/Urho3D/UI/UI.h:60:18: note: candidates are: ‘class Urho3D::UI’**
>    60 | class URHO3D_API UI : public Object
> In file included from /usr/include/openssl/crypto.h:25,
>                  from /usr/include/openssl/bio.h:20,
>                  from /usr/include/openssl/conf.h:13,
>                  from ../include/boost/asio/ssl/detail/openssl_types.hpp:23,
>                  from ../include/boost/asio/ssl/context_base.hpp:19,
>                  from ../include/boost/asio/ssl/context.hpp:23,
>                  from ../include/boost/asio/ssl/stream.hpp:26,
>                  from ../include/boost/beast/websocket/ssl.hpp:16,
>                  from ../include/boost/beast/ssl/ssl_stream.hpp:16,
>                  from ../include/boost/beast/ssl.hpp:15,
>                  from include/websocket.hpp:111,
>                  from login.hpp:10,
>                  from main.cpp:1:
> **/usr/include/openssl/ossl_typ.h:144:22: note:                 ‘typedef struct ui_st UI’**
>   144 | typedef struct ui_st UI;
> In file included from /usr/include/openssl/engine.h:24,
>                  from ../include/boost/asio/ssl/detail/openssl_types.hpp:26,
>                  from ../include/boost/asio/ssl/context_base.hpp:19,
>                  from ../include/boost/asio/ssl/context.hpp:23,
>                  from ../include/boost/asio/ssl/stream.hpp:26,
>                  from ../include/boost/beast/websocket/ssl.hpp:16,
>                  from ../include/boost/beast/ssl/ssl_stream.hpp:16,
>                  from ../include/boost/beast/ssl.hpp:15,
>                  from include/websocket.hpp:111,
>                  from login.hpp:10,
>                  from main.cpp:1:

Note `reference to ‘UI’ is ambiguous` and the two suggested candidates in the above (one from Urho3D, and other from OpenSSL). I have bolded the relevant lines to make it slightly easier to read.

I am not polluting namespaces (not using `using` anywhere).

Is this something we were already aware of? How do I get around it if both Urho3D and OpenSSL want UI in the public namespace?

I am running G++ v9.3.0 from the Ubuntu 20.04 repos.

-------------------------

1vanK | 2021-02-16 19:29:30 UTC | #2

I have never used this, but maybe this is what you need?  https://github.com/urho3d/Urho3D/blob/master/Source/Samples/43_HttpRequestDemo/HttpRequestDemo.cpp#L88-L92

-------------------------

S.L.C | 2021-02-16 19:56:41 UTC | #3

I don't really understand why the `UI` inside the `Urho3D` namespace is conflicting with `UI` from a C(ish) global scope.

As long as the header which contains `typedef struct ui_st UI` was included outside of `Urho3D` namespace. Both of them should be accessible without conflict based on current scope.

I.e. if you're inside `Urho3D` namespace then you access `Urho3D::UI` simply as `UI` and the one from OpenSSL as `::UI`. Note the `::` which implies you want the one from the global scope.

And if you are in the global scope then you access `UI` from `Urho3D` namespace as `Urho3D::UI` and `UI` from OpenSSL simply as `UI`.

The only time this becomes an issue is when a macro is used that doesn't take that into consideration. In which case the macro must be adjusted to account for the possible conflict.

First make sure the OpenSSL headers were not included inside the `Urho3D` namespace. Like:
```cpp
namespace Urho3D {
#include <someheader.h>
}
```

Second. Make sure you are not importing the `Urho3D` namespace into your global scope. Like:
```cpp
namespace Urho3D {
}
using namespace Urho3D;
```
Rather, import what you need:
```cpp
namespace Urho3D {
}
using Urho3D::TypeYouNeed;
using Urho3D::FunctionYouNeed;
```

Once you make sure those identifiers don't exist in the same scope at the same time. You should have no issues addressing one or the other.

Anyway, I haven't really tried to use OpenSSL with Urho at the same time. So I have no clue about your current situation.

-------------------------

nickwebha | 2021-02-16 20:10:21 UTC | #4

This is the strange part.

I am not using `using namespace Urho3D;` (grep'ed to be extra sure). Nor is my code using any namespaces at all yet (this is still the start of the project so I have not gotten that far yet).

They just conflict. I am not really sure how to further investigate this.

-------------------------

nickwebha | 2021-02-16 23:16:14 UTC | #5

Update.

By changing the order in which the headers were included (Urho3D last) fixed the issue.

No idea what that is about.

-------------------------

1vanK | 2021-02-17 00:52:19 UTC | #6

Did you include DebugNew.h?

-------------------------

nickwebha | 2021-02-17 16:11:40 UTC | #7

Not really sure what that is besides what I can take away from the name. I will look into it.

Thanks.

**Edit**
That seems to be for MSVC only. I am on Linux using GCC. I appreciate the help, though.

-------------------------

nickwebha | 2021-03-19 00:41:04 UTC | #8

This issue has cropped up again.

I have a little demo I built in Urho3D. I needed to make HTTP requests so I included Boost (1.75.0). It seems Urho3D is spilling out of its namespace and into the global scope.

For example, OpenSSL complains like this
>     In file included from /usr/include/openssl/engine.h:24,
>                      from /home/nick/boost_1_75_0/boost/asio/ssl/detail/openssl_types.hpp:26,
>                      from /home/nick/boost_1_75_0/boost/asio/ssl/context_base.hpp:19,
>                      from /home/nick/boost_1_75_0/boost/asio/ssl/context.hpp:23,
>                      from /home/nick/boost_1_75_0/boost/asio/ssl/stream.hpp:26,
>                      from /home/nick/boost_1_75_0/boost/beast/websocket/ssl.hpp:16,
>                      from /home/nick/boost_1_75_0/boost/beast/ssl/ssl_stream.hpp:16,
>                      from /home/nick/boost_1_75_0/boost/beast/ssl.hpp:15,
>                      from include/httpClient.hpp:26,
>                      from source/world.cpp:3:
>     /usr/include/openssl/ui.h:42:1: error: reference to ‘UI’ is ambiguous
>        42 | UI *UI_new(void);
>           | ^~
(plus a lot more).

Since OpenSSL is all C Urho3D would need to be the one to stay inside its namespace. It is even allowing me to do things like `SharedPtr< Node > cameraNode_;` instead of requiring `Urho3d::SharedPtr< Urho3d::Node > cameraNode_;`, etc.

Moving around the order in which the files are included does not seem to be fixing it now.

**Edit**
`Urho3DAll.h` has `using namespace Urho3D;` at the bottom of it! D'oh.

-------------------------

