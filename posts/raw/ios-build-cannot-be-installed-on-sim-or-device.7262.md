KatekovAnton | 2022-05-12 15:36:52 UTC | #1

Hi. Im trying to build an rbfx app for the ios but facing a weird problem. Project compiles successfully but installing it to sumulator or device failing with a following errror:

![Screen Shot 2022-05-12 at 21.15.11|505x500](upload://uTA77iJWFxO9MscUUuIk3QMwJCB.png)

I build it generating xcode project with a following script

```
	mkdir -p buildios && \
	cd buildios && \
	cmake -G Xcode \
	-T buildsystem=12 \
	-DCMAKE_TOOLCHAIN_FILE=Vendors/rbfx/cmake/Toolchains/IOS.cmake \
	-DENABLE_BITCODE=OFF \
	-DPLATFORM=OS64COMBINED \
	-DDEPLOYMENT_TARGET=11.0 \
	-DURHO3D_COMPUTE=OFF \
	-DURHO3D_GRAPHICS_API=GLES2 \
	-DBUILD_SHARED_LIBS=ON \
	-DURHO3D_GLOW=OFF \
	-DURHO3D_FEATURES="SYSTEMUI" \
	-DURHO3D_PROFILING=OFF \
	-DURHO3D_PLAYER=OFF \
	-DURHO3D_EXTRAS=OFF \
	-DURHO3D_TOOLS=OFF \
	-DURHO3D_RMLUI=ON \
	..
```


```
set_target_properties(${PROJECT_NAME} PROPERTIES 

            MACOSX_BUNDLE_INFO_PLIST "${CMAKE_CURRENT_SOURCE_DIR}/Platform/iOS/Info.plist"

            MACOSX_BUNDLE_BUNDLE_VERSION "1.0.0"
            XCODE_ATTRIBUTE_INFOPLIST_OUTPUT_FORMAT "same-as-input"
            XCODE_ATTRIBUTE_OTHER_CODE_SIGN_FLAGS "--deep"
            
            XCODE_ATTRIBUTE_CURRENT_PROJECT_VERSION "1.0.0"
            XCODE_ATTRIBUTE_MARKETING_VERSION "1.0.0"
            XCODE_ATTRIBUTE_ONLY_ACTIVE_ARCH[variant=Debug] YES
            XCODE_ATTRIBUTE_ONLY_ACTIVE_ARCH[variant=Release] NO
            XCODE_ATTRIBUTE_ONLY_ACTIVE_ARCH[variant=RelWithDebInfo] NO
            XCODE_ATTRIBUTE_ONLY_ACTIVE_ARCH[variant=MinSizeRel] NO
            XCODE_ATTRIBUTE_CODE_SIGN_ENTITLEMENTS "../midkindtales/Platform/iOS/Tales.entitlements"
            
            XCODE_ATTRIBUTE_DEVELOPMENT_TEAM "1234"
            XCODE_ATTRIBUTE_CLANG_ENABLE_OBJC_ARC "YES"
            XCODE_ATTRIBUTE_CODE_SIGN_STYLE "Automatic"
            XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY "Apple Development"
        )
```

I can see that value exists in the output IPA
```
<key>CFBundleVersion</key>
	<string>1.0.0</string>
```

but installation still fails. I was even trying to replace Info.plist with the one from a valid package but still no results. So I think problem is not in the info plist.

Do you have any advises? Thank you.

-------------------------

KatekovAnton | 2022-05-12 16:13:22 UTC | #2

It appeared that xcode cannot handle a folder called Resources on the root level. Renaming it to Assets fixed the problem

-------------------------

