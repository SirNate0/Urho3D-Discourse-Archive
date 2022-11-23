rasteron | 2017-01-02 00:58:50 UTC | #1

Hey guys, it would be nice to add screenshot feature inside editor as already existed in Utilities.as script file.

In EditorUI.as around line 1139 and a 'Screenshots' folder in Bin path ..

[code]
else if (key == KEY_F1)
        console.Toggle();
    else if (key == KEY_F2)
        ToggleRenderingDebug();
    else if (key == KEY_F3)
        TogglePhysicsDebug();
    else if (key == KEY_F4)
        ToggleOctreeDebug();
    else if (key == KEY_F11)
        {
            Image@ screenshot = Image();
            graphics.TakeScreenShot(screenshot);
            // Here we save in the Data folder with date and time appended
            screenshot.SavePNG(fileSystem.programDir + "Screenshots/Screenshot_" +
                time.timeStamp.Replaced(':', '_').Replaced('.', '_').Replaced(' ', '_') + ".png");
        }	

[/code]

cheers.

-------------------------

