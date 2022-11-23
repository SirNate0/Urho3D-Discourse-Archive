devhang | 2019-12-26 19:36:29 UTC | #1

Hello, I am start to experiment with Urho3D on Android, I have already built the system and install into  mobile device successfully, I follow the launcher example to using Urho3DPlayer load the script from assets folder, but is it possible to load the script from app's internal storage (eg. /data/data/com.github.urho3d.launcher) or sdcard storage (eg. /mnt/sdcard)?

-------------------------

devhang | 2019-12-26 19:36:37 UTC | #2

After some testing, I find out I can set the resources prefix path to sdcard or internal storage to achieve the goal.
from LauncherActivity.kt
Urho3DPlayer:Scripts/$argument:-pp:/mnt/sdcard/urho3d/bin
Thank for the nice engine.

-------------------------

Modanung | 2019-12-26 19:37:36 UTC | #3

Good to hear you solved your issue. Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

