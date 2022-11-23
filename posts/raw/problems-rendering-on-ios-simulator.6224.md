btschumy | 2020-06-24 21:06:51 UTC | #1

I and using UrhoSharp to crate a visualization of the Galaxy.  The Urho3D scene is rendering fine on an actual device, but when I use the iPhone simulator on an iMac, there are rendering uses where sections of nodes appear and disappear depending on the camera's orientation.

Is this a known problem?  The compile/run turnaround time on a device is quite a bit longer than on the simulator so I'd like to use the simulator if possible.

If important, my iMac uses a Radeon Pro 560X 4 GB graphics chip.

-------------------------

johnnycable | 2020-06-25 15:33:22 UTC | #2

You probably know the ios simulator and a real device are two completely different beasts. On a mac, the ios env is simulated. You're really running on mac graphic card. That is only intended for simple testing on Apple sdk.
In short, do not expect it to work. Besides, UrhoSharp is abandonware...

-------------------------

btschumy | 2020-06-25 16:32:56 UTC | #3

Yes, I'm well aware that the simulator uses the Mac's graphics card.  That is why I included its specs in my original post.  I have not seen any mention that Urho3D doesn't work on Macs.  There are build scripts for the Mac so I would assume it is designed to work.

I could believe that Urho3D doesn't work in the iOS simulator.  Is that a known issue?

It is distressing to hear you say the UrhoSharp is abandonware.  Microsoft's Xamarin website is still promoting it as *the* way to do 3D graphics in Xamarin.  I'm basing a new, important project on UrhoSharp.

Why do you think the project has been abandoned?  What is one supposed to use for 3D graphics in Xamarin?

Edit:  OK, I did find this: https://forums.xamarin.com/discussion/141631/urhosharp-is-dead-should-we-fork-it
Would anyone care to comment?  I was hoping to create a cross-platform app (iOS, macOS, Android, UWP) that embedded a Urho3D view.  Is this not possible?

-------------------------

adhoc99 | 2020-06-25 18:05:23 UTC | #4

Take a look at [rbfx](https://github.com/rokups/rbfx). It’s a Urho3D fork with extensive C# support.

Their Github repository has a link to their Gitter. Maybe you could ask them if it supports what you need.

-------------------------

