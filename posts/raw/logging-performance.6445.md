vmost | 2020-10-18 13:40:28 UTC | #1

I recently started adding Urho3D logging to my projects, and noticed a significant overhead from log levels that weren't even active (in a test case that was pounding away at something). [EDIT: I checked and there is a ton of overhead just calling `Urho3D::ToString()` to convert a formatted C-style log message to an `Urho3D::String`... which never gets used.]

Basically the compiler isn't getting rid of log lines that don't do anything. I'm wondering if it would make more sense to define log levels in the build system and `#ifdef` away all the unneeded log lines in `Urho3D/IO/Log.h`. Or maybe I am misusing logging... Interested in anyone's thoughts.

-------------------------

SirNate0 | 2020-10-18 15:10:55 UTC | #2

I'd certainly be fine with that approach, but I'd prefer it as a `#define MAX_LOG_LEVEL`, while still allowing runtime setting of the log level below that. That way apps can have a verbose/debug setting that the user can enable, but you could still achieve what you want (the compiler removing all the extra calls).

Another approach might be too see about making String constexpr, but I'm no expert on that.

-------------------------

Eugene | 2020-10-18 15:38:45 UTC | #3

[quote="vmost, post:1, topic:6445"]
’m wondering if it would make more sense to define log levels in the build system and `#ifdef` away all the unneeded log lines
[/quote]
Do you you mean that you want per-level defines instead of global?
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/IO/Log.h#L133-L159

-------------------------

vmost | 2020-10-18 15:42:30 UTC | #4

@Eugene they are only removed if logging is completely disabled. I am looking for a more fine-tuned approach that only executes log statements when they are actually used.

@SirNate0  `ToString()` is only executed for formatted log messages, which are evaluated at run time.

-------------------------

weitjong | 2020-10-19 04:18:38 UTC | #5

In Java/Kotlin with Log4J pattern, computationally expensive string construction for the logging should be guarded inside the `isXXXEnabled()`. e.g.:

    if (isDebugEnabled()) {
        // Construct the expensive string here
        val expensiveString = .....
        logger.debug(expensiveString)
    }

Although Urho3D API does not provide such guard methods, it does provide the `GetLevel()` method to do the equivalent.

-------------------------

vmost | 2020-10-19 04:28:24 UTC | #6

The problem with `GetLevel()` is you'd need to add a static `GetLevelStatic()` for accessing the logging singleton, which implies a mandatory indirection `logInstance->GetLevel()`, if you want to do something like
```
#define URHO3D_LOGTRACEF(format, ...) GetLevelStatic() <= LOG_TRACE ? Write(LOG_TRACE, ToString(...)) : (void)0
```

@weitjong I am trying to add a `URHO3D_MIN_LOG_LEVEL` input to the build system for logging, but can't quite get it to work. Here are relevant parts of the diff

```
diff --git a/CMake/Modules/UrhoCommon.cmake b/CMake/Modules/UrhoCommon.cmake
index 4c1ac5989..7ec1aa0df 100644
--- a/CMake/Modules/UrhoCommon.cmake
+++ b/CMake/Modules/UrhoCommon.cmake
@@ -250,6 +250,8 @@ cmake_dependent_option (URHO3D_PACKAGING "Enable resources packaging support" FA
 option (URHO3D_PROFILING "Enable profiling support" TRUE)
 # Enable logging by default. If disabled, LOGXXXX macros become no-ops and the Log subsystem is not instantiated.
 option (URHO3D_LOGGING "Enable logging support" TRUE)
+# Enable all log levels by default. Log levels lower than the min log level are no-ops. Can be set to any log level in the range [-1, 5] where any level >= 5 is no logging and any level <= 0 is 'all logging'. Log level -1 forces all log messages to be 'raw'.
+option (URHO3D_MIN_LOG_LEVEL "Set minimum log level from [-1, 5]" -1)
 # Enable threading by default, except for Emscripten because its thread support is yet experimental                                                                    
 if (NOT WEB)                                                                                                                                                           
     set (THREADING_DEFAULT TRUE)                                                                                                                                       
@@ -391,6 +393,7 @@ if (URHO3D_CLANG_TOOLS)                                                                                                                             
             URHO3D_IK                                                                                                                                                  
             URHO3D_LOGGING                                                                                                                                             
             URHO3D_LUA                                                                                                                                                 
+            URHO3D_MIN_LOG_LEVEL                                                                                                                                       
             URHO3D_NAVIGATION                                                                                                                                          
             URHO3D_NETWORK                                                                                                                                             
             URHO3D_PHYSICS                                                                                                                                             
@@ -440,6 +443,7 @@ foreach (OPT                                                                                                                                        
         URHO3D_IK                                                                                                                                                      
         URHO3D_LOGGING                                                                                                                                                 
         URHO3D_LUA                                                                                                                                                     
+        URHO3D_MIN_LOG_LEVEL                                                                                                                                           
         URHO3D_MINIDUMPS                                                                                                                                               
         URHO3D_NAVIGATION                                                                                                                                              
         URHO3D_NETWORK    
diff --git a/script/.build-options b/script/.build-options                                                                                                              
index 0b56fe363..b5059e962 100644                                                                                                                                       
--- a/script/.build-options                                                                                                                                             
+++ b/script/.build-options                                                                                                                                             
@@ -37,6 +37,7 @@ URHO3D_HASH_DEBUG                                                                                                                                     
 URHO3D_PACKAGING                                                                                                                                                       
 URHO3D_PROFILING                                                                                                                                                       
 URHO3D_LOGGING                                                                                                                                                         
+URHO3D_MIN_LOG_LEVEL                                                                                                                                                   
 URHO3D_THREADING                                                                                                                                                       
 URHO3D_TESTING                                                                                                                                                         
 URHO3D_TEST_TIMEOUT                                                                                                                                                    
diff --git a/script/.env-file b/script/.env-file                                                                                                                        
index b076050bb..1c6cf0fc3 100644                                                                                                                                       
--- a/script/.env-file                                                                                                                                                  
+++ b/script/.env-file                                                                                                                                                  
@@ -120,6 +120,7 @@ URHO3D_LUAJIT                                                                                                                                       
 URHO3D_LUAJIT_AMALG                                                                                                                                                    
 URHO3D_LUA_RAW_SCRIPT_LOADER                                                                                                                                           
 URHO3D_MACOSX_BUNDLE                                                                                                                                                   
+URHO3D_MIN_LOG_LEVEL                                                                                                                                                   
 URHO3D_MINIDUMPS                                                                                                                                                       
 URHO3D_MMX                                                                                                                                                             
 URHO3D_NAVIGATION  
```

-------------------------

weitjong | 2020-10-19 04:36:54 UTC | #7

Not all strings are expensive to construct. Most are just constant which cost nothing during runtime. So usually I peppered the check in my code at the place where I need it where the logger object is already known.

Back to your question. You basically wants to bake the level when building the engine itself. I don’t think that is the right direction. But i won’t stop you. You have to be more explicit on what was the errors you encountered if you need my help.

-------------------------

vmost | 2020-10-19 04:40:54 UTC | #8

I want to bake the level when building a project, not the engine. For example I have two build scripts with `-DURHO3D_PROFILING=ON/OFF` for debug/release builds of my project. Don't need to rebuild the library. I could be misunderstanding things though. Yes, I probably am... hmm

-------------------------

vmost | 2020-10-19 06:28:02 UTC | #9

Made a [PR](https://github.com/urho3d/Urho3D/pull/2685) for my solution

-------------------------

