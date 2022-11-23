shinyclaw | 2017-05-18 12:16:46 UTC | #1

Hi all. Is it normal to have so much warnings when compiling Urho3D on Win64 platform? In CMake I use Visual Studio 14 2015 Win64 as a generator and when compiling the Urho3D solution under VS 2015 I got output like below. I know that many of these warnings comes from 3rd libraries, but maybe there is a way to make a more clean build?

https://pastebin.com/eQL9Mjaw

Thanks for any info!

-------------------------

Jillinger | 2017-05-18 19:00:31 UTC | #2

Hi @shinyclaw
I had problems when I first started building with Urho3D. I then started sticking Ogre3D dependencies inside the root directory, and from there I had no problem. For android, stick the deps in the include directory of the build tree (builds\android\include), and exclude LUA. At least that's what worked for me.
I had no warnings or errors in my cmake or vs builds for both 32 and 64 bit.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/06c921b1b30a63d788b6c0f90f4b1ea47896a265.jpg" width="690" height="253">

Perhaps you can try getting the Ogre3D dependencies, and see how it goes.
Here is what my directory structure looks like.
    C:\Urho3D\Urho3D-master\deps\

    <Dir>bin
    <Dir>include
    <Dir>lib

    C:\Urho3D\Urho3D-master\deps\bin\

    <Dir>Debug
    <Dir>Release

    C:\Urho3D\Urho3D-master\deps\bin\Debug\

    cg.dll	8530240Bytes
    OIS_d.dll	518656Bytes
    SDL2.dll	730624Bytes

    C:\Urho3D\Urho3D-master\deps\bin\Release\

    cg.dll	8530240Bytes
    OIS.dll	102400Bytes
    SDL2.dll	730624Bytes

    C:\Urho3D\Urho3D-master\deps\include\

    <Dir>Cg
    <Dir>freetype
    <Dir>OIS
    <Dir>rapidjson
    <Dir>SDL2
    <Dir>zzip

    AmdDxExt.h	7476Bytes
    AmdDxExtApi.h	8510Bytes
    AmdDxExtIface.h	6873Bytes
    AmdDxExtQbStereoApi.h	7193Bytes
    AtiDx9Stereo.h	9974Bytes
    FreeImage.h	53522Bytes
    ft2build.h	2185Bytes
    nvapi.h	593676Bytes
    NvApiDriverSettings.h	52543Bytes
    zconf.h	15508Bytes
    zlib.h	87883Bytes

    C:\Urho3D\Urho3D-master\deps\include\Cg\

    cg.h	64961Bytes

    C:\Urho3D\Urho3D-master\deps\include\freetype\

    <Dir>config
    <Dir>internal

    freetype.h	246597Bytes
    ftadvanc.h	10342Bytes
    ftbbox.h	5245Bytes
    ftbdf.h	6749Bytes
    ftbitmap.h	13998Bytes
    ftbzip2.h	4307Bytes
    ftcache.h	60826Bytes
    ftchapters.h	7342Bytes
    ftcid.h	5579Bytes
    fterrdef.h	12179Bytes
    fterrors.h	9467Bytes
    ftgasp.h	4502Bytes
    ftglyph.h	39819Bytes
    ftgxval.h	12600Bytes
    ftgzip.h	4288Bytes
    ftimage.h	82550Bytes
    ftincrem.h	11406Bytes
    ftlcdfil.h	7709Bytes
    ftlist.h	16764Bytes
    ftlzw.h	4256Bytes
    ftmac.h	17098Bytes
    ftmm.h	22712Bytes
    ftmodapi.h	26626Bytes
    ftmoderr.h	7481Bytes
    ftotval.h	7136Bytes
    ftoutln.h	32657Bytes
    ftpfr.h	6289Bytes
    ftrender.h	11719Bytes
    ftsizes.h	9561Bytes
    ftsnames.h	11175Bytes
    ftstroke.h	21069Bytes
    ftsynth.h	3897Bytes
    ftsystem.h	10197Bytes
    fttrigon.h	8443Bytes
    fttypes.h	34976Bytes
    ftwinfnt.h	10403Bytes
    ftxf86.h	4721Bytes
    t1tables.h	27036Bytes
    ttnameid.h	62170Bytes
    tttables.h	40090Bytes
    tttags.h	5002Bytes
    ttunpat.h	2229Bytes

    C:\Urho3D\Urho3D-master\deps\include\freetype\config\

    ftconfig.h	19680Bytes
    ftheader.h	25095Bytes
    ftmodule.h	1399Bytes
    ftoption.h	50672Bytes
    ftstdlib.h	7313Bytes

    C:\Urho3D\Urho3D-master\deps\include\freetype\internal\

    <Dir>services

    autohint.h	14056Bytes
    ftcalc.h	8672Bytes
    ftdebug.h	11376Bytes
    ftdriver.h	22613Bytes
    ftgloadr.h	6498Bytes
    ftmemory.h	14848Bytes
    ftobjs.h	79039Bytes
    ftpic.h	2470Bytes
    ftrfork.h	13977Bytes
    ftserv.h	39808Bytes
    ftstream.h	23253Bytes
    fttrace.h	5401Bytes
    ftvalid.h	7104Bytes
    internal.h	3099Bytes
    psaux.h	35945Bytes
    pshints.h	22395Bytes
    sfnt.h	52000Bytes
    t1types.h	9930Bytes
    tttypes.h	86595Bytes

    C:\Urho3D\Urho3D-master\deps\include\freetype\internal\services\

    svbdf.h	3133Bytes
    svcid.h	3884Bytes
    svgldict.h	3442Bytes
    svgxval.h	2739Bytes
    svkern.h	1783Bytes
    svmm.h	4484Bytes
    svotval.h	1946Bytes
    svpfr.h	2270Bytes
    svpostnm.h	2937Bytes
    svpscmap.h	6871Bytes
    svpsinfo.h	4402Bytes
    svsfnt.h	3380Bytes
    svttcmap.h	4746Bytes
    svtteng.h	1687Bytes
    svttglyf.h	2343Bytes
    svwinfnt.h	1702Bytes
    svxf86nm.h	2047Bytes

    C:\Urho3D\Urho3D-master\deps\include\OIS\

    <Dir>win32

    OIS.h	1367Bytes
    OISConfig.h	2711Bytes
    OISEffect.h	8470Bytes
    OISEvents.h	1315Bytes
    OISException.h	2556Bytes
    OISFactoryCreator.h	2524Bytes
    OISForceFeedback.h	3680Bytes
    OISInputManager.h	6079Bytes
    OISInterface.h	1374Bytes
    OISJoyStick.h	7022Bytes
    OISKeyboard.h	10113Bytes
    OISMouse.h	4193Bytes
    OISMultiTouch.h	5877Bytes
    OISObject.h	2956Bytes
    OISPrereqs.h	6456Bytes

    C:\Urho3D\Urho3D-master\deps\include\OIS\win32\

    Win32ForceFeedback.h	3468Bytes
    Win32InputManager.h	3600Bytes
    Win32JoyStick.h	2808Bytes
    Win32KeyBoard.h	2600Bytes
    Win32Mouse.h	1827Bytes
    Win32Prereqs.h	2003Bytes

    C:\Urho3D\Urho3D-master\deps\include\rapidjson\

    <Dir>error
    <Dir>internal
    <Dir>msinttypes

    allocators.h	10367Bytes
    document.h	92163Bytes
    encodedstream.h	9961Bytes
    encodings.h	23547Bytes
    filereadstream.h	2889Bytes
    filewritestream.h	3111Bytes
    memorybuffer.h	2563Bytes
    memorystream.h	2471Bytes
    pointer.h	56862Bytes
    prettywriter.h	7926Bytes
    rapidjson.h	22543Bytes
    reader.h	62467Bytes
    stringbuffer.h	3167Bytes
    writer.h	14238Bytes

    C:\Urho3D\Urho3D-master\deps\include\rapidjson\error\

    en.h	3677Bytes
    error.h	5704Bytes

    C:\Urho3D\Urho3D-master\deps\include\rapidjson\internal\

    biginteger.h	9128Bytes
    diyfp.h	11358Bytes
    dtoa.h	6867Bytes
    ieee754.h	2931Bytes
    itoa.h	10306Bytes
    meta.h	6753Bytes
    pow10.h	3650Bytes
    stack.h	6323Bytes
    strfunc.h	1448Bytes
    strtod.h	8616Bytes
    swap.h	1322Bytes

    C:\Urho3D\Urho3D-master\deps\include\rapidjson\msinttypes\

    inttypes.h	8372Bytes
    stdint.h	9386Bytes

    C:\Urho3D\Urho3D-master\deps\include\SDL2\

    begin_code.h	4432Bytes
    close_code.h	1417Bytes
    SDL.h	4101Bytes
    SDL_assert.h	10860Bytes
    SDL_atomic.h	9653Bytes
    SDL_audio.h	28541Bytes
    SDL_bits.h	2527Bytes
    SDL_blendmode.h	2252Bytes
    SDL_clipboard.h	1966Bytes
    SDL_config.h	13487Bytes
    SDL_config_android.h	3861Bytes
    SDL_config_iphoneos.h	4187Bytes
    SDL_config_macosx.h	5397Bytes
    SDL_config_minimal.h	2619Bytes
    SDL_config_pandora.h	3275Bytes
    SDL_config_psp.h	3736Bytes
    SDL_config_windows.h	5778Bytes
    SDL_config_winrt.h	5950Bytes
    SDL_config_wiz.h	3145Bytes
    SDL_copying.h	939Bytes
    SDL_cpuinfo.h	4360Bytes
    SDL_egl.h	73519Bytes
    SDL_endian.h	5944Bytes
    SDL_error.h	2271Bytes
    SDL_events.h	28064Bytes
    SDL_filesystem.h	5255Bytes
    SDL_gamecontroller.h	12233Bytes
    SDL_gesture.h	2157Bytes
    SDL_haptic.h	38771Bytes
    SDL_hints.h	36894Bytes
    SDL_joystick.h	12075Bytes
    SDL_keyboard.h	6437Bytes
    SDL_keycode.h	14847Bytes
    SDL_loadso.h	2866Bytes
    SDL_log.h	6483Bytes
    SDL_main.h	4595Bytes
    SDL_messagebox.h	4611Bytes
    SDL_mouse.h	10922Bytes
    SDL_mutex.h	6665Bytes
    SDL_name.h	1155Bytes
    SDL_opengl.h	82372Bytes
    SDL_opengl_glext.h	731497Bytes
    SDL_opengles.h	1254Bytes
    SDL_opengles2.h	1552Bytes
    SDL_opengles2_gl2.h	31876Bytes
    SDL_opengles2_gl2ext.h	98695Bytes
    SDL_opengles2_gl2platform.h	913Bytes
    SDL_opengles2_khrplatform.h	10022Bytes
    SDL_pixels.h	17031Bytes
    SDL_platform.h	4917Bytes
    SDL_power.h	2463Bytes
    SDL_quit.h	2106Bytes
    SDL_rect.h	4445Bytes
    SDL_render.h	34464Bytes
    SDL_revision.h	71Bytes
    SDL_rwops.h	7242Bytes
    SDL_scancode.h	14946Bytes
    SDL_shape.h	5688Bytes
    SDL_stdinc.h	18399Bytes
    SDL_surface.h	19156Bytes
    SDL_system.h	7603Bytes
    SDL_syswm.h	8915Bytes
    SDL_test.h	1971Bytes
    SDL_test_assert.h	3243Bytes
    SDL_test_common.h	4906Bytes
    SDL_test_compare.h	2163Bytes
    SDL_test_crc32.h	3385Bytes
    SDL_test_font.h	2336Bytes
    SDL_test_fuzzer.h	13122Bytes
    SDL_test_harness.h	4612Bytes
    SDL_test_images.h	2215Bytes
    SDL_test_log.h	1954Bytes
    SDL_test_md5.h	4630Bytes
    SDL_test_random.h	3156Bytes
    SDL_thread.h	10114Bytes
    SDL_timer.h	3454Bytes
    SDL_touch.h	2335Bytes
    SDL_types.h	1031Bytes
    SDL_version.h	5161Bytes
    SDL_video.h	43855Bytes

    C:\Urho3D\Urho3D-master\deps\include\zzip\

    _config.h	6799Bytes
    _msvc.h	6343Bytes
    conf.h	6311Bytes
    plugin.h	3285Bytes
    types.h	2164Bytes
    zzip.h	8050Bytes

    C:\Urho3D\Urho3D-master\deps\lib\

    <Dir>Debug
    <Dir>Release

    SDL2.lib	2031142Bytes
    SDL2main.lib	4392Bytes

    C:\Urho3D\Urho3D-master\deps\lib\Debug\

    cg.lib	84788Bytes
    FreeImage_d.lib	45129154Bytes
    freetype_d.lib	2309896Bytes
    nvapi.lib	477236Bytes
    OIS_d.lib	63784Bytes
    zlib_d.lib	244276Bytes
    zziplib_d.lib	199042Bytes

    C:\Urho3D\Urho3D-master\deps\lib\Release\

    cg.lib	84788Bytes
    FreeImage.lib	17698672Bytes
    freetype.lib	799234Bytes
    nvapi.lib	477236Bytes
    OIS.lib	63368Bytes
    zlib.lib	107662Bytes
    zziplib.lib	66520Bytes

If that doesn't work, then it might be a missing link that need to be set in your environment variables.
Hope this helps.

-------------------------

weitjong | 2017-05-19 09:51:40 UTC | #3

First of all Urho3D build system only uses the third-party dependency libs that are found in its own source tree. It doesn't depend on other project's dependencies.

We have only lightly modified the 3rd-party source to fix critical bugs or to make them play nice with Urho in order to minimize the delta change and make our life easier when we need to upgrade the libs from their upstream repo. We don't alter them just to suppress the warnings, however. You can pass in the compiler flags to suppress the warnings if they bother you.

-------------------------

