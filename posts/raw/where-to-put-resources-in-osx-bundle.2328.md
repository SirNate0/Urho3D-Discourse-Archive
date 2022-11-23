godan | 2017-01-02 01:14:47 UTC | #1

When I build my app with the Urho build system with MACOS_BUNDLE, I get the following PList:

[code]
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDevelopmentRegion</key>
    <string>en</string>
    <key>CFBundleExecutable</key>
    <string>IogramEditor</string>
    <key>CFBundleGetInfoString</key>
    <string></string>
    <key>CFBundleIconFile</key>
    <string>ioeditor.icns</string>
    <key>CFBundleIdentifier</key>
    <string></string>
    <key>CFBundleInfoDictionaryVersion</key>
    <string>6.0</string>
    <key>CFBundleLongVersionString</key>
    <string></string>
    <key>CFBundleName</key>
    <string>IogramEditor</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleShortVersionString</key>
    <string></string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>CFBundleVersion</key>
    <string></string>
    <key>LSMinimumSystemVersion</key>
    <string>$(MACOSX_DEPLOYMENT_TARGET)</string>
    <key>CSResourcesFileMapped</key>
    <true/>
    <key>LSRequiresCarbon</key>
    <true/>
    <key>NSHumanReadableCopyright</key>
    <string></string>
    <key>LSEnvironment</key>
    <dict>
        <key>URHO3D_PREFIX_PATH</key>
        <string>../Resources</string>
    </dict>
</dict>
</plist>

[/code]

The last line seems to say something about the preferred resource directions. I assume this points to Contents>Resources. However, when I drop the Data/CoreData folders in there - I get the "No resource found error".

Has anyone encountered this before?

-------------------------

